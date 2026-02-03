# SpecKit Company Context

A framework for structured company knowledge capture, adapting GitHub's SpecKit spec-driven development approach to organizational AI readiness.

## Project Purpose

Enable systematic discovery, extraction, and documentation of company knowledge required for effective AI deployment. Instead of software specifications driving code implementation, **knowledge specifications** drive context artifact creation.

## Framework Overview

```text
.context/
├── memory/constitution.md     # Engagement definition + capture principles
├── outcomes/[###-name]/       # Knowledge outcomes (what to capture)
│   ├── outcome.md             # What artifact is needed
│   ├── strategy.md            # How to capture it
│   └── tasks.md               # Extraction work items
├── templates/                 # Document templates
├── scripts/                   # Automation
└── commands/                  # Slash command definitions

context-artifacts/             # The captured knowledge outputs
```

## Core Adaptation

| SpecKit (Software)     | This Framework (Knowledge)                  |
|------------------------|---------------------------------------------|
| `.specify/`            | `.context/`                                 |
| Constitution           | Engagement Definition + Capture Principles  |
| Specify (User Stories) | Outcome (Knowledge artifact needed)         |
| Plan (Architecture)    | Strategy (Capture approach and sources)     |
| Tasks                  | Extraction/Synthesis Work Items             |
| Implement              | Capture (Execute tasks, validate artifacts) |

## Constitution: Two Parts

### Part 1: Engagement Definition (Factual)

- **Organization**: What company/entity
- **Scope**: Whole company, department, team, or project
- **AI Deployment Goal**: What AI capability needs this context
- **Key Stakeholders**: Sponsors, SMEs, AI users
- **Boundaries**: In/out of scope, sensitive areas

### Part 2: Capture Principles (Normative)

- Source attribution requirements
- Currency tracking standards
- Validation requirements
- Quality gates

## Workflow Commands

| Command | Purpose | Output |
|---------|---------|--------|
| `/context.constitution` | Establish engagement + principles | `memory/constitution.md` |
| `/context.outcome` | Define knowledge artifact needed | `outcomes/[name]/outcome.md` |
| `/context.strategy` | Plan capture approach | `outcomes/[name]/strategy.md` |
| `/context.tasks` | Generate extraction tasks | `outcomes/[name]/tasks.md` |
| `/context.capture` | Execute and validate | Completed artifacts |
| `/context.clarify` | Resolve ambiguities | Updated docs |
| `/context.analyze` | Check consistency | Validation report |

## Key Concepts

- **Knowledge Outcome**: A specific artifact that enables AI to operate effectively
- **Capture Method**: How knowledge is acquired (interview, synthesis, export, form)
- **Context Artifact**: The resulting document/structure embedding company knowledge
- **Engagement Definition**: The "playing field" - who, what scope, what AI goal

## Development Status

Early concept phase - framework design complete, implementation pending.

## Key Documents

- [FRAMEWORK.md](../FRAMEWORK.md) - Complete technical design
- [MISSION.md](../MISSION.md) - Problem statement and solution overview

## Related

- [GitHub Spec-Kit](https://github.com/github/spec-kit) - Original framework
- [T-0 speckit-ralph](https://github.com/T-0-co/speckit-ralph) - T-0's SpecKit fork
