# Capture Tasks: [OUTCOME_NAME]

**Outcome**: KO-[###] | **Branch**: `[###-outcome-name]` | **Generated**: [DATE]
**Input**: Strategy from `strategy.md`

---

## Task Legend

- `[P]` - Can run in parallel (no dependencies on other tasks)
- `[KO-###]` - Links to specific knowledge outcome
- `[B]` - Blocking (must complete before next phase)

---

## Phase 1: Source Gathering

*Collect and organize all source materials*

- [ ] T001 [B] Verify access to all identified document sources
- [ ] T002 [P] Download/export documents from [SOURCE_1]
- [ ] T003 [P] Download/export documents from [SOURCE_2]
- [ ] T004 [P] Export data from [SYSTEM_1]
- [ ] T005 Schedule interviews with identified knowledge holders
- [ ] T006 [P] Extract relevant Slack/Teams threads from [CHANNEL]

**Phase 1 Checkpoint**:

- [ ] All documents collected in working directory
- [ ] All system exports completed
- [ ] All interviews scheduled
- [ ] Chat extractions complete

---

## Phase 2: Extraction

*Extract knowledge from sources*

### Document Extraction

- [ ] T007 [P] [KO-###] Extract key information from [DOC_1]
- [ ] T008 [P] [KO-###] Extract key information from [DOC_2]
- [ ] T009 [P] [KO-###] Parse and structure data from [SYSTEM_EXPORT]

### Interview Execution

- [ ] T010 [KO-###] Conduct interview with [NAME] - [TOPIC]
  - Duration: [MINUTES]
  - Key questions: [LINK_TO_QUESTIONS]
- [ ] T011 [KO-###] Conduct interview with [NAME] - [TOPIC]
  - Duration: [MINUTES]
  - Key questions: [LINK_TO_QUESTIONS]
- [ ] T012 [P] Transcribe and structure interview notes

### Chat Extraction

- [ ] T013 [P] [KO-###] Identify key decisions from [THREAD_1]
- [ ] T014 [P] [KO-###] Extract process details from [THREAD_2]

**Phase 2 Checkpoint**:

- [ ] All document extractions complete
- [ ] All interviews conducted and notes structured
- [ ] Chat extractions organized

---

## Phase 3: Synthesis

*Combine extracted knowledge into coherent artifact*

- [ ] T015 [B] [KO-###] Create initial artifact draft from extractions
- [ ] T016 [KO-###] Reconcile conflicting information from sources
- [ ] T017 [KO-###] Fill gaps identified during extraction
- [ ] T018 [KO-###] Add cross-references to related artifacts
- [ ] T019 [KO-###] Apply artifact template structure
- [ ] T020 [KO-###] Add source attribution to all sections

**Phase 3 Checkpoint**:

- [ ] Complete artifact draft exists
- [ ] No unresolved conflicts
- [ ] All gaps documented or filled
- [ ] Source attribution complete

---

## Phase 4: Validation

*Verify accuracy and completeness with SMEs*

- [ ] T021 [B] [KO-###] Submit artifact for SME review - [NAME]
- [ ] T022 [KO-###] Address SME feedback round 1
- [ ] T023 [KO-###] Verify against acceptance criteria AC-1
- [ ] T024 [KO-###] Verify against acceptance criteria AC-2
- [ ] T025 [KO-###] Verify against acceptance criteria AC-3
- [ ] T026 [KO-###] Final SME sign-off

**Phase 4 Checkpoint**:

- [ ] SME has validated content
- [ ] All acceptance criteria verified
- [ ] No outstanding issues

---

## Phase 5: Integration

*Prepare artifact for AI consumption*

- [ ] T027 [KO-###] Format artifact for AI indexing
- [ ] T028 [KO-###] Add metadata (last verified, owner, review frequency)
- [ ] T029 [KO-###] Create cross-reference links
- [ ] T030 [KO-###] Move to final location in `context-artifacts/`
- [ ] T031 [KO-###] Update artifact index/registry
- [ ] T032 Test AI retrieval of new artifact

**Phase 5 Checkpoint**:

- [ ] Artifact in final location
- [ ] Metadata complete
- [ ] AI can retrieve and use artifact

---

## Summary

| Phase | Total Tasks | Parallel Tasks | Estimated Effort |
|-------|-------------|----------------|------------------|
| 1. Source Gathering | [N] | [N] | [HOURS/DAYS] |
| 2. Extraction | [N] | [N] | [HOURS/DAYS] |
| 3. Synthesis | [N] | [N] | [HOURS/DAYS] |
| 4. Validation | [N] | [N] | [HOURS/DAYS] |
| 5. Integration | [N] | [N] | [HOURS/DAYS] |
| **Total** | [N] | [N] | [HOURS/DAYS] |

---

## Blockers & Issues

| Issue | Blocking Task | Status | Resolution |
|-------|---------------|--------|------------|
| [ISSUE] | T### | [Open/Resolved] | [ACTION] |

---

## Completion Log

| Task | Completed | Notes |
|------|-----------|-------|
| T001 | [DATE] | [NOTES] |
