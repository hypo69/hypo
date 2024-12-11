```python
import pytest

# Input code (Assuming this is the code to be tested)
def calculate_sum(a, b):
    """Calculates the sum of two numbers."""
    try:
        return a + b
    except TypeError:
        return "Invalid input types"

def add_numbers(a, b):
    """Adds two numbers using the calculate_sum function."""
    result = calculate_sum(a, b)
    return result


# Tests for calculate_sum
def test_calculate_sum_valid_integers():
    """Tests calculate_sum with valid integer inputs."""
    assert calculate_sum(5, 3) == 8

def test_calculate_sum_valid_floats():
    """Tests calculate_sum with valid float inputs."""
    assert calculate_sum(5.5, 3.2) == 8.7


def test_calculate_sum_invalid_input_type():
    """Tests calculate_sum with invalid input types."""
    assert calculate_sum(5, "a") == "Invalid input types"

#Tests for add_numbers
def test_add_numbers_valid_integers():
    """Tests add_numbers with valid integer inputs."""
    assert add_numbers(5, 3) == 8


def test_add_numbers_valid_floats():
    """Tests add_numbers with valid float inputs."""
    assert add_numbers(5.5, 3.2) == 8.7

def test_add_numbers_invalid_input_type():
    """Tests add_numbers with invalid input types."""
    assert add_numbers(5, "a") == "Invalid input types"

def test_add_numbers_zero_inputs():
    """Tests add_numbers with zero inputs."""
    assert add_numbers(0,0) == 0

def test_calculate_sum_large_numbers():
    """Tests calculate_sum with large numbers."""
    assert calculate_sum(1000000, 2000000) == 3000000
```