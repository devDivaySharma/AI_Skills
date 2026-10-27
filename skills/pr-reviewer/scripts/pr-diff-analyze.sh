#!/usr/bin/env bash
# pr-diff-analyze.sh - Extracts and summarizes git diff stats against a target branch
set -euo pipefail

TARGET_BRANCH="${1:-main}"

# Check if target branch exists locally or remotely
if git show-ref --verify --quiet "refs/heads/$TARGET_BRANCH"; then
  BASE="$TARGET_BRANCH"
elif git show-ref --verify --quiet "refs/remotes/origin/$TARGET_BRANCH"; then
  BASE="origin/$TARGET_BRANCH"
elif git show-ref --verify --quiet "refs/heads/master"; then
  BASE="master"
elif git show-ref --verify --quiet "refs/remotes/origin/master"; then
  BASE="origin/master"
else
  echo "Target base branch not found. Falling back to HEAD~1"
  BASE="HEAD~1"
fi

echo "=================================================="
echo "          PULL REQUEST DIFF ANALYSIS             "
echo "=================================================="
echo "Base Reference : $BASE"
echo "Current HEAD   : $(git rev-parse --short HEAD)"
echo "--------------------------------------------------"

echo "Modified Files Summary:"
git diff --stat "$BASE"...HEAD

echo "--------------------------------------------------"
TOTAL_FILES=$(git diff --name-only "$BASE"...HEAD | wc -l | tr -d ' ')
INSERTIONS=$(git diff --shortstat "$BASE"...HEAD | grep -oE '[0-9]+ insertion' | cut -d' ' -f1 || echo "0")
DELETIONS=$(git diff --shortstat "$BASE"...HEAD | grep -oE '[0-9]+ deletion' | cut -d' ' -f1 || echo "0")

echo "Total Files Changed: $TOTAL_FILES"
echo "Insertions (+): ${INSERTIONS:-0}"
echo "Deletions  (-): ${DELETIONS:-0}"

echo "--------------------------------------------------"
echo "Sensitive files touched (if any):"
git diff --name-only "$BASE"...HEAD | grep -E '(\.env|secret|config|credentials|auth|security|docker-compose|package\.json|go\.mod|Cargo\.toml)' || echo "No sensitive config files modified."
echo "=================================================="
