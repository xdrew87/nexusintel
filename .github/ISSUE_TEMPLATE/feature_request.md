name: "Feature Request"
description: "Suggest a new feature"
labels: ["enhancement"]

body:
  - type: markdown
    attributes:
      value: "## Feature Request"
  
  - type: textarea
    attributes:
      label: "Description"
      description: "What feature would you like?"
      placeholder: "I'd like..."
    validations:
      required: true
  
  - type: textarea
    attributes:
      label: "Use Case"
      description: "Why is this feature useful?"
      placeholder: "This would help because..."
  
  - type: textarea
    attributes:
      label: "Proposed Solution"
      description: "How should it work?"
      placeholder: "It could..."
