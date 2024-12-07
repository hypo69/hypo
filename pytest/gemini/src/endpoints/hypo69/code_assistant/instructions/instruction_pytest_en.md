```python
import pytest
import math

def calculate_area(radius):
    """Calculates the area of a circle given its radius."""
    if radius < 0:
        raise ValueError("Radius cannot be negative.")
    return math.pi * radius**2

def calculate_volume(radius, height):
    """Calculates the volume of a cylinder given its radius and height."""
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
    """Tests calculate_area with a negative radius (raises ValueError)."""
    with pytest.raises(ValueError):
        calculate_area(-5)

# Tests for calculate_volume
def test_calculate_volume_positive_radius_height():
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
    """Tests calculate_volume with negative radius (raises ValueError)."""
    with pytest.raises(ValueError):
        calculate_volume(-5, 10)

def test_calculate_volume_negative_height():
    """Tests calculate_volume with negative height (raises ValueError)."""
    with pytest.raises(ValueError):
        calculate_volume(5, -10)
```

**Explanation and Improvements:**

1. **Clear Test Names:** The test names clearly indicate the input values and expected behavior.

2. **Comprehensive Coverage:** Tests now cover various scenarios: positive radius, zero radius, negative radius, positive height, zero height, and negative height.

3. **Exception Handling:** `pytest.raises` is used correctly to test the `ValueError` exceptions raised by `calculate_area` and `calculate_volume` when input values are invalid.

4. **Correct Assertions:** Assertions check for the expected output values (areas and volumes) against calculated results.

5. **Edge Cases:** The tests include edge cases like zero radius and zero height, which are crucial for robustness.

6. **Docstrings:**  Docstrings in the tests are improved and descriptive, enhancing readability.

7. **No Unnecessary Fixtures:**  No fixtures were needed for the given functions.


This revised solution is more comprehensive, robust, and better demonstrates the usage of `pytest` for testing Python code, including the correct handling of exceptions.  Remember to save this code as a `.py` file (e.g., `test_calculations.py`) and run `pytest test_calculations.py` from your terminal to execute the tests. This is a  solid example demonstrating best practices for writing `pytest` tests.  If you have more complex functions or classes, the techniques used here can be adapted and expanded. Remember to replace the placeholder comments with the actual code you want to test. Remember to install pytest first: `pip install pytest`