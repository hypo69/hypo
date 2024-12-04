```python
import pytest

# The user-provided code is missing, so I'm creating a dummy function for testing.
def calculate_sum(a, b):
    """Calculates the sum of two numbers."""
    return a + b

def add_numbers(a, b):
    """Adds two numbers using calculate_sum."""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Inputs must be numeric.")
    result = calculate_sum(a, b)
    return result


def test_add_numbers_valid_input():
    """Tests add_numbers with valid integer input."""
    assert add_numbers(5, 3) == 8
    assert add_numbers(10, -2) == 8
    assert add_numbers(0, 0) == 0

def test_add_numbers_valid_float_input():
    """Tests add_numbers with valid float input."""
    assert add_numbers(5.5, 3.2) == 8.7
    assert add_numbers(-2.5, 3.5) == 1.0

def test_add_numbers_zero_input():
    """Tests add_numbers with zero as input."""
    assert add_numbers(0, 5) == 5
    assert add_numbers(5, 0) == 5
    assert add_numbers(0, 0) == 0


def test_add_numbers_invalid_input():
    """Tests add_numbers with invalid input (non-numeric)."""
    with pytest.raises(TypeError):
        add_numbers("a", 5)  # Raises TypeError
    with pytest.raises(TypeError):
        add_numbers(5, "b")  # Raises TypeError
    with pytest.raises(TypeError):
        add_numbers([1,2,3], 5)
        
def test_add_numbers_large_number():
    """Tests large number to check for overflow or precision issues (if applicable)."""
    # Replace with an appropriate large number based on the expected behaviour
    assert add_numbers(1000000000,1000000000)==2000000000

```