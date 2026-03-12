# Hybrid KB Review Checklist

Use this checklist for KB template, script, or spec changes.

- Does this change belong in Tier 1 or Tier 2?
- If Tier 1, is it truly required for every project?
- Does it increase the default read set or token cost?
- Does it preserve the frozen v1 pilot contract?
- Is the file still concise and scannable?
- Do canonical templates include the shared section headings?
- Do KB content templates include the expected front matter fields?
- If owners or freshness rules changed, is `.kb-config.yml` still sufficient to validate them?
- Is ownership clear: human, automation, or mixed with explicit review?
- Does the change preserve tool-agnostic plain Markdown content?
- If config changed, was `.kb-config.yml` compatibility considered?
- If automation changed, does it remain safe on repeated runs?
- If legacy support changed, is the compatibility impact documented?
