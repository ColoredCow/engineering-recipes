---
id: kb.architecture
title: Architecture
owners:
  - architecture
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
  - architecture
---

# Architecture: {{PROJECT_NAME}}

## Purpose

Describe the current system boundaries, modules, integration points, and non-negotiable engineering rules that should shape implementation and review.

## Scope

Use this file for architecture that is true today. Keep long historical reasoning and deep decision history in Tier 2 logs such as `advanced/decision-log.md`.

## What is true today

### Tech stack

| Layer | Technology | Version | Notes |
|---|---|---|---|
| {{LAYER_1}} | {{TECH_1}} | {{VERSION_1}} | {{NOTES_1}} |
| {{LAYER_2}} | {{TECH_2}} | {{VERSION_2}} | {{NOTES_2}} |
| {{LAYER_3}} | {{TECH_3}} | {{VERSION_3}} | {{NOTES_3}} |

### Ownership boundaries

| Path or module | Responsibility | Must not contain |
|---|---|---|
| `{{DIR_1}}` | {{RESPONSIBILITY_1}} | {{FORBIDDEN_1}} |
| `{{DIR_2}}` | {{RESPONSIBILITY_2}} | {{FORBIDDEN_2}} |
| `{{DIR_3}}` | {{RESPONSIBILITY_3}} | {{FORBIDDEN_3}} |

### Integration points

| System | Purpose | Contract | Notes |
|---|---|---|---|
| {{SYSTEM_1}} | {{PURPOSE_1}} | {{CONTRACT_1}} | {{NOTES_4}} |

### Example

- Example: "Permissions are enforced in the service layer, not in controllers" is the kind of non-negotiable architectural rule that belongs here.

## Key rules

- Document what is true in production or the mainline branch today, not a proposed future state.
- Keep module boundaries and sensitive paths explicit.
- Update this file whenever system responsibilities, data flow, caching strategy, integrations, or permission boundaries change.
- Link major trade-offs to `advanced/decision-log.md` when that file is enabled.

## Known gaps / uncertainty

- Areas needing a deeper map: {{ARCHITECTURE_GAPS}}
- Open technical questions: {{OPEN_TECHNICAL_QUESTIONS}}

## Linked evidence

- ADR or decision record: {{ADR_LINK}}
- System diagram: {{SYSTEM_DIAGRAM_LINK}}
- Integration contract docs: {{INTEGRATION_DOC_LINK}}

## Next review trigger

- Review this file when a service boundary, integration, schema strategy, data flow, or non-negotiable engineering rule changes.
