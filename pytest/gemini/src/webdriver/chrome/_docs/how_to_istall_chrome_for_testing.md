```python
import pytest


# Since the provided code is empty,  we'll create example functions for testing.
# Replace these with your actual code.


def add_numbers(a, b):
    """Adds two numbers."""
    return a + b


def divide_numbers(a, b):
    """Divides two numbers.  Raises ZeroDivisionError if b is zero."""
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b


def greet(name):
    """Greets the person by name."""
    if not isinstance(name, str):
        raise TypeError("Name must be a string")
    return f"Hello, {name}!"



# Tests for add_numbers
def test_add_numbers_positive():
    """Tests addition with positive numbers."""
    assert add_numbers(2, 3) == 5


def test_add_numbers_negative():
    """Tests addition with negative numbers."""
    assert add_numbers(-2, -3) == -5


def test_add_numbers_zero():
    """Tests addition with zero."""
    assert add_numbers(0, 5) == 5


# Tests for divide_numbers
def test_divide_numbers_positive():
    """Tests division with positive numbers."""
    assert divide_numbers(10, 2) == 5.0


def test_divide_numbers_negative():
    """Tests division with negative numbers."""
    assert divide_numbers(-10, 2) == -5.0


def test_divide_numbers_zero_numerator():
    """Tests division with zero numerator."""
    assert divide_numbers(0, 5) == 0.0


def test_divide_numbers_zero_divisor_raises_exception():
    """Tests for ZeroDivisionError when dividing by zero."""
    with pytest.raises(ZeroDivisionError, match="Cannot divide by zero"):
        divide_numbers(10, 0)


# Tests for greet
def test_greet_valid_name():
    """Tests greeting with a valid name."""
    assert greet("Alice") == "Hello, Alice!"


def test_greet_invalid_input():
    """Tests handling of non-string input."""
    with pytest.raises(TypeError, match="Name must be a string"):
        greet(123)


```