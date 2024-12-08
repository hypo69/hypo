# Writing pytest Tests

## Overview

This document describes the instructions for writing comprehensive pytest test cases for a given Python code.  The tests should cover various scenarios, including valid inputs, invalid/unexpected inputs, edge cases, and exception handling.  The generated tests should adhere to best practices for pytest, ensuring that each test function is isolated and descriptive.

## Instructions

The prompt outlines the process for writing pytest tests. It includes a detailed set of requirements and a suggested structure.  This structure involves defining test functions that cover different aspects of the code, including valid and invalid inputs, boundary conditions, and handling exceptions.

## Function Structure (Example)

For test cases, the structure should be as follows:

### `test_function_name`

**Description**: Provides a brief description of what the test case is verifying.

**Parameters**: Lists the arguments passed to the function being tested, along with their types and descriptions.

**Expected Output**: Details the expected return value or behavior of the function given the input parameters.

**Test Implementation**: The actual implementation of the test case using pytest assertions.

**Example:**

```python
import pytest

def my_function(input_value):
    """Does something with the input."""
    if input_value < 0:
        raise ValueError("Input must be non-negative.")
    return input_value * 2

def test_my_function_valid_input():
    """Checks the function with a valid positive input."""
    result = my_function(5)
    assert result == 10

def test_my_function_invalid_input():
    """Checks exception handling for negative input."""
    with pytest.raises(ValueError, match="Input must be non-negative."):
        my_function(-5)
```


## Considerations

- **Fixture Definitions:** If the functions under test require data or setup, define fixtures using `@pytest.fixture` to create test data.
- **Edge Cases:** Thoroughly test edge cases (minimum, maximum, boundary values, empty inputs) and unexpected inputs to ensure robustness.
- **Exception Handling:** Use `pytest.raises` to test exception handling capabilities of the functions. Ensure the exception message matches the expected error message.


## Best Practices

- **Descriptive Function Names:** Use descriptive names like `test_my_function_with_valid_input` to understand the test's purpose at a glance.
- **Isolated Tests:** Each test function should be isolated to avoid interference between them.
- **Clear Assertions:** Use assertions to check for the expected outcomes (e.g., `assert result == 10`).
- **Maintainability:** Write maintainable and readable tests.


## Further Steps

To proceed with generating specific test cases, please provide the Python code that you want to test.  The generated documentation will be based on this code and will follow the structure outlined above.