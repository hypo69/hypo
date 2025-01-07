# Анализ кода модуля autodoc

**Качество кода**
8
 -  Плюсы
    - Код хорошо структурирован и легко читается.
    - Используется декоратор для автоматического обновления docstring, что является хорошей практикой.
    - Код содержит подробные комментарии и docstring в формате reStructuredText (RST).
    - Используется библиотека `functools` для сохранения метаданных декорируемой функции.
 -  Минусы
    - Не используется логирование ошибок.
    - Используется стандартный `time` модуль.

**Рекомендации по улучшению**
1. **Логирование**:
   - Добавить логирование ошибок при работе с docstring.
   - Использовать `from src.logger.logger import logger` для логирования.
2. **Улучшение docstring**:
   -  Уточнить docstring для модуля и функций, добавив примеры использования в формате RST.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-

#! venv/bin/python/python3.12

"""
.. module:: src.utils.autodoc
   :platform: Windows, Unix
   :synopsis: Демонстрация использования декоратора для автоматического обновления docstring функции.

Описание:
    Этот модуль содержит декоратор :func:`autodoc`, который обновляет строку документации функции с добавлением времени последнего вызова функции.
    Декоратор используется для автоматического обновления docstring функции при её вызове.

    Декоратор оборачивает функцию, обновляя её docstring перед вызовом, добавляя в него строку с текущим временем.
    Для получения текущего времени используется библиотека `time`.

Пример использования:
    Пример функции :func:`example_function`, которая использует декоратор :func:`autodoc`.
    Каждый раз при её вызове её docstring обновляется, и в неё добавляется информация о времени последнего вызова функции.

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
        print(example_function.__doc__)  # Вывод обновленного docstring
        example_function(2, "another test")
        print(example_function.__doc__)  # Вывод обновленного docstring
"""



import functools
import time
#  Импортируем logger
from src.logger.logger import logger


def autodoc(func):
    """
    Декоратор для автоматического обновления docstring функции.

    :param func: Функция, docstring которой нужно обновить.
    :type func: Callable
    :return: Обернутая функция.
    :rtype: Callable
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Обновляем docstring перед вызовом функции
        update_docstring(func)
        return func(*args, **kwargs)

    return wrapper


def update_docstring(func):
    """
    Обновляет docstring функции, добавляя информацию о времени последнего вызова.

    :param func: Функция, docstring которой нужно обновить.
    :type func: Callable
    """
    current_time = time.strftime("%Y-%m-%d %H:%M:%S")
    # Проверяем, существует ли docstring
    if func.__doc__:
        #  Добавляем информацию о времени последнего вызова
        try:
            func.__doc__ += f"\n\nLast called at: {current_time}"
        except Exception as ex:
            logger.error(f'Ошибка при обновлении docstring функции {func.__name__}: {ex}')
    else:
        #  Если docstring не существует, создаем его
        try:
            func.__doc__ = f"Last called at: {current_time}"
        except Exception as ex:
            logger.error(f'Ошибка при создании docstring функции {func.__name__}: {ex}')


# Пример использования декоратора
@autodoc
def example_function(param1: int, param2: str) -> None:
    """
    Пример функции.

    :param param1: Первое значение.
    :type param1: int
    :param param2: Второе значение.
    :type param2: str
    """
    print(f"Processing {param1} and {param2}")

# Тестирование функции
example_function(1, "test")
print(example_function.__doc__)  # Вывод обновленного docstring
example_function(2, "another test")
print(example_function.__doc__)  # Вывод обновленного docstring
```