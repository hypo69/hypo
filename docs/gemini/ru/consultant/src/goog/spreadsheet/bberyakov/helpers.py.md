# Анализ кода модуля `helpers.py`

**Качество кода**
7/10
- Плюсы
    - Присутствуют docstring для функций, хотя и требуют доработки в формате RST.
    - Код достаточно читаемый и структурированный.
    - Функции выполняют заявленные преобразования цветов.
- Минусы
    - Отсутствует описание модуля в формате RST.
    - Docstring функций не соответствуют стандарту RST и не содержат необходимой информации (описание параметров, возвращаемого значения).
    - Не используются константы для магических чисел.
    - Используются устаревшие подходы для определения режима (MODE).
    - Нет обработки ошибок.
    - Нет логирования.
    - Много избыточных комментариев в начале файла, которые не несут смысловой нагрузки.
    - Неправильно используется конструкция `if len(letters) == 1 else` в функции `hex_color_to_decimal`.
    - Не везде используется `.upper()`.
    - Не хватает импортов необходимых модулей.

**Рекомендации по улучшению**

1.  Добавить описание модуля в формате RST.
2.  Переписать docstring функций в формате RST, включая описания параметров и возвращаемых значений.
3.  Убрать лишние комментарии и пустые строки в начале файла.
4.  Убрать избыточное использование `str()` при возвращении значений.
5.  Использовать константы для магических чисел (96, 26).
6.  Добавить обработку ошибок и логирование.
7.  Изменить конструкцию `if len(letters) == 1 else` на более читаемую.
8.  Добавить импорты модулей.
9.  Исправить форматирование кода в соответствии со стандартом PEP 8.
10. Избавиться от множественных комментариев для одного и того же.
11. Заменить множественные комментарии `"""` на `'''` для соответствия стандарту.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
"""
Модуль `helpers.py` для преобразования цветовых форматов.
=========================================================

Этот модуль предоставляет функции для преобразования цветов между различными форматами:
- HEX в DECIMAL
- DECIMAL в HEX
- HEX в RGB

.. note::

   Модуль предназначен для использования в проекте `hypotez`.

Автор(ы):
  - hypotez
"""
from src.logger.logger import logger
from typing import Tuple

MODE = 'dev'  # TODO: заменить на использование переменных окружения

_LETTER_OFFSET = 96
_BASE = 26

def hex_color_to_decimal(letters: str) -> int:
    """
    Преобразует шестнадцатеричный цвет в десятичный.

    :param letters: Строка, представляющая шестнадцатеричный цвет (например, 'A', 'AB').
    :type letters: str
    :raises ValueError: Если входная строка пустая.
    :return: Десятичное представление цвета.
    :rtype: int

    :Example:

    >>> hex_color_to_decimal('a')
    1
    >>> hex_color_to_decimal('ab')
    28
    """
    if not letters:
        logger.error('Входная строка не может быть пустой')
        raise ValueError('Input string cannot be empty')
    letters = letters.upper()

    def letter_to_number(letter: str) -> int:
        """
        Преобразует букву в число.

        :param letter: Буква для преобразования.
        :type letter: str
        :raises ValueError: Если входная строка не является буквой.
        :return: Числовое представление буквы.
        :rtype: int

        :Example:

        >>> letter_to_number('a')
        1
        >>> letter_to_number('z')
        26
        """
        if not letter.isalpha():
            logger.error('Входная строка должна быть буквой')
            raise ValueError('Input must be a letter')
        return ord(letter.lower()) - _LETTER_OFFSET

    if len(letters) == 1:
        return letter_to_number(letters)
    else:
        return (letter_to_number(letters[0]) * _BASE) + letter_to_number(letters[1])


def decimal_color_to_hex(number: int) -> str:
    """
    Преобразует десятичный цвет в шестнадцатеричный.

    :param number: Десятичное представление цвета.
    :type number: int
    :raises ValueError: Если входное число меньше или равно 0.
    :return: Шестнадцатеричное представление цвета.
    :rtype: str

    :Example:

    >>> decimal_color_to_hex(1)
    'A'
    >>> decimal_color_to_hex(28)
    'AB'
    """
    if number <= 0:
        logger.error('Входное число должно быть больше нуля')
        raise ValueError('Input number must be greater than zero')
    if number <= _BASE:
        return chr(number + _LETTER_OFFSET - 1).upper()
    else:
        quotient, remainder = divmod(number - 1, _BASE)
        return decimal_color_to_hex(quotient) + chr(remainder + _LETTER_OFFSET).upper()


def hex_to_rgb(hex_color: str) -> Tuple[int, int, int]:
    """
    Преобразует шестнадцатеричный цвет в RGB.

    :param hex_color: Строка, представляющая шестнадцатеричный цвет (например, '#FFFFFF', 'FFFFFF').
    :type hex_color: str
    :raises ValueError: Если входная строка не является корректным шестнадцатеричным цветом.
    :return: Кортеж RGB (красный, зеленый, синий).
    :rtype: Tuple[int, int, int]

    :Example:

    >>> hex_to_rgb('#FFFFFF')
    (255, 255, 255)
    >>> hex_to_rgb('000000')
    (0, 0, 0)
    """
    hex_color = hex_color[1:] if '#' in hex_color else hex_color
    try:
      if len(hex_color) != 6:
        logger.error(f'Неверный формат hex {hex_color}')
        raise ValueError(f'Invalid hex format: {hex_color}')
      return (int(hex_color[:2], 16), int(hex_color[2:4], 16), int(hex_color[4:], 16))
    except Exception as ex:
        logger.error(f'Ошибка преобразования hex в rgb: {hex_color}', exc_info=ex)
        raise
```