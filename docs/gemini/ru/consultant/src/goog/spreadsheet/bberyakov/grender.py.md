## Анализ кода модуля `grender.py`

**Качество кода: 6/10**
- **Плюсы:**
    - Код имеет базовую структуру, разбит на функции и классы.
    - Используется библиотека `gspread` для работы с Google Sheets.
    - Присутствуют некоторые комментарии, описывающие назначение функций.
- **Минусы:**
    - Не все функции и классы имеют docstring.
    - Комментарии не соответствуют стандарту reStructuredText (RST).
    - В коде используется `json.loads` вместо `j_loads` или `j_loads_ns`.
    - Присутствует избыточное использование `...` (точки останова).
    - Не хватает обработки ошибок с использованием `logger.error`.
    - Есть неиспользуемый код.
    - Некоторые строки длиннее 80 символов.
    - Переменная `MODE` объявлена в нескольких местах.

**Рекомендации по улучшению:**

1.  **Документация:**
    -   Добавить docstring в формате RST для всех классов, функций и методов.
    -   Использовать Sphinx-совместимый формат docstring (например, `:param`, `:return`).
2.  **Импорты:**
    -   Добавить отсутствующие импорты из `src.utils.jjson` и `src.logger.logger`.
3.  **Обработка данных:**
    -   Заменить `json.loads` на `j_loads` или `j_loads_ns` из `src.utils.jjson`.
4.  **Логирование:**
    -   Использовать `logger.error` для обработки исключений и логирования ошибок.
    -   Избегать стандартных блоков `try-except` без необходимости.
5.  **Код:**
    -   Убрать избыточные `...` (точки останова).
    -   Переменная `MODE` должна быть объявлена только один раз.
    -   Избегать дублирования кода.
    -   Разбить длинные строки на более короткие.
    -   Убрать неиспользуемый код.
6. **Стиль кода**
    -   Привести в порядок отступы.
    -   Удалить комментарии, которые не несут смысловой нагрузки.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
"""
Модуль для рендеринга таблиц Google Sheets.
=================================================

Этот модуль предоставляет класс :class:`GSRender` для форматирования и
рендеринга таблиц в Google Sheets, включая установку заголовков,
объединение ячеек и настройку направления текста.

Примеры
-------

Пример использования класса `GSRender`:

.. code-block:: python

    from src import gs
    from spread import Worksheet, Spreadsheet
    
    sh = gs.get_spreadsheet('my_spreadsheet')
    ws = sh.worksheet('Sheet1')
    renderer = GSRender()
    renderer.render_header(ws, "My Table Title")
"""
from src import gs
from src.helpers import logger, WebDriverException, pprint
from src.utils.jjson import j_loads  # Используем j_loads для загрузки JSON
# ------------------------------
import json
from typing import List, Type, Union
from spread_formatting import *
from spread import Spreadsheet, Worksheet
from goog.helpers import hex_color_to_decimal, decimal_color_to_hex, hex_to_rgb
from spread.utils import ValueInputOption, ValueRenderOption
from src.logger.logger import logger
MODE = 'dev'


