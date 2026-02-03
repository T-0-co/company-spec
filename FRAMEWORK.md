# Company Context Framework - Design Document

> Adapting SpecKit's spec-driven development to organizational knowledge capture

## Directory Structure

```
project/
├── .context/                          # Framework root (parallel to .specify/)
│   ├── memory/
│   │   └── constitution.md            # Engagement definition + capture principles
│   │
│   ├── outcomes/                      # Knowledge outcomes (parallel to specs/)
│   │   └── [###-outcome-name]/
│   │       ├── outcome.md             # What knowledge artifact is needed
│   │       ├── strategy.md            # How to capture it (approach, sources, methods)
│   │       ├── tasks.md               # Extraction/synthesis work items
│   │       └── checklists/            # Quality gates
│   │
│   ├── templates/
│   │   ├── constitution-template.md
│   │   ├── outcome-template.md
│   │   ├── strategy-template.md
│   │   ├── tasks-template.md
│   │   └── commands/                  # Slash command definitions
│   │       ├── constitution.md
│   │       ├── outcome.md
│   │       ├── strategy.md
│   │       ├── tasks.md
│   │       ├── capture.md
│   │       ├── clarify.md
│   │       └── analyze.md
│   │
│   └── scripts/
│       └── bash/
│           ├── check-prerequisites.sh
│           ├── common.sh
│           ├── create-new-outcome.sh
│           └── setup-strategy.sh
│
└── context-artifacts/                 # Captured knowledge outputs
    ├── glossaries/
    ├── processes/
    ├── decisions/
    ├── authorities/
    └── systems/
```

## Constitution: Engagement Definition + Principles

The constitution serves two purposes:

### Part 1: Engagement Definition (Factual)

Establishes the "playing field" - what context we're capturing and for whom.

```markdown
## Engagement Definition

**Organization**: [Company name]
**Scope**: [Whole company | Division | Department | Team | Project]
**Scope Details**: [Specific team/department names, boundaries]

**AI Deployment Goal**:
[What AI capability are we enabling? What will the AI do with this context?]
- Example: "AI assistant for marketing team to draft on-brand content"
- Example: "AI agent to handle tier-1 customer support"
- Example: "AI co-pilot for engineering to understand codebase context"

**Key Stakeholders**:
| Role | Name/Team | Knowledge Domain |
|------|-----------|------------------|
| Sponsor | [Who authorized this] | [Strategic context] |
| Subject Matter Experts | [List] | [Their domains] |
| AI Users | [Who will use the AI] | [Their needs] |

**Boundaries**:
- In Scope: [What areas/topics are included]
- Out of Scope: [What's explicitly excluded]
- Sensitive Areas: [Topics requiring special handling]

**Timeline**: [If applicable]
**Constraints**: [Budget, access limitations, compliance requirements]
```

### Part 2: Capture Principles (Normative)

Rules governing how knowledge is captured and maintained.

```markdown
## Capture Principles

### Article I: Source Attribution
Every artifact must cite its authoritative source or knowledge holder.

### Article II: Currency Tracking
All artifacts must include last-verified date and owner responsible for updates.

### Article III: Completeness Over Perfection
Capture "good enough" knowledge quickly; refine iteratively based on AI usage feedback.

### Article IV: Context Preservation
Document the "why" behind processes and decisions, not just the "what."

### Article V: Validation Required
No artifact is complete until validated by a subject matter expert.

[Add/remove principles based on engagement needs]
```

## Workflow Commands

### `/context.constitution`

Establish or update the engagement definition and capture principles.

**Inputs**: Organization info, scope, AI deployment goal
**Outputs**: `memory/constitution.md`
**When to use**: Project kickoff, scope changes

### `/context.outcome`

Define a knowledge outcome - what artifact is needed.

