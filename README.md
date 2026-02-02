# Claude GitHub PR Agent

Automated code review for GitHub pull requests using Claude AI.

## Overview

This project integrates Anthropic's Claude Code into your GitHub workflow to automatically review pull requests. When a PR is opened or updated, Claude analyzes the code changes against your project's coding standards and provides feedback as PR comments.

## How It Works

```
┌─────────────────┐     ┌──────────────────┐     ┌─────────────────┐
│  PR Opened or   │────▶│  GitHub Actions  │────▶│  Claude Code    │
│  Updated        │     │  Triggers        │     │  Reviews Code   │
└─────────────────┘     └──────────────────┘     └────────┬────────┘
                                                          │
                                                          ▼
                                                ┌─────────────────┐
                                                │  Review Posted  │
                                                │  as PR Comment  │
                                                └─────────────────┘
```

1. **Trigger**: A pull request is opened, synchronized, or reopened
2. **Action**: GitHub Actions runs the `anthropics/claude-code-action@v1`
3. **Review**: Claude analyzes changes against guidelines in `CLAUDE.md`
4. **Feedback**: Review results are posted as comments on the PR

## Setup

### 1. Get Claude Code OAuth Token

You need an OAuth token from Anthropic to authenticate Claude Code.

1. Visit the [Anthropic Console](https://console.anthropic.com/)
2. Generate an OAuth token for Claude Code
3. Copy the token for the next step

### 2. Add GitHub Secret

1. Go to your repository on GitHub
2. Navigate to **Settings** → **Secrets and variables** → **Actions**
3. Click **New repository secret**
4. Name: `CLAUDE_CODE_OAUTH_TOKEN`
5. Value: Paste your OAuth token
6. Click **Add secret**

### 3. Copy Workflow File

The workflow file is located at `.github/workflows/claude-code-review.yml`. If you're using this as a template for another project, copy this file to your repository.

### 4. Customize Review Guidelines (Optional)

Edit `CLAUDE.md` to define your project's coding standards. Claude uses this file to understand what to check during reviews.

## Testing the Integration

### Method 1: Create a Test Branch

```bash
# Create a new branch
git checkout -b test-review

# Make some code changes
echo "def bad_function():" >> test.py
echo "    pass" >> test.py

# Commit and push
git add test.py
git commit -m "test: add test file for review"
git push origin test-review
```

Then create a pull request from `test-review` to your main branch on GitHub.

### Method 2: Use the Example File

This repository includes `example.py` as a test case:

```bash
# Switch to the test branch
git checkout test-python-review

# Create a PR to main (if not already created)
gh pr create --title "Test: Python code review" --body "Testing Claude code review"
```

### Method 3: Modify Existing Code

1. Create a branch from main
2. Make intentional code quality issues (missing type hints, security issues, etc.)
3. Push and create a PR
4. Watch the Actions tab for the review workflow
5. Check PR comments for Claude's feedback

## Workflow Configuration

The workflow file (`.github/workflows/claude-code-review.yml`) supports several customization options:

### Filter by File Type

Uncomment the `paths` section to only review specific file types:

```yaml
on:
  pull_request:
    paths:
      - "**.py"
      - "**.ts"
      - "**.js"
```

### Filter by Author

Review only external contributors:

```yaml
- uses: anthropics/claude-code-action@v1
  if: github.event.pull_request.author_association != 'MEMBER'
```

## Project Structure

```
claude-github-pr-agent/
├── .github/
│   └── workflows/
│       └── claude-code-review.yml  # GitHub Actions workflow
├── CLAUDE.md                        # Code review guidelines
├── example.py                       # Example Python code for testing
└── README.md                        # This file
```

## Code Review Guidelines

The `CLAUDE.md` file defines what Claude checks during reviews:

- **Code Style**: PEP 8, naming conventions, line length
- **Type Hints**: Required for all functions
- **Documentation**: Docstrings for public APIs
- **Security**: Input validation, no hardcoded secrets, safe practices
- **Error Handling**: Specific exceptions, graceful failures
- **Testing**: Coverage requirements

## Troubleshooting

### Workflow Not Triggering

- Verify the workflow file is in `.github/workflows/`
- Check that GitHub Actions is enabled for your repository
- Ensure the PR event type matches the workflow triggers

### Authentication Errors

- Verify `CLAUDE_CODE_OAUTH_TOKEN` secret is set correctly
- Check the token hasn't expired
- Ensure the token has appropriate permissions

### No Review Comments

- Check the Actions tab for workflow run logs
- Verify the workflow completed successfully
- Look for errors in the Claude Code action step

## Requirements

- GitHub repository with Actions enabled
- Anthropic Claude Code OAuth token
- Pull request workflow permissions (read contents, read/write PRs)

## License

MIT
