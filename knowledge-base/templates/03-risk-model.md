---
id: kb.risk-model
title: Risk Model
owners:
  - risk_model
audiences:
  - engineering
  - qa
  - product
last_reviewed: "{{LAST_REVIEWED_DATE}}"
review_cycle_days: 30
confidence: high
change_frequency: medium
source_refs: []
tags:
  - tier1
  - risk
---

# Risk Model: {{PROJECT_NAME}}

## Purpose

Capture the flows, modules, and release conditions most likely to create regressions, operational incidents, or high-cost review mistakes.

## Scope

Use this file for actionable risk guidance that should influence implementation, review, testing, and incident response. Keep sprint-specific status in `04-active-sprint.md`.

## What is true today

### Risk classification

| Area or module | Risk level | Reason | Required review gate |
|---|---|---|---|
| {{MODULE_1}} | High | {{REASON_1}} | {{GATE_1}} |
| {{MODULE_2}} | Medium | {{REASON_2}} | {{GATE_2}} |
| {{MODULE_3}} | Low | {{REASON_3}} | Standard PR review |

### Fragile areas

| Area | Known issue pattern | Mitigation |
|---|---|---|
| {{AREA_1}} | {{PATTERN_1}} | {{MITIGATION_1}} |

### Example

- Example: "Enrollment state transitions must have integration coverage because repeated regressions have escaped unit tests" is the level of concrete risk guidance this file should keep.

## Key rules

- Update this file when a bug, incident, or review failure reveals new fragility.
- Define the minimum review and test expectation for high-risk areas.
- Record security-sensitive or compliance-sensitive paths explicitly.
- Keep risk statements concrete enough that reviewers can act on them.

## Known gaps / uncertainty

- Missing risk coverage: {{MISSING_RISK_AREAS}}
- Open release concerns: {{OPEN_RELEASE_CONCERNS}}

## Linked evidence

- Incident or RCA doc: {{INCIDENT_DOC_LINK}}
- Test strategy doc: {{TEST_STRATEGY_LINK}}
- Security or compliance reference: {{SECURITY_DOC_LINK}}

## Next review trigger

- Review this file when recurring regressions appear, an incident occurs, a critical flow changes, or release criteria need tighter coverage.
