# SpecKit Company Context

> A structured framework for capturing organizational knowledge to enable AI deployment

## The Problem

When deploying AI solutions within a company, the AI needs context to generate real value:

- **Who decides what?** Decision-making authority, approval workflows, escalation paths
- **What do terms mean?** Internal jargon, product names, project codenames
- **How do we work?** Processes, conventions, unwritten rules
- **What matters most?** Priorities, constraints, non-negotiables
- **Where is everything?** Systems, tools, documentation locations

This knowledge exists in various states:

| State | Example | Challenge |
|-------|---------|-----------|
| **Documented & usable** | Public API docs | Just needs indexing |
| **Documented but fragmented** | Scattered Confluence pages, old wikis | Needs synthesis |
| **Documented but wrong format** | Tribal knowledge in Slack threads | Needs transformation |
| **Undocumented** | "Ask Sarah, she knows" | Needs extraction |

Most AI deployments underperform because this context work is ad-hoc, incomplete, or never done.

## The Solution

Apply SpecKit's structured approach to knowledge capture:

1. **Constitution** - establish the engagement (who, what scope, what AI goal) + capture principles
2. **Outcome** - define what knowledge artifacts are needed
3. **Strategy** - plan capture approach, sources, and methods
4. **Tasks** - break down into executable extraction/synthesis work
5. **Capture** - execute tasks, validate artifacts

### Framework Adaptation

**Constitution → Engagement Definition + Capture Principles**

The constitution serves two purposes, establishing both the "playing field" and the rules:

Part 1 - Engagement Definition (Factual):

```markdown
**Organization**: Acme Corp
**Scope**: Marketing Team
**AI Deployment Goal**: AI assistant for on-brand content drafting

**Key Stakeholders**:
- Sponsor: VP Marketing (strategic context)
- SMEs: Brand Manager, Content Lead (domain knowledge)
- AI Users: Content writers (their needs shape what we capture)

**Boundaries**:
- In Scope: Brand voice, content guidelines, approval workflows
- Out of Scope: Engineering processes, finance data
```

Part 2 - Capture Principles (Normative):

- "All process documentation must include the 'why', not just the 'what'"
- "Decision records require context on alternatives considered"
- "Terminology definitions link to authoritative source or owner"

**Outcome → Knowledge Artifacts Needed**

Instead of user stories, define knowledge outcomes with acceptance criteria:

```markdown
## KO-001: Decision Authority Map

**Priority:** P1 (blocking for AI task delegation)

**Outcome:** Clear documentation of who can approve what, with escalation paths.

**Acceptance Criteria:**
- Given an AI needs to take an action requiring approval
- When it references the authority map
- Then it can identify the correct approver and escalation path

**Capture Methods:**
- [ ] Interview department heads
- [ ] Extract from existing org chart
- [ ] Synthesize from historical approval threads
```

**Strategy → Capture Approach**

Define the approach, structure, and key decisions for capture:

Structure:

- Repository structure (folders, naming conventions)
- Document templates (decision records, process docs, glossaries)
- Cross-referencing system (how artifacts link to each other)

Approach & Research:

- What capture methods apply to each outcome?
- What existing sources can be leveraged?
- What tools/integrations are available?
- Who are the key knowledge holders?

Decisions:

- Prioritization of knowledge areas
- Depth vs breadth trade-offs
- Maintenance model (how knowledge stays current)
- Quality gates (what makes an artifact "complete"?)

**Tasks → Extraction Work Items**

Granular, executable tasks:

```markdown
## Phase 1: Foundation

- [ ] T001 Interview CEO on strategic priorities (30 min)
- [ ] T002 Extract org chart from HR system
- [ ] T003 [P] Synthesize product glossary from marketing docs
- [ ] T004 [P] Synthesize engineering glossary from tech docs

## Phase 2: Process Mapping

- [ ] T005 [KO-001] Document finance approval thresholds
- [ ] T006 [KO-001] Map engineering review requirements
```

**Capture → Execute and Validate**

Execute tasks phase by phase, validating as you go:

- Work through extraction tasks systematically
- Validate each artifact against acceptance criteria
- Flag gaps or conflicts for resolution
- Update progress tracking in tasks file
- Checkpoint after each phase before proceeding

## Capture Methods

The framework supports multiple extraction approaches:

| Method | Best For | Output |
|--------|----------|--------|
| **Document Synthesis** | Existing written knowledge | Consolidated artifact |
| **Interview** | Tacit knowledge, context | Transcript → structured doc |
| **Form/Survey** | Standardized data collection | Structured responses |
| **System Export** | Structured data in tools | Raw data → formatted artifact |
| **Observation** | Process understanding | Process documentation |
| **Chat Extraction** | Historical decisions in threads | Decision records |

## Knowledge Artifact Types

Common artifacts this framework helps create:

- **Glossary**: Terms, definitions, ownership
- **Decision Records**: Context, alternatives, rationale, outcome
- **Process Documentation**: Steps, roles, exceptions, escalation
- **Authority Maps**: Who approves what, thresholds, delegation
- **System Inventory**: Tools, owners, integrations, access
- **Org Context**: Structure, responsibilities, communication patterns
- **Constraints Documentation**: Compliance, security, legal requirements
- **Priority Framework**: How trade-offs are made, what trumps what

## Success Metrics

The framework succeeds when:

1. **Coverage**: All critical knowledge areas have documented artifacts
2. **Accessibility**: AI systems can retrieve relevant context
3. **Accuracy**: Artifacts reflect actual company reality
4. **Currency**: Knowledge stays updated as company evolves
5. **Actionability**: AI can make better decisions using the context

## Status

Framework design complete. See [FRAMEWORK.md](FRAMEWORK.md) for full technical specification.

Next steps:

1. Create template files (constitution, outcome, strategy, tasks)
2. Write automation scripts (bash/powershell)
3. Define slash commands for Claude Code integration
4. Build example deployment for a test case
5. Develop maintenance/update workflows

## Related Work

- [SpecKit](https://github.com/github/spec-kit) - GitHub's spec-driven development framework
- [speckit-ralph](https://github.com/T-0-co/speckit-ralph) - T-0's autonomous execution layer
- Architecture Decision Records (ADRs)
- Knowledge Management frameworks (DIKW, etc.)
