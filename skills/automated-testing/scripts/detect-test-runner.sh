#!/usr/bin/env bash
# detect-test-runner.sh - Inspects repo files to auto-detect test framework and execution command
set -euo pipefail

echo "=================================================="
echo "          TEST RUNNER AUTO-DETECTION              "
echo "=================================================="

DETECTED=false

# 1. Node.js / JavaScript / TypeScript
if [ -f "package.json" ]; then
  if grep -q '"vitest"' package.json; then
    echo "Framework: Vitest (Node/TypeScript)"
    echo "Command  : npx vitest run"
    DETECTED=true
  elif grep -q '"jest"' package.json; then
    echo "Framework: Jest (Node/JavaScript)"
    echo "Command  : npx jest"
    DETECTED=true
  elif grep -q '"test"' package.json; then
    echo "Framework: Node npm test script"
    echo "Command  : npm test"
    DETECTED=true
  fi
fi

# 2. Python
if [ -f "pyproject.toml" ] || [ -f "pytest.ini" ] || [ -f "setup.py" ] || [ -f "requirements.txt" ]; then
  echo "Framework: Pytest (Python)"
  echo "Command  : pytest"
  DETECTED=true
fi

# 3. Go
if [ -f "go.mod" ]; then
  echo "Framework: Go standard testing"
  echo "Command  : go test -v ./..."
  DETECTED=true
fi

# 4. Rust
if [ -f "Cargo.toml" ]; then
  echo "Framework: Cargo test (Rust)"
  echo "Command  : cargo test"
  DETECTED=true
fi

if [ "$DETECTED" = false ]; then
  echo "No recognized test framework detected in current directory."
  echo "Tip: Verify you are running this from your project root."
fi
echo "=================================================="
