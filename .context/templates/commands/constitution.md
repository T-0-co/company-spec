---
description: Establish or update the engagement definition and capture principles for a company context project
---

## User Input

```text
$ARGUMENTS
```

You **MUST** consider the user input before proceeding (if not empty).

## Outline

1. **Check existing constitution**: Look for `.context/memory/constitution.md`
   - If exists: Load and prepare for update workflow
   - If not exists: Prepare for creation workflow

2. **Load template**: Read `.context/templates/constitution-template.md`

3. **Gather engagement definition** (Part 1):

   If user input is empty or incomplete, ask for:
   - Organization name and industry
   - Scope (whole company, department, team, project)
   - AI deployment goal (what capability needs this context?)
   - Key stakeholders (sponsor, SMEs, AI users)
   - Boundaries (in scope, out of scope, sensitive areas)
   - Constraints (timeline, budget, access, compliance)

4. **Establish capture principles** (Part 2):

   Present default principles from template and ask:
   - Which principles apply to this engagement?
   - Are there additional principles needed?
   - Should any default principles be modified?

5. **Generate constitution**:
   - Replace all placeholders with gathered values
   - Set version to 1.0 (or increment if updating)
   - Set dates appropriately

6. **Validate output**:
   - No unexplained bracket tokens `[...]` remain
   - Dates in ISO format (YYYY-MM-DD)
   - All required sections populated

7. **Write constitution**:
   - Save to `.context/memory/constitution.md`
   - Report success and next steps

## Key Rules

- Use absolute paths
- Constitution is foundational - no outcomes can be created without it
- Engagement definition must be complete before proceeding
- Capture principles can be minimal initially and expanded later

## Next Steps

After constitution is established:
- Create first knowledge outcome with `/context.outcome`
