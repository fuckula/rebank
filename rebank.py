#!/usr/bin/env python3
"""
rebank — rebuild FMOD Studio .bank (FEV) files into named samples and an editable project.

Banks do not store sample names. Names are rebuilt through the chain
  strings.bank (GUID -> path) -> EVTB (event) -> track -> WAIT/MUIT (instrument)
  -> WAIB (waveform) -> WAV (sample index) -> FSB5 sound_N
and samples are laid out as <event path>/<index>_<name>.wav.

Usage:
  rebank BANK.bank [options]         unwrap one bank (or: python rebank.py ...)
  rebank init DIR                    new mod workspace on the official Gaijin project
  rebank check MOD_DIR --game DIR    validate built mod banks against the game
  rebank catalog GAME_DIR            list every event of every bank (docs/EVENTS.md)

Options:
  -s, --strings PATH     *.strings.bank (default: masterbank.strings.bank next to the bank)
  -a, --assets PATH      paired X.assets.bank holding the samples (split-bank layout)
  -o, --out DIR          output root (default: <bank>_unwrapped)
  --csv PATH             sample -> events report (default: <out>/<bank>_samples.csv)
  --json PATH            name map (default: <out>/<bank>_names.json)
  --rename-dir DIR       folder with pre-extracted sound_N.wav (repeat per FSB: [0], [1], ...)
  --fsb-dir DIR          folder with cut-out .fsb files (saved as <out>/fsb/N.fsb)
  --fspro                generate an FMOD Studio project (<out>/fspro/<bank>.fspro)
  --game DIR             fill events missing or left empty in your bank from the game's sound dir
  --game-wav DIR         pre-extracted vanilla sound_N.wav folders (alternative to decoding)
  --diff DIR             report: compare against the game's sound dir
  --apply                write files (without it only reports are written)

Example:
  fbu RWSM/aircraft_gui.bank --fspro --game "C:/.../War Thunder/sound" --apply
"""
import argparse
import csv
import json
import os
import re
import shutil
import struct
import subprocess
import sys
import uuid
import wave
from collections import defaultdict

# ------------------------------------------------------------------ RIFF/GUID

def walk_chunks(data, start, end):
    """(offset, fourcc, size, list_type) for the RIFF chunks in [start, end)."""
    p = start
    while p + 8 <= end:
        cid = data[p:p+4]
        sz = struct.unpack('<I', data[p+4:p+8])[0]
        typ = data[p+8:p+12] if cid == b'LIST' else None
        yield p, cid, sz, typ
        p += 8 + sz + (sz & 1)


def guid_str(raw):
    d1, d2, d3 = struct.unpack('<IHH', raw[:8])
    d4 = raw[8:16]
    return '{%08x-%04x-%04x-%s-%s}' % (d1, d2, d3, d4[:2].hex(), d4[2:].hex())


def read_varint(buf, off):
    w = struct.unpack('<H', buf[off:off+2])[0]
    off += 2
    if w & 0x8000:
        w2 = struct.unpack('<H', buf[off:off+2])[0]
        off += 2
        return ((w & 0x7FFF) | (w2 << 15)), off
    return w, off


def read_array(buf, off):
    """Array layout of the Studio reader (sub_1800AEFB0): varint n (raw>>1), then a
    u16 elemSize written ONCE (sub_1800BB510 when v5==0), then n×elemSize bytes.
    -> ([bytes...], offset after the array)"""
    w, off = read_varint(buf, off)
    n = w >> 1
    if n == 0:
        return [], off
    es = struct.unpack_from('<H', buf, off)[0]
    off += 2
    end = off + es * n
    if end > len(buf):
        raise ValueError('array overrun: n=%d es=%d' % (n, es))
    return [buf[off + es * i:off + es * (i + 1)] for i in range(n)], end


# --------------------------------------------------------------- strings.bank

def parse_strings_bank(path):
    """GUID (raw 16 bytes) -> path (event:/..., bus:/...)."""
    data = open(path, 'rb').read()
    stdt = None
    for p, cid, sz, typ in walk_chunks(data, 12, len(data)):
        if cid == b'LIST' and typ == b'PROJ':
            for q, c2, s2, _ in walk_chunks(data, p+12, p+8+sz):
                if c2 == b'STDT':
                    stdt = data[q+8:q+8+s2]
                    break
            break
    if stdt is None:
        raise ValueError('STDT chunk not found: %s' % path)
    off = 4
    # same arrays as EVTB: varint n, then u16 elemSize ONCE, then n*es
    nodes_raw, off = read_array(stdt, off)
    nodes = []
    for raw in nodes_raw:
        v1, v2 = struct.unpack('<II', raw[:8])
        nodes.append((v1 & 0xFFFFFF, v2 & 0xFFFFFF, (v2 >> 24) & 0xFF))
    guids_raw, off = read_array(stdt, off)
    guids = [bytes(raw[:16]) for raw in guids_raw]
    sl, off = read_varint(stdt, off)
    pool = stdt[off:off+sl]
    off += sl
    # tail: two arrays of u16 count + count×3 bytes (no varint/elemSize):
    # guid -> node, then node -> parent (0xFFFFFF = root)
    def u24_at(o):
        return stdt[o] | (stdt[o+1] << 8) | (stdt[o+2] << 16)
    mc = struct.unpack_from('<H', stdt, off)[0]
    off += 2 + mc * 3
    pc = struct.unpack_from('<H', stdt, off)[0]
    off += 2
    parents = [u24_at(off + 3*i) for i in range(pc)]
    parents = [v if v != 0xFFFFFF else -1 for v in parents]
    out = {}
    for idx, (_so, cg, cc) in enumerate(nodes):
        if cc == 0 and idx != 0:
            segs, cur = [], idx
            while cur != -1:
                s_off = nodes[cur][0]
                if s_off != 0xFFFFFF and s_off < len(pool):
                    e = pool.find(b'\x00', s_off)
                    segs.append(pool[s_off:e].decode('utf-8', 'replace'))
                cur = parents[cur]
            if cg < len(guids):
                out[guids[cg]] = ''.join(reversed(segs))
    return out


# ------------------------------------------------------------------ FEV bank

class Bank:
    def __init__(self, path):
        self.path = path
        self.data = d = open(path, 'rb').read()
        if d[:4] != b'RIFF' or d[8:12] != b'FEV ':
            raise ValueError('%s: not an FMOD FEV bank' % path)
        self.fmt_version = struct.unpack('<I', d[20:24])[0]
        self.name = os.path.splitext(os.path.basename(path))[0]
        proj = None
        for p, cid, sz, typ in walk_chunks(d, 12, len(d)):
            if cid == b'LIST' and typ == b'PROJ':
                proj = (p, sz)
                break
        if not proj:
            raise ValueError('LIST PROJ not found')
        self.sections = {}
        for p, cid, sz, typ in walk_chunks(d, proj[0]+12, proj[0]+8+proj[1]):
            self.sections[(cid + (typ or b'')).decode('latin1')] = (p, sz)

    def items(self, list_tag, item_tag, wanted):
        """Walk LIST list_tag { item_tag: subchunks... } keeping the wanted fields."""
        sec = self.sections.get(list_tag)
        if not sec:
            return []
        p0, sz = sec
        out = []
        for p, cid, s, typ in walk_chunks(self.data, p0+12, p0+8+sz):
            if cid == b'LIST' and typ == item_tag:
                rec = {}
                for q, c2, s2, _ in walk_chunks(self.data, p+12, p+8+s):
                    if c2 in wanted:
                        rec[c2] = self.data[q+8:q+8+s2]
                out.append(rec)
        return out


