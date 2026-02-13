# Bug Investigator Agent

A Claude Code agent that systematically investigates bugs — from clarifying symptoms to isolating root causes to proposing solution options with trade-offs. Designed as the **first pass** before implementation: a human reviews the findings, and the `implementation-planner` agent handles the fix plan in the **second pass**.

## What It Does

- Clarifies expected vs. actual behavior from the bug report
- Builds a reproduction profile (who, where, when, how, what data)
- Traces the issue through the codebase to isolate the root cause
- Proposes 2–3 solution options with complexity, risk, and trade-off analysis
- Posts the investigation report directly as a GitHub issue comment for team visibility
- Flags anything it cannot verify from code alone — so the human knows what to test
- Builds persistent memory of your project's common bug patterns over time

## How It Fits in the Workflow

```
Bug reported → bug-investigator agent → investigation report posted to issue
                                              ↓
                                   Human reviews & validates
                                              ↓
                              Human confirms approach & solution
                                              ↓
                        implementation-planner agent → fix plan posted to issue
                                              ↓
                                     Developer implements fix
```

## Setup

### 1. Copy the agent file

```bash
cp bug-investigator.md <your-project>/.claude/agents/bug-investigator.md
```

### 2. Replace the placeholders

Open the copied file and replace each `{{PLACEHOLDER}}` with your project-specific values. See the reference table below.

### 3. Register in your project's CLAUDE.md

Add the following row to your project's `CLAUDE.md` under the "Custom Agents" section:

```markdown
| `bug-investigator` | When the user reports a bug, wants to investigate unexpected behavior, or needs root-cause analysis for a defect. Accepts a GitHub issue URL/number, investigates the codebase, and posts an investigation report with reproduction steps, root cause, and solution options to the GitHub issue. |
```

## Placeholder Reference

| Placeholder | Description | Example (Django project) | Example (Next.js project) |
|---|---|---|---|
| `{{TECH_STACK}}` | Primary technologies the project uses | `Django REST Framework, Python backend systems` | `Next.js, TypeScript, React` |
| `{{PROJECT_NAME}}` | Name of the project/platform | `IAGES` | `Acme Dashboard` |
| `{{FRONTEND_REPO_RELATIVE_PATH}}` | Relative path from this repo to the sibling frontend repo. Remove the entire Multi-Repository Context section if not applicable. | `../iages-frontend` | `../acme-web` |
| `{{REPRODUCTION_CHECKLIST}}` | Extra context-specific items to check when reproducing (see example below) | *(see below)* | *(see below)* |
| `{{CODEBASE_INVESTIGATION_CHECKLIST}}` | Bullet list of what to trace through when investigating (see example below) | *(see below)* | *(see below)* |
| `{{PROJECT_SPECIFIC_GUIDELINES}}` | Key patterns, conventions, and debugging tips specific to your project (see example below) | *(see below)* | *(see below)* |
| `{{MEMORY_RECORDING_EXAMPLES}}` | Bullet list of what kind of debugging patterns the agent should record in its memory | *(see below)* | *(see below)* |

## Example Values

### `{{REPRODUCTION_CHECKLIST}}` — Django project

```markdown
Check these additional reproduction factors:
- **Authentication state:** Is the user logged in? What token/session state?
- **Role & permissions:** What role does the affected user have? Are permission classes filtering data differently?
- **Database state:** Are there missing records, null fields, or orphaned foreign keys involved?
- **Celery tasks:** If async processing is involved, did the task complete? Check task logs.
- **API request/response:** What does the actual API payload look like? Check for missing or malformed fields.
- **Migration state:** Is the database schema in sync with the models? Were migrations run after the last deploy?
```

### `{{REPRODUCTION_CHECKLIST}}` — Next.js project

```markdown
Check these additional reproduction factors:
- **Authentication state:** Is the user logged in? Is the session/token valid or expired?
- **Role & permissions:** Does the user's role affect what data or UI they see?
- **Browser & device:** Is this browser-specific? Desktop vs. mobile?
- **Network conditions:** Are API calls failing silently? Check for CORS or timeout issues.
- **Hydration mismatches:** Is the server-rendered HTML different from client-side rendering?
- **Cache state:** Is stale data being served from browser cache, CDN, or React Query/SWR cache?
- **Build artifacts:** Was the latest deployment built from the correct branch? Check build logs.
```

### `{{CODEBASE_INVESTIGATION_CHECKLIST}}` — Django project

