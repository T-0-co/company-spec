---
description: Plan the capture approach for a knowledge outcome - sources, methods, timeline
---

## User Input

```text
$ARGUMENTS
```

You **MUST** consider the user input before proceeding (if not empty).

## Outline

1. **Prerequisites check**:
   - Run `.context/scripts/bash/check-prerequisites.sh --json`
   - Verify outcome.md exists for the target outcome
   - If not: Stop and instruct user to run `/context.outcome` first

2. **Load context**:
   - Read `.context/memory/constitution.md` (principles, boundaries)
   - Read target `outcome.md` (artifact definition, acceptance criteria)
   - Load `.context/templates/strategy-template.md`

3. **Constitution check**:
   - Verify outcome is within scope boundaries
   - Identify applicable capture principles
   - Note any sensitive area handling requirements

4. **Analyze knowledge sources**:

   From outcome.md, categorize:
   - Document sources (existing docs to synthesize)
   - System sources (data to export)
   - Human sources (people to interview)
   - Chat sources (threads to extract)

5. **Select capture approach**:

   For each source type, determine:
   - Primary capture method
   - Tools/scripts needed
   - Access requirements
   - Estimated effort

6. **Design artifact structure**:
   - Output format (markdown, JSON, etc.)
   - Template/schema for the artifact
   - Cross-references to other artifacts

7. **Define quality gates**:
   - Pre-capture gates (what must be true before starting)
   - Post-capture gates (what must be true when complete)

8. **Risk assessment**:
   - What could block capture?
   - What's the mitigation?

9. **Estimate timeline**:
   - Phase breakdown with durations
   - Dependencies between phases

10. **Write strategy file**:
    - Save to `.context/outcomes/[###-name]/strategy.md`
    - Report completion and next steps

## Key Rules

- Strategy must address ALL acceptance criteria from outcome.md
- Every source must have an access status
- Timeline must be realistic given constraints in constitution

## Next Steps

After strategy is complete:
- Generate capture tasks with `/context.tasks`