def parse_bank(path):
    bank = Bank(path)
    events = {}   # eventGuid -> body
    for rec in bank.items('LISTEVTS', b'EVNT', {b'EVTB'}):
        body = rec[b'EVTB']
        events[body[0:16]] = body
    waits = []    # single instruments
    for rec in bank.items('LISTWAIS', b'WAIT', {b'WAIB', b'INST'}):
        waib, inst = rec.get(b'WAIB'), rec.get(b'INST')
        if not waib:
            continue
        waits.append({'ig': waib[0:16], 'wg': waib[16:32],
                      'tg': inst[0:16] if inst else None})
    muits = []    # multi instruments: playlist items -> WAIB instanceGuid
    for rec in bank.items('LISTMUIS', b'MUIT', {b'MUIB', b'PLST', b'INST'}):
        plst, inst, muib = rec.get(b'PLST'), rec.get(b'INST'), rec.get(b'MUIB')
        if not plst:
            continue
        cnt = struct.unpack('<H', plst[8:10])[0] >> 1
        items = [plst[12+20*i:12+20*i+16] for i in range(cnt)]
        muits.append({'tg': inst[0:16] if inst else None, 'items': items,
                      'guid': muib[:16] if muib else None})
    wavs = []     # waveform descriptors
    sec = bank.sections.get('LISTWAVS')
    if sec:
        p0, sz = sec
        for p, cid, s2, _ in walk_chunks(bank.data, p0+12, p0+8+sz):
            if cid == b'WAV ':
                b = bank.data[p+8:p+8+s2]
                wavs.append({
                    'guid': b[0:16],
                    'flags': struct.unpack('<I', b[16:20])[0],
                    'index': struct.unpack('<I', b[20:24])[0] >> 16,
                    'field': struct.unpack('<I', b[24:28])[0],
                    'sub': struct.unpack('<H', b[28:30])[0],
                })
    evis = []    # event instruments: (targetEventGuid, ownerTrackGuid) — nested events
    for rec in bank.items('LISTEVIS', b'EVIT', {b'EVIB', b'INST'}):
        evib, inst = rec.get(b'EVIB'), rec.get(b'INST')
        if evib and inst:
            evis.append((evib[16:32], inst[0:16]))
    bank.evis = evis
    # Parameter sheets (ActionSheet): PMLB.owner — slot of the event at EVTB[0x5D],
    # paramGuid — the parameter (track/intense/volume), items — WAIT.ig / MUIT / scatterer.
    # EVTB cursor (reader sub_1800ABC30): 0x5D varint n, then u16 elemSize ONCE,
    # then n×elemSize bytes (sub_1800AEFB0 → sub_1800BB510(v5=0) once).
    bank.params = {}     # paramGuid -> (name, min, max)
    bank.pml = {}        # ownerGuid -> [(paramGuid, [itemGuid...]), ...]
    bank.ev_slots = {}   # eventGuid -> [slotGuid...]
    sec = bank.sections.get('LISTPRMS')
    if sec:
        for rec in bank.items('LISTPRMS', b'PARM', {b'PRMB'}):
            bl = rec.get(b'PRMB')
            if bl and len(bl) >= 26:
                nlen = struct.unpack('<H', bl[24:26])[0]
                f = struct.unpack_from('<fff', bl, 26 + nlen) if len(bl) >= 26 + nlen + 12 else (0.0, 1.0, 0.0)
                bank.params[bl[:16]] = (bl[26:26 + nlen].decode('utf-8', 'replace'),) + f
    sec = bank.sections.get('LISTPMLS')
    if sec:
        for p, cid, s, typ in walk_chunks(bank.data, sec[0] + 12, sec[0] + 8 + sec[1]):
            if cid == b'LIST' and typ == b'PMLO':
                for q, c2, s2, _ in walk_chunks(bank.data, p + 12, p + 8 + s):
                    if c2 == b'PMLB':
                        x = bank.data[q + 8:q + 8 + s2]
                        try:
                            items, _ = read_array(x, 32)
                        except (ValueError, struct.error):
                            items = []
                        bank.pml.setdefault(x[:16], []).append((x[16:32], items))
    for eg, body in events.items():
        try:
            slots, _ = read_array(body, 0x5D)
        except (ValueError, struct.error):
            slots = []
        if slots:
            bank.ev_slots[eg] = slots
    fsbs = []     # embedded FSB5 containers (SNDH -> SND offsets)
    sec = bank.sections.get('SNDH')
    if sec:
        p0, sz = sec
        h = bank.data[p0+8:p0+8+sz]
        n = (sz - 4) // 8
        for i in range(n):
            off, size = struct.unpack('<II', h[4+8*i:12+8*i])
            if off and bank.data[off:off+4] == b'FSB5':
                ver, ns, hs, nt, ds, mode = struct.unpack('<6I', bank.data[off+4:off+28])
                fsbs.append({'offset': off, 'size': size, 'num': ns, 'mode': mode})
    return bank, events, waits, muits, wavs, fsbs


def event_owners(events, evis):
    """inner eventGuid -> outer eventGuid through EVIS: the instrument sits on the
    outer event's track (EVTB[0x20]/[0x40]) and plays the inner one (EVIB[16:32])."""
    out2ev = {body[0x20:0x30]: eg for eg, body in events.items()}
    master2ev = {body[0x40:0x50]: eg for eg, body in events.items()}
    owner = {}
    for inner, tg in evis:
        outer = out2ev.get(tg) or master2ev.get(tg)
        if outer and outer != inner:
            owner[inner] = outer
    return owner


def link_samples(events, waits, muits, wavs, evis=()):
    """-> sample_events: (fsb, index) -> {eventGuid}, tg2ev, wg2wav.
    Instruments (WAIT/MUIT) sit on the event's mixer track — outputBusGuid in
    EVTB (0x20), one per event. Playlists with a zero trackGuid belong to no
    event (parameter sheets, skipped). Instruments of unnamed inner events
    (EVIS) are credited to their outer owner."""
    owner = event_owners(events, evis)
    out2ev = {body[0x20:0x30]: eg for eg, body in events.items()}
    master2ev = {body[0x40:0x50]: eg for eg, body in events.items()}
    tg2ev = {}
    for tg in {w['tg'] for w in waits} | {m['tg'] for m in muits}:
        if not tg or tg == b'\x00' * 16:
            continue
        tg2ev[tg] = out2ev.get(tg) or master2ev.get(tg)
    wg2wav = {}
    seen = defaultdict(int)
    for w in wavs:
        # when index k repeats, the second WAV row refers to the next FSB
        # container (FMOD serialization order)
        seen[w['index']] += 1
        wg2wav[w['guid']] = (seen[w['index']] - 1, w)
    ig2w = {w['ig']: w for w in waits}
    sample_events = defaultdict(set)
    for w in waits:
        rec = wg2wav.get(w['wg'])
        eg = tg2ev.get(w['tg']) if rec else None
        eg = owner.get(eg, eg) if eg else None
        if rec and eg:
            sample_events[(rec[0], rec[1]['index'])].add(eg)
    for m in muits:
        eg = tg2ev.get(m['tg'])
        eg = owner.get(eg, eg) if eg else None
        if not eg:
            continue
        for g in m['items']:
            w = ig2w.get(g)
            rec = wg2wav.get(w['wg']) if w else None
            if rec:
                sample_events[(rec[0], rec[1]['index'])].add(eg)
    return sample_events, tg2ev, wg2wav


def instrument_keys(item, waits, muits, wg2rec, audio_map, prefix='v'):
    """Instrument GUID from PMLB.items -> ('S'|'M', [keys]) or None: WAIT.ig -> ('S', sample),
    MUIT (by MUIB guid or tg) -> ('M', samples of its playlist). Only keys present in audio_map."""
    ig2w = {w['ig']: w for w in waits}
    def key(w):
        rec = wg2rec.get(w['wg']) if w else None
        return (prefix, rec[0], rec[1]['index']) if rec and (prefix, rec[0], rec[1]['index']) in audio_map else None
    w = ig2w.get(item)
    if w:
        k = key(w)
        return ('S', [k]) if k else None
    for m in muits:
        if item in (m.get('guid'), m['tg']):
            ks = [k for it in m['items'] if (k := key(ig2w.get(it)))]
            return ('M', ks) if ks else None
    return None


def sheet_mods(ev_slots, pml, params, waits, muits, wg2rec, audio_map, prefix='v'):
    """PMLB parameter sheets of every EVTB[0x5D] slot of an event.
    -> [(paramGuid, (name, min, max), [[mod, ...], ...])]: one ParameterProxy per
    parameter, one module list per PMLB, one module per instrument, bank order."""
    merged = {}
    for slot in ev_slots:
        for pg, its in pml.get(slot, []):
            mods = [mod for it in its if (mod := instrument_keys(it, waits, muits, wg2rec, audio_map, prefix))]
            if mods:
                merged.setdefault(pg, []).append(mods)
    return [(pg, params.get(pg, (guid_str(pg), 0.0, 1.0, 0.0))[:3], groups) for pg, groups in merged.items()]


# ------------------------------------------------------------------ renaming

BAD = re.compile(r'[<>:"/\\|?*\x00-\x1f]')


def safe_name(s):
    s = BAD.sub('_', s).strip(' .')
    return s or 'unnamed'


def event_rel_dir(path):
    """event:/a/b/c -> (folder path 'a/b' without the last segment, name)."""
    rel = path.replace('event:/', '', 1)
    parts = [safe_name(x) for x in rel.split('/')]
    return parts[:-1], parts[-1]


