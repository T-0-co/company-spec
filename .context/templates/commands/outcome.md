---
description: Define a knowledge outcome - what artifact is needed for AI to operate effectively
---

## User Input

```text
$ARGUMENTS
```

You **MUST** consider the user input before proceeding (if not empty).

## Outline

1. **Prerequisites check**:
   - Verify `.context/memory/constitution.md` exists
   - If not: Stop and instruct user to run `/context.constitution` first
   - Load constitution for context (scope, AI goal, boundaries)

2. **Determine outcome number**:
   - Scan `.context/outcomes/` for existing folders
   - Find highest number (###-name pattern)
   - Assign next sequential number

3. **Generate outcome name**:
   - From user input, create 2-4 word identifier
   - Use noun or noun-phrase format (e.g., "authority-map", "product-glossary")
   - Create folder: `.context/outcomes/[###-outcome-name]/`

4. **Load template**: Read `.context/templates/outcome-template.md`

5. **Populate outcome specification**:

   From user input or by asking:
   - What knowledge artifact is needed?
   - Why does the AI need it? What decisions/actions does it enable?
   - What's the current gap without this knowledge?
   - Priority (P1/P2/P3) and justification

   Generate:
   - Acceptance criteria (Given/When/Then format)
   - Known and potential knowledge sources
   - Proposed capture methods
   - Scope clarifications (in/out)
   - Dependencies on other outcomes

6. **Validate against constitution**:
   - Is this within defined scope boundaries?
   - Does it serve the stated AI deployment goal?
   - Any sensitive area considerations?

7. **Write outcome file**:
   - Save to `.context/outcomes/[###-outcome-name]/outcome.md`
   - Report outcome ID (KO-###) and next steps

## Clarification Handling

If user input is vague, ask maximum 3 clarifying questions:

1. What specific knowledge gap are we addressing?
2. How will the AI use this knowledge?
3. What priority should this have (P1 = blocking, P2 = important, P3 = nice to have)?

## Key Rules

- Maximum 3 `[NEEDS CLARIFICATION]` markers in output
- All outcomes must trace to AI deployment goal
- Acceptance criteria must be testable

## Next Steps

After outcome is defined:
- Plan capture approach with `/context.strategy`
