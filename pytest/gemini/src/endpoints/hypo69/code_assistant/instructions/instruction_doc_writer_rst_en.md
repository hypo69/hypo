```python
import pytest

# Placeholder for the Python code to be tested
# Replace this with the actual code you want to test

def function1(param: str, param1: str = None) -> dict:
    """
    Args:
        param (str): Description of the `param` parameter.
        param1 (str, optional): Description of the `param1` parameter. Defaults to None.

    Returns:
        dict: Description of the return value. Returns a dictionary.

    Raises:
        ValueError: Description of the situation in which the ValueError exception is raised.
    """
    if param is None:
        raise ValueError("Param cannot be None")
    result = {"param": param}
    if param1:
        result["param1"] = param1
    return result


def function2(data: list) -> int:
    """
    Args:
        data (list): Description of the data parameter.
    
    Returns:
        int: Description of the return value.
    
    Raises:
        TypeError: Description of the situation in which the TypeError exception is raised.
    """
    if not isinstance(data, list):
        raise TypeError("Input must be a list")

    total = 0
    for item in data:
        if not isinstance(item, (int, float)):
          raise TypeError("List elements must be numbers")
        total += item
    return total


# Tests for function1
def test_function1_valid_input():
    result = function1("test_param", "test_param1")
    assert result == {"param": "test_param", "param1": "test_param1"}

def test_function1_param1_none():
  result = function1("test_param")
  assert result == {"param": "test_param"}

def test_function1_invalid_input():
    with pytest.raises(ValueError) as exinfo:
        function1(None)
    assert str(exinfo.value) == "Param cannot be None"


# Tests for function2
def test_function2_valid_input():
    data = [1, 2, 3, 4, 5]
    result = function2(data)
    assert result == 15

def test_function2_empty_list():
  data = []
  result = function2(data)
  assert result == 0

def test_function2_mixed_types():
    with pytest.raises(TypeError) as exinfo:
        function2([1, 2, "a"])
    assert "List elements must be numbers" in str(exinfo.value)


def test_function2_invalid_input_type():
  with pytest.raises(TypeError) as exinfo:
    function2("not a list")
  assert "Input must be a list" in str(exinfo.value)


```

```markdown
This file contains pytest test cases for the provided Python code.  The tests cover various scenarios, including valid inputs, invalid inputs, and edge cases.  Exception handling is also included using `pytest.raises`.  Please replace the placeholder code with the actual Python code you want to test.