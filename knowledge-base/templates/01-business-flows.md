---
id: kb.business-flows
title: Business Flows
owners:
  - business_flows
audiences:
  - product
  - engineering
  - qa
last_reviewed: "{{LAST_REVIEWED_DATE}}"
review_cycle_days: 30
confidence: high
change_frequency: medium
source_refs: []
tags:
  - tier1
  - business
---

# Business Flows: {{PROJECT_NAME}}

## Purpose

Capture the user-facing flows, business rules, approvals, and glossary terms that engineering and QA should not rediscover from code alone.

## Scope

Use this file for high-value workflows and business truth. Keep implementation details, UI mechanics, and technical trade-offs out unless they directly affect business behavior.

## What is true today

### Core flows

| Flow ID | Flow name | Initiator | Outcome | Notes |
|---|---|---|---|---|
| BF-01 | {{FLOW_NAME_1}} | {{INITIATOR_1}} | {{OUTCOME_1}} | {{NOTES_1}} |
| BF-02 | {{FLOW_NAME_2}} | {{INITIATOR_2}} | {{OUTCOME_2}} | {{NOTES_2}} |

### Workflow details

#### {{FLOW_NAME_1}}

- Trigger: {{TRIGGER_1}}
- Main path: {{MAIN_PATH_1}}
- Edge cases: {{EDGE_CASES_1}}
- Important business rule: {{BUSINESS_RULE_1}}

#### {{FLOW_NAME_2}}

- Trigger: {{TRIGGER_2}}
- Main path: {{MAIN_PATH_2}}
- Edge cases: {{EDGE_CASES_2}}
- Important business rule: {{BUSINESS_RULE_2}}

### Example

- Example: "Learner submits assessment" should name the trigger, the happy path, approval logic, and what happens if the submission is incomplete.

## Key rules

- Prefer business language over technical design language.
- Keep the highest-value workflows in this file; move history into Tier 2 if needed.
- Update this file whenever business behavior or approval logic changes.
- Add glossary terms when the same business word is repeatedly misunderstood.

## Known gaps / uncertainty

- Missing workflows: {{MISSING_WORKFLOWS}}
- Unresolved business questions: {{OPEN_BUSINESS_QUESTIONS}}

## Linked evidence

- Product requirement doc: {{PRD_LINK}}
- Acceptance criteria source: {{ACCEPTANCE_CRITERIA_LINK}}
- Process or SOP reference: {{PROCESS_DOC_LINK}}

## Next review trigger

- Review this file when a feature changes user behavior, approval logic, role interactions, or business terminology.
