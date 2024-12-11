```python
import pytest
import sys

# Example Code (Replace with the actual code)
def add_numbers(a, b):
    """Adds two numbers."""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Inputs must be numbers.")
    return a + b


def subtract_numbers(a, b):
    """Subtracts two numbers."""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Inputs must be numbers.")
    return a - b


# Tests for add_numbers function
def test_add_numbers_valid_input():
    """Tests add_numbers with valid integer inputs."""
    assert add_numbers(5, 3) == 8
    assert add_numbers(10, -2) == 8


def test_add_numbers_valid_float_input():
    """Tests add_numbers with valid float inputs."""
    assert add_numbers(3.14, 2.71) == 5.85


def test_add_numbers_invalid_input():
    """Tests add_numbers with invalid input (not a number)."""
    with pytest.raises(TypeError):
        add_numbers("hello", 5)  # Example of string input
    with pytest.raises(TypeError):
        add_numbers(5, "world")  # Example of string input
    with pytest.raises(TypeError):
        add_numbers(5, True) #Example of boolean input
    with pytest.raises(TypeError):
        add_numbers(True, 5)  # Example of boolean input

def test_add_numbers_zero_input():
  """Tests add_numbers with zero input."""
  assert add_numbers(0, 0) == 0
  assert add_numbers(5, 0) == 5

# Tests for subtract_numbers function
def test_subtract_numbers_valid_input():
    """Tests subtract_numbers with valid integer inputs."""
    assert subtract_numbers(5, 3) == 2
    assert subtract_numbers(10, -2) == 12


def test_subtract_numbers_valid_float_input():
    """Tests subtract_numbers with valid float inputs."""
    assert subtract_numbers(3.14, 2.71) == 0.43


def test_subtract_numbers_invalid_input():
    """Tests subtract_numbers with invalid input (not a number)."""
    with pytest.raises(TypeError):
        subtract_numbers("hello", 5)  # Example of string input
    with pytest.raises(TypeError):
        subtract_numbers(5, "world")  # Example of string input
    with pytest.raises(TypeError):
      subtract_numbers(5, True) #Example of boolean input
    with pytest.raises(TypeError):
      subtract_numbers(True, 5)  # Example of boolean input

```