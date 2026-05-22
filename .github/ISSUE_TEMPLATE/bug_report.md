name: "Bug Report"
description: "Report a bug or issue"
labels: ["bug"]

body:
  - type: markdown
    attributes:
      value: "## Bug Report"
  
  - type: textarea
    attributes:
      label: "Description"
      description: "Clear description of the bug"
      placeholder: "What happened?"
    validations:
      required: true
  
  - type: textarea
    attributes:
      label: "Steps to Reproduce"
      description: "How to reproduce the issue"
      placeholder: "1. ...\n2. ...\n3. ..."
    validations:
      required: true
  
  - type: textarea
    attributes:
      label: "Expected Behavior"
      placeholder: "What should happen?"
  
  - type: textarea
    attributes:
      label: "Screenshots"
      description: "If applicable"
  
  - type: input
    attributes:
      label: "Version"
      placeholder: "1.0.0"
  
  - type: input
    attributes:
      label: "Environment"
      placeholder: "OS, Python version, etc."
