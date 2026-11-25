#!/usr/bin/env python3
"""Build the per-type vehicle -> sound tables and the weapon table under docs/.

Reads the text output of wt_ext_cli for aces.vromfs.bin. The banks cannot
tell which vehicle plays which sound; the game data can:

  aircraft     gamedata/flightmodels/*.blk without a top-level `helicopter {`
  helicopters  gamedata/flightmodels/*.blk with one
  tanks        gamedata/units/tankmodels/*.blk (+ tracked_/wheeled_vehicles)
  ships        gamedata/units/ships/*.blk
  weapons      gamedata/weapons/**/*.blk that carry sound presets

Flight models: sensors name their alarm through `signalSfxName`; the Sound
block selects the engine and gun presets. Tanks and ships share one
`sound { }` block: engine, AI engine, track/wake, turret and gun turn. Every
vehicle lists the weapon blocks it mounts (`blk:t = "gamedata/weapons/…"`);
a container (pylon) resolves one level down to the missile it holds.

Weapon presets (`sound`, `sound_inside`, `sfxReloadBullet`, `guidanceSfx`,
`cockpit/outside/ai/charge`) resolve to events through `sound_path` /
`sound_pathStudio` (see docs/SOUND_REFS.md). Torpedoes and human weapons carry
no sound fields (native code).

    python scripts/vehicle_table.py <type> GAMEDATA_DIR -o docs/<TYPE>.md [--find f_16] [--csv]
    python scripts/vehicle_table.py aircraft GAMEDATA_DIR --all -o docs [--split-weapons]
"""
import argparse
import csv
import glob
import os
import re

FLIGHT_FIELDS = [  # Sound { } keys of a flight model
    ('Engine', 'Engine'),
    ('gun', 'Gun'),
    ('turretTurnSfxName', 'Turret turn'),
    ('nozzleMoveSfx', 'Nozzle'),
]
GROUND_FIELDS = [  # sound { } keys shared by tanks and ships
    ('EngineName', 'Engine'),
    ('EngineNameAi', 'Engine (AI)'),
    ('TrackSoundName', 'Tracks / wake'),
    ('TrackSoundNameCockpit', 'Tracks (cockpit)'),
    ('TrackSoundNameAi', 'Tracks (AI)'),
    ('turret_turn', 'Turret turn'),
    ('gun_turn', 'Gun turn'),
    ('backfireSound', 'Backfire'),
    ('hornSound', 'Horn'),
]
WEAPON_FIELDS = [  # (key in gamedata/weapons/*.blk, column header); several keys may share a column
    ('sound', 'Sound'),
    ('sound_inside', 'Inside'),
    ('cockpit', 'Cockpit'),
    ('outside', 'Outside'),
    ('ai', 'AI'),
    ('charge', 'Charge'),
    ('sound_charge', 'Charge'),
    ('charge_inside', 'Charge (inside)'),
    ('sound_charge_inside', 'Charge (inside)'),
    ('sfxReloadBullet', 'Reload'),
    ('reload_sound', 'Reload'),
    ('sfxManualReloadBullet', 'Reload'),
    ('guidanceSfx', 'Guidance sfx'),
    ('launchSfx', 'Launch sfx'),
    ('sound_path', 'Path'),
    ('sound_pathStudio', 'Path (Studio)'),
]
WEAPON_HEAD = ['Weapon', 'Folder', 'Type', 'Sound', 'Inside', 'Cockpit', 'Outside', 'AI', 'Charge',
               'Charge (inside)', 'Reload', 'Guidance sfx', 'Launch sfx', 'Path', 'Path (Studio)']
WEAPON_DIRS = ('groundmodels_weapons', 'navalmodels_weapons', 'rocketguns', 'bombguns',
               'payloadguns', 'torpedoes', 'containers', 'equipment', 'mines', 'drop_tank',
               'angular_limits_tv_weapons', 'human_weapons')
PYLON_PREFIXES = ('ter_', 'bru_', 'mer_', 'lau_', 'dummy')

FLIGHT_HEAD = ['Flight model', 'RWR indicator', 'Sensors', 'RWR / MLWS events',
               'Engine', 'Gun', 'Turret turn', 'Nozzle']
