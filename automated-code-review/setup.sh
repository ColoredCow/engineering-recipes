#!/usr/bin/env bash

set -e

BRANCH_NAME="chore/enable-automated-code-review"

WORKFLOW_DIR=".github/workflows"
WORKFLOW_FILE="$WORKFLOW_DIR/code-review.yml"

CODE_REVIEW_DOCS_DIR="docs/code-review"
GUIDELINES_FILE="$CODE_REVIEW_DOCS_DIR/review-guidelines.md"

ENGINEERING_RECIPES_BASE_URL="https://raw.githubusercontent.com/ColoredCow/engineering-recipes/main"
RECIPE_WORKFLOW_URL="$ENGINEERING_RECIPES_BASE_URL/automated-code-review/workflow.yml"
TEMPLATE_GUIDELINES_URL="$ENGINEERING_RECIPES_BASE_URL/automated-code-review/templates/review-guidelines.md"

echo "▶️  Setting up automated code review"
echo "-----------------------------------"

# STEP 1 — Create setup branch
if git show-ref --quiet refs/heads/"$BRANCH_NAME"; then
  echo "ℹ️  Branch $BRANCH_NAME already exists, checking it out"
  git checkout "$BRANCH_NAME"
else
  echo "➡️  Creating setup branch: $BRANCH_NAME"
  git checkout -b "$BRANCH_NAME"
fi

# STEP 2 — Create workflow directory if missing
if [ ! -d "$WORKFLOW_DIR" ]; then
  echo "➡️  Creating $WORKFLOW_DIR directory"
  mkdir -p "$WORKFLOW_DIR"
else
  echo "ℹ️  $WORKFLOW_DIR already exists"
fi

# STEP 3 — Pull the workflow recipe
echo "➡️  Fetching code review workflow from engineering-recipes"
curl -fsSL "$RECIPE_WORKFLOW_URL" -o "$WORKFLOW_FILE"

echo "✅ Workflow added at $WORKFLOW_FILE"

# STEP 4 — Add code-review guidelines (Claude / LLM specific)
if [ ! -f "$GUIDELINES_FILE" ]; then
  echo "➡️  Adding default automated code review guidelines"
  mkdir -p "$CODE_REVIEW_DOCS_DIR"

  curl -fsSL "$TEMPLATE_GUIDELINES_URL" -o "$GUIDELINES_FILE"

  echo "✅ Guidelines added at $GUIDELINES_FILE"
else
  echo "ℹ️  Code review guidelines already exist, skipping"
fi

# STEP 5 — Commit changes
echo "➡️  Committing changes (if any)"

git add "$WORKFLOW_FILE" "$GUIDELINES_FILE"

git commit --no-verify -m "chore: enable automated code review" \
  || echo "ℹ️  No changes to commit"

# STEP 6 — Push branch
echo "➡️  Pushing branch to origin"
git push -u origin "$BRANCH_NAME"

echo ""
echo "🎉 Setup complete!"
echo "Next steps:"
echo "1. Open a Pull Request from '$BRANCH_NAME' to main/develop"
echo "2. Ensure the Code Review GitHub App is installed"
echo "3. Add ANTHROPIC_API_KEY as a GitHub Actions secret"
echo "4. Add the label 'status: ready for review' to trigger review"
