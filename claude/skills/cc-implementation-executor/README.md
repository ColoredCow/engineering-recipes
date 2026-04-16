# cc-implementation-executor Skill

A Claude Code skill that ensures the `implementation-executor` agent is always invoked for plan execution, and surfaces live task progress in the terminal as the agent works.

## What It Does

- Creates a task checklist before the agent runs so the user can see every step
- Guarantees the `implementation-executor` agent is triggered — never attempts the work inline
- Updates task status (in_progress → completed) as each step finishes

## Steps Tracked

1. Fetch and parse the implementation plan from the GitHub issue
2. Set up feature branch
3. Implement each task sequentially with commits
4. Push branch to remote
5. Create pull request
6. Assign PR and verify CI checks

## Setup

### 1. Copy the skill directory

```bash
cp -r cc-implementation-executor/ <your-project>/.claude/skills/cc-implementation-executor/
```

### 2. Ensure the `implementation-executor` agent is installed

This skill is a wrapper — it requires the `implementation-executor` agent to be set up in `.claude/agents/implementation-executor.md`. See [`../../../claude/agents/implementation-executor/`](../../agents/implementation-executor/README.md) for agent setup instructions.

## Usage

Once installed, the skill auto-triggers when you ask Claude Code to execute a plan:

```
> Execute the implementation plan on issue #584
> Implement the plan we just created
> Start coding the plan from this comment: <github-comment-url>
> We've planned the feature, now let's build it
```
