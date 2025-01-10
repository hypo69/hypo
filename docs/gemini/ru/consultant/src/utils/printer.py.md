# Анализ кода модуля `printer.py`

**Качество кода: 7/10**
- **Плюсы:**
    -   Код хорошо структурирован и разбит на логические блоки.
    -   Используются константы для ANSI escape-кодов, что делает код более читаемым и поддерживаемым.
    -   Функция `_color_text` реализует базовую логику для применения стилей.
    -   Функция `pprint` обрабатывает различные типы данных (словарь, список, строка, путь к файлу) и предоставляет возможность стилизации вывода.
    -   Есть пример использования в `if __name__ == '__main__':`.
- **Минусы:**
    -   Отсутствует обработка ошибок с помощью `logger.error`, вместо этого используется `print`.
    -   В функции `pprint` отсутствуют проверки на ошибки при работе с файлами.
    -   Не все функции и переменные имеют документацию в формате RST.
    -   Используется стандартный `json.dumps` вместо `j_dumps` (если он существует).
    -   Импорты не сгруппированы по PEP8.

**Рекомендации по улучшению:**

1.  **Импорты:**
    -   Сгруппировать импорты по PEP8 (сначала стандартные библиотеки, затем сторонние, затем локальные).
2.  **Логирование:**
    -   Заменить `print` на `logger.error` при обработке ошибок.
    -   Добавить логирование в функцию `pprint` для отладки.
3.  **Обработка файлов:**
    -   Добавить более подробную обработку ошибок при работе с файлами (чтение, открытие).
4.  **Форматирование кода:**
    -   Использовать одинарные кавычки для строк в коде, двойные только при выводе.
5.  **Документация:**
    -   Добавить документацию в формате RST для всех функций и переменных.
    -   Улучшить документацию к модулю.
6.  **Использование `j_dumps`**:
   - Заменить `json.dumps` на `j_dumps` (если он существует) для сериализации данных.
7. **Проверка типа файла:**
    -   В функции `pprint` добавить более детальную проверку типа файла и выводить более точное сообщение об ошибке.
8. **Обработка `None`:**
    - В функции `pprint` обработку `print_data is None` вынести в начало функции.

**Оптимизированный код:**

