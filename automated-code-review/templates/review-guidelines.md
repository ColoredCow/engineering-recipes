# Code Review Guidelines

> **Note:** Claude reads all `.md` files in `docs/code-review/` before reviewing PRs. You can split guidelines into multiple files (e.g., `security.md`, `style.md`, `api.md`).

These guidelines are used by Claude to align feedback with project expectations.

## Focus areas

- Readability and maintainability
- Avoiding unnecessary complexity
- Performance impact on critical user flows
- Database query efficiency
- Security implications (auth, payments, PII)

## Review tone

- Be constructive
- Prefer suggestions over rewrites
- Call out risks clearly
- Avoid stylistic nitpicking unless it affects clarity or safety

## Project-specific rules (customize these)

<!-- Add your project-specific rules below. Examples: -->
<!-- - All API endpoints must have authentication middleware -->
<!-- - Use TypeScript strict mode - no `any` types -->
<!-- - Database migrations must be reversible -->
<!-- - Feature flags required for new user-facing features -->
