```python
import pytest

# Input code (assuming this is the code to be tested)
def calculate_sum(a, b):
    """Calculates the sum of two numbers."""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Inputs must be numeric.")
    return a + b

def add_numbers(a, b):
    """Adds two numbers using calculate_sum."""
    return calculate_sum(a, b)
```

```python
import pytest

# Tests for calculate_sum
def test_calculate_sum_valid_input():
    """Checks correct behavior with valid input."""
    assert calculate_sum(5, 3) == 8
    assert calculate_sum(10.5, 2.5) == 13.0


def test_calculate_sum_invalid_input():
    """Checks handling of invalid input (non-numeric)."""
    with pytest.raises(TypeError):
        calculate_sum("hello", 5)
    with pytest.raises(TypeError):
        calculate_sum(5, "world")


def test_calculate_sum_zero():
    """Tests for zero input values."""
    assert calculate_sum(0, 0) == 0
    assert calculate_sum(5, 0) == 5
    assert calculate_sum(0, -5) == -5


# Tests for add_numbers
def test_add_numbers_valid_input():
    """Checks correct behavior with valid input."""
    assert add_numbers(5, 3) == 8
    assert add_numbers(10.5, 2.5) == 13.0


def test_add_numbers_invalid_input():
    """Checks handling of invalid input (passed to calculate_sum)."""
    with pytest.raises(TypeError):
        add_numbers("hello", 5)
    with pytest.raises(TypeError):
        add_numbers(5, "world")


def test_add_numbers_zero():
    """Tests with zero input values."""
    assert add_numbers(0, 0) == 0
    assert add_numbers(5, 0) == 5
    assert add_numbers(0, -5) == -5

```