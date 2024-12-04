```python
import pytest
import inspect

# Placeholder for the Python code to be tested.  Replace with the actual code.
def some_function(param: str, param1: str = None) -> dict | None:
    """
    Args:
        param (str): Описание параметра `param`.
        param1 (Optional[str], optional): Описание параметра `param1`. По умолчанию `None`.

    Returns:
        dict | None: Описание возвращаемого значения. Возвращает словарь или `None`.

    Raises:
        ValueError: Возникает, если `param` пустая строка.
    """
    if not param:
        raise ValueError("Параметр param не может быть пустой строкой.")
    result = {"param": param}
    if param1:
        result["param1"] = param1
    return result


# Tests for some_function
def test_some_function_valid_input():
    """Checks correct behavior with valid input."""
    param = "valid_input"
    result = some_function(param)
    assert result == {"param": "valid_input"}


def test_some_function_valid_input_with_param1():
    """Checks correct behavior with valid input and param1."""
    param = "valid_input"
    param1 = "additional_input"
    result = some_function(param, param1)
    assert result == {"param": "valid_input", "param1": "additional_input"}


def test_some_function_invalid_input():
    """Checks correct handling of empty input."""
    with pytest.raises(ValueError) as exinfo:
        some_function("", "test")
    assert "Параметр param не может быть пустой строкой." in str(exinfo.value)

```