# Example: Standard PR Review Output

### PR Review: Add JWT Refresh Token Rotation

**Verdict**: `Request Changes` (1 Blocker, 1 Warning, 1 Praise)

---

### Executive Summary
This PR implements refresh token rotation for authentication. The core cryptographic generation and token storage look solid, but there is an unhandled token reuse attack vulnerability and a missing expiration index on the database table.

---

### Detailed Findings

#### 1. [BLOCKER] Unhandled Token Reuse Attack
- **File**: `src/auth/token_service.py:L78-L92`
- **Issue**: If a stolen refresh token is used after it has already been rotated, the system currently only returns an unauthorized error without revoking the downstream compromised family of tokens.
- **Impact**: Attacker can hijack sessions if they race the legitimate user.
- **Suggested Fix**:
  ```python
  if token.is_used:
      # Suspected token theft: Revoke all refresh tokens for this user session immediately
      await self.revoke_token_family(token.family_id)
      raise SecurityCompromiseException("Suspicious token reuse detected; session revoked.")
  ```

#### 2. [WARNING] Missing Database Index on `expires_at`
- **File**: `migrations/004_create_refresh_tokens.sql:L12`
- **Issue**: Periodic cleanup worker executes `DELETE FROM refresh_tokens WHERE expires_at < NOW()`, but `expires_at` is not indexed.
- **Impact**: Full table scan on every cleanup run; will degrade DB throughput as table scales.
- **Suggested Fix**:
  ```sql
  CREATE INDEX idx_refresh_tokens_expires_at ON refresh_tokens (expires_at);
  ```

#### 3. [PRAISE] Clean Unit Tests & Fixtures
- **File**: `tests/auth/test_token_rotation.py`
- **Comment**: Excellent test coverage with mock time clocks (`freezegun`). Clean separation of expired token cases versus active token cases.

---

### Recommendation
Address the token family revocation and add the migration index. Once resolved, this will be ready to approve!
