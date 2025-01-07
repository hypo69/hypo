## \file /src/utils/autodoc.py
# -*- coding: utf-8 -*-

#! venv/bin/python/python3.12

"""
.. module:: src.utils 
   :platform: Windows, Unix
   :synopsis: Демонстрация использования декоратора для автоматического обновления docstring функции.

Описание:
    Этот модуль содержит декоратор `autodoc`, который обновляет строку документации функции с добавлением времени последнего вызова функции.
    Декоратор используется для того, чтобы автоматически обновлять docstring функции при её вызове.

    Декоратор оборачивает функцию, обновляя её docstring перед вызовом, добавляя в него строку с текущим временем.
    Для получения текущего времени используется библиотека `time`.

Пример использования:
    Пример функции `example_function`, которая использует декоратор `autodoc`. Каждый раз при её вызове её docstring обновляется, и в неё добавляется информация о времени последнего вызова функции.
    
    Пример кода:
    ```python
    @autodoc
    def example_function(param1: int, param2: str) -> None:
        "\""Пример функции.
    
        Args:
            param1 (int): Первое значение.
            param2 (str): Второе значение.
        "\""
        print(f"Processing {param1} and {param2}")
    
    example_function(1, "test")
    print(example_function.__doc__)  # Вывод обновленного docstring
    example_function(2, "another test")
    print(example_function.__doc__)  # Вывод обновленного docstring
    ```

"""



import functools
import time

def autodoc(func):
    """Декоратор для автоматического обновления docstring функции."""

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Обновляем docstring перед вызовом функции
        update_docstring(func)
        return func(*args, **kwargs)

    return wrapper

def update_docstring(func):
    """Обновляет docstring функции."""
    current_time = time.strftime("%Y-%m-%d %H:%M:%S")
    
    # Проверяем, существует ли docstring
    if func.__doc__:
        # Добавляем информацию о времени последнего вызова
        func.__doc__ += f"\n\nLast called at: {current_time}"
    else:
        func.__doc__ = f"Last called at: {current_time}"

# Пример использования декоратора
@autodoc
def example_function(param1: int, param2: str) -> None:
    """Пример функции.

    Args:
        param1 (int): Первое значение.
        param2 (str): Второе значение.
    """
    print(f"Processing {param1} and {param2}")

# Тестирование функции
example_function(1, "test")
print(example_function.__doc__)  # Вывод обновленного docstring
example_function(2, "another test")
print(example_function.__doc__)  # Вывод обновленного docstring
