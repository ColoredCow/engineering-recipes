## Knowledge Base

This project stores structured context in `knowledge-base/`.

### Reading Rules
- Read `knowledge-base/00-master.md` first.
- If `knowledge-base/.kb-config.yml` exists, use it as the source of truth for enabled modules and loading defaults.
- Load only the files needed for the current task.
- Treat KB files as read-only unless you are the designated KB maintenance flow.
- If the numbered flat KB does not exist, you may fall back to the older numbered tree layout or the legacy flat layout if present.

### Write Policy
- Consumer agents are read-only.
- Only `knowledge-base-manager` may automate KB writes.
- If KB context is missing or clearly incomplete, do not fabricate facts.

### Delivery Rule
- Every task must make an explicit KB impact decision before it is considered done.

### Graceful Degradation
If no knowledge base exists, proceed normally without KB-aware behavior.
