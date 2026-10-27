# Examples: Unit & Integration Test Patterns

### Pattern 1: TypeScript / Vitest Unit Test with AAA Pattern

```typescript
import { describe, it, expect, beforeEach, vi } from 'vitest';
import { DiscountCalculator } from './discount_calculator';

describe('DiscountCalculator', () => {
  let calculator: DiscountCalculator;

  beforeEach(() => {
    calculator = new DiscountCalculator();
  });

  it('applies 10% discount for orders exceeding 100 dollars', () => {
    // Arrange
    const cartTotal = 150.0;
    const isVip = false;

    // Act
    const finalPrice = calculator.compute(cartTotal, isVip);

    // Assert
    expect(finalPrice).toBe(135.0);
  });

  it('throws an error when cart total is negative', () => {
    // Arrange & Act & Assert
    expect(() => calculator.compute(-10, false)).toThrow('Cart total cannot be negative');
  });
});
```

---

### Pattern 2: Python / Pytest Integration Test with Database Fixture

```python
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from myapp.models import Base, User
from myapp.repositories import UserRepository

@pytest.fixture(scope="function")
def db_session():
    # Ephemeral SQLite in-memory DB for isolated integration testing
    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    try:
        yield session
    finally:
        session.close()

def test_user_repository_creates_and_queries_user(db_session):
    # Arrange
    repo = UserRepository(db_session)

    # Act
    created = repo.create_user(email="alice@example.com", name="Alice")
    fetched = repo.find_by_email("alice@example.com")

    # Assert
    assert fetched is not None
    assert fetched.id == created.id
    assert fetched.name == "Alice"
```
