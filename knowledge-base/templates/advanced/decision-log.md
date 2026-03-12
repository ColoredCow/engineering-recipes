---
id: kb.decision-log
title: Decision Log
owners:
  - decision_log
audiences:
  - engineering
  - product
  - qa
last_reviewed: "{{LAST_REVIEWED_DATE}}"
review_cycle_days: 90
confidence: medium
change_frequency: medium
source_refs: []
tags:
  - tier2
  - decision-log
---

# Decision Log: {{PROJECT_NAME}}

## Purpose

Append-only record of meaningful architecture or product decisions that should remain discoverable after the immediate implementation work is over.

## Scope

Capture decisions that changed system boundaries, delivery risk, or business behavior. Skip trivial implementation details.

## Update rules

- Append newest entries at the top.
- Keep each entry under 6 bullets.
- Record context, decision, trade-off, and follow-up.

## Entry template

### {{DATE}}: {{DECISION_TITLE}}

- Context: {{DECISION_CONTEXT}}
- Decision: {{DECISION_TAKEN}}
- Trade-off: {{DECISION_TRADEOFF}}
- Follow-up: {{DECISION_FOLLOWUP}}

## Example entry

### 2026-03-07: Cache read-heavy report queries for five minutes

- Context: The report endpoint was timing out under repeated staff queries.
- Decision: Add a short-lived cache around the aggregated report response.
- Trade-off: Metrics may be slightly stale for a few minutes.
- Follow-up: Revisit cache invalidation if staff workflows become real-time.
