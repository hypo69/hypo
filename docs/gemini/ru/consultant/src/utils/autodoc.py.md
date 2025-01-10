# Анализ кода модуля `autodoc`

**Качество кода**
7
-  Плюсы
    - Код достаточно прост и понятен.
    - Использование `functools.wraps` для сохранения метаданных декорируемой функции.
    - Наличие docstring для функций.
    - Есть пример использования декоратора.
-  Минусы
    - Отсутствует импорт `logger` из `src.logger.logger`.
    - Отсутствует обработка возможных ошибок в коде.
    - Docstring не соответствует стандарту reST (необходима корректировка).
    - Не хватает документации для модуля в формате RST.
    - Нет проверок типов и значений аргументов.
    - Нет проверки на существование docstring перед его использованием.
    - Нет обработки исключений при работе со временем.
    - Не используется форматирование строк f-строками где это возможно.

**Рекомендации по улучшению**
1. Добавить импорт `logger` из `src.logger.logger`.
2. Улучшить docstring в формате reST для соответствия стандартам.
3. Добавить обработку ошибок с использованием `logger.error`.
4. Добавить проверку на существование docstring перед его использованием.
5. Использовать f-строки для форматирования строк.
6. Задокументировать модуль в начале файла с использованием rST формата.
7. Добавить примеры использования в docstring.
8. Убрать лишние комментарии.
9. Проверить и добавить недостающие импорты.

**Оптимизированный код**
```python
# -*- coding: utf-8 -*-
"""
Модуль для автоматического обновления docstring функций.
=========================================================================================

Этот модуль содержит декоратор :func:`autodoc`, который обновляет строку документации функции,
добавляя информацию о времени последнего вызова.

Пример использования
--------------------

Пример функции `example_function`, использующей декоратор `autodoc`.
При каждом вызове её docstring обновляется и содержит время последнего вызова.

.. code-block:: python

    @autodoc
    def example_function(param1: int, param2: str) -> None:
        \"\"\"
        Пример функции.

        Args:
            param1 (int): Первое значение.
            param2 (str): Второе значение.
        \"\"\"
        print(f"Processing {param1} and {param2}")

    example_function(1, "test")
    print(example_function.__doc__)  # Вывод обновленного docstring
    example_function(2, "another test")
    print(example_function.__doc__)  # Вывод обновленного docstring
"""
import functools
import time
from src.logger.logger import logger  # импортируем logger


def autodoc(func):
    """
    Декоратор для автоматического обновления docstring функции.

    Args:
        func (Callable): Декорируемая функция.

    Returns:
        Callable: Обернутая функция.

    Example:
        >>> @autodoc
        ... def example_func():
        ...     '''Example docstring'''
        ...     pass
        >>> example_func()
        >>> print(example_func.__doc__)
        Example docstring

        Last called at: 2024-07-03 14:35:00
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Обновление docstring перед вызовом функции
        update_docstring(func)
        return func(*args, **kwargs)

    return wrapper


def update_docstring(func):
    """
    Обновляет docstring функции, добавляя информацию о времени последнего вызова.

    Args:
        func (Callable): Функция, docstring которой необходимо обновить.
    """
    try:
        current_time = time.strftime('%Y-%m-%d %H:%M:%S') # получаем текущее время
    except Exception as e:
        logger.error(f'Ошибка при получении текущего времени: {e}')
        return

    # Проверка существования docstring
    if func.__doc__:
        # Добавляем информацию о времени последнего вызова
        func.__doc__ += f'\n\nLast called at: {current_time}'
    else:
        func.__doc__ = f'Last called at: {current_time}'

# Пример использования декоратора
@autodoc
def example_function(param1: int, param2: str) -> None:
    """
    Пример функции.

    Args:
        param1 (int): Первое значение.
        param2 (str): Второе значение.

    Example:
        >>> example_function(1, "test")
        Processing 1 and test
    """
    print(f'Processing {param1} and {param2}')


# Тестирование функции
example_function(1, 'test')
print(example_function.__doc__)  # Вывод обновленного docstring
example_function(2, 'another test')
print(example_function.__doc__)  # Вывод обновленного docstring
```