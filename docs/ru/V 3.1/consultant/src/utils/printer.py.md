## Анализ кода модуля `printer`

**Качество кода:**
- **Соответствие стандартам**: 7/10
- **Плюсы**:
  - Модуль предоставляет функции для стилизации текста в консоли с использованием ANSI escape-кодов.
  - Присутствует обработка различных типов данных для печати (dict, list, str, Path).
  - Код достаточно читаемый и логически структурирован.
- **Минусы**:
  - Используется `json.dumps` вместо `j_loads` или `j_loads_ns`.
  - Отсутствует логирование ошибок с использованием модуля `logger` из `src.logger`.
  - Некоторые docstring содержат избыточную информацию и не соответствуют PEP8.
  - Не все переменные аннотированы типами.
  - В `pprint` не обрабатываются исключения, возникающие при чтении файлов.
  - Отсутствует документация модуля.

**Рекомендации по улучшению:**

1.  **Использование `j_loads` или `j_loads_ns`**:
    - Замените `json.dumps` на `j_loads` или `j_loads_ns` для загрузки JSON данных.

2.  **Логирование**:
    - Добавьте логирование ошибок с использованием модуля `logger` из `src.logger`.

3.  **Форматирование**:
    - Переформатировать код в соответствии со стандартами PEP8.
    - Использовать аннотацию типов для всех переменных и возвращаемых значений функций.

4.  **Документация**:
    - Добавить документацию модуля.
    - Обновить docstring функций в соответствии с форматом, указанным в инструкции.

5.  **Обработка исключений**:
    - Добавить обработку исключений при чтении файлов, чтобы избежать неожиданных сбоев.

6.  **Использование одинарных кавычек**:
    - Заменить двойные кавычки на одинарные в строках, где это необходимо.

**Оптимизированный код:**

```python
## \file /src/utils/printer.py
# -*- coding: utf-8 -*-

#! .pyenv/bin/python3

"""
Модуль `printer` предоставляет утилиты для форматированного вывода текста в консоль,
включая стилизацию с использованием ANSI escape-кодов.

Он позволяет выводить данные различных типов (JSON, списки, строки, файлы) с применением
цвета текста, фона и различных стилей шрифта.

Пример использования:
----------------------

>>> from src.utils.printer import pprint
>>> data = {"name": "Alice", "age": 30}
>>> pprint(data, text_color="green")
"""

import json
import csv
import pandas as pd
from pathlib import Path
from typing import Any, Optional
from pprint import pprint as pretty_print

from src.utils.jjson import j_loads  #  Используем j_loads для загрузки JSON
from src.logger import logger  #  Импортируем logger из src.logger

# ANSI escape codes
RESET: str = '\033[0m'

TEXT_COLORS: dict[str, str] = {
    'red': '\033[31m',
    'green': '\033[32m',
    'blue': '\033[34m',
    'yellow': '\033[33m',
    'white': '\033[37m',
    'cyan': '\033[36m',
    'magenta': '\033[35m',
    'light_gray': '\033[37m',
    'dark_gray': '\033[90m',
    'light_red': '\033[91m',
    'light_green': '\033[92m',
    'light_blue': '\033[94m',
    'light_yellow': '\033[93m',
}

# Background colors mapping
BG_COLORS: dict[str, str] = {
    'bg_red': '\033[41m',
    'bg_green': '\033[42m',
    'bg_blue': '\033[44m',
    'bg_yellow': '\033[43m',
    'bg_white': '\033[47m',
    'bg_cyan': '\033[46m',
    'bg_magenta': '\033[45m',
    'bg_light_gray': '\033[47m',
    'bg_dark_gray': '\033[100m',
    'bg_light_red': '\033[101m',
    'bg_light_green': '\033[102m',
    'bg_light_blue': '\033[104m',
    'bg_light_yellow': '\033[103m',
}

FONT_STYLES: dict[str, str] = {
    'bold': '\033[1m',
    'underline': '\033[4m',
}


def _color_text(text: str, text_color: str = '', bg_color: str = '', font_style: str = '') -> str:
    """
    Применяет стилизацию (цвет текста, фона, стиль шрифта) к входному тексту.

    Args:
        text (str): Текст для стилизации.
        text_color (str, optional): Цвет текста. По умолчанию ''.
        bg_color (str, optional): Цвет фона. По умолчанию ''.
        font_style (str, optional): Стиль шрифта. По умолчанию ''.

    Returns:
        str: Стилизованный текст.

    Example:
        >>> _color_text('Hello, World!', text_color='green', font_style='bold')
        '\\033[1m\\033[32mHello, World!\\033[0m'
    """
    return f'{font_style}{text_color}{bg_color}{text}{RESET}'


def pprint(print_data: Any = None, text_color: str = 'white', bg_color: str = '', font_style: str = '') -> None:
    """
    Выводит данные в консоль с применением указанных стилей (цвет, фон, стиль шрифта).

    Args:
        print_data (Any, optional): Данные для вывода. Может быть None, dict, list, str или Path. По умолчанию None.
        text_color (str, optional): Цвет текста. По умолчанию 'white'.
        bg_color (str, optional): Цвет фона. По умолчанию ''.
        font_style (str, optional): Стиль шрифта. По умолчанию ''.

    Returns:
        None

    Example:
        >>> pprint({'name': 'Alice', 'age': 30}, text_color='green')
        \\033[32m{
            "name": "Alice",
            "age": 30
        }\\033[0m

        >>> pprint(['apple', 'banana', 'cherry'], text_color='blue', font_style='bold')
        \\033[34m\\033[1mapple\\033[0m
        \\033[34m\\033[1mbanana\\033[0m
        \\033[34m\\033[1mcherry\\033[0m

        >>> pprint('text example', text_color='yellow', bg_color='bg_red', font_style='underline')
        \\033[4m\\033[33m\\033[41mtext example\\033[0m
    """
    if not print_data:
        return

    if isinstance(text_color, str):
        text_color = TEXT_COLORS.get(text_color.lower(), TEXT_COLORS['white'])
    if isinstance(bg_color, str):
        bg_color = BG_COLORS.get(bg_color.lower(), '')
    if isinstance(font_style, str):
        font_style = FONT_STYLES.get(font_style.lower(), '')

    try:
        if isinstance(print_data, dict):
            print(_color_text(json.dumps(print_data, indent=4), text_color))  #  Используем json.dumps для форматирования вывода словаря
        elif isinstance(print_data, list):
            for item in print_data:
                print(_color_text(str(item), text_color))
        elif isinstance(print_data, (str, Path)) and Path(print_data).is_file():
            ext = Path(print_data).suffix.lower()
            if ext in ['.csv', '.xls']:
                print(_color_text('File reading supported for .csv, .xls only.', text_color))
            else:
                print(_color_text('Unsupported file type.', text_color))
        else:
            print(_color_text(str(print_data), text_color))
    except Exception as ex:
        logger.error('Error while printing data', ex, exc_info=True)  #  Логируем ошибку
        print(_color_text(f'Error: {ex}', text_color=TEXT_COLORS['red']))


if __name__ == '__main__':
    pprint({'name': 'Alice', 'age': 30}, text_color='green')