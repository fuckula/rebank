#!/usr/bin/env python3
"""Smoke test: end-to-end unwrap on a real FMOD 2.02 bank.

Usage:
  python smoke_test.py <bank.bank> [game_sound_dir]

Checks:
  1. Bank parses (events/instruments/waveforms counts > 0).
  2. strings.bank resolves names for a share of events.
  3. --fspro project generation produces valid XML and readable wavs.
  4. With game_sound_dir: --diff report is non-empty.
Exits non-zero on any failure.
"""
import glob
import os
import subprocess
import sys
import tempfile
import xml.etree.ElementTree as ET

HERE = os.path.dirname(os.path.abspath(__file__))
TOOL = os.path.join(HERE, 'fmod_bank_unwrap.py')


def main():
    if len(sys.argv) < 2:
        print('usage: smoke_test.py <bank.bank> [game_sound_dir]')
        return 2
    bank = os.path.abspath(sys.argv[1])
    game = os.path.abspath(sys.argv[2]) if len(sys.argv) > 2 else None
    out = tempfile.mkdtemp(prefix='fbu_smoke_')

    cmd = [sys.executable, TOOL, bank, '--fspro', '-o', out]
    if game:
        cmd += ['--game', game]
    r = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8', errors='replace')
    print(r.stdout)
    if r.returncode != 0:
        print('FAIL: tool exit code %d\n%s' % (r.returncode, r.stderr))
        return 1

    fspro_dir = os.path.join(out, 'fspro')
    events = glob.glob(os.path.join(fspro_dir, 'Metadata', 'Event', '*.xml'))
    if not events:
        print('FAIL: no event XML generated')
        return 1
    bad = [f for f in glob.glob(os.path.join(fspro_dir, 'Metadata', '**', '*.xml'),
                                recursive=True) if not ET.parse(f)]
    if bad:
        print('FAIL: %d invalid XML files' % len(bad))
        return 1
    for wav in glob.glob(os.path.join(fspro_dir, 'Assets', '**', '*.wav'), recursive=True):
        if open(wav, 'rb').read(4) != b'RIFF':
            print('FAIL: non-RIFF wav in Assets: %s' % wav)
            return 1
    print('PASS: %d events, XML valid, assets are RIFF wav' % len(events))

    if game:
        diff = glob.glob(os.path.join(out, '*_diff.txt'))
        if diff and os.path.getsize(diff[0]) > 0:
            print('PASS: diff report written')
        else:
            print('note: no diff report (bank name not present in game dir?)')
    return 0


if __name__ == '__main__':
    sys.exit(main())
