#!/usr/bin/env bash

set -e

BRANCH_NAME="chore/enable-claude-code-review"
WORKFLOW_DIR=".github/workflows"
WORKFLOW_FILE="$WORKFLOW_DIR/claude-code-review.yml"
GUIDELINES_FILE="docs/code-review-guidelines.md"
RECIPE_WORKFLOW_URL="https://raw.githubusercontent.com/ColoredCow/engineering-recipes/main/automated-code-review/claude/workflow.yml"

echo "▶️  Setting up Claude-based automated code review"
echo "-----------------------------------------------"

# STEP 1 — Create setup branch
echo "➡️  Creating setup branch: $BRANCH_NAME"
git checkout -b "$BRANCH_NAME"

# STEP 2 — Create workflow directory if missing
if [ ! -d "$WORKFLOW_DIR" ]; then
  echo "➡️  Creating $WORKFLOW_DIR directory"
  mkdir -p "$WORKFLOW_DIR"
else
  echo "ℹ️  $WORKFLOW_DIR already exists"
fi

# STEP 3 — Pull the workflow recipe
echo "➡️  Fetching Claude workflow from engineering-recipes"
curl -fsSL "$RECIPE_WORKFLOW_URL" -o "$WORKFLOW_FILE"

echo "✅ Workflow added at $WORKFLOW_FILE"

# STEP 4 — Add review guidelines (only if missing)
if [ ! -f "$GUIDELINES_FILE" ]; then
  echo "➡️  Adding default code review guidelines"
  mkdir -p "$(dirname "$GUIDELINES_FILE")"

  cat << 'EOF' > "$GUIDELINES_FILE"
# Code Review Guidelines

Focus areas:
- Readability and maintainability
- Avoiding unnecessary complexity
- Performance impact on critical user flows
- Database query efficiency
- Security implications (auth, payments, PII)

Be pragmatic. Suggest improvements, not rewrites.
EOF

  echo "✅ Guidelines created at $GUIDELINES_FILE"
else
  echo "ℹ️  Guidelines already exist, skipping"
fi

# STEP 5 — Commit changes
echo "➡️  Committing changes"
git add "$WORKFLOW_FILE" "$GUIDELINES_FILE"
git commit -m "chore: enable Claude-based automated code review"

# STEP 6 — Push branch
echo "➡️  Pushing branch to origin"
git push -u origin "$BRANCH_NAME"

echo ""
echo "🎉 Setup complete!"
echo "Next steps:"
echo "1. Open a Pull Request from '$BRANCH_NAME' to main"
echo "2. Add ANTHROPIC_API_KEY as a GitHub Actions secret"
echo "3. Add the 'Ready For Review' label to any PR to trigger review"
