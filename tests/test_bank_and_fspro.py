"""End-to-end tests on synthetic FEV banks, .fspro output, catalog, CLI, and doc scripts.

Run:  python -m unittest tests.test_bank_and_fspro -v
No game assets required.
"""
import os
import struct
import subprocess
import sys
import tempfile
import unittest
import wave
import xml.etree.ElementTree as ET

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)
sys.path.insert(0, os.path.join(ROOT, 'scripts'))

import sound_refs as SR  # noqa: E402
import vehicle_table as VT  # noqa: E402

import rebank as U  # noqa: E402


def _chunk(cid, payload):
    pad = b'\x00' if (len(payload) & 1) else b''
    return cid + struct.pack('<I', len(payload)) + payload + pad


def _list_chunk(ltype, *children):
    body = ltype + b''.join(children)
    return _chunk(b'LIST', body)


def _pack_array(items):
    if not items:
        return struct.pack('<H', 0)
    es = len(items[0])
    assert all(len(x) == es for x in items)
    return struct.pack('<HH', len(items) << 1, es) + b''.join(items)


def _evtb(ev_guid, out_bus, master_track, slots=()):
    buf = bytearray(0x5D)
    buf[0x00:0x10] = ev_guid
    buf[0x10:0x20] = b'\xaa' * 16
    buf[0x20:0x30] = out_bus
    buf[0x30:0x40] = b'\xbb' * 16
    buf[0x40:0x50] = master_track
    struct.pack_into('<II', buf, 0x50, 1, 0)
    struct.pack_into('<I', buf, 0x59, 0)
    return bytes(buf) + _pack_array(list(slots))


def _make_wav(path, frames=4410, rate=44100):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with wave.open(path, 'wb') as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(rate)
        wf.writeframes(b'\x00\x00' * frames)


def _build_strings_bank(entries):
    """Build minimal STDT bank for [(guid16, path), ...]."""
    nodes = [(0xFFFFFF, 0xFFFFFF, len(entries))]
    parents = [0xFFFFFF]
    guids = []
    pool = bytearray()
    for gi, (guid, path) in enumerate(entries):
        guids.append(guid)
        off = len(pool)
        pool.extend(path.encode('utf-8') + b'\x00')
        nodes.append((off, gi, 0))
        parents.append(0)
    node_recs = [struct.pack('<II', so & 0xFFFFFF, (cg & 0xFFFFFF) | (cc << 24)) for so, cg, cc in nodes]
    u24 = lambda v: bytes((v & 0xFF, (v >> 8) & 0xFF, (v >> 16) & 0xFF))  # noqa: E731
    tail = struct.pack('<H', 0) + struct.pack('<H', len(parents)) + b''.join(u24(p) for p in parents)
    stdt = struct.pack('<I', 1) + _pack_array(node_recs) + _pack_array(guids) \
        + struct.pack('<H', len(pool)) + bytes(pool) + tail
    proj = _list_chunk(b'PROJ', _chunk(b'STDT', stdt))
    return b'RIFF' + struct.pack('<I', 4 + len(proj)) + b'FEV ' + proj


def _build_fev_bank(fmt_version=0x8E, events=(), waits=(), muits=(), wavs=(), evis=(), params=(), pmls=()):
    fmt = _chunk(b'FMT ', struct.pack('<II', fmt_version, 0))
    evts = _list_chunk(b'EVTS', *[_list_chunk(b'EVNT', _chunk(b'EVTB', b)) for b in events])
    wais = _list_chunk(b'WAIS', *[
        _list_chunk(b'WAIT', _chunk(b'WAIB', ig + wg), _chunk(b'INST', tg))
        for ig, wg, tg in waits
    ])
    muis = _list_chunk(b'MUIS', *[
        _list_chunk(
            b'MUIT',
            _chunk(b'MUIB', mg),
            _chunk(b'PLST', b'\x00' * 8 + struct.pack('<HH', len(items) << 1, 20) + b''.join(it + b'\x00' * 4 for it in items)),
            _chunk(b'INST', tg),
        )
        for mg, items, tg in muits
    ])
    wavc = _list_chunk(b'WAVS', *[
        _chunk(b'WAV ', wg + struct.pack('<IIIH', 0, idx << 16, 1, 0))
        for wg, idx in wavs
    ])
    evic = _list_chunk(b'EVIS', *[
        _list_chunk(b'EVIT', _chunk(b'EVIB', b'\x00' * 16 + inner), _chunk(b'INST', tg))
        for inner, tg in evis
    ])
    prmc = _list_chunk(b'PRMS', *[
        _list_chunk(b'PARM', _chunk(b'PRMB', pg + b'\x00' * 8 + struct.pack('<H', len(name.encode('utf-8')))
                                    + name.encode('utf-8') + struct.pack('<fff', pmin, pmax, pdef)))
        for pg, name, pmin, pmax, pdef in params
    ])
    pmlc = _list_chunk(b'PMLS', *[
        _list_chunk(b'PMLO', _chunk(b'PMLB', owner + pg + _pack_array(items)))
        for owner, pg, items in pmls
    ])
    proj = _list_chunk(b'PROJ', evts, wais, muis, wavc, evic, prmc, pmlc)
    return b'RIFF' + struct.pack('<I', 4 + len(fmt) + len(proj)) + b'FEV ' + fmt + proj


