# The Testing Pyramid & Test Classification

A healthy, maintainable test suite relies on balance across three test layers.

## 1. Unit Tests (Base, ~70% of Suite)
- **Scope**: Single function, method, class, or isolated component.
- **Speed**: Milliseconds per test.
- **Dependencies**: All external dependencies (DB, network, file system) are mocked or injected as stubs.
- **Goal**: Exhaustive verification of business logic, algorithms, calculations, state machines, and edge cases.

## 2. Integration Tests (Middle, ~20% of Suite)
- **Scope**: Two or more subsystems collaborating (e.g., API handler + database repository, cache + data store).
- **Speed**: Tens to hundreds of milliseconds.
- **Dependencies**: Often uses real or containerized local databases (e.g. SQLite, testcontainers) with ephemeral test data.
- **Goal**: Verify SQL queries, serialization/deserialization, transaction boundaries, and interface contracts.

## 3. End-to-End & Smoke Tests (Top, ~10% of Suite)
- **Scope**: Full application stack from entry point (HTTP/browser) to backend storage.
- **Speed**: Seconds per test.
- **Dependencies**: Fully wired live or staging environment.
- **Goal**: Ensure the primary happy paths and critical transactions (login, checkout, signup) work together seamlessly.

---

## Anti-Patterns to Avoid
- **Ice Cream Cone**: Having hundreds of brittle, slow E2E tests and very few unit tests. Leads to slow CI and flaky builds.
- **Testing Implementation Details**: Asserting on private variables or internal method invocation counts instead of final return values.
- **Sleep in Tests**: Using `time.sleep(2)` to wait for async jobs instead of awaiting promises or polling assertions with timeouts.
