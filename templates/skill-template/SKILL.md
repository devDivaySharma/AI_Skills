---
name: skill-name
description: >-
  Concise 2-3 sentence description of when and why the agent should activate this skill.
  Must use third-person ("Use this skill when..."). Explain the trigger conditions clearly.
version: 1.0.0
author: Divay Sharma
category: developer-workflows
compatibility:
  antigravity: ">=1.0"
  claude-code: ">=1.0"
  cursor: ">=0.40"
  openai-agents: "universal"
tags:
  - workflow
  - template
---

# Skill Name

High-level overview of what this skill enables the agent to do.

## When to Activate

Trigger this skill when the user asks to:
- Specific trigger 1 (e.g., "Review my pull request")
- Specific trigger 2 (e.g., "Check git status and rebase")
- Specific trigger 3 (e.g., "Generate unit tests")

Do NOT activate when:
- Out-of-scope scenario 1
- Out-of-scope scenario 2

## Step-by-Step Instructions

### Step 1: Pre-checks and Context Gathering
1. Inspect current workspace state and relevant files.
2. Confirm prerequisites before executing destructive actions.

### Step 2: Core Execution
1. Follow standard procedures outlined below.
2. If scripts are provided in `./scripts/`, reference or execute them:
   - `bash ./scripts/helper.sh --arg value`

### Step 3: Verification & Output
1. Verify the result using assertions, tests, or status checks.
2. Format output cleanly for the user with actionable next steps.

## Reference Materials

- [Detailed Guide](./references/guide.md) - In-depth concepts and edge cases
- [Examples](./examples/basic-usage.md) - Reference inputs and outputs
