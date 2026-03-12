# Install Hybrid Knowledge Base

Paste the following prompt into the target project's coding agent session from the project root.

```text
I want to install the hybrid knowledge base starter kit from the `https://github.com/anuragk16/engineering-recipes` repository into this project.

Source directory to read from:
- `knowledge-base/templates/`
- `knowledge-base/templates/advanced/`
- `knowledge-base/templates/.kb-config.yml`
- `knowledge-base/templates/CLAUDE.section.md`
- `knowledge-base/project-files/KB-PROCESS.md`
- `knowledge-base/scripts/scaffold_hybrid_kb.py`
- `knowledge-base/scripts/validate_hybrid_kb.py`
- `claude/agents/knowledge-base-manager/knowledge-base-manager.md`
- `claude/agents/knowledge-base-manager/README.md`

Follow these steps exactly:

1. Explore this project shallowly:
   - README
   - top-level config files
   - top-level directory structure
   - the 5 most recent git commits
2. Check whether `knowledge-base/` already exists.
   - If it exists, do not overwrite files silently.
   - Show me which files already exist, which are missing, and whether this looks like a partial install.
   - Ask how to proceed before making changes.
3. Evaluate whether Tier 2 is needed for this project before installing anything.
   - Use evidence only from the codebase and project docs.
   - Consider Tier 2 justified only when the project shows real complexity such as:
     - recurring incidents or fragile areas
     - multiple external integrations
     - long-lived architecture decisions worth preserving
     - hard technical or business constraints
     - meaningful shipped feature history that would help onboarding
   - If Tier 2 does NOT appear justified, recommend Tier 1 only.
4. If Tier 2 may be useful, present a recommendation table before creating any Tier 2 files.
   For each optional file below, mark one of: `Recommend`, `Optional`, `Do Not Recommend`, and give a one-line reason.
   - `advanced/decision-log.md`
   - `advanced/incident-log.md`
   - `advanced/feature-history.md`
   - `advanced/integration-map.md`
   - `advanced/metrics.md`
   - `advanced/known-constraints.md`
5. Ask me whether I want Tier 2 for this project.
   - If I say no: continue with Tier 1 only.
   - If I say yes: ask me to confirm exactly which Tier 2 files to include, using your recommendations as the default suggestion.
   - Do not install any Tier 2 files until I confirm the selection.
6. Install the starter kit by running the reusable scaffold script from the source repo instead of manually recreating the template files.
   - Prefer running `knowledge-base/scripts/scaffold_hybrid_kb.py` from the source repo against this project root.
   - Use `--enable` only for the Tier 2 modules I confirmed.
   - Use `--install-kb-manager` if this project uses Claude agents.
   - Use `--install-kb-process` if this project does not already have a KB workflow doc.
   - Only fall back to manual file copying if the scaffold script cannot be run.
   - The install must create the numbered flat hybrid contract:
     - `00-master.md`
     - `01-business-flows.md`
     - `02-architecture.md`
     - `03-risk-model.md`
     - `04-active-sprint.md`
     - `.kb-config.yml`
     - `advanced/` only when Tier 2 modules are selected
     - `scripts/` for helper scripts
7. Complete the project-level ownership and policy fields in `knowledge-base/.kb-config.yml`.
   - Fill at least the named owners for:
     - `kb_process`
     - `business_flows`
     - `architecture`
     - `risk_model`
     - `active_sprint`
   - Keep `agent_policy` aligned with the KB contract:
     - consumers are read-only
     - only `knowledge-base-manager` automates writes
8. After scaffolding, replace placeholders only when you can infer values confidently from the codebase.
   - Do not rewrite the entire KB templates.
   - Fill only the fields you can justify from project evidence.
   - Keep the rest of the starter-kit structure intact.
9. If a value cannot be inferred confidently, leave the placeholder unchanged and list it in your summary. Do not guess.
10. Check whether `.claude/agents/knowledge-base-manager.md` already exists.
   - If it does not exist:
     - create `.claude/agents/` if needed
     - copy `claude/agents/knowledge-base-manager/knowledge-base-manager.md` into `.claude/agents/knowledge-base-manager.md`
   - If it already exists: do not overwrite it silently. Mention that it already exists in your summary.
11. Add the `Knowledge Base` section from `CLAUDE.section.md` to the project root `CLAUDE.md` if it is not already present.
12. Ensure the project root `CLAUDE.md` has a `Custom Agents` section that includes `knowledge-base-manager`.
    - If the section is missing, create it.
    - If the section exists but does not list `knowledge-base-manager`, add it.
    - Do not duplicate an existing entry.
13. If the project does not already have a KB workflow doc, copy `knowledge-base/project-files/KB-PROCESS.md` to `docs/kb-process.md`.
14. Run the installed validator from this project's root:
    - `python3 knowledge-base/scripts/validate_hybrid_kb.py .`
    - If validation fails, show me the errors and stop.
    - If validation passes with warnings, summarize the warnings and which ones are expected placeholders vs real setup gaps.
15. At the end, show me:
   - files created
   - whether the scaffold script was used or whether you had to fall back to manual copying
   - placeholders inferred
   - placeholders left unresolved
   - whether Tier 2 was recommended
   - which Tier 2 files were recommended vs not recommended
   - Tier 2 modules enabled
   - owners assigned in `.kb-config.yml`
   - whether `knowledge-base-manager` agent was installed or already existed
   - whether the KB process doc was installed
   - the exact scaffold command that was run
   - the exact validation command that was run
```
