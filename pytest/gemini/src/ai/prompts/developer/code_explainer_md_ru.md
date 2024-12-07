```python
import pytest

# The user-provided code goes here
# (Assuming the code to be explained is a placeholder)
def add_numbers(a, b):
    """Adds two numbers."""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Inputs must be numbers.")
    return a + b


def test_add_numbers_valid_input():
    """Tests adding two positive integers."""
    assert add_numbers(5, 3) == 8


def test_add_numbers_valid_input_float():
    """Tests adding two floats."""
    assert add_numbers(2.5, 3.5) == 6.0

def test_add_numbers_zero():
    """Tests adding zero to a number."""
    assert add_numbers(5, 0) == 5
    assert add_numbers(0, 5) == 5


def test_add_numbers_negative():
    """Tests adding negative numbers."""
    assert add_numbers(-5, 3) == -2
    assert add_numbers(5, -3) == 2


def test_add_numbers_invalid_input():
    """Tests handling of non-numeric input."""
    with pytest.raises(TypeError):
        add_numbers("hello", 5)
    with pytest.raises(TypeError):
        add_numbers(5, "world")


def test_add_numbers_mixed_type():
  """Tests handling of mixed types."""
  with pytest.raises(TypeError):
        add_numbers(5, "hello")

```