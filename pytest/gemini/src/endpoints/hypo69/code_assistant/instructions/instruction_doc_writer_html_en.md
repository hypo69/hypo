```python
import pytest

# Example function (replace with your actual code)
def calculate_average(numbers: list[int]) -> float:
    """
    Calculates the average of a list of numbers.

    Args:
        numbers (list[int]): A list of integers.

    Returns:
        float: The average of the numbers in the list. Returns 0 if the list is empty.

    Raises:
        TypeError: if input is not a list of integers.
    """
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list.")
    if not all(isinstance(num, int) for num in numbers):
        raise TypeError("All elements in the list must be integers.")

    if not numbers:
        return 0.0
    return sum(numbers) / len(numbers)



# Tests for calculate_average function
def test_calculate_average_valid_input():
    """Checks correct behavior with a valid list of integers."""
    numbers = [1, 2, 3, 4, 5]
    expected_average = 3.0
    assert calculate_average(numbers) == expected_average

def test_calculate_average_empty_list():
    """Checks the function's behavior with an empty list."""
    numbers = []
    assert calculate_average(numbers) == 0.0

def test_calculate_average_mixed_types():
    """Tests the error handling for a list with mixed types."""
    numbers = [1, 2, "a"]
    with pytest.raises(TypeError):
        calculate_average(numbers)


def test_calculate_average_non_list_input():
    """Tests error handling for non-list input."""
    with pytest.raises(TypeError):
        calculate_average(123)

def test_calculate_average_non_integer_input():
    """Tests error handling for non-integer input."""
    numbers = [1, 2, "a"]
    with pytest.raises(TypeError):
        calculate_average(numbers)

```