class GSRender:
    """
    Класс для рендеринга таблиц в Google Sheets.

    Предоставляет методы для форматирования ячеек, установки заголовков,
    объединения ячеек и установки направления текста.
    """
    render_schemas: dict

    def __init__(self, *args, **kwargs) -> None:
        """
        Инициализация класса GSRender.

        :param args: Произвольные позиционные аргументы.
        :param kwards: Произвольные именованные аргументы.
        """
        # self.render_schemas = json.loads('goog\\\\schema.json')
        # Код временно отключен
        ...

    def render_header(self, ws: Worksheet, world_title: str, range: str = 'A1:Z1',
                      merge_type: str = 'MERGE_ALL') -> None:
        """
        Форматирует и рендерит заголовок таблицы.

        Устанавливает цвет фона, выравнивание текста, направление текста,
        жирный шрифт и размер шрифта для заголовка таблицы.

        :param ws: Таблица (worksheet) в Google Sheets.
        :type ws: Worksheet
        :param world_title: Заголовок таблицы.
        :type world_title: str
        :param range: Диапазон ячеек заголовка.
        :type range: str
        :param merge_type: Тип объединения ячеек.
        :type merge_type: str, ('MERGE_ALL', 'MERGE_COLUMNS', 'MERGE_ROWS')
        """
        bg_color = hex_to_rgb('#FFAAAA')
        fg_color = hex_to_rgb('#AAAAAA')

        fmt = CellFormat(
            backgroundColor=Color(bg_color[0] / 255, bg_color[1] / 255, bg_color[2] / 255),
            horizontalAlignment="RIGHT",
            textDirection='RIGHT_TO_LEFT',
            textFormat=TextFormat(bold=True,
                                   foregroundColor=Color(fg_color[0] / 255, fg_color[1] / 255,
                                                         fg_color[2] / 255),
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

        :param ws: Таблица (worksheet) в Google Sheets.
        :type ws: Worksheet
        :param range: Диапазон ячеек для объединения.
        :type range: str
        :param merge_type: Тип объединения ячеек ('MERGE_ALL', 'MERGE_COLUMNS', 'MERGE_ROWS').
        :type merge_type: str
        """
        try:
            ws.merge_cells(range, merge_type)
        except Exception as ex:
            logger.error(f'Ошибка при объединении ячеек в диапазоне {range}', exc_info=ex)
            ...

    def set_worksheet_direction(self, sh: Spreadsheet, ws: Worksheet,
                                direction: str = 'rtl'):
        """
        Устанавливает направление текста для таблицы.

        :param sh: Google Sheets.
        :type sh: Spreadsheet
        :param ws: Таблица (worksheet) в Google Sheets.
        :type ws: Worksheet
        :param direction: Направление текста ('ltr' или 'rtl').
        :type direction: str
        """
        data: dict = {
            "requests": [
                {
                    "updateSheetProperties": {
                        "properties": {
                            "sheetId": int(ws.id),
                            "rightToLeft": True if direction == 'rtl' else False

                        },
                        "fields": "rightToLeft",
                    }
                }
            ]
        }
        try:
            sh.batch_update(data)
        except Exception as ex:
            logger.error(f'Ошибка при установке направления текста для таблицы {ws.title}', exc_info=ex)
            ...

    def header(self, ws: Worksheet, ws_header: str | list, row: int = None):
        """
        Записывает и форматирует заголовок таблицы.

        :param ws: Таблица (worksheet) в Google Sheets.
        :type ws: Worksheet
        :param ws_header: Заголовок таблицы (строка или список).
        :type ws_header: str | list
        :param row: Номер строки для записи заголовка.
        :type row: int, optional
        """
        row: int = (self.get_first_empty_row(ws)) if not row else row
        table_range: str = f'A{row}'
        ws_header = [ws_header] if isinstance(ws_header, str) else ws_header
        try:
            ws.append_row(values=ws_header, table_range=table_range)
        except Exception as ex:
             logger.error(f'Ошибка при записи заголовка таблицы', exc_info=ex)
             ...

        table_range = f'{table_range}:E{row}'

        self.render_header(ws, ws_header, table_range, 'MERGE_COLUMNS')
        ...

    def write_category_title(self, ws: Worksheet, ws_category_title: str | list, row: int = None):
        """
        Записывает и форматирует заголовок категории.

        :param ws: Таблица (worksheet) в Google Sheets.
        :type ws: Worksheet
        :param ws_category_title: Заголовок категории (строка или список).
        :type ws_category_title: str | list
        :param row: Номер строки для записи заголовка категории.
        :type row: int, optional
        """
        table_range: str = f'B{row}'
        ws_category_title = [ws_category_title] if isinstance(ws_category_title, str) else ws_category_title
        try:
            ws.append_row(values=ws_category_title, table_range=table_range)
        except Exception as ex:
            logger.error(f'Ошибка при записи заголовка категории', exc_info=ex)
            ...

        merge_range = f'{table_range}:E{row}'
        self.merge_range(ws, merge_range)
        ...

    def get_first_empty_row(self, ws: Worksheet, by_col: int = None) -> int:
        """
        Возвращает номер первой пустой строки в таблице.

        :param ws: Таблица (worksheet) в Google Sheets.
        :type ws: Worksheet
        :param by_col: Номер столбца для поиска пустой строки.
        :type by_col: int, optional
        :return: Номер первой пустой строки.
        :rtype: int
        """
        if not by_col is None:
            str_list = list(filter(None, ws.col_values(1)))
        else:
            str_list = list(filter(None, ws.get_all_values()))
        return len(str_list) + 1