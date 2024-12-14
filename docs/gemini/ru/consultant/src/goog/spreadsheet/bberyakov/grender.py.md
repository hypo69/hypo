## Анализ кода модуля `grender.py`

**Качество кода**
7/10
- **Плюсы**
    - Код структурирован в класс `GSRender`, что способствует организации и повторному использованию.
    - Присутствует базовая функциональность для работы с Google Sheets API, включая форматирование и объединение ячеек.
    - Используются аннотации типов, что улучшает читаемость и помогает в отладке.
    - Есть docstring для классов и методов, что улучшает понимание кода.

- **Минусы**
    - Не все docstring заполнены (есть `[Function's description]` и `[Class's description]`).
    -  Отсутствует обработка ошибок, особенно при работе с Google Sheets API, что может привести к непредсказуемому поведению.
    -  В коде много повторяющегося кода, особенно при формировании диапазонов ячеек.
    - Используется стандартный `json.loads`  вместо `j_loads` или `j_loads_ns` из `src.utils.jjson`.
    - Присутствуют избыточные комментарии.
    - Не используется `logger` для логирования ошибок.
    -  Не везде используется reStructuredText (RST) для docstring и комментариев.

**Рекомендации по улучшению**
1.  **Документация**:
    -   Заполнить все docstring в формате RST, добавив подробные описания параметров и возвращаемых значений.
    -   Использовать RST для всех комментариев, включая описания модулей, классов, методов и переменных.
2.  **Обработка ошибок**:
    -   Использовать `from src.logger.logger import logger` для логирования ошибок.
    -   Избегать стандартных `try-except` блоков, предпочитая логирование ошибок с помощью `logger.error`.
3.  **Рефакторинг**:
    -   Уменьшить дублирование кода, например, вынеся логику формирования диапазонов ячеек в отдельную функцию.
    -   Использовать более информативные имена переменных.
    -   Использовать `j_loads` или `j_loads_ns` из `src.utils.jjson` вместо стандартного `json.loads`.
4.  **Форматирование**:
    -   Соблюдать PEP 8.
    -   Удалить лишние комментарии, которые не несут смысловой нагрузки.

