```python
import pytest
import sys
import io

# Placeholder for the user-provided code.  Replace this with the actual code.
#  This example shows a basic function.
def process_data(input_data: str, operation: str = "default") -> dict | None:
    """
    Args:
        input_data (str): Data to be processed.
        operation (str, optional): Operation to perform. Defaults to "default".

    Returns:
        dict | None: Processed data as a dictionary or None if error.

    Raises:
        TypeError: If input_data is not a string.
        ValueError: If input_data is empty.
    """
    if not isinstance(input_data, str):
        raise TypeError("Input data must be a string")
    if not input_data:
        raise ValueError("Input data cannot be empty")
    
    processed_data = {"input": input_data, "operation": operation}
    return processed_data


def test_process_data_valid_input():
    """Checks correct behavior with valid input."""
    result = process_data("some data", "uppercase")
    assert result == {"input": "some data", "operation": "uppercase"}

def test_process_data_default_operation():
    """Checks correct behavior with default operation."""
    result = process_data("test")
    assert result == {"input": "test", "operation": "default"}


def test_process_data_invalid_input_type():
    """Checks exception handling for invalid input type."""
    with pytest.raises(TypeError):
        process_data(123)

def test_process_data_invalid_input_empty():
    """Checks exception handling for empty input."""
    with pytest.raises(ValueError):
        process_data("")
```