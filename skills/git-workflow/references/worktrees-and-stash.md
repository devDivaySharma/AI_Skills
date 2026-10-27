# Git Worktrees and Advanced Stashing

## Git Worktrees: Parallel Checkouts Without Re-cloning

Git worktrees allow you to check out multiple branches of the same repository simultaneously in separate directories on disk.

### Benefits
- **Zero context switching delay**: No need to stash uncommitted files or switch branches.
- **Shared `.git` object database**: Uses negligible additional disk space compared to a full second clone.
- **Ideal for hotfixes & code reviews**: Keep your feature branch active while testing another branch in a parallel worktree.

### Common Commands
```bash
# List all active worktrees
git worktree list

# Add a new worktree for branch 'bugfix/urgent' in sibling directory
git worktree add ../repo-bugfix bugfix/urgent

# Add a worktree with a newly created branch based on main
git worktree add -b feature/experiment ../repo-experiment main

# Delete / clean up a worktree when finished
git worktree remove ../repo-bugfix
```

---

## Named Stashes: Preventing Mystery Stashes

Default `git stash` produces nameless entries like `stash@{0}: WIP on main...` which are hard to distinguish after days.

### Best Practice
```bash
# Always label stashes descriptively
git stash push -m "2026-10-27: auth-modal halfway through OAuth implementation"

# List stashes with messages
git stash list

# Inspect what is inside a stash before applying
git stash show -p stash@{0}

# Apply without dropping (safe preview)
git stash apply stash@{0}

# Drop only once verified
git stash drop stash@{0}
```
