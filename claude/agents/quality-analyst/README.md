# Quality Analyst Agent

A Claude Code agent that generates structured, requirement-driven test plans from GitHub issues, PRs, or plain-text requirements — covering manual, functional, performance, security, accessibility, usability, and reliability testing.

## What It Does

- Parses requirements from a GitHub issue, PR, branch, or plain text
- Extracts actors, user stories, acceptance criteria, business rules, and non-functional expectations
- Scans code diffs and static signals to surface performance and security risks
- Generates human-executable test cases with unambiguous pass/fail criteria
- Supports selective generation via `--type` flag (e.g. `--type manual`, `--type security,performance`)
- Posts the test plan as a GitHub comment or saves it locally
- Builds persistent memory of project-specific risk signals and coverage patterns

## Setup

### 1. Copy the agent file

```bash
cp quality-analyst.md <your-project>/.claude/agents/quality-analyst.md
```

### 2. Register in your project's CLAUDE.md

Add the following to your project's `CLAUDE.md`:

```markdown
## Custom Agents

Custom agents are defined in `.claude/agents/`. Use them via the Task tool with the matching `subagent_type`.

| Agent | When to Use |
|-------|-------------|
| `quality-analyst-agent` | When the user needs a structured test plan from a GitHub issue, PR, or plain-text requirement. Supports --type flag for selective section generation. |
```

> No placeholders to replace — this agent works out of the box.

## Supported --type values

| --type value | Section generated |
|---|---|
| `manual` | Section A — Manual test cases |
| `functional` | Section B — Functional test cases |
| `performance` | Section C — Performance test cases |
| `security` | Section D — Security test cases |
| `accessibility` | Section E — Accessibility test cases |
| `usability` | Section F — Usability test cases |
| `reliability` | Section G — Reliability / non-functional test cases |
| `all` | All sections A–G (default) |

Multiple values accepted as comma-separated list: `--type manual,functional`

## Usage

Once set up, the agent is triggered automatically when you ask Claude Code to generate a test plan:

```
> Generate a test plan for issue #42
> I only need security and performance tests for PR #18
> Write manual test cases for this requirement: Users can reset their password via email link
> We finished the implementation. Can you create a QA checklist?
```

The agent will:
1. Parse the source and `--type` flag
2. Fetch the GitHub issue or PR (or use plain text directly)
3. Extract requirements, actors, and acceptance criteria
4. Scan code diff and static signals for risk (skipped for manual/accessibility/usability-only runs)
5. Generate only the requested test sections with prioritised, verifiable test cases
6. Post the plan as a GitHub comment or save to `docs/test-plans/`
