## Анализ кода модуля `grender.py`

**Качество кода**
7/10
-   **Плюсы**
    -   Код структурирован в класс `GSRender`.
    -   Используются аннотации типов.
    -   Присутствуют docstring для функций, но требуют доработки.
    -   Логика работы с Google Sheets API инкапсулирована в классе.
-   **Минусы**
    -   Не все docstring соответствуют формату reStructuredText (RST) и требуют доработки.
    -   Не хватает обработки ошибок с использованием `logger.error`.
    -   Использование `json.loads` без обработки исключений.
    -   Некоторые комментарии избыточны или неинформативны.
    -   Используется `...` как заглушка.
    -   Не все импорты используются.
    -   Много лишних комментариев
    -   Общее описание класса не соответствует RST

**Рекомендации по улучшению**

1.  **Форматирование docstring**: Привести все docstring к формату reStructuredText (RST), добавить параметры, возвращаемые значения.
2.  **Обработка ошибок**: Заменить `try-except` на использование `logger.error` для обработки ошибок и избегать `...`
3.  **Использование `j_loads`**: Применять `j_loads` или `j_loads_ns` из `src.utils.jjson` для чтения файлов.
4.  **Удалить неиспользуемые импорты**.
5.  **Удалить лишние комментарии**
6.  **Обновить описание класса в RST формате**
7.  **Удалить неиспользуемые переменные**

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
Модуль для рендеринга таблиц Google Sheets.
=========================================

Этот модуль содержит класс :class:`GSRender`, который используется для форматирования и отображения данных в Google Sheets.
Он включает в себя функции для рендеринга заголовков, объединения ячеек и установки направления текста.

Пример использования
--------------------

.. code-block:: python

    from src.goog.spreadsheet.bberyakov.grender import GSRender
    from spread import Worksheet, Spreadsheet

    gs_render = GSRender()
    # sh: Spreadsheet
    # ws: Worksheet
    gs_render.render_header(ws, "Заголовок таблицы", "A1:Z1")

