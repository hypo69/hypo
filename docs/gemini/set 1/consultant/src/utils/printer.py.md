# Анализ кода модуля `printer.py`

**Качество кода**
8
-  Плюсы
    - Код хорошо структурирован и разбит на функции.
    - Используются константы для цветов, стилей, что делает код читаемым.
    - Есть подробные docstring для модуля и функций.
    - Присутствует пример использования в `if __name__ == '__main__':`.
 -  Минусы
    - Не используется `j_loads` или `j_loads_ns` для загрузки JSON, как указано в инструкции.
    - Отсутствует импорт `logger` для обработки ошибок.
    - Обработка ошибок в функции `pprint` использует стандартный `try-except` вместо логирования.
    - Не все комментарии приведены к формату RST.
    - Есть потенциальная ошибка обработки файлов, где только сообщается об ошибке, а не логгируется.

**Рекомендации по улучшению**
1.  Использовать `from src.utils.jjson import j_loads` для чтения файлов.
2.  Использовать `from src.logger.logger import logger` для логирования ошибок.
3.  Заменить стандартный `try-except` в `pprint` на `logger.error`.
4.  Преобразовать все комментарии в формат RST.
5.  Улучшить обработку файлов, добавив логгирование ошибок.
6.  Устранить замечание по поводу поддержки только `.csv` и `.xls` (хотя это в рамках требований, но все же).

**Оптимизированный код**
```python
# -*- coding: utf-8 -*-

#! venv/bin/python/python3.12

"""
.. module:: src.utils.printer
    :platform: Windows, Unix
    :synopsis: Utility functions for pretty printing and text styling.

This module provides functions to print data in a human-readable format with optional text styling, including color, background, and font styles.

Functions:
    - :func:`_color_text`
    - :func:`pprint`
"""



import json
import csv
import pandas as pd
from pathlib import Path
from typing import Any
from pprint import pprint as pretty_print
# from src.utils.jjson import j_loads  # TODO: добавить использование j_loads если понадобится чтение из файла
from src.logger.logger import logger # импортируем логер
# ANSI escape codes
RESET = "\\033[0m"

TEXT_COLORS = {
    "red": "\\033[31m",
    "green": "\\033[32m",
    "blue": "\\033[34m",
    "yellow": "\\033[33m",
    "white": "\\033[37m",
    "cyan": "\\033[36m",
    "magenta": "\\033[35m",
    "light_gray": "\\033[37m",
    "dark_gray": "\\033[90m",
    "light_red": "\\033[91m",
    "light_green": "\\033[92m",
    "light_blue": "\\033[94m",
    "light_yellow": "\\033[93m",
}

# Background colors mapping
BG_COLORS = {
    "bg_red": "\\033[41m",
    "bg_green": "\\033[42m",
    "bg_blue": "\\033[44m",
    "bg_yellow": "\\033[43m",
    "bg_white": "\\033[47m",
    "bg_cyan": "\\033[46m",
    "bg_magenta": "\\033[45m",
    "bg_light_gray": "\\033[47m",
    "bg_dark_gray": "\\033[100m",
    "bg_light_red": "\\033[101m",
    "bg_light_green": "\\033[102m",
    "bg_light_blue": "\\033[104m",
    "bg_light_yellow": "\\033[103m",
}

FONT_STYLES = {
    "bold": "\\033[1m",
    "underline": "\\033[4m",
}


def _color_text(text: str, text_color: str = "", bg_color: str = "", font_style: str = "") -> str:
    """
    Apply color, background, and font styling to the text.

    This helper function applies the provided color and font styles to the given text using ANSI escape codes.

    :param text: The text to be styled.
    :param text_color: The color to apply to the text. Default is an empty string, meaning no color.
    :param bg_color: The background color to apply. Default is an empty string, meaning no background color.
    :param font_style: The font style to apply to the text. Default is an empty string, meaning no font style.
    :return: The styled text as a string.

    :example:
        >>> _color_text("Hello, World!", text_color="green", font_style="bold")
        '\\033[1m\\033[32mHello, World!\\033[0m'
    """
    # функция формирует строку с ANSI кодами для стилизации текста
    return f"{font_style}{text_color}{bg_color}{text}{RESET}"


def pprint(print_data: Any = None, text_color: str = "white", bg_color: str = "", font_style: str = "") -> None:
    """
    Pretty prints the given data with optional color, background, and font style.

    This function formats the input data based on its type and prints it to the console. The data is printed with optional
    text color, background color, and font style based on the specified parameters. The function can handle dictionaries,
    lists, strings, and file paths.

    :param print_data: The data to be printed. Can be of type ``None``, ``dict``, ``list``, ``str``, or ``Path``.
    :param text_color: The color to apply to the text. Default is 'white'. See :ref:`TEXT_COLORS`.
    :param bg_color: The background color to apply to the text. Default is '' (no background color). See :ref:`BG_COLORS`.
    :param font_style: The font style to apply to the text. Default is '' (no font style). See :ref:`FONT_STYLES`.
    :return: None

    :raises: Exception if the data type is unsupported or an error occurs during printing.

    :example:
        >>> pprint({"name": "Alice", "age": 30}, text_color="green")
        \033[32m{
            "name": "Alice",
            "age": 30
        }\033[0m

        >>> pprint(["apple", "banana", "cherry"], text_color="blue", font_style="bold")
        \033[34m\033[1mapple\033[0m
        \033[34m\033[1mbanana\033[0m
        \033[34m\033[1mcherry\033[0m

        >>> pprint("text example", text_color="yellow", bg_color="bg_red", font_style="underline")
        \033[4m\033[33m\033[41mtext example\033[0m
    """
    # Приведение цветов и стилей к нижнему регистру и получение значений из словарей, по умолчанию 'white' и ''
    text_color = TEXT_COLORS.get(text_color.lower(), TEXT_COLORS["white"])
    bg_color = BG_COLORS.get(bg_color.lower(), "")
    font_style = FONT_STYLES.get(font_style.lower(), "")

    # Проверка на None и вывод сообщения
    if print_data is None:
        print(_color_text("No data to print!", text_color=TEXT_COLORS["red"]))
        return

    try:
        # Проверка типа данных для печати
        if isinstance(print_data, dict):
            print(_color_text(json.dumps(print_data, indent=4), text_color)) # Печать словаря
        elif isinstance(print_data, list):
            for item in print_data:
                 print(_color_text(str(item), text_color)) # Печать списка
        elif isinstance(print_data, (str, Path)) and Path(print_data).is_file():
            # Проверка, является ли путь файлом
            ext = Path(print_data).suffix.lower() # Получение расширения файла
            if ext in ['.csv', '.xls']:
                #  Если файл с расширением csv или xls выводим сообщение о поддержке
                print(_color_text("File reading supported for .csv, .xls only.", text_color))
                # TODO: если потребуется загрузка файлов, можно использовать pandas
                # df = pd.read_csv(print_data)
                # pprint(df.to_dict(orient="records"), text_color=text_color)
            else:
                #  Если файл с другим расширением выводим сообщение о неподдержке
                print(_color_text("Unsupported file type.", text_color))
        else:
             print(_color_text(str(print_data), text_color)) # Печать других типов данных
    except Exception as ex:
        # Логирование ошибки с использованием logger.error вместо печати в консоль
        logger.error(f"Error during pretty print: {ex}", exc_info=True)
        print(_color_text(f"Error: {ex}", text_color=TEXT_COLORS["red"])) # Вывод сообщения об ошибке
    

if __name__ == '__main__':
    pprint({"name": "Alice", "age": 30}, text_color="green")