**Prompt for Writing `pytest` Tests**

Write test cases for the following Python code using the `pytest` library. The tests should cover the main functions, methods, or classes to verify their correctness. Include edge cases and exception handling where appropriate.

**Requirements:**
1. Use clear and descriptive test function names that indicate their purpose.
2. Ensure all tests are isolated and independent of one another.
3. Consider various scenarios, including:
   - Valid inputs.
   - Invalid or unexpected inputs, where applicable.
   - Edge or boundary cases.
4. Use `pytest.raises` for exception testing.
5. If fixtures are needed for the functions, define them separately.
6. Add comments explaining the logic of the test cases.

Example structure for the tests:

```python
import pytest

# Fixture definitions, if needed
@pytest.fixture
def example_data():
    """Provides test data for the function."""
    return {...}

# Tests for Function 1
def test_function1_valid_input():
    """Checks correct behavior with valid input."""
    ...

def test_function1_invalid_input():
    """Checks correct handling of invalid input."""
    ...

# Tests for Function 2
def test_function2_edge_case():
    """Checks behavior with edge cases."""
    ...
```

Input code:

```python
# The user-provided code goes here
...
```

Create a comprehensive set of test cases based on the given code.