GROUND_HEAD = ['Vehicle', 'Type', 'Engine', 'Engine (AI)', 'Tracks / wake', 'Tracks (cockpit)',
               'Tracks (AI)', 'Turret turn', 'Gun turn', 'Backfire', 'Horn']
DOC_NAME = {'aircraft': 'AIRCRAFT', 'helicopters': 'HELICOPTERS', 'tanks': 'TANKS', 'ships': 'SHIPS'}
DOCS_NAV = '[← Docs](README.md) · [Vehicle Weapons](VEHICLE_WEAPONS.md) · [Weapons](WEAPONS.md) · [Sound Refs](SOUND_REFS.md) · [Events](EVENTS.md)'


def read_text(path):
    with open(path, encoding='utf-8', errors='replace') as f:
        return f.read()


def write_text(path, text):
    os.makedirs(os.path.dirname(os.path.abspath(path)), exist_ok=True)
    with open(path, 'w', encoding='utf-8', newline='\n') as f:
        f.write(text)


def block(text, name):
    m = re.search(r'^%s \{(.*?)^\}' % re.escape(name), text, re.M | re.S)
    return m.group(1) if m else ''


def field(body, key):
    m = re.search(r'^\s*%s:t\s*=\s*"([^"]*)"' % re.escape(key), body, re.M)
    return m.group(1) if m else ''


def core_name(base):
    """Collapse `<core>_default/_user/_ai/_tmc` variants of one weapon to `<core>` without
    touching national prefixes (us_, ru_, germ_…): only a trailing variant suffix is cut."""
    return re.sub(r'_(default|user|ai|tmc)$', '', base, count=1)


def weapon_refs(text, sounding=frozenset(), weapon_cache=None):
    """Weapon blocks a vehicle mounts, by `blk:t`; containers resolve one level
    down to the missile they hold. Only blocks in `sounding` (those with a sound
    preset, matched by lower-case basename) are kept, pylon launchers are
    dropped. -> [core name, deduplicated]"""
    cache = weapon_cache or {}
    out = []
    for ref in re.findall(r'blk:t\s*=\s*"gamedata/weapons/([^"]+)"', text):
        base = ref[:-4] if ref.endswith('.blk') else ref
        for cand in (base, cache.get(base) or cache.get(os.path.basename(base))):
            if not cand or cand.startswith(PYLON_PREFIXES):
                continue
            if os.path.basename(cand).lower() not in sounding:
                continue
            core = core_name(os.path.basename(cand))
            if core not in out:
                out.append(core)
    return out


def load_weapon_cache(gamedata):
    cache = {}
    for sub in WEAPON_DIRS:
        for f in glob.glob(os.path.join(gamedata, 'weapons', sub, '*.blk')):
            name = os.path.basename(f)[:-4]
            m = re.search(r'blk:t\s*=\s*"gamedata/weapons/([^"]+)"', read_text(f))
            if m:
                cache[name] = m.group(1)[:-4] if m.group(1).endswith('.blk') else m.group(1)
    return cache


def load_sensors(gamedata):
    sensors = {}
    for f in glob.glob(os.path.join(gamedata, 'sensors', '*.blk')):
        t = read_text(f)
        sfx = re.search(r'^\s*signalSfxName:t\s*=\s*"([^"]+)"', t, re.M)
        nm = re.search(r'^\s*name:t\s*=\s*"([^"]+)"', t, re.M)
        if sfx:
            sensors['gamedata/sensors/' + os.path.basename(f)] = (
                nm.group(1) if nm else os.path.basename(f)[:-4], sfx.group(1))
    return sensors