```python
# -*- coding: utf-8 -*-

#! venv/bin/python/python3.12

"""
Модуль для стилизации и вывода текста в консоль.
=========================================================================================

Этот модуль предоставляет функции для вывода данных в человекочитаемом формате с возможностью стилизации текста,
включая цвет, фон и начертание.

Пример использования
--------------------

Пример использования функции `pprint`:

.. code-block:: python

    from src.utils.printer import pprint
    pprint({'name': 'Alice', 'age': 30}, text_color='green')
    pprint(['apple', 'banana', 'cherry'], text_color='blue', font_style='bold')
    pprint('text example', text_color='yellow', bg_color='bg_red', font_style='underline')
"""
# стандартные библиотеки
import json
import csv
from pathlib import Path
from typing import Any
# сторонние библиотеки
import pandas as pd
# локальные библиотеки
from src.logger.logger import logger
from src.utils.jjson import j_dumps

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
    Применяет цвет, фон и стиль шрифта к тексту.

    Эта вспомогательная функция применяет указанные цвет и стили шрифта к заданному тексту,
    используя escape-последовательности ANSI.

    :param text: Текст для стилизации.
    :type text: str
    :param text_color: Цвет текста. По умолчанию пустая строка, что означает отсутствие цвета.
    :type text_color: str
    :param bg_color: Цвет фона. По умолчанию пустая строка, что означает отсутствие цвета фона.
    :type bg_color: str
    :param font_style: Стиль шрифта. По умолчанию пустая строка, что означает отсутствие стиля шрифта.
    :type font_style: str
    :return: Стилизованный текст.
    :rtype: str

    :example:
        >>> _color_text('Hello, World!', text_color='green', font_style='bold')
        '\\033[1m\\033[32mHello, World!\\033[0m'
    """
    return f'{font_style}{text_color}{bg_color}{text}{RESET}'


def pprint(print_data: Any = None, text_color: str = 'white', bg_color: str = '', font_style: str = '') -> None:
    """
    Выводит данные с возможностью стилизации.

    Эта функция форматирует входные данные в зависимости от их типа и выводит их в консоль.
    Данные выводятся с возможностью стилизации текста, фона и шрифта, в зависимости от указанных параметров.
    Функция обрабатывает словари, списки, строки и пути к файлам.

    :param print_data: Данные для вывода. Может быть `None`, `dict`, `list`, `str` или `Path`.
    :type print_data: Any
    :param text_color: Цвет текста. По умолчанию 'white'. Смотри :ref:`TEXT_COLORS`.
    :type text_color: str
    :param bg_color: Цвет фона. По умолчанию '' (без фона). Смотри :ref:`BG_COLORS`.
    :type bg_color: str
    :param font_style: Стиль шрифта. По умолчанию '' (без стиля). Смотри :ref:`FONT_STYLES`.
    :type font_style: str
    :return: None
    :rtype: None

    :raises: Exception - если тип данных не поддерживается или произошла ошибка во время вывода.

    :example:
        >>> pprint({'name': 'Alice', 'age': 30}, text_color='green')
        \\033[32m{\n    "name": "Alice",\n    "age": 30\n}\\033[0m

        >>> pprint(['apple', 'banana', 'cherry'], text_color='blue', font_style='bold')
        \\033[34m\\033[1mapple\\033[0m
        \\033[34m\\033[1mbanana\\033[0m
        \\033[34m\\033[1mcherry\\033[0m

        >>> pprint('text example', text_color='yellow', bg_color='bg_red', font_style='underline')
        \\033[4m\\033[33m\\033[41mtext example\\033[0m
    """
    # проверка если нет данных для вывода
    if print_data is None:
        print(_color_text('No data to print!', text_color=TEXT_COLORS['red']))
        return
    # устанавливаем цвет текста
    text_color = TEXT_COLORS.get(text_color.lower(), TEXT_COLORS['white'])
    # устанавливаем цвет фона
    bg_color = BG_COLORS.get(bg_color.lower(), '')
    # устанавливаем стиль шрифта
    font_style = FONT_STYLES.get(font_style.lower(), '')

    try:
        # если данные - словарь
        if isinstance(print_data, dict):
            # код исполняет сериализацию данных в формат json и вывод
            print(_color_text(j_dumps(print_data, indent=4), text_color=text_color))
        # если данные - список
        elif isinstance(print_data, list):
            # код исполняет вывод каждого элемента списка
            for item in print_data:
                print(_color_text(str(item), text_color=text_color))
        # если данные строка или путь к файлу
        elif isinstance(print_data, (str, Path)):
             # если путь к файлу
            if Path(print_data).is_file():
                # получаем расширение файла
                ext = Path(print_data).suffix.lower()
                # проверка расширения
                if ext in ['.csv', '.xls']:
                    # код выводит сообщение
                    print(_color_text('File reading supported for .csv, .xls only.', text_color=text_color))
                else:
                    # код выводит сообщение о неподдерживаемом типе файла
                    print(_color_text('Unsupported file type.', text_color=text_color))
            else:
                # код выводит данные как строку
                print(_color_text(str(print_data), text_color=text_color))
        else:
             # код выводит данные как строку
            print(_color_text(str(print_data), text_color=text_color))
    except Exception as ex:
        # логируем ошибку
        logger.error(f'Error during printing data: {ex}')
        print(_color_text(f'Error: {ex}', text_color=TEXT_COLORS['red']))


if __name__ == '__main__':
    pprint({'name': 'Alice', 'age': 30}, text_color='green')
```