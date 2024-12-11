```python
import pytest

# Example code (replace with your actual code)
from src.utils.calculator import calculate_sum


def add_numbers(a, b):
    result = calculate_sum(a, b)
    return result


def test_add_numbers_valid_input():
    """Tests add_numbers with valid integer inputs."""
    assert add_numbers(2, 3) == 5
    assert add_numbers(-1, 1) == 0
    assert add_numbers(0, 0) == 0


def test_add_numbers_valid_float_input():
    """Tests add_numbers with valid float inputs."""
    assert add_numbers(2.5, 3.5) == 6.0
    assert add_numbers(-1.5, 1.5) == 0.0


def test_add_numbers_invalid_input_type():
    """Tests add_numbers with non-numeric inputs (raises TypeError)."""
    with pytest.raises(TypeError):
        add_numbers("a", 2)
    with pytest.raises(TypeError):
        add_numbers(2, "b")
    with pytest.raises(TypeError):
        add_numbers("a", "b")


def test_add_numbers_large_numbers():
    """Tests add_numbers with very large numbers (potentially overflow)."""
    #  This assumes calculate_sum handles large numbers appropriately.
    large_number = 10**10
    result = add_numbers(large_number, 1)
    assert result == large_number + 1


# Add more test cases based on the expected behavior
# of 'calculate_sum' and the 'add_numbers' function,
# including:
# - negative numbers
# - boundary cases (minimum and maximum possible numbers)
# - edge cases (e.g., a very large positive number + a very large negative number).
# Remember to check how calculate_sum handles exceptional cases


```