# ------------------------------------------------------- FMOD Studio project

def new_guid():
    return '{%s}' % uuid.uuid4()


def _xml_obj(cls, oid, body=''):
    if not body:
        return '\t<object class="%s" id="%s" />\n' % (cls, oid)
    return '\t<object class="%s" id="%s">\n%s\t</object>\n' % (cls, oid, body)


def _prop(name, val):
    return '\t\t<property name="%s">\n\t\t\t<value>%s</value>\n\t\t</property>\n' % (name, val)


def _rel(name, *dests):
    if not dests:
        return ''
    ds = ''.join('\t\t\t<destination>%s</destination>\n' % d for d in dests)
    return '\t\t<relationship name="%s">\n%s\t\t</relationship>\n' % (name, ds)


def _xml(model, *objs):
    return ('<?xml version="1.0" encoding="UTF-8"?>\n'
            '<objects serializationModel="%s">\n%s</objects>\n' % (model, ''.join(objs)))


def wav_facts(path):
    """(kHz, channels, seconds) of a wav file; (44.1, 2, 0.0) on error."""
    try:
        with wave.open(path, 'rb') as wf:
            return wf.getframerate() / 1000.0, wf.getnchannels(), \
                wf.getnframes() / float(wf.getframerate())
    except Exception:
        return 44.1, 2, 0.0


