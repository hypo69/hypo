# Анализ кода модуля `printer.py`

**Качество кода: 7**
-  Плюсы
    - Код хорошо структурирован и читаем, с разделением на функции для форматирования текста и вывода данных.
    - Присутствует обработка разных типов данных (словарь, список, строка, путь к файлу).
    - Используются константы для ANSI escape кодов, что делает код более понятным и поддерживаемым.
    - Код содержит примеры использования функций в `if __name__ == '__main__':`.
-  Минусы
    - Отсутствует импорт `j_loads` или `j_loads_ns` из `src.utils.jjson`.
    - Не используется `logger.error` для логирования ошибок.
    - Не все комментарии оформлены в стиле reStructuredText (RST).
    - Обработка ошибок в `pprint` использует стандартный блок `try-except` вместо `logger.error`.
    - В `pprint` не используется `j_loads` или `j_loads_ns` при чтении файлов.
    - Отсутствует обработка ошибок при чтении файлов.
    - Присутствует неиспользуемый импорт `pprint as pretty_print`.

**Рекомендации по улучшению**

1. **Импорт `j_loads`:**  Добавить импорт `j_loads` из `src.utils.jjson`.
2. **Логирование ошибок:** Использовать `logger.error` для логирования исключений вместо стандартного `print`.
3. **Формат RST:** Привести все комментарии и docstring к формату RST.
4. **Обработка ошибок:** Заменить `try-except` в функции `pprint` на логирование ошибок с помощью `logger.error` .
5. **Чтение файлов:** Использовать `j_loads` для чтения файлов и добавить обработку ошибок при чтении файла.
6. **Удаление неиспользуемых импортов:** Удалить неиспользуемый импорт `pprint as pretty_print`.
7. **Упростить условные выражения**: Убрать лишнее обращение к `lower()`

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
"""
Модуль для форматированного вывода в консоль.
=========================================================================================

Этот модуль предоставляет функции для вывода данных в человекочитаемом формате с возможностью
стилизации текста, включая цвет, фон и шрифтовые стили.

Функции:
    - :func:`_color_text`
    - :func:`pprint`
"""



import json
import csv
import pandas as pd
from pathlib import Path
from typing import Any
from src.utils.jjson import j_loads
from src.logger.logger import logger


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
    Применяет к тексту цвет, фон и стиль шрифта.

    Эта вспомогательная функция применяет заданные цвет и стили шрифта к заданному тексту, используя
    управляющие последовательности ANSI.

    :param text: Текст, к которому применяется стиль.
    :type text: str
    :param text_color: Цвет текста. По умолчанию - пустая строка, что означает отсутствие цвета.
    :type text_color: str, optional
    :param bg_color: Цвет фона. По умолчанию - пустая строка, что означает отсутствие цвета фона.
    :type bg_color: str, optional
    :param font_style: Стиль шрифта. По умолчанию - пустая строка, что означает отсутствие стиля.
    :type font_style: str, optional
    :return: Текст со стилями.
    :rtype: str

    :Example:
        >>> _color_text("Hello, World!", text_color="green", font_style="bold")
        '\\033[1m\\033[32mHello, World!\\033[0m'
    """
    return f"{font_style}{text_color}{bg_color}{text}{RESET}"


def pprint(print_data: Any = None, text_color: str = "white", bg_color: str = "", font_style: str = "") -> None:
    """
    Выводит данные в консоль с применением стилей.

    Эта функция форматирует входные данные в зависимости от их типа и выводит их в консоль.
    Данные выводятся с дополнительным цветом текста, фоновым цветом и стилем шрифта на основе
    указанных параметров. Функция может обрабатывать словари, списки, строки и пути к файлам.

    :param print_data: Данные для вывода. Может быть типа ``None``, ``dict``, ``list``, ``str``, или ``Path``.
    :type print_data: Any, optional
    :param text_color: Цвет текста. По умолчанию ``'white'``. См. :ref:`TEXT_COLORS`.
    :type text_color: str, optional
    :param bg_color: Цвет фона. По умолчанию ``''`` (нет фона). См. :ref:`BG_COLORS`.
    :type bg_color: str, optional
    :param font_style: Стиль шрифта. По умолчанию ``''`` (нет стиля). См. :ref:`FONT_STYLES`.
    :type font_style: str, optional
    :raises: Exception если тип данных не поддерживается или произошла ошибка при выводе.

    :Example:
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
    # Код приводит text_color к нижнему регистру и получает соответствующий код цвета из словаря TEXT_COLORS, по умолчанию белый
    text_color = TEXT_COLORS.get(text_color.lower(), TEXT_COLORS["white"])
    # Код приводит bg_color к нижнему регистру и получает соответствующий код цвета из словаря BG_COLORS, по умолчанию пустая строка
    bg_color = BG_COLORS.get(bg_color.lower(), "")
    # Код приводит font_style к нижнему регистру и получает соответствующий код стиля из словаря FONT_STYLES, по умолчанию пустая строка
    font_style = FONT_STYLES.get(font_style.lower(), "")


    if print_data is None:
        # Код выводит сообщение об отсутствии данных
        print(_color_text("No data to print!", text_color=TEXT_COLORS["red"]))
        return

    try:
        # Код проверяет, является ли print_data словарем
        if isinstance(print_data, dict):
            # Код преобразует словарь в JSON строку с отступами и выводит её
            print(_color_text(json.dumps(print_data, indent=4), text_color))
        # Код проверяет, является ли print_data списком
        elif isinstance(print_data, list):
            # Код итерируется по списку и выводит каждый элемент
            for item in print_data:
                print(_color_text(str(item), text_color))
        # Код проверяет, является ли print_data строкой или Path и существует ли файл по указанному пути
        elif isinstance(print_data, (str, Path)) and Path(print_data).is_file():
            # Код получает расширение файла в нижнем регистре
            ext = Path(print_data).suffix.lower()
            # Код проверяет расширение файла
            if ext in ['.csv', '.xls']:
                # Код выводит сообщение о поддержке файлов .csv и .xls
                print(_color_text("File reading supported for .csv, .xls only.", text_color))
                try:
                  # Код пытается прочитать файл с использованием j_loads
                    with open(print_data, 'r', encoding='utf-8') as f:
                        file_data = j_loads(f)
                    print(_color_text(str(file_data), text_color))
                except Exception as ex:
                      # Логирование ошибки при чтении файла
                    logger.error(f"Error reading file {print_data}: {ex}")
                    return
            else:
                 # Код выводит сообщение о неподдерживаемом типе файла
                print(_color_text("Unsupported file type.", text_color))
        else:
           # Код выводит данные как строку
            print(_color_text(str(print_data), text_color))
    except Exception as ex:
        # Логирование ошибки
        logger.error(f"Error during printing: {ex}")

if __name__ == '__main__':
    pprint({"name": "Alice", "age": 30}, text_color="green")
```