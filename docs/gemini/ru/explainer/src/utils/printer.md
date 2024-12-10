# <input code>

```python
## \file hypotez/src/utils/printer.py
# -*- coding: utf-8 -*-\
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
.. module:: src.utils
    :platform: Windows, Unix
    :synopsis: Utility functions for pretty printing and text styling.

This module provides functions to print data in a human-readable format with optional text styling, including color, background, and font styles.

Functions:
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
    """Apply color, background, and font styling to the text."""
    return f"{font_style}{text_color}{bg_color}{text}{RESET}"


def pprint(print_data: Any = None, text_color: str = "white", bg_color: str = "", font_style: str = "") -> None:
    """Pretty prints the given data with optional color, background, and font style."""
    text_color = TEXT_COLORS.get(text_color.lower(), TEXT_COLORS["white"])
    bg_color = BG_COLORS.get(bg_color.lower(), "")
    font_style = FONT_STYLES.get(font_style.lower(), "")

    if print_data is None:
        print(_color_text("No data to print!", text_color=TEXT_COLORS["red"]))
        return

    try:
        if isinstance(print_data, dict):
            print(_color_text(json.dumps(print_data, indent=4), text_color))
        elif isinstance(print_data, list):
            for item in print_data:
                print(_color_text(str(item), text_color))
        elif isinstance(print_data, (str, Path)) and Path(print_data).is_file():
            ext = Path(print_data).suffix.lower()
            if ext in ['.csv', '.xls']:
                print(_color_text("File reading supported for .csv, .xls only.", text_color))
            else:
                print(_color_text("Unsupported file type.", text_color))
        else:
            print(_color_text(str(print_data), text_color))
    except Exception as ex:
        print(_color_text(f"Error: {ex}", text_color=TEXT_COLORS["red"]))


if __name__ == '__main__':
    pprint({"name": "Alice", "age": 30}, text_color="green")
```

# <algorithm>

**Описание алгоритма (блок-схема):**

```mermaid
graph TD
    A[Пользовательский ввод] --> B{Тип данных print_data?};
    B -- dict --> C[Форматирование JSON];
    B -- list --> D[Итерация по списку];
    B -- str/Path --> E[Проверка типа файла];
    B -- другое --> F[Преобразование в строку];
    C --> G[Вывод с форматированием];
    D --> H[Вывод каждого элемента с форматированием];
    E -- .csv/.xls --> I[Вывод сообщения];
    E -- другое --> I;
    F --> G;
    I --> G;
    B -- None --> J[Вывод сообщения об отсутствии данных];
    J --> G;
    G --> K[Завершение];
    subgraph Ошибки
        G -.--> L[Обработка исключений];
        L --> M[Вывод сообщения об ошибке];
    end
```

**Примеры:**

* **print_data = {"name": "Alice", "age": 30}**: Происходит переход по ветке `dict`, выполняется форматирование JSON, вывод в консоль.
* **print_data = ["apple", "banana", "cherry"]**: Происходит переход по ветке `list`, итерация по списку, вывод каждого элемента с форматированием.
* **print_data = "my_file.csv"**: Происходит переход по ветке `str/Path`, проверяется тип файла, если `.csv` или `.xls`, то выводится сообщение.
* **print_data = None**: Происходит переход по ветке `None`, выводится сообщение об отсутствии данных.
* **print_data = 123**: Происходит переход по ветке "другое", выполняется преобразование в строку, вывод в консоль.

**Перемещение данных:**

Функция `pprint` принимает `print_data` и форматирующие параметры.  Внутри функции происходит проверка типа данных `print_data`.  В зависимости от типа данные обрабатываются и выводятся с форматированием. Результат обработки передается в функцию `_color_text` для применения стилей.


# <mermaid>

```mermaid
graph LR
    A[pprint] --> B{print_data is None?};
    B -- yes --> C[Вывод "No data..."];
    B -- no --> D{Тип print_data?};
    D -- dict --> E[json.dumps];
    D -- list --> F[Итерация по списку];
    D -- str/Path --> G[Проверка расширения];
    G -- .csv/.xls --> H[Вывод сообщения];
    G -- другое --> I[Вывод сообщения];
    E --> J[Вывод с форматированием];
    F --> K[Вывод каждого элемента с форматированием];
    H --> J;
    I --> J;
    J --> L[Завершение];
    subgraph Ошибки
        J -.--> M[Обработка исключений];
        M --> N[Вывод сообщения об ошибке];
    end
    A --> _color_text;
    _color_text --> J;
    _color_text --> K;
    _color_text --> L;
```

# <explanation>

**Импорты:**

* `json`: Для работы с JSON-данными.
* `csv`: Для работы с CSV-файлами.
* `pandas as pd`: Для работы с таблицами данных.
* `pathlib`: Для работы с файлами и путями.
* `typing`: Для задания типов переменных.
* `pprint`: Для красивой печати данных в консоль (из `pprint`).

**Классы:**

В данном модуле нет классов. Только функции.


**Функции:**

* `_color_text`:
    * Аргументы: `text`, `text_color`, `bg_color`, `font_style`.
    * Возвращаемое значение: отформатированная строка.
    * Назначение: Применяет ANSI escape коды для задания цвета, фона и стилей шрифта к тексту.
* `pprint`:
    * Аргументы: `print_data`, `text_color`, `bg_color`, `font_style`.
    * Возвращаемое значение: `None`.
    * Назначение: Печатает данные в красивом формате с возможностью применения стилей. Обрабатывает различные типы данных (словари, списки, строки, пути к файлам).
    * Обрабатывает ошибки, если встречаются исключения при работе с данными (например, при чтении файла).

**Переменные:**

* `MODE`: Строковая переменная, хранит значение 'dev'.
* `RESET`, `TEXT_COLORS`, `BG_COLORS`, `FONT_STYLES`: Переменные, хранящие ANSI escape коды для форматирования текста. Это константы, содержащие различные цветовые и стилистические коды для вывода форматированного текста в консоль.  Они позволяют динамически менять цвет, фон и стиль шрифта при выводе информации.


**Возможные ошибки и улучшения:**

* **Обработка ошибок:** Обработка исключений выполняется, но можно добавить более подробную информацию об ошибках.
* **Поддержка других типов файлов:** Можно добавить поддержку других типов файлов (например, `.txt`, `.json`).
* **Улучшение форматирования:** Можно добавить дополнительные опции форматирования, такие как отображение таблиц.
* **Документация:** Добавлены комментарии к коду, но можно добавить docstrings для функций и классов.
* **Модульность:** Функция `pprint` могла бы быть разложена на несколько более мелких функций для лучшей читаемости и повторного использования.


**Взаимосвязи с другими частями проекта:**

Модуль `printer` служит инструментом для вывода данных в удобном и стилизованном виде. Он может быть использован в других частях проекта (например, для отображения результатов обработки данных, журналов или отчетов), повышая удобочитаемость и наглядность.