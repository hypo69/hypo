# Анализ кода модуля `autodoc`

**Качество кода**
8
-  Плюсы
    -   Код хорошо структурирован и понятен.
    -   Используется `functools.wraps` для сохранения метаданных декорируемой функции.
    -   Есть пример использования декоратора, что облегчает понимание его работы.
    -   Присутствует документация модуля в формате reStructuredText, что соответствует требованиям.

-  Минусы
    -   Не используется `from src.logger.logger import logger` для логирования.
    -   Отсутствуют try-except блоки для обработки ошибок.
    -   В комментариях местами используются слова "получаем", "делаем" и подобные.

**Рекомендации по улучшению**
1.  Добавить логирование с помощью `from src.logger.logger import logger`.
2.  Избегать `try-except` блоков.
3.  Улучшить комментарии, переформулировать их более конкретно, избегая слов "получаем", "делаем" и т.д.

**Оптимизированный код**
```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
.. module:: src.utils.autodoc
   :platform: Windows, Unix
   :synopsis: Демонстрация использования декоратора для автоматического обновления docstring функции.

Описание:
    Этот модуль содержит декоратор :func:`autodoc`, который обновляет строку документации функции с добавлением времени последнего вызова функции.
    Декоратор используется для того, чтобы автоматически обновлять docstring функции при её вызове.

    Декоратор оборачивает функцию, обновляя её docstring перед вызовом, добавляя в него строку с текущим временем.
    Для получения текущего времени используется библиотека `time`.

Пример использования:
    Пример функции `example_function`, которая использует декоратор `autodoc`. Каждый раз при её вызове её docstring обновляется, и в неё добавляется информация о времени последнего вызова функции.

    Пример кода:

    .. code-block:: python

        @autodoc
        def example_function(param1: int, param2: str) -> None:
            \"\"\"Пример функции.

            :param param1: Первое значение.
            :param param2: Второе значение.
            \"\"\"
            print(f"Processing {param1} and {param2}")

        example_function(1, "test")
        print(example_function.__doc__)
        example_function(2, "another test")
        print(example_function.__doc__)
"""



import functools
import time
from src.logger.logger import logger


def autodoc(func):
    """
    Декоратор для автоматического обновления docstring функции.

    :param func: Декорируемая функция.
    :return: Обернутая функция.
    """

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Код обновляет docstring перед вызовом функции
        update_docstring(func)
        return func(*args, **kwargs)

    return wrapper


def update_docstring(func):
    """
    Обновляет docstring функции, добавляя время последнего вызова.

    :param func: Функция, docstring которой нужно обновить.
    """
    current_time = time.strftime("%Y-%m-%d %H:%M:%S")

    # Проверяет, существует ли docstring
    if func.__doc__:
        # Код добавляет информацию о времени последнего вызова в конец docstring
        func.__doc__ += f"\n\nLast called at: {current_time}"
    else:
        # Код устанавливает docstring с информацией о времени последнего вызова
        func.__doc__ = f"Last called at: {current_time}"


# Пример использования декоратора
@autodoc
def example_function(param1: int, param2: str) -> None:
    """
    Пример функции.

    :param param1: Первое значение.
    :param param2: Второе значение.
    """
    print(f"Processing {param1} and {param2}")


# Тестирование функции
example_function(1, "test")
print(example_function.__doc__)  # Вывод обновленного docstring
example_function(2, "another test")
print(example_function.__doc__)  # Вывод обновленного docstring
```