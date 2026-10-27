#!/usr/bin/env bash
# git-summary.sh - High-level summary of local git repository state
set -euo pipefail

echo "=================================================="
echo "               GIT WORKSPACE SUMMARY              "
echo "=================================================="

# Check if inside git repo
if ! git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  echo "Error: Not a git repository."
  exit 1
fi

BRANCH=$(git rev-parse --abbrev-ref HEAD)
COMMIT=$(git rev-parse --short HEAD 2>/dev/null || echo "empty")
STATUS=$(git status --porcelain)
UNTRACKED=$(echo "$STATUS" | grep -c '^??' || true)
STAGED=$(echo "$STATUS" | grep -c '^[MADRC]' || true)
UNSTAGED=$(echo "$STATUS" | grep -c '^.[MADRC]' || true)

echo "Current Branch : $BRANCH"
echo "Current HEAD   : $COMMIT"
echo "Staged Files   : $STAGED"
echo "Unstaged Files : $UNSTAGED"
echo "Untracked Files: $UNTRACKED"
echo "--------------------------------------------------"

if [ -z "$STATUS" ]; then
  echo "Working tree is clean."
else
  echo "Modified / Untracked files:"
  git status -s
fi

echo "--------------------------------------------------"
echo "Recent Commits (last 5):"
git log -n 5 --oneline --decorate 2>/dev/null || echo "No commits yet."
echo "=================================================="
