#!/usr/bin/env bash
# validate-commit-msg.sh - Validates git commit messages against Conventional Commits spec
set -euo pipefail

REGEX="^(feat|fix|docs|style|refactor|perf|test|build|ci|chore|revert)(\([a-z0-9_\-]+\))?!?: .+$"

echo "=================================================="
echo "      CONVENTIONAL COMMITS VALIDATION             "
echo "=================================================="

# Check commits on current branch relative to origin/main or HEAD~5
BASE=$(git describe --tags --abbrev=0 2>/dev/null || echo "HEAD~5")
if ! git rev-parse "$BASE" >/dev/null 2>&1; then
  BASE="HEAD~1"
fi

COMMITS=$(git log "$BASE"..HEAD --oneline 2>/dev/null || git log -n 5 --oneline)

if [ -z "$COMMITS" ]; then
  echo "No new commits to validate."
  exit 0
fi

FAILED=0
TOTAL=0

while IFS= read -r line; do
  TOTAL=$((TOTAL + 1))
  HASH=$(echo "$line" | cut -d' ' -f1)
  MSG=$(echo "$line" | cut -d' ' -f2-)

  if echo "$MSG" | grep -qE "$REGEX"; then
    echo "✅ PASS: [$HASH] $MSG"
  else
    echo "❌ FAIL: [$HASH] $MSG"
    echo "   -> Expected format: <type>(<scope>): <summary>"
    FAILED=$((FAILED + 1))
  fi
done <<< "$COMMITS"

echo "--------------------------------------------------"
echo "Total commits checked: $TOTAL"
if [ "$FAILED" -gt 0 ]; then
  echo "Validation failed with $FAILED non-compliant commit message(s)."
  exit 1
else
  echo "All inspected commits adhere to Conventional Commits!"
fi
echo "=================================================="
