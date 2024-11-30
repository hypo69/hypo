```python
import pytest

# Since there's no provided code, I'm creating example functions and tests.
# Replace these with the actual code from hypotez/src/endpoints/hypo69/code_assistant/instructions/readme.md

def add_numbers(x, y):
    """Adds two numbers together."""
    return x + y

def divide_numbers(x, y):
    """Divides two numbers.  Raises ZeroDivisionError if y is zero."""
    if y == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return x / y


# Tests for add_numbers function
def test_add_numbers_positive():
    """Tests addition with positive integers."""
    assert add_numbers(5, 3) == 8

def test_add_numbers_negative():
    """Tests addition with negative integers."""
    assert add_numbers(-5, -3) == -8

def test_add_numbers_zero():
    """Tests addition with zero."""
    assert add_numbers(0, 5) == 5

# Tests for divide_numbers function
def test_divide_numbers_positive():
    """Tests division with positive integers."""
    assert divide_numbers(10, 2) == 5.0

def test_divide_numbers_negative():
    """Tests division with negative and positive integers."""
    assert divide_numbers(-10, 2) == -5.0

def test_divide_numbers_zero_numerator():
    """Tests division with zero numerator."""
    assert divide_numbers(0, 5) == 0.0

def test_divide_numbers_zero_denominator():
  """Tests division with zero denominator, expecting ZeroDivisionError."""
  with pytest.raises(ZeroDivisionError, match="Cannot divide by zero"):
      divide_numbers(10, 0)


def test_divide_numbers_float():
    """Tests division with float inputs."""
    assert divide_numbers(10.5, 3) == 3.5
```