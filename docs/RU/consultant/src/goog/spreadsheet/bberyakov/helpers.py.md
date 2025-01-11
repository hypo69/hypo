## Анализ кода модуля helpers

**Качество кода**
8
-  Плюсы
    - Код выполняет заявленную функциональность: преобразование цветовых форматов (HEX -> DECIMAL, DECIMAL -> HEX, HEX -> RGB).
    - Присутствует базовая документация функций, хотя и требует доработки.
    - Код относительно читаемый и структурирован.
-  Минусы
    - Отсутствует описание модуля в начале файла.
    - Некорректное использование docstring.
    - Функция `letter_to_number` преобразует букву в число, но результат возвращается как строка, что является некорректным.
    - Не хватает обработки ошибок и проверок входных данных.
    - Не используются константы для магических чисел (например, 96, 26).
    - Нет импорта необходимых модулей.
    - Использование множественных пустых строк и лишние комментарии.
    - Отсутствует логирование.

**Рекомендации по улучшению**

1.  **Добавить описание модуля:** В начале файла добавить описание модуля с использованием docstring.
2.  **Улучшить docstring:** Привести docstring функций к стандарту RST, добавить описания параметров и возвращаемых значений.
3.  **Исправить `letter_to_number`:** Функция должна возвращать число, а не строку.
4.  **Добавить обработку ошибок:** Внедрить обработку возможных ошибок и исключений.
5.  **Использовать константы:** Заменить магические числа константами.
6.  **Добавить импорты:** Добавить необходимые импорты для `logger` и других необходимых модулей.
7.  **Убрать лишние строки и комментарии:** Очистить код от лишних пустых строк и ненужных комментариев.
8.  **Логирование:** Добавить логирование ошибок с помощью `logger.error` из `src.logger.logger`.
9.  **Проверки входных данных:** Добавить проверки входных данных для предотвращения ошибок.
10. **Переименовать переменную `hex`:** Переименовать переменную `hex` в `hex_color` для более ясного понимания.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
"""
Модуль для преобразования цветовых форматов.
=========================================================================================

Этот модуль предоставляет функции для преобразования цветов из формата HEX в DECIMAL,
из DECIMAL в HEX, и из HEX в RGB.

Пример использования
--------------------

.. code-block:: python

    from src.goog.spreadsheet.bberyakov.helpers import hex_color_to_decimal, decimal_color_to_hex, hex_to_rgb

    hex_color = '#FF0000'
    decimal_color = hex_color_to_decimal('A')
    hex_color_from_decimal = decimal_color_to_hex(27)
    rgb_color = hex_to_rgb(hex_color)

    print(f"HEX to DECIMAL: {decimal_color}")
    print(f"DECIMAL to HEX: {hex_color_from_decimal}")
    print(f"HEX to RGB: {rgb_color}")
"""
from src.logger.logger import logger
LETTER_A_ORD = 96
BASE = 26

def hex_color_to_decimal(letters: str) -> int:
    """Преобразует шестнадцатеричный цвет в десятичный.

    :param letters: Строка, представляющая шестнадцатеричный цвет (например, 'A', 'AA', 'AB').
    :type letters: str
    :raises TypeError: Если входное значение `letters` не является строкой.
    :raises ValueError: Если длина строки `letters` больше 2.
    :return: Десятичное представление цвета.
    :rtype: int

    Example:
        >>> hex_color_to_decimal('A')
        1
        >>> hex_color_to_decimal('AA')
        27
    """
    if not isinstance(letters, str):
         logger.error(f"TypeError: Input value must be a string, but received {type(letters)}")
         raise TypeError(f"Input value must be a string, but received {type(letters)}")
    if len(letters) > 2:
        logger.error(f"ValueError: Length of input string can\'t be greater than 2, but received {len(letters)}")
        raise ValueError(f"Length of input string can\'t be greater than 2, but received {len(letters)}")

    letters = letters.upper()

    def letter_to_number(letter: str) -> int:
        """Преобразует букву в число.

        :param letter: Буква для преобразования (например, 'A').
        :type letter: str
        :return: Числовое представление буквы.
        :rtype: int
        """
        return ord(letter.lower()) - LETTER_A_ORD

    return letter_to_number(letters) if len(letters) == 1 else (letter_to_number(letters[0]) * BASE) + letter_to_number(letters[1])


def decimal_color_to_hex(number: int) -> str:
    """Преобразует десятичный цвет в шестнадцатеричный.

    :param number: Десятичное представление цвета.
    :type number: int
    :raises TypeError: Если входное значение `number` не является целым числом.
    :raises ValueError: Если входное значение `number` меньше 1.
    :return: Строка, представляющая шестнадцатеричный цвет.
    :rtype: str

    Example:
        >>> decimal_color_to_hex(1)
        'A'
        >>> decimal_color_to_hex(27)
        'AA'
    """
    if not isinstance(number, int):
        logger.error(f"TypeError: Input value must be an integer, but received {type(number)}")
        raise TypeError(f"Input value must be an integer, but received {type(number)}")
    if number < 1:
        logger.error(f"ValueError: Input value must be greater or equal to 1, but received {number}")
        raise ValueError(f"Input value must be greater or equal to 1, but received {number}")

    if number <= BASE:
        return chr(number + LETTER_A_ORD).upper()
    else:
        quotient, remainder = divmod(number - 1, BASE)
        return (decimal_color_to_hex(quotient) + chr(remainder + LETTER_A_ORD + 1)).upper()

def hex_to_rgb(hex_color: str) -> tuple[int, int, int]:
    """Преобразует шестнадцатеричный цвет в RGB.

    :param hex_color: Строка, представляющая шестнадцатеричный цвет (например, '#FFFFFF' или 'FFFFFF').
    :type hex_color: str
    :raises TypeError: Если входное значение `hex_color` не является строкой.
    :raises ValueError: Если длина входной строки не равна 6 или 7 символам.
    :return: Кортеж, представляющий RGB цвет (например, (255, 255, 255)).
    :rtype: tuple[int, int, int]

    Example:
        >>> hex_to_rgb('#FFFFFF')
        (255, 255, 255)
        >>> hex_to_rgb('000000')
        (0, 0, 0)
    """
    if not isinstance(hex_color, str):
        logger.error(f"TypeError: Input value must be a string, but received {type(hex_color)}")
        raise TypeError(f"Input value must be a string, but received {type(hex_color)}")
    hex_color = hex_color[1:] if '#' in hex_color else hex_color
    if len(hex_color) != 6:
        logger.error(f"ValueError: Length of input string must be 6 or 7, but received {len(hex_color)}")
        raise ValueError(f"Length of input string must be 6, but received {len(hex_color)}")
    try:
        return (int(hex_color[:2], 16), int(hex_color[2:4], 16), int(hex_color[4:], 16))
    except ValueError as e:
        logger.error(f"ValueError: Invalid hex format: {hex_color}. {e}")
        raise ValueError(f"Invalid hex format: {hex_color}") from e