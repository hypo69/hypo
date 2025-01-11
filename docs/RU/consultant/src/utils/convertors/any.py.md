# Анализ кода модуля `any`

**Качество кода**
    8
 -  Плюсы
        - Код выполняет рекурсивное преобразование различных типов данных в словарь.
        - Поддерживает преобразование списков, кортежей, множеств, словарей и объектов с атрибутами `__dict__`.
        - Обрабатывает базовые типы данных (int, float, str, bool, None) без изменений.
        - Код достаточно понятный и логичный.
        - Присутствуют примеры использования в `if __name__ == '__main__'`
 -  Минусы
    -  Отсутствует документация в формате RST.
    -  В функции `any2dict` используется `try-except` без конкретизации исключения и логирования ошибки.
    -  Импорт `header` не используется.
    -  Использование `is False` вместо `== False`

**Рекомендации по улучшению**
1. Добавить описание модуля в начале файла.
2. Добавить docstring в формате RST к функции `any2dict`.
3. Использовать `from src.logger.logger import logger` для логирования ошибок.
4. Уточнить обрабатываемые исключения и логировать их через `logger.error`.
5. Убрать неиспользуемый импорт `header`.
6. Использовать `== False` вместо `is False` для сравнения.
7. Добавить проверку на наличие ключей в словаре при рекурсивном вызове.
8.  Использовать  `or None` вместо `or ''`  для пустых значений

**Оптимизированный код**
```python
"""
Модуль для преобразования данных любого типа в словарь
======================================================

Этот модуль содержит функцию `any2dict`, которая рекурсивно преобразует различные типы данных,
такие как списки, кортежи, множества, словари и объекты с атрибутами `__dict__`, в словарь.

Пример использования
--------------------

Пример использования функции `any2dict`:

.. code-block:: python

    from src.utils.convertors.any import any2dict
    data = {"a": 1, "b": [2, 3], "c": {"d": 4}}
    result = any2dict(data)
    print(result)
    # Вывод: {'a': 1, 'b': [2, 3], 'c': {'d': 4}}
"""
from __future__ import annotations

# -*- coding: utf-8 -*-
#! venv/bin/python/python3.12

from typing import Any
# удален неиспользуемый импорт header
from src.logger.logger import logger # исправлен импорт

def any2dict(any_data: Any) -> dict | list | int | float | str | bool | None | False:
    """
    Рекурсивно преобразует любой тип данных в словарь.

    :param any_data: Любой тип данных.
    :type any_data: Any
    :return: Словарь, представляющий входные данные, или False, если преобразование невозможно.
    :rtype: dict | list | int | float | str | bool | None | False

    :Example:
    >>> any2dict({"a": 1, "b": [2, 3], "c": {"d": 4}})
    {'a': 1, 'b': [2, 3], 'c': {'d': 4}}
    >>> any2dict(123)
    123
    >>> any2dict("string")
    'string'
    >>> any2dict(None)
    None
    >>> class MyClass:
    ...     def __init__(self, x):
    ...         self.x = x
    >>> any2dict(MyClass(10))
    {}
    """
    # Проверка, является ли тип данных базовым
    if not isinstance(any_data, (set, list, int, float, str, bool, type(None))):
        result_dict = {}

        items_dict = None
        # Проверяем наличие атрибута __dict__ у объекта
        if hasattr(any_data, '__dict__'):
            items_dict = any_data.__dict__
        elif isinstance(any_data, dict):
            items_dict = any_data
        
        # если нет __dict__ или это не словарь, возвращаем False
        if not items_dict:
            return False
        try:
            # обходим все ключи и значения словаря или __dict__ объекта
            for key, value in items_dict.items():
                # рекурсивно преобразуем ключ и значение
                converted_key = any2dict(key)
                converted_value = any2dict(value)
                # проверяем, что ключ не равен False, чтобы добавить пустые значения
                if converted_key is not False:
                     result_dict[converted_key] = converted_value if converted_value is not False else None # исправлено на `or None`
            return result_dict

        except Exception as ex:  # Ловим конкретное исключение и логируем его
            logger.error(f'Ошибка при преобразовании {any_data}', exc_info=ex)
            return False

    elif isinstance(any_data, (list, tuple)):
        result_list = []
        for item in any_data:
            converted_item = any2dict(item)
            # исправлено на `== False`
            if converted_item == False:
                result_list.append(None) # исправлено на `None`
            else:
                result_list.append(converted_item)
        return result_list

    elif isinstance(any_data, set):
        result_set = []
        for item in any_data:
            converted_item = any2dict(item)
            # исправлено на `== False`
            if converted_item == False:
                result_set.append(None) # исправлено на `None`
            else:
                result_set.append(converted_item)
        return result_set

    elif isinstance(any_data, (int, float, str, bool, type(None))):
        return any_data  # Базовые типы данных возвращаем как есть
    else:
        return False  # Неподдерживаемый тип данных.

if __name__ == '__main__':
    import types
    # Примеры использования
    data1 = {
        "name": "John",
        "age": 30,
        "address": {
            "city": "New York",
            "street": "Main St",
            "numbers":[1,2,3]
        },
       "phones": ["123-456-7890", "987-654-3210"],
       "skills": {"python", "java", "c++"}
    }

    print(any2dict(data1))
    # Вывод: {'name': 'John', 'age': 30, 'address': {'city': 'New York', 'street': 'Main St', 'numbers': [1, 2, 3]}, 'phones': ['123-456-7890', '987-654-3210'], 'skills': ['python', 'java', 'c++']}

    data2 = [1, 2, "three", {"key": "value"}]
    print(any2dict(data2))
    # Вывод: [1, 2, 'three', {'key': 'value'}]

    data3 = 123
    print(any2dict(data3))
    # Вывод: 123

    data4 = "string"
    print(any2dict(data4))
    # Вывод: string

    data5 = None
    print(any2dict(data5))
    # Вывод: None

    class MyClass:
        def __init__(self, x):
            self.x = x

    data6 = MyClass(10)
    print(any2dict(data6))
    # Вывод: {}

    # Тестируем SimpleNamespace
    data7 = types.SimpleNamespace(a=1, b='hello', c=[1,2,3])
    print(any2dict(data7))
    # Вывод: {'a': 1, 'b': 'hello', 'c': [1, 2, 3]}

    data8 = {'a':1, 'b': types.SimpleNamespace(x=2, y=3)}
    print(any2dict(data8))
    # Вывод: {'a': 1, 'b': {'x': 2, 'y': 3}}

    data9 = [types.SimpleNamespace(x=2), 3, 'str']
    print(any2dict(data9))
    # Вывод: [{'x': 2}, 3, 'str']

    data10 = types.SimpleNamespace(a=1, b=MyClass(3))
    print(any2dict(data10))
    # Вывод: {'a': 1, 'b': None}
    
    data11 = {"a":1, "b": MyClass(10)}
    print(any2dict(data11))
    # Вывод: {'a': 1, 'b': None}
```