def _g(n):
    return bytes([n]) * 16


class BankParsingAndFspro(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = self.tmp.name

    def tearDown(self):
        self.tmp.cleanup()

    def test_synthetic_bank_parse_link_fspro_and_diff(self):
        ev1, bus1, ig1, wg1 = _g(1), _g(2), _g(3), _g(4)
        ev2, bus2, mg2, ig2, wg2 = _g(5), _g(6), _g(7), _g(8), _g(9)
        ev_outer, bus_outer, ev_inner, tg_inner, ig_inner, wg_inner = _g(10), _g(11), _g(12), _g(13), _g(14), _g(15)
        slot1, pg1, ig_sheet, wg_sheet = _g(16), _g(17), _g(18), _g(19)
        snap_guid = _g(20)

        strings_bytes = _build_strings_bank([
            (ev1, 'event:/aircraft/gui/alarm_rwr & test'),
            (ev2, 'event:/aircraft/gui/multi'),
            (ev_outer, 'event:/aircraft/gui/outer'),
            (snap_guid, 'snapshot:/ignore_me'),
        ])
        bank_bytes = _build_fev_bank(
            events=[
                _evtb(ev1, bus1, _g(91), slots=[slot1]),
                _evtb(ev2, bus2, _g(92)),
                _evtb(ev_outer, bus_outer, _g(93)),
                _evtb(ev_inner, tg_inner, _g(94)),
                _evtb(snap_guid, _g(95), _g(96)),
            ],
            waits=[
                (ig1, wg1, bus1),
                (ig2, wg2, _g(0)),
                (ig_inner, wg_inner, tg_inner),
                (ig_sheet, wg_sheet, _g(0)),
            ],
            muits=[(mg2, [ig2], bus2)],
            wavs=[(wg1, 0), (wg2, 1), (wg_inner, 2), (wg_sheet, 0)],  # idx 0 repeats -> fsb 1
            evis=[(ev_inner, bus_outer)],
            params=[(pg1, 'track & pitch', 0.0, 10.0, 0.0)],
            pmls=[(slot1, pg1, [ig_sheet])],
        )
        strings_path = os.path.join(self.root, 'masterbank.strings.bank')
        bank_path = os.path.join(self.root, 'aircraft_gui.bank')
        with open(strings_path, 'wb') as f:
            f.write(strings_bytes)
        with open(bank_path, 'wb') as f:
            f.write(bank_bytes)

        strings = U.parse_strings_bank(strings_path)
        self.assertEqual(strings[ev1], 'event:/aircraft/gui/alarm_rwr & test')

        bank, events, waits, muits, wavs, fsbs = U.parse_bank(bank_path)
        self.assertEqual(bank.fmt_version, 0x8E)
        self.assertEqual(len(events), 5)
        self.assertEqual(len(muits), 1)
        self.assertEqual(muits[0]['items'], [ig2])
        self.assertIn(pg1, bank.params)
        self.assertEqual(bank.params[pg1][0], 'track & pitch')

        sample_events, tg2ev, wg2rec = U.link_samples(events, waits, muits, wavs, bank.evis)
        self.assertEqual(sample_events[(0, 0)], {ev1})
        self.assertEqual(sample_events[(0, 1)], {ev2})
        self.assertEqual(sample_events[(0, 2)], {ev_outer})  # inner event attributed to outer
        self.assertEqual(wg2rec[wg_sheet][0], 1)  # second index=0 gets fsb=1

        # Split-bank merge updates indices from .assets.bank descriptors
        merged = U.merge_split_wavs(wavs[:1], [{'guid': wg1, 'index': 7, 'flags': 0, 'field': 1, 'sub': 0},
                                               {'guid': wg2, 'index': 8, 'flags': 0, 'field': 1, 'sub': 0}])
        self.assertEqual({m['guid']: m['index'] for m in merged}[wg1], 7)

        # Build wavs and generate .fspro
        audio_map = {}
        for key, path in [
            (('v', 0, 0), os.path.join(self.root, 'w0.wav')),
            (('v', 0, 1), os.path.join(self.root, 'w1.wav')),
            (('v', 0, 2), os.path.join(self.root, 'w2.wav')),
            (('v', 1, 0), os.path.join(self.root, 'ws.wav')),
        ]:
            _make_wav(path, frames=22050, rate=22050)
            audio_map[key] = path

        fspro_dir = os.path.join(self.root, 'fspro')
        info = U.generate_fspro(fspro_dir, 'aircraft_gui', events, strings, waits, muits,
                                tg2ev, wg2rec, audio_map, evis=bank.evis, bank_obj=bank)
        self.assertEqual(info['events'], 3)  # snapshots & unnamed inner event excluded
        self.assertEqual(info['audiofiles'], 4)

        # Parse EVERY generated XML to verify well-formedness & Studio 2.02 invariants
        param_defs = {}
        for dirpath, _dirs, files in os.walk(fspro_dir):
            for fn in files:
                if not fn.endswith(('.xml', '.fspro')):
                    continue
                xml_path = os.path.join(dirpath, fn)
                with open(xml_path, encoding='utf-8') as f:
                    root_el = ET.fromstring(f.read())
                if dirpath.endswith('ParameterPreset'):
                    gp = root_el.find("./object[@class='GameParameter']")
                    pp = root_el.find("./object[@class='ParameterPreset']")
                    param_defs[pp.attrib['id']] = gp.attrib['id']

        self.assertEqual(len(param_defs), 1)
        ev1_xml = os.path.join(fspro_dir, 'Metadata', 'Event', U.guid_str(ev1) + '.xml')
        with open(ev1_xml, encoding='utf-8') as f:
            ev_tree = ET.fromstring(f.read())
        proxy = ev_tree.find("./object[@class='ParameterProxy']")
        self.assertIsNotNone(proxy)
        preset_dest = proxy.find("./relationship[@name='preset']/destination").text
        self.assertIn(preset_dest, set(param_defs.values()))
        self.assertNotIn(preset_dest, set(param_defs.keys()))

        # diff_against against same dir -> 0 missing, 0 extra
        diff = U.diff_against(bank_path, self.root, strings)
        self.assertIn('MISSING (in game, not in bank): 0', diff)
        self.assertIn('EXTRA (not in the current game): 0', diff)

    def test_catalog_split_mode_and_cli_version(self):
        ev1, bus1, ig1, wg1 = _g(30), _g(31), _g(32), _g(33)
        empty_ev = _g(40)
        strings_bytes = _build_strings_bank([(ev1, 'event:/aircraft/weapons/gun_20mm')])
        populated = _build_fev_bank(events=[_evtb(ev1, bus1, _g(90))], waits=[(ig1, wg1, bus1)], wavs=[(wg1, 0)])
        empty_bank = _build_fev_bank(events=[_evtb(empty_ev, _g(41), _g(42))])

        game_dir = os.path.join(self.root, 'sound')
        os.makedirs(game_dir)
        for rel, blob in [
            ('masterbank.strings.bank', strings_bytes),
            ('aircraft_guns.bank', populated),
            ('vo_extra.bank', empty_bank),
        ]:
            with open(os.path.join(game_dir, rel), 'wb') as f:
                f.write(blob)

        out_md = os.path.join(self.root, 'docs', 'EVENTS.md')
        split_dir = os.path.join(self.root, 'docs', 'events')
        csv_path = os.path.join(self.root, 'out', 'events.csv')
        index_md = U.catalog(game_dir, out_path=out_md, csv_path=csv_path, split_dir=split_dir)

        self.assertIn('**2 total banks** (1 with named events, 1 empty/assets-only) · **1 named events**', index_md)
        self.assertTrue(os.path.isfile(os.path.join(split_dir, 'aircraft.md')))
        self.assertTrue(os.path.isfile(os.path.join(split_dir, 'misc.md')))
        with open(os.path.join(split_dir, 'aircraft.md'), encoding='utf-8') as f:
            self.assertIn('event:/aircraft/weapons/gun_20mm', f.read())
        with open(os.path.join(split_dir, 'misc.md'), encoding='utf-8') as f:
            misc_text = f.read()
        self.assertIn('Empty / assets-only banks', misc_text)
        self.assertIn('`vo_extra`', misc_text)

        # Verify load_catalog reads split directory and strips 'event:/' prefix
        loaded_events, bank_of = SR.load_catalog(out_md)
        self.assertIn('aircraft/weapons/gun_20mm', loaded_events)
        self.assertEqual(bank_of['aircraft/weapons/gun_20mm'], 'aircraft_guns')

        # Verify CLI --version
        proc = subprocess.run([sys.executable, os.path.join(ROOT, 'rebank.py'), '--version'],
                              capture_output=True, text=True, check=True)
        self.assertIn(U.__version__, proc.stdout)

    def test_doc_scripts_helpers(self):
        self.assertTrue(SR.is_noise_key('engineRoomDmPart'))
        self.assertTrue(SR.is_noise_key('cls_turret01'))
        self.assertFalse(SR.is_noise_key('signalSfxName'))
        self.assertEqual(VT.core_name('120mm_rh120_user'), '120mm_rh120')
        self.assertEqual(VT.core_name('us_aim9l_default'), 'us_aim9l')

        out_vw = os.path.join(self.root, 'docs', 'VEHICLE_WEAPONS.md')
        split_vw = os.path.join(self.root, 'docs', 'vehicle_weapons')
        rows = {'aircraft': [('f_16a', 'us_20mm_m61a1')], 'tanks': [('us_m1a2', '120mm_m256')]}
        VT.write_vehicle_weapons(out_vw, rows, split_dir=split_vw)
        self.assertTrue(os.path.isfile(out_vw))
        self.assertTrue(os.path.isfile(os.path.join(split_vw, 'aircraft.md')))
        self.assertTrue(os.path.isfile(os.path.join(split_vw, 'tanks.md')))


if __name__ == '__main__':
    unittest.main()
