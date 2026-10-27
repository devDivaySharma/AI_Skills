---
name: pr-reviewer
description: >-
  Use this skill when the user asks to review a pull request, analyze code diffs,
  audit changes for security/performance flaws, evaluate architectural consistency,
  or prepare structured, actionable code review comments.
version: 1.0.0
author: Divay Sharma
category: developer-workflows
compatibility:
  antigravity: ">=1.0"
  claude-code: ">=1.0"
  cursor: ">=0.40"
  openai-agents: "universal"
tags:
  - code-review
  - pr
  - pull-request
  - quality
  - security
  - diff-analysis
---

# Pull Request Reviewer

An expert code review skill for evaluating pull requests and diffs systematically. Produces concise, constructive, prioritised feedback across correctness, security, performance, test coverage, and design clarity.

## When to Activate

Trigger this skill when:
- The user asks to "review my PR", "audit this diff", or "inspect changes against main".
- The user wants a pre-commit or pre-merge architectural and safety check.
- The user asks for feedback on whether a branch is ready to merge.
- The user wants automated formatting of PR comments (nit, suggestion, blocking issue).

Do NOT activate when:
- The user simply wants to run tests (use `automated-testing` instead).
- The user is resolving merge conflicts (use `git-workflow` instead).

---

## Review Methodology: The 5-Pillar Audit

Evaluate all changes against five structured dimensions:

1. **Correctness & Logic**:
   - Does the implementation fulfill the intended requirements?
   - Are edge cases handled (null/undefined, zero-length arrays, network timeouts, race conditions)?
2. **Security & Vulnerabilities**:
   - Are inputs sanitized/validated at boundary layers?
   - Any secret leaks, SQLi, XSS, CSRF, or insecure deserialization?
   - Are authorization and authentication checks enforced before data access?
3. **Performance & Scalability**:
   - Any N+1 query patterns, unintentional $O(n^2)$ loops, or memory leaks?
   - Are resources (database connections, file handles, streams) released reliably?
4. **Testability & Coverage**:
   - Are there unit tests for new logic and edge cases?
   - Do existing tests still pass, or were tests silenced/deleted?
5. **Maintainability & Idiomatic Style**:
   - Is naming self-descriptive and domain-accurate?
   - Does it adhere to existing codebase architectural conventions?

---

## Feedback Formatting Standard

Categorize every review observation using standard tags:

- **`[BLOCKER]`**: Critical bug, data loss risk, or security vulnerability that must be fixed before merge.
- **`[WARNING]`**: Likely bug, performance bottleneck, or missing test case for an edge case.
- **`[SUGGESTION]`**: Clean code improvement, refactoring opportunity, or idiomatic modernization.
- **`[NIT]`**: Minor formatting, typo in comments/docs, or aesthetic preference (non-blocking).
- **`[PRAISE]`**: Recognition for well-designed abstractions, clean tests, or elegant solutions.

Each feedback comment should specify:
1. **File and Line Number**: e.g., `src/services/billing.ts:L45-L52`
2. **Issue**: What is wrong or risky.
3. **Impact**: Why it matters.
4. **Suggested Code Fix**: Provide a concrete drop-in snippet.

---

## Step-by-Step Execution

### Step 1: Extract Diff & Context
```bash
# Analyze diff against base branch (e.g., origin/main or origin/master)
bash ./scripts/pr-diff-analyze.sh main
```

### Step 2: Audit Checklist
Run through the items in [Review Checklist](./references/review-checklist.md) and [Security Anti-Patterns](./references/security-anti-patterns.md).

### Step 3: Compile Report
Present a summary table with:
- **Verdict**: (Approve / Request Changes / Comment)
- **Summary**: 2-sentence executive overview.
- **Findings by Severity**: Blockers, Warnings, Suggestions, Nits.
- **Recommended Action Items**.

---

## Resources & Examples

- Helper: `bash ./scripts/pr-diff-analyze.sh <base-branch>`
- [Comprehensive Review Checklist](./references/review-checklist.md)
- [Common Security Anti-Patterns](./references/security-anti-patterns.md)
- [Example PR Review Report](./examples/sample-pr-review.md)
