---
name: automated-testing
description: >-
  Use this skill when the user asks to write unit, integration, or end-to-end tests,
  increase test coverage, set up testing harnesses (Jest, Vitest, Pytest, Go testing, Cargo test),
  mock external dependencies, or fix broken/flaky tests.
version: 1.0.0
author: Divay Sharma
category: developer-workflows
compatibility:
  antigravity: ">=1.0"
  claude-code: ">=1.0"
  cursor: ">=0.40"
  openai-agents: "universal"
tags:
  - testing
  - tdd
  - jest
  - vitest
  - pytest
  - go-test
  - unit-testing
  - mocking
---

# Automated Testing

A rigorous automated testing skill for designing high-confidence, resilient test suites across unit, integration, and contract levels. Enforces deterministic execution, comprehensive boundary coverage, and clean mocking without over-coupling.

## When to Activate

Trigger this skill when:
- The user asks to write tests for existing or new code ("add tests for user service").
- The user wants to improve code coverage or identify untested edge cases.
- The user is debugging failing or flaky tests.
- The user asks how to mock network requests, databases, third-party APIs, or system time.
- The user wants to adopt Test-Driven Development (TDD) for a new feature.

Do NOT activate when:
- The task is simply reviewing pull request diffs (use `pr-reviewer` instead).
- The user is resolving git merge conflicts (use `git-workflow` instead).

---

## Testing Principles

1. **Test Behavior, Not Implementation Details**:
   Assert on inputs and observable outputs/side-effects rather than inspecting private state or internal method calls.
2. **Deterministic & Isolated**:
   Each test must run independently in any order without relying on shared mutable state or sleep timers.
3. **The Testing Pyramid**:
   - 70% Unit Tests: Fast, isolated, test pure business logic and edge cases.
   - 20% Integration Tests: Test module interactions, database queries, and boundary adapters.
   - 10% E2E / Smoke Tests: Verify critical user journeys end-to-end.
4. **Arrange-Act-Assert (AAA)**:
   Clearly separate the setup, action, and assertion phases in every test case.

---

## Supported Ecosystems & Auto-Detection

Run the detection script to detect the active test framework in the workspace:
```bash
bash ./scripts/detect-test-runner.sh
```

Supported runners:
- **Node/TS**: `vitest`, `jest`, `mocha`, `node:test`
- **Python**: `pytest`, `unittest`
- **Go**: `go test ./...`
- **Rust**: `cargo test`

---

## Standard TDD Workflow

1. **Write Failing Test (Red)**:
   Draft the test describing the expected behavior and verify that it fails for the expected reason.
2. **Implement Minimal Code (Green)**:
   Write the simplest implementation that makes the test pass.
3. **Refactor**:
   Clean up code design, eliminate duplication, and verify tests remain green.

---

## Edge Case Coverage Matrix

When writing tests for any function or endpoint, verify the following inputs:
- **Null / Undefined / None / Nil**
- **Zero Values & Empty Collections**: `0`, `""`, `[]`, `{}`
- **Boundary Conditions**: Max allowed length, off-by-one indices, negative integers
- **Malformed Inputs**: Invalid email formats, malformed JSON, out-of-range dates
- **Failure States**: Upstream timeouts, network failure, disk write errors

---

## Helper Scripts & References

- Detection helper: `bash ./scripts/detect-test-runner.sh`
- [The Testing Pyramid & Test Types](./references/testing-pyramid.md)
- [Mocking Best Practices & Pitfalls](./references/mocking-best-practices.md)
- [Examples: Unit & Integration Patterns](./examples/unit-and-integration.md)