def flight_rows(gamedata, find, helicopters, sounding=frozenset(), weapon_cache=None, vehicle_weapons=None):
    sensors = load_sensors(gamedata)
    rows = []
    vw = vehicle_weapons if vehicle_weapons is not None else {}
    for f in sorted(glob.glob(os.path.join(gamedata, 'flightmodels', '*.blk'))):
        name = os.path.basename(f)[:-4]
        if find and find.lower() not in name.lower():
            continue
        t = read_text(f)
        if ('helicopter {' in t) != helicopters:
            continue
        found = [sensors[b] for b in sorted(set(re.findall(r'blk:t\s*=\s*"(gamedata/sensors/[^"]+)"', t)))
                 if b in sensors]
        snd = block(t, 'Sound')
        names, sfx = [], []
        for n, s in found:          # one sensor blk can be mounted several times
            if n not in names:
                names.append(n)
            if s not in sfx:
                sfx.append(s)
        ind = re.search(r'^rwrIndicator:t\s*=\s*"([^"]+)"', t, re.M)
        rows.append([name, ind.group(1) if ind else '', ', '.join(names), ', '.join(sfx)]
                    + [field(snd, k) for k, _ in FLIGHT_FIELDS])
        vw.setdefault(('helicopters' if helicopters else 'aircraft'), []).append(
            (name, ', '.join(weapon_refs(t, sounding, weapon_cache))))
    return rows


def ground_rows(gamedata, find, subdirs, sounding=frozenset(), weapon_cache=None, vehicle_weapons=None):
    rows = []
    vw = vehicle_weapons if vehicle_weapons is not None else {}
    for sub in subdirs:
        for f in sorted(glob.glob(os.path.join(gamedata, 'units', sub, '*.blk'))):
            name = os.path.basename(f)[:-4]
            if find and find.lower() not in name.lower():
                continue
            t = read_text(f)
            if not re.search(r'^sound \{', t, re.M):
                continue
            snd = block(t, 'sound')
            typ = re.search(r'^type:t\s*=\s*"([^"]+)"', t, re.M)
            rows.append([name, (typ.group(1) if typ else '').removeprefix('type')]
                        + [field(snd, k) for k, _ in GROUND_FIELDS])
            vw.setdefault(('ships' if sub == 'ships' else 'tanks'), []).append(
                (name, ', '.join(weapon_refs(t, sounding, weapon_cache))))
    return rows


def weapon_rows(gamedata, find, sounding=None):
    rows = []
    for sub in WEAPON_DIRS:
        for f in sorted(glob.glob(os.path.join(gamedata, 'weapons', sub, '*.blk'))):
            name = os.path.basename(f)[:-4]
            if find and find.lower() not in name.lower():
                continue
            t = read_text(f)
            # one column per header; keys sharing a header (charge, reload) merge, first wins
            col = {}
            for k, h in WEAPON_FIELDS:
                v = field(t, k)
                if v and h not in col:
                    col[h] = v
            if not col:
                continue
            if sounding is not None:
                sounding[name.lower()] = True
            typ = re.search(r'^type:t\s*=\s*"([^"]+)"', t, re.M)
            rows.append([name, sub, typ.group(1) if typ else '']
                        + [col.get(h, '') for h in WEAPON_HEAD[3:]])
    return rows