def generate_fspro(out_dir, bank_name, events, strings, waits, muits, tg2ev,
                  wg2rec, audio_map, vanilla_fill=None, vanilla_events=None, evis=(), bank_obj=None,
                  model='Studio.02.02.00'):
    """FMOD Studio project: events with the original GUIDs and paths from strings,
    SingleSound/MultiSound instruments, AudioFile + Assets for the wavs.
    audio_map: (fsb, index) -> path of the already extracted wav."""
    meta = os.path.join(out_dir, 'Metadata')
    for d in ('Asset', 'AudioFile', 'Bank', 'BankFolder', 'EffectPresetFolder',
              'EncodingSetting', 'Event', 'EventFolder', 'Group',
              'ParameterPreset', 'ParameterPresetFolder', 'Platform', 'ProfilerFolder',
              'Return', 'SandboxFolder', 'Snapshot', 'SnapshotGroup', 'VCA'):
        os.makedirs(os.path.join(meta, d), exist_ok=True)
    os.makedirs(os.path.join(out_dir, 'Assets'), exist_ok=True)

    def W():
        return new_guid()

    ws_g, m_ef, m_tf, m_epf, m_pf, m_bf, m_sf, m_af = (W() for _ in range(8))
    mixer_g, prof_g, plat_g, snap_g, master_bus, bank_g = (W() for _ in range(6))

    open(os.path.join(out_dir, bank_name + '.fspro'), 'w', encoding='utf-8').write(
        '<?xml version="1.0" encoding="UTF-8"?>\n<objects serializationModel="%s" />\n' % model)
    open(os.path.join(meta, 'Workspace.xml'), 'w', encoding='utf-8').write(_xml(model,
        _xml_obj('Workspace', ws_g,
            _prop('builtBanksOutputDirectory', 'Build') + _prop('builtBanksSeparateAssets', 'true') +
            _prop('builtBanksMirrorBrowserFolderHierarchy', 'true') +
            _rel('masterEventFolder', m_ef) + _rel('masterTagFolder', m_tf) +
            _rel('masterEffectPresetFolder', m_epf) + _rel('masterParameterPresetFolder', m_pf) +
            _rel('masterBankFolder', m_bf) + _rel('masterSandboxFolder', m_sf) +
            _rel('masterAssetFolder', m_af) + _rel('mixer', mixer_g) +
            _rel('profilerSessionFolder', prof_g) + _rel('platforms', plat_g))))
    mef_chain, mef_pan, mef_fader = W(), W(), W()
    open(os.path.join(meta, 'Master.xml'), 'w', encoding='utf-8').write(_xml(model,
        _xml_obj('MixerMaster', master_bus,
                 _prop('name', 'Master Bus') + _rel('effectChain', mef_chain) +
                 _rel('panner', mef_pan) + _rel('mixer', mixer_g)),
        _xml_obj('MixerBusEffectChain', mef_chain, _rel('effects', mef_fader)),
        _xml_obj('MixerBusPanner', mef_pan, _prop('overridingOutputFormat', 6)),
        _xml_obj('MixerBusFader', mef_fader)))
    open(os.path.join(meta, 'Mixer.xml'), 'w', encoding='utf-8').write(_xml(model,
        _xml_obj('Mixer', mixer_g, _rel('masterBus', master_bus) + _rel('snapshotList', snap_g))))
    open(os.path.join(meta, 'Tags.xml'), 'w', encoding='utf-8').write(_xml(model,
        _xml_obj('MasterTagFolder', m_tf, _prop('name', 'Master'))))
    open(os.path.join(meta, 'SnapshotGroup', snap_g + '.xml'), 'w', encoding='utf-8').write(_xml(model,
        _xml_obj('SnapshotList', snap_g, _rel('mixer', mixer_g))))
    singletons = (('MasterAssetFolder', m_af, 'Asset', None),
                  ('MasterBankFolder', m_bf, 'BankFolder', None),
                  ('MasterEffectPresetFolder', m_epf, 'EffectPresetFolder', None),
                  ('MasterParameterPresetFolder', m_pf, 'ParameterPresetFolder', None),
                  ('MasterSandboxFolder', m_sf, 'SandboxFolder', None),
                  ('ProfilerSessionFolder', prof_g, 'ProfilerFolder', None),
                  ('MasterEventFolder', m_ef, 'EventFolder', 'Master'))
    for cls, g, folder, nm in singletons:
        open(os.path.join(meta, folder, g + '.xml'), 'w', encoding='utf-8').write(_xml(model,
            _xml_obj(cls, g, _prop('name', nm) if nm else '')))
    open(os.path.join(meta, 'Platform', plat_g + '.xml'), 'w', encoding='utf-8').write(_xml(model,
        _xml_obj('Platform', plat_g, _prop('hardwareType', 0) + _prop('name', 'Desktop') +
                 _prop('subDirectory', 'sound') + _prop('speakerFormat', 6))))
    enc_g = W()
    open(os.path.join(meta, 'EncodingSetting', enc_g + '.xml'), 'w', encoding='utf-8').write(_xml(model,
        _xml_obj('EncodingSetting', enc_g, _prop('encodingFormat', 3) + _prop('quality', 37) +
                 _rel('platform', plat_g) + _rel('encodable', plat_g))))
    open(os.path.join(meta, 'Bank', bank_g + '.xml'), 'w', encoding='utf-8').write(_xml(model,
        _xml_obj('Bank', bank_g, _prop('name', bank_name) + _rel('folder', m_bf))))

    # events -> instruments (same code for own events and for the vanilla backfill)
    folder_guids = {}
    preset_cache = {}
    audio_guids = {}
    counter = {'events': 0, 'audiofiles': 0}

    def ensure_folder(parts):
        parent = m_ef
        acc = ''
        for seg in parts:
            acc = acc + '/' + seg if acc else seg
            if acc not in folder_guids:
                folder_guids[acc] = W()
                open(os.path.join(meta, 'EventFolder', folder_guids[acc] + '.xml'),
                     'w', encoding='utf-8').write(_xml(model,
                    _xml_obj('EventFolder', folder_guids[acc],
                             _prop('name', seg) + _rel('folder', parent))))
            parent = folder_guids[acc]
        return parent

    asset_dirs = {}

    def ensure_asset_dir(rel_dir):
        """Folder under Assets/ -> EncodableAsset (without it Studio shows an empty asset tree)."""
        if not rel_dir or rel_dir in asset_dirs:
            return
        ensure_asset_dir(os.path.dirname(rel_dir).replace('\\', '/'))
        g = W()
        asset_dirs[rel_dir] = g
        open(os.path.join(meta, 'Asset', g + '.xml'), 'w', encoding='utf-8').write(_xml(model,
            _xml_obj('EncodableAsset', g, _prop('assetPath', rel_dir + '/') +
                     _rel('masterAssetFolder', m_af))))

    def sound_guid(epath, key, audio_map):
        if key not in audio_guids:
            ag = W()
            rel_path = epath.replace('event:/', '') + '/%03d.wav' % key[2]
            ensure_asset_dir(os.path.dirname(rel_path))
            dst = os.path.join(out_dir, 'Assets', *rel_path.split('/'))
            os.makedirs(os.path.dirname(dst), exist_ok=True)
            src = audio_map[key]
            if open(src, 'rb').read(4) != b'RIFF':
                # ogg (decoded by python-fsb5) -> PCM wav through ffmpeg, otherwise
                # Studio marks the asset as damaged
                subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-i', src,
                                '-c:a', 'pcm_s16le', dst], check=True)
            else:
                shutil.copy2(src, dst)
            hz, ch, dur = wav_facts(dst)
            open(os.path.join(meta, 'AudioFile', ag + '.xml'), 'w', encoding='utf-8').write(_xml(model,
                _xml_obj('AudioFile', ag,
                         _prop('assetPath', rel_path) + _prop('frequencyInKHz', '%.7f' % hz) +
                         _prop('channelCount', ch) + _prop('length', '%.10f' % dur) +
                         _rel('masterAssetFolder', m_af))))
            audio_guids[key] = ag
            counter['audiofiles'] += 1
        return audio_guids[key]

    def emit_event(eg, epath, ev_mods, audio_map, sheets=None):
        """ev_mods: [('S', [key]) | ('M', [keys])] — track instruments of the event in
        bank order; WAIT -> ('S', one sample), MUIT -> ('M', its playlist).
        sheets: [(paramGuid, (name, min, max), [[mod, ...], ...])] — parameter sheets."""
        parts = epath.replace('event:/', '').strip('/').split('/')
        parent = ensure_folder(parts[:-1])
        emix, mtrk, minp, aprops, mtrk2, tline = (W() for _ in range(6))
        emaster, ichain, ipan, gchain, gpan = (W() for _ in range(5))
        f1, f2 = W(), W()
        sounds_xml = ''
        multi_groups, group_tracks, group_xml = [], [], ''
        # Track modules keep the bank's instrument order and shape: a WAIT
        # (SingleSound) stays a SingleSound on the track, a MUIT becomes a
        # MultiSound whose playlist is exactly the MUIT's items. Wrapping
        # every sample group in a MultiSound turns a one-sample WAIT into a
        # MUIT in the built bank and two MUITs into one playlist, so the game
        # plays one random sound instead of both.
        for kind, keys in ev_mods:
            if kind == 'S':
                sg = W()
                sounds_xml += _xml_obj('SingleSound', sg,
                    _prop('length', '%g' % max(1.0, round(wav_facts(audio_map[keys[0]])[2], 3))) +
                    _rel('audioFile', sound_guid(epath, keys[0], audio_map)))
                multi_groups.append(sg)
            else:
                mg = W()
                gdests = []
                for key in keys:
                    sg = W()
                    gdests.append(sg)
                    sounds_xml += _xml_obj('SingleSound', sg,
                        _prop('length', '%g' % max(1.0, round(wav_facts(audio_map[key])[2], 3))) +
                        _rel('audioFile', sound_guid(epath, key, audio_map)))
                sounds_xml += _xml_obj('MultiSound', mg, _rel('sounds', *gdests))
                multi_groups.append(mg)
        params_rel = ''
        if sheets is None and bank_obj:
            # EVTB[0x5D] slots -> PMLB(owner): (param, items); see sheet_mods.
            sheets = sheet_mods(bank_obj.ev_slots.get(eg, []), bank_obj.pml, bank_obj.params,
                                waits, muits, wg2rec, audio_map)
        proxies = []
        proxy_xml = ''
        for pg, (pname, pmin, pmax), grps in (sheets or []):
            if pg not in preset_cache:
                gparam, gpreset = W(), W()
                preset_cache[pg] = (gparam, gpreset)
                open(os.path.join(meta, 'ParameterPreset', gpreset + '.xml'), 'w',
                     encoding='utf-8').write(_xml(model,
                    _xml_obj('ParameterPreset', gpreset, _prop('name', pname) +
                             _rel('folder', m_pf) + _rel('parameter', gparam)),
                    _xml_obj('GameParameter', gparam,
                             _prop('initialValue', '%g' % pmin) +
                             _prop('minimum', '%g' % pmin) + _prop('maximum', '%g' % pmax) +
                             _prop('isExposedRecursively', 'false'))))
            gparam, gpreset = preset_cache[pg]
            proxy = W()
            proxies.append(proxy)
            # A parameter sheet is the modules on the ParameterProxy (Gaijin
            # reference: ParameterProxy.modules -> MultiSound; 2607 events with
            # two or more proxies). A module on MasterTrack/Timeline is built
            # as a plain track module and leaves the PMLB slot empty, so the
            # event stays silent in game. preset must point at the
            # GameParameter or Studio drops the proxy ("Relationship 'preset'
            # expects a destination of entity type 'GameParameter'").
            # Every sheet module also hangs on a GroupTrack (reference: 1897 of
            # 1906 proxy-module events). The proxy binds the parameter, the
            # group track is the audio track the module plays on; without it
            # Studio marks the module invalid and drops it from the bank.
            proxy_modules = []
            for mods in grps:
                for kind, keys in mods:
                    if kind == 'W':
                        sg = W()
                        proxy_modules.append(sg)
                        sounds_xml += _xml_obj('SingleSound', sg,
                            _prop('length', '%g' % max(1.0, round(wav_facts(audio_map[keys[0]])[2], 3))) +
                            _rel('audioFile', sound_guid(epath, keys[0], audio_map)))
                    else:
                        mg = W()
                        proxy_modules.append(mg)
                        gdests = []
                        for key in keys:
                            sg = W()
                            gdests.append(sg)
                            sounds_xml += _xml_obj('SingleSound', sg,
                                _prop('length', '%g' % max(1.0, round(wav_facts(audio_map[key])[2], 3))) +
                                _rel('audioFile', sound_guid(epath, key, audio_map)))
                        sounds_xml += _xml_obj('MultiSound', mg, _rel('sounds', *gdests))
            proxy_xml += _xml_obj('ParameterProxy', proxy,
                                  _rel('modules', *proxy_modules) + _rel('preset', gparam))
            # one group track per parameter sheet ("layer00", "layer01", ...)
            gtrack, gmix, gchain2, gpan2, gfader = (W() for _ in range(5))
            group_tracks.append(gtrack)
            group_xml += _xml_obj('GroupTrack', gtrack,
                                  _rel('modules', *proxy_modules) + _rel('mixerGroup', gmix))
            group_xml += _xml_obj('EventMixerGroup', gmix,
                                  _prop('name', 'layer%02d' % (len(group_tracks) - 1)) +
                                  _rel('effectChain', gchain2) + _rel('panner', gpan2) +
                                  _rel('output', emaster))
            group_xml += _xml_obj('MixerBusEffectChain', gchain2, _rel('effects', gfader))
            group_xml += _xml_obj('MixerBusPanner', gpan2)
            group_xml += _xml_obj('MixerBusFader', gfader)
        if proxies:
            params_rel = _rel('parameters', *proxies)
        # Gaijin layout for a plain sound: the module sits on Timeline.modules
        # and on one GroupTrack ("Audio 1") that owns the mixer group; the
        # MasterTrack stays empty. A module placed only on MasterTrack is
        # built as a MUIT instead of the bank's WAIT.
        if multi_groups:
            gtrack, gmix, gchain2, gpan2, gfader = (W() for _ in range(5))
            group_tracks.insert(0, gtrack)
            group_xml = _xml_obj('GroupTrack', gtrack,
                                 _rel('modules', *multi_groups) + _rel('mixerGroup', gmix)) + \
                _xml_obj('EventMixerGroup', gmix, _prop('name', 'Audio 1') +
                         _rel('effectChain', gchain2) + _rel('panner', gpan2) +
                         _rel('output', emaster)) + \
                _xml_obj('MixerBusEffectChain', gchain2, _rel('effects', gfader)) + \
                _xml_obj('MixerBusPanner', gpan2) + \
                _xml_obj('MixerBusFader', gfader) + group_xml
        mods_rel = _rel('modules', *multi_groups) if multi_groups else ''
        groups_rel = _rel('groupTracks', *group_tracks)
        open(os.path.join(meta, 'Event', guid_str(eg) + '.xml'), 'w', encoding='utf-8').write(_xml(model,
            _xml_obj('Event', guid_str(eg), _prop('name', parts[-1]) + _prop('outputFormat', 2) +
                     _rel('folder', parent) + _rel('mixer', emix) + _rel('masterTrack', mtrk) +
                     _rel('mixerInput', minp) + _rel('automatableProperties', aprops) +
                     _rel('markerTracks', mtrk2) + groups_rel + _rel('timeline', tline) +
                     params_rel + _rel('banks', bank_g)),
            _xml_obj('EventMixer', emix, _rel('masterBus', emaster)),
            _xml_obj('MasterTrack', mtrk, _rel('mixerGroup', emaster)),
            _xml_obj('MixerInput', minp, _rel('effectChain', ichain) + _rel('panner', ipan) +
                     _rel('output', master_bus)),
            _xml_obj('EventAutomatableProperties', aprops),
            _xml_obj('MarkerTrack', mtrk2),
            _xml_obj('Timeline', tline, mods_rel),
            _xml_obj('EventMixerMaster', emaster, _rel('effectChain', gchain) +
                     _rel('panner', gpan) + _rel('mixer', emix)),
            _xml_obj('MixerBusEffectChain', ichain, _rel('effects', f1)),
            _xml_obj('MixerBusPanner', ipan),
            _xml_obj('MixerBusEffectChain', gchain, _rel('effects', f2)),
            _xml_obj('MixerBusPanner', gpan),
            _xml_obj('MixerBusFader', f1),
            _xml_obj('MixerBusFader', f2),
            proxy_xml + group_xml + sounds_xml))
        counter['events'] += 1

    ev_owner = event_owners(events, evis)

    def collect(eg, waits, muits, tg2ev, wg2rec, audio_map):
        """-> [mod] of event eg in instrument order: WAIT -> ('S', [key]),
        MUIT -> ('M', [keys of its playlist])."""
        def key(w):
            rec = wg2rec.get(w['wg'])
            return ('v', rec[0], rec[1]['index']) if rec and ('v', rec[0], rec[1]['index']) in audio_map else None
        mods = []
        for w in waits:
            if ev_owner.get(tg2ev.get(w['tg']), tg2ev.get(w['tg'])) != eg:
                continue
            k = key(w)
            if k:
                mods.append(('S', [k]))
        for m in muits:
            if ev_owner.get(tg2ev.get(m['tg']), tg2ev.get(m['tg'])) != eg:
                continue
            grp = []
            for it in m['items']:
                w = next((x for x in waits if x['ig'] == it), None)
                k = key(w) if w else None
                if k:
                    grp.append(k)
            if grp:
                mods.append(('M', grp))
        return mods

    # snapshots (snapshot:/…), buses and banks share the EVTS section with events;
    # they are not playable events and must not become Event objects
    for eg, epath in sorted(((e, strings[e]) for e in events
                             if e in strings and strings[e].startswith('event:/')), key=lambda kv: kv[1]):
        s = collect(eg, waits, muits, tg2ev, wg2rec, audio_map)
        sheets = None
        if (vanilla_fill or {}).get(eg):
            # the event is empty in the mod bank: sound and parameter sheets
            # come from vanilla
            s, sheets = vanilla_fill[eg]
        emit_event(eg, epath, s, audio_map, sheets=sheets)
    for ge, gp, s, sheets in (vanilla_events or []):
        emit_event(ge, gp, s, audio_map, sheets=sheets or None)

    return {'fspro': os.path.join(out_dir, bank_name + '.fspro'),
            'events': counter['events'], 'audiofiles': counter['audiofiles'],
            'events_without_name': len(events) - counter['events']}


