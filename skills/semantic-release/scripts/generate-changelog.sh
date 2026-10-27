#!/usr/bin/env bash
# generate-changelog.sh - Extracts commits and compiles a structured CHANGELOG snippet
set -euo pipefail

NEW_TAG="${1:-v1.0.0}"
DATE=$(date +"%Y-%m-%d")
PREV_TAG=$(git describe --tags --abbrev=0 2>/dev/null || echo "")

echo "Generating changelog for: $NEW_TAG ($DATE)"

if [ -n "$PREV_TAG" ]; then
  RANGE="$PREV_TAG..HEAD"
else
  RANGE="HEAD"
fi

echo "## [$NEW_TAG] - $DATE"
echo ""

# Features
FEATS=$(git log $RANGE --grep="^feat" --format="- %s (%h)" 2>/dev/null || true)
if [ -n "$FEATS" ]; then
  echo "### ✨ Features"
  echo "$FEATS"
  echo ""
fi

# Bug Fixes
FIXES=$(git log $RANGE --grep="^fix" --format="- %s (%h)" 2>/dev/null || true)
if [ -n "$FIXES" ]; then
  echo "### 🐛 Bug Fixes"
  echo "$FIXES"
  echo ""
fi

# Performance & Refactoring
PERF=$(git log $RANGE --grep="^\(perf\|refactor\)" --format="- %s (%h)" 2>/dev/null || true)
if [ -n "$PERF" ]; then
  echo "### ⚡ Performance & Refactoring"
  echo "$PERF"
  echo ""
fi

# Documentation & Maintenance
CHORES=$(git log $RANGE --grep="^\(docs\|chore\|ci\)" --format="- %s (%h)" 2>/dev/null || true)
if [ -n "$CHORES" ]; then
  echo "### 🔧 Maintenance & Documentation"
  echo "$CHORES"
  echo ""
fi
