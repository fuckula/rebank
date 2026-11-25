"""Unit tests for the sound-mod completeness check.

Run:  python -m unittest tests.test_mod_check
No game assets required — fixtures are synthetic.
"""
import os
import struct
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import rebank as U  # noqa: E402


def minimal_bank(name, event_guid):
    """Smallest parseable bank: FMT + one event + STDT with the event path."""
    fmt = b'FMT ' + struct.pack('<I', 8) + struct.pack('<HHI', 0x8E, 0, 0)
    evt = b'EVT ' + struct.pack('<I', 16) + event_guid
    stdt = b'STDT' + struct.pack('<I', 4) + struct.pack('<I', 1)
    proj = b'LIST' + struct.pack('<I', 4 + 8 + len(fmt) + 8 + len(evt) + 8 + len(stdt)) + b'PROJ' \
        + b'BNKI' + struct.pack('<I', 0) + fmt + evt + stdt
    return b'RIFF' + struct.pack('<I', 4 + len(proj)) + b'FBNK' + proj


BLK = '''maxChannels:i = 256
masterBanks {
\tname:t = "masterbank"
\tname:t = "masterbank.strings"
}
banks {
\tfolder:t = "sound"
\textension:t = ".bank"
\tpresets {
\t\tmaster {
\t\t\tmasterbank.strings { async:b = false }
\t\t\taircraft_gui { async:b = true }
\t\t\tdialogs { async:b = true optional:b = true }
\t\t}
\t}
}
'''


class SoundStudioBlk(unittest.TestCase):
    def test_required_and_optional(self):
        req = U.required_banks_from_blk(BLK)
        self.assertEqual(req['folder'], 'sound')
        self.assertEqual(req['extension'], '.bank')
        self.assertEqual(req['required'], ['masterbank.strings', 'aircraft_gui'])
        self.assertEqual(req['optional'], ['dialogs'])


class CheckMod(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.game = os.path.join(self.tmp.name, 'sound')
        self.mod = os.path.join(self.tmp.name, 'mod')
        os.makedirs(self.game)
        os.makedirs(self.mod)
        g = b'\x11' * 16
        open(os.path.join(self.game, 'masterbank.strings.bank'), 'wb').write(b'strings')
        for name in ('masterbank.strings', 'masterbank', 'aircraft_gui', 'aircraft_gui.assets', 'dialogs'):
            open(os.path.join(self.game, name + '.bank'), 'wb').write(b'bank:' + name.encode())
        open(os.path.join(self.mod, 'aircraft_gui.bank'), 'wb').write(b'bank:aircraft_gui')
        # the bank parsers are covered by tests.test_primitives; here they return the same event for every file
        self._orig = (U.parse_strings_bank, U.parse_bank)
        U.parse_strings_bank = lambda path: {g: 'event:/aircraft/gui/test'}
        U.parse_bank = lambda path: (None, {g: None}, [], [], [], [])

    def tearDown(self):
        U.parse_strings_bank, U.parse_bank = self._orig
        self.tmp.cleanup()

    def test_without_blk_only_names_are_checked(self):
        ok, report = U.check_mod(self.mod, self.game)
        self.assertTrue(ok, report)

    def test_missing_required_bank_is_a_problem(self):
        ok, report = U.check_mod(self.mod, self.game, studio_blk=BLK)
        self.assertFalse(ok)
        self.assertIn('masterbank.strings.bank', report)
        self.assertIn('switches the whole mod off', report)
        self.assertNotIn('dialogs', report)  # optional banks are not required

    def test_full_set_passes(self):
        for name in ('masterbank.strings', 'masterbank', 'aircraft_gui.assets'):
            open(os.path.join(self.mod, name + '.bank'), 'wb').write(b'bank:' + name.encode())
        ok, report = U.check_mod(self.mod, self.game, studio_blk=BLK)
        self.assertTrue(ok, report)

    def test_assets_pair_is_checked_without_blk(self):
        # aircraft_gui has an .assets.bank in the game, but the mod ships the metadata half only
        open(os.path.join(self.game, 'extra.bank'), 'wb').write(b'bank:extra')
        ok, report = U.check_mod(self.mod, self.game)
        self.assertTrue(ok)  # metadata-only is a warning, not an error
        self.assertIn('aircraft_gui.assets.bank', report)


if __name__ == '__main__':
    unittest.main()
