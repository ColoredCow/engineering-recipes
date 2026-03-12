---
id: kb.incident-log
title: Incident Log
owners:
  - incident_log
audiences:
  - engineering
  - qa
  - product
last_reviewed: "{{LAST_REVIEWED_DATE}}"
review_cycle_days: 90
confidence: medium
change_frequency: medium
source_refs: []
tags:
  - tier2
  - incident-log
---

# Incident Log: {{PROJECT_NAME}}

## Purpose

Append-only record of incidents, regressions, or reliability events that should inform future work and reduce repeat failures.

## Scope

Capture events that changed detection, prevention, or recovery expectations. Skip transient noise that taught the team nothing durable.

## Update rules

- Append newest incidents at the top.
- Record symptom, root cause, fix, and prevention.
- Link the incident to risk model updates when the learning changes future review or test expectations.

## Entry template

### {{DATE}}: {{INCIDENT_TITLE}}

- Symptom: {{INCIDENT_SYMPTOM}}
- Root cause: {{INCIDENT_ROOT_CAUSE}}
- Fix: {{INCIDENT_FIX}}
- Prevention: {{INCIDENT_PREVENTION}}

## Example entry

### 2026-03-07: Background sync stopped processing retry jobs

- Symptom: Retry queues grew for two hours and learner notifications were delayed.
- Root cause: A scheduler change removed the retry worker from one environment.
- Fix: Restore the worker and replay the queued jobs.
- Prevention: Add a deployment smoke check that confirms every required worker is running.
