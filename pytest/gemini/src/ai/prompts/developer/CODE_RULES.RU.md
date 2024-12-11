```python
import pytest
from typing import Optional

# The user-provided code goes here
# (Assuming no code is provided, this example demonStartes testing)
def calculate_area(length: int, width: int) -> int:
    """
    Calculates the area of a rectangle.

    :param length: The length of the rectangle.
    :type length: int
    :param width: The width of the rectangle.
    :type width: int
    :returns: The area of the rectangle.
    :rtype: int
    :raises ValueError: If length or width is negative.
    """
    if length < 0 or width < 0:
        raise ValueError("Length and width must be non-negative")
    return length * width


# Fixture definitions (if needed)
# (Example assuming we need a fixture for test data)


@pytest.fixture
def rectangle_data():
    """Provides test data for calculate_area."""
    return [
        (5, 10, 50),  # Valid input
        (0, 0, 0),   # Valid input (zero values)
        (-5, 10, ValueError),  # Invalid input (negative length)
        (5, -10, ValueError),  # Invalid input (negative width)
    ]


# Tests for calculate_area
def test_calculate_area_valid_input(rectangle_data):
    """Checks correct behavior with valid input."""
    for length, width, expected_area in rectangle_data:
        if isinstance(expected_area, int):
            assert calculate_area(length, width) == expected_area
        elif isinstance(expected_area, type): #Checking for exception type
            with pytest.raises(expected_area):
                calculate_area(length, width)


def test_calculate_area_invalid_input(rectangle_data):
    """Checks correct handling of invalid input."""
    for length, width, expected_area in rectangle_data:
        if isinstance(expected_area, type) : #Checking for exception type
           with pytest.raises(expected_area) as excinfo:
               calculate_area(length,width)
           assert str(excinfo.value) == "Length and width must be non-negative"


# Example usage (add more tests as needed)
# test_calculate_area_valid_input()
# test_calculate_area_invalid_input()


```