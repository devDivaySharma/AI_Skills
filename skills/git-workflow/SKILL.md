---
name: git-workflow
description: >-
  Use this skill when the user asks to manage Git repositories, resolve merge conflicts,
  perform interactive rebases, manage branches, handle worktrees, create atomic commits,
  or safely recover lost commits using reflog.
version: 1.0.0
author: Divay Sharma
category: developer-workflows
compatibility:
  antigravity: ">=1.0"
  claude-code: ">=1.0"
  cursor: ">=0.40"
  openai-agents: "universal"
tags:
  - git
  - vcs
  - version-control
  - rebase
  - merge-conflicts
---

# Git Workflow

A comprehensive guide for safe, professional, and deterministic Git workflows. Enforces clean commit history, atomic commits, conflict resolution without data loss, and advanced tools (rebase, worktree, bisect, reflog).

## When to Activate

Trigger this skill when:
- The user asks to rebase, merge, cherry-pick, or sync branches.
- The user has encountered merge conflicts or detached HEAD state.
- The user wants atomic commits following Conventional Commits format.
- The user asks to recover lost commits or reset mistakes via `git reflog`.
- The user wants to work across multiple branches simultaneously using `git worktree`.
- The user asks to isolate a bug using `git bisect`.

Do NOT activate when:
- The task is simply checking `git status` without further workflow actions.
- The user is creating a GitHub release (use `semantic-release` instead).

---

## Safety Principles (Zero Data Loss)

1. **Check Working State Before Mutating**:
   Always run `git status` and `git diff --stat` before branch switches, rebases, or resets.
2. **Never Stash Blindly**:
   If uncommitted work exists, either create a temporary commit (`git commit -m "wip: save state"`) or name your stash explicitly (`git stash push -m "feature-backup-2026-10-27"`).
3. **Reflog as Safety Net**:
   Before any forced operation or hard reset, note `git rev-parse HEAD`. You can always restore to that SHA via `git reset --hard <sha>` if needed.
4. **Interactive Rebases**:
   Never rebase public/shared branches that other team members are actively tracking. Only rebase local feature branches.

---

## Core Workflows

### 1. Preparing Clean Feature Branches
```bash
# 1. Fetch latest remote state
git fetch origin

# 2. Rebase feature branch on top of main/master
git checkout feature/my-feature
git rebase origin/main

# 3. If conflicts arise, examine the conflicted files
git status
```

### 2. Conflict Resolution Protocol
1. Identify conflicting files marked with `both modified:`.
2. Inspect markers:
   - `<<<<<<< HEAD` (current branch changes)
   - `=======` (separator)
   - `>>>>>>> <branch-or-commit>` (incoming changes)
3. Edit the file to integrate both sets of changes cleanly without losing intent.
4. Run tests or linter to ensure syntax and tests pass.
5. Stage the resolved files: `git add <file>`.
6. Continue rebase/merge: `git rebase --continue` (or `git merge --continue`).
7. **Never** use `git rebase --skip` unless you deliberately intend to discard the entire commit.

### 3. Atomic Conventional Commits
Structure each commit to represent one logical change:
```bash
# Format: <type>(<scope>): <short imperative summary>
# Types: feat, fix, docs, style, refactor, perf, test, build, ci, chore
git commit -m "feat(auth): add OAuth2 refresh token rotation"
git commit -m "fix(api): handle timeout when upstream service is unreachable"
git commit -m "test(cart): add edge cases for expired coupon codes"
```

### 4. Git Worktrees for Parallel Branch Contexts
Instead of stashing or cloning multiple times, use Git Worktrees:
```bash
# Create a parallel workspace for a hotfix while keeping feature work intact
git worktree add ../project-hotfix main
cd ../project-hotfix
# Perform fix, commit, and push
# Remove worktree when done
cd -
git worktree remove ../project-hotfix
```

### 5. Git Bisect for Automated Regression Hunting
```bash
git bisect start
git bisect bad                 # Current commit is broken
git bisect good v1.2.0         # v1.2.0 was known good
# Git checks out intermediate commits. Test each:
git bisect run npm test        # Fully automated bisect run
git bisect reset               # Return to original HEAD
```

---

## Helper Scripts & References

- Run inspection helper: `bash ./scripts/git-summary.sh`
- [Rebase & Merge Strategies](./references/rebase-and-merge.md)
- [Worktrees & Stash Best Practices](./references/worktrees-and-stash.md)
- [Example: Clean Rebase Walkthrough](./examples/clean-rebase.md)
