---
name: semantic-release
description: >-
  Use this skill when the user asks to manage software releases, determine version numbers
  following SemVer (Semantic Versioning), validate Conventional Commits, generate CHANGELOGs,
  or automate release tagging and GitHub Releases.
version: 1.0.0
author: Divay Sharma
category: developer-workflows
compatibility:
  antigravity: ">=1.0"
  claude-code: ">=1.0"
  cursor: ">=0.40"
  openai-agents: "universal"
tags:
  - release
  - semver
  - conventional-commits
  - changelog
  - versioning
  - git-tag
---

# Semantic Release & Versioning

A deterministic release skill for calculating semantic version bumps, validating Conventional Commits, compiling automated changelogs, and managing version release workflows.

## When to Activate

Trigger this skill when:
- The user asks: "What should the next version number be?"
- The user wants to generate or update `CHANGELOG.md` from git commit history.
- The user wants to validate commit messages against Conventional Commits specs.
- The user is preparing a production release tag (`git tag -a vX.Y.Z`).
- The user wants to set up automated CI release workflows.

Do NOT activate when:
- The task is simply resolving git merge conflicts (use `git-workflow` instead).
- The user is doing general code reviews (use `pr-reviewer` instead).

---

## Semantic Versioning (SemVer 2.0.0) Rules

Given a version number `MAJOR.MINOR.PATCH`:

1. **`MAJOR` (e.g. 1.0.0 -> 2.0.0)**:
   - Incremented when making incompatible API changes or breaking changes.
   - Conventional Commit trigger: `BREAKING CHANGE:` in footer or `!` after type (e.g., `feat!: remove deprecated v1 API`).
2. **`MINOR` (e.g. 1.0.0 -> 1.1.0)**:
   - Incremented when adding functionality in a backward-compatible manner.
   - Conventional Commit trigger: `feat: add export to CSV option`.
3. **`PATCH` (e.g. 1.0.0 -> 1.0.1)**:
   - Incremented when making backward-compatible bug fixes.
   - Conventional Commit trigger: `fix: handle null pointer in auth middleware`.
4. Non-bumping types (typically do not bump public version unless configured):
   - `docs:`, `style:`, `refactor:`, `perf:`, `test:`, `build:`, `ci:`, `chore:`.

---

## Step-by-Step Release Workflow

### Step 1: Validate Recent Commit Messages
Run the validator to ensure commits conform to standard format:
```bash
bash ./scripts/validate-commit-msg.sh
```

### Step 2: Determine Next Version
1. Identify the latest git tag: `git describe --tags --abbrev=0 2>/dev/null || echo "v0.0.0"`
2. Inspect all commits since that tag:
   ```bash
   git log $(git describe --tags --abbrev=0)..HEAD --oneline
   ```
3. Evaluate highest precedence bump:
   - Any `BREAKING CHANGE` or `!` -> **MAJOR**
   - Any `feat:` -> **MINOR**
   - Any `fix:` -> **PATCH**

### Step 3: Generate Changelog Entry
Execute the changelog generator script:
```bash
bash ./scripts/generate-changelog.sh v1.1.0
```

### Step 4: Tag & Publish
```bash
# 1. Update version files (e.g. package.json, pyproject.toml)
# 2. Commit release
git add CHANGELOG.md package.json
git commit -m "chore(release): v1.1.0 [skip ci]"

# 3. Create annotated Git tag
git tag -a v1.1.0 -m "Release v1.1.0"

# 4. Push branch and tag
git push origin main --tags
```

---

## Helper Scripts & References

- Commit validator: `bash ./scripts/validate-commit-msg.sh`
- Changelog generator: `bash ./scripts/generate-changelog.sh <version>`
- [Conventional Commits Specification Guide](./references/conventional-commits.md)
- [Release Workflow Example](./examples/release-workflow.md)
