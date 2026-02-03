---
description: Resolve ambiguities and [NEEDS CLARIFICATION] markers in outcomes or strategies
---

## User Input

```text
$ARGUMENTS
```

You **MUST** consider the user input before proceeding (if not empty).

## Outline

1. **Identify target**:
   - If user specifies outcome: Use that outcome folder
   - If not: List outcomes with unresolved clarifications

2. **Scan for clarifications needed**:
   - Search outcome.md for `[NEEDS CLARIFICATION]` markers
   - Search strategy.md for `[NEEDS CLARIFICATION]` markers
   - Search for `Open Questions` sections with unchecked items

3. **Prioritize clarifications**:
   - Critical (blocking capture): Ask first
   - Important (affects quality): Ask second
   - Minor (nice to have): Ask last

4. **Present questions**:

   For each clarification needed:

   ```markdown
   ## Question [N]: [TOPIC]

   **Context**: [WHY_THIS_MATTERS]
   **Current State**: [WHAT_WE_KNOW]

   **Options**:
   | Option | Description | Implications |
   |--------|-------------|--------------|
   | A | [OPTION_A] | [IMPLICATIONS] |
   | B | [OPTION_B] | [IMPLICATIONS] |
   | C | Custom | [USER_PROVIDES] |

   **Recommendation**: [IF_APPLICABLE]
   ```

5. **Collect responses**:
   - Wait for user input
   - Validate response is actionable

6. **Update documents**:
   - Replace `[NEEDS CLARIFICATION]` with resolved value
   - Check off resolved open questions
   - Add decision rationale where appropriate

7. **Report completion**:
   - List clarifications resolved
   - List any remaining clarifications
   - Suggest next steps

## Key Rules

- Maximum 5 questions per clarification session
- Provide recommended option when possible
- Document decision rationale for future reference

## Next Steps

After clarifications resolved:
- If outcome.md was updated: Proceed to `/context.strategy`
- If strategy.md was updated: Proceed to `/context.tasks`
