# Hybrid KB Spec Reconciliation

## Purpose

This note reconciles three KB layouts that now exist in project history:
- the original numbered-tree layout
- the temporary unnumbered flat layout
- the current numbered-flat layout

## Current vs Target

| Area | Older states | Hybrid V1 target | Decision |
|---|---|---|---|
| Core layout | Numbered-tree and temporary flat layouts both existed | Numbered flat files under `knowledge-base/` | New installs use numbered-flat layout |
| Entry file | `knowledge-base/00-master.md` and temporary `00-index.md` | `knowledge-base/00-master.md` | Standardize on `00-master.md` |
| Section files | `01-business-flows/00-index.md` or `business-flows.md` style files | `01-business-flows.md`, `02-architecture.md`, `03-risk-model.md`, `04-active-sprint.md` | One file per Tier 1 section |
| Runtime contract | `CLAUDE.md` guidance plus `.kb-config.yml` | `.kb-config.yml` plus mirrored `CLAUDE.md` guidance | `.kb-config.yml` remains source of truth |
| Sprint file | `04-active-sprint/00-index.md` or `active-sprint.md` | `04-active-sprint.md` | Standardize on numbered-flat sprint file |
| Advanced memory | Optional modules under `advanced/` | Optional modules under `advanced/` | Keep as explicit optional templates |
| Automation | Manual validation only | Manual validation only | Do not ship sync automation in the starter kit |

## Frozen Outcomes

### Layout
- **Canonical:** numbered-flat layout.
- **Reason:** preserves scoped reads while keeping writes simple and reliable.

### Entry file
- **Canonical:** `knowledge-base/00-master.md`.
- **Compatibility:** agents may still fall back to `knowledge-base/00-index.md` for older projects.

### Tier 1 write model
- **Decision:** one main file per Tier 1 section.
- **Reason:** the KB manager updates single-file sections more reliably than index-plus-child-file structures.

### Compatibility support
- **Numbered-tree:** supported as read/write fallback for older projects.
- **Legacy flat:** supported as read/write fallback for projects created during the temporary flat phase.

## Migration Impact

### For new projects
- Use the numbered-flat hybrid contract.
- Generate `.kb-config.yml` and append KB rules to the project root `CLAUDE.md`.

### For projects on the numbered-tree layout
- No forced rewrite in V1.
- Updated agents and validator still support the tree structure.
- Migration can happen later by merging section content into numbered-flat files.

### For projects on the legacy flat layout
- No forced rewrite in V1.
- Updated agents and validator still support the layout.
- Migration can happen later by renaming files into the numbered-flat scheme.

## Agent Behavior Differences

| Agent | Older compatibility behavior | Hybrid V1 behavior |
|---|---|---|
| `implementation-planner` | Falls back to tree or legacy-flat section files when needed | Reads `00-master.md`, then loads numbered-flat section files |
| `implementation-executor` | Falls back to tree or legacy-flat architecture files | Reads `02-architecture.md` |
| `business-analyst` | Falls back to tree or legacy-flat business files | Reads `01-business-flows.md` |
| `knowledge-base-manager` | Supports older tree/flat write targets as fallback | Prefers `04-active-sprint.md` and single-file Tier 1 updates |

## Scope of This Implementation

Implemented in this repo:
- V1 hybrid spec using numbered-flat layout
- Tier 1 and Tier 2 templates
- `.kb-config.yml` contract
- scaffold prompt and reusable scripts
- agent documentation updates
- KB validation helper

Not implemented in this repo:
- direct migration of Sneha or IAGES repositories
- automatic sprint sync or scheduling
