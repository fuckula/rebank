# How FMOD Studio 2.02 builds banks — decisions

Scope: what the Studio writer really produces, from `fmodstudioui.dll`
(2.02.22, sha256 `e9a74f7c…`) with IDA 9.5, and how ReBank's `.fspro` and the
mod packaging relate to it. Decompile scratch: `Temp/fmod_pkg/studio_out/`.

**Status:** active · **Evidence:** confirmed (decompile + built output), except
the `encodingFormat` enum, marked below.

## Where the logic lives

- `fmodstudio.exe` == `fmodstudiocl.exe` (same sha256): a 16 KB launcher whose
  only import from `fmodstudioui.dll` is `FMODStudioTool::launchCLI`.
  Everything — CLI parsing, ScriptServer (port 3663), project model, bank
  writer, FSBank — is in `fmodstudioui.dll` (20 MB, Qt5).
- `FMOD Studio.exe` is the GUI stub; it loads the same DLL.

## Bank build path (decompiled)

- `BankBuilderThread::run` (`0x1800478e0`, `bankbuilderthread.cpp`) iterates
  banks × platforms and calls `Bank::build` with a flag word:
  `v113 = base | 0x3800`; a **localized** bank (`sub_1803208A0`) gets `|2`
  (assets inside the per-locale bank), otherwise `|0xC` — i.e. `.assets`
  **and** `.streams` are always separate files for normal banks; bits are
  dropped again when the bank has no streaming / no sample data; `|0x4000`
  is added before the call.
- `Bank::build` (`0x18031f860`, `model/bank.cpp`): suffix by flag bits —
  `&1` → metadata (`""`), `&0xA` → `".assets"`, `&4` → `".streams"`; path =
  `platform.absoluteOutputDirectory() / <name>[_<locale>]<suffix>.bank`
  (`sub_180320AF0`); the master bank also writes `<name>.strings.bank` via
  `modelBuilder.builder()->addStringPath(guid, path)` + `writeToStream`.
  Assertion text: `buildBank(this, dataType, absoluteBinaryPath(platform,
  locale, sBankSuffix(dataType)))`.
- Build settings are **project-level** in `Metadata/Workspace.xml`
  (`builtBanksSeparateAssets`, `builtBanksOutputDirectory`,
  `builtBanksMirrorBrowserFolderHierarchy`, `platforms`), not per Bank XML.
  The official Gaijin project has `builtBanksSeparateAssets=true`, output
  dir empty (= `Build/`), hierarchy mirroring **off**, Platform `Desktop`,
  `subDirectory="sound"`, `speakerFormat=6`, EncodingSetting
  `encodingFormat=1 quality=37 sampleRate=44100`.

## Decisions for ReBank

- **Mod packaging = full required set.** Gate 1 of the game rejects a partial
  folder (see `sound-mod-loading.md`), so `rebank check --studio-blk` now
  verifies that every non-optional bank of `config/sound_studio.blk` is
  present, and without the blk warns about a metadata bank whose
  `<name>.assets.bank` the game ships but the mod lacks.
  **Reason:** one missing file silently disables the whole mod; no error is
  visible to the user (`.clog` is encrypted). **Rejected:** documenting only —
  the failure is silent, a tool check is the only guard.
- **Assets-only SPO patch (in-place FSB sample swap)** is kept as a one-off
  workflow, not a ReBank command: it relies on copying the donor's whole
  sample header (frequency, channel count, Vorbis codebook crc, sample count)
  together with its data so the WAVS table and waveform GUIDs stay vanilla.
  Verified on the 8 RWR slots: after the swap every slot's header equals its
  donor's (48 kHz / 2 ch / crc 3301116457) and the decoded OGG is
  byte-identical to the donor. Studio cannot produce this (its build assigns
  new waveform GUIDs).
- `encodingFormat`: ReBank writes `3`, Gaijin writes `1`. The enum is
  `FMOD_STUDIO_ENCODING_FORMAT` (`PCM8=0, PCM16=1, PCM24=2, PCM32=3,
  PCMFLOAT=4, Vorbis=5, FADPCM=6, XMA=7, AT9=8, Opus=9`) **Evidence:
  unknown** — the DLL's combobox order matches, but neither value maps to
  the Vorbis (mode 15) FSB the vanilla bank carries, so the per-platform
  default (`EncodingSetting` is per asset here) must be read from the build
  output; left unchanged until a Studio build proves which value yields
  Vorbis.
