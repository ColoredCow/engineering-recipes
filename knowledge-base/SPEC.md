# Hybrid KB Specification v1

## Status
- Version: `1`
- Date: `2026-03-07`
- State: `Current`

## Goal

Provide a project-local, token-efficient knowledge base that is easy to scaffold, easy to maintain, and reusable across projects of different stacks and domains.

This contract is frozen for the v1 pilot as described in [KB-CONTRACT-V1-PILOT-SCOPE.md](KB-CONTRACT-V1-PILOT-SCOPE.md).

## Design Principles

1. Project-local storage: each project owns its own `knowledge-base/` directory.
2. Small default footprint: Tier 1 is required and intentionally compact.
3. Optional advanced depth: Tier 2 is opt-in per project.
4. Deterministic reads: agents read the entry file first, then load only mapped files.
5. Reliable writes over deep structure: Tier 1 uses one file per section so KB updates remain predictable.
6. Tool agnostic content: KB content stays plain Markdown plus lightweight config.

## Canonical Project Layout

```text
knowledge-base/
├── 00-master.md
├── 01-business-flows.md
├── 02-architecture.md
├── 03-risk-model.md
├── 04-active-sprint.md
├── .kb-config.yml
├── advanced/
│   ├── decision-log.md
│   ├── incident-log.md
│   ├── feature-history.md
│   ├── integration-map.md
│   ├── metrics.md
│   └── known-constraints.md
└── scripts/
    └── validate_hybrid_kb.py
```

## Tier Model

### Tier 1: Required
- `00-master.md`
- `01-business-flows.md`
- `02-architecture.md`
- `03-risk-model.md`
- `04-active-sprint.md`

### Tier 2: Optional
- `advanced/decision-log.md`
- `advanced/incident-log.md`
- `advanced/feature-history.md`
- `advanced/integration-map.md`
- `advanced/metrics.md`
- `advanced/known-constraints.md`

## File Ownership

| File | Owner | Notes |
|---|---|---|
| `00-master.md` | Human | Keep concise; update when KB structure or project metadata changes |
| `01-business-flows.md` | Human or guided KB maintenance | Main business context file |
| `02-architecture.md` | Human or guided KB maintenance | Main architecture/context file |
| `03-risk-model.md` | Human or guided KB maintenance | Main risk and review guidance file |
| `04-active-sprint.md` | Human or project-specific process | Main volatile delivery-state file |
| Tier 2 append-only logs | Human or semi-automated | Prefer append-only entries |

## Read Contract

### Entry-point rule
Agents read `knowledge-base/00-master.md` first.

### Config rule
If `knowledge-base/.kb-config.yml` exists, it is the runtime source of truth for enabled modules and loading defaults.

### Default loading map

| Task | Files |
|---|---|
| Code review | `02-architecture.md`, `03-risk-model.md` |
| Planning | `01-business-flows.md`, `02-architecture.md`, `04-active-sprint.md` |
| Sprint work | `04-active-sprint.md` |
| Onboarding | All Tier 1 files |
| Incident response | `03-risk-model.md`, `advanced/incident-log.md` when enabled |

### No-assumptions rule
If a relevant file is missing or clearly incomplete, agents skip it and continue with available context. They do not fabricate missing context.

### Graceful degradation rule
If `knowledge-base/` or the entry file does not exist, agents proceed without KB-aware behavior.

## Write Contract

1. Only the designated KB maintenance flow may write automated updates.
2. This starter kit ships scaffold + validation only.
3. Tier 1 section files are the default write targets. Do not require automatic child-file creation for routine updates.
4. Tier 2 logs should prefer append-only updates.
5. Agents that consume KB context remain read-only.

## `.kb-config.yml` Contract

Minimum supported keys:
- `version`
- `project.name`
- `enabled_tier2`
- `loading_defaults`

Recommended extension keys:
- `source_of_truth`
- `project.summary`
- `project.domain`
- `project.repo_type`
- `owners`
- `review`
- `agent_policy`

## Metadata Contract For Markdown KB Files

Canonical numbered-flat KB files should include YAML front matter with these fields:
- `id`
- `title`
- `owners`
- `audiences`
- `last_reviewed`
- `review_cycle_days`
- `confidence`
- `change_frequency`
- `source_refs`
- `tags`

Front matter `owners` should reference keys or named values defined in `.kb-config.yml` when the project provides an `owners` block.

## Tier 1 Section Schema

Each canonical Tier 1 file should use the same top-level section pattern:
1. `Purpose`
2. `Scope`
3. `What is true today`
4. `Key rules`
5. `Known gaps / uncertainty`
6. `Linked evidence`
7. `Next review trigger`

The section content can be file-specific, but the top-level headings should remain consistent so agents and validators can reason about the files deterministically.

## Compatibility Rules

### Numbered-tree support
Agents and helpers may support these older numbered-tree files when the canonical numbered-flat layout is absent:
- `knowledge-base/00-master.md`
- `knowledge-base/01-business-flows/00-index.md`
- `knowledge-base/02-architecture/00-index.md`
- `knowledge-base/03-risk-model/00-index.md`
- `knowledge-base/04-active-sprint/00-index.md`

### Legacy flat support
Agents and helpers may also support these temporary flat-layout files when the canonical numbered-flat layout is absent:
- `knowledge-base/00-index.md`
- `knowledge-base/business-flows.md`
- `knowledge-base/architecture.md`
- `knowledge-base/risks.md`
- `knowledge-base/active-sprint.md`

New installs must use the numbered-flat layout.

## Maintenance Cadence

Recommended default:
- update Tier 1 when project reality changes
- keep Tier 1 concise enough for routine agent reads
- use append-only updates for Tier 2 logs where possible
- run the KB validator after setup or structural changes

## Operational Workflow Expectations

- every task should make an explicit KB impact decision
- review should check code and KB alignment together
- `04-active-sprint.md` is the default automation target
- business, architecture, risk, and sprint each need named owners in the downstream project
- missing KB context must not be fabricated by agents

## Rollout Order

1. Sneha pilot
2. IAGES backend pilot
3. Additional projects after contract validation

## Review Checklist

- Is the change Tier 1 or Tier 2?
- Does it increase default token cost?
- Is the relevant Tier 1 file still concise and scannable?
- Is the change write-friendly for the KB manager?
- Is ownership clear?
- Does the change preserve tool-agnostic plain-text content?
