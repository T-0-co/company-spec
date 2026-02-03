---
description: Execute capture tasks phase by phase, validating artifacts against acceptance criteria
---

## User Input

```text
$ARGUMENTS
```

You **MUST** consider the user input before proceeding (if not empty).

## Outline

1. **Prerequisites check**:
   - Run `.context/scripts/bash/check-prerequisites.sh --json --require-tasks`
   - Verify outcome.md, strategy.md, AND tasks.md all exist
   - If not: Stop and instruct user to run prerequisite commands first

2. **Load context**:
   - Read `.context/memory/constitution.md` (principles)
   - Read target `outcome.md` (acceptance criteria)
   - Read target `strategy.md` (artifact structure)
   - Read target `tasks.md` (task list)

3. **Check for checklists** (if `.context/outcomes/[###]/checklists/` exists):
   - Scan all checklist files
   - Count complete vs incomplete items
   - If incomplete: Ask user whether to proceed

4. **Parse tasks.md**:
   - Identify current phase (first phase with incomplete tasks)
   - Extract task list with properties ([P], [B], [KO-###])
   - Identify parallel task groups

5. **Execute tasks phase by phase**:

   For each phase:

   a. **Start phase**:
      - Report phase name and task count
      - Identify blocking tasks

   b. **Execute tasks**:
      - Sequential tasks: Execute in order
      - Parallel tasks [P]: Can execute together
      - For each task:
        - Report task start
        - Execute task actions
        - Mark complete: `- [ ]` → `- [x]`
        - Report task completion

   c. **Phase checkpoint**:
      - Verify all phase tasks complete
      - Check phase checkpoint criteria
      - Report phase completion
      - Proceed to next phase or stop if errors

6. **Error handling**:
   - Sequential task fails: STOP, report error, suggest fix
   - Parallel task fails: Continue others, report failed task at phase end
   - Blocking task fails: Cannot proceed to next phase

7. **Validation during Phase 4**:
   - For each acceptance criterion, verify artifact meets it
   - Document verification results
   - Flag any criteria not met

8. **Completion**:
   - Verify all tasks complete
   - Verify artifact in final location
   - Verify AI can retrieve artifact
   - Report final status

## Progress Tracking

After each task completion:

```markdown
✓ T### [TASK_DESCRIPTION]
  Files: [FILES_CREATED_OR_MODIFIED]
  Notes: [ANY_RELEVANT_NOTES]
```

## Key Rules

- Never skip phases
- Blocking tasks [B] must complete before phase proceeds
- Always update tasks.md checkboxes as tasks complete
- Report blockers immediately with suggested resolution

## Final Report

```markdown
# Capture Complete: KO-###

## Summary
- Total Tasks: [N]
- Completed: [N]
- Duration: [TIME]

## Artifact Created
- Location: context-artifacts/[TYPE]/[NAME].md
- Validated by: [SME_NAME]
- AI Retrieval: Verified

## Acceptance Criteria
- [x] AC-1: [DESCRIPTION]
- [x] AC-2: [DESCRIPTION]
- [x] AC-3: [DESCRIPTION]

## Next Steps
- [RECOMMENDATIONS]
```
