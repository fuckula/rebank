# How the game loads sound mods — decisions

Scope: why a mod bank under `sound/mod/` can be ignored. Static analysis of
`win64/aces.exe` (client 2026-11-23, sha256 `4540a9cc…`), Hex-Rays output in
`Temp/ida_decomp/out/*.c` (scratch, not committed). The rules come from the
binary, not from the wiki; the wiki only says "put banks in sound/mod and set
enable_mod". FMOD itself (core + studio) is linked statically into `aces.exe`;
the `win64/fmod*.dll` files are an older 1.10 build the game does not use for
banks (loading a 2.02 bank through them gives FMOD_ERR_VERSION).

Decompiling this LTO build: Hex-Rays fails with `call analysis failed` on any
function whose direct callees are not typed. Defining every call target as a
function (`.pdata` bounds) and giving it a `__int64 __fastcall f(a0..a3)`
prototype (`, ...` for the printf-like helpers that spill XMM registers in the
prologue) makes it decompile. Without that, `decompile()` returns `None`.

## Gate 1: `aces_early_init_sound` (`0x1415c0820`)

1. `config.blk` → `sound{ enable_mod:b=yes }` → global `g_mod_on`
   (`0x147bba7bc`). Without it nothing below runs.
2. `forceDisableMods:b` in `sound_studio.blk` (shipped false): true →
   `Sound.MOD force disabled`, mod off.
3. `checkModsIntegrity:b` (absent → false): true → every `masterBanks` entry
   must exist in `sound/mod/`; false → at least one of
   `sound/mod/masterbank*.bank` (`0x1415bfc30`, format `sound/mod/%s.bank`).
4. `banks{ folder:"sound" extension:".bank" presets{ master{ … } } }` —
   for **every** bank block without `optional:b=true` the file
   `sound/mod/<name><extension>` must exist (`0x1415bf1f0`, format
   `sound/mod/%s%s`, decompiled verbatim). The first missing one logs
   `Sound.MOD disabled: modded bank is missing: <path>` and the whole mod is
   off (reason 1). In the shipped `sound_studio.blk` that is **47 banks**
   (all `aircraft_*`, `tanks_*`, `ships_*`, `masterbank*` and their
   `.assets`); only `dialogs*`, `crew_dialogs_common*`, `football*`,
   `event*` are optional.
5. FNV-1a 64 over the first 4 MiB of `sound/mod/masterbank.bank` must not be
   in `cache/prohibitedMods` (`0x1415bf8f0` → `0x1415bedf0`; the list file
   `0x1415bfd80` is 8 × u64). That list is written by the game itself
   (`0x1415beb60`, "added masterbank … to prohibitedMods list") when a
   masterbank fails a later check (`0x1415c4c80`, gated by `0x144660bc0`); a
   vanilla `masterbank.bank` is never in it. A match is reason 2.
6. `blockModsOnAssert:b=true`: an assert while loading the mod banks turns
   the mod off.

Consequence for a partial mod: one patched bank in `sound/mod/<dir>/` is
**not** a working mod. The folder must hold the full set; the usual way is
to copy every required vanilla bank and replace only the patched one.

## Gate 2: `load_banks` (`0x1437f99c0`, called from gate 1 at `0x1415c1af1`)

Gate 1 writes its verdict into `banks.enableMod` of the blk tree and calls
`load_banks`, the function that really reads the files:

1. `banks.enableMod` (from gate 1) and `banks.mod.allow` (default true; the
   `mod` block is absent in the shipped blk). Either false →
   `[SNDSYS] bank mods disabled`, vanilla banks only.
2. For every name in `masterBanks` the file `sound/mod/<name><ext>` is
   hashed: size + FNV-1a 64 over the whole file, logged as
   `[SNDSYS] modded #%d '%s' size=%d hash=%llu`.
3. Each (size, hash) is compared with a triple passed in by the caller
   (server-provided list of banned masterbanks). A match logs
   `[SNDSYS] Bank mod '%s' is prohibited … label='%s'` and sets
   `bank mods disallowed: prohibited banks found`; otherwise
   `[SNDSYS] bank mods enabled`.
4. Only then are the banks from `sound/mod/<dir>/` loaded instead of
   `sound/`, logged as `[SOUND] Mod is used, modded banks:` /
   `[SOUND] bank %s`.

A vanilla `masterbank.bank` never matches the banned triples, so step 3 is
only a risk for mods that ship a modified masterbank.

## Other facts

- Mod files are looked up by bank name only; the sub-folder name under
  `sound/mod/` is free (single level).
- `sound/mod/tank_sound_overloads.blk` and `ship_sound_overloads.blk` are an
  unrelated optional hook (`0x14046fb40`, `0x1407e3270`) that remaps tank and
  ship preset names; absent in vanilla.
- `.game_logs/*.clog` are encrypted (uniform byte entropy, no header); the
  `Sound.MOD …` and `[SNDSYS]` lines cannot be read without the game's cipher.
