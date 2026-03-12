---
id: kb.master
title: Knowledge Base Master
owners:
  - kb_process
audiences:
  - engineering
  - product
  - qa
last_reviewed: "{{LAST_REVIEWED_DATE}}"
review_cycle_days: 30
confidence: high
change_frequency: high
source_refs: []
tags:
  - tier1
  - routing
---

# Knowledge Base: {{PROJECT_NAME}}

## Purpose

Single entry point for the project knowledge base. Agents always read this file first, then load only the KB files needed for the task.

## Scope

This file routes readers to the right KB sections, captures the current project snapshot, and records missing KB areas. It does not replace the detailed Tier 1 files.

## What is true today

### Project summary

{{PROJECT_ONE_PARAGRAPH_SUMMARY}}

### Current snapshot

- Objectives: {{PROJECT_OBJECTIVES}}
- System stage: {{SYSTEM_STAGE}}
- Primary surfaces: {{PRIMARY_SURFACES}}
- Runtime source of truth: `knowledge-base/.kb-config.yml`

### Role-based reading paths

| Role / task | Read first | Then read |
|---|---|---|
| Planning | `00-master.md` | `01-business-flows.md`, `02-architecture.md`, `04-active-sprint.md` |
| Code review | `00-master.md` | `02-architecture.md`, `03-risk-model.md` |
| Onboarding | `00-master.md` | all Tier 1 files |
| Incident response | `00-master.md` | `03-risk-model.md`, `advanced/incident-log.md` when enabled |

### KB file map

| File | When to read it | Owner key |
|---|---|---|
| `01-business-flows.md` | user journeys, rules, approvals, glossary | `business_flows` |
| `02-architecture.md` | architecture, boundaries, integrations, non-negotiables | `architecture` |
| `03-risk-model.md` | fragile areas, release risk, review expectations | `risk_model` |
| `04-active-sprint.md` | current delivery state and sprint sync | `active_sprint` |

### Example

- A planner working on a new feature should start here, then load business flows, architecture, and active sprint before reading code.

## Key rules

- Read this file before any other KB file.
- Follow `knowledge-base/.kb-config.yml` for enabled modules and loading defaults.
- Consumer agents are read-only; only `knowledge-base-manager` may automate KB writes.
- If a relevant KB section is missing or clearly incomplete, do not fabricate facts.
- Keep this file small and move detail into linked Tier 1 or Tier 2 files.

## Known gaps / uncertainty

- Missing sections: {{KNOWN_MISSING_SECTIONS}}
- Open questions: {{OPEN_QUESTIONS}}

## Linked evidence

- Product brief: {{PRODUCT_BRIEF_LINK}}
- Architecture overview: {{ARCHITECTURE_OVERVIEW_LINK}}
- Sprint board or issue query: {{SPRINT_BOARD_LINK}}

## Next review trigger

- Review this file when the KB map, ownership model, system stage, or reading paths change.
