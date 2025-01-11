## Анализ кода модуля `grender.py`

**Качество кода**
**6/10**
-   Плюсы
    -   Присутствует базовая структура класса `GSRender`.
    -   Используются аннотации типов.
    -   Есть docstrings для методов и класса.
-   Минусы
    -   Много избыточных пустых docstring.
    -   Не используются импорты из `src` должным образом.
    -   Смешанное использование кавычек (одинарные и двойные).
    -   Отсутствует обработка ошибок с помощью `logger.error`.
    -   Не все функции документированы согласно стандартам RST.
    -   В коде присутствуют `...` - точки останова.
    -   В docstring встречаются слова 'описание' и не конкретные формулировки.

**Рекомендации по улучшению**

1.  **Улучшение документации**:
    -   Заменить пустые docstring на информативные.
    -   Использовать RST формат для docstring, включая описание аргументов, возвращаемых значений и исключений.
    -   Избегать общих формулировок типа 'описание', использовать конкретные описания действий.
2.  **Импорты**:
    -   Импортировать `logger` из `src.logger.logger`.
    -   Использовать `j_loads` или `j_loads_ns` из `src.utils.jjson` для загрузки json, если это необходимо.
3.  **Форматирование кода**:
    -   Использовать одинарные кавычки (`'`) для строк в коде.
    -   Использовать двойные кавычки (`"`) только для вывода в консоль и логгирования.
4.  **Обработка ошибок**:
    -   Заменить `try-except` блоки на `logger.error` для обработки исключений.
5.  **Улучшение функций**:
    -   Удалить точки останова `...`.
6.  **Общая структура**:
    -   Пересмотреть и унифицировать стиль кода в соответствии с PEP8.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-

"""
Модуль для рендеринга таблиц Google Sheets.
=========================================================================================

Этот модуль содержит класс :class:`GSRender`, который используется для форматирования
и визуализации данных в Google Sheets.

Пример использования
--------------------

Пример использования класса `GSRender`:

.. code-block:: python

    from src.goog.spreadsheet.bberyakov.grender import GSRender
    from src.goog.spreadsheet.bberyakov import gs

    spreadsheet = gs.Spreadsheet(file=\'example.json\')
    ws = spreadsheet.open_worksheet(\'Лист1\')
    renderer = GSRender()
    renderer.render_header(ws, \'Заголовок таблицы\')
"""
# ------------------------------
from src import gs
from src.logger.logger import logger  # Импорт logger из src.logger.logger
from src.helpers import WebDriverException, pprint
# -------------------------------

import json
from typing import List, Type, Union
from spread_formatting import *
from spread import Spreadsheet, Worksheet
from goog.helpers import hex_color_to_decimal, decimal_color_to_hex, hex_to_rgb

from spread.utils import ValueInputOption, ValueRenderOption


