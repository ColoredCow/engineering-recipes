---
id: kb.integration-map
title: Integration Map
owners:
  - integration_map
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
  - integration-map
---

# Integration Map: {{PROJECT_NAME}}

## Purpose

List the external systems and cross-boundary dependencies that materially affect implementation, delivery risk, or incident response.

## Scope

Only keep integrations that matter to reliability or delivery. Skip purely internal calls that are already obvious from the main architecture file.

## Update rules

- Update this file when a new external dependency is added or a contract changes.
- Keep auth, failure mode, and fallback ownership explicit.
- Link deeper technical details from outside this file if needed.

## Integration table

| System | Purpose | Auth | Failure mode | Fallback or owner |
|---|---|---|---|---|
| {{SYSTEM_1}} | {{PURPOSE_1}} | {{AUTH_1}} | {{FAILURE_1}} | {{FALLBACK_1}} |

## Example

| System | Purpose | Auth | Failure mode | Fallback or owner |
|---|---|---|---|---|
| Payment gateway | Collect course fees | API key + webhook signing | Delayed webhook confirmation | Finance ops + retry job |
