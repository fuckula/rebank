# ReBank

[![CI](https://github.com/fuckula/rebank/actions/workflows/ci.yml/badge.svg)](https://github.com/fuckula/rebank/actions/workflows/ci.yml)
[![PyPI](https://img.shields.io/pypi/v/rebank)](https://pypi.org/project/rebank/)
[![Python](https://img.shields.io/pypi/pyversions/rebank)](https://pypi.org/project/rebank/)
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

Core has **no dependencies** (Python ≥ 3.10, standard library only).

```sh
pip install rebank            # parsing, reports, project from existing wav
pip install "rebank[decode]"  # + FSB5 decoding (Vorbis / FADPCM) via python-fsb5
```

Windows users without Python: grab `rebank-<version>-windows.zip` from
[Releases](https://github.com/fuckula/rebank/releases) — a
self-contained `rebank.exe`.

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
