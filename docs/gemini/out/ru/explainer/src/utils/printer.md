# <input code>

```python
## \file hypotez/src/utils/printer.py
# -*- coding: utf-8 -*-
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
    # ... (rest of the function)
```

# <algorithm>

**Алгоритм работы pprint:**

1. **Обработка входящих параметров:** Функция получает данные `print_data`, цвет текста `text_color`, цвет фона `bg_color` и стиль шрифта `font_style`.
2. **Обработка цвета:** Выбирает цвет текста из `TEXT_COLORS` по ключу `text_color`. Если цвет не найден, использует "white". Аналогично обрабатываются `bg_color` и `font_style`.
3. **Проверка на None:** Если `print_data` равно `None`, выводится сообщение "No data to print!".
4. **Обработка типов данных:**
    * **dict:** Используя `json.dumps` с отступом в 4 пробела, преобразует словарь в отформатированную строку и выводит её, применяя выбранный цвет.
    * **list:** Перебирает элементы списка, преобразует их в строки и выводит каждую строку, применяя выбранный цвет.
    * **str/Path (файл):** Проверяет, является ли `print_data` путём к файлу. Если файл существует и имеет расширение .csv или .xls, печатает сообщение "File reading supported for .csv, .xls only.". В противном случае печатает сообщение "Unsupported file type."
    * **Другой тип:** Преобразует данные в строку и выводит её, применяя выбранный цвет.
5. **Обработка ошибок:** В блоке `try...except` обрабатываются потенциальные исключения, возникающие при работе с данными. Если исключение возникает, печатает сообщение об ошибке с красным цветом.

**Примеры:**

* **Словарь:** `pprint({"name": "Alice", "age": 30}, text_color="green")` выведет отформатированный вывод словаря с зелёным цветом.
* **Список:** `pprint(["apple", "banana", "cherry"], text_color="blue", font_style="bold")` выведет каждый элемент списка в синем цвете и жирным шрифтом.
* **Файл (csv):** `pprint("data.csv", text_color="blue")` выведет информацию о файле, если это .csv или .xls.
* **Ошибка:** Если `print_data` не поддерживаемый тип, будет выведено сообщение об ошибке.

# <mermaid>

```mermaid
graph TD
    A[pprint(data, color, style)] --> B{data is None?};
    B -- Yes --> C[Print "No data to print!" (red)];
    B -- No --> D{Type of data?};
    D -- dict --> E[json.dumps(data, indent=4)];
    D -- dict --> F[Print formatted JSON (color)];
    D -- list --> G[Loop through list elements];
    D -- list --> H[Print each element (color)];
    D -- str/Path (file) --> I[Check file extension];
    I -- .csv/.xls --> J[Print "File reading supported..." (color)];
    I -- Other --> K[Print "Unsupported file type." (color)];
    D -- Other --> L[Convert data to string];
    D -- Other --> M[Print data (color)];
    E --> F;
    G --> H;
    I --> J;
    I --> K;
    L --> M;
    C --> N[End];
    F --> N;
    H --> N;
    J --> N;
    K --> N;
    M --> N;
```

**Подключаемые зависимости:**

* `json`: для работы со словарными данными.
* `csv`: для работы с CSV-файлами.
* `pandas`: для работы с таблицами данных.
* `pathlib`: для работы с путями к файлам.
* `typing`: для улучшения типизации.
* `pprint`: для красивого вывода данных (из `pprint` модуля).
* `sys`: для получения аргументов командной строки (если надо).

# <explanation>

**Импорты:**

* `json`: используется для форматированного вывода словарей.
* `csv`: используется для работы с CSV-файлами (хотя в функции `pprint` используется только для проверки типа файла).
* `pandas`: используется для работы с данными в формате DataFrame (пока что не используется напрямую).
* `pathlib`: используется для работы с путями к файлам.
* `typing`: используется для улучшения типизации (например, `Any` для указания произвольного типа данных).
* `pprint`: импортирует функцию `pprint` из модуля `pprint`, которая используется в коде для красивого вывода данных, но используется под другим именем `pretty_print` внутри.

**Классы:**

Нет классов в коде, только функции.

**Функции:**

* `_color_text(text, text_color="", bg_color="", font_style="")`: Функция для применения стилей (цвета, фона, шрифта) к тексту. Она принимает текст и опциональные параметры для изменения цвета, фона и стиля шрифта, возвращает строку с применёнными стилями, используя ANSI escape коды.
* `pprint(print_data=None, text_color="white", bg_color="", font_style="")`: Функция для красивого вывода данных в консоль. Она обрабатывает различные типы данных (словари, списки, строки, пути к файлам), применяя заданные цвета и стили к выводу. Обрабатывает потенциальные исключения при чтении файлов.

**Переменные:**

* `MODE`: переменная со значением 'dev'. Вероятно, используется для выбора режима работы.
* `RESET`: строка ANSI escape кода, которая используется для сброса стилей.
* `TEXT_COLORS`, `BG_COLORS`, `FONT_STYLES`: Словари, содержащие ANSI escape коды для разных цветов текста и фона, а также стилей шрифта.

**Возможные ошибки и улучшения:**

* **Обработка исключений:** Обработка исключений в блоке `try...except` улучшает отказоустойчивость кода.
* **Дополнительные типы данных:** Можно добавить поддержку других типов данных (например, чисел, кортежей).
* **Дополнительные стили:** Возможность настройки большего количества стилей, например, размера шрифта, курсива, или большее количество цветовых вариантов.
* **Валидация входов:** Можно добавить валидацию входных параметров `text_color`, `bg_color`, `font_style`, чтобы убедиться, что они соответствуют допустимым значениям.
* **Вывод Pandas DataFrame:**  Функция должна уметь обработать и вывести Pandas DataFrame. Для этого нужно добавить условие `elif isinstance(print_data, pd.DataFrame):`.
* **Вывод файлов других типов:** Функция `pprint` не поддерживает вывод файлов, кроме CSV и XLS. Необходимо добавить поддержку других типов файлов.


**Взаимосвязи с другими частями проекта:**

Функция `pprint` является частью модуля `utils`, который, скорее всего, используется в других частях проекта для удобного вывода информации.  Она служит для красивого вывода данных в консоли, что помогает разработчикам отображать информацию (логи, результаты работы) в понятном формате.