def write_vehicle_weapons(out, vehicle_weapons, split_dir=None):
    """docs/VEHICLE_WEAPONS.md (+ optional docs/vehicle_weapons/*.md): every vehicle and the sounding weapons it mounts."""
    title = {'aircraft': 'Aircraft', 'helicopters': 'Helicopters', 'tanks': 'Tanks', 'ships': 'Ships'}
    total = sum(len(v) for v in vehicle_weapons.values())
    if split_dir:
        out_dir = os.path.dirname(os.path.abspath(out))
        rel_split = os.path.relpath(os.path.abspath(split_dir), out_dir).replace('\\', '/')
        os.makedirs(split_dir, exist_ok=True)
        idx = [
            DOCS_NAV, '',
            '# Vehicle → weapons', '',
            'Which sounding weapon blocks ([WEAPONS.md](WEAPONS.md)) each vehicle mounts, by `blk:t`; containers '
            'resolve one level down to the missile they hold, pylon launchers are dropped and '
            '`_default/_user/_ai/_tmc` variants collapse to the core name. Generated by `scripts/vehicle_table.py`.', '',
            '**%d total vehicles** split by category so every table stays under GitHub\'s 512 KB rendering cap.' % total, '',
            '| Category | Vehicles | Table |', '| --- | ---: | --- |',
        ]
        for typ in ('aircraft', 'helicopters', 'tanks', 'ships'):
            rows = vehicle_weapons.get(typ, [])
            if not rows:
                continue
            idx.append('| **%s** | %d | [`%s/%s.md`](%s/%s.md) |' % (title[typ], len(rows), rel_split, typ, rel_split, typ))
            sub_lines = [
                '[← Vehicle Weapons](../VEHICLE_WEAPONS.md) · [Weapons](../WEAPONS.md) · [← Docs](../README.md)', '',
                '# %s → mounted sounding weapons' % title[typ], '',
                '**%d vehicles**. See [WEAPONS.md](../WEAPONS.md) for each weapon\'s fire/reload/guidance sound presets.' % len(rows), '',
                '| Vehicle | Weapons |', '| --- | --- |',
            ]
            sub_lines += ['| `%s` | %s |' % r for r in rows]
            write_text(os.path.join(split_dir, typ + '.md'), '\n'.join(sub_lines) + '\n')
        write_text(out, '\n'.join(idx) + '\n')
    else:
        lines = [
            DOCS_NAV, '',
            '# Vehicle → weapons', '',
            'Which sounding weapon blocks ([WEAPONS.md](WEAPONS.md)) each vehicle mounts, by `blk:t`; containers '
            'resolve one level down to the missile they hold, pylon launchers are dropped and '
            '`_default/_user/_ai/_tmc` variants collapse to the core name. Generated by '
            '`scripts/vehicle_table.py`.', '',
        ]
        for typ in ('aircraft', 'helicopters', 'tanks', 'ships'):
            rows = vehicle_weapons.get(typ, [])
            if not rows:
                continue
            lines += ['## %s' % title[typ], '', '| Vehicle | Weapons |', '| --- | --- |']
            lines += ['| `%s` | %s |' % r for r in rows]
            lines.append('')
        write_text(out, '\n'.join(lines).rstrip('\n') + '\n')
    print('vehicle_weapons: %s (%d vehicles)' % (out, total))


TYPES = {
    'aircraft': dict(
        title='Aircraft → sound events and weapons',
        intro='Per flight model (no top-level `helicopter {` block): RWR indicator, mounted sensors, '
              'the `alarm_radar_*` / `alarm_launch_detected_*` events they name (`signalSfxName`) '
              'and the sound sets selected in `Sound { }`. Mounted weapons: [VEHICLE_WEAPONS.md](VEHICLE_WEAPONS.md).',
        head=FLIGHT_HEAD,
        run=lambda g, find, **kw: flight_rows(g, find, helicopters=False, **kw)),
    'helicopters': dict(
        title='Helicopters → sound events and weapons',
        intro='Per flight model with a top-level `helicopter {` block; same columns as the [aircraft table](AIRCRAFT.md). '
              'Mounted weapons: [VEHICLE_WEAPONS.md](VEHICLE_WEAPONS.md).',
        head=FLIGHT_HEAD,
        run=lambda g, find, **kw: flight_rows(g, find, helicopters=True, **kw)),
    'tanks': dict(
        title='Tanks → sound presets and weapons',
        intro='Per ground vehicle (`units/tankmodels`, `tracked_vehicles`, `wheeled_vehicles`): the '
              '`sound { }` presets — engine, AI engine, tracks, turret and gun turn, backfire. '
              'Presets resolve to events through `sound_path` / `TrackSoundPath` ([SOUND_REFS.md](SOUND_REFS.md)); '
              'mounted weapons: [VEHICLE_WEAPONS.md](VEHICLE_WEAPONS.md).',
        head=GROUND_HEAD,
        run=lambda g, find, **kw: ground_rows(g, find, ('tankmodels', 'tracked_vehicles', 'wheeled_vehicles'), **kw)),
    'ships': dict(
        title='Ships → sound presets and weapons',
        intro='Per ship (`units/ships`): the `sound { }` presets — engine, AI engine, wake/track, '
              'turret and gun turn. Mounted weapons: [VEHICLE_WEAPONS.md](VEHICLE_WEAPONS.md).',
        head=GROUND_HEAD,
        run=lambda g, find, **kw: ground_rows(g, find, ('ships',), **kw)),
    'weapons': dict(
        title='Weapons → sound presets',
        intro='Per weapon block under `gamedata/weapons/` that carries sound fields: fire sound, '
              'interior variant, reload, guidance tone, and the `sound_path` that resolves the preset '
              'to an event (`<sound_path>/<sound>`; see [SOUND_REFS.md](SOUND_REFS.md)). Containers list no sound of '
              'their own; the missile they hold is a separate row. Torpedoes and human weapons carry '
              'no sound fields (native code).',
        head=WEAPON_HEAD,
        run=lambda g, find, **kw: weapon_rows(g, find)),
}


