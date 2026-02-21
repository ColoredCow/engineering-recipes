# Business Analyst Agent

A Claude Code agent that refines raw feature requests into clear, business-aligned requirements — without drifting into architecture, implementation planning, or code-level design.

## What It Does

- Restates rough requests in clear business language
- Identifies ambiguity, missing decisions, and conflicts
- Produces structured requirement documents for product, engineering, QA, and stakeholders
- Keeps scope controlled (no unrequested features)
- Produces verifiable acceptance criteria
- Builds persistent memory of domain terms and requirement-writing conventions

## Setup

### 1. Copy the agent file

```bash
cp business-analyst.md <your-project>/.claude/agents/business-analyst.md
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
| `business-analyst` | When the user shares rough requirements and needs them refined into clear, business-readable, testable requirement docs without technical implementation details. |
```

## Placeholder Reference

| Placeholder | Description | Example |
|---|---|---|
| `{{PROJECT_NAME}}` | Product/platform name used for context in requirement writing | `Sneha LMS` |
| `{{DOMAIN_CONTEXT}}` | One short paragraph describing business domain and product context | `A learning management platform for schools with role-based workflows.` |
| `{{BUSINESS_TERMS_GUIDANCE}}` | Key terminology rules (preferred terms, banned ambiguous terms, naming consistency) | `Use "Learner" not "User" in requirement documents.` |
| `{{REQUIREMENT_CONSTRAINTS}}` | Business/legal/operational constraints that should be considered while refining requirements | `Data retention policies, compliance needs, approval flows.` |

## Usage

Once set up, the agent is triggered automatically when you ask Claude Code to refine requirements:

```
> Refine these raw requirements into a stakeholder-ready requirement doc
> Clean up this feature request and make acceptance criteria testable
> Convert these notes into a clear requirement with in-scope/out-of-scope
> I need a business analyst pass on this request before engineering planning
```

The agent will:
1. Restate intent and identify requirement gaps
2. Refine into a strict, business-readable structure
3. Produce scope, requirements, constraints, and acceptance criteria
4. Flag truly blocking open questions
