```python
import pytest

#  No code provided to test, so creating dummy functions for demonstration.
def add_numbers(a, b):
    """Adds two numbers."""
    return a + b

def divide_numbers(a, b):
    """Divides two numbers. Raises ZeroDivisionError if b is zero."""
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b

def greet(name):
  """Greets the person with their name"""
  if not name:
    raise ValueError("Name cannot be empty")
  return f"Hello, {name}!"

# Tests for add_numbers
def test_add_numbers_positive():
    """Tests addition with positive integers."""
    assert add_numbers(5, 3) == 8

def test_add_numbers_negative():
    """Tests addition with negative integers."""
    assert add_numbers(-5, -3) == -8

def test_add_numbers_zero():
    """Tests addition with zero."""
    assert add_numbers(5, 0) == 5

# Tests for divide_numbers
def test_divide_numbers_positive():
    """Tests division with positive integers."""
    assert divide_numbers(10, 2) == 5.0

def test_divide_numbers_negative():
    """Tests division with negative integers."""
    assert divide_numbers(-10, 2) == -5.0

def test_divide_numbers_zero_numerator():
    """Tests division with zero numerator."""
    assert divide_numbers(0, 5) == 0.0

def test_divide_numbers_zero_denominator():
    """Tests division by zero."""
    with pytest.raises(ZeroDivisionError, match="Cannot divide by zero"):
        divide_numbers(10, 0)

# Tests for greet
def test_greet_valid_name():
  """Tests greeting with a valid name."""
  assert greet("Alice") == "Hello, Alice!"


def test_greet_empty_name():
  """Tests greeting with an empty name."""
  with pytest.raises(ValueError, match="Name cannot be empty"):
    greet("")


# This is a crucial step for more complex tests.
# It ensures that the functions are used as intended by the developer.
# The functions are now fully tested, but this example demonstrates
# the essential structure of a well-written test suite.
```