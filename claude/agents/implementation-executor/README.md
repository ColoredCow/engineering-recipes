# Implementation Executor Agent

A Claude Code agent that takes structured implementation plans and turns them into production-ready code — one task at a time, with clean commits and a well-formed pull request at the end.

## What It Does

- Reads an implementation plan from a GitHub issue comment (produced by the `implementation-planner` agent or a human)
- Implements each task/phase sequentially, following existing codebase patterns
- Runs linting and tests after each task
- Creates one commit per task for clean, reviewable history
- Pushes the branch and opens a PR with a structured description
- Assigns the PR and verifies CI checks
- Handles multi-repository projects (e.g., separate backend + frontend repos)
- Builds persistent memory of your project's conventions over time

## Setup

### 1. Copy the agent file

```bash
cp implementation-executor.md <your-project>/.claude/agents/implementation-executor.md
```

### 2. Replace the placeholders

Open the copied file and replace each `{{PLACEHOLDER}}` with your project-specific values. See the reference table below.

### 3. Register in your project's CLAUDE.md

Add the following to your project's `CLAUDE.md`:

```markdown
## Custom Agents

Custom agents are defined in `.claude/agents/`. Use them via the Task tool with the matching `subagent_type`.

| Agent | When to Use |
|-------|-------------|
| `implementation-executor` | When the user wants to execute an existing implementation plan — reads the plan from a GitHub issue, implements each task sequentially, commits after each task, pushes, and opens a PR. |
```

## Placeholder Reference

| Placeholder | Description | Example (Django project) | Example (Next.js project) |
|---|---|---|---|
| `{{PROJECT_NAME}}` | Name of the project/platform | `IAGES` | `Acme Dashboard` |
| `{{FRONTEND_REPO_RELATIVE_PATH}}` | Relative path from this repo to the sibling frontend repo. Remove the entire Multi-Repository Context section if not applicable. | `../iages-frontend` | `../acme-web` |
| `{{DEFAULT_BRANCH}}` | The default/base branch for PRs | `develop` | `main` |
| `{{BRANCH_NAMING_CONVENTION}}` | Instructions for how to name new branches (see example below) | *(see below)* | *(see below)* |
| `{{CODE_STYLE_CHECKLIST}}` | Bullet list of code style rules and patterns to follow (see example below) | *(see below)* | *(see below)* |
| `{{LINT_COMMAND}}` | Command to run linting on changed files | `` `pre-commit run --files <file1> <file2> ...` `` | `` `npx eslint <file1> <file2> ...` `` |
| `{{TEST_RUN_COMMAND}}` | Command to run tests | `` `pytest <test-file-path>` `` | `` `npm test -- --testPathPattern=<module>` `` |
| `{{COMMIT_MESSAGE_GUIDELINES}}` | Additional commit message rules specific to your project (see example below) | *(see below)* | *(see below)* |
| `{{PR_TITLE_FORMAT}}` | Format string for PR titles | `feat: <description> (#<issue-number>)` | `feat: <description>` |
| `{{PR_ISSUE_REFERENCE_FORMAT}}` | How to reference the issue at the top of the PR body | `Targets <full-issue-url>` | `Closes #<issue-number>` |
| `{{PR_GUIDELINES}}` | Additional PR rules specific to your project (see example below) | *(see below)* | *(see below)* |
| `{{PROJECT_SPECIFIC_GUIDELINES}}` | Key patterns, conventions, and constraints specific to your project (see example below) | *(see below)* | *(see below)* |

## Example Values

### `{{BRANCH_NAMING_CONVENTION}}` — Django project

```markdown
   - Features: `feat/{issue-number}/{short-description}`
   - Fixes: `fix/{issue-number}/{short-description}`
   - Derive the name from the issue number and plan title.
```

### `{{BRANCH_NAMING_CONVENTION}}` — Next.js project

```markdown
   - Features: `feature/<issue-number>-<short-description>`
   - Fixes: `fix/<issue-number>-<short-description>`
   - Derive the name from the issue number and plan title.
```

### `{{CODE_STYLE_CHECKLIST}}` — Django project

```markdown
   - The project's code style (Black, isort, flake8 compliance)
   - Existing architectural patterns (service layer, response helpers, permission classes)
   - The specific instructions in the task description
```

### `{{CODE_STYLE_CHECKLIST}}` — Next.js project

```markdown
   - The project's code style (ESLint, Prettier compliance)
   - Existing architectural patterns (component structure, hooks, API layer)
   - The specific instructions in the task description
```

### `{{COMMIT_MESSAGE_GUIDELINES}}` — Django project

```markdown
   - Do NOT include the issue number (e.g., `(#123)`) in commit messages — it clutters the issue page with cross-references.
```

### `{{COMMIT_MESSAGE_GUIDELINES}}` — Next.js project

```markdown
   - Include the issue number in the commit body (not the subject line) when relevant.
```

### `{{PR_GUIDELINES}}` — Django project

```markdown
**Important PR rules:**
- PR title: `feat: description (#issue-number)` — under 72 chars
- NEVER use "Closes/Fixes/Resolves" — reference the issue with `Targets <full-issue-url>` at the very top of the PR body (before `## Summary`)
- Always use the **full GitHub URL** for issue references (e.g., `https://github.com/org/repo/issues/123`), not shorthand like `#123`. This ensures cross-repo PRs link correctly.
- PR body must have `## Summary`, `## Changes`, `## Test plan`
```

### `{{PR_GUIDELINES}}` — Next.js project

```markdown
**Important PR rules:**
- PR title should be under 72 chars
- Use `Closes #<issue-number>` to auto-close the linked issue
- PR body must have `## Summary`, `## Changes`, `## Test plan`
```

### `{{PROJECT_SPECIFIC_GUIDELINES}}` — Django project

```markdown
- **Follow all Git Rules from CLAUDE.md** — never commit to `develop` or `main` directly, stage specific files, conventional commits, etc.
- **Follow existing patterns:** This project uses a service layer pattern, custom response helpers, and role-based permissions.
- **Never skip pre-commit hooks** — fix lint/format issues. Only use `--no-verify` for pre-existing mypy errors in files you did NOT modify.
```

### `{{PROJECT_SPECIFIC_GUIDELINES}}` — Next.js project

```markdown
- **Follow all Git Rules from CLAUDE.md** — never commit to `main` directly, stage specific files, conventional commits, etc.
- **Follow existing patterns:** This project uses [your patterns]. Match the existing code style and architecture.
- **Never skip linting or formatting checks** — fix issues before committing.
```

## Usage

Once set up, the agent is triggered automatically when you ask Claude Code to execute a plan:

```
> Execute the implementation plan on issue #584
> Implement the plan we just created for the membership sync fix
> Start coding the plan from this comment: <github-comment-url>
> We've planned the feature, now let's build it
```

The agent will:
1. Fetch and parse the implementation plan from the GitHub issue
2. Ask about branch setup (new or existing)
3. Implement each task sequentially, committing after each one
4. Run linting and tests along the way
5. Push the branch and open a PR
6. Assign the PR and verify CI checks
