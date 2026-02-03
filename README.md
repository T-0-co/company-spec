<div align="center">
    <h1>🏢 Company Spec</h1>
    <h3><em>Structured organizational knowledge capture for AI deployment</em></h3>
</div>

<p align="center">
    <strong>A toolkit that enables systematic discovery, extraction, and documentation of company knowledge required for effective AI deployment.</strong>
</p>

<p align="center">
    <em>Built on <a href="https://github.com/github/spec-kit">GitHub's Spec Kit</a> methodology, adapted for knowledge capture instead of software development.</em>
</p>

---

## Table of Contents

- [The Problem](#-the-problem)
- [The Spec Kit Connection](#-the-spec-kit-connection)
- [How Company Spec Works](#-how-company-spec-works)
- [Get Started](#-get-started)
- [Core Methodology](#-core-methodology)
- [The Five Phases](#-the-five-phases)
- [CLI Reference](#-cli-reference)
- [Directory Structure](#-directory-structure)
- [Capture Methods](#-capture-methods)
- [Knowledge Artifact Types](#-knowledge-artifact-types)
- [License](#-license)

---

## 🤔 The Problem

When deploying AI solutions within a company, the AI needs **context** to generate real value:

| Question | Example |
|----------|---------|
| **Who decides what?** | Decision-making authority, approval workflows, escalation paths |
| **What do terms mean?** | Internal jargon, product names, project codenames |
| **How do we work?** | Processes, conventions, unwritten rules |
| **What matters most?** | Priorities, constraints, non-negotiables |
| **Where is everything?** | Systems, tools, documentation locations |

This knowledge exists in various states:

| State | Example | Challenge |
|-------|---------|-----------|
| **Documented & usable** | Public API docs, official policies | Just needs indexing |
| **Documented but fragmented** | Scattered Confluence pages, old wikis | Needs synthesis |
| **Documented but wrong format** | Tribal knowledge in Slack threads | Needs transformation |
| **Undocumented** | "Ask Sarah, she knows" | Needs extraction |

**Most AI deployments underperform because this context work is ad-hoc, incomplete, or never done.**

The AI assistant that doesn't know your approval thresholds will suggest actions that get rejected. The chatbot that doesn't understand your product terminology will confuse customers. The code assistant that doesn't know your architectural constraints will generate non-compliant solutions.

---

## 🔗 The Spec Kit Connection

Company Spec is directly inspired by and built upon [GitHub's Spec Kit](https://github.com/github/spec-kit), an open-source toolkit for **Specification-Driven Development (SDD)**.

### What Spec Kit Does

Spec Kit inverts traditional software development: instead of specifications serving code, **code serves specifications**. The workflow:

1. **Constitution** → Establish immutable project principles
2. **Specify** → Transform ideas into precise specifications with user stories
3. **Plan** → Convert specs into technical architecture
4. **Tasks** → Derive executable, parallelizable tasks
5. **Implement** → Execute tasks phase by phase

This structured approach ensures consistency, traceability, and quality in software development.

### What We Adapted

We recognized that the same structured approach could solve the **knowledge capture problem** for AI deployment:

| Spec Kit (Software) | Company Spec (Knowledge) |
|---------------------|--------------------------|
| Project principles | Engagement definition + capture principles |
| Feature specifications | Knowledge outcome definitions |
| Technical architecture | Capture strategy (sources, methods) |
| Implementation tasks | Extraction and synthesis tasks |
| Code execution | Knowledge capture and validation |

Instead of specifications driving code generation, **knowledge specifications drive context artifact creation**.

### Credit

Company Spec would not exist without GitHub's Spec Kit. We've adapted their methodology, workflow patterns, CLI structure, and template approach. The original Spec Kit is available at [github.com/github/spec-kit](https://github.com/github/spec-kit) and documented at [github.github.io/spec-kit](https://github.github.io/spec-kit/).

---

## 🧠 How Company Spec Works

### The Core Insight

Just as Spec Kit makes specifications the **source of truth** for software (not an afterthought), Company Spec makes knowledge specifications the source of truth for AI context.

Before capturing any knowledge, you must:
1. **Define the engagement** - Who is this for? What's the scope? What AI capability needs this context?
2. **Specify the outcomes** - What knowledge artifacts are needed? How will the AI use them?
3. **Plan the capture** - Where does this knowledge exist? How will we extract it?
4. **Execute systematically** - Work through extraction tasks phase by phase
5. **Validate against criteria** - Does the artifact actually enable the AI to work effectively?

### The Transformation

| Traditional Approach | Company Spec Approach |
|---------------------|----------------------|
| Ad-hoc knowledge gathering | Structured engagement definition |
| "We need some docs for the AI" | Specific knowledge outcomes with acceptance criteria |
| Interview whoever's available | Mapped knowledge sources and stakeholders |
| Dump everything into a folder | Phased extraction with validation |
| Hope the AI figures it out | Verified artifacts that pass acceptance criteria |

---

## ⚡ Get Started

### 1. Install Company Spec CLI

**Option 1: Persistent Installation (Recommended)**

```bash
uv tool install company-spec --from git+https://github.com/T-0-co/company-spec.git
```

Then use directly:

```bash
companyspec init my-engagement --org "Acme Corp" --scope team
```

**Option 2: One-time Usage**

```bash
uvx --from git+https://github.com/T-0-co/company-spec.git companyspec init my-engagement
```

### 2. Initialize Your Engagement

```bash
# Create new engagement with interactive setup
companyspec init acme-marketing --org "Acme Corp" --scope team --goal "AI content assistant"

# Or initialize in current directory
companyspec init . --org "Company Name"
```

### 3. Complete the Constitution

Edit `.context/memory/constitution.md` to define:
- Organization and scope boundaries
- AI deployment goal
- Key stakeholders
- Capture principles

### 4. Use Slash Commands with Your AI Agent

```
/context.constitution  - Review and finalize engagement setup
/context.outcome       - Define knowledge artifacts needed
/context.strategy      - Plan capture approach
/context.tasks         - Generate extraction tasks
/context.capture       - Execute and validate
```

---

## 📚 Core Methodology

### The Constitution: Two Parts

The constitution is the foundation of every engagement, containing both **facts** and **rules**.

#### Part 1: Engagement Definition (Factual)

Establishes the "playing field" - what context we're capturing and for whom:

```markdown
## Engagement Definition

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

#### Part 2: Capture Principles (Normative)

Rules governing how knowledge is captured and maintained:

```markdown
## Capture Principles

### Article I: Source Attribution
Every artifact must cite its authoritative source or knowledge holder.

### Article II: Currency Tracking
All artifacts must include last-verified date and owner.

### Article III: Completeness Over Perfection
Capture "good enough" knowledge quickly; refine based on AI usage feedback.

### Article IV: Context Preservation
Document the "why" behind processes, not just the "what."

### Article V: Validation Required
No artifact is complete until validated by a subject matter expert.
```

---

## 🎯 The Five Phases

### Phase 1: Constitution

**Purpose**: Establish the engagement scope and ground rules

**Output**: `.context/memory/constitution.md`

**Key Questions**:
- What organization/team are we capturing knowledge for?
- What AI capability needs this context?
- Who are the key stakeholders?
- What's in scope and out of scope?

### Phase 2: Outcome

**Purpose**: Define what knowledge artifacts are needed

**Output**: `.context/outcomes/[###-name]/outcome.md`

**Key Elements**:
- Knowledge artifact description
- Why the AI needs it
- Acceptance criteria (Given/When/Then)
- Known and potential sources
- Priority (P1/P2/P3)

**Example**:
```markdown
## KO-001: Brand Voice Guidelines

**Priority**: P1 (blocking for content generation)

**Outcome**: Structured documentation of tone, vocabulary, and style rules.

**Acceptance Criteria**:
- Given the AI is drafting marketing content
- When it references the brand voice guidelines
- Then it produces content that passes brand review without tone corrections
```

### Phase 3: Strategy

**Purpose**: Plan how to capture the knowledge

**Output**: `.context/outcomes/[###-name]/strategy.md`

**Key Elements**:
- Primary capture method (synthesis, interview, export, etc.)
- Source analysis (documents, systems, people)
- Artifact structure/template
- Quality gates
- Timeline estimate

### Phase 4: Tasks

**Purpose**: Break down capture into executable work items

**Output**: `.context/outcomes/[###-name]/tasks.md`

**Task Phases**:
1. **Source Gathering** - Collect and organize materials
2. **Extraction** - Extract knowledge from sources
3. **Synthesis** - Combine into coherent artifact
4. **Validation** - SME review and approval
5. **Integration** - Format for AI consumption

**Task Markers**:
- `[P]` - Can run in parallel
- `[B]` - Blocking (must complete before next phase)
- `[KO-###]` - Links to outcome

### Phase 5: Capture

**Purpose**: Execute tasks and validate artifacts

**Process**:
1. Work through tasks phase by phase
2. Mark completion in tasks.md (`- [ ]` → `- [x]`)
3. Checkpoint after each phase
4. Validate against acceptance criteria
5. Get SME sign-off
6. Place artifact in `context-artifacts/`

---

## 🔧 CLI Reference

### Commands

| Command | Description |
|---------|-------------|
| `companyspec init <name>` | Initialize new engagement |
| `companyspec init .` | Initialize in current directory |
| `companyspec check` | Check engagement status |
| `companyspec list` | List all knowledge outcomes |
| `companyspec version` | Show version info |

### init Options

```bash
companyspec init <name> [OPTIONS]

Options:
  --org, -o TEXT      Organization name (required)
  --scope, -s TEXT    Scope: company, division, department, team, project
  --goal, -g TEXT     AI deployment goal
  --here              Initialize in current directory
  --force             Force init even if not empty
  --no-git            Skip git initialization
```

### Slash Commands (AI Agent)

| Command | Purpose | Prerequisite |
|---------|---------|--------------|
| `/context.constitution` | Establish engagement + principles | None |
| `/context.outcome` | Define knowledge artifact needed | Constitution |
| `/context.strategy` | Plan capture approach | Outcome |
| `/context.tasks` | Generate extraction tasks | Strategy |
| `/context.capture` | Execute and validate | Tasks |
| `/context.clarify` | Resolve ambiguities | Any doc with `[NEEDS CLARIFICATION]` |
| `/context.analyze` | Check consistency | Any time |

---

## 📁 Directory Structure

After initialization:

```
my-engagement/
├── .context/
│   ├── memory/
│   │   └── constitution.md     # Engagement definition + principles
│   │
│   ├── outcomes/               # Knowledge outcomes
│   │   └── 001-brand-voice/
│   │       ├── outcome.md      # What artifact is needed
│   │       ├── strategy.md     # How to capture it
│   │       └── tasks.md        # Extraction work items
│   │
│   ├── templates/              # Document templates
│   │   ├── constitution-template.md
│   │   ├── outcome-template.md
│   │   ├── strategy-template.md
│   │   ├── tasks-template.md
│   │   └── commands/           # Slash command definitions
│   │
│   └── scripts/
│       └── bash/               # Automation scripts
│
└── context-artifacts/          # Captured knowledge outputs
    ├── glossaries/
    ├── processes/
    ├── decisions/
    ├── authorities/
    └── systems/
```

---

## 🔍 Capture Methods

Company Spec supports multiple extraction approaches:

| Method | Best For | Output |
|--------|----------|--------|
| **Document Synthesis** | Existing written knowledge | Consolidated artifact |
| **Interview** | Tacit knowledge, context, "why" | Transcript → structured doc |
| **Form/Survey** | Standardized data collection | Structured responses |
| **System Export** | Structured data in tools | Raw data → formatted artifact |
| **Observation** | Process understanding | Process documentation |
| **Chat Extraction** | Historical decisions in threads | Decision records |

The strategy phase determines which methods apply to each outcome based on where the knowledge currently exists.

---

## 📋 Knowledge Artifact Types

Common artifacts this framework produces:

| Type | Purpose | Example Content |
|------|---------|-----------------|
| **Glossary** | Term definitions | Product names, internal jargon, acronyms |
| **Process Doc** | How work flows | Steps, roles, exceptions, escalation |
| **Decision Record** | Why choices were made | Context, alternatives, rationale |
| **Authority Map** | Who approves what | Thresholds, delegation rules |
| **System Inventory** | Tool landscape | Owners, integrations, access |
| **Org Context** | How team works | Structure, responsibilities, norms |

Each artifact type has a template in `.context/templates/` ensuring consistency.

---

## 🎯 Success Metrics

The framework succeeds when:

1. **Coverage** - All critical knowledge areas have documented artifacts
2. **Accessibility** - AI systems can retrieve relevant context
3. **Accuracy** - Artifacts reflect actual company reality
4. **Currency** - Knowledge stays updated as company evolves
5. **Actionability** - AI makes better decisions using the context

---

## 🛠️ Requirements

- Python 3.11+
- [uv](https://docs.astral.sh/uv/) (recommended) or pip
- Git (optional, for repository initialization)
- An AI coding assistant (Claude Code, GitHub Copilot, etc.) for slash commands

---

## 📖 Related Work

- [GitHub Spec Kit](https://github.com/github/spec-kit) - The original framework this is built upon
- [Spec-Driven Development](https://github.github.io/spec-kit/) - Spec Kit methodology documentation
- [Architecture Decision Records](https://adr.github.io/) - Related pattern for decision documentation

---

## 📄 License

MIT

---

<div align="center">
    <p><strong>Built with ❤️ by <a href="https://t-0.dev">T-0</a></strong></p>
    <p><em>Standing on the shoulders of <a href="https://github.com/github/spec-kit">GitHub's Spec Kit</a></em></p>
</div>
