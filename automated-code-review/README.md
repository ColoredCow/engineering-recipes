# Claude-based Code Review

## Steps to enable in a project

1. Add repository secret:
   - `ANTHROPIC_API_KEY`

2. Copy the workflow file into:
   `.github/workflows/code-review.yml`

3. Open a pull request.
   The bot will comment with review feedback.

Notes:
- This does not block merges by default.
- Each project should use its own API key.
