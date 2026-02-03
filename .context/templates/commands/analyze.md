---
description: Check consistency across constitution, outcomes, strategies, and artifacts
---

## User Input

```text
$ARGUMENTS
```

You **MUST** consider the user input before proceeding (if not empty).

## Outline

1. **Load all documents**:
   - `.context/memory/constitution.md`
   - All `.context/outcomes/*/outcome.md`
   - All `.context/outcomes/*/strategy.md`
   - All `.context/outcomes/*/tasks.md`
   - All `context-artifacts/**/*`

2. **Constitution consistency checks**:

   - [ ] All outcomes within defined scope
   - [ ] All outcomes serve stated AI deployment goal
   - [ ] No outcomes violate sensitive area boundaries
   - [ ] Capture principles consistently applied

3. **Outcome consistency checks**:

   For each outcome:
   - [ ] Has acceptance criteria
   - [ ] Has priority assigned
   - [ ] Dependencies reference valid outcomes
   - [ ] No circular dependencies

4. **Strategy consistency checks**:

   For each strategy:
   - [ ] References valid outcome
   - [ ] All sources from outcome are addressed
   - [ ] All acceptance criteria have coverage plan
   - [ ] Timeline is realistic

5. **Tasks consistency checks**:

   For each tasks.md:
   - [ ] References valid strategy
   - [ ] All phases have tasks
   - [ ] Parallel markers are valid (no hidden dependencies)
   - [ ] All acceptance criteria have verification tasks

6. **Artifact consistency checks**:

   For each artifact:
   - [ ] Has source attribution
   - [ ] Has last-verified date
   - [ ] Has owner assigned
   - [ ] Cross-references are valid

7. **Cross-document checks**:

   - [ ] All outcomes referenced in strategies exist
   - [ ] All dependencies between outcomes are mutual
   - [ ] No orphaned artifacts (no outcome reference)
   - [ ] No missing artifacts (outcome complete, no artifact)

8. **Generate report**:

   ```markdown
   # Consistency Analysis Report

   **Date**: [DATE]
   **Scope**: [WHAT_WAS_ANALYZED]

   ## Summary

   | Check Category | Pass | Fail | Warning |
   |----------------|------|------|---------|
   | Constitution | [N] | [N] | [N] |
   | Outcomes | [N] | [N] | [N] |
   | Strategies | [N] | [N] | [N] |
   | Tasks | [N] | [N] | [N] |
   | Artifacts | [N] | [N] | [N] |
   | Cross-Document | [N] | [N] | [N] |

   ## Issues Found

   ### Critical (Must Fix)
   - [ISSUE_1]: [DESCRIPTION] - [LOCATION]

   ### Warnings (Should Review)
   - [WARNING_1]: [DESCRIPTION] - [LOCATION]

   ## Recommendations
   1. [RECOMMENDATION_1]
   2. [RECOMMENDATION_2]
   ```

## Key Rules

- Report ALL issues found, not just first
- Categorize by severity (Critical, Warning, Info)
- Provide specific file locations for issues
- Suggest fixes where possible

## Next Steps

After analysis:
- Fix critical issues before proceeding with capture
- Review warnings and decide on action