def decode_game_fsbs(assets_path, out_root):
    """Decode every FSB5 of the paired assets bank into <out>/_game_audio/<bank>[N]/.
    -> ('g', fsb, index) -> file. Needs python-fsb5 (+libogg/libvorbis from pyogg)."""
    try:
        import fsb5
    except ImportError:
        print('!! python-fsb5 is not installed — provide vanilla wavs and pass --game-wav')
        return {}
    here = os.path.dirname(os.path.abspath(__file__))
    for src_dir in (os.path.join(here, 'bin'),):
        for dll in ('libogg.dll', 'libvorbis.dll'):
            src = os.path.join(src_dir, dll)
            if os.path.exists(src) and not os.path.exists(os.path.join(os.getcwd(), dll)):
                try:
                    shutil.copy2(src, dll)
                except OSError:
                    pass
    try:
        import pyogg
        for dll in ('libogg.dll', 'libvorbis.dll'):
            src = os.path.join(os.path.dirname(pyogg.__file__), dll)
            if os.path.exists(src) and not os.path.exists(os.path.join(here, 'bin', dll)):
                shutil.copy2(src, os.path.join(here, 'bin', dll))
                shutil.copy2(src, dll)
    except ImportError:
        pass
    from enum import IntEnum
    members = [(m.name, m.value) for m in fsb5.SoundFormat]
    if 'FADPCM' not in fsb5.SoundFormat.__members__:
        _ext = fsb5.SoundFormat.file_extension.fget
        _pcm = fsb5.SoundFormat.is_pcm.fget
        NewSF = IntEnum('SoundFormat', members + [('FADPCM', 16)])
        NewSF.file_extension = property(lambda s: 'wav' if s.value == 16 else _ext(s))
        NewSF.is_pcm = property(lambda s: s.value == 16 or _pcm(s))
        fsb5.SoundFormat = NewSF
    _, _, _, _, _, fsbs = parse_bank(assets_path)
    data = open(assets_path, 'rb').read()
    base = os.path.splitext(os.path.basename(assets_path))[0]
    out = {}
    for i, f in enumerate(fsbs):
        outdir = os.path.join(out_root, '_game_audio', '%s[%d]' % (base, i))
        os.makedirs(outdir, exist_ok=True)
        bank = fsb5.FSB5(data[f['offset']:f['offset'] + f['size']])
        for n, s in enumerate(bank.samples):
            try:
                blob = bank.rebuild_sample(s)
            except Exception as e:
                print('  !! decode %s[%d] #%d: %s' % (base, i, n, e))
                continue
            ext = fsb5.SoundFormat(int(bank.header.mode)).file_extension
            path = os.path.join(outdir, 'sound_%d.%s' % (n, ext))
            open(path, 'wb').write(blob)
            out[('g', i, n)] = path
        print('  decoded %s[%d]: %d' % (base, i, len(bank.samples)))
    return out

# ------------------------------------------------------------------- diff

def diff_against(bank_path, game_dir, strings):
    """Compare the bank with the current game bank: events by their strings paths."""
    ref_base = os.path.basename(bank_path)
    ref_bank = os.path.join(game_dir, ref_base)
    lines = ['=== diff: %s vs %s ===' % (ref_base, game_dir)]
    _, evts, _, _, _, _ = parse_bank(bank_path)
    local_paths = {strings.get(e) for e in evts}
    local_paths = {p for p in local_paths if p}
    if os.path.exists(ref_bank):
        ref_strings = parse_strings_bank(os.path.join(game_dir, 'masterbank.strings.bank'))
        _, rev, _, _, _, _ = parse_bank(ref_bank)
        ref_paths = {ref_strings.get(e) for e in rev if ref_strings.get(e)}
        missing = sorted(ref_paths - local_paths)
        extra = sorted(local_paths - ref_paths)
        lines.append('events in game: %d | in this bank: %d' % (len(ref_paths), len(local_paths)))
        lines.append('MISSING (in game, not in bank): %d' % len(missing))
        lines += ['  ' + p for p in missing[:300]]
        if len(missing) > 300:
            lines.append('  ... %d more' % (len(missing) - 300))
        lines.append('EXTRA (not in the current game): %d' % len(extra))
        lines += ['  ' + p for p in extra[:200]]
    else:
        lines.append('!! bank %s not found in %s (whole bank outdated)' % (ref_base, game_dir))
    return '\n'.join(lines)


# ------------------------------------------------------- mod workflow helpers

REFERENCE_REPO = 'https://github.com/GaijinEntertainment/fmod_studio_warthunder_for_modders.git'
REFERENCE_STUDIO = '2.02.22'


def _bank_event_params(bank_obj, ev):
    """Parameter names of an event (from its sheets) — for the catalog."""
    names = []
    for s in bank_obj.ev_slots.get(ev, []):
        for pg, _its in bank_obj.pml.get(s, []):
            n = bank_obj.params.get(pg, (guid_str(pg),))[0]
            if n not in names:
                names.append(n)
    return names


