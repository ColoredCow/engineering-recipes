# Hybrid KB Governance

## Ownership

- Contract owner: maintainers of `engineering-recipes`
- Project KB owner: the downstream project team
- Default automation owner: `knowledge-base-manager` flow or equivalent project-maintained automation
- Pilot scope reference: [KB-CONTRACT-V1-PILOT-SCOPE.md](KB-CONTRACT-V1-PILOT-SCOPE.md)

## Change Classes

### Non-breaking changes
Examples:
- clarifying wording
- adding examples
- improving scripts without changing file contract
- adding optional Tier 2 modules in a backward-compatible way

These can be released within the current major version.

### Breaking changes
Examples:
- renaming required files
- changing `.kb-config.yml` required keys
- changing the required Tier 1 set
- changing the entry-point rule

These require a new major KB contract version and an explicit migration note.

## Versioning Rules

- Current contract: `v1`
- Contract version is documented in `knowledge-base/SPEC.md`
- Downstream projects should pin to the contract they installed until they intentionally migrate

## Approval Rules

The following changes require maintainer review in `engineering-recipes`:
- changes to Tier 1 required files
- changes to the read contract
- changes to `.kb-config.yml` schema
- changes to sprint sync behavior
- addition of new Tier 2 module types
- changes that make the validator reject previously valid v1 installs

## Upgrade Rules For Downstream Projects

1. Review the spec diff first.
2. Check whether the change is breaking or non-breaking.
3. Run the KB validator after applying changes.
4. Update the project root `CLAUDE.md` guidance if the adapter contract changed.
5. Run the KB validator after structural KB changes.

## Recommended Maintainer Checklist

- Is the change adding default token cost?
- Is the change backward-compatible with legacy projects where claimed?
- Does the change keep Tier 1 concise?
- Is ownership still clear after the change?
- Is migration guidance included if needed?
- Does the change preserve the v1 pilot freeze on required files, entrypoint, and minimum config keys?
