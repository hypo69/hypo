### Анализ кода модуля `printer`

**Качество кода**:
- **Соответствие стандартам**: 7
- **Плюсы**:
    -   Хорошая организация кода, разделение на функции.
    -   Использование ANSI escape-кодов для стилизации текста.
    -   Наличие документации для функций.
- **Минусы**:
    -   Не все строки соответствуют PEP8 (например, длина строк).
    -   Используется стандартный `json.dumps`, а не `j_dumps` или `j_dumps_ns` из `src.utils.jjson`.
    -   Отсутствует импорт `logger` из `src.logger`.
    -   Не все комментарии в стиле RST, не хватает подробностей.
    -   Слишком общий блок `try-except` в функции `pprint`, нет логирования ошибок.
    -   Использованы двойные кавычки для строк в примере использования.

**Рекомендации по улучшению**:
-   Привести код в соответствие со стандартом PEP8, исправить длину строк.
-   Заменить `json.dumps` на `j_dumps` или `j_dumps_ns` из `src.utils.jjson`.
-   Добавить импорт `logger` из `src.logger`.
-   Добавить подробную документацию в стиле RST, включая примеры использования для всех функций.
-   В функции `pprint` использовать логирование ошибок через `logger.error` вместо общего `try-except` с выводом ошибки через `print`.
-   Исправить одинарные кавычки на двойные в выводе `print`.

**Оптимизированный код**:
```python
"""
Модуль для работы с печатью в консоль.
=======================================

Этот модуль предоставляет функции для вывода данных в консоль с возможностью стилизации текста,
включая цвета, фоны и шрифтовые стили.

Пример использования:
---------------------
.. code-block:: python

    from src.utils.printer import pprint

    data = {'name': 'Alice', 'age': 30}
    pprint(data, text_color='green')
"""

import csv  # сохраняем импорт
from pathlib import Path
from typing import Any

import pandas as pd  # сохраняем импорт
from src.utils.jjson import j_dumps  # Используем j_dumps
from src.logger import logger # Импортируем logger
from pprint import pprint as pretty_print  # Сохраняем оригинальный импорт

# ANSI escape codes
RESET = '\033[0m'

TEXT_COLORS = {
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
BG_COLORS = {
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

FONT_STYLES = {
    'bold': '\033[1m',
    'underline': '\033[4m',
}


def _color_text(text: str, text_color: str = '', bg_color: str = '', font_style: str = '') -> str:
    """
    Применяет стили к тексту.

    Эта вспомогательная функция применяет указанный цвет, фон и стили шрифта к заданному тексту,
    используя ANSI escape-коды.

    :param text: Текст для стилизации.
    :type text: str
    :param text_color: Цвет текста.
    :type text_color: str, optional
    :param bg_color: Цвет фона.
    :type bg_color: str, optional
    :param font_style: Стиль шрифта.
    :type font_style: str, optional
    :return: Стилизованный текст.
    :rtype: str

    :Example:
        >>> _color_text('Hello, World!', text_color='green', font_style='bold')
        '\\033[1m\\033[32mHello, World!\\033[0m'
    """
    return f'{font_style}{text_color}{bg_color}{text}{RESET}'


def pprint(print_data: Any = None, text_color: str = 'white', bg_color: str = '', font_style: str = '') -> None:
    """
    Выводит данные в консоль с возможностью стилизации.

    Эта функция форматирует входные данные в зависимости от их типа и выводит их в консоль.
    Данные выводятся с дополнительным цветом текста, цветом фона и стилем шрифта на основе указанных параметров.
    Функция может обрабатывать словари, списки, строки и пути к файлам.

    :param print_data: Данные для вывода.
    :type print_data: Any, optional
    :param text_color: Цвет текста.
    :type text_color: str, optional
    :param bg_color: Цвет фона.
    :type bg_color: str, optional
    :param font_style: Стиль шрифта.
    :type font_style: str, optional
    :return: None
    :rtype: None

    :raises Exception: Если тип данных не поддерживается или возникает ошибка во время вывода.

    :Example:
        >>> pprint({'name': 'Alice', 'age': 30}, text_color='green')
        \033[32m{
            "name": "Alice",
            "age": 30
        }\033[0m

        >>> pprint(['apple', 'banana', 'cherry'], text_color='blue', font_style='bold')
        \033[34m\033[1mapple\033[0m
        \033[34m\033[1mbanana\033[0m
        \033[34m\033[1mcherry\033[0m

        >>> pprint('text example', text_color='yellow', bg_color='bg_red', font_style='underline')
        \033[4m\033[33m\033[41mtext example\033[0m
    """
    text_color = TEXT_COLORS.get(text_color.lower(), TEXT_COLORS['white'])
    bg_color = BG_COLORS.get(bg_color.lower(), '')
    font_style = FONT_STYLES.get(font_style.lower(), '')

    if print_data is None:
        print(_color_text('No data to print!', text_color=TEXT_COLORS['red']))
        return

    try:
        if isinstance(print_data, dict):
            print(_color_text(j_dumps(print_data, indent=4), text_color)) # используем j_dumps
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
        logger.error(f'Error during printing: {ex}') # Логируем ошибку
        print(_color_text(f'Error: {ex}', text_color=TEXT_COLORS['red']))



if __name__ == '__main__':
    pprint({'name': 'Alice', 'age': 30}, text_color='green')