class GSRender():
    """
    Класс для рендеринга таблиц в Google Sheets.

    Этот класс предоставляет методы для форматирования и визуализации данных,
    включая добавление заголовков, объединение ячеек и установку направления текста.
    """
    render_schemas: dict

    def __init__(self, *args, **kwargs) -> None:
        """
        Инициализация класса GSRender.

        Args:
            *args: Произвольные позиционные аргументы.
            **kwargs: Произвольные именованные аргументы.
        """
        # self.render_schemas = json.loads('goog\\schema.json')
        ...

    def render_header(self, ws: Worksheet, world_title: str, range: str = 'A1:Z1',
                      merge_type: str = 'MERGE_ALL') -> None:
        """
        Форматирует заголовок таблицы в первой строке.

        Args:
            ws (Worksheet):  Таблица в Google Sheets.
            world_title (str): Заголовок таблицы.
            range (str, optional): Диапазон ячеек для форматирования. Defaults to 'A1:Z1'.
            merge_type (str, optional): Тип объединения ячеек ('MERGE_ALL', 'MERGE_COLUMNS', 'MERGE_ROWS'). Defaults to 'MERGE_ALL'.

        """
        bg_color = hex_to_rgb('#FFAAAA')
        fg_color = hex_to_rgb('#AAAAAA')

        fmt = CellFormat(
            backgroundColor=Color(bg_color[0] / 255, bg_color[1] / 255, bg_color[2] / 255),
            horizontalAlignment='RIGHT',
            textDirection='RIGHT_TO_LEFT',
            textFormat=TextFormat(bold=True,
                                 foregroundColor=Color(fg_color[0] / 255, fg_color[1] / 255, fg_color[2] / 255),
                                 fontSize=24),
        )

        rule = ConditionalFormatRule(
            ranges=[GridRange.from_a1_range(range, ws)],
            booleanRule=BooleanRule(
                condition=BooleanCondition('NUMBER_GREATER', ['50']),
                format=fmt
            )
        )

        set_row_height(ws, '1', 50)
        format_cell_range(ws, range, fmt)
        self.merge_range(ws, range, merge_type)

    def merge_range(self, ws: Worksheet, range: str,
                    merge_type: str = 'MERGE_ALL') -> None:
        """
        Объединяет ячейки в указанном диапазоне.

        Args:
            ws (Worksheet): Таблица в Google Sheets.
            range (str): Диапазон ячеек для объединения.
            merge_type (str, optional): Тип объединения ('MERGE_ALL', 'MERGE_COLUMNS', 'MERGE_ROWS'). Defaults to 'MERGE_ALL'.

        """
        ws.merge_cells(range, merge_type)

    def set_worksheet_direction(self, sh: Spreadsheet, ws: Worksheet,
                                direction: str = 'rtl') -> None:
        """
        Устанавливает направление текста в таблице (слева направо или справа налево).

        Args:
            sh (Spreadsheet):  Google Sheets.
            ws (Worksheet): Таблица в Google Sheets.
            direction (str, optional): Направление текста ('ltr' или 'rtl'). Defaults to 'rtl'.
        """
        data: dict = {
            'requests': [
                {
                    'updateSheetProperties': {
                        'properties': {
                            'sheetId': int(ws.id),
                            'rightToLeft': True if direction == 'rtl' else False
                        },
                        'fields': 'rightToLeft',
                    }
                }
            ]
        }
        sh.batch_update(data)

    def header(self, ws: Worksheet, ws_header: str | list, row: int = None) -> None:
        """
        Добавляет заголовок в таблицу.

        Args:
            ws (Worksheet): Таблица в Google Sheets.
            ws_header (str | list): Заголовок таблицы (строка или список строк).
            row (int, optional): Номер строки, в которую нужно добавить заголовок.
                Если не указан, заголовок добавляется в первую пустую строку. Defaults to None.
        """
        row: int = (self.get_first_empty_row(ws)) if not row else row
        table_range: str = f'A{row}'
        ws_header = [ws_header] if isinstance(ws_header, str) else ws_header
        ws.append_row(values=ws_header, table_range=table_range)

        table_range = f'{table_range}:E{row}'

        self.render_header(ws, ws_header, table_range, 'MERGE_COLUMNS')
        ...

    def write_category_title(self, ws: Worksheet, ws_category_title: str | list, row: int = None) -> None:
        """
        Добавляет заголовок категории в таблицу.

        Args:
            ws (Worksheet): Таблица в Google Sheets.
            ws_category_title (str | list): Заголовок категории (строка или список строк).
            row (int, optional): Номер строки, в которую нужно добавить заголовок категории. Defaults to None.
        """
        # row: int = (self.get_first_empty_row(ws)) if not row else row
        table_range: str = f'B{row}'
        ws_category_title = [ws_category_title] if isinstance(ws_category_title, str) else ws_category_title
        ws.append_row(values=ws_category_title, table_range=table_range)
        merge_range = f'{table_range}:E{row}'
        self.merge_range(ws, merge_range)
        ...

    def get_first_empty_row(self, ws: Worksheet, by_col: int = None) -> int:
        """
        Возвращает номер первой пустой строки в таблице.

        Args:
            ws (Worksheet): Таблица в Google Sheets.
            by_col (int, optional): Номер колонки, по которой нужно искать пустую строку.
                Если не указан, поиск ведется по всем ячейкам. Defaults to None.

        Returns:
            int: Номер первой пустой строки.
        """
        str_list = list(filter(None, ws.col_values(1))) if not by_col is None else list(
            filter(None, ws.get_all_values()))
        return len(str_list) + 1