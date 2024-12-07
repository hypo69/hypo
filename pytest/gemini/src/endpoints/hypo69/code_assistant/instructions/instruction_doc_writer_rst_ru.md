```python
import pytest
import re
from typing import Optional


# Example code (replace with the actual code)
def process_docstring(docstring: str) -> str:
    """
    Обрабатывает строку документации.

    Аргументы:
        docstring (str): Строка документации.

    Возвращаемое значение:
        str: Обработанная строка документации. Возвращает None если docstring пустой или не соответствует формату.

    Исключения:
        ValueError: Если docstring не соответствует формату.
    """

    # Проверка на пустую строку
    if not docstring:
        return None

    # Проверка на наличие ключевого слова "Аргументы:"
    if not re.search(r"Аргументы:", docstring, re.IGNORECASE):
        raise ValueError("Docstring must contain 'Аргументы:'")


    return docstring


# Test cases
def test_process_docstring_valid_input():
    """Тестирует функцию с валидным входным значением."""
    docstring = """
    Аргументы:
        param (str): Описание параметра `param`.
        param1 (Optional[str], optional): Описание параметра `param1`. По умолчанию равно `None`.

    Возвращаемое значение:
        str: Описание возвращаемого значения.
    """

    result = process_docstring(docstring)
    assert result == docstring


def test_process_docstring_valid_input_with_typehints():
    """Тестирует функцию с валидным входным значением и typehints."""
    docstring = """
    Аргументы:
        param (str): Описание параметра `param`.
        param1 (Optional[str | dict | str], optional): Описание параметра `param1`. По умолчанию равно `None`.

    Возвращаемое значение:
        dict | None: Описание возвращаемого значения. Возвращает словарь или `None`.
    """

    result = process_docstring(docstring)
    assert result == docstring



def test_process_docstring_invalid_input():
    """Тестирует функцию с невалидным входным значением."""
    docstring = "Невалидная строка документации."

    with pytest.raises(ValueError):
        process_docstring(docstring)


def test_process_docstring_empty_input():
    """Тестирует функцию с пустым входным значением."""
    docstring = ""
    result = process_docstring(docstring)
    assert result is None


def test_process_docstring_missing_arguments_section():
    """Тестирует функцию с входным значением, не содержащим раздела Аргументы."""
    docstring = """
    Возвращаемое значение:
        str: Описание возвращаемого значения.
    """
    with pytest.raises(ValueError):
        process_docstring(docstring)


# Example usage (for demonstration):
#process_docstring("Valid docstring")


```