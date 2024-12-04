```python
import pytest
import math

def calculate_area(radius):
    """Calculates the area of a circle."""
    if radius < 0:
        raise ValueError("Radius cannot be negative.")
    return math.pi * radius**2

def calculate_volume(radius, height):
    """Calculates the volume of a cylinder."""
    if radius < 0 or height < 0:
        raise ValueError("Radius and height cannot be negative.")
    return math.pi * radius**2 * height

# Tests for calculate_area
def test_calculate_area_positive_radius():
    """Tests calculate_area with a positive radius."""
    radius = 5
    expected_area = math.pi * radius**2
    assert calculate_area(radius) == expected_area

def test_calculate_area_zero_radius():
    """Tests calculate_area with a zero radius."""
    radius = 0
    expected_area = 0
    assert calculate_area(radius) == expected_area
    
def test_calculate_area_negative_radius():
    """Tests calculate_area with a negative radius (exception handling)."""
    with pytest.raises(ValueError) as excinfo:
        calculate_area(-5)
    assert str(excinfo.value) == "Radius cannot be negative."

# Tests for calculate_volume
def test_calculate_volume_positive_input():
    """Tests calculate_volume with positive radius and height."""
    radius = 5
    height = 10
    expected_volume = math.pi * radius**2 * height
    assert calculate_volume(radius, height) == expected_volume

def test_calculate_volume_zero_radius():
    """Tests calculate_volume with zero radius."""
    radius = 0
    height = 10
    expected_volume = 0
    assert calculate_volume(radius, height) == expected_volume


def test_calculate_volume_zero_height():
    """Tests calculate_volume with zero height."""
    radius = 5
    height = 0
    expected_volume = 0
    assert calculate_volume(radius, height) == expected_volume

def test_calculate_volume_negative_radius():
    """Tests calculate_volume with negative radius (exception handling)."""
    with pytest.raises(ValueError) as excinfo:
        calculate_volume(-5, 10)
    assert str(excinfo.value) == "Radius and height cannot be negative."

def test_calculate_volume_negative_height():
    """Tests calculate_volume with negative height (exception handling)."""
    with pytest.raises(ValueError) as excinfo:
        calculate_volume(5, -10)
    assert str(excinfo.value) == "Radius and height cannot be negative."
```

**Explanation and Improvements:**

1. **Clear Test Names:**  Test names clearly indicate the input and expected outcome (e.g., `test_calculate_area_positive_radius`).

2. **Comprehensive Coverage:** Tests cover positive, zero, and negative inputs for both functions, including edge cases (zero radius, zero height).

3. **Exception Handling:** `pytest.raises` is used correctly to check for `ValueError` exceptions when invalid inputs are provided.  Crucially, it now asserts the *specific* error message.

4. **Docstrings:**  Docstrings are added to the test functions to explain the purpose of each test, making the tests more readable and maintainable.


This improved solution demonstrates a complete and thorough testing strategy using pytest for the provided (hypothetical) functions.  Remember to replace the placeholder code (`# The user-provided code goes here`) with the actual code. Remember to install pytest if you haven't already (`pip install pytest`). Then, you can run the tests using `pytest`.