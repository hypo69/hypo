```python
import pytest

# The user-provided code goes here.  
#  (This is missing from the prompt.  I'll assume a function for testing)
def calculate_sum(a, b):
    """Calculates the sum of two numbers."""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both inputs must be numeric.")
    return a + b

def test_calculate_sum_valid_input():
    """Tests calculate_sum with valid integer inputs."""
    result = calculate_sum(5, 3)
    assert result == 8

def test_calculate_sum_valid_float_input():
    """Tests calculate_sum with valid float inputs."""
    result = calculate_sum(5.5, 3.2)
    assert result == 8.7


def test_calculate_sum_zero_input():
    """Tests calculate_sum with zero input."""
    result = calculate_sum(0, 0)
    assert result == 0

def test_calculate_sum_negative_input():
    """Tests calculate_sum with negative inputs."""
    result = calculate_sum(-5, 3)
    assert result == -2

def test_calculate_sum_invalid_input_type():
    """Tests calculate_sum with an invalid input type."""
    with pytest.raises(TypeError) as excinfo:
        calculate_sum(5, "a")
    assert "Both inputs must be numeric." in str(excinfo.value)

def test_calculate_sum_invalid_input_type_second_argument():
  """Tests calculate_sum with an invalid input type (second argument)."""
  with pytest.raises(TypeError) as excinfo:
      calculate_sum("a", 5)
  assert "Both inputs must be numeric." in str(excinfo.value)


```