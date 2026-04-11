---
name: cc-implementation-executor
description: Use when the user wants to execute an existing implementation plan — including "execute the plan on issue #X", "implement the plan", "start coding the plan", "we've planned it, now build it", or when an implementation plan already exists on a GitHub issue and needs to be turned into committed code with a pull request.
---

# cc-implementation-executor

Invokes the `implementation-executor` agent to execute an existing plan and open a pull request. Never implement code inline — the agent must always be invoked, no exceptions.

## Before Invoking the Agent

Call `TaskCreate` for each of the following steps:

1. Fetch and parse the implementation plan from the GitHub issue
2. Set up feature branch
3. Implement each task sequentially with commits
4. Push branch to remote
5. Create pull request
6. Assign PR and verify CI checks

Then call `TaskUpdate` to mark task 1 `in_progress`.

## Invoke the Agent

```
Agent(
  subagent_type="implementation-executor",
  prompt="<full user message with all context>"
)
```

**The agent must always be invoked. Never do the work inline.**

## After the Agent Completes

Call `TaskUpdate` on each task in sequence — mark `in_progress` then `completed` — based on what the agent reported completing.
