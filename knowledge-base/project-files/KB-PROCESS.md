# Knowledge Base Process

Use this file in downstream projects as the working agreement for KB maintenance.

## Definition Of Done

- Every task requires a KB impact decision.
- If KB impact exists, the relevant KB file must be updated before merge.
- `knowledge-base-manager` keeps sprint state current, but human owners still approve truth for business, architecture, and risk files.

## Update Trigger Matrix

| Trigger | File |
|---|---|
| business behavior change | `knowledge-base/01-business-flows.md` |
| architecture or module boundary change | `knowledge-base/02-architecture.md` |
| risk or regression discovery | `knowledge-base/03-risk-model.md` |
| issue state change | `knowledge-base/04-active-sprint.md` |
| decision or trade-off | `knowledge-base/advanced/decision-log.md` |
| incident or root cause | `knowledge-base/advanced/incident-log.md` |
| feature evolution | `knowledge-base/advanced/feature-history.md` |
| external integration detail | `knowledge-base/advanced/integration-map.md` |
| measurable operational learning | `knowledge-base/advanced/metrics.md` |
| recurring limitation or debt | `knowledge-base/advanced/known-constraints.md` |

## Recommended Issue Labels

- `kb:update-required`
- `kb:business`
- `kb:architecture`
- `kb:risk`
- `kb:decision`
- `kb:incident`
- `kb:sprint`

## Ownership Template

| Area | Named owner |
|---|---|
| business flows | {{BUSINESS_OWNER}} |
| architecture | {{ARCHITECTURE_OWNER}} |
| risk model | {{RISK_OWNER}} |
| active sprint | {{SPRINT_OWNER}} |
| KB process | {{KB_PROCESS_OWNER}} |

## Review Paths

- architecture change: engineer drafts, tech lead reviews, validator runs, merge
- business flow change: PM or BA drafts, QA or tech cross-checks, validator runs, merge
- incident learning: responder drafts, QA or tech lead reviews, merge

## Maintenance Cadence

- daily: sprint sync and KB-impact triage
- weekly: review KB gaps in sprint review or planning
- monthly: review Tier 1 freshness and owners
- quarterly: review contract adoption and Tier 2 usage
