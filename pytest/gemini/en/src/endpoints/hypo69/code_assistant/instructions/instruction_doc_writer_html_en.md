```python
import pytest

# Placeholder for the actual Python code.  Replace with the input code.
#  The example below is a placeholder.

def greet(name: str, greeting: str = "Hello") -> str:
    """
    Args:
        name (str): The name to greet.
        greeting (str, optional): The greeting message. Defaults to "Hello".

    Returns:
        str: The greeting message with the name.

    Raises:
        TypeError: If name is not a string.
    """
    if not isinstance(name, str):
        raise TypeError("Name must be a string.")
    return f"{greeting}, {name}!"

def add(x: int, y: int) -> int:
    """
    Args:
        x (int): The first number.
        y (int): The second number.

    Returns:
        int: The sum of x and y.
    """
    return x + y

# Tests for the greet function
def test_greet_valid_name():
    """Checks the greet function with a valid name."""
    assert greet("Alice") == "Hello, Alice!"
    assert greet("Bob", greeting="Hi") == "Hi, Bob!"


def test_greet_invalid_name():
    """Tests the greet function with an invalid name (not a string)."""
    with pytest.raises(TypeError):
        greet(123)


# Tests for the add function
def test_add_positive_numbers():
    """Tests add function with positive numbers."""
    assert add(2, 3) == 5
    assert add(10, 5) == 15

def test_add_zero():
    """Tests add function with zero."""
    assert add(0, 5) == 5
    assert add(5,0) == 5


# Test with a negative number
def test_add_negative_numbers():
    """Tests add function with negative numbers."""
    assert add(-2, -3) == -5

# Example of edge case test
def test_add_large_numbers():
    """Tests add function with very large numbers."""
    assert add(1000000, 2000000) == 3000000
```