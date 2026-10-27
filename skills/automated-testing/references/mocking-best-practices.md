# Mocking Best Practices & Guidelines

Mocks isolate code under test from slow, unpredictable, or external dependencies. Used incorrectly, however, mocks can give a false sense of security or make refactoring painful.

## Rules of Thumb for Mocking

1. **Only Mock at System Boundaries**:
   - ✅ Mock: External HTTP APIs (Stripe, Twilio, GitHub API), emails/SMS providers, system clock, payment gateways.
   - ❌ Don't Mock: Your own domain entities, pure helper functions, standard libraries (math, string formatting).

2. **Prefer Fakes over Heavy Mocks**:
   - An in-memory repository (e.g. `InMemoryUserRepository` storing to a Map) is often simpler, more realistic, and less brittle than configuring 10 lines of `mock.onGet().reply(200)` assertions.

3. **Verify State over Interactions**:
   - Prefer: `expect(order.status).toBe('CANCELLED')`
   - Avoid: `expect(mockOrderDb.updateStatus).toHaveBeenCalledWith('CANCELLED')` unless tracking an external side-effect (like sending an email).

4. **Always Reset Mocks Between Tests**:
   - Vitest/Jest: `beforeEach(() => { vi.clearAllMocks(); });`
   - Pytest: Use function-scoped fixtures rather than module-scoped mutable mocks.
