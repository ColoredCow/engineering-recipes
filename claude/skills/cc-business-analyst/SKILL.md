---
name: cc-business-analyst
description: Use when the user wants to refine rough, ambiguous, or unstructured feature requests into clear, business-aligned requirement documents — including requests like "refine this requirement", "clean up this feature request", "make this testable", "convert these notes to requirements", "I need a BA pass on this", or whenever stakeholders need a structured, verifiable requirement doc before technical planning.
---

# cc-business-analyst

Invokes the `business-analyst` agent to refine raw requirements into a structured, stakeholder-ready document. Never attempt requirement refinement inline — the agent must always be invoked, no exceptions.

## Before Invoking the Agent

Call `TaskCreate` for each of the following steps:

1. Read raw request and restate intent in plain language
2. Identify ambiguities, missing decisions, and conflicting statements
3. Refine into structured requirement document (purpose, scope, functional requirements, business rules, acceptance criteria)
4. Validate acceptance criteria are specific and verifiable
5. Flag truly blocking open questions

Then call `TaskUpdate` to mark task 1 `in_progress`.

## Invoke the Agent

```
Agent(
  subagent_type="business-analyst",
  prompt="<full user message with all context>"
)
```

**The agent must always be invoked. Never do the work inline.**

## After the Agent Completes

Call `TaskUpdate` on each task in sequence — mark `in_progress` then `completed` — based on what the agent reported completing.
