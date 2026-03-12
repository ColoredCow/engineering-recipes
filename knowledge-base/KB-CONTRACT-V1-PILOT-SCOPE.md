# KB Contract V1 Pilot Scope

## Frozen In The Pilot

These items are locked for the v1 pilot:
- required Tier 1 files remain `00-master.md`, `01-business-flows.md`, `02-architecture.md`, `03-risk-model.md`, `04-active-sprint.md`
- the entry-point rule remains `knowledge-base/00-master.md`
- `.kb-config.yml` minimum required keys remain `version`, `project.name`, `enabled_tier2`, and `loading_defaults`
- the canonical new-install layout remains numbered-flat

## Adjustable During The Pilot

These changes are safe within v1:
- better templates and examples
- stronger validators and scaffold helpers
- clearer ownership and freshness guidance
- downstream install docs and workflow assets
- optional Tier 2 additions that stay backward-compatible

## Explicitly Out Of Scope During The Pilot

Do not make these changes during the pilot without a new major contract version:
- renaming required Tier 1 files
- changing the required Tier 1 set
- changing the entry-point rule
- changing the required `.kb-config.yml` keys

## Approval Model

- Contract owner: maintainers of `engineering-recipes`
- Required approvers for contract-level changes: repository maintainers
- Breaking changes require: maintainer review, migration guidance, and a new major contract version

## Pilot Goal

Make the KB repeatable in real project repos without redesigning the contract:
- every project starts from the same foundation
- ownership and review are explicit
- KB impact is checked as part of normal delivery
- AI agents read KB first and stay read-only unless they are the KB manager