def write_table(typ, gamedata, find, out, sounding=frozenset(), weapon_cache=None, vehicle_weapons=None):
    """One Markdown table for `typ` into `out`; columns empty in every row are dropped."""
    spec = TYPES[typ]
    rows = spec['run'](gamedata, find, sounding=sounding, weapon_cache=weapon_cache, vehicle_weapons=vehicle_weapons)
    keep = [i for i in range(len(spec['head'])) if i == 0 or any(r[i] for r in rows)]
    head = [spec['head'][i] for i in keep]
    lines = [
        DOCS_NAV, '',
        '# ' + spec['title'], '',
        spec['intro'], '',
        'Generated by `scripts/vehicle_table.py %s` (**%d rows**).' % (typ, len(rows)), '',
        '| ' + ' | '.join(head) + ' |',
        '|' + '---|' * len(head),
    ]
    lines += ['| ' + ' | '.join(('`%s`' % c) if i == 0 else c for i, c in enumerate([r[k] for k in keep])) + ' |'
              for r in rows]
    write_text(out, '\n'.join(lines) + '\n')
    print('%s: %s (%d rows)' % (typ, out, len(rows)))
    return rows


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('type', choices=sorted(TYPES))
    ap.add_argument('gamedata', help='unpacked aces.vromfs.bin_u/gamedata')
    ap.add_argument('-o', '--out', help='write Markdown here (default: print)')
    ap.add_argument('--csv', help='also write CSV')
    ap.add_argument('--all', dest='all_types', action='store_true',
                    help='with -o DIR: write every vehicle table plus VEHICLE_WEAPONS.md into DIR')
    ap.add_argument('--split-weapons', action='store_true',
                    help='with --all: split VEHICLE_WEAPONS.md into <out>/vehicle_weapons/*.md')
    ap.add_argument('--find', help='only rows whose first column contains this (case-insensitive)')
    a = ap.parse_args()
    gamedata = a.gamedata.replace('\\', '/')
    if not os.path.isdir(os.path.join(gamedata, 'flightmodels')) and a.type in ('aircraft', 'helicopters'):
        raise SystemExit('!! no flightmodels folder under %s (unpack aces.vromfs.bin with wt_ext_cli first)' % gamedata)
    weapon_cache = load_weapon_cache(gamedata)
    sounding = {}
    weapon_rows(gamedata, None, sounding=sounding)   # fills sounding so vehicles list only sounding weapons
    vehicle_weapons = {}
    if a.all_types:
        if not a.out:
            ap.error('--all needs -o DIR')
        for typ in ('aircraft', 'helicopters', 'tanks', 'ships'):
            write_table(typ, gamedata, a.find, os.path.join(a.out, DOC_NAME[typ] + '.md'),
                        sounding=sounding, weapon_cache=weapon_cache, vehicle_weapons=vehicle_weapons)
        vw_out = os.path.join(a.out, 'VEHICLE_WEAPONS.md')
        split_dir = os.path.join(a.out, 'vehicle_weapons') if a.split_weapons else None
        write_vehicle_weapons(vw_out, vehicle_weapons, split_dir=split_dir)
        return
    rows = (write_table(a.type, gamedata, a.find, a.out, sounding=sounding,
                        weapon_cache=weapon_cache, vehicle_weapons=vehicle_weapons)
            if a.out else TYPES[a.type]['run'](gamedata, a.find, sounding=sounding,
                                               weapon_cache=weapon_cache, vehicle_weapons=vehicle_weapons))
    if not a.out:
        print(' | '.join(TYPES[a.type]['head']))
        for r in rows:
            print(' | '.join(r))
    if a.csv:
        with open(a.csv, 'w', newline='', encoding='utf-8-sig') as f:
            w = csv.writer(f)
            w.writerow(TYPES[a.type]['head'])
            w.writerows(rows)
        print('csv:', a.csv)


if __name__ == '__main__':
    main()
