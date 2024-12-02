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

**Шаг 1:** Модуль импортирует необходимые библиотеки: `json`, `csv`, `pandas`, `Path`, `typing`, и `pprint`.

**Шаг 2:** Определяются константы `TEXT_COLORS`, `BG_COLORS`, `FONT_STYLES` для хранения ANSI escape кодов для форматирования текста.  

**Шаг 3:** Функция `_color_text` принимает текст и опциональные параметры цвета, фона и стиля. Возвращает отформатированный текст с применением ANSI escape кодов.

**Шаг 4:** Функция `pprint` принимает данные и параметры форматирования.

   *   Если входные данные `None`, выводит сообщение "No data to print!".
   *   В зависимости от типа входных данных (dict, list, str/Path):
       *   Для словарей, выводит отформатированное JSON представление.
       *   Для списков, выводит элементы списка с форматированием.
       *   Для файлов `.csv` и `.xls`, выводит сообщение о поддержке формата.
       *   В противном случае, выводит данные как строку.

   *   Обрабатывает все возможные исключения.

**Пример:**

Входные данные: `{"name": "Alice", "age": 30}`, `text_color="green"`

Выходные данные: Отформатированный JSON вывод с зеленым цветом.


# <mermaid>

```mermaid
graph TD
    A[pprint] --> B{print_data is None?};
    B -- Yes --> C[Print "No data to print!"];
    B -- No --> D{Type Check};
    D -- dict --> E[json.dumps];
    D -- list --> F[Loop through list];
    D -- str/Path --> G{is_file?};
    G -- Yes --> H{ext .csv/.xls?};
    H -- Yes --> I[Print "File reading supported..."];
    H -- No --> J[Print "Unsupported file type"];
    G -- No --> K[Print str(print_data)];
    E --> L[Print formatted json];
    F --> M[Print formatted item];
    C --> N[Exit];
    I --> N;
    J --> N;
    L --> N;
    M --> N;
    K --> N;
    subgraph _Error Handling_
      D -.-> O[Error Handling];
      O --> P[Print "Error..."];
      P --> N;
    end
```

**Объяснение диаграммы:**

Диаграмма показывает структуру функций и принятие решений при вызове `pprint`.  `pprint` принимает на вход данные и параметры форматирования.  В зависимости от типа данных (`None`, `dict`, `list`, `str`/`Path`) и свойств данных, выполняется соответствующее форматирование и вывод в консоль. Основной блок обработки ошибок показан в подграфе, который обработает исключения и выведет сообщение об ошибке.


# <explanation>

**Импорты:**

- `json`: для обработки JSON данных, если ввод представляет собой словарь.
- `csv`: для чтения CSV файлов, но используется только для проверки типа файла.
- `pandas`: для чтения файлов `.xls`. Но не используется в случае, если `print_data` не файл.
- `pathlib`: для работы с файловыми путями.
- `typing`: для явного указания типов, улучшая читаемость и поддержку.
- `pprint`: используется для удобного вывода структуры данных (словарь).

**Классы:**

Нет классов в данном коде, только функции и константы.

**Функции:**

- `_color_text(text, text_color="", bg_color="", font_style="")`:  Вспомогательная функция, которая применяет стили (цвет, фон, шрифт) к тексту, используя ANSI escape коды.
- `pprint(print_data, text_color="white", bg_color="", font_style="")`: Основная функция, которая выводит данные в консоль с поддержкой форматирования.

**Переменные:**

- `MODE`: Строковая константа, предположительно, для обозначения режима работы программы (например, 'dev', 'prod').
- `RESET`, `TEXT_COLORS`, `BG_COLORS`, `FONT_STYLES`: Словари, содержащие ANSI escape коды для изменения цвета, фона и стиля текста.

**Возможные ошибки и улучшения:**

- Отсутствие обработки более сложных типов данных (например, numpy arrays).
- Не проверяется, что в функциях `pprint` и `_color_text` передаются строки или пути, что может привести к ошибкам.
- Недостаточно подробная документация для функций и использования ANSI escape кодов.
- Могло бы быть удобно добавить опцию для выбора формата вывода (например, JSON, CSV).
- Можно добавить проверку на корректность input, чтобы избежать unexpected errors, например, если input будет байтовым объектом (bytes).

**Взаимосвязи с другими частями проекта:**

Функция `pprint` скорее всего используется в других частях проекта для удобной визуализации данных, например, для отображения результатов вычислений или отладки.  `utils` папка служит для хранения общих функций, которые могут использоваться в различных частях приложения.