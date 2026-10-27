# Git Rebase vs. Merge: Decision Framework & Best Practices

## When to Rebase vs. When to Merge

| Scenario | Recommended Strategy | Reason |
| :--- | :--- | :--- |
| **Updating a local feature branch with `main`** | `git rebase origin/main` | Maintains a linear history; eliminates redundant "Merge branch 'main' into feature" commits. |
| **Completing a feature branch into `main` (team repo)** | Squash & Merge (or PR merge) | Packages the feature as a concise, discrete unit on `main`. |
| **Collaborative branch with multiple active contributors** | `git merge origin/feature` | Avoids rewriting commit history that other developers have pulled. |
| **Cleaning up WIP commits before PR review** | `git rebase -i HEAD~N` | Squashes "wip", "typo", and temporary commits into coherent atomic commits. |

## Interactive Rebase Cheatsheet

Run:
```bash
git rebase -i HEAD~4
```

Commands available in the editor:
- `p, pick <commit>`: Use commit as-is.
- `r, reword <commit>`: Use commit, but edit commit message.
- `e, edit <commit>`: Pause rebase to amend files or split commit.
- `s, squash <commit>`: Meld commit into previous commit; combine commit messages.
- `f, fixup <commit>`: Like squash, but discard this commit's log message.
- `d, drop <commit>`: Remove commit entirely.

## Abort & Recovery

If a rebase becomes tangled or confused:
```bash
# Abort cleanly and return to exact state prior to rebase:
git rebase --abort

# If you accidentally ran --skip or completed with errors:
git reflog
# Find the commit before the rebase started (e.g. HEAD@{5})
git reset --hard HEAD@{5}
```
