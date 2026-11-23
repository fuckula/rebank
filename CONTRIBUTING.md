# Contributing

Thanks for helping improve ReBank (`rebank`).

## Bug reports

Open an issue with:

- the exact command line you ran,
- the tool's first output line (`bank X fmt=0x8C/0x8D/0x8E: events=…`),
- the FMOD Studio version you target,
- what you expected vs what happened.

**Never attach `.bank` files or audio from a commercial game** — they are
proprietary. If a bank is needed to reproduce a problem, say so and we will
find another way (hex dumps of a few dozen bytes are fine).

## Pull requests

- One change per PR; keep the diff reviewable.
- `ruff check .` must pass; run `smoke_test.py` against a bank you own or
  have rights to.
- New code: standard library only for the core. Anything that needs
  `fsb5` goes behind the `[decode]` extra and must degrade with a clear
  message when the package is missing.
- Public-facing text (README, `--help`, messages) is English.

## Development setup

```sh
git clone https://github.com/OWNER/rebank
cd rebank
pip install -e ".[decode]"
ruff check .
python smoke_test.py path/to/your.bank
```

## Design notes

Parser decisions and the verified bank layout live in
`context/fmod-bank-layout.md`. Read it before touching `parse_bank`,
`read_array` or the `.fspro` emitter — most subtle bugs come from the array
encoding (one element size per array, not per element) and from Studio's
object ownership rules.