**Оптимизированный код**
```python
"""
Модуль для рендеринга таблиц Google Sheets.
=========================================================================================

Этот модуль предоставляет класс :class:`GSRender`, который используется для форматирования
и рендеринга данных в Google Sheets.

Пример использования
--------------------

Пример создания и использования класса `GSRender`:

.. code-block:: python

    from src.goog.spreadsheet.bberyakov.grender import GSRender
    from spread import Spreadsheet, Worksheet

    # Пример использования класса GSRender
    gs_render = GSRender()
    # Получаем экземпляр таблицы и листа
    #sh: Spreadsheet = ...
    #ws: Worksheet = ...
    # gs_render.render_header(ws, 'Заголовок таблицы', 'A1:Z1')
    # gs_render.header(ws, 'Заголовок', 2)
"""
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

# ------------------------------
from src import gs
from src.helpers import  WebDriverException, pprint
from src.logger.logger import logger
# -------------------------------

import json
from typing import List, Type, Union
from spread_formatting import *
from spread import Spreadsheet, Worksheet
from goog.helpers import hex_color_to_decimal, decimal_color_to_hex, hex_to_rgb

from spread.utils import ValueInputOption, ValueRenderOption
from src.utils.jjson import j_loads
MODE = 'dev'


class GSRender:
    """
    Класс для рендеринга таблиц Google Sheets.

    Предоставляет методы для форматирования заголовков,
    объединения ячеек и установки направления текста.
    """

    render_schemas: dict

    def __init__(self, *args, **kwargs) -> None:
        """
        Инициализирует объект GSRender.

        :param args: Произвольные позиционные аргументы.
        :param kwargs: Произвольные именованные аргументы.
        """
        # TODO: fix use j_loads or j_loads_ns
        # try:
        #     with open('goog/schema.json', 'r', encoding='utf-8') as f:
        #         self.render_schemas = j_loads(f)
        # except Exception as e:
        #     logger.error(f'Ошибка при загрузке файла goog/schema.json: {e}')
        #     ...
        self.render_schemas = ...

    def render_header(self, ws: Worksheet, world_title: str, range: str = 'A1:Z1',
                      merge_type: str = 'MERGE_ALL') -> None:
        """
        Отрисовывает заголовок таблицы в первой строке.

        :param ws: Объект Worksheet, представляющий таблицу.
        :param world_title: Заголовок таблицы.
        :param range: Диапазон ячеек для заголовка, по умолчанию 'A1:Z1'.
        :param merge_type: Тип объединения ячеек ('MERGE_ALL', 'MERGE_COLUMNS', 'MERGE_ROWS'), по умолчанию 'MERGE_ALL'.
        """
        bg_color = hex_to_rgb('#FFAAAA')
        fg_color = hex_to_rgb('#AAAAAA')

        fmt = CellFormat(
            backgroundColor=Color(bg_color[0] / 255, bg_color[1] / 255, bg_color[2] / 255),
            horizontalAlignment="RIGHT",
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

        :param ws: Объект Worksheet, представляющий таблицу.
        :param range: Диапазон ячеек для объединения.
        :param merge_type: Тип объединения ячеек ('MERGE_ALL', 'MERGE_COLUMNS', 'MERGE_ROWS'), по умолчанию 'MERGE_ALL'.
        """
        ws.merge_cells(range, merge_type)

    def set_worksheet_direction(self, sh: Spreadsheet, ws: Worksheet,
                                direction: str = 'rtl') -> None:
        """
        Устанавливает направление текста для листа.

        :param sh: Объект Spreadsheet, представляющий книгу.
        :param ws: Объект Worksheet, представляющий лист.
        :param direction: Направление текста ('ltr' - слева направо, 'rtl' - справа налево), по умолчанию 'rtl'.
        """
        data: dict = {
            "requests": [
                {
                    "updateSheetProperties": {
                        "properties": {
                            "sheetId": int(ws.id),
                            "rightToLeft": direction == 'rtl'
                        },
                        "fields": "rightToLeft",
                    }
                }
            ]
        }
        sh.batch_update(data)

    def header(self, ws: Worksheet, ws_header: str | list, row: int = None) -> None:
        """
        Добавляет заголовок в указанную строку.

        :param ws: Объект Worksheet, представляющий таблицу.
        :param ws_header: Заголовок таблицы (строка или список строк).
        :param row: Номер строки для заголовка, по умолчанию - первая пустая строка.
        """
        row = (self.get_first_empty_row(ws)) if not row else row
        table_range = f'A{row}'
        ws_header = [ws_header] if isinstance(ws_header, str) else ws_header
        ws.append_row(values=ws_header, table_range=table_range)

        table_range = f'{table_range}:E{row}'

        self.render_header(ws, ws_header, table_range, 'MERGE_COLUMNS')

    def write_category_title(self, ws: Worksheet, ws_category_title: str | list, row: int = None) -> None:
        """
        Записывает заголовок категории в указанную строку.

        :param ws: Объект Worksheet, представляющий таблицу.
        :param ws_category_title: Заголовок категории (строка или список строк).
        :param row: Номер строки для заголовка категории, по умолчанию - первая пустая строка.
        """
        table_range = f'B{row}' if row else f'B{self.get_first_empty_row(ws)}'
        ws_category_title = [ws_category_title] if isinstance(ws_category_title, str) else ws_category_title
        ws.append_row(values=ws_category_title, table_range=table_range)
        merge_range = f'{table_range}:E{row if row else self.get_first_empty_row(ws)}'
        self.merge_range(ws, merge_range)

    def get_first_empty_row(self, ws: Worksheet, by_col: int = None) -> int:
        """
        Возвращает номер первой пустой строки в колонке, если в таблице есть значения, иначе 1.

        :param ws: Объект Worksheet, представляющий таблицу.
        :param by_col: Номер колонки для поиска первой пустой строки, если None - поиск по всей таблице.
        :return: Номер первой пустой строки.
        """
        str_list = list(filter(None, ws.col_values(1))) if not by_col is None else list(
            filter(None, ws.get_all_values()))
        return len(str_list) + 1