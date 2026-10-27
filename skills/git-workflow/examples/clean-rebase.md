# Example: End-to-End Clean Rebase Walkthrough

This scenario shows a developer updating `feature/user-profiles` with the latest changes from `origin/main`, resolving a conflict in `src/models/user.ts`, and squashing trivial commits before PR submission.

## Scenario Timeline

1. Fetch latest upstream changes:
   ```bash
   git fetch origin
   ```

2. Rebase on top of upstream:
   ```bash
   git checkout feature/user-profiles
   git rebase origin/main
   ```

3. Conflict encountered:
   ```text
   CONFLICT (content): Merge conflict in src/models/user.ts
   error: could not apply a1b2c3d... feat(user): add avatar url
   hint: Resolve all conflicts manually, mark them as resolved with
   hint: "git add/rm <conflicted_files>", then run "git rebase --continue".
   ```

4. Examine conflict in `src/models/user.ts`:
   ```typescript
   <<<<<<< HEAD
   export interface User {
     id: string;
     email: string;
     role: 'admin' | 'member';
   }
   =======
   export interface User {
     id: string;
     email: string;
     avatarUrl?: string;
   }
   >>>>>>> a1b2c3d (feat(user): add avatar url)
   ```

5. Resolved file:
   ```typescript
   export interface User {
     id: string;
     email: string;
     role: 'admin' | 'member';
     avatarUrl?: string;
   }
   ```

6. Stage and proceed:
   ```bash
   git add src/models/user.ts
   git rebase --continue
   ```

7. Interactive squash of temporary commits:
   ```bash
   git rebase -i HEAD~3
   ```
   Select `pick` for the primary feature commit, and `fixup` for "typo fix" commits.

8. Result: Clean, single atomic commit on top of main, verified with `git log -n 2 --stat`.
