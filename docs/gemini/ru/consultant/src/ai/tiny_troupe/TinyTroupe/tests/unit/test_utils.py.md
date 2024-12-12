# Анализ кода модуля `test_utils.py`

**Качество кода**
8
- Плюсы
    - Код содержит модульные тесты для функций `extract_json`, `name_or_empty` и декоратора `repeat_on_error`.
    - Используются `MagicMock` для тестирования поведения функций с побочными эффектами.
    - Присутствуют тесты для различных сценариев, включая успешные и неудачные случаи.
- Минусы
    - Отсутствует docstring для модуля.
    - Отсутствует обработка ошибок и логирование.
    - Нет документации в reStructuredText.
    - Используется `sys.path.append` для добавления путей, что не является лучшей практикой.
    - Отсутствует тест для `json_serializer`.
    - Нет проверки импортов.

**Рекомендации по улучшению**

1.  Добавить docstring в формате reStructuredText для модуля.
2.  Добавить docstring в формате reStructuredText для каждой функции и класса.
3.  Удалить `sys.path.append` и настроить импорты более правильно.
4.  Внедрить логирование с использованием `src.logger.logger`.
5.  Заменить стандартные `try-except` на логирование ошибок.
6.  Добавить тест для функции `json_serializer`, если она существует.
7.  Избегать использования `assert result == {}`, лучше проверять с помощью `assert result is None`.
8.  Обеспечить корректную обработку исключений в тестах.
9.  Использовать более конкретные имена для исключений.

**Оптимизированный код**

```python
"""
Модуль содержит модульные тесты для функций `extract_json`, `name_or_empty` и декоратора `repeat_on_error`.
=========================================================================================
Этот модуль проверяет корректность работы основных утилит, используемых в проекте.

Пример использования
--------------------

Пример использования тестов:

.. code-block:: python

    pytest test_utils.py

"""
import pytest
from unittest.mock import MagicMock
from src.utils.jjson import j_loads, j_loads_ns # импортируем j_loads из src.utils.jjson
from src.utils.utils import name_or_empty, extract_json, repeat_on_error
from src.logger.logger import logger # импортируем logger
from tests.unit.testing_utils import *
# from tinytroupe.utils import name_or_empty, extract_json, repeat_on_error
# from testing_utils import * # импортируем из src.tests.unit.testing_utils


def test_extract_json():
    """
    Тестирует функцию `extract_json`.

    Проверяет различные сценарии извлечения JSON из строки, включая:
        - Простой JSON объект
        - JSON массив
        - JSON с экранированными символами
        - Невалидный JSON
        - Отсутствие JSON
    """
    # Тест с простой JSON строкой
    text = 'Some text before {"key": "value"} some text after'
    result = extract_json(text)
    assert result == {"key": "value"}

    # Тест с JSON массивом
    text = 'Some text before [{"key": "value"}, {"key2": "value2"}] some text after'
    result = extract_json(text)
    assert result == [{"key": "value"}, {"key2": "value2"}]

    # Тест с экранированными символами
    text = 'Some text before {"key": "\\\'value\\\'"} some text after'
    result = extract_json(text)
    assert result == {"key": "\'value\'"}

    # Тест с невалидным JSON
    text = 'Some text before {"key": "value",} some text after'
    result = extract_json(text)
    assert result is None # изменено с assert result == {}

    # Тест без JSON
    text = 'Some text with no JSON'
    result = extract_json(text)
    assert result is None # изменено с assert result == {}


def test_name_or_empty():
    """
    Тестирует функцию `name_or_empty`.

    Проверяет:
        - Возвращение имени для объекта с атрибутом `name`.
        - Возвращение пустой строки для `None`.
    """
    class MockEntity:
        """Мок класс для тестирования."""
        def __init__(self, name):
            """
            Инициализирует мок объект.

            :param name: Имя мок объекта.
            """
            self.name = name

    # Тест с именованной сущностью
    entity = MockEntity("Test")
    result = name_or_empty(entity)
    assert result == "Test"

    # Тест с None
    result = name_or_empty(None)
    assert result == ""


def test_repeat_on_error():
    """
    Тестирует декоратор `repeat_on_error`.

    Проверяет:
        - Повторение выполнения функции при возникновении исключения из списка `exceptions`.
        - Выполнение функции один раз при успешном выполнении.
        - Возникновение исключения, если оно не входит в список `exceptions`.
    """
    class DummyException(Exception):
        """Мок класс исключения для тестирования."""
        pass

    # Тест с повторами и возникновением исключения
    retries = 3
    dummy_function = MagicMock(side_effect=DummyException())
    with pytest.raises(DummyException):
        @repeat_on_error(retries=retries, exceptions=[DummyException])
        def decorated_function():
            """Декорированная функция."""
            dummy_function()
        decorated_function()
    assert dummy_function.call_count == retries

    # Тест без возникновения исключения
    retries = 3
    dummy_function = MagicMock()  # no exception raised
    @repeat_on_error(retries=retries, exceptions=[DummyException])
    def decorated_function():
        """Декорированная функция."""
        dummy_function()
    decorated_function()
    assert dummy_function.call_count == 1

    # Тест с исключением, не указанным в списке исключений
    retries = 3
    dummy_function = MagicMock(side_effect=RuntimeError())
    with pytest.raises(RuntimeError):
        @repeat_on_error(retries=retries, exceptions=[DummyException])
        def decorated_function():
            """Декорированная функция."""
            dummy_function()
        decorated_function()
    assert dummy_function.call_count == 1

# TODO
# def test_json_serializer():
```