```python
import pytest

# The user-provided code goes here (replace with your actual code)
def calculate_sum(a, b):
    """Calculates the sum of two numbers."""
    return a + b

def add_numbers(a, b):
    """Adds two numbers using the calculate_sum function."""
    result = calculate_sum(a, b)
    return result

# Tests for calculate_sum
def test_calculate_sum_positive_integers():
    """Tests calculate_sum with positive integers."""
    assert calculate_sum(2, 3) == 5
    assert calculate_sum(10, 20) == 30

def test_calculate_sum_negative_integers():
    """Tests calculate_sum with negative integers."""
    assert calculate_sum(-2, -3) == -5
    assert calculate_sum(-10, -20) == -30

def test_calculate_sum_zero():
    """Tests calculate_sum with zero."""
    assert calculate_sum(0, 0) == 0
    assert calculate_sum(5, 0) == 5
    assert calculate_sum(0, -5) == -5
    
def test_calculate_sum_mixed_signs():
    """Tests calculate_sum with mixed signs."""
    assert calculate_sum(5, -3) == 2
    assert calculate_sum(-5, 3) == -2

def test_calculate_sum_large_numbers():
    """Tests calculate_sum with large numbers."""
    assert calculate_sum(100000, 200000) == 300000

def test_calculate_sum_float():
    """Tests calculate_sum with float numbers."""
    assert calculate_sum(2.5, 3.5) == 6.0
    assert calculate_sum(-2.5, -3.5) == -6.0

def test_calculate_sum_float_integer():
  """Tests calculate_sum with float and integer"""
  assert calculate_sum(2.5, 3) == 5.5


# Tests for add_numbers
def test_add_numbers_positive_integers():
    """Tests add_numbers with positive integers."""
    assert add_numbers(2, 3) == 5

def test_add_numbers_negative_integers():
    """Tests add_numbers with negative integers."""
    assert add_numbers(-2, -3) == -5

def test_add_numbers_zero():
    """Tests add_numbers with zero."""
    assert add_numbers(0, 0) == 0
    assert add_numbers(5, 0) == 5
    assert add_numbers(0, -5) == -5

def test_add_numbers_mixed_signs():
    """Tests add_numbers with mixed signs."""
    assert add_numbers(5, -3) == 2
    assert add_numbers(-5, 3) == -2
    assert add_numbers(-5, 2) == -3

def test_add_numbers_large_numbers():
    """Tests add_numbers with large numbers."""
    assert add_numbers(100000, 200000) == 300000

def test_add_numbers_float():
    """Tests add_numbers with float numbers."""
    assert add_numbers(2.5, 3.5) == 6.0

# Example of testing for exceptions.  Replace with relevant exceptions for your code
def test_calculate_sum_invalid_input():
    with pytest.raises(TypeError):  #Example, Replace with specific exception
        calculate_sum("a", 5)

def test_add_numbers_invalid_input():
    with pytest.raises(TypeError): #Example, Replace with specific exception
        add_numbers("a", 5)
```