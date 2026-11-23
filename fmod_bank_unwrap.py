#!/usr/bin/env python3
"""
fmod_bank_unwrap.py — разбор FMOD Studio .bank (FEV) с сохранением имён событий.

Идея: банк не хранит имена аудиофайлов. Имена восстанавливаются цепочкой
  strings.bank (GUID->путь) -> EVTB (событие) -> трек -> WAIT/MUIT (инструмент)
  -> WAIB (waveform) -> WAV (индекс сэмпла) -> FSB5 sound_N
и файлы раскладываются/переименовываются в <путь события>/<индекс>_<имя>.wav

Использование:
  python fmod_bank_unwrap.py BANK.bank [опции]

Опции:
  -s, --strings PATH     *.strings.bank (по умолчанию masterbank.strings.bank рядом)
  -o, --out DIR          корень вывода (по умолчанию <bank>_unwrapped)
  --csv PATH             CSV-отчёт (по умолчанию <out>/<bank>_samples.csv)
  --rename-dir DIR       папка с уже извлечёнными sound_N.wav (повторять по числу
                         FSB: сначала [0], потом [1]); с --apply файлы копируются
                         в дерево событий
  --fsb-dir DIR          папка с вырезанными .fsb (сохранить как <out>/fsb/N.fsb)
  --apply                выполнять копирование (без неё только отчёт)
  --json PATH            сохранить карту имён (по умолчанию <out>/<bank>_names.json)

Пример (War Thunder):
  python fmod_bank_unwrap.py RWSM/aircraft_gui.bank ^
      --rename-dir "FMOD Bank Tools/wav/aircraft_gui[0]" ^
      --rename-dir "FMOD Bank Tools/wav/aircraft_gui[1]" --apply
"""
import argparse
import csv
import json
import os
import re
import shutil
import struct
import sys
import subprocess
import uuid
import wave
from collections import defaultdict

# ------------------------------------------------------------------ RIFF/GUID

