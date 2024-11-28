```python
import pytest

def add_numbers(x, y):
    """Adds two numbers."""
    return x + y

def subtract_numbers(x, y):
    """Subtracts two numbers."""
    return x - y

def divide_numbers(x, y):
    """Divides two numbers."""
    if y == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return x / y


# Tests for add_numbers function
def test_add_numbers_positive():
    """Tests add_numbers with positive integers."""
    assert add_numbers(5, 3) == 8

def test_add_numbers_negative():
    """Tests add_numbers with negative integers."""
    assert add_numbers(-5, -3) == -8
    
def test_add_numbers_zero():
    """Tests add_numbers with zero."""
    assert add_numbers(5, 0) == 5
    
def test_add_numbers_float():
    """Tests add_numbers with floats."""
    assert add_numbers(2.5, 3.5) == 6.0
    
def test_add_numbers_mixed():
    """Tests add_numbers with mixed types."""
    assert add_numbers(2, 3.5) == 5.5


# Tests for subtract_numbers function
def test_subtract_numbers_positive():
    """Tests subtract_numbers with positive integers."""
    assert subtract_numbers(5, 3) == 2

def test_subtract_numbers_negative():
    """Tests subtract_numbers with negative integers."""
    assert subtract_numbers(-5, -3) == -2
    
def test_subtract_numbers_zero():
    """Tests subtract_numbers with zero."""
    assert subtract_numbers(5, 0) == 5
    
def test_subtract_numbers_float():
    """Tests subtract_numbers with floats."""
    assert subtract_numbers(2.5, 3.5) == -1.0
    
def test_subtract_numbers_mixed():
    """Tests subtract_numbers with mixed types."""
    assert subtract_numbers(2, 3.5) == -1.5


# Tests for divide_numbers function
def test_divide_numbers_positive():
    """Tests divide_numbers with positive integers."""
    assert divide_numbers(10, 2) == 5.0

def test_divide_numbers_negative():
    """Tests divide_numbers with negative integers."""
    assert divide_numbers(-10, 2) == -5.0

def test_divide_numbers_zero_denominator():
    """Tests divide_numbers with zero denominator."""
    with pytest.raises(ZeroDivisionError, match="Cannot divide by zero"):
        divide_numbers(10, 0)

def test_divide_numbers_float():
    """Tests divide_numbers with floats."""
    assert divide_numbers(10.5, 2.1) == 5.0

def test_divide_numbers_mixed():
    """Tests divide_numbers with mixed types."""
    assert divide_numbers(10, 2.0) == 5.0

```