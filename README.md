# fmod-bank-unwrap

Unwrap compiled FMOD Studio `.bank` files (FEV container, FMOD Studio 2.0x /
format version 0x8C–0x8E) back into named audio and an editable FMOD Studio
project.

Banks do not store names. This tool rebuilds the chain:

```
masterbank.strings.bank   (STDT radix-trie: GUID -> event:/ bus:/ path)
        |
EVTS / EVTB              (event: GUID, event-mixer track at 0x20)
        |
WAIS / MUIS instruments  (trackGuid -> waveformGuid)
        |
WAVS / WAV               (waveformGuid -> sample index; a repeated index
        |                  belongs to the next FSB container)
        v
sound_N.wav  ->  aircraft/gui/000_focus.wav
```

## Features

| Command | What it does |
|---|---|
| default | Parses the bank, writes `<bank>_samples.csv` (sample -> events map) and `<bank>_names.json` |
| `--rename-dir DIR...` | Copies decoded `sound_N.wav` folders (Fmod Bank Tools output) into an event-path tree `aircraft/gui/000_focus.wav` |
| `--diff GAME_DIR` | Report: which events your bank is missing vs the current game install |
| `--fspro` | Generates a **FMOD Studio project** (`<out>/fspro/<bank>.fspro`): events with original GUIDs (game-compatible), SingleSound/MultiSound instruments, `Assets/` audio — open, edit, Build |
| `--game GAME_DIR` | Backfills events missing from your bank using the game's vanilla bank pair (`X.bank` + `X.assets.bank`), decoding its FSB5 samples (Vorbis/FADPCM) on the fly |
| `-a X.assets.bank` | Vanilla-style banks where events and samples live in separate files |

Deps: `pip install -r requirements.txt` (+ `ffmpeg` on PATH for Ogg->WAV
conversion; DLL fallback `bin/libogg.dll`, `bin/libvorbis.dll`).

## Usage

```bat
REM 1) name-tag samples (decode first with Fmod Bank Tools if you have its wav folders)
python fmod_bank_unwrap.py RWSM\aircraft_gui.bank ^
    --rename-dir "FMOD Bank Tools\wav\aircraft_gui[0]" ^
    --rename-dir "FMOD Bank Tools\wav\aircraft_gui[1]" --apply

REM 2) diff against the installed game
python fmod_bank_unwrap.py RWSM\aircraft_gui.bank ^
    --diff "C:\...\War Thunder\sound"

REM 3) editable FMOD Studio project + backfill missing sounds from vanilla
python fmod_bank_unwrap.py RWSM\aircraft_gui.bank ^
    --rename-dir "FMOD Bank Tools\wav\aircraft_gui[0]" ^
    --rename-dir "FMOD Bank Tools\wav\aircraft_gui[1]" ^
    --fspro --game "C:\...\War Thunder\sound" --apply
```

Then open `<out>\fspro\<bank>.fspro` in FMOD Studio 2.02.22, edit, Build.

## Verified against (War Thunder, 2026-11)

- RWSM mod banks (single-file layout): 330 events / 378 samples unwrapped,
  249 named via `masterbank.strings.bank`.
- Vanilla game banks (split `X.bank` + `X.assets.bank`): 311 events / 408
  samples; `--fspro --game` merges both sources into one 311-event project.
- 55 RWSM-only events have no strings entry (mod author's custom actions);
  19 remain unnamed by design — names only exist in the mod's source project.

## Known limitation: parameter-driven playlists

Multi Instruments whose `trackGuid` is zero (parameter-scatter playlists,
e.g. per-RWR warning tones) are not linked to their events by the bank
format itself — FMOD resolves them at runtime through parameter values.
The tool links every instrument that has an explicit track; zero-track
playlists are skipped rather than guessed (their 53 decoded samples remain
in the report). Mixer buses, snapshots and automation curves are not
exported into the generated project.

## Credits

- Bank format reverse-engineering: [wheatleyinspace/fmod-bank-tools](https://github.com/wheatleyinspace/fmod-bank-tools) specifications.
- FSB5 decode: [HearthSim/python-fsb5](https://github.com/HearthSim/python-fsb5); Ogg/Vorbis libs via [TeamPyOgg/PyOgg](https://github.com/TeamPyOgg/PyOgg) (bundled in `bin/`).
- Reference project structure: [GaijinEntertainment/fmod_studio_warthunder_for_modders](https://github.com/GaijinEntertainment/fmod_studio_warthunder_for_modders).

## License

MIT — see [LICENSE](LICENSE).
