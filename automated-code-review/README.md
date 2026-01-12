# Automated Code Review

This recipe sets up **label-triggered automated code reviews** using Claude.

Reviews are posted as **PR comments** when you explicitly ask for them.

---

## Prerequisites


### 1. Get the Anthropic API key

* Contact **Infra Support** to request an **Anthropic API key** for your project
* Do **not** create or use personal keys
* Infra will share the key securely

### 2. Add the key as a GitHub Actions secret

In your **project repository**, add the key as a repository secret so GitHub Actions can access it.


**Steps:**
1. Go to your repository on GitHub
2. Navigate to:
   ```
   Settings → Secrets and variables → Actions
   ```
3. Click **New repository secret**
4. Add:
   ```
   Name: ANTHROPIC_API_KEY
   Value: <key provided by Infra>
   ```

Once this secret is added, the Claude review workflow can consume it automatically.

### 3. Install the Claude Code GitHub App

The automated review workflow relies on the **Claude Code GitHub App** to read pull requests and post review comments.

* This app must be installed on the repository (or org-wide)
* Installation is typically handled by **Infra Support**

Install link:

* [https://github.com/apps/claude](https://github.com/apps/claude)

Without this app, the workflow will fail with a `401 Unauthorized` error.

---

## One-command setup

Run this command **from inside your project repository**:

```bash
curl -fsSL \
  https://raw.githubusercontent.com/ColoredCow/engineering-recipes/main/automated-code-review/setup.sh \
  | bash
```

### What this command does

* Creates a setup branch: `chore/enable-claude-code-review`
* Adds the Claude review workflow
* Adds default (generic) review guidelines
* Commits and pushes the changes

---

## Next steps (manual, required)

### 1. Open the Pull Request

Open a PR from:

```
chore/enable-claude-code-review → develop (or main)
```


### 2. Trigger a review

On any Pull Request:

1. Add the label:

   ```
   Ready For Review
   ```
2. Wait ~30–60 seconds
3. Claude will post a review comment on the PR

You can re-trigger a review by removing and re-adding the label.


## Notes

* Reviews are **comment-only**
* Merges are **not blocked**
* Review runs only when the label is added
* Teams can customize `docs/code-review-guidelines.md`
