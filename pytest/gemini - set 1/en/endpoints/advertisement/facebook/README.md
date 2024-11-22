```python
import pytest

def add_numbers(a, b):
    """Adds two numbers together.

    Args:
        a: The first number.
        b: The second number.

    Returns:
        The sum of a and b.
        Raises TypeError if inputs are not numbers.
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Inputs must be numbers.")
    return a + b

def subtract_numbers(a, b):
    """Subtracts b from a.

    Args:
        a: The minuend.
        b: The subtrahend.

    Returns:
        The difference between a and b.
        Raises TypeError if inputs are not numbers.
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Inputs must be numbers.")
    return a - b

# Tests for add_numbers
def test_add_numbers_valid_input():
    """Tests addition with valid integer inputs."""
    assert add_numbers(5, 3) == 8

def test_add_numbers_valid_float_input():
    """Tests addition with valid float inputs."""
    assert add_numbers(2.5, 3.5) == 6.0

def test_add_numbers_zero_input():
    """Tests addition with zero inputs."""
    assert add_numbers(0, 0) == 0

def test_add_numbers_negative_input():
    """Tests addition with negative inputs."""
    assert add_numbers(-5, 3) == -2

def test_add_numbers_invalid_input_type():
    """Tests for TypeError when input is not a number."""
    with pytest.raises(TypeError):
        add_numbers("a", 5)

def test_add_numbers_invalid_input_type2():
    """Tests for TypeError with second input not a number."""
    with pytest.raises(TypeError):
        add_numbers(5, "b")


# Tests for subtract_numbers
def test_subtract_numbers_valid_input():
    """Tests subtraction with valid integer inputs."""
    assert subtract_numbers(10, 5) == 5

def test_subtract_numbers_zero_input():
   """Tests subtraction with zero inputs."""
   assert subtract_numbers(0, 0) == 0

def test_subtract_numbers_negative_input():
   """Tests subtraction with negative inputs."""
   assert subtract_numbers(-2, 5) == -7

def test_subtract_numbers_float_input():
   """Tests subtraction with float inputs."""
   assert subtract_numbers(10.5, 2.5) == 8.0

def test_subtract_numbers_invalid_input_type():
    """Tests for TypeError when input is not a number."""
    with pytest.raises(TypeError):
        subtract_numbers("a", 5)

def test_subtract_numbers_invalid_input_type2():
    """Tests for TypeError with second input not a number."""
    with pytest.raises(TypeError):
        subtract_numbers(5, "b")
```