# Анализ кода модуля `test_utils.py`

**Качество кода**
8
-  Плюсы
    - Код содержит хорошие тесты для функций `extract_json`, `name_or_empty` и декоратора `repeat_on_error`.
    - Используется `pytest` для тестирования, что является хорошей практикой.
    - Тесты покрывают различные сценарии, включая корректные и некорректные данные, а также исключения.
-  Минусы
    -  Не хватает документации для функций и модуля.
    -  Импорты `sys.path.append` выглядят избыточно и могут быть реорганизованы.
    -  Не используется `from src.logger.logger import logger` для логирования.
    -  В коде используются двойные кавычки (") вместо одинарных (') в строках, что противоречит требованиям.
    -  Отсутствует тест для функции `json_serializer`, который помечен как `TODO`.

**Рекомендации по улучшению**

1.  Добавить docstring для модуля, функций и классов, чтобы улучшить читаемость и понимание кода.
2.  Использовать одинарные кавычки для всех строк в коде, кроме случаев вывода (`print`, `logger.error`, `input`).
3.  Заменить `sys.path.append` на более явный способ импорта. Например, можно использовать `from src.utils import ...`.
4.  Использовать `from src.logger.logger import logger` для логирования ошибок.
5.  Реализовать тест для функции `json_serializer`, который помечен как `TODO`.
6.  Избегать избыточного использования `try-except` блоков.
7.  Удалить дублирование кода в тестах `repeat_on_error`.
8.  Вместо MagicMock использовать `unittest.mock.Mock`.

**Оптимизированный код**

```python
"""
Модуль тестирования для утилит TinyTroupe
=========================================================================================

Этот модуль содержит набор тестов для проверки корректности работы утилит,
таких как `name_or_empty`, `extract_json`, и декоратора `repeat_on_error`.

Пример использования
--------------------

Пример запуска тестов:

.. code-block:: bash

    pytest test_utils.py

"""
import pytest
from unittest.mock import Mock
import sys
from pathlib import Path

# sys.path.append('../../tinytroupe/') # Избыточный импорт, убираем
# sys.path.append('../../') # Избыточный импорт, убираем
# sys.path.append('../') # Избыточный импорт, убираем
# from tinytroupe.utils import name_or_empty, extract_json, repeat_on_error
# from testing_utils import *

# TODO: Заменить на нормальный импорт
sys.path.append(str(Path(__file__).parent.parent.parent))
from src.ai.tiny_troupe.TinyTroupe.tinytroupe.utils import name_or_empty, extract_json, repeat_on_error
from src.ai.tiny_troupe.TinyTroupe.tests.unit.testing_utils import *
from src.logger.logger import logger



def test_extract_json():
    """
    Тестирует функцию extract_json для извлечения JSON из строки.
    
    Проверяет извлечение JSON из различных сценариев, включая корректный JSON,
    JSON массивы, JSON с экранированными символами, некорректный JSON,
    и отсутствие JSON.
    """
    # Test with a simple JSON string
    text = 'Some text before {"key": "value"} some text after'
    result = extract_json(text)
    assert result == {'key': 'value'}

    # Test with a JSON array
    text = 'Some text before [{"key": "value"}, {"key2": "value2"}] some text after'
    result = extract_json(text)
    assert result == [{'key': 'value'}, {'key2': 'value2'}]

    # Test with escaped characters
    text = 'Some text before {"key": "\\\'value\\\'"} some text after'
    result = extract_json(text)
    assert result == {'key': '\'value\''}

    # Test with invalid JSON
    text = 'Some text before {"key": "value",} some text after'
    result = extract_json(text)
    assert result == {}

    # Test with no JSON
    text = 'Some text with no JSON'
    result = extract_json(text)
    assert result == {}


def test_name_or_empty():
    """
    Тестирует функцию name_or_empty для получения имени объекта или пустой строки.
    
    Проверяет, что функция возвращает имя объекта, если оно существует,
    или пустую строку, если объект равен None.
    """
    class MockEntity:
        """Моковый класс для тестирования."""
        def __init__(self, name):
            """Инициализация мокового объекта."""
            self.name = name

    # Test with a named entity
    entity = MockEntity('Test')
    result = name_or_empty(entity)
    assert result == 'Test'

    # Test with None
    result = name_or_empty(None)
    assert result == ''


def test_repeat_on_error():
    """
    Тестирует декоратор repeat_on_error для повторения функции при возникновении ошибки.
    
    Проверяет, что декоратор повторно вызывает функцию при возникновении указанных исключений,
    и не повторяет вызов, если исключения нет, или если исключение не входит в список
    обрабатываемых.
    """
    class DummyException(Exception):
        """Моковое исключение для тестирования."""
        pass

    # Test with retries and an exception occurring
    retries = 3
    dummy_function = Mock(side_effect=DummyException())
    with pytest.raises(DummyException):
        @repeat_on_error(retries=retries, exceptions=[DummyException])
        def decorated_function():
            dummy_function()
        decorated_function()
    assert dummy_function.call_count == retries

    # Test without any exception occurring
    retries = 3
    dummy_function = Mock()  # no exception raised
    @repeat_on_error(retries=retries, exceptions=[DummyException])
    def decorated_function():
        dummy_function()
    decorated_function()
    assert dummy_function.call_count == 1

    # Test with an exception that is not specified in the exceptions list
    retries = 3
    dummy_function = Mock(side_effect=RuntimeError())
    with pytest.raises(RuntimeError):
        @repeat_on_error(retries=retries, exceptions=[DummyException])
        def decorated_function():
            dummy_function()
        decorated_function()
    assert dummy_function.call_count == 1

# TODO: Implement test for json_serializer
# def test_json_serializer():
#     pass
```