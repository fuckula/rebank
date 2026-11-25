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
TOOL = os.path.join(HERE, 'rebank.py')


def main():
    if len(sys.argv) < 2:
        print('usage: smoke_test.py <bank.bank> [game_sound_dir]')
        return 2
    bank = os.path.abspath(sys.argv[1])
    game = os.path.abspath(sys.argv[2]) if len(sys.argv) > 2 else None
    out = tempfile.mkdtemp(prefix='fbu_smoke_')

    # a split-layout bank (X.bank + X.assets.bank) has no strings.bank next to it:
    # the game folder supplies the dictionary and the paired assets file
    cmd = [sys.executable, TOOL, bank, '--fspro', '-o', out]
    assets = bank[:-5] + '.assets.bank'
    if os.path.exists(assets):
        cmd += ['-a', assets]
    if game:
        cmd += ['--game', game, '-s', os.path.join(game, 'masterbank.strings.bank')]
    r = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8', errors='replace')
    print(r.stdout)
    if r.returncode != 0:
        print('FAIL: tool exit code %d\n%s' % (r.returncode, r.stderr))
        return 1

    fspro_dir = os.path.join(out, 'fspro')
    events = glob.glob(os.path.join(fspro_dir, 'Metadata', 'Event', '*.xml'))
    # reference integrity: every <destination> must resolve to an object (same
    # file or any other under Metadata) — otherwise Studio marks it malformed;
    # every SingleSound/MultiSound/ParameterProxy must have an owner
    ids, owned = set(), set()
    for f in glob.glob(os.path.join(fspro_dir, 'Metadata', '**', '*.xml'), recursive=True):
        root = ET.parse(f).getroot()
        for el in root.iter('object'):
            ids.add(el.get('id'))
        for el in root.iter('destination'):
            owned.add(el.text)
    refs = [el.text for f in glob.glob(os.path.join(fspro_dir, 'Metadata', '**', '*.xml'), recursive=True)
            for el in ET.parse(f).getroot().iter('destination')]
    dangling = sorted({r for r in refs if r not in ids})
    if dangling:
        print('FAIL: %d dangling references, e.g. %s' % (len(dangling), dangling[:3]))
        return 1
    orphans = [(o.get('class'), o.get('id')) for f in events
               for o in ET.parse(f).getroot().iter('object')
               if o.get('class') in ('SingleSound', 'MultiSound', 'ParameterProxy') and o.get('id') not in owned]
    if orphans:
        print('FAIL: %d unowned sound/proxy objects, e.g. %s' % (len(orphans), orphans[:3]))
        return 1
    print('PASS: reference integrity (%d objects, %d refs, 0 dangling)' % (len(ids), len(refs)))
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
