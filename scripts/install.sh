#!/usr/bin/env bash
# install.sh - Quick installation helper for AI_Skills
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"

echo "=================================================="
echo "          AI_Skills Installation Helper           "
echo "=================================================="
echo "Repo Root: $REPO_ROOT"
echo ""

# Ensure python3 is available
if ! command -v python3 >/dev/null 2>&1; then
  echo "Error: python3 is required to run the skill installer."
  exit 1
fi

TARGET="${1:-antigravity-global}"
MODE="${2:---symlink}"

echo "Running sync.py with target: $TARGET"
python3 "$REPO_ROOT/scripts/sync.py" install --target "$TARGET" "$MODE"

echo ""
echo "Installation completed! The skills are now active."