def catalog(game_dir, out_path=None, csv_path=None):
    """Catalog of every game bank: events, parameters, sample count -> Markdown (+CSV)."""
    strings = parse_strings_bank(os.path.join(game_dir, 'masterbank.strings.bank'))
    banks = sorted(p for p in os.listdir(game_dir)
                   if p.endswith('.bank') and not p.endswith(('.assets.bank', '.strings.bank')))
    rows, lines = [], ['# War Thunder sound banks', '',
                       'Generated by `rebank catalog`. One row per event; parameters are the',
                       'game parameters the event reacts to. Do not rename events, paths,',
                       'banks or mixer buses in a sound mod.', '']
    for name in banks:
        path = os.path.join(game_dir, name)
        base = name[:-5]
        try:
            b, events, _w, _m, wavs, _f = parse_bank(path)
        except Exception as e:  # noqa: BLE001 — catalog must not die on one bad bank
            lines.append('## %s — unreadable (%s)' % (base, e))
            continue
        assets = os.path.join(game_dir, base + '.assets.bank')
        n_wav = len(wavs)
        if os.path.exists(assets):
            try:
                n_wav = len(parse_bank(assets)[4])
            except Exception:  # noqa: BLE001
                pass
        named = [(strings[e], e) for e in events if e in strings and strings[e].startswith('event:/')]
        lines += ['## %s' % base, '',
                  '%d events (%d named), %d waveforms.' % (len(events), len(named), n_wav), '',
                  '| Event | Parameters |', '|---|---|']
        for p, e in sorted(named):
            ps = ', '.join(_bank_event_params(b, e))
            lines.append('| `%s` | %s |' % (p, ps))
            rows.append((base, p, ps))
        lines.append('')
    text = '\n'.join(lines)
    if out_path:
        os.makedirs(os.path.dirname(os.path.abspath(out_path)), exist_ok=True)
        open(out_path, 'w', encoding='utf-8', newline='\n').write(text)
        print('catalog:', out_path)
    if csv_path:
        with open(csv_path, 'w', newline='', encoding='utf-8-sig') as f:
            w = csv.writer(f)
            w.writerow(['bank', 'event', 'parameters'])
            w.writerows(rows)
        print('csv:', csv_path)
    if not out_path and not csv_path:
        print(text)
    return text


def required_banks_from_blk(text):
    """config/sound_studio.blk -> {'folder', 'extension', 'required': [...], 'optional': [...]}.
    The game switches the whole sound mod off when any bank of
    banks/presets/master without optional:b=true is missing from sound/mod/
    ("Sound.MOD disabled: modded bank is missing")."""
    tokens = re.findall(r'"[^"]*"|[{}]|[^\s{}"]+', text)
    stack = [[]]
    i = 0
    while i < len(tokens):
        t = tokens[i]
        if t == '{':
            # anonymous block: attach to the previous name when there is one
            i += 1
            continue
        if t == '}':
            if len(stack) > 1:
                stack.pop()
            i += 1
            continue
        if i + 1 < len(tokens) and tokens[i + 1] == '{':
            node = []
            stack[-1].append((t, node))
            stack.append(node)
            i += 2
            continue
        parts = []
        while i < len(tokens) and tokens[i] not in '{}':
            parts.append(tokens[i])
            i += 1
            if parts[-1] == '=':
                if i < len(tokens) and tokens[i] not in '{}':
                    parts.append(tokens[i])
                    i += 1
                break
            if parts[-1].startswith('='):
                break
        m = re.match(r'([\w.]+):([a-z]\w*)\s*=\s*(.*)', ''.join(parts))
        if m:
            stack[-1].append(('param', m.group(1), m.group(3).strip('"')))
    root = stack[0]

    def child(node, name):
        return next((n[1] for n in node if len(n) == 2 and n[0] == name), [])

    banks = child(root, 'banks')
    master = child(child(banks, 'presets'), 'master')
    req, opt = [], []
    for n in master:
        if len(n) != 2:
            continue
        optional = any(p == 'optional' and v == 'true' for q in n[1] if len(q) == 3 for p, v in [(q[1], q[2])])
        (opt if optional else req).append(n[0])
    params = {n[1]: n[2] for n in banks if len(n) == 3}
    return {'folder': params.get('folder', 'sound'), 'extension': params.get('extension', '.bank'),
            'required': req, 'optional': opt}


def check_mod(mod_dir, game_dir, studio_blk=None):
    """Check the built mod banks against the game: bank names, event names and their
    bank membership must not change (Gaijin rules), and the mod must be complete
    enough for the game to switch it on. -> (ok, report)

    studio_blk: text of config/sound_studio.blk (unpacked from aces.vromfs.bin).
    With it every non-optional bank of banks/presets/master must be present in
    mod_dir; without it the game sound folder is used: each shipped .bank whose
    pair <name>.assets.bank exists must come with that pair."""
    strings = parse_strings_bank(os.path.join(game_dir, 'masterbank.strings.bank'))
    problems = []
    warnings = []
    banks = sorted(p for p in os.listdir(mod_dir) if p.endswith('.bank') and not p.endswith('.assets.bank'))
    if not banks:
        return False, 'no .bank files in %s' % mod_dir
    if studio_blk:
        req = required_banks_from_blk(studio_blk)
        missing = [n + req['extension'] for n in req['required']
                   if not os.path.exists(os.path.join(mod_dir, n + req['extension']))]
        if missing:
            problems.append('%d required bank(s) missing: the game switches the whole mod off '
                            '("Sound.MOD disabled: modded bank is missing") until all of them are '
                            'present: %s' % (len(missing), ', '.join(missing[:8])
                                             + (' ...' if len(missing) > 8 else '')))
    for name in banks:
        ref = os.path.join(game_dir, name)
        if not os.path.exists(ref):
            problems.append('%s: bank does not exist in the game — the game will ignore it' % name)
            continue
        if not studio_blk and os.path.exists(os.path.join(game_dir, name[:-5] + '.assets.bank')) \
                and not os.path.exists(os.path.join(mod_dir, name[:-5] + '.assets.bank')):
            warnings.append('%s: the game ships %s.assets.bank; the mod has only the metadata half — '
                            'vanilla samples are used' % (name, name[:-5]))
        try:
            _, mine, _, _, _, _ = parse_bank(os.path.join(mod_dir, name))
            _, theirs, _, _, _, _ = parse_bank(ref)
        except Exception as e:  # noqa: BLE001
            problems.append('%s: unreadable (%s)' % (name, e))
            continue
        mine_paths = {strings.get(e) for e in mine if e in strings}
        their_paths = {strings.get(e) for e in theirs if e in theirs and strings.get(e)}
        lost = their_paths - mine_paths
        extra = mine_paths - their_paths
        if lost:
            problems.append('%s: %d event(s) missing vs game (rename breaks the mod): %s'
                            % (name, len(lost), ', '.join(sorted(lost)[:5])))
        if extra:
            problems.append('%s: %d event(s) not in the game bank (ignored or unknown): %s'
                            % (name, len(extra), ', '.join(sorted(extra)[:5])))
    ok = not problems
    lines = ['%s: %s' % ('OK' if ok else 'PROBLEMS', mod_dir)] + problems + ['warning: ' + w for w in warnings]
    return ok, '\n'.join(lines)


