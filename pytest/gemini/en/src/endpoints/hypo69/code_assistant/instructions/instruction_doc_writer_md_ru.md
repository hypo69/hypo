```python
import pytest
import sys
from typing import Optional


def example_function(param: str, param1: Optional[str | dict | str] = None) -> dict | None:
    """
    Args:
        param (str): Описание параметра `param`.
        param1 (Optional[str | dict | str], optional): Описание параметра `param1`. По умолчанию `None`.

    Returns:
        dict | None: Описание возвращаемого значения. Возвращает словарь или `None`.

    Raises:
        ValueError: Если параметр `param` пустой строкой.
    """
    if not param:
        raise ValueError("Параметр param не может быть пустой строкой")
    result = {"param": param}
    if param1:
        result["param1"] = param1
    return result


def test_example_function_valid_input():
    """Проверка корректной работы с валидным входом."""
    result = example_function("valid_input", "additional_data")
    assert result == {"param": "valid_input", "param1": "additional_data"}


def test_example_function_empty_param():
    """Проверка обработки пустого параметра."""
    with pytest.raises(ValueError, match="Параметр param не может быть пустой строкой"):
        example_function("")


def test_example_function_param1_is_none():
    """Проверка обработки параметра param1 равного None."""
    result = example_function("valid_input")
    assert result == {"param": "valid_input"}


def test_example_function_param1_is_dict():
    """Проверка обработки параметра param1 равного словарику."""
    param1 = {"key": "value"}
    result = example_function("valid_input", param1)
    assert result == {"param": "valid_input", "param1": {"key": "value"}}


def test_example_function_param1_is_string():
    """Проверка обработки параметра param1 равного строке."""
    param1 = "another_string"
    result = example_function("valid_input", param1)
    assert result == {"param": "valid_input", "param1": "another_string"}


def test_example_function_param1_typeerror():
    """Проверка обработки некорректного типа параметра."""
    with pytest.raises(TypeError):
        example_function("test", 123)  # Некорректный тип для param1
```