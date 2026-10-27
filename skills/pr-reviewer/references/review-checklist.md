# Comprehensive Code Review Checklist

Use this checklist during every pull request inspection.

## 1. Logic & Functionality
- [ ] Requirements: Does this change solve the issue or implement the specification?
- [ ] Boundary conditions: Are empty collections, zero values, negative numbers, and max limits handled?
- [ ] Error handling: Are exceptions caught specifically rather than swallowed silently?
- [ ] Concurrency: Are shared states protected against race conditions?

## 2. Security
- [ ] Input Validation: Are all external/user parameters validated before processing?
- [ ] Secrets: Are API keys, passwords, or tokens excluded from commits?
- [ ] SQL Injection: Are parameterized queries or ORM safe-builders used exclusively?
- [ ] Authorization: Is permission verified before returning or modifying resources?
- [ ] Dependencies: Are any newly introduced packages vetted, secure, and maintained?

## 3. Performance & Resource Management
- [ ] Algorithmic efficiency: Are nested iterations over large datasets avoided?
- [ ] Database queries: Are queries indexed? Is the N+1 query problem avoided?
- [ ] Clean up: Are connections, file descriptors, and intervals closed in `finally` / defer blocks?
- [ ] Memory: Are large payloads or streams buffered appropriately?

## 4. Testing
- [ ] Unit tests: Are new functions and classes accompanied by focused unit tests?
- [ ] Regression tests: If fixing a bug, is there a test that reproduces the bug and verifies the fix?
- [ ] Mocking: Are network calls, databases, and clocks mocked cleanly in unit tests?
- [ ] Flakiness: Are tests deterministic without hardcoded `sleep` calls?

## 5. Architecture & Documentation
- [ ] Single Responsibility: Does each module, function, or class have one clear purpose?
- [ ] Public API documentation: Are exported methods, REST endpoints, or RPC interfaces documented?
- [ ] Backward compatibility: Are breaking API changes avoided or properly versioned?
