# Engineering Recipes

Reusable, opinionated engineering practices and automation patterns used across ColoredCow projects.

This repository is a reference library.
Individual projects opt into recipes by copying or referencing them.

## Recipes

| Category | Recipe | Description |
|----------|--------|-------------|
| Automated Code Review | [automated-code-review/](automated-code-review/) | Automated code review patterns |
| Claude Agents | [claude/agents/implementation-planner/]
| Claude Agents | [claude/agents/quality-analyst/](https://github.com/ColoredCow/engineering-recipes/blob/main/claude/agents/quality-analyst) | Claude Code agent that generates requirement-driven test plans covering manual, functional, performance, security, accessibility, usability, and reliability test cases. Supports selective generation via `--type` flag. |(claude/agents/implementation-planner/) | Claude Code agent that creates 4-hour task breakdown implementation plans from feature requirements and posts them to GitHub issues |
| Claude Agents | [claude/agents/](claude/agents/) | Claude Code agents for requirement refinement, implementation planning, and plan execution |
| Claude Skills | [claude/skills/](claude/skills/) | Companion skills that guarantee correct agent invocation and show live task progress in the terminal |
