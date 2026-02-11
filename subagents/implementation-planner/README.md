# Implementation Planner Subagent

A Claude Code subagent that translates high-level feature requests into comprehensive implementation plans using the **4-hour task theory** — every task broken into chunks of max 4 hours with clear definitions of done.

## What It Does

- Explores your codebase to understand existing patterns and architecture
- Creates phased implementation plans with dependency-aware task ordering
- Posts the plan directly as a GitHub issue comment for team visibility
- Handles multi-repository projects (e.g., separate backend + frontend repos)
- Builds persistent memory of your project's conventions over time

## Setup

### 1. Copy the agent file

```bash
cp implementation-planner.md <your-project>/.claude/agents/implementation-planner.md
```

### 2. Replace the placeholders

Open the copied file and replace each `{{PLACEHOLDER}}` with your project-specific values. See the reference table below.

### 3. Register in your project's CLAUDE.md

Add the following to your project's `CLAUDE.md`:

```markdown
## Custom Subagents

Custom subagents are defined in `.claude/agents/`. Use them via the Task tool with the matching `subagent_type`.

| Agent | When to Use |
|-------|-------------|
| `implementation-planner` | When the user asks for an implementation plan, technical breakdown, or task planning for a feature or issue. Accepts a GitHub issue URL/number, explores the codebase, creates a detailed plan with 4-hour task breakdowns, and posts it as a comment on the GitHub issue. |
```

## Placeholder Reference

| Placeholder | Description | Example (Django project) | Example (Next.js project) |
|---|---|---|---|
| `{{TECH_STACK}}` | Primary technologies the project uses | `Django REST Framework, Python backend systems` | `Next.js, TypeScript, React` |
| `{{PROJECT_NAME}}` | Name of the project/platform | `IAGES` | `Acme Dashboard` |
| `{{FRONTEND_REPO_RELATIVE_PATH}}` | Relative path from this repo to the sibling frontend repo. Remove the entire Multi-Repository Context section if not applicable. | `../iages-frontend` | `../acme-web` |
| `{{MODULE_TERM}}` | What you call a grouping of related code | `Django app` | `Module` |
| `{{CODEBASE_EXPLORATION_CHECKLIST}}` | Bullet list of what to explore in the codebase (see example below) | *(see below)* | *(see below)* |
| `{{PLAN_EXTRA_SECTIONS}}` | Additional sections in the plan template specific to your stack (e.g., Database Changes, API Endpoints). Use markdown. | *(see below)* | *(see below)* |
| `{{TEST_RUN_COMMAND}}` | Command to run tests | `pytest apps/<app>/tests/test_<feature>.py` | `npm test -- --testPathPattern=<module>` |
| `{{TEST_FRAMEWORK}}` | Testing framework used | `pytest` | `Jest + React Testing Library` |
| `{{PROJECT_SPECIFIC_GUIDELINES}}` | Key patterns, conventions, and constraints specific to your project (see example below) | *(see below)* | *(see below)* |
| `{{MEMORY_RECORDING_EXAMPLES}}` | Bullet list of what kind of patterns the agent should record in its memory | *(see below)* | *(see below)* |

## Example Values

### `{{CODEBASE_EXPLORATION_CHECKLIST}}` — Django project

```markdown
  - Which Django app(s) this touches (check `apps/` directory)
  - Existing models, serializers, views, services, and URL patterns in related apps
  - How similar features have been implemented in the codebase
  - What shared utilities exist in `apps/common/` that can be reused
  - Current database schema and relationships relevant to the feature
  - Permission classes and authentication patterns needed
  - Whether Celery tasks, signals, or other async patterns are needed
```

### `{{CODEBASE_EXPLORATION_CHECKLIST}}` — Next.js project

```markdown
  - Which modules/features this touches (check `src/` directory)
  - Existing components, hooks, API routes, and utility functions in related modules
  - How similar features have been implemented in the codebase
  - What shared components exist in `src/components/common/` that can be reused
  - Current data models and API integration patterns relevant to the feature
  - Authentication and authorization patterns needed
  - Whether server actions, API routes, or external API calls are needed
```

### `{{PLAN_EXTRA_SECTIONS}}` — Django project

```markdown
## 4. Database Changes

[List new models, fields, migrations needed — include field types and relationships]

## 5. API Endpoints

| Method | Endpoint | Description | Auth/Permissions |
|--------|----------|-------------|------------------|
| POST   | /api/v1/... | ... | ... |
```

### `{{PLAN_EXTRA_SECTIONS}}` — Next.js project

```markdown
## 4. Data Model Changes

[List new types/interfaces, database schema changes, API contract changes]

## 5. Routes & Pages

| Route | Page/Component | Description | Auth Required |
|-------|----------------|-------------|---------------|
| /dashboard/... | ... | ... | ... |
```

### `{{PROJECT_SPECIFIC_GUIDELINES}}` — Django project

```markdown
- **Follow existing patterns:** This project uses a service layer pattern, custom response helpers (`success_response`/`error_response`), and role-based permissions. Your plan must align with these.
- **Be specific with file paths:** Don't say "create a serializer" — say "create `apps/assessment/serializers/notification.py`"
- **Consider the full stack:** Models -> Migrations -> Serializers -> Services -> Views -> URLs -> Permissions -> Tests
- **Account for migrations:** Always include a task for creating and reviewing migrations
- **Include error handling:** Plan for error cases, validation, and the custom exception handler
- **Think about permissions:** Every endpoint needs appropriate permission classes
- **Consider async needs:** If the feature involves emails, heavy processing, or external API calls, plan for Celery tasks
- **Be realistic with estimates:** 4 hours is the MAX, not the target. Simple tasks can be 0.5h or 1h.
```

### `{{PROJECT_SPECIFIC_GUIDELINES}}` — Next.js project

```markdown
- **Follow existing patterns:** This project uses [your patterns]. Your plan must align with these.
- **Be specific with file paths:** Don't say "create a component" — say "create `src/components/dashboard/NotificationBell.tsx`"
- **Consider the full stack:** Types -> API layer -> Hooks -> Components -> Pages -> Tests
- **Include error handling:** Plan for error boundaries, loading states, and API error handling
- **Think about auth:** Every page/API route needs appropriate middleware or auth checks
- **Consider SSR vs CSR:** Decide whether components need server-side rendering or can be client-only
- **Be realistic with estimates:** 4 hours is the MAX, not the target. Simple tasks can be 0.5h or 1h.
```

### `{{MEMORY_RECORDING_EXAMPLES}}` — Django project

```markdown
- Model inheritance patterns and base classes used
- Service layer conventions in specific apps
- Common utility functions in apps/common/
- Permission class combinations used for similar features
- URL routing patterns and API versioning conventions
- Celery task patterns for async operations
- Test structure and fixture patterns across apps
```

### `{{MEMORY_RECORDING_EXAMPLES}}` — Next.js project

```markdown
- Component patterns and shared UI primitives
- Data fetching patterns (server components vs client hooks)
- API route conventions and middleware chains
- Authentication and authorization patterns
- State management approach and store structure
- Testing patterns and mock strategies
- Route organization and layout conventions
```

## Usage

Once set up, the agent is triggered automatically when you ask Claude Code to plan a feature:

```
> Plan the implementation for adding a notification system
> Break down this feature into tasks: [paste requirements]
> Create a technical breakdown for issue #42
```

The agent will:
1. Ask for a GitHub issue number (if not provided)
2. Explore your codebase to understand existing patterns
3. Generate a phased implementation plan with 4-hour tasks
4. Post the plan as a comment on the GitHub issue
