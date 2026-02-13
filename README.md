# Engineering Recipes

Reusable, opinionated engineering practices and automation patterns used across ColoredCow projects.

This repository is a reference library.
Individual projects opt into recipes by copying or referencing them.

## Recipes

| Category | Recipe | Description |
|----------|--------|-------------|
| Automated Code Review | [automated-code-review/](automated-code-review/) | Automated code review patterns |
| Claude Agents | [claude/agents/implementation-planner/](claude/agents/implementation-planner/) | Claude Code agent that creates 4-hour task breakdown implementation plans from feature requirements and posts them to GitHub issues |
| Claude Agents | [claude/agents/bug-investigator/](claude/agents/bug-investigator/) | Claude Code agent that investigates bugs — clarifies symptoms, builds reproduction profiles, isolates root causes, and proposes solution options. Designed as a first pass before the implementation-planner creates the fix plan. |
