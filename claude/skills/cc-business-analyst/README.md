# cc-business-analyst Skill

A Claude Code skill that ensures the `business-analyst` agent is always invoked for requirement refinement, and surfaces live task progress in the terminal as the agent works.

## What It Does

- Creates a task checklist before the agent runs so the user can see every step
- Guarantees the `business-analyst` agent is triggered — never attempts the work inline
- Updates task status (in_progress → completed) as each step finishes

## Steps Tracked

1. Read raw request and restate intent in plain language
2. Identify ambiguities, missing decisions, and conflicting statements
3. Refine into structured requirement document
4. Validate acceptance criteria are specific and verifiable
5. Flag truly blocking open questions

## Setup

### 1. Copy the skill directory

```bash
cp -r cc-business-analyst/ <your-project>/.claude/skills/cc-business-analyst/
```

### 2. Ensure the `business-analyst` agent is installed

This skill is a wrapper — it requires the `business-analyst` agent to be set up in `.claude/agents/business-analyst.md`. See [`../../../claude/agents/business-analyst/`](../../agents/business-analyst/README.md) for agent setup instructions.

## Usage

Once installed, the skill auto-triggers when you ask Claude Code to work on requirements:

```
> Refine these rough notes into a proper requirement doc
> Clean up this feature request and make the acceptance criteria testable
> I need a BA pass on this before we plan the implementation
> Convert this client call transcript into structured requirements
```
