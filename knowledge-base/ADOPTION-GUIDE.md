# Hybrid KB Adoption Guide

Use this guide when rolling the hybrid KB into a downstream project. It assumes the v1 contract in [SPEC.md](SPEC.md) and the pilot boundaries in [KB-CONTRACT-V1-PILOT-SCOPE.md](KB-CONTRACT-V1-PILOT-SCOPE.md).

## Operating Model

- `engineering-recipes` owns the contract, templates, scaffold tooling, validator, and agent definitions.
- Each project owns its local `knowledge-base/` directory and the truth inside it.
- Tier 1 is the small, required baseline.
- Tier 2 is optional and should be enabled only when the project needs it.
- Consumer agents read KB first and remain read-only.
- `knowledge-base-manager` is the only automated KB writer.

## Source Repo Deliverables

This repo now provides:
- the versioned KB contract
- metadata-enabled KB templates
- a validator that checks contract structure, metadata, loading references, and KB hygiene for canonical numbered-flat installs
- a scaffold script that can install the KB, KB manager, and optional workflow assets
- a reusable downstream workflow file for KB delivery rules

Compatibility note:
- numbered-tree and legacy-flat installs still validate for required files, entry references, config, and enabled Tier 2 modules
- deep checks such as front matter, shared Tier 1 headings, size budgets, and duplicate-claim hygiene apply only to the canonical numbered-flat layout

## Project Install Checklist

1. Scaffold the KB into the target project.
2. Complete `knowledge-base/.kb-config.yml`.
3. Assign named owners for business flows, architecture, risk model, active sprint, and overall KB process.
4. Add the KB guidance section to the project root `CLAUDE.md`.
5. Install `knowledge-base-manager` if the project uses Claude agents.
6. Run `python3 knowledge-base/scripts/validate_hybrid_kb.py .` from the project root.

## Canonical Baseline

Populate Tier 1 in this order:
1. `00-master.md`: project summary, objectives, stage, file map, role-based reading paths, and known KB gaps
2. `01-business-flows.md`: core workflows, business rules, edge cases, and glossary terms
3. `02-architecture.md`: major modules, integration boundaries, data flow, and non-negotiable rules
4. `03-risk-model.md`: critical flows, fragile modules, release risks, and review/test expectations
5. `04-active-sprint.md`: current sprint state seeded from the issue tracker

Enable Tier 2 only when it is justified:
- `decision-log.md`
- `incident-log.md`
- `feature-history.md`
- `integration-map.md`
- `metrics.md`
- `known-constraints.md`

## Update Trigger Matrix

| Trigger | Update target |
|---|---|
| business behavior changes | `01-business-flows.md` |
| architecture or boundary changes | `02-architecture.md` |
| regression or release risk discovery | `03-risk-model.md` |
| issue state movement | `04-active-sprint.md` |
| significant trade-off or decision | `advanced/decision-log.md` |
| incident or root cause learning | `advanced/incident-log.md` |
| feature evolution worth preserving | `advanced/feature-history.md` |
| external integration detail change | `advanced/integration-map.md` |
| measurable operational learning | `advanced/metrics.md` |
| recurring limitation or debt | `advanced/known-constraints.md` |

## Delivery Workflow Rules

- Every task must make an explicit KB impact decision before it is considered done.
- KB impact belongs in the documented delivery workflow, not in memory.
- Reviewers should check code and KB consistency together when KB impact is marked.
- The KB manager should keep `04-active-sprint.md` current, but other Tier 1 files should still be reviewed by human owners.

## Ownership Model

Recommended default owners:
- business flows: PM or BA
- architecture: tech lead
- risk model: QA lead with tech lead support
- active sprint: engineering lead or KB manager workflow owner
- Tier 2 logs: domain-specific owners
- overall KB process: project lead or engineering manager

Front matter `owners` fields should reference keys from `.kb-config.yml` so validation can confirm the links.

## AI Usage Contract

- Read `knowledge-base/00-master.md` first.
- If `.kb-config.yml` exists, use it as the runtime source of truth.
- Load only the files needed for the task.
- If KB content is missing or obviously incomplete, do not fabricate facts.
- Consumer agents remain read-only.
- Only `knowledge-base-manager` may automate KB writes.
- Keep Tier 1 concise enough for routine reads.

## Maintenance Cadence

- Daily: sync sprint state and check open KB-impact work
- Weekly: review KB gaps during sprint review or planning
- Monthly: review Tier 1 freshness and ownership validity
- Quarterly: review contract adoption, Tier 2 usage, and token cost

## 30-Day Rollout Backlog

### Week 1
- freeze pilot scope
- finalize starter kit
- add metadata front matter and section schema
- strengthen the validator
- package KB manager installation

### Week 2
- install KB in pilot project 1
- complete `.kb-config.yml`
- assign owners
- update root `CLAUDE.md`
- populate the Tier 1 baseline

### Week 3
- add KB issue labels
- publish/update the project KB process doc
- run the first real update flows and remove friction

### Week 4
- install KB in pilot project 2
- compare pilot learnings
- finalize org SOP
- prepare demo/training material

## Related Assets

- [project-files/KB-PROCESS.md](project-files/KB-PROCESS.md)
- [prompts/install-hybrid-kb.md](prompts/install-hybrid-kb.md)
