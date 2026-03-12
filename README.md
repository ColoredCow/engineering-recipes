# Engineering Recipes

Reusable, opinionated engineering practices and automation patterns used across ColoredCow projects.

This repository is a reference library.
Individual projects opt into recipes by copying or referencing them.

## Recipes

| Category | Recipe | Description |
|----------|--------|-------------|
| Automated Code Review | [automated-code-review/](automated-code-review/) | Automated code review patterns |
| Claude Agents | [claude/agents/implementation-planner/](claude/agents/implementation-planner/) | Claude Code agent that creates 4-hour task breakdown implementation plans from feature requirements and posts them to GitHub issues |
| Claude Agents | [claude/agents/implementation-executor/](claude/agents/implementation-executor/) | Claude Code agent that executes an existing implementation plan from a GitHub issue — implementing tasks sequentially, committing after each, and opening a PR |
| Claude Agents | [claude/agents/business-analyst/](claude/agents/business-analyst/) | Claude Code agent that refines raw or ambiguous feature requests into clear, business-aligned, non-technical requirement documents |
| Claude Agents | [claude/agents/knowledge-base-manager/](claude/agents/knowledge-base-manager/) | Claude Code agent that syncs the project knowledge base with GitHub issue state — the only agent with write access to KB files |
| Knowledge Base | [knowledge-base/](knowledge-base/) | Hybrid project-local KB starter kit with numbered-flat Tier 1 files, advanced context modules, scaffolding, and validation |

## Hybrid Knowledge Base

The current KB model is a hybrid starter kit:
- `engineering-recipes` owns the reusable contract, templates, scaffold tools, and validation helpers.
- Each project owns its instantiated KB inside its own repo.
- Tier 1 is small and required.
- Tier 2 is optional and loaded on demand.
- The default structure is numbered-flat so agents can read sections selectively and update Tier 1 reliably.
- Validation is explicit and lightweight after setup.

Start with [knowledge-base/README.md](knowledge-base/README.md).

Key KB rollout documents:
- [knowledge-base/KB-CONTRACT-V1-PILOT-SCOPE.md](knowledge-base/KB-CONTRACT-V1-PILOT-SCOPE.md)
- [knowledge-base/ADOPTION-GUIDE.md](knowledge-base/ADOPTION-GUIDE.md)
