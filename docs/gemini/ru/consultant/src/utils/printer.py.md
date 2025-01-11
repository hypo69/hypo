# Анализ кода модуля `printer`

**Качество кода:**

*   **Соответствие стандартам**: 7/10
*   **Плюсы**:
    *   Хорошая базовая структура для стилизации текста в консоли.
    *   Использование ANSI escape кодов для управления цветом, фоном и стилем текста.
    *   Наличие документации для функций и модуля.
    *   Поддержка различных типов данных для печати.
*   **Минусы**:
    *   Отсутствует импорт `logger` из `src.logger`.
    *   Используется стандартный `json.dumps` вместо `j_dumps` из `src.utils.jjson`.
    *   Не используется `logger` для вывода ошибок, вместо этого используется `print`.
    *   Избыточное использование `try-except` без логирования.
    *   Смешивание форматирования строк (f-строки) и конкатенации.
    *   В примере использования функции `pprint`, используются двойные кавычки вместо одинарных.
    *   В документации используется `code-block` без указания языка.

**Рекомендации по улучшению:**

*   Импортировать `logger` из `src.logger` для логирования ошибок.
*   Использовать `j_dumps` из `src.utils.jjson` вместо `json.dumps`.
*   Заменить `print` на `logger.error` при возникновении ошибок.
*   Удалить избыточный `try-except` и использовать `logger.error` для обработки исключений.
*   Использовать f-строки для всех форматирований строк.
*   Унифицировать использование кавычек, использовать одинарные кавычки в коде, двойные кавычки только в выводе.
*   Добавить `python` в `code-block` для корректного отображения примеров.
*   Использовать RST формат для документации функций.
*   Добавить проверку типа для `print_data` в `pprint`, чтобы избегать лишних вызовов `Path()`.
*   Добавить комментарии для не очевидных действий.

**Оптимизированный код:**

```python
## \file /src/utils/printer.py
# -*- coding: utf-8 -*-

#! venv/bin/python/python3.12

"""
Модуль для управления печатью
================================

Этот модуль предоставляет функции для печати данных в удобочитаемом формате с дополнительной стилизацией текста,
включая цвет, фон и стили шрифта.

Пример использования
----------------------
.. code-block:: python

    from src.utils.printer import pprint

    data = {'name': 'Alice', 'age': 30}
    pprint(data, text_color='green')

"""
import csv # импортируем csv
import pandas as pd # импортируем pandas
from pathlib import Path # импортируем Path
from typing import Any # импортируем Any
from src.utils.jjson import j_dumps # импортируем j_dumps
from src.logger import logger # импортируем logger для логирования
from pprint import pprint as pretty_print # импортируем pretty_print

# ANSI escape codes
RESET = '\033[0m' # константа для сброса стилей

TEXT_COLORS = { # словарь с цветами текста
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
BG_COLORS = { # словарь с цветами фона
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


FONT_STYLES = { # словарь со стилями шрифта
    'bold': '\033[1m',
    'underline': '\033[4m',
}


def _color_text(text: str, text_color: str = '', bg_color: str = '', font_style: str = '') -> str:
    """
    Применяет цвет, фон и стиль шрифта к тексту.

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
    Выводит данные с применением стилизации текста.

    :param print_data: Данные для вывода.
    :type print_data: Any, optional
    :param text_color: Цвет текста.
    :type text_color: str, optional
    :param bg_color: Цвет фона.
    :type bg_color: str, optional
    :param font_style: Стиль шрифта.
    :type font_style: str, optional
    :raises Exception: В случае ошибки при выводе данных.

    :Example:
        >>> pprint({'name': 'Alice', 'age': 30}, text_color='green')
        \\033[32m{\\n    "name": "Alice",\\n    "age": 30\\n}\\033[0m
        >>> pprint(['apple', 'banana', 'cherry'], text_color='blue', font_style='bold')
        \\033[34m\\033[1mapple\\033[0m
        \\033[34m\\033[1mbanana\\033[0m
        \\033[34m\\033[1mcherry\\033[0m
        >>> pprint('text example', text_color='yellow', bg_color='bg_red', font_style='underline')
        \\033[4m\\033[33m\\033[41mtext example\\033[0m
    """
    text_color = TEXT_COLORS.get(text_color.lower(), TEXT_COLORS['white']) # получаем цвет текста, по умолчанию белый
    bg_color = BG_COLORS.get(bg_color.lower(), '') # получаем цвет фона, по умолчанию пустая строка
    font_style = FONT_STYLES.get(font_style.lower(), '') # получаем стиль шрифта, по умолчанию пустая строка

    if print_data is None: # если данных нет, выводим сообщение об этом
        print(_color_text('No data to print!', text_color=TEXT_COLORS['red'])) # выводим сообщение об отсутствии данных
        return # выходим из функции

    try: # пробуем выполнить печать
        if isinstance(print_data, dict): # если данные - словарь, печатаем его как json
            print(_color_text(j_dumps(print_data, indent=4), text_color)) # печатаем словарь с отступом 4
        elif isinstance(print_data, list): # если данные - список, печатаем каждый элемент
            for item in print_data: # проходимся по списку и выводим каждый элемент
                print(_color_text(str(item), text_color)) # выводим каждый элемент
        elif isinstance(print_data, (str, Path)) and Path(print_data).is_file(): # если данные - строка или путь к файлу и это файл
            ext = Path(print_data).suffix.lower() # получаем расширение файла
            if ext in ['.csv', '.xls']: # если расширение .csv или .xls
                 print(_color_text('File reading supported for .csv, .xls only.', text_color)) # выводим сообщение об поддержке форматов
            else: # если другой формат
                print(_color_text('Unsupported file type.', text_color)) # выводим сообщение о неподдерживаемом формате
        else: # если тип данных не поддерживается
            print(_color_text(str(print_data), text_color)) # выводим данные как строку
    except Exception as ex: # если произошла ошибка
        logger.error(f'Error: {ex}') # логируем ошибку, используя logger, вместо print


if __name__ == '__main__':
    pprint({'name': 'Alice', 'age': 30}, text_color='green')
```