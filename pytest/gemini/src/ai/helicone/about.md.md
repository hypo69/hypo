```python
import pytest

# This is a markdown document, so there's no code to test.
# The following tests are examples of how tests could be written if there were code.
# We'll create some mock functions to use as examples.

# Mock function example 1
def add_numbers(a, b):
    """
    Mock function to simulate adding two numbers
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
      raise TypeError("Inputs must be numbers.")
    return a + b

# Mock function example 2
def divide_numbers(a, b):
    """
    Mock function to simulate division of two numbers
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
      raise TypeError("Inputs must be numbers.")
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def test_add_numbers_valid_input():
    """
    Checks correct behavior of add_numbers with valid input
    """
    assert add_numbers(5, 3) == 8
    assert add_numbers(-1, 1) == 0
    assert add_numbers(2.5, 2.5) == 5.0

def test_add_numbers_invalid_input():
    """
    Checks correct handling of invalid input for add_numbers
    """
    with pytest.raises(TypeError):
      add_numbers("a", 1)
    with pytest.raises(TypeError):
      add_numbers(1, "b")
    with pytest.raises(TypeError):
        add_numbers(None, 1)

def test_divide_numbers_valid_input():
    """
    Checks correct behavior of divide_numbers with valid input
    """
    assert divide_numbers(10, 2) == 5
    assert divide_numbers(5, 2) == 2.5
    assert divide_numbers(0, 5) == 0

def test_divide_numbers_invalid_input():
    """
    Checks correct handling of invalid input for divide_numbers
    """
    with pytest.raises(ValueError):
        divide_numbers(10, 0)

    with pytest.raises(TypeError):
        divide_numbers("a", 1)
    
    with pytest.raises(TypeError):
        divide_numbers(1, "b")

    with pytest.raises(TypeError):
        divide_numbers(None, 1)
```