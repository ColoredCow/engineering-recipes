---
id: kb.active-sprint
title: Active Sprint
owners:
  - active_sprint
audiences:
  - engineering
  - product
  - qa
last_reviewed: "{{LAST_REVIEWED_DATE}}"
review_cycle_days: 7
confidence: medium
change_frequency: high
source_refs: []
tags:
  - tier1
  - sprint
---

# Active Sprint: {{PROJECT_NAME}}

## Purpose

Track the current sprint goal, active work, blockers, and recent completions so planning and execution agents do not need to reconstruct current delivery state from scratch.

## Scope

This file is the canonical volatile Tier 1 file. Keep it focused on the current sprint or active delivery window. Archive long-running history into project systems of record or Tier 2 if needed.

## What is true today

### Sprint summary

- Sprint: {{SPRINT_NAME_OR_NUMBER}}
- Sprint goal: {{SPRINT_GOAL}}
- Period: {{SPRINT_START_DATE}} to {{SPRINT_END_DATE}}

### Active issues

| Issue | Title | Assignee | Status | Notes |
|---|---|---|---|---|
| #{{ISSUE_NUMBER_1}} | {{ISSUE_TITLE_1}} | {{ASSIGNEE_1}} | {{STATUS_1}} | {{PROGRESS_NOTE_1}} |
| #{{ISSUE_NUMBER_2}} | {{ISSUE_TITLE_2}} | {{ASSIGNEE_2}} | {{STATUS_2}} | {{PROGRESS_NOTE_2}} |

### Blocked items

| Issue | Blocker | Owner |
|---|---|---|
| #{{BLOCKED_ISSUE}} | {{BLOCKER_DESCRIPTION}} | {{BLOCKER_OWNER}} |

### Completed this sprint

| Issue | Title | Completed on |
|---|---|---|
| #{{DONE_ISSUE_1}} | {{DONE_TITLE_1}} | {{DONE_DATE_1}} |

### Example

- Example: when issue `#123` moves from active work to review, update the existing row instead of inserting a duplicate issue entry.

## Key rules

- Keep this file current; it is the default KB automation target.
- Update issue rows in place to avoid duplicates.
- Move completed work into the completion table when it is done or closed.
- Keep notes short, factual, and tied to visible sprint state.

## Known gaps / uncertainty

- Missing issue context: {{MISSING_SPRINT_CONTEXT}}
- Unresolved blockers: {{OPEN_BLOCKERS}}

## Linked evidence

- Sprint board: {{SPRINT_BOARD_LINK}}
- Delivery issue query: {{ISSUE_QUERY_LINK}}
- Sprint review notes: {{SPRINT_REVIEW_LINK}}

## Next review trigger

- Review this file whenever issue state changes, blockers appear, sprint scope changes, or the sprint window rolls over.