def walk_chunks(data, start, end):
    """(offset, fourcc, size, list_type) для RIFF-чанков в [start, end)."""
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
    """Массив IDA-ридера sub_1800AEFB0: varint n (raw>>1), затем u16 elemSize
    ОДИН раз (sub_1800BB510 при v5==0), затем n×elemSize байт. -> ([bytes...], new_off)"""
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
    """GUID (raw 16 байт) -> путь (event:/..., bus:/...)."""
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
    nv, off = read_varint(stdt, off)
    n = nv >> 1
    off += 2
    nodes = []
    for _ in range(n):
        v1 = struct.unpack('<I', stdt[off:off+4])[0]
        v2 = struct.unpack('<I', stdt[off+4:off+8])[0]
        nodes.append((v1 & 0xFFFFFF, v2 & 0xFFFFFF, (v2 >> 24) & 0xFF))
        off += 8
    gv, off = read_varint(stdt, off)
    g = gv >> 1
    off += 2
    guids = [stdt[off+16*i:off+16*i+16] for i in range(g)]
    off += 16 * g
    sl, off = read_varint(stdt, off)
    pool = stdt[off:off+sl]
    off += sl
    mc, off = read_varint(stdt, off)
    off += mc * 3
    pc, off = read_varint(stdt, off)
    parents = []
    for _ in range(pc):
        b3 = stdt[off:off+3]
        v = b3[0] | (b3[1] << 8) | (b3[2] << 16)
        parents.append(v if v != 0xFFFFFF else -1)
        off += 3
    out = {}
    for idx, (so, cg, cc) in enumerate(nodes):
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
            raise ValueError('%s: не FMOD FEV bank' % path)
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
        """Обход LIST list_tag { item_tag: subchunks... } с выбранными полями."""
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
    evis = []    # event instruments: (targetEventGuid, ownerTrackGuid) — вложенные события
    for rec in bank.items('LISTEVIS', b'EVIT', {b'EVIB', b'INST'}):
        evib, inst = rec.get(b'EVIB'), rec.get(b'INST')
        if evib and inst:
            evis.append((evib[16:32], inst[0:16]))
    bank.evis = evis
    # параметрические листы (ActionSheet): PMLB.owner — слот события на EVTB[0x5D],
    # paramGuid — параметр (track/intense/volume), items — WAIT.ig / MUIT / scatterer.
    # Курсор EVTB (ридер sub_1800ABC30): 0x5D varint n, затем u16 elemSize ОДИН раз,
    # затем n×elemSize байт (sub_1800AEFB0 → sub_1800BB510(v5=0) один раз).
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
    """inner eventGuid -> outer eventGuid через EVIS: инструмент лежит на треке
    outer (EVTB[0x20]/[0x40]) и играет inner (EVIB[16:32])."""
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
    Инструменты (WAIT/MUIT) сидят на event-mixer треке события — в EVTB это
    outputBusGuid (0x20), у каждого события свой. Плейлисты с нулевым trackGuid
    событиям не принадлежат (параметрические, пропускаем). Инструменты
    безымянных inner-событий (EVIS) приписываются их outer-владельцу."""
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
        # при дублировании индекса k второе вхождение строки WAV относится
        # к следующему FSB-контейнеру (порядок сериализации FMOD)
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
    """GUID инструмента из PMLB.items -> ключи сэмплов: WAIT.ig -> сэмпл,
    MUIT (по MUIB guid или tg) -> сэмплы его плейлиста. Только те, что есть в audio_map."""
    ig2w = {w['ig']: w for w in waits}
    keys = []
    w = ig2w.get(item)
    if w:
        rec = wg2rec.get(w['wg'])
        if rec and (prefix, rec[0], rec[1]['index']) in audio_map:
            keys.append((prefix, rec[0], rec[1]['index']))
        return keys
    for m in muits:
        if item in (m.get('guid'), m['tg']):
            for it in m['items']:
                w = ig2w.get(it)
                rec = wg2rec.get(w['wg']) if w else None
                if rec and (prefix, rec[0], rec[1]['index']) in audio_map:
                    keys.append((prefix, rec[0], rec[1]['index']))
    return keys


# ------------------------------------------------------------------ renaming

BAD = re.compile(r'[<>:"/\\|?*\x00-\x1f]')


def safe_name(s):
    s = BAD.sub('_', s).strip(' .')
    return s or 'unnamed'


def event_rel_dir(path):
    """event:/a/b/c -> ('a/b/c-папка' без последнего сегмента, имя)."""
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
    ds = ''.join('\t\t\t<destination>%s</destination>\n' % d for d in dests)
    return '\t\t<relationship name="%s">\n%s\t\t</relationship>\n' % (name, ds)


def _xml(model, *objs):
    return ('<?xml version="1.0" encoding="UTF-8"?>\n'
            '<objects serializationModel="%s">\n%s</objects>\n' % (model, ''.join(objs)))


def wav_facts(path):
    """(кГц, каналы, секунды) wav-файла; (44.1, 2, 0.0) при ошибке."""
    try:
        with wave.open(path, 'rb') as wf:
            return wf.getframerate() / 1000.0, wf.getnchannels(), \
                wf.getnframes() / float(wf.getframerate())
    except Exception:
        return 44.1, 2, 0.0


def generate_fspro(out_dir, bank_name, events, strings, waits, muits, tg2ev,
                  wg2rec, audio_map, vanilla_events=None, evis=(), bank_obj=None,
                  model='Studio.02.02.00'):
    """Открытый проект FMOD Studio: события с оригинальными GUID и путями из
    strings, инструменты SingleSound/MultiSound, AudioFile + Assets для wav.
    audio_map: (fsb, index) -> путь к уже извлечённому wav."""
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

    # события -> инструменты (одинаковый код для своих событий и добора из ванилы)
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
        """Папка в Assets/ -> EncodableAsset (иначе дерево ассетов в Studio пустое)."""
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
                # ogg (декод python-fsb5) -> PCM wav через ffmpeg, иначе Studio
                # пометит ассет как повреждённый
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

    def emit_event(eg, epath, ev_waits, ev_multi, audio_map, sheets=None):
        """ev_waits: [key], ev_multi: [[key], ...] — собранные ключи сэмплов.
        sheets: [(paramGuid, (name, min, max), [[key], ...])] — параметрические листы."""
        parts = epath.replace('event:/', '').strip('/').split('/')
        parent = ensure_folder(parts[:-1])
        emix, mtrk, minp, aprops, mtrk2, tline = (W() for _ in range(6))
        emaster, ichain, ipan, gchain, gpan = (W() for _ in range(5))
        f1, f2 = W(), W()
        sounds_xml = ''
        multi_groups = []
        for keys in ([ev_waits] if ev_waits else []) + list(ev_multi):
            # каждый сэмпл — SingleSound; все сэмплы одной группы уходят в один
            # MultiSound-плейлист, иначе «лишние» SingleSound остаются без
            # владельца (dangling) и Studio помечает событие как malformed
            mg = W()
            multi_groups.append(mg)
            gdests = []
            for key in keys:
                sg = W()
                gdests.append(sg)
                sounds_xml += _xml_obj('SingleSound', sg,
                    _prop('length', '%g' % max(1.0, round(wav_facts(audio_map[key])[2], 3))) +
                    _rel('audioFile', sound_guid(epath, key, audio_map)))
            sounds_xml += _xml_obj('MultiSound', mg, _rel('sounds', *gdests))
        mods_rel = _rel('modules', *multi_groups) if multi_groups else ''
        params_rel = ''
        # параметрический лист (ActionSheet): EVTB[0x5D] слоты -> PMLB(owner) ->
        # параметр + инструменты. Каждый слот = свой диапазон параметра
        # (ParameterCondition) и свой MultiSound; всё вешается на ParameterProxy.
        if sheets is None and bank_obj:
            # слоты EVTB[0x5D] -> PMLB(owner): (param, items). Слоты одного события
            # могут задавать РАЗНЫЕ параметры (track/volume/launch/new) — один
            # ParameterProxy на параметр; несколько PMLB одного параметра = его группы.
            merged = {}
            for s in bank_obj.ev_slots.get(eg, []):
                for pg, its in bank_obj.pml.get(s, []):
                    grp = [k for it in its
                           for k in instrument_keys(it, waits, muits, wg2rec, audio_map)]
                    if grp:
                        merged.setdefault(pg, []).append(grp)
            sheets = [(pg, bank_obj.params.get(pg, (guid_str(pg), 0.0, 1.0, 0.0))[:3], grps)
                      for pg, grps in merged.items()]
        proxies = []
        for pg, (pname, pmin, pmax), grps in (sheets or []):
            if pg not in preset_cache:
                gparam, gpreset = W(), W()
                preset_cache[pg] = gpreset
                open(os.path.join(meta, 'ParameterPreset', gpreset + '.xml'), 'w',
                     encoding='utf-8').write(_xml(model,
                    _xml_obj('ParameterPreset', gpreset, _prop('name', pname) +
                             _rel('folder', m_pf) + _rel('parameter', gparam)),
                    _xml_obj('GameParameter', gparam,
                             _prop('initialValue', '%g' % pmin) +
                             _prop('minimum', '%g' % pmin) + _prop('maximum', '%g' % pmax) +
                             _prop('isExposedRecursively', 'false'))))
            gpreset = preset_cache[pg]
            proxy = W()
            proxies.append(proxy)
            pmods = []
            for keys in grps:
                mg = W()
                pmods.append(mg)
                gdests = []
                for key in keys:
                    sg = W()
                    gdests.append(sg)
                    sounds_xml += _xml_obj('SingleSound', sg,
                        _prop('length', '%g' % max(1.0, round(wav_facts(audio_map[key])[2], 3))) +
                        _rel('audioFile', sound_guid(epath, key, audio_map)))
                sounds_xml += _xml_obj('MultiSound', mg, _rel('sounds', *gdests))
            sounds_xml += _xml_obj('ParameterProxy', proxy,
                _rel('modules', *pmods) + _rel('preset', gpreset))
        if proxies:
            params_rel = _rel('parameters', *proxies)
        open(os.path.join(meta, 'Event', guid_str(eg) + '.xml'), 'w', encoding='utf-8').write(_xml(model,
            _xml_obj('Event', guid_str(eg), _prop('name', parts[-1]) + _prop('outputFormat', 2) +
                     _rel('folder', parent) + _rel('mixer', emix) + _rel('masterTrack', mtrk) +
                     _rel('mixerInput', minp) + _rel('automatableProperties', aprops) +
                     _rel('markerTracks', mtrk2) + _rel('timeline', tline) +
                     params_rel + _rel('banks', bank_g)),
            _xml_obj('EventMixer', emix, _rel('masterBus', emaster)),
            _xml_obj('MasterTrack', mtrk, mods_rel + _rel('mixerGroup', emaster)),
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
            sounds_xml))
        counter['events'] += 1

    ev_owner = event_owners(events, evis)

    def collect(eg, waits, muits, tg2ev, wg2rec, audio_map):
        """-> (single_keys, [multi_key_groups]) события eg."""
        singles = []
        for w in waits:
            if ev_owner.get(tg2ev.get(w['tg']), tg2ev.get(w['tg'])) != eg:
                continue
            rec = wg2rec.get(w['wg'])
            if rec and ('v', rec[0], rec[1]['index']) in audio_map:
                singles.append(('v', rec[0], rec[1]['index']))
        multis = []
        for m in muits:
            if ev_owner.get(tg2ev.get(m['tg']), tg2ev.get(m['tg'])) != eg:
                continue
            grp = []
            for it in m['items']:
                w = next((x for x in waits if x['ig'] == it), None)
                if not w:
                    continue
                rec = wg2rec.get(w['wg'])
                if rec and ('v', rec[0], rec[1]['index']) in audio_map:
                    grp.append(('v', rec[0], rec[1]['index']))
            if grp:
                multis.append(grp)
        return singles, multis

    for eg, epath in sorted(((e, strings[e]) for e in events if e in strings), key=lambda kv: kv[1]):
        s, m = collect(eg, waits, muits, tg2ev, wg2rec, audio_map)
        emit_event(eg, epath, s, m, audio_map)
    for ge, gp, s, mlt, sheets in (vanilla_events or []):
        emit_event(ge, gp, s, mlt, audio_map, sheets=sheets or None)

    return {'fspro': os.path.join(out_dir, bank_name + '.fspro'),
            'events': counter['events'], 'audiofiles': counter['audiofiles'],
            'events_without_name': len(events) - counter['events']}


def decode_game_fsbs(assets_path, out_root):
    """Декодировать все FSB5 парного assets-банка в <out>/_game_audio/<bank>[N]/.
    Возвращает ('g', fsb, index) -> файл. Нужен python-fsb5 (+libogg/libvorbis из pyogg)."""
    try:
        import fsb5
    except ImportError:
        print('!! python-fsb5 не установлен — положите ванильные wav и укажите --game-wav')
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
    """Сверка банка с актуальным банком игры: события по путям strings."""
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
        lines.append('событий в игре: %d | в этом банке: %d' % (len(ref_paths), len(local_paths)))
        lines.append('НЕ ХВАТАЕТ (есть в игре, нет в банке): %d' % len(missing))
        lines += ['  ' + p for p in missing[:300]]
        if len(missing) > 300:
            lines.append('  ... ещё %d' % (len(missing) - 300))
        lines.append('ЛИШНИЕ (нет в текущей игре): %d' % len(extra))
        lines += ['  ' + p for p in extra[:200]]
    else:
        lines.append('!! банка %s нет в %s (устарел весь банк)' % (ref_base, game_dir))
    return '\n'.join(lines)
def main():
    ap = argparse.ArgumentParser(
        description='FMOD .bank unwrap: имена событий -> раскладка сэмплов',
        formatter_class=argparse.RawDescriptionHelpFormatter, epilog=__doc__.split('Опции:')[-1])
    ap.add_argument('bank')
    ap.add_argument('-s', '--strings')
    ap.add_argument('-a', '--assets',
                    help='парный X.assets.bank с сэмплами (формат ванильных банков игры)')
    ap.add_argument('-o', '--out')
    ap.add_argument('--csv')
    ap.add_argument('--json', dest='json_out')
    ap.add_argument('--rename-dir', action='append', default=[])
    ap.add_argument('--fsb-dir')
    ap.add_argument('--fspro', action='store_true',
                    help='сгенерировать проект FMOD Studio (<out>/<bank>.fspro)')
    ap.add_argument('--diff', metavar='GAME_SOUND_DIR',
                    help='отчёт: сверка с банком игры (папка sound)')
    ap.add_argument('--game', metavar='GAME_SOUND_DIR',
                    help='добор недостающих событий из ванильного банка игры (с --fspro)')
    ap.add_argument('--game-wav', action='append', default=[],
                    help='папки ванильных sound_N.wav (после Extract в Fmod Bank Tools)')
    ap.add_argument('--apply', action='store_true')
    args = ap.parse_args()
    bank_path = args.bank
    strings_path = args.strings or os.path.join(
        os.path.dirname(os.path.abspath(bank_path)), 'masterbank.strings.bank')
    strings = {}
    if os.path.exists(strings_path):
        strings = parse_strings_bank(strings_path)
        print('strings: %d записей из %s' % (len(strings), strings_path))
    else:
        print('!! strings.bank не найден (%s): имена "?"' % strings_path)

    bank, events, waits, muits, wavs, fsbs = parse_bank(bank_path)
    if args.assets:
        # ванильный формат: события в X.bank, сэмплы (WAVS+FSB) в X.assets.bank
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

    # карта сэмплов для --fspro: ('v', fsb, index) -> исходный wav; добор из игры: ('g', fsb, index)
    audio_map = {}
    vanilla_events = []
    out_root = args.out or (os.path.splitext(bank_path)[0] + '_unwrapped')
    if args.fspro:
        for d_idx, d in enumerate(args.rename_dir):
            if not os.path.isdir(d):
                print('!! нет папки', d)
                continue
            for f in os.listdir(d):
                m = re.match(r'sound_(\d+)\.wav$', f)
                if m:
                    audio_map.setdefault(('v', d_idx, int(m.group(1))), os.path.join(d, f))
        if not audio_map and fsbs:
            # своих wav нет (Fmod Bank Tools не прогоняли) — декодируем сами
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
                local_paths = {strings.get(e) for e in events}
                n_fill = 0
                # ванильные wav/ogg: папки --game-wav (по числу FSB assets-банка);
                # если пусто — декодируем сами через python-fsb5 (+libogg/libvorbis из pyogg)
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
                # вложенные события: EVIT { EVIB.targetGuid, INST.trackGuid }:
                # безымянное inner-событие играется внутри именованного outer
                g_nested = defaultdict(set)   # inner event guid -> outer track guids
                for rec in gbank_obj.items('LISTEVIS', b'EVIT', {b'EVIB', b'INST'}):
                    evib, inst = rec.get(b'EVIB'), rec.get(b'INST')
                    if not evib or not inst:
                        continue
                    g_nested[evib[16:32]].add(inst[0:16])
                ev_owner = {}   # inner event guid -> outer named event guid
                for inner_eg, tgs in g_nested.items():
                    for tg in tgs:
                        for oe, body in gevents.items():
                            if tg in body or body[0x40:0x50] == tg:
                                if gstrings.get(oe):
                                    ev_owner[inner_eg] = oe
                                break
                for ge, gp in ((e, gstrings.get(e)) for e in gevents):
                    if not gp or gp in local_paths:
                        continue  # есть в моде или без имени
                    # прямые инструменты + инструменты вложенных (unnamed) событий
                    targets = [ge]
                    for inner, outer in ev_owner.items():
                        if outer == ge:
                            targets.append(inner)
                    s, mlt = [], []
                    for tgt in targets:
                        for w in gwaits:
                            if gtg2ev.get(w['tg']) != tgt:
                                continue
                            rec = gwg2.get(w['wg'])
                            if rec and ('g', rec[0], rec[1]['index']) in g_audio:
                                s.append(('g', rec[0], rec[1]['index']))
                        for mrec in gmuits:
                            if gtg2ev.get(mrec['tg']) != tgt:
                                continue
                            grp = []
                            for it in mrec['items']:
                                w = next((x for x in gwaits if x['ig'] == it), None)
                                rec = gwg2.get(w['wg']) if w else None
                                if rec and ('g', rec[0], rec[1]['index']) in g_audio:
                                    grp.append(('g', rec[0], rec[1]['index']))
                            if grp:
                                mlt.append(grp)
                    merged = {}
                    for sl in gbank_obj.ev_slots.get(ge, []):
                        for pg, its in gbank_obj.pml.get(sl, []):
                            grp = [k for it in its
                                   for k in instrument_keys(it, gwaits, gmuits, gwg2, g_audio, prefix='g')]
                            if grp:
                                merged.setdefault(pg, []).append(grp)
                    sheets = [(pg, gbank_obj.params.get(pg, (guid_str(pg), 0.0, 1.0, 0.0))[:3], grps)
                              for pg, grps in merged.items()]
                    vanilla_events.append((ge, gp, s, mlt, sheets))
                    for key in s + [k for grp in mlt for k in grp] + \
                            [k for _pg, _pm, grps in sheets for grp in grps for k in grp]:
                        src = g_audio[key]
                        rel = gp.replace('event:/', '') + '/%03d_vanilla.wav' % key[2]
                        dst = os.path.join(van_dir, *rel.split('/'))
                        os.makedirs(os.path.dirname(dst), exist_ok=True)
                        shutil.copy2(src, dst)
                        audio_map[('g', key[1], key[2])] = dst
                    n_fill += 1
                print('vanilla backfill: %d событий, %d wav' % (n_fill, len(vanilla_events)))
    out_root = args.out or (os.path.splitext(bank_path)[0] + '_unwrapped')
    os.makedirs(out_root, exist_ok=True)

    # CSV-отчёт
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

    # JSON-карта: "0_123" -> [event paths]
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

    # Раскладка sound_N.wav по дереву событий
    if args.rename_dir:
        copied = skipped = 0
        for d_idx, d in enumerate(args.rename_dir):
            if not os.path.isdir(d):
                print('!! нет папки', d)
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
                    # GUID-событие без имени в strings -> карантин
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
        print('%s: %d файлов%s' % ('скопировано' if args.apply else 'план', copied if args.apply else skipped,
                                   '' if args.apply else ' (без --apply только план)'))

    # Проект FMOD Studio
    if args.fspro:
        fspro_dir = os.path.join(out_root, 'fspro')
        info = generate_fspro(fspro_dir, bank.name.replace('.assets', '') or 'project',
                              events, strings, waits, muits, tg2ev, wg2rec, audio_map,
                              vanilla_events=vanilla_events, evis=getattr(bank, 'evis', ()),
                              bank_obj=bank)
        print('fspro: %(fspro)s (events=%(events)d, audiofiles=%(audiofiles)d, '
              'events_without_name=%(events_without_name)d)' % info)

    # Diff с актуальной версией игры
    if args.diff:
        report = diff_against(bank_path, args.diff, strings)
        diff_path = os.path.join(out_root, bank.name + '_diff.txt')
        open(diff_path, 'w', encoding='utf-8').write(report)
        print('diff:', diff_path)
        print(report.splitlines()[1] if len(report.splitlines()) > 1 else report)
    print('done: %s' % out_root)


if __name__ == '__main__':
    main()
