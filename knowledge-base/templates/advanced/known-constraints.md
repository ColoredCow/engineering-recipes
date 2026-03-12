---
id: kb.known-constraints
title: Known Constraints
owners:
  - known_constraints
audiences:
  - engineering
  - product
  - qa
last_reviewed: "{{LAST_REVIEWED_DATE}}"
review_cycle_days: 90
confidence: medium
change_frequency: low
source_refs: []
tags:
  - tier2
  - constraints
---

# Known Constraints: {{PROJECT_NAME}}

## Purpose

Document hard technical, business, or operational constraints that teams should not have to rediscover repeatedly.

## Scope

Keep only durable constraints here. Temporary sprint blockers belong in `04-active-sprint.md`.

## Update rules

- Add constraints that materially shape implementation choices.
- State the constraint and why it exists.
- Remove constraints only when the underlying limitation is genuinely gone.

## Constraint list

- {{CONSTRAINT_1}}
- {{CONSTRAINT_2}}
- {{CONSTRAINT_3}}

## Example

- Course completion data must be retained for audit purposes even if a learner account is later deactivated.
