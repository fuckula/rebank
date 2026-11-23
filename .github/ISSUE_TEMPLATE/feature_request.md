---
name: Feature request
about: A new option, format support or workflow improvement
title: "[feat] "
labels: enhancement
body:
  - type: textarea
    id: problem
    attributes:
      label: What are you trying to do?
      description: The workflow, not the solution
    validations:
      required: true
  - type: textarea
    id: proposal
    attributes:
      label: Proposed behaviour
  - type: input
    id: fmt
    attributes:
      label: Bank format version (if relevant)
      description: The `fmt=0x...` value printed by the tool