**Inputs**: Description of knowledge gap or AI need
**Outputs**: `outcomes/[###-name]/outcome.md`
**Process**:
1. Scan existing outcomes for next number
2. Create semantic branch/folder
3. Populate outcome template with:
   - Knowledge artifact description
   - Acceptance criteria (how do we know it's complete?)
   - Priority (P1/P2/P3 based on AI deployment needs)
   - Capture methods to consider

### `/context.strategy`

Plan how to capture the knowledge.

**Prerequisites**: `outcome.md` exists
**Outputs**: `strategy.md`, potentially `sources.md`, `stakeholders.md`
**Process**:
1. Analyze outcome requirements
2. Identify capture methods (interview, synthesis, export, etc.)
3. Map knowledge sources and stakeholders
4. Define artifact structure/template
5. Establish quality gates

### `/context.tasks`

Generate extraction/synthesis work items.

**Prerequisites**: `strategy.md` exists
**Outputs**: `tasks.md`
**Process**:
1. Analyze strategy for concrete actions
2. Break down by phase:
   - Phase 1: Source gathering
   - Phase 2: Extraction/interviews
   - Phase 3: Synthesis
   - Phase 4: Validation
   - Phase 5: Integration
3. Mark parallel tasks `[P]`
4. Link tasks to outcome `[KO-###]`

### `/context.capture`

Execute capture tasks (equivalent to `/speckit.implement`).

**Prerequisites**: `tasks.md` exists
**Process**:
1. Check prerequisites and checklists
2. Execute tasks phase by phase
3. Track progress in tasks.md
4. Validate artifacts against acceptance criteria
5. Report completion status

### `/context.clarify`

Resolve ambiguities in outcomes or strategy.

### `/context.analyze`

Check consistency across constitution, outcomes, and artifacts.

## Capture Methods

The framework supports multiple extraction approaches:

| Method | Script Support | Best For |
|--------|----------------|----------|
| Document Synthesis | `synthesize.sh` | Existing docs → consolidated artifact |
| Interview | `interview-prep.sh` | Tacit knowledge extraction |
| Form/Survey | `generate-form.sh` | Standardized data collection |
| System Export | `export-*.sh` | Structured data from tools |
| Chat Extraction | `extract-thread.sh` | Historical decisions in Slack/Teams |

## Artifact Types

Common knowledge artifacts this framework produces:

| Type | Template | Purpose |
|------|----------|---------|
| Glossary | `glossary-template.md` | Terms, definitions, ownership |
| Process Doc | `process-template.md` | Steps, roles, exceptions |
| Decision Record | `decision-template.md` | Context, alternatives, rationale |
| Authority Map | `authority-template.md` | Who approves what, thresholds |
| System Inventory | `systems-template.md` | Tools, owners, integrations |
| Org Context | `org-template.md` | Structure, responsibilities |

## CLI Tool: `context`

Parallel to SpecKit's `specify` CLI:

```bash
# Initialize a new engagement
context init <engagement-name> --org "Company Name" --scope "Marketing Team"

# Check prerequisites
context check

# List outcomes
context list

# Validate artifacts
context validate
```

## Quality Gates

Each outcome can have checklists in `outcomes/[name]/checklists/`:

- `sources.md` - Are all sources identified and accessible?
- `coverage.md` - Does artifact cover all required topics?
- `validation.md` - Has SME validated the content?
- `integration.md` - Is artifact accessible to AI system?

## Integration with AI Systems

The captured artifacts should be structured for AI consumption:

1. **Indexable**: Clear headings, structured content
2. **Retrievable**: Consistent naming, cross-references
3. **Citable**: Source attribution for AI to reference
4. **Updatable**: Clear ownership and freshness tracking

## Comparison: SpecKit vs Company Context

| Aspect | SpecKit | Company Context |
|--------|---------|-----------------|
| Root folder | `.specify/` | `.context/` |
| Core artifact | Code | Knowledge documents |
| Specification | Feature requirements | Knowledge outcomes |
| Plan | Technical architecture | Capture strategy |
| Tasks | Implementation work | Extraction/synthesis work |
| Implement | Write code | Capture knowledge |
| Validation | Tests pass | SME approval |
| Output | Working software | AI-ready context |
