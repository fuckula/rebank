# FMOD 2.02 bank layout — decisions

Scope: `rebank.py` parser and `.fspro` writer. Offsets verified
against the bank reader in `fmodstudio64.dll` (IDA, `sub_1800ABC30` and
helpers); see `wtcli/rev/BANK_LAYOUT.md` scratch notes for the decompile.

## Array encoding (all nested arrays)

`varint n` (`raw >> 1`, `u16` with `0x8000` extension), then **one** `u16`
element size, then `n × elemSize` bytes (`sub_1800AEFB0` → `sub_1800BB510`
with `v5 == 0`). Reading `elemSize` per element is wrong and silently
mis-aligns everything after it.

## Strings bank (`STDT` inside `LIST/PROJ`)

`[u32 ver][array(n, es=8) nodes][array(g, es=16) guids][u16 sl][pool]`
`[u16 mc][mc×3 guid→node][u16 pc][pc×3 parent]`. Nodes are two `u32`:
`v1 = strOff (u24)`, `v2 = guidIdx (u24) | childCount << 24`. `0xFFFFFF`
means "none". **`sl` and the two tail counts are plain `u16`, not shifted
varints** — the only place in the format where that is true.
`tests/test_primitives.py` builds a synthetic `STDT` from these rules; it
caught the tail arrays being mis-read as varints.

## Event body (`EVTB`)

| Offset | Field |
|---|---|
| `0x00` | eventGuid |
| `0x10` | timelineGuid |
| `0x20` | outputBus = **instrument track** (`WAIT.tg`) |
| `0x30` | inputBus |
| `0x40` | masterTrack |
| `0x50` / `0x54` | maxInstances / stealing (`u32`) |
| `0x59` | priority (`u32`, unaligned) |
| `0x5D` | slot array → `PMLB` owner GUIDs (parameter sheets) |
| after | two link arrays (`AF9C0`, `AFB70`), then gated `f32` tail |

## Parameter sheets (`PMLB`)

`owner16 + paramGuid16 + array(items, 16)`. Items are `WAIT.ig`, `MUIT`
`MUIB` guid, or scatterer `SPIB`. Slots of one event can drive **different**
parameters; several `PMLB` may share a parameter. `CTRO` (conditions) is
empty in every WT bank seen.

Project mapping: `Event.parameters → ParameterProxy`, one proxy per
parameter, modules on the tracks. No `ParameterCondition` is fabricated.
Studio 2.02 rule (verified through the scripting API): **`ParameterProxy.preset`
and `ParameterCondition.parameter` must point at the `GameParameter`**, never
at the `ParameterPreset`; the `GameParameter` has no file of its own and lives
inside the `ParameterPreset/*.xml` of its preset. A proxy aimed at the preset
is dropped on load and flags the event as "invalid components". Modules must
hang off a track (`MasterTrack`/`Timeline`/`GroupTrack`), not off the proxy.

## Nested events (`LISTEVIS`)

`EVIB[16:32]` = inner (target) event, `INST[0:16]` = owner track/timeline.
Inner unnamed events are merged into the outer named event.

## Why canonical Studio event shape

Studio flags "incomplete or malformed components" when: a `SingleSound`
has no owner, `</object></objects>` are glued, modules sit only on a
`GroupTrack` without `Timeline`. Therefore: modules on `MasterTrack` and
`Timeline` (same GUIDs), every sample inside a `MultiSound`, empty objects
self-closing. Proven with Studio scripting API (`Entity.findInstances`,
`isValid`).

## Facts, not bugs

- `WAIT.tg == 0` instruments belong to parameter sheets, not tracks.
- Events with zero instruments (e.g. `alarm_radar` parent) are empty in the
  bank itself; all 24 `alarm_radar_*` tones come from vanilla via `--game`.
- 55 RWSM-only events have no strings entry; 19 stay unnamed by design.
