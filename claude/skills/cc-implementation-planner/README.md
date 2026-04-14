# cc-implementation-planner Skill

A Claude Code skill that ensures the `implementation-planner` agent is always invoked for technical planning, and surfaces live task progress in the terminal as the agent works.

## What It Does

- Creates a task checklist before the agent runs so the user can see every step
- Guarantees the `implementation-planner` agent is triggered — never attempts the work inline
- Updates task status (in_progress → completed) as each step finishes

## Steps Tracked

1. Determine GitHub issue ID (ask user if not provided)
2. Explore codebase to understand context, patterns, and architecture
3. Create phased implementation plan with 4-hour task breakdowns
4. Post plan as a comment on the GitHub issue

## Setup

### 1. Copy the skill directory

```bash
cp -r cc-implementation-planner/ <your-project>/.claude/skills/cc-implementation-planner/
```

### 2. Ensure the `implementation-planner` agent is installed

This skill is a wrapper — it requires the `implementation-planner` agent to be set up in `.claude/agents/implementation-planner.md`. See [`../../../claude/agents/implementation-planner/`](../../agents/implementation-planner/README.md) for agent setup instructions.

## Usage

Once installed, the skill auto-triggers when you ask Claude Code to plan a feature:

```
> Plan the implementation for adding a notification system
> Create a technical breakdown for issue #42
> Break down this feature into tasks: [paste requirements]
> How should I implement this? [paste requirements]
```
