---
name: Bug report
about: The tool crashes, produces a project FMOD Studio rejects, or writes wrong output
title: "[bug] "
labels: bug
body:
  - type: dropdown
    id: install
    attributes:
      label: How are you running ReBank?
      options:
        - Windows standalone executable (rebank.exe)
        - Python source / pip install
        - Python source / pip install ".[decode]"
    validations:
      required: true
  - type: input
    id: version
    attributes:
      label: Version
      description: Output of `rebank --version` (or git commit SHA)
      placeholder: "rebank 0.1.1"
    validations:
      required: true
  - type: input
    id: cmd
    attributes:
      label: Command line
      description: The exact `rebank ...` invocation (redact personal folder names if needed)
      placeholder: 'rebank aircraft_gui.bank --fspro --game "C:/Games/War Thunder/sound" --apply'
    validations:
      required: true
  - type: textarea
    id: header
    attributes:
      label: Tool output and traceback
      description: Paste the `bank ... fmt=0x8C/0x8D/0x8E: events=...` line and any error output
    validations:
      required: true
  - type: input
    id: studio
    attributes:
      label: FMOD Studio version (if you opened the generated project)
      placeholder: "2.02.22"
  - type: textarea
    id: expect
    attributes:
      label: Expected vs actual
    validations:
      required: true
  - type: checkboxes
    id: rules
    attributes:
      label: Checklist
      options:
        - label: I did not attach any `.bank` or audio files from a commercial game (they are proprietary).
          required: true
        - label: I installed the `[decode]` extra if running from source and the problem involves sample decoding.
