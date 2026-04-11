# Claude Agents & Skills

This directory contains reusable, templatized Claude Code agents and skills that can be set up in any project.

## Available Agents

| Agent | Description |
|-------|-------------|
| [implementation-planner](agents/implementation-planner/) | Translates feature requests into phased implementation plans using the 4-hour task theory and posts them as GitHub issue comments. |
| [implementation-executor](agents/implementation-executor/) | Takes an existing implementation plan from a GitHub issue and executes it — implementing each task sequentially, committing after each, pushing, and opening a PR. |
| [business-analyst](agents/business-analyst/) | Refines raw or ambiguous requests into clear, business-aligned, non-technical requirement documents with explicit scope and acceptance criteria. |

## Available Skills

Skills are companion wrappers for the agents above. Each skill guarantees its agent is always invoked (never bypassed), and creates a live task checklist in the terminal so you can see progress step by step.

| Skill | Wraps Agent | Description |
|-------|-------------|-------------|
| [cc-business-analyst](skills/cc-business-analyst/) | `business-analyst` | Shows live progress and guarantees the business-analyst agent is always triggered for requirement refinement. |
| [cc-implementation-planner](skills/cc-implementation-planner/) | `implementation-planner` | Shows live progress and guarantees the implementation-planner agent is always triggered for technical planning. |
| [cc-implementation-executor](skills/cc-implementation-executor/) | `implementation-executor` | Shows live progress and guarantees the implementation-executor agent is always triggered for plan execution. |

> **Recommended:** Install both the agent and its companion skill together. The skill ensures the agent is always used correctly.

## Setting Up Agents & Skills in Your Project

> **Important:** Run the prompt below from your project's root directory so that Claude can access and review your project structure, tech stack, and conventions to automatically fill in placeholders.

### Steps

1. Open Claude Code in your project directory.
2. Copy and paste the prompt below.
3. Claude will review your codebase, set up the agent and skill files, and ask you about anything it can't infer on its own.

### Prompt

```
I want to set up Claude Code agents and skills from the engineering-recipes repo into this project.

Source repo: https://github.com/ColoredCow/engineering-recipes (browse the `claude/agents/` directory for all available agents and their READMEs, and `claude/skills/` for all available skills).

For each agent in `claude/agents/`:

1. Read the agent's template file and its README (which contains the placeholder reference and example values).
2. Copy the agent template to `.claude/agents/<agent-name>.md` in this project.
3. Replace all `{{PLACEHOLDER}}` values with project-specific values by:
   a. First, explore this project's codebase — look at the directory structure, config files, package.json/requirements.txt, existing patterns, test setup, and conventions to infer as many placeholder values as possible.
   b. For any placeholder you cannot confidently determine from the codebase, ask me before proceeding. Present what you've inferred so far and ask only about the ones you're unsure of.
4. If the agent template has optional sections that don't apply to this project (e.g., Multi-Repository Context for a single-repo project), remove them.

For each skill in `claude/skills/`:

5. Copy the entire skill directory to `.claude/skills/<skill-name>/` in this project (skills have no placeholders — copy as-is).

Then:

6. Register all set-up agents and skills in this project's CLAUDE.md. Create CLAUDE.md if it doesn't exist. Do NOT mention how to manually invoke agents or skills — Claude Code handles invocation automatically based on their description frontmatter.

   For agents, add a "Custom Agents" section. Example format:

   ## Custom Agents
   Custom agents are defined in `.claude/agents/`. They are automatically invoked based on your request.

   | Agent | When to Use |
   |-------|-------------|
   | `business-analyst` | When the user shares rough requirements and needs them refined into clear, business-readable, testable requirement docs without technical implementation details. |
   | `implementation-planner` | When the user asks for an implementation plan, technical breakdown, or task planning for a feature or issue. |
   | `implementation-executor` | When the user wants to execute an existing implementation plan — reads the plan from a GitHub issue, implements each task sequentially, commits, pushes, and opens a PR. |

   For skills, add a "Custom Skills" section. Example format:

   ## Custom Skills
   Custom skills are defined in `.claude/skills/`. They wrap agents to guarantee correct invocation and show live task progress.

   | Skill | Purpose |
   |-------|---------|
   | `cc-business-analyst` | Triggers the business-analyst agent with task tracking |
   | `cc-implementation-planner` | Triggers the implementation-planner agent with task tracking |
   | `cc-implementation-executor` | Triggers the implementation-executor agent with task tracking |

After setup, show me a summary of what was configured and any values you'd recommend I review or adjust.
```
