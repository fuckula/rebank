---
name: Bug report
about: The tool crashes, produces a project FMOD Studio rejects, or wrong output
title: "[bug] "
labels: bug
body:
  - type: input
    id: cmd
    attributes:
      label: Command line
      description: The exact `fbu ...` invocation
    validations:
      required: true
  - type: input
    id: header
    attributes:
      label: Tool output, first lines
      description: Paste the `bank ... fmt=0x8C/0x8D/0x8E: events=...` line and any traceback
    validations:
      required: true
  - type: input
    id: studio
    attributes:
      label: FMOD Studio version (if you opened the generated project)
      placeholder: 2.02.22
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
        - label: I installed the `[decode]` extra if the problem involves sample decoding.
