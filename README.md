# ReBank

[![CI](https://github.com/fuckula/rebank/actions/workflows/ci.yml/badge.svg)](https://github.com/fuckula/rebank/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

**Turn compiled FMOD Studio `.bank` files back into named audio samples and an
editable FMOD Studio project.**

A bank stores GUIDs, not names. ReBank rebuilds the chain
`strings.bank → events → instruments → waveforms → FSB5 samples`, so every
sample lands under its real event path (`aircraft/gui/alarm_radar_an_alr_56/001.wav`)
and every event comes back with its original name, GUID and game parameters —
ready to open in FMOD Studio 2.02, edit and Build again.

Built for War Thunder sound modders (vanilla backfill, RWR/GUI banks,
`--diff` against the installed game), works with any FMOD Studio 2.0x bank
(format `0x8C`–`0x8E`).

```
masterbank.strings.bank   (STDT radix-trie: GUID -> event:/ bus:/ path)
        |
EVTS / EVTB              (event GUID, instrument track, parameter sheets)
        |
WAIS / MUIS instruments  (trackGuid / parameter sheet -> waveformGuid)
        |
WAVS / WAV               (waveformGuid -> sample index; a repeated index
        |                  belongs to the next FSB container)
        v
sound_N.wav  ->  aircraft/gui/000_focus.wav  ->  fspro project
```

> **Created with AI assistance.** This project was designed and written by an
> AI coding assistant under human direction; the bank format was verified
> against real files. Please review the code before relying on it for
> anything important.

## Install

**Windows (no Python needed):** download `rebank.exe` from the latest
[Release](https://github.com/fuckula/rebank/releases) and run it from any
folder. It is a single self-contained file with FSB5 decoding built in.

**From source** (any OS, Python ≥ 3.10, core has no dependencies):

```sh
git clone https://github.com/fuckula/rebank
cd rebank
pip install .                 # parsing, reports, project from existing wav
pip install ".[decode]"       # + FSB5 decoding (Vorbis / FADPCM) via python-fsb5
```

Or run it straight from the checkout: `python rebank.py …` (same as `rebank`).


`ffmpeg` on `PATH` is needed only when decoded samples are Ogg (FMOD Studio
imports PCM wav).

## Usage

`$WT` below is the War Thunder installation folder (`…/War Thunder`). Omit
`--apply` to get reports only.

**A. Inspect a bank without extracting anything**
```sh
rebank weapon_turret.bank
```
Reads `masterbank.strings.bank` next to it, writes `weapon_turret_samples.csv`
(which event plays which sample) and `weapon_turret_names.json`. Nothing else
is touched.

**B. Rebuild a mod author's bank into a Studio project (single-file layout)**
```sh
rebank RWSM/aircraft_gui.bank --fspro --apply
```
The mod bank embeds its FSB5 containers; samples are decoded with
`[decode]`, placed under `fspro/Assets/<event path>/`, and the project opens
with the mod's event names and GUIDs.

**C. Vanilla game bank (split layout) with names from the game**
```sh
rebank "$WT/sound/aircraft_gui.bank" -a "$WT/sound/aircraft_gui.assets.bank" \
    -s "$WT/sound/masterbank.strings.bank" --fspro --apply
```
Events live in `X.bank`, samples in `X.assets.bank`; `-s` points at the game's
string dictionary.

**D. Mod bank + fill the gaps from the game**
```sh
rebank RWSM/aircraft_gui.bank --fspro --game "$WT/sound" --apply
```
Every event the mod lacks (or leaves without instruments — e.g. RWR alarm
tones) is taken from the vanilla bank pair, samples copied to
`_from_vanilla/`, parameter sheets (`track`/`volume`/…) preserved. The result
is a complete project you can build as a drop-in replacement.

**E. Use wav files extracted by another tool instead of decoding**
```sh
rebank my.bank --fspro \
    --rename-dir "FMOD Bank Tools/wav/my[0]" \
    --rename-dir "FMOD Bank Tools/wav/my[1]" --apply
```
No `[decode]` extra needed; folders are matched to FSB containers in order.

**F. Keep a mod up to date with game patches**
```sh
rebank RWSM/aircraft_gui.bank --diff "$WT/sound"
```
Writes `RWSM_vs_vanilla_report.txt`: events added or removed in the game
since the bank was built.

**G. Several banks at once**
```sh
for b in "$WT/sound/"{tanks,weapons,aircraft}.bank; do
  rebank "$b" -a "${b%.bank}.assets.bank" --fspro --apply
done
```
Each bank becomes its own `fspro/` project.

## Starting a mod from scratch

Step-by-step recipes — the complete bank set, split `.bank`/`.assets.bank`
pairs, rebuilding a bank with ReBank and Studio, changing samples without
touching the metadata bank, and the mistakes that make the game ignore a mod
silently — are in [`docs/MODDING_GUIDE.md`](docs/MODDING_GUIDE.md).

The supported base for a new sound mod is Gaijin's official project
[`fmod_studio_warthunder_for_modders`](https://github.com/GaijinEntertainment/fmod_studio_warthunder_for_modders)
(FMOD Studio 2.02.22). `rebank init` sets up a workspace around it:

```sh
rebank init my-mod                        # clones the reference project into my-mod/reference
rebank init my-mod --reference ./fmod_studio_warthunder_for_modders-master   # or reuse a local copy
```

```
my-mod/
├── reference/     official project: open sounds.fspro, edit events, Build
└── mod/
    ├── README.txt  rules + install snippet for users
    └── sound/      your built .bank (+ .assets.bank) files
```

The game does not merge a partial mod: with `enable_mod:b=yes` it checks that
**every bank** of `config/sound_studio.blk` without `optional:b=true` (47
banks in the Sky Odyssey build: `masterbank*`, all `aircraft_*`, `tanks_*`,
`ships_*` and their `.assets` pairs) exists in `sound/mod/<any folder>/`. The
first missing one switches the whole mod off (`Sound.MOD disabled: modded bank
is missing`) and the game plays vanilla sound. So ship the full set — the
vanilla banks copied unchanged plus the ones you rebuilt — and validate
before sharing:

```sh
rebank check my-mod/mod/sound --game "$WT/sound" \
    --studio-blk /tmp/wt_aces/aces.vromfs.bin_u/config/sound_studio.blk
```

It reports events that were renamed or dropped versus the game bank (both
break the mod), banks the game does not know and — with `--studio-blk` —
banks the game requires but the folder lacks. Without `--studio-blk` it warns
about metadata banks whose `<name>.assets.bank` exists in the game but not in
the mod (vanilla samples are used for those). Exit code is non-zero on
problems, so it fits a build script.

Banks are built as split pairs (`.bank` = metadata, `.assets.bank` = sample
data), exactly as the official project does (`Workspace` → "Build metadata
and assets to separate banks"); both halves of a rebuilt bank go into the
mod folder.

The reference project covers **107 of the 139** banks the game ships; the
rest (localised dialogs, `infantry_*`, `football`) are not in it. For those,
and for events the project leaves out (all 24 RWR `alarm_radar_*` tones, for
example), build the project from the vanilla bank instead (scenario C/D) and
copy the events you need into your mod project.

## Event catalog

`rebank catalog` lists every event of every bank with the game parameters it
reacts to:

```sh
rebank catalog "$WT/sound" -o docs/EVENTS.md --csv docs/EVENTS.csv
```

| Bank group | What lives there |
|---|---|
| `aircraft_gui` | cockpit warnings, RWR alarms, lock/launch tones, GUI |
| `aircraft_*`, `weapons_*`, `engines_*` | airframes, guns, missiles, engines |
| `tanks_*`, `ships_*` | ground and naval vehicles |
| `*_crew_dialogs_*`, `_dialogs_*` | localized crew voice (not in the reference project) |
| `infantry_*`, `football`, `dialogs` | infantry and event modes (not in the reference project) |

The catalog for the tested build is committed at
[`docs/EVENTS.md`](docs/EVENTS.md) (34k lines, one row per event).

## Who calls which event

The banks cannot tell which vehicle plays which event; the game data can.
The scripts under `scripts/` read the text output of
[wt_ext_cli](https://github.com/Warthunder-Open-Source-Foundation/wt_ext_cli)
(third-party; ReBank only reads its output) and regenerate the committed
tables after a game patch:

```sh
wt_ext_cli unpack_vromf -i "$WT/aces.vromfs.bin"  -o /tmp/wt_aces  --format BlkText
wt_ext_cli unpack_vromf -i "$WT/char.vromfs.bin"  -o /tmp/wt_char  --format BlkText
wt_ext_cli unpack_vromf -i "$WT/game.vromfs.bin"  -o /tmp/wt_game  --format BlkText
G=/tmp/wt_aces/aces.vromfs.bin_u/gamedata
python scripts/vehicle_table.py aircraft $G --all -o docs
python scripts/vehicle_table.py weapons  $G -o docs/WEAPONS.md
python scripts/sound_refs.py /tmp/wt_aces/aces.vromfs.bin_u /tmp/wt_char/char.vromfs.bin_u \
    /tmp/wt_game/game.vromfs.bin_u -o docs/SOUND_REFS.md
```

| Document | Rows | Content |
|---|---|---|
| [`docs/AIRCRAFT.md`](docs/AIRCRAFT.md) | 1547 | per flight model: RWR indicator, sensors, alarm events, engine / gun / turret presets |
| [`docs/HELICOPTERS.md`](docs/HELICOPTERS.md) | 119 | same columns as aircraft |
| [`docs/TANKS.md`](docs/TANKS.md) | 1483 | per ground vehicle: engine, AI engine, tracks, turret / gun turn, backfire presets |
| [`docs/SHIPS.md`](docs/SHIPS.md) | 756 | per ship: engine, AI engine, wake, turret / gun turn presets |
| [`docs/VEHICLE_WEAPONS.md`](docs/VEHICLE_WEAPONS.md) | 3905 | per vehicle: the sounding weapon blocks it mounts |
| [`docs/WEAPONS.md`](docs/WEAPONS.md) | 2883 | per weapon block with sound fields: fire sound, interior variant, reload, guidance tone, `sound_path` |
| [`docs/SOUND_REFS.md`](docs/SOUND_REFS.md) | 1898 | per event: the data fields that name it; plus sound fields that hold presets resolved by native code |

`VEHICLE_WEAPONS.md` lists the weapon blocks each vehicle mounts by `blk:t`,
only those with a sound preset: pylon launchers are dropped, a container
resolves to the missile it holds and `_default/_user/_ai/_tmc` variants
collapse to the core name. Their presets are one lookup away in `WEAPONS.md`.

Static air-defence guns (`units/air_defence`) carry no sound block of their
own and are therefore not listed; events with no row in `SOUND_REFS.md` (crew
dialogs, chat, voice warnings) are started from native code by path or GUID.

## Output

Output (`<bank>_unwrapped/` by default):

| Path | Content |
|---|---|
| `<bank>_samples.csv` | sample -> events map |
| `<bank>_names.json` | event GUID -> name |
| `fspro/<bank>.fspro` | FMOD Studio project (`--fspro`) |
| `fspro/Assets/<event path>/NNN.wav` | samples placed under their event path |
| `_from_vanilla/` | samples borrowed from the game bank (`--game`) |

## Tested against

Verified with the official War Thunder modding project
[`GaijinEntertainment/fmod_studio_warthunder_for_modders`](https://github.com/GaijinEntertainment/fmod_studio_warthunder_for_modders)
at the **Sky Odyssey update (16 Sep 2026)** — FMOD Studio **2.02.22**,
`serializationModel="Studio.02.02.00"`. Banks: `aircraft_gui` mod bank
(330 events / 378 samples) and vanilla split pair (311 events / 408
samples). Bank format `fmt=0x8E`. Older FMOD 2.0x banks (`0x8C`/`0x8D`)
parse with the same code path but were not exercised.

## Options

| Option | Meaning |
|---|---|
| `-s, --strings PATH` | `*.strings.bank` (default: `masterbank.strings.bank` next to the bank) |
| `-a, --assets PATH` | paired `X.assets.bank` holding the samples (split layout) |
| `-o, --out DIR` | output root (default: `<bank>_unwrapped`) |
| `--csv PATH`, `--json PATH` | custom report paths |
| `--rename-dir DIR` (repeat) | folders with pre-extracted `sound_N.wav`, one per FSB |
| `--fsb-dir DIR` | folder with cut-out `.fsb` files |
| `--fspro` | generate the FMOD Studio project |
| `--game DIR` | backfill missing events from a game sound dir (with `--fspro`) |
| `--game-wav DIR` (repeat) | pre-extracted vanilla `sound_N.wav` instead of decoding |
| `--diff DIR` | report differences against a game sound dir |
| `--apply` | write files (default: reports only) |

## What the project keeps

- Event names, paths and GUIDs (game-compatible).
- Single instruments as `SingleSound`, playlists as `MultiSound`.
- Parameter sheets (`track`, `volume`, `on_shot`, …) as `ParameterProxy`
  modules per game parameter, with the original parameter names.
- Nested events merged into their named outer event.

## Limitations

- Mixer buses, snapshots, automation curves and transition regions are not
  reconstructed; the project targets a flat master bus.
- Events with no resolvable instrument stay empty — the bank has nothing
  to play for them.
- Banks without a `strings.bank` yield unnamed events (names live only in
  the author's source project).
- FMOD Studio 2.02 project model (`serializationModel="Studio.02.02.00"`).

## War Thunder notes

Built and verified against War Thunder banks (FMOD Studio **2.02.22**).
When shipping a sound mod, the game requires event names, folder layout,
bank names and mixer bus structure to stay identical to the official
project — change the *content* of events, not their identity.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Bug reports that include the bank
format version (`fmt=0x8C/0x8D/0x8E` printed by the tool) are the most
useful. **Do not attach game banks** — they are proprietary.

## License

[MIT](LICENSE). Not affiliated with Firelight Technologies or Gaijin
Entertainment. Bundled `libogg`/`libvorbis` DLLs are under their own BSD-style
licenses, see [NOTICE](NOTICE).
