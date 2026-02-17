# Claude Agents

This directory contains reusable, templatized Claude Code agents that can be set up in any project.

## Available Agents

| Agent | Description |
|-------|-------------|
| [implementation-planner](agents/implementation-planner/) | Translates feature requests into phased implementation plans using the 4-hour task theory and posts them as GitHub issue comments. |
| [implementation-executor](agents/implementation-executor/) | Takes an existing implementation plan from a GitHub issue and executes it — implementing each task sequentially, committing after each, pushing, and opening a PR. |

## Setting Up Agents in Your Project

> **Important:** Run the prompt below from your project's root directory so that Claude can access and review your project structure, tech stack, and conventions to automatically fill in placeholders.

### Steps

1. Open Claude Code in your project directory.
2. Copy and paste the prompt below.
3. Claude will review your codebase, set up the agent files, and ask you about anything it can't infer on its own.

### Prompt

```
I want to set up Claude Code agents from the engineering-recipes repo into this project.

Source repo: https://github.com/ColoredCow/engineering-recipes (browse the `claude/agents/` directory for all available agents and their README).

For each agent found there:

1. Read the agent's template file and its README (which contains the placeholder reference and example values).
2. Copy the agent template to `.claude/agents/<agent-name>.md` in this project.
3. Replace all `{{PLACEHOLDER}}` values with project-specific values by:
   a. First, explore this project's codebase — look at the directory structure, config files, package.json/requirements.txt, existing patterns, test setup, and conventions to infer as many placeholder values as possible.
   b. For any placeholder you cannot confidently determine from the codebase, ask me before proceeding. Present what you've inferred so far and ask only about the ones you're unsure of.
4. If the agent template has optional sections that don't apply to this project (e.g., Multi-Repository Context for a single-repo project), remove them.
5. Register all set-up agents in this project's CLAUDE.md under a "Custom Agents" section. Create CLAUDE.md if it doesn't exist.

After setup, show me a summary of what was configured and any values you'd recommend I review or adjust.
```
