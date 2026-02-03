---
description: Generate extraction and synthesis tasks from a capture strategy
---

## User Input

```text
$ARGUMENTS
```

You **MUST** consider the user input before proceeding (if not empty).

## Outline

1. **Prerequisites check**:
   - Run `.context/scripts/bash/check-prerequisites.sh --json --require-strategy`
   - Verify outcome.md AND strategy.md exist
   - If not: Stop and instruct user to run prerequisite commands first

2. **Load context**:
   - Read target `outcome.md` (acceptance criteria, dependencies)
   - Read target `strategy.md` (sources, methods, timeline)
   - Load `.context/templates/tasks-template.md`

3. **Parse strategy for task generation**:

   From strategy.md, extract:
   - Document sources → document extraction tasks
   - System sources → system export tasks
   - Human sources → interview tasks
   - Chat sources → chat extraction tasks
   - Artifact structure → synthesis tasks
   - Quality gates → validation tasks

4. **Generate phased task list**:

   **Phase 1: Source Gathering**
   - Access verification tasks
   - Download/export tasks
   - Interview scheduling tasks

   **Phase 2: Extraction**
   - Document extraction tasks
   - Interview execution tasks
   - Chat extraction tasks
   - Data parsing tasks

   **Phase 3: Synthesis**
   - Initial draft creation
   - Conflict reconciliation
   - Gap filling
   - Template application
   - Source attribution

   **Phase 4: Validation**
   - SME review submission
   - Feedback incorporation
   - Acceptance criteria verification
   - Sign-off

   **Phase 5: Integration**
   - Formatting for AI
   - Metadata addition
   - Cross-reference linking
   - Final placement
   - AI retrieval testing

5. **Mark task properties**:
   - `[P]` for tasks that can run in parallel
   - `[B]` for blocking tasks
   - `[KO-###]` linking to outcome ID
   - Estimated effort per task

6. **Add checkpoints**:
   - End-of-phase checkpoints with verification criteria

7. **Calculate summary**:
   - Tasks per phase
   - Parallel task count
   - Total estimated effort

8. **Write tasks file**:
   - Save to `.context/outcomes/[###-name]/tasks.md`
   - Report task count and next steps

## Key Rules

- Every acceptance criterion must have at least one verification task
- Phase dependencies must be respected (no Phase 3 tasks before Phase 2 complete)
- Parallel tasks must truly be independent (no shared resources)

## Next Steps

After tasks are generated:
- Begin capture with `/context.capture`
