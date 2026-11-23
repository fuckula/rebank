"""Unit tests for the binary primitives and the strings parser.

Run:  python -m unittest tests.test_primitives
No game assets required — every fixture is built from synthetic bytes.
"""
import os
import struct
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import rebank as U  # noqa: E402


def u16(v):
    return struct.pack('<H', v)


def u24(v):
    return struct.pack('<I', v)[:3]


def varint(n):
    """Encoder for the bank's shifted varint: raw = n << 1."""
    raw = n << 1
    if raw < 0x8000:
        return u16(raw)
    return u16(0x8000 | (raw & 0x7FFF)) + u16(raw >> 15)


def chunk(fourcc, payload):
    return fourcc + struct.pack('<I', len(payload)) + payload


def riff(typ, payload):
    return b'RIFF' + struct.pack('<I', 4 + len(payload)) + typ + payload


class Varint(unittest.TestCase):
    def test_small(self):
        self.assertEqual(U.read_varint(u16(9) + u16(0), 0), (9, 2))

    def test_extended(self):
        buf = u16(0x8000 | 3) + u16(2)
        self.assertEqual(U.read_varint(buf, 0), (3 | (2 << 15), 4))

    def test_roundtrip(self):
        for n in (0, 1, 0x3FFF, 0x4000, 0x4001, 1 << 20):
            v, off = U.read_varint(varint(n), 0)
            self.assertEqual(v >> 1, n)
            self.assertEqual(off, len(varint(n)))

    def test_truncated_raises(self):
        with self.assertRaises(struct.error):
            U.read_varint(b'\x01', 0)


class Array(unittest.TestCase):
    def test_layout(self):
        # varint raw=4 -> n=2, elemSize=3 once, then 2*3 bytes, then tail
        buf = u16(4) + u16(3) + b'abcdef' + b'ZZ'
        items, off = U.read_array(buf, 0)
        self.assertEqual(items, [b'abc', b'def'])
        self.assertEqual(off, 10)

    def test_empty(self):
        items, off = U.read_array(u16(0) + b'tail', 0)
        self.assertEqual((items, off), ([], 2))

    def test_overrun_raises(self):
        with self.assertRaises(ValueError):
            U.read_array(u16(2) + u16(16) + b'\x00' * 4, 0)


class WalkChunks(unittest.TestCase):
    def test_list_type_is_exposed(self):
        data = riff(b'FEV ', chunk(b'LIST', b'PROJ' + chunk(b'STDT', b'xy')))
        top = list(U.walk_chunks(data, 12, len(data)))
        self.assertEqual([(c, t) for _, c, _, t in top], [(b'LIST', b'PROJ')])
        p, c, s, t = top[0]
        inner = list(U.walk_chunks(data, p + 12, p + 8 + s))
        self.assertEqual([(c2, s2) for _, c2, s2, _ in inner], [(b'STDT', 2)])


class Strings(unittest.TestCase):
    """STDT radix trie inside LIST/PROJ, mirroring the real layout:

    [u32 ver][varint n][u16 8][n x {u24 strOff, u24 guidIdx, u8 childCount}]
    [varint g][u16 16][g x 16 guid bytes][u16 sl][pool]      (sl: plain u16, NOT shifted)
    [u16 mc][mc x 3 guid->node][u16 pc][pc x 3 parents]   (no varint/elemSize)
    """

    GUID = bytes(range(16))

    def _bank(self):
        pool = b'\x00a/b\x00'          # strOff 1 -> 'a/b'
        root = u24(0xFFFFFF) + b'\x00' + u24(0) + b'\x01'    # v1: no segment, v2: childCount=1
        leaf = u24(1) + b'\x00' + u24(0) + b'\x00'           # 'a/b', guid index 0, no children
        body = (struct.pack('<I', 0x1A) + varint(2) + u16(8) + root + leaf
                + varint(1) + u16(16) + self.GUID
                + u16(len(pool)) + pool
                + u16(1) + u24(0)                            # guid 0 -> node 0
                + u16(2) + u24(0xFFFFFF) + u24(0))           # parents: root=-1, leaf->root
        return riff(b'FEV ', chunk(b'LIST', b'PROJ' + chunk(b'STDT', body)))

    def test_parse_leaf_path(self):
        with tempfile.NamedTemporaryFile(delete=False, suffix='.bank') as f:
            f.write(self._bank())
            path = f.name
        try:
            out = U.parse_strings_bank(path)
        finally:
            os.unlink(path)
        self.assertEqual(out, {self.GUID: 'a/b'})

    def test_missing_stdt_raises(self):
        with tempfile.NamedTemporaryFile(delete=False, suffix='.bank') as f:
            f.write(riff(b'FEV ', chunk(b'LIST', b'PROJ')))
            path = f.name
        try:
            with self.assertRaises(ValueError):
                U.parse_strings_bank(path)
        finally:
            os.unlink(path)


class Helpers(unittest.TestCase):
    def test_guid_str_braced(self):
        s = U.guid_str(bytes(range(16)))
        self.assertTrue(s.startswith('{') and s.endswith('}'))
        self.assertEqual(len(s), 38)

    def test_safe_name_flattens_separators(self):
        self.assertEqual(U.safe_name('event:/aircraft/gui/alarm_radar'), 'event__aircraft_gui_alarm_radar')

    def test_event_rel_dir(self):
        self.assertEqual(U.event_rel_dir('event:/aircraft/gui/alarm_radar'),
                         (['aircraft', 'gui'], 'alarm_radar'))


if __name__ == '__main__':
    unittest.main()