def init_mod(dest, reference=None, game_dir=None, clone=True):
    """Mod workspace on top of the official Gaijin project:
    <dest>/reference/ (clone of the repo or a local copy), <dest>/mod/sound/."""
    dest = os.path.abspath(dest)
    os.makedirs(dest, exist_ok=True)
    ref_dir = os.path.join(dest, 'reference')
    if not os.path.isdir(ref_dir):
        if reference and os.path.isdir(reference):
            shutil.copytree(reference, ref_dir, ignore=shutil.ignore_patterns('.git', '.cache', '.user'))
            print('reference: copied from %s' % reference)
        elif clone:
            r = subprocess.run(['git', 'clone', '--depth', '1', REFERENCE_REPO, ref_dir],
                               capture_output=True, text=True)
            if r.returncode != 0:
                print('!! git clone failed:', r.stderr.strip()[:200])
                return 1
            print('reference: cloned %s' % REFERENCE_REPO)
        else:
            print('!! no reference project at %s' % ref_dir)
            return 1
    readme = os.path.join(ref_dir, 'Readme.md')
    if os.path.exists(readme):
        m = re.search(r'Fmod Studio version\s*[-—]\s*([\d.]+)', open(readme, encoding='utf-8').read())
        ver = m.group(1) if m else '?'
        print('reference project: FMOD Studio %s (expected %s)%s'
              % (ver, REFERENCE_STUDIO, '' if ver == REFERENCE_STUDIO else '  !! version mismatch — update the clone'))
    mod_sound = os.path.join(dest, 'mod', 'sound')
    os.makedirs(mod_sound, exist_ok=True)
    notes = os.path.join(dest, 'mod', 'README.txt')
    if not os.path.exists(notes):
        open(notes, 'w', encoding='utf-8').write(
            'ReBank mod workspace\n'
            '====================\n\n'
            'reference/  official Gaijin FMOD Studio project (open sounds.fspro in FMOD Studio %s)\n'
            'mod/sound/  put built .bank (+ .assets.bank) files here; the game loads them\n'
            '            from <game>/sound/mod/ with enable_mod:b=yes in config.blk\n\n'
            'Rules (Gaijin): keep event names, folder layout, bank names and mixer\n'
            'buses unchanged.\n\n'
            'The game switches the whole mod off unless every bank it requires is present\n'
            'in sound/mod/<folder>/ (47 banks in the Sky Odyssey build: masterbank*, all\n'
            'aircraft_*, tanks_*, ships_* and their .assets pairs). Copy the vanilla banks\n'
            'you do not change unchanged and replace only the ones you rebuilt.\n\n'
            'Validate before sharing:  rebank check mod/sound "<game>/sound" --studio-blk <sound_studio.blk>\n'
            'Import vanilla events missing from the reference project (e.g. RWR alarms):\n'
            '  rebank "<game>/sound/aircraft_gui.bank" -a "<game>/sound/aircraft_gui.assets.bank" --fspro --apply\n'
            % REFERENCE_STUDIO)
    print('workspace: %s\n  reference: %s\n  mod banks: %s' % (dest, ref_dir, mod_sound))
    if game_dir:
        ok, report = check_mod(mod_sound, game_dir) if os.listdir(mod_sound) else (None, 'mod/sound is empty')
        if ok is False:
            print(report)
            return 1
    return 0
def _workflow_command(cmd, argv):
    sp = argparse.ArgumentParser(prog='rebank ' + cmd)
    if cmd == 'init':
        sp.add_argument('dest', help='workspace folder to create')
        sp.add_argument('--reference', help='local copy of the Gaijin project instead of git clone')
        sp.add_argument('--game', help='game sound dir: validate mod/sound right away')
        sp.add_argument('--no-clone', action='store_true', help='fail if no local reference is given')
        a = sp.parse_args(argv)
        return init_mod(a.dest, a.reference, a.game, clone=not a.no_clone)
    if cmd == 'check':
        sp.add_argument('mod_dir', help='folder with built mod .bank files (e.g. mod/sound)')
        sp.add_argument('--game', required=True, help='game sound dir to compare against')
        sp.add_argument('--studio-blk', help='config/sound_studio.blk unpacked from aces.vromfs.bin: '
                         'also verifies that every bank the game requires is present in mod_dir')
        a = sp.parse_args(argv)
        blk = open(a.studio_blk, encoding='utf-8', errors='replace').read() if a.studio_blk else None
        ok, report = check_mod(a.mod_dir, a.game, studio_blk=blk)
        print(report)
        return 0 if ok else 1
    # catalog
    sp.add_argument('game_dir', help='game sound dir')
    sp.add_argument('-o', '--out', help='write Markdown here (default: docs/EVENTS.md in cwd)')
    sp.add_argument('--csv', help='also write CSV')
    a = sp.parse_args(argv)
    catalog(a.game_dir, a.out or os.path.join('docs', 'EVENTS.md'), a.csv)
    return 0

