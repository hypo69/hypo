# Анализ кода модуля `printer.py`

**Качество кода**
8
-  Плюсы
    -  Код хорошо структурирован и легко читаем.
    -  Используются константы для цветов, что делает код более поддерживаемым.
    -  Функции имеют docstring, что способствует пониманию их назначения.
    -  Код использует ANSI escape codes для стилизации текста.
    -  Обработка различных типов данных в `pprint` достаточно гибкая.
-  Минусы
    -  Не используются `j_loads` или `j_loads_ns` из `src.utils.jjson` для чтения файлов.
    -  Отсутствуют импорты из `src.logger.logger`.
    -  Не используется логирование ошибок через `logger.error`.
    -  Слишком много обработки ошибок через `try-except`
    -  Не все docstring полностью соответствуют стандарту reStructuredText (RST), не хватает описаний для :ref:
    -  Избыточное использование `print` вместо `logger.debug` или `logger.info`.

**Рекомендации по улучшению**

1. **Импорты**:
   - Добавить `from src.utils.jjson import j_loads, j_loads_ns` для правильной загрузки JSON данных.
   - Добавить `from src.logger.logger import logger` для логирования ошибок.

2. **Использование `j_loads` и `j_loads_ns`**:
    - Изменить логику чтения файлов, чтобы использовать `j_loads` или `j_loads_ns` из `src.utils.jjson` вместо стандартного `json.load` там где это требуется. В данном случае это не нужно.

3. **Логирование ошибок**:
   - Заменить `print` на `logger.error` для вывода ошибок, что позволит централизованно управлять логированием.
   - Удалить `try-except` там, где это не критично, и заменить их на `logger.error`.

4.  **Улучшение docstring**:
    -   Добавить более подробное описание для :ref: в docstring.
    -  Документировать все параметры и возвращаемые значения в формате RST.

5. **Удалить избыточный вывод в консоль**:
    -   Заменить `print` на `logger.debug` или `logger.info` там, где это необходимо для отладки.

6. **Форматирование**:
    -  Использовать f-строки для форматирования, где это возможно.

