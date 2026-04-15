# Code Review Guidelines

<!-- Claude reads all .md files in docs/code-review/ before reviewing PRs.
     Keep guidelines short and direct — Claude reads this every run.
     Split into multiple files if needed (e.g. security.md, api.md). -->

## Focus areas

- Auth gaps and PII handling
- Null paths and missing error handling
- Performance on critical user flows
- DB query efficiency

## Rules

- Flag bugs and risks. Skip stylistic nitpicks unless they affect clarity or safety.
- Do not suggest changes outside the PR's stated scope.

## Project-specific rules

<!-- Add project rules below. Keep each rule one line. Examples:
- All API endpoints must have auth middleware
- No `any` types in TypeScript
- DB migrations must be reversible
- New user-facing features require a feature flag
-->