"""
# ------------------------------
from src.logger.logger import logger
from src.utils.jjson import j_loads
from src.helpers import WebDriverException, pprint
# ------------------------------
from typing import List, Type, Union
from spread_formatting import CellFormat, Color, TextFormat, ConditionalFormatRule, BooleanRule, BooleanCondition, GridRange
from spread import Spreadsheet, Worksheet
from goog.helpers import hex_to_rgb



class GSRender():
    """
    Класс для рендеринга таблиц Google Sheets.
    =========================================

    Предоставляет методы для форматирования ячеек, установки заголовков, объединения ячеек и установки направления текста.

    :ivar render_schemas: Словарь со схемами рендеринга.
    :vartype render_schemas: dict
    """
    render_schemas: dict

    def __init__(self, *args, **kwards) -> None:
        """
        Инициализирует класс GSRender.

        :param args: Произвольные позиционные аргументы.
        :param kwards: Произвольные именованные аргументы.
        :return: None
        """
        try:
            # загружает json файл
           self.render_schemas = j_loads('goog/schema.json')
        except Exception as ex:
             logger.error('Ошибка загрузки файла `goog/schema.json`', ex)
            
    def render_header(self, ws: Worksheet, world_title: str, range: str = 'A1:Z1', merge_type: str = 'MERGE_ALL') -> None:
        """
        Форматирует заголовок таблицы в первой строке.

        :param ws: Объект Worksheet, представляющий таблицу.
        :type ws: Worksheet
        :param world_title: Заголовок таблицы.
        :type world_title: str
        :param range: Диапазон ячеек для форматирования, по умолчанию 'A1:Z1'.
        :type range: str
        :param merge_type: Тип объединения ячеек ('MERGE_ALL', 'MERGE_COLUMNS', 'MERGE_ROWS'), по умолчанию 'MERGE_ALL'.
        :type merge_type: str
        :return: None
        """
        bg_color = hex_to_rgb('#FFAAAA')
        fg_color = hex_to_rgb('#AAAAAA')

        fmt = CellFormat(
            backgroundColor=Color(bg_color[0] / 255, bg_color[1] / 255, bg_color[2] / 255),
            horizontalAlignment="RIGHT",
            textDirection='RIGHT_TO_LEFT',
            textFormat=TextFormat(
                bold=True,
                foregroundColor=Color(fg_color[0] / 255, fg_color[1] / 255, fg_color[2] / 255),
                fontSize=24,
            ),
        )
        # применяет форматирование к ячейкам в заданном диапазоне
        rule = ConditionalFormatRule(
            ranges=[GridRange.from_a1_range(range, ws)],
            booleanRule=BooleanRule(
                condition=BooleanCondition('NUMBER_GREATER', ['50']),
                format=fmt,
            ),
        )

        set_row_height(ws, '1', 50)
        #format_cell_ranges(ws, [range], rule)
        format_cell_range(ws, range, fmt)
        self.merge_range(ws, range, merge_type)

    def merge_range(self, ws: Worksheet, range: str, merge_type: str = 'MERGE_ALL') -> None:
        """
        Объединяет ячейки в заданном диапазоне.

        :param ws: Объект Worksheet, представляющий таблицу.
        :type ws: Worksheet
        :param range: Диапазон ячеек для объединения.
        :type range: str
        :param merge_type: Тип объединения ячеек ('MERGE_ALL', 'MERGE_COLUMNS', 'MERGE_ROWS'), по умолчанию 'MERGE_ALL'.
        :type merge_type: str
        :return: None
        """
        # обьединяет ячейки
        ws.merge_cells(range, merge_type)

    def set_worksheet_direction(self, sh: Spreadsheet, ws: Worksheet, direction: str = 'rtl') -> None:
        """
        Устанавливает направление текста на листе.

        :param sh: Объект Spreadsheet, представляющий книгу.
        :type sh: Spreadsheet
        :param ws: Объект Worksheet, представляющий таблицу.
        :type ws: Worksheet
        :param direction: Направление текста ('ltr' или 'rtl'), по умолчанию 'rtl'.
        :type direction: str
        :return: None
        """
        # подготавливает данные для обновления свойств листа
        data: dict = {
            "requests": [
                {
                    "updateSheetProperties": {
                        "properties": {
                            "sheetId": int(ws.id),
                            "rightToLeft": True,
                        },
                        "fields": "rightToLeft",
                    }
                }
            ]
        }
        # отправляет запрос на обновление
        sh.batch_update(data)

################################################################################################################

    def header(self, ws: Worksheet, ws_header: str | list, row: int = None) -> None:
        """
        Записывает и форматирует заголовок таблицы.

        :param ws: Объект Worksheet, представляющий таблицу.
        :type ws: Worksheet
        :param ws_header: Заголовок таблицы (строка или список).
        :type ws_header: str | list
        :param row: Номер строки для записи заголовка, если None, то используется первая пустая строка.
        :type row: int, optional
        :return: None
        """
        # определяет номер строки
        row = self.get_first_empty_row(ws) if not row else row
        table_range: str = f'A{row}'
        ws_header = [ws_header] if isinstance(ws_header, str) else ws_header
        # записывает заголовок в таблицу
        ws.append_row(values=ws_header, table_range=table_range)

        table_range = f'{table_range}:E{row}'
        # применяет форматирование к заголовку
        self.render_header(ws, ws_header, table_range, 'MERGE_COLUMNS')

    def write_category_title(self, ws: Worksheet, ws_category_title: str | list, row: int = None) -> None:
        """
        Записывает заголовок категории.

        :param ws: Объект Worksheet, представляющий таблицу.
        :type ws: Worksheet
        :param ws_category_title: Заголовок категории (строка или список).
        :type ws_category_title: str | list
        :param row: Номер строки для записи заголовка категории, если None, то используется первая пустая строка.
        :type row: int, optional
        :return: None
        """
        table_range: str = f'B{row}'
        ws_category_title = [ws_category_title] if isinstance(ws_category_title, str) else ws_category_title
        # записывает заголовок категории
        ws.append_row(values=ws_category_title, table_range=table_range)
        merge_range = f'{table_range}:E{row}'
        # объединяет ячейки заголовка
        self.merge_range(ws, merge_range)

    def get_first_empty_row(self, ws: Worksheet, by_col: int = None) -> int:
        """
        Возвращает номер первой пустой строки в таблице.

        :param ws: Объект Worksheet, представляющий таблицу.
        :type ws: Worksheet
        :param by_col: Номер колонки для проверки (если None, то по всей таблице), по умолчанию None.
        :type by_col: int, optional
        :return: Номер первой пустой строки.
        :rtype: int
        """
        # получает список всех значений в колонке или во всей таблице
        str_list = list(filter(None, ws.col_values(1))) if by_col is None else list(filter(None, ws.get_all_values()))
        # возвращает номер первой пустой строки
        return len(str_list) + 1