def main():
    if len(sys.argv) > 1 and sys.argv[1] in ('init', 'check', 'catalog'):
        return _workflow_command(sys.argv[1], sys.argv[2:])
    ap = argparse.ArgumentParser(
        prog='rebank',
        description='Rebuild FMOD Studio .bank files: event names, samples, editable project. '
                    'Subcommands: init, check, catalog (see: rebank <cmd> -h).',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='example:\n  rebank aircraft_gui.bank --fspro --game "C:/Games/War Thunder/sound" --apply')
    ap.add_argument('bank', help='FMOD Studio .bank (FEV) file')
    ap.add_argument('-s', '--strings', help='*.strings.bank (default: masterbank.strings.bank next to the bank)')
    ap.add_argument('-a', '--assets',
                    help='paired X.assets.bank holding the samples (split-bank layout)')
    ap.add_argument('-o', '--out', help='output root (default: <bank>_unwrapped)')
    ap.add_argument('--csv', help='sample -> events report (default: <out>/<bank>_samples.csv)')
    ap.add_argument('--json', dest='json_out', help='name map (default: <out>/<bank>_names.json)')
    ap.add_argument('--rename-dir', action='append', default=[],
                    help='folder with pre-extracted sound_N.wav (repeat per FSB: [0], [1], ...)')
    ap.add_argument('--fsb-dir', help='folder with cut-out .fsb files (saved as <out>/fsb/N.fsb)')
    ap.add_argument('--fspro', action='store_true',
                    help='generate an FMOD Studio project (<out>/fspro/<bank>.fspro)')
    ap.add_argument('--diff', metavar='GAME_SOUND_DIR',
                    help='report: compare against the game\'s sound dir')
    ap.add_argument('--game', metavar='GAME_SOUND_DIR',
                    help='fill events missing or left empty in your bank from the game\'s sound dir (with --fspro)')
    ap.add_argument('--game-wav', action='append', default=[],
                    help='pre-extracted vanilla sound_N.wav folders (alternative to decoding)')
    ap.add_argument('--apply', action='store_true',
                    help='write files (without it only reports are written)')
    args = ap.parse_args()
    bank_path = args.bank
    strings_path = args.strings or os.path.join(
        os.path.dirname(os.path.abspath(bank_path)), 'masterbank.strings.bank')
    strings = {}
    if os.path.exists(strings_path):
        strings = parse_strings_bank(strings_path)
        print('strings: %d entries from %s' % (len(strings), strings_path))
    else:
        print('!! strings.bank not found (%s): names "?"' % strings_path)

    bank, events, waits, muits, wavs, fsbs = parse_bank(bank_path)
    if args.assets:
        # vanilla layout: events in X.bank, samples (WAVS+FSB) in X.assets.bank
        _, _, _, _, awavs, afsbs = parse_bank(args.assets)
        by_guid = {w['guid']: w for w in wavs}
        for w in awavs:
            if w['guid'] in by_guid:
                by_guid[w['guid']]['index'] = w['index']
            else:
                wavs.append(w)
        fsbs = afsbs
        bank.name = bank.name.replace('.assets', '')
        print('assets merged: %s (+%d waveforms, fsb=%d)' %
              (os.path.basename(args.assets), len(awavs), len(fsbs)))
    print('bank %s fmt=%#x: events=%d single=%d multi=%d waveforms=%d fsb=%d' %
          (bank.name, bank.fmt_version, len(events), len(waits), len(muits), len(wavs), len(fsbs)))

    sample_events, tg2ev, wg2rec = link_samples(events, waits, muits, wavs, getattr(bank, 'evis', ()))
    named = sum(1 for v in sample_events.values() if v)
    print('samples referenced: %d, named: %d' % (len(sample_events), named))

    # sample map for --fspro: ('v', fsb, index) -> source wav; backfill from the game: ('g', fsb, index)
    audio_map = {}
    vanilla_fill = {}    # mod event guid -> (mods, sheets) taken from the game bank
    vanilla_events = []  # game events absent from the mod bank: emitted as they are
    out_root = args.out or (os.path.splitext(bank_path)[0] + '_unwrapped')
    if args.fspro:
        for d_idx, d in enumerate(args.rename_dir):
            if not os.path.isdir(d):
                print('!! no folder', d)
                continue
            for f in os.listdir(d):
                m = re.match(r'sound_(\d+)\.wav$', f)
                if m:
                    audio_map.setdefault(('v', d_idx, int(m.group(1))), os.path.join(d, f))
        if not audio_map and fsbs:
            # no wavs of our own (Fmod Bank Tools was not run) — decode them ourselves
            audio_map = decode_game_fsbs(args.assets or bank_path, out_root)
            audio_map = {('v', k[1], k[2]): v for k, v in audio_map.items()}
        if args.game:
            gbank = os.path.join(args.game, os.path.basename(bank_path))
            gassets = os.path.splitext(gbank)[0] + '.assets.bank'
            if os.path.exists(gbank) and os.path.exists(gassets):
                gstrings = parse_strings_bank(os.path.join(args.game, 'masterbank.strings.bank'))
                gbank_obj, gevents, gwaits, gmuits, gwavs, _ = parse_bank(gbank)
                _, _, _, _, gawavs, _ = parse_bank(gassets)
                gwg2 = {}
                seen = defaultdict(int)
                gw = gwavs + gawavs
                for wrec in gw:
                    seen[wrec['index']] += 1
                    gwg2[wrec['guid']] = (seen[wrec['index']] - 1, wrec)
                _, gtg2ev, _ = link_samples(gevents, gwaits, gmuits, gw, gbank_obj.evis)
                # A mod event without instruments and without parameter sheets is an
                # untouched placeholder: take its sound from vanilla (vanilla_fill by the
                # mod event GUID). Events missing from the mod are emitted from vanilla
                # as they are (vanilla_events). A mod event is recognised by GUID or by
                # path (_by_path): an event recreated by the author carries a new GUID.
                _by_path = {strings[e]: e for e in events if strings.get(e, '').startswith('event:/')}
                _ev_owner = event_owners(events, getattr(bank, 'evis', ()))
                _tgs = [w['tg'] for w in waits] + [m['tg'] for m in muits]
                _filled = {_ev_owner.get(tg2ev.get(t), tg2ev.get(t)) for t in _tgs}
                _filled |= set(getattr(bank, 'ev_slots', {}))
                _filled.discard(None)
                n_fill = 0
                # vanilla wav/ogg: --game-wav folders (one per FSB of the assets bank);
                # if empty — decode through python-fsb5 (+libogg/libvorbis from pyogg)
                g_audio = {}
                for d_idx, d in enumerate(args.game_wav or []):
                    if not os.path.isdir(d):
                        continue
                    for f in os.listdir(d):
                        m = re.match(r'sound_(\d+)\.(wav|ogg)$', f)
                        if m:
                            g_audio.setdefault(('g', d_idx, int(m.group(1))), os.path.join(d, f))
                if not g_audio:
                    g_audio = decode_game_fsbs(gassets, out_root)
                van_dir = os.path.join(out_root, '_from_vanilla')
                ev_owner = event_owners(gevents, gbank_obj.evis)   # inner -> outer named
                for ge, gp in ((e, gstrings.get(e)) for e in gevents):
                    if not gp or not gp.startswith('event:/'):
                        continue  # no name
                    # the same event is recognised by GUID or by path: the mod author may
                    # have recreated the event (new GUID, same path) — Studio rejects a
                    # second copy with the same path at Build ("duplicate paths")
                    local = ge if ge in events else _by_path.get(gp)
                    if local is not None and local in _filled:
                        continue  # present in the mod with sound
                    # direct instruments + instruments of nested (unnamed) events
                    targets = [ge]
                    for inner, outer in ev_owner.items():
                        if outer == ge:
                            targets.append(inner)
                    mods = []
                    for tgt in targets:
                        for w in gwaits:
                            if gtg2ev.get(w['tg']) == tgt and (rec := gwg2.get(w['wg'])) and \
                                    ('g', rec[0], rec[1]['index']) in g_audio:
                                mods.append(('S', [('g', rec[0], rec[1]['index'])]))
                        for mrec in gmuits:
                            if gtg2ev.get(mrec['tg']) != tgt:
                                continue
                            grp = [('g', rec[0], rec[1]['index']) for it in mrec['items']
                                   if (w := next((x for x in gwaits if x['ig'] == it), None))
                                   and (rec := gwg2.get(w['wg'])) and ('g', rec[0], rec[1]['index']) in g_audio]
                            if grp:
                                mods.append(('M', grp))
                    sheets = sheet_mods(gbank_obj.ev_slots.get(ge, []), gbank_obj.pml, gbank_obj.params,
                                        gwaits, gmuits, gwg2, g_audio, prefix='g')
                    if local is not None:
                        vanilla_fill[local] = (mods, sheets)   # empty mod event — fill it
                    else:
                        vanilla_events.append((ge, gp, mods, sheets))  # absent from the mod — emit
                    for key in [k for _kind, ks in mods for k in ks] + \
                            [k for _pg, _pm, groups in sheets for grp in groups for _kd, ks in grp for k in ks]:
                        src = g_audio[key]
                        rel = gp.replace('event:/', '') + '/%03d_vanilla.wav' % key[2]
                        dst = os.path.join(van_dir, *rel.split('/'))
                        os.makedirs(os.path.dirname(dst), exist_ok=True)
                        shutil.copy2(src, dst)
                        audio_map[('g', key[1], key[2])] = dst
                    n_fill += 1
                print('vanilla backfill: %d events, %d wav' % (len(vanilla_fill) + len(vanilla_events), n_fill))
    out_root = args.out or (os.path.splitext(bank_path)[0] + '_unwrapped')
    os.makedirs(out_root, exist_ok=True)

    # CSV report
    csv_path = args.csv or os.path.join(out_root, bank.name + '_samples.csv')
    with open(csv_path, 'w', newline='', encoding='utf-8-sig') as f:
        w = csv.writer(f)
        w.writerow(['fsb', 'index', 'waveform_guid', 'field', 'events'])
        seen_idx = defaultdict(int)
        for wav in sorted(wavs, key=lambda x: x['index']):
            seen_idx[wav['index']] += 1
            fsb_i = seen_idx[wav['index']] - 1
            evs = sorted(strings.get(e, guid_str(e)) for e in sample_events.get((fsb_i, wav['index']), ()))
            w.writerow([fsb_i, wav['index'], guid_str(wav['guid']), wav['field'], ' | '.join(evs)])
    print('csv:', csv_path)

    # JSON map: "0_123" -> [event paths]
    json_path = args.json_out or os.path.join(out_root, bank.name + '_names.json')
    json.dump({'%d_%d' % k: sorted(strings.get(e, guid_str(e)) for e in v)
               for k, v in sample_events.items()},
              open(json_path, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print('json:', json_path)

    # FSB dump
    if args.fsb_dir:
        os.makedirs(args.fsb_dir, exist_ok=True)
        for i, fb in enumerate(fsbs):
            dst = os.path.join(args.fsb_dir, '%s[%d].fsb' % (bank.name, i))
            open(dst, 'wb').write(bank.data[fb['offset']:fb['offset']+fb['size']])
            print('fsb:', dst)

    # Lay sound_N.wav out along the event tree
    if args.rename_dir:
        copied = skipped = 0
        for d_idx, d in enumerate(args.rename_dir):
            if not os.path.isdir(d):
                print('!! no folder', d)
                continue
            for f in os.listdir(d):
                m = re.match(r'sound_(\d+)\.wav$', f)
                if not m:
                    continue
                idx = int(m.group(1))
                evs = sample_events.get((d_idx, idx)) or sample_events.get((0, idx))
                if not evs:
                    skipped += 1
                    continue
                primary = sorted(strings.get(e, guid_str(e)) for e in evs)[0]
                if primary.startswith('event:/'):
                    parts, leaf = event_rel_dir(primary)
                else:
                    # GUID event without a name in strings -> quarantine
                    parts, leaf = ['_unmatched'], primary
                sub = os.path.join(out_root, *parts) if parts else out_root
                dst = os.path.join(sub, '%03d_%s.wav' % (idx, leaf))
                os.makedirs(sub, exist_ok=True)
                src = os.path.join(d, f)
                if args.apply:
                    shutil.copy2(src, dst)
                    copied += 1
                else:
                    print('plan: %s -> %s' % (src, os.path.relpath(dst, out_root)))
        print('%s: %d files%s' % ('copied' if args.apply else 'plan', copied if args.apply else skipped,
                                   '' if args.apply else ' (without --apply this is only a plan)'))

    # FMOD Studio project
    if args.fspro:
        fspro_dir = os.path.join(out_root, 'fspro')
        info = generate_fspro(fspro_dir, bank.name.replace('.assets', '') or 'project',
                              events, strings, waits, muits, tg2ev, wg2rec, audio_map,
                              vanilla_fill=vanilla_fill, vanilla_events=vanilla_events,
                              evis=getattr(bank, 'evis', ()),
                              bank_obj=bank)
        print('fspro: %(fspro)s (events=%(events)d, audiofiles=%(audiofiles)d, '
              'events_without_name=%(events_without_name)d)' % info)

    # Diff against the current game version
    if args.diff:
        report = diff_against(bank_path, args.diff, strings)
        diff_path = os.path.join(out_root, bank.name + '_diff.txt')
        open(diff_path, 'w', encoding='utf-8').write(report)
        print('diff:', diff_path)
        print(report.splitlines()[1] if len(report.splitlines()) > 1 else report)
    print('done: %s' % out_root)


if __name__ == '__main__':
    sys.exit(main())
