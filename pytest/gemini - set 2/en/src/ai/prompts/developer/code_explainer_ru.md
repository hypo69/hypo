```python
import pytest

# Example functions (replace with your actual code)
def calculate_sum(a, b):
    """Calculates the sum of two numbers."""
    return a + b

def subtract_numbers(a, b):
    """Subtracts two numbers."""
    return a - b

def divide_numbers(a, b):
    """Divides two numbers. Raises ZeroDivisionError if b is zero."""
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b


# Tests for calculate_sum
def test_calculate_sum_positive_numbers():
    """Tests calculate_sum with positive numbers."""
    assert calculate_sum(5, 3) == 8

def test_calculate_sum_negative_numbers():
    """Tests calculate_sum with negative numbers."""
    assert calculate_sum(-5, -3) == -8


def test_calculate_sum_zero():
    """Tests calculate_sum with zero."""
    assert calculate_sum(0, 5) == 5
    assert calculate_sum(5, 0) == 5
    assert calculate_sum(0, 0) == 0

def test_calculate_sum_float():
    """Tests calculate_sum with float inputs."""
    assert calculate_sum(2.5, 3.5) == 6.0

# Tests for subtract_numbers
def test_subtract_numbers_positive():
    assert subtract_numbers(10, 5) == 5

def test_subtract_numbers_negative():
    assert subtract_numbers(-5, 3) == -8

def test_subtract_numbers_zero():
    assert subtract_numbers(0, 5) == -5


# Tests for divide_numbers
def test_divide_numbers_positive():
    assert divide_numbers(10, 2) == 5.0

def test_divide_numbers_negative():
    assert divide_numbers(-10, 2) == -5.0


def test_divide_numbers_zero_divisor():
    with pytest.raises(ZeroDivisionError, match="Cannot divide by zero"):
        divide_numbers(10, 0)


#Tests for edge cases
def test_calculate_sum_large_numbers():
    """Tests with large numbers to ensure no integer overflow."""
    assert calculate_sum(9223372036854775807, 1) == 9223372036854775808  #Use very large numbers

```