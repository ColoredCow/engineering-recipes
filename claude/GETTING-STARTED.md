# Getting Started with AI at ColoredCow

Welcome to how we use AI as a team. This document covers everything you need to get started — read it top to bottom before your first session.

---

## 1. Claude basics

If you've used ChatGPT before, Claude works similarly at the surface. A few things worth knowing upfront:

- Claude follows detailed instructions very well. The more context you give it, the better the output.
- Claude Chat is the starting point — open [claude.ai](https://claude.ai) and sign in with your work account.
- Claude Code is where most of the real engineering work happens — it has full context of your project folder. More on this in the next section.

**Opening Claude Chat:**

![Claude Chat interface showing the three options — Chat, Cowork, and Code](images/claude-chat-interface.png)

---

## 2. Claude Code and sub-agents

Claude Code is the CLI tool that connects Claude to your actual project. Once set up, Claude can read your folder structure, understand your codebase, and give you relevant answers instead of generic ones.

### Step 1 — Install Claude Code

Use the native installer for your OS. No Node.js required.

**macOS**
```bash
curl -fsSL https://claude.ai/install.sh | bash
```

**Linux**
```bash
curl -fsSL https://claude.ai/install.sh | bash
```

**Windows (PowerShell)**
```powershell
irm https://claude.ai/install.ps1 | iex
```

> **Windows tip:** Run this in PowerShell, not CMD. If you see `'irm' is not recognized`, you're in CMD — switch to PowerShell. If you prefer a Linux environment on Windows, install WSL first and then use the Linux command above inside it.

Verify the install:
```bash
claude --version
```

### Step 2 — Authenticate

Run `claude` in your terminal. On first launch it opens your browser — log in with your work Anthropic account and authorise. The session token is stored locally so you only do this once.


### Step 3 — Initialise Claude in your project

Navigate to your project folder and run:

```bash
cd your-project
claude init
```

`claude init` reads your entire project structure and creates a `CLAUDE.md` file. This is the most important file — Claude reads it first on every session to understand your project context.


### Step 4 — Set up the ColoredCow agents

We maintain three finalized agents in the [engineering-recipes repo](https://github.com/ColoredCow/engineering-recipes) under the `/claude/` folder.

**To add them to your project:**

1. Go to [`coloredcow/engineering-recipes`](https://github.com/ColoredCow/engineering-recipes) → `/claude/`
2. Copy the setup prompt from there
3. Paste it into your Claude Code session — it replaces the placeholders with your project's context and creates all three agents automatically

![Engineering recipes repo /claude/ folder](images/engineering-recipes-claude-folder.png)

Once done, type `/agent` in Claude Code to see the three agents listed under your project.

![Claude Code showing Business Analyst, Implementation Planner, Implementation Executor listed](images/claude-code-agents-list.png)

### The three agents

**Business Analyst**
Converts a vague 2–3 line requirement into a fully scoped document. Give it the GitHub issue URL — it reads the codebase, asks open questions where context is missing, and produces a final requirement with purpose, scope, acceptance criteria, and open questions.

```
# Example usage in Claude Code
Use the business-analyst agent.
Issue: https://github.com/your-org/your-project/issues/123
Don't assume anything. Post all open questions first.
```

**Implementation Planner** *(uses Opus)*
Takes a refined requirement and produces a full technical plan — frontend/backend file-level changes, DB impact, task breakdown using the 4-hour theory, and a testing strategy. Review the plan before handing it to the executor.

```
# Example usage in Claude Code
Use the implementation-planner agent.
Requirement: [paste refined requirement here]
```

**Implementation Executor** *(uses Sonnet)*
Takes an approved implementation plan and executes it — creates a checklist, syncs the branch, implements changes file by file, and pushes. Only use this after the plan has been reviewed.

```
# Example usage in Claude Code
Use the implementation-executor agent.
Plan: [paste approved plan here]
```

> **Note:** If your project (IGS, Sneha, Spark) already has Claude set up, skip Steps 3 and 4 — open Claude Code from the project folder and the agents are already there.

---

## 3. Contribute back

If you build a new agent, find a useful prompt pattern, or identify a gap — add it to the engineering recipes repo.

**Areas with no agents yet:** SEO, DevOps, Playwright/Cypress, QA automation patterns, performance auditing.

To contribute:
- Make your agent generic (project-specific context goes in placeholders, not hardcoded)
- Open a PR in [coloredcow/engineering-recipes](https://github.com/coloredcow/engineering-recipes)
- Tag it with `agent` or `skill` accordingly

The repo grows because people contribute back. If it worked for you, it will work for someone else.

---

## 4. Limits, models, and prompting

### Session and weekly limits

- You have a **per-session limit** (~4–5 hours of active usage)
- You have a **weekly limit** on top of that
- Claude Code shows a warning at 90% usage — plan accordingly

![Claude Code Usage Tracking](images/claude-code-usage-tracking.png)

### Which model to use

| Task | Model |
|---|---|
| Planning, research, complex reasoning | **Opus** |
| Coding, execution, implementation | **Sonnet** |
| Quick lookups, tool comparisons, internet search | **Haiku** |

**Extended thinking** is available on all models. Enable it when normal prompting isn't giving you a clean solution — it gives Claude extra time to reason before responding.

### Prompting tips

- **Give it a role:** "You are a senior backend engineer working on a multi-tenant SaaS app."
- **Be explicit about format:** Tell it exactly what you want — bullet points, a table, JSON, a numbered plan.
- **Use XML tags for large inputs:** Wrap code, docs, or long text in `<document>` tags so Claude processes it cleanly.
- **Ask for step-by-step reasoning:** Adding "think step by step" improves output quality on complex tasks.
- **Iterate in the same conversation:** Claude remembers the full context. Don't start a new chat — just refine in place.

---

## 5. Ask ColoredCow

We have a custom Google Chat integration that lets you query your project's Slack/Chat history directly from Claude.

### Connecting it

1. Open [claude.ai](https://claude.ai)
2. Go to connectors / available apps
3. Find **ColoredCow Google Chat** and click Connect
4. Authenticate with your work Google account

![Connectors screen showing ColoredCow Google Chat with Connect button](images/google-chat-connector.png)

### Using it

Once connected, you can ask things like:

- *"Summarise all activity in the Sneha LMS channel from the last week"*
- *"What deployments happened in the past month on this project?"*
- *"Find the discussion we had about CI/CD workflow in March"*

---

## 6. Two different Claude accounts — important

We have **two separate Claude setups** and they are billed differently:

| | Team account | Code review API |
|---|---|---|
| What it is | claude.ai team subscription | Anthropic API used in our GitHub workflow |
| Who pays | ColoredCow | ColoredCow — per API call |
| What it's for | Your daily use, sub-agents, Claude Code | Automated PR code reviews |
| How to access | Sign in at claude.ai | Triggered by the `ready for review` label on a PR |

**The code review API costs money per call.** Only add the `ready for review` label when your PR is actually ready. Don't use it for early drafts or WIP reviews.

![GitHub PR showing the ready for review label](images/github-pr-ready-for-review-label.png)

---

## 7. Keep exploring other tools

Claude is our primary AI tool but it shouldn't be your only one. A few reasons:

- Limits get hit — if Claude is unavailable, you shouldn't be stuck
- Other tools are better at specific things — Codex for execution, etc
- The goal is to grow your ability to use AI effectively — not to use one tool the same way forever

The team currently uses:
- **Claude** — planning, agents, complex reasoning
- **Codex** — execution and implementation (saves Claude credits)

Try them. See where each one performs better. Bring what you learn back to the team.

---



*To update this doc — open a PR in [coloredcow/engineering-recipes](https://github.com/coloredcow/engineering-recipes). Don't let it go stale.*