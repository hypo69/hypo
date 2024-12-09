```python
import pytest

# Replace with the actual Python code you want to test.  
# This example is a placeholder.

def calculate_sum(numbers: list[int]) -> int:
    """
    Calculates the sum of a list of numbers.

    Args:
        numbers (list[int]): A list of integers.

    Returns:
        int: The sum of the numbers in the list.

    Raises:
        TypeError: If input is not a list of integers.
    """
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list.")
    if not all(isinstance(num, int) for num in numbers):
        raise TypeError("All elements in the list must be integers.")

    total = 0
    for number in numbers:
        total += number
    return total


def greet(name: str, greeting: str = "Hello") -> str:
    """
    Greets the person by name.

    Args:
        name (str): The name of the person to greet.
        greeting (str, optional): The greeting to use. Defaults to "Hello".

    Returns:
        str: The greeting message.
    """
    return f"{greeting}, {name}!"


# Test cases for calculate_sum
def test_calculate_sum_valid_input():
    """Tests calculate_sum with a valid list of integers."""
    numbers = [1, 2, 3, 4, 5]
    expected_sum = 15
    assert calculate_sum(numbers) == expected_sum


def test_calculate_sum_empty_list():
    """Tests calculate_sum with an empty list."""
    numbers = []
    expected_sum = 0
    assert calculate_sum(numbers) == expected_sum


def test_calculate_sum_with_negative_numbers():
    """Tests calculate_sum with negative numbers."""
    numbers = [-1, -2, -3]
    expected_sum = -6
    assert calculate_sum(numbers) == expected_sum


def test_calculate_sum_invalid_input_not_list():
    """Tests calculate_sum with invalid input (not a list)."""
    with pytest.raises(TypeError) as exinfo:
        calculate_sum(123)
    assert "Input must be a list." in str(exinfo.value)


def test_calculate_sum_invalid_input_not_int():
    """Tests calculate_sum with invalid input (not all integers)."""
    with pytest.raises(TypeError) as exinfo:
        calculate_sum([1, 2, 'a'])
    assert "All elements in the list must be integers." in str(exinfo.value)




# Test cases for greet
def test_greet_valid_input():
    """Tests greet with a valid name."""
    name = "Alice"
    expected_greeting = "Hello, Alice!"
    assert greet(name) == expected_greeting


def test_greet_custom_greeting():
    """Tests greet with a custom greeting."""
    name = "Bob"
    greeting = "Hi"
    expected_greeting = "Hi, Bob!"
    assert greet(name, greeting) == expected_greeting


```