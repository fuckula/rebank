# War Thunder sound modding guide

Recipes that work with the current game build, each with the failure it
prevents. Everything below was verified against the Sky Odyssey client
(`aces.exe` sha256 `4540a9cc…`, FMOD Studio 2.02.22): the game code was
read with IDA, the banks were parsed, the Studio build was run.

`$WT` is the War Thunder folder (`…/War Thunder`). All commands are run
from the ReBank checkout.

## 1. The mod folder must be complete

**Rule.** `sound/mod/<any folder>/` must contain every bank of
`config/sound_studio.blk` (`banks → presets → master`) that has no
`optional:b=true` — **47 banks** in this build: `masterbank`,
`masterbank.strings`, `masterbank.assets`, every `aircraft_*`, `tanks_*`,
`ships_*` bank and its `.assets` pair. Only `dialogs*`,
`crew_dialogs_common*`, `football*`, `event*`, `event_tgw*` are optional.

**Failure it prevents.** The first missing bank switches the **whole mod**
off: the game logs `Sound.MOD disabled: modded bank is missing: …` and
plays vanilla sound everywhere. Nothing in the UI tells you; the log
(`.game_logs/*.clog`) is encrypted.

**Recipe.**

1. Create the folder and copy the untouched vanilla banks into it:
   ```sh
   mkdir -p "$WT/sound/mod/my_mod"
   cp "$WT/sound/"*.bank "$WT/sound/mod/my_mod/"
   ```
2. Replace only the banks you rebuilt (both halves, see §3).
3. Enable mods in `$WT/config.blk`:
   ```
   sound{
     fmod_sound_enable:b=yes
     enable_mod:b=yes
   }
   ```
4. Verify before sharing:
   ```sh
   rebank check "$WT/sound/mod/my_mod" --game "$WT/sound" \
       --studio-blk /tmp/wt_aces/aces.vromfs.bin_u/config/sound_studio.blk
   ```
   (`/tmp/wt_aces` is `wt_ext_cli unpack_vromf -i "$WT/aces.vromfs.bin" -o /tmp/wt_aces --format BlkText`.)
   Without `--studio-blk` the check still warns about a metadata bank
   whose `.assets.bank` exists in the game but not in the mod.

**Do not** ship a folder with a single changed bank — that is the
number-one cause of "the mod is ignored".

## 2. Keep the identity of everything

**Rule.** Event names, event paths, bank names, the mixer bus tree and
the parameters the game drives (`track`, `volume`, `on_shot`, …) must stay
exactly as in the game. Change the *content* of events, not their
identity.

**Failure it prevents.** The game starts events by path (`event:/aircraft/gui/alarm_radar_an_alr_56`) and sets parameters by name; a renamed event or a missing parameter is silently ignored. The reference project's
Readme says the same.

**Recipe.** Start from Gaijin's
[`fmod_studio_warthunder_for_modders`](https://github.com/GaijinEntertainment/fmod_studio_warthunder_for_modders)
(FMOD Studio **2.02.22** — `rebank init my-mod` sets up a workspace) or
from the vanilla bank itself with `rebank … --fspro` when the event is not
in the reference project (all 24 RWR `alarm_radar_*` tones, localised
dialogs, `infantry_*`, `football`). `rebank check` fails on renamed or
dropped events.

## 3. Banks come in split pairs

**Rule.** Every bank is built as two files: `<name>.bank` (metadata:
events, instruments, parameter sheets) and `<name>.assets.bank` (sample
data). The master bank also produces `masterbank.strings.bank` (paths).
This is FMOD Studio's "Build metadata and assets to separate banks"
setting; the official project has it on, and the game ships this layout.

**Failure it prevents.** A `.bank` without its `.assets.bank` leaves every
event of that bank silent; a `.bank` from one build with an
`.assets.bank` from another build resolves **no samples at all** — Studio
assigns new waveform GUIDs on every build (verified: 0 GUIDs shared
between a Studio build of the vanilla project and the vanilla bank).

**Recipe.** Build in Studio (File → Build), then copy **both** files of
every bank you changed from `Build/sound/` (or your build output folder)
into the mod folder, next to the untouched vanilla banks. Never mix a
Studio-built `assets.bank` with the vanilla metadata bank.

## 4. Rebuilding a bank from the game with ReBank

**Recipe.**

```sh
rebank "$WT/sound/aircraft_gui.bank" -a "$WT/sound/aircraft_gui.assets.bank" \
    --fspro -o my_project --apply          # project from the vanilla pair
```

Open `my_project/fspro/aircraft_gui.fspro` in FMOD Studio 2.02.22, edit
the events, Build. The generated project keeps event GUIDs, paths, game
parameters and the original samples; mixer buses are flat (master bus), so
for events with sends to mixer buses (`_headphones` returns and the like)
prefer the official project.

**Checks that must pass before you ship the result:**

```sh
python smoke_test.py Build/sound/aircraft_gui.bank "$WT/sound"   # PASS, 0 dangling refs
rebank check Build/sound --game "$WT/sound"
```

**Known Studio behaviour, not an error:** `SingleSound` instruments on
parameter sheets are serialised by Studio as one-entry `MultiSound`
(537/167 instead of 475/35 in the vanilla `aircraft_gui`); playback is
identical.

## 5. Changing samples without touching the metadata bank (assets-only patch)

**When.** You want the vanilla event bank untouched and only some samples
replaced — for example F-15/Eurofighter RWR tones replaced by the F-16
ones. Studio cannot do this (new GUIDs, §3); the samples inside the
vanilla `<name>.assets.bank` are replaced in place.

**Rule.** The sample table (`WAVS`: waveform GUID → sample index) and every
header field of the replaced sample must stay consistent: copy the
donor's **whole** sample header (frequency, channel count, sample count,
Vorbis codebook id) together with its data, then fix the container
offsets/sizes (`SNDH` table, FSB header `sampleHeadersSize`/`dataSize`).

**Failure it prevents.** Copying only the data leaves the old header's
sample count and codebook id — the FSB decodes garbage or nothing. The
vanilla FSB mixes 48 kHz and 16 kHz Vorbis with two different codebooks;
a swap that ignores the header breaks on exactly those slots.

**Verified result (8 RWR slots):** each target slot ends with its donor's
header (48 kHz, 2 ch, crc 3301116457) and decodes byte-identically to the
donor; `WAVS` unchanged, so the vanilla event bank resolves everything.
This is a one-off workflow, not a ReBank command.

## 6. Game patch arrived

**Recipe.** Recopy the vanilla banks into the mod folder (§1), rebuild
your project from the new vanilla pair (§4), check which events the game
added or removed:

```sh
rebank my_mod/sound/aircraft_gui.bank --diff "$WT/sound"
rebank check my_mod/sound --game "$WT/sound" --studio-blk <sound_studio.blk>
```

A mod built for the previous patch can miss new required banks — and §1
applies again.

## 7. Checklist

- [ ] `sound/mod/<folder>/` holds all 47 required banks (`rebank check --studio-blk` → OK)
- [ ] every rebuilt bank shipped as `.bank` + `.assets.bank` from the same build
- [ ] no Studio-built `.assets.bank` next to a vanilla `.bank`
- [ ] event names/paths, bank names, parameters unchanged (`rebank check` → OK)
- [ ] `smoke_test.py` on the built bank → PASS
- [ ] `config.blk` has `enable_mod:b=yes` inside `sound{}`
- [ ] tested in game: the event plays the new sound (the only proof that counts)
