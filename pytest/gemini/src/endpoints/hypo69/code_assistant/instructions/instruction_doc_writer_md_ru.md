```python
import pytest
import inspect

# Placeholder for the Python code to be tested.  Replace this with the actual code.
def my_function(param: str, param1: str = None) -> dict:
    """
    Args:
        param (str): Description of parameter 'param'.
        param1 (str, optional): Description of parameter 'param1'. Defaults to None.

    Returns:
        dict: Description of the returned value. Returns a dictionary.

    Raises:
        ValueError: Raised if param is empty.
    """
    if not param:
        raise ValueError("Parameter 'param' cannot be empty")
    result = {'param': param}
    if param1:
        result['param1'] = param1
    return result


def test_my_function_valid_input():
    """Checks correct behavior with valid input."""
    result = my_function("valid_input", "another_input")
    assert result == {'param': 'valid_input', 'param1': 'another_input'}


def test_my_function_empty_param():
    """Checks exception handling for empty input."""
    with pytest.raises(ValueError) as ex:
        my_function("", "test")
    assert str(ex.value) == "Parameter 'param' cannot be empty"



def test_my_function_none_param1():
  """Checks the function with a None value for param1"""
  result = my_function("test_param")
  assert result == {'param': 'test_param'}
```