```markdown
- Trace the request path: URL pattern → view → serializer → service → model
- Check permission classes on the affected view — are they filtering correctly?
- Read the queryset logic — are filters, annotations, or prefetch_related calls correct?
- Check for try/except blocks that may be silently swallowing errors
- Look at the serializer validation — is it rejecting valid input or accepting invalid input?
- If Celery tasks are involved, trace the task chain and check for retry/failure handling
- Check if signals or post_save hooks are triggering unexpected side effects
- Review the migration history for the affected models — was a recent migration problematic?
- Look at related test files — do existing tests cover this scenario? If they pass, why?
```

### `{{CODEBASE_INVESTIGATION_CHECKLIST}}` — Next.js project

```markdown
- Trace the data flow: user action → event handler → API call → server response → state update → render
- Check the API route or server action handling the request — is it returning the right data?
- Read the component logic — are conditional renders, useEffect dependencies, or state updates correct?
- Look for race conditions in async operations (concurrent fetches, stale closures)
- Check error boundaries and error handling — are errors being caught and displayed properly?
- If using React Query/SWR, check cache keys, invalidation logic, and stale time settings
- Review middleware — is the request being redirected, blocked, or modified unexpectedly?
- Check TypeScript types vs. runtime data — is there a mismatch between expected and actual API shapes?
- Look at related test files — do existing tests cover this scenario? If they pass, why?
```

### `{{PROJECT_SPECIFIC_GUIDELINES}}` — Django project

```markdown
- **Read the actual code:** Don't guess from function names. Read the implementation of views, serializers, and services involved in the bug.
- **Be specific with locations:** Always reference exact file paths and line numbers (e.g., `apps/assessment/views/submission.py:L142`).
- **Check the permission layer:** Many bugs in this project stem from permission classes filtering querysets differently per role.
- **Check the service layer:** Business logic lives in services, not views — that's where most logic bugs hide.
- **Inspect serializer validation:** Serializers may silently drop fields or transform data unexpectedly.
- **Look for silent failures:** Check for bare `except` blocks, missing logging, or Celery tasks that fail without alerting.
- **Don't assume the ORM does what you think:** Read the actual SQL if needed (`queryset.query`). Annotations and aggregations are common sources of bugs.
- **Flag what you can't verify:** If reproduction requires specific data or environment access, say so clearly.
```

### `{{PROJECT_SPECIFIC_GUIDELINES}}` — Next.js project

```markdown
- **Read the actual code:** Don't guess from component names. Read the implementation of components, hooks, and API routes involved in the bug.
- **Be specific with locations:** Always reference exact file paths and line numbers (e.g., `src/components/dashboard/Chart.tsx:L87`).
- **Check server vs. client:** Many bugs stem from code running on the server when it expects browser APIs, or vice versa.
- **Inspect data shapes:** Check that API responses match the TypeScript interfaces the components expect. Runtime != compile-time.
- **Look for hydration issues:** If the bug only appears on first load or after refresh, it may be a server/client rendering mismatch.
- **Check effect dependencies:** Missing or extra dependencies in useEffect/useMemo/useCallback are a top source of bugs.
- **Look for silent failures:** Check for missing error handling in fetch calls, unhandled promise rejections, or swallowed exceptions.
- **Flag what you can't verify:** If reproduction requires specific user accounts, environments, or data, say so clearly.
```

### `{{MEMORY_RECORDING_EXAMPLES}}` — Django project

```markdown
- Common bug patterns found and their root causes (e.g., "permission filtering on X queryset causes Y")
- Silent failure points — places where errors are swallowed
- Frequently affected code paths and their quirks
- Data integrity patterns — common null/orphan scenarios
- Celery task failure patterns and recovery approaches
- Permission class behavior differences across roles
- Test coverage gaps discovered during investigations
```

### `{{MEMORY_RECORDING_EXAMPLES}}` — Next.js project

```markdown
- Common bug patterns found and their root causes (e.g., "stale cache after mutation on X page")
- Hydration mismatch patterns and their fixes
- API response shape inconsistencies discovered
- State management pitfalls in specific components
- Race condition patterns in async operations
- Browser-specific rendering issues
- Test coverage gaps discovered during investigations
```

## Usage

Once set up, the agent is triggered automatically when you report or reference a bug:

```
> Users are getting a 500 error when they try to submit the assessment form
> The export feature works for admins but not for regular users
> Investigate the bug in issue #87
> This was working last week but now the dashboard is broken
```

The agent will:
1. Ask for a GitHub issue number (if not provided)
2. Clarify expected vs. actual behavior (if not clear from the report)
3. Investigate the codebase to build reproduction steps and isolate the root cause
4. Propose solution options with trade-offs
5. Post the investigation report as a comment on the GitHub issue
6. The human reviews, validates, and picks an approach
7. The `implementation-planner` agent creates the fix plan in the second pass
