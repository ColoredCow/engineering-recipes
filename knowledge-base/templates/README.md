# Templates

These templates are copied into downstream projects.

## Core templates
- `00-master.md`
- `01-business-flows.md`
- `02-architecture.md`
- `03-risk-model.md`
- `04-active-sprint.md`
- `.kb-config.yml`
- `CLAUDE.section.md`

## Optional advanced templates
- `advanced/decision-log.md`
- `advanced/incident-log.md`
- `advanced/feature-history.md`
- `advanced/integration-map.md`
- `advanced/metrics.md`
- `advanced/known-constraints.md`

## Authoring rules
- Keep Tier 1 section files concise but directly useful.
- Do not force child-file creation for routine KB updates.
- Treat Tier 2 as opt-in and mostly append-only.
- Keep KB content plain Markdown plus lightweight config.
- Canonical KB content templates should include front matter metadata.
- Canonical Tier 1 templates should keep the shared top-level section schema:
  - `Purpose`
  - `Scope`
  - `What is true today`
  - `Key rules`
  - `Known gaps / uncertainty`
  - `Linked evidence`
  - `Next review trigger`
- `CLAUDE.section.md` is a helper snippet, not a KB content file, so it does not use front matter.
