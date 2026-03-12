# Claude Agents

This directory contains reusable, templatized Claude Code agents that can be set up in any project.

## Available Agents

| Agent | Description |
|-------|-------------|
| [implementation-planner](agents/implementation-planner/) | Translates feature requests into phased implementation plans using the 4-hour task theory and posts them as GitHub issue comments. |
| [implementation-executor](agents/implementation-executor/) | Takes an existing implementation plan from a GitHub issue and executes it — implementing each task sequentially, committing after each, pushing, and opening a PR. |
| [business-analyst](agents/business-analyst/) | Refines raw or ambiguous requests into clear, business-aligned, non-technical requirement documents with explicit scope and acceptance criteria. |
| [knowledge-base-manager](agents/knowledge-base-manager/) | Syncs the project knowledge base with GitHub issue activity — the only agent with write access to the KB. |

## Knowledge Base Contract

These agents now prefer the numbered-flat hybrid KB contract:
- entry file: `knowledge-base/00-master.md`
- runtime config: `knowledge-base/.kb-config.yml`
- core files: `01-business-flows.md`, `02-architecture.md`, `03-risk-model.md`, `04-active-sprint.md`
- consumer agents remain read-only when using the KB
- `knowledge-base-manager` is the only write-enabled KB automation flow

Older numbered-tree and legacy-flat KB layouts remain supported as fallbacks.

## Setting Up Agents in Your Project

> Run the install steps from your project's root directory so the agent can inspect that project directly.

1. Copy the relevant agent markdown file into `.claude/agents/` in the target project.
2. If the target project uses the hybrid knowledge base, also install the KB starter kit from [`knowledge-base/`](../knowledge-base/).
3. Register the agents in the project's root `CLAUDE.md` if needed.

## Copy-Paste Install Prompt

Paste the following prompt into your coding agent session from the target project's root directory:

```text
I want to set up Claude Code agents from the `https://github.com/anuragk16/engineering-recipes` repo into this project.

Source repo: read the `claude/agents/` directory and each agent's README.

Follow these steps exactly:

1. Explore this project's codebase shallowly:
   - README
   - top-level config files
   - top-level directory structure
   - existing `CLAUDE.md` if present

2. Ensure `.claude/agents/` exists in this project.
   - Create it if missing.

3. Copy the relevant agent templates from the source repo into `.claude/agents/`:
   - `implementation-planner`
   - `implementation-executor`
   - `business-analyst`
   - `knowledge-base-manager` if this project will use the knowledge base

4. For each copied agent:
   - Read the agent template and README
   - Replace `{{PLACEHOLDER}}` values only when they can be inferred confidently from this codebase
   - If a value cannot be inferred confidently, stop and ask me only about the unresolved placeholders
   - Remove optional sections that clearly do not apply to this project

5. Check whether this project already has a hybrid knowledge base:
   - `knowledge-base/00-master.md`
   - `knowledge-base/.kb-config.yml`
   If it does, keep the KB-aware instructions in the agents.
   If it does not, leave the agent KB guidance intact because the agents already degrade gracefully when no KB exists.

6. Update the project root `CLAUDE.md`:
   - If it does not exist, create it
   - Add a `Custom Agents` section if missing
   - Register the installed agents in a table
   - Add or preserve the `Knowledge Base` section only if this project has a KB or I ask you to install one

7. At the end, show me:
   - which agents were installed
   - which placeholders were inferred
   - which placeholders still need input
   - whether `CLAUDE.md` was created or updated
```

### Recommended Order

1. Install the hybrid KB starter kit first if the project needs structured AI context.
2. Then run the agent installation prompt.

This keeps the downstream `CLAUDE.md` and KB-aware agent behavior aligned from the start.

For KB installation guidance, start with [knowledge-base/README.md](../knowledge-base/README.md).