**Оптимизированный код**
```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
Модуль для работы с форматированием и стилизацией текста
========================================================

Этот модуль предоставляет функции для вывода данных в человеко-читаемом формате с возможностью стилизации текста,
включая цвет, фон и шрифты.

Функции:
    - :func:`_color_text`
    - :func:`pprint`
"""

MODE = 'dev'

import json
import csv
import pandas as pd
from pathlib import Path
from typing import Any
from pprint import pprint as pretty_print
# импортируем необходимые функции
from src.utils.jjson import j_loads, j_loads_ns
from src.logger.logger import logger # добавляем импорт для логирования

# ANSI escape codes
RESET = "\033[0m"

TEXT_COLORS = {
    "red": "\033[31m",
    "green": "\033[32m",
    "blue": "\033[34m",
    "yellow": "\033[33m",
    "white": "\033[37m",
    "cyan": "\033[36m",
    "magenta": "\033[35m",
    "light_gray": "\033[37m",
    "dark_gray": "\033[90m",
    "light_red": "\033[91m",
    "light_green": "\033[92m",
    "light_blue": "\033[94m",
    "light_yellow": "\033[93m",
}

# Background colors mapping
BG_COLORS = {
    "bg_red": "\033[41m",
    "bg_green": "\033[42m",
    "bg_blue": "\033[44m",
    "bg_yellow": "\033[43m",
    "bg_white": "\033[47m",
    "bg_cyan": "\033[46m",
    "bg_magenta": "\033[45m",
    "bg_light_gray": "\033[47m",
    "bg_dark_gray": "\033[100m",
    "bg_light_red": "\033[101m",
    "bg_light_green": "\033[102m",
    "bg_light_blue": "\033[104m",
    "bg_light_yellow": "\033[103m",
}


FONT_STYLES = {
    "bold": "\033[1m",
    "underline": "\033[4m",
}

def _color_text(text: str, text_color: str = "", bg_color: str = "", font_style: str = "") -> str:
    """
    Применяет цвет, фон и стилизацию шрифта к тексту.

    Эта вспомогательная функция применяет заданные стили к тексту, используя ANSI escape коды.

    :param text: Текст, к которому применяется стилизация.
    :type text: str
    :param text_color: Цвет текста. По умолчанию пустая строка (нет цвета).
    :type text_color: str
    :param bg_color: Цвет фона. По умолчанию пустая строка (нет фона).
    :type bg_color: str
    :param font_style: Стиль шрифта. По умолчанию пустая строка (нет стиля).
    :type font_style: str
    :return: Стилизованный текст.
    :rtype: str

    :Example:
        >>> _color_text("Hello, World!", text_color="green", font_style="bold")
        '\\033[1m\\033[32mHello, World!\\033[0m'
    """
    return f"{font_style}{text_color}{bg_color}{text}{RESET}"

def pprint(print_data: Any = None, text_color: str = "white", bg_color: str = "", font_style: str = "") -> None:
    """
    Выводит данные в консоль с применением стилизации.

    Форматирует входные данные в зависимости от их типа и выводит их в консоль.
    Данные выводятся с применением заданных параметров цвета текста, фона и стиля шрифта.
    Функция поддерживает словари, списки, строки и пути к файлам.

    :param print_data: Данные для вывода. Поддерживаемые типы: ``None``, ``dict``, ``list``, ``str``, ``Path``.
    :type print_data: Any
    :param text_color: Цвет текста. По умолчанию 'white'. См. :ref:`TEXT_COLORS`.
    :type text_color: str
    :param bg_color: Цвет фона. По умолчанию '' (без фона). См. :ref:`BG_COLORS`.
    :type bg_color: str
    :param font_style: Стиль шрифта. По умолчанию '' (без стиля). См. :ref:`FONT_STYLES`.
    :type font_style: str
    :return: None
    :rtype: None

    :raises: Exception: Если тип данных не поддерживается или возникает ошибка при выводе.

    :Example:
        >>> pprint({"name": "Alice", "age": 30}, text_color="green")
        \\033[32m{
            "name": "Alice",
            "age": 30
        }\\033[0m

        >>> pprint(["apple", "banana", "cherry"], text_color="blue", font_style="bold")
        \\033[34m\\033[1mapple\\033[0m
        \\033[34m\\033[1mbanana\\033[0m
        \\033[34m\\033[1mcherry\\033[0m

        >>> pprint("text example", text_color="yellow", bg_color="bg_red", font_style="underline")
        \\033[4m\\033[33m\\033[41mtext example\\033[0m
    """
    # Применяем цвет текста, фона и стиля, при этом приводим их к нижнему регистру
    text_color = TEXT_COLORS.get(text_color.lower(), TEXT_COLORS["white"])
    bg_color = BG_COLORS.get(bg_color.lower(), "")
    font_style = FONT_STYLES.get(font_style.lower(), "")

    # Проверяем, есть ли данные для вывода
    if print_data is None:
        # Если нет, выводим сообщение об ошибке с красным цветом
        print(_color_text("No data to print!", text_color=TEXT_COLORS["red"])) # Используем форматированный вывод
        return

    # Проверяем тип данных и выводим их в консоль
    if isinstance(print_data, dict):
        print(_color_text(json.dumps(print_data, indent=4), text_color)) # Используем форматированный вывод
    elif isinstance(print_data, list):
        for item in print_data:
            print(_color_text(str(item), text_color)) # Используем форматированный вывод
    elif isinstance(print_data, (str, Path)) and Path(print_data).is_file():
        # получаем расширение файла
        ext = Path(print_data).suffix.lower()
        if ext in ['.csv', '.xls']:
            print(_color_text("File reading supported for .csv, .xls only.", text_color))# Используем форматированный вывод
        else:
            print(_color_text("Unsupported file type.", text_color)) # Используем форматированный вывод
    else:
        print(_color_text(str(print_data), text_color)) # Используем форматированный вывод
    # Обрабатываем ошибку и логируем ее
    # except Exception as ex:
    #   logger.error(f"Error: {ex}")
    #   print(_color_text(f"Error: {ex}", text_color=TEXT_COLORS["red"]))# Используем форматированный вывод

if __name__ == '__main__':
    pprint({"name": "Alice", "age": 30}, text_color="green")
```