# Contributing

Thanks for helping improve ReBank (`rebank`).

## Bug reports

Open an issue using the [Bug report form](.github/ISSUE_TEMPLATE/bug_report.md) with:

- your `rebank --version` and how you run it (`rebank.exe` or Python source),
- the exact `rebank ...` command line you ran,
- the tool's first output line (`bank X fmt=0x8C/0x8D/0x8E: events=…`),
- the FMOD Studio version you target,
- what you expected vs what happened.

> [!CAUTION]
> **Never attach `.bank` files or audio from a commercial game** — they are proprietary. If a bank is needed to reproduce a problem, say so and we will find another way (hex dumps of a few dozen bytes or synthetic test fixtures are fine).

## Pull requests

- One focused change per PR; keep the diff reviewable.
- `ruff check .` and `python -m unittest discover -s tests -v` must pass; run `smoke_test.py` against a bank you own or have rights to.
- New code: standard library only for the core. Anything that needs `fsb5` goes behind the `[decode]` extra and must degrade with a clear message when the package is missing.
- Public-facing text (`README.md`, `docs/`, `--help`, CLI messages) is English.
- If you change CLI flags or doc generators (`rebank catalog`, `scripts/vehicle_table.py`, `scripts/sound_refs.py`), update the corresponding docs and tests.

## Development setup

```sh
git clone https://github.com/fuckula/rebank
cd rebank
pip install -e ".[decode]"
ruff check .
python -m unittest discover -s tests -v
python smoke_test.py path/to/your.bank
```

To check Markdown formatting locally (same rules as CI):

```sh
npx markdownlint-cli2 "README.md" "CONTRIBUTING.md" "SECURITY.md" "CODE_OF_CONDUCT.md" "docs/README.md" "docs/ARCHITECTURE.md" "docs/MODDING_GUIDE.md"
```

## Design notes

Parser decisions, binary offsets, and FMOD Studio 2.02 XML invariants live in [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md). Read it before touching `parse_bank`, `read_array`, or `generate_fspro` — most subtle bugs come from the array encoding (one `elemSize` per array, not per element) and Studio's object ownership rules.
