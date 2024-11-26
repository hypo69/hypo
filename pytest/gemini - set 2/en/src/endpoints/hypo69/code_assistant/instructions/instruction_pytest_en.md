```python
import pytest
import math

def calculate_area(length, width):
    """Calculates the area of a rectangle."""
    if length <= 0 or width <= 0:
        raise ValueError("Length and width must be positive values.")
    return length * width

def calculate_circle_area(radius):
    """Calculates the area of a circle."""
    if radius <= 0:
        raise ValueError("Radius must be a positive value.")
    return math.pi * radius**2


# Tests for calculate_area
def test_calculate_area_valid_input():
    """Tests calculate_area with valid positive inputs."""
    assert calculate_area(5, 10) == 50
    assert calculate_area(2.5, 7.2) == 18.0
    

def test_calculate_area_zero_input():
    """Tests calculate_area with zero length or width."""
    with pytest.raises(ValueError):
        calculate_area(0, 10)
    with pytest.raises(ValueError):
        calculate_area(5, 0)


def test_calculate_area_negative_input():
    """Tests calculate_area with negative length or width."""
    with pytest.raises(ValueError):
        calculate_area(-5, 10)
    with pytest.raises(ValueError):
        calculate_area(5, -10)

# Tests for calculate_circle_area
def test_calculate_circle_area_valid_input():
    """Tests calculate_circle_area with valid positive inputs."""
    assert calculate_circle_area(5) == pytest.approx(78.53981633974483)  # Using pytest.approx for floating-point comparisons
    assert calculate_circle_area(10) == pytest.approx(314.1592653589793)


def test_calculate_circle_area_zero_radius():
    """Tests calculate_circle_area with zero radius."""
    with pytest.raises(ValueError):
        calculate_circle_area(0)


def test_calculate_circle_area_negative_radius():
    """Tests calculate_circle_area with negative radius."""
    with pytest.raises(ValueError):
        calculate_circle_area(-5)


```

**Explanation and Improvements:**

1. **Clear Test Names:**  Test names are now more descriptive (e.g., `test_calculate_area_valid_input`).

2. **pytest.raises:** Used correctly to test for `ValueError` exceptions, crucial for robust error handling.

3. **Edge Cases:**  Added tests for zero and negative inputs to thoroughly test the `ValueError` handling.

4. **Floating-Point Comparisons:** The `calculate_circle_area` tests now use `pytest.approx()` when comparing floating-point results.  This is essential because floating-point calculations can sometimes have slight inaccuracies.

5. **Comprehensive Coverage:** The tests now cover various valid inputs (positive numbers, decimals) and clearly demonstrate the desired exception behavior for invalid inputs.

6. **Docstrings:** Docstrings for the tests provide context and explanation of the test's purpose.

**How to run the tests:**

1.  Save the above code as a Python file (e.g., `test_calculations.py`).
2.  Make sure you have pytest installed (`pip install pytest`).
3.  Run the tests from your terminal using: `pytest test_calculations.py`

This improved solution provides a much more thorough set of tests that validate both the expected outputs and the error handling. Remember to replace the example functions with the actual functions from your provided code. Remember to install the `pytest` library if you haven't already: `pip install pytest`.  This updated example provides a template for writing robust `pytest` tests for any function that might raise exceptions. Remember to tailor the test cases to the specific behavior of the functions you're testing.