---
name: cc-implementation-planner
description: Use when the user wants an implementation plan, technical breakdown, or task planning for a feature — including "plan this feature", "create a technical breakdown", "break this into tasks", "how should I implement this", or when requirements need to be translated into actionable, 4-hour development tasks to be posted on a GitHub issue.
---

# cc-implementation-planner

Invokes the `implementation-planner` agent to produce a phased, 4-hour task breakdown plan and post it to a GitHub issue. Never attempt planning inline — the agent must always be invoked, no exceptions.

## Before Invoking the Agent

Call `TaskCreate` for each of the following steps:

1. Determine GitHub issue ID (ask user if not provided)
2. Explore codebase to understand context, patterns, and architecture
3. Create phased implementation plan with 4-hour task breakdowns
4. Post plan as a comment on the GitHub issue

Then call `TaskUpdate` to mark task 1 `in_progress`.

## Invoke the Agent

```
Agent(
  subagent_type="implementation-planner",
  prompt="<full user message with all context>"
)
```

**The agent must always be invoked. Never do the work inline.**

## After the Agent Completes

Call `TaskUpdate` on each task in sequence — mark `in_progress` then `completed` — based on what the agent reported completing.
