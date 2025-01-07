## Анализ кода модуля `gworksheets.py`

**Качество кода**
- **Соответствие требованиям**: 7/10
    - **Плюсы:**
        - Код в целом структурирован и выполняет заявленные функции.
        - Присутствует разделение на классы и методы, что улучшает читаемость.
        - Используется класс `GSRender` для отрисовки, что соответствует принципу разделения ответственности.
    - **Минусы:**
        - Отсутствует полная документация в формате reStructuredText (RST).
        - Использование стандартного `print` для вывода сообщений вместо логирования.
        - Не все комментарии достаточно информативны или соответствуют стандарту RST.
        - Не используется `j_loads` или `j_loads_ns` из `src.utils.jjson`.
        - Присутствует избыточное использование `...` как точек остановки.
        - Не все методы класса `GWorksheet` имеют docstring.
        - В некоторых местах код можно сделать более лаконичным и читаемым.
        - Присутсвует дублирование кода в функциях `get` и `direction`.

**Рекомендации по улучшению**
1. **Документация**:
    - Добавить docstring в формате RST для всех классов, методов и переменных, включая описание параметров и возвращаемых значений.
    - Переписать все существующие комментарии в формате RST, если это необходимо.
2. **Логирование**:
    - Заменить `print` на логирование с помощью `from src.logger.logger import logger`.
    - Добавить логирование ошибок и отладочные сообщения.
3. **Использование `j_loads`**:
    - Убедиться, что для чтения файлов используется `j_loads` или `j_loads_ns` из `src.utils.jjson`, если это необходимо.
4. **Удаление точек остановки**:
    - Избегать использования `...` в коде.
5. **Обработка ошибок**:
     - Избегать использования стандартных блоков `try-except`, и логировать ошибки через `logger.error`.
6. **Рефакторинг**:
    - Устранить дублирование кода в методах `get` и `direction`, выделив общие операции в отдельные функции.
    - Избегать избыточного использования переменных `_ws`.

**Оптимизированный код**
```python
# -*- coding: utf-8 -*-

#! venv/bin/python/python3.12

"""
Модуль для работы с Google Sheets API.
=========================================================================================

Этот модуль предоставляет класс :class:`GWorksheet`, который упрощает взаимодействие
с Google Sheets API для создания, открытия и управления листами (worksheets) в
электронных таблицах. Класс также включает методы для установки направления текста
и добавления заголовков.

Пример использования
--------------------

Пример создания и настройки нового листа:

.. code-block:: python

    from global_settingspread import Spreadsheet
    from goog.spreadsheet.bberyakov.gworksheets import GWorksheet

    spreadsheet = Spreadsheet(file_name='my_spreadsheet.json')
    gws = GWorksheet(spreadsheet, ws_title='My New Sheet', rows=150, cols=50)
    gws.header('My Sheet Header', range='A1:F1')

"""


from global_settingspread import Spreadsheet, Worksheet
from goog.grender import GSRender
from typing import Union
from src.logger.logger import logger # импортируем logger


class GWorksheet(Worksheet):
    """
    Класс для работы с листом Google Таблиц.

    Предоставляет методы для создания, открытия, настройки направления текста
    и добавления заголовков в листы Google Таблиц.

    :ivar sh: Объект Spreadsheet.
    :vartype sh: Spreadsheet
    :ivar ws: Объект Worksheet.
    :vartype ws: Worksheet
    :ivar render: Объект GSRender для отрисовки элементов.
    :vartype render: GSRender
    """
    sh = None
    ws: Worksheet = None
    render: GSRender = GSRender()

    def __init__(self, sh: Spreadsheet, ws_title: str = 'new', rows: int = None, cols: int = None,
                 direction: str = 'rtl', wipe_if_exist: bool = True, *args, **kwards) -> None:
        """
        Инициализация объекта GWorksheet.

        :param sh: Объект Spreadsheet.
        :type sh: Spreadsheet
        :param ws_title: Название листа.
        :type ws_title: str, optional
        :param rows: Количество строк листа.
        :type rows: int, optional
        :param cols: Количество столбцов листа.
        :type cols: int, optional
        :param direction: Направление текста ('rtl' или 'ltr').
        :type direction: str, optional
        :param wipe_if_exist: Очистить лист при открытии, если существует.
        :type wipe_if_exist: bool, optional
        :param args: Дополнительные позиционные аргументы.
        :type args: tuple
        :param kwards: Дополнительные именованные аргументы.
        :type kwards: dict
        :raises Exception: Если не удалось получить лист.
        """
        self.sh = sh
        try:
            self.get(sh, ws_title, rows, cols, direction, wipe_if_exist)
        except Exception as ex:
           logger.error(f'Ошибка при инициализации GWorksheet: {ex}')
        

    def _get_worksheet(self, sh: Spreadsheet, ws_title: str, rows: int, cols: int, wipe_if_exist: bool) -> Worksheet:
        """
        Получение или создание листа Google Таблиц.

        :param sh: Объект Spreadsheet.
        :type sh: Spreadsheet
        :param ws_title: Название листа.
        :type ws_title: str
        :param rows: Количество строк листа.
        :type rows: int
        :param cols: Количество столбцов листа.
        :type cols: int
        :param wipe_if_exist: Очистить лист при открытии, если существует.
        :type wipe_if_exist: bool
        :return: Объект Worksheet.
        :rtype: Worksheet
        :raises Exception: Если не удалось получить или создать лист.
        """
        if ws_title == 'new':
            try:
                ws = sh.gsh.get()
                return ws
            except Exception as ex:
                logger.error(f'Не удалось получить новый лист: {ex}')
                raise
        else:
            try:
                if ws_title in [ws.title for ws in sh.gsh.worksheets()]:
                    logger.info(f'Лист {ws_title} уже существует.')
                    ws = sh.gsh.worksheet(ws_title)
                    if wipe_if_exist:
                        ws.clear()
                    return ws
                else:
                    ws = sh.gsh.add_worksheet(ws_title, rows, cols)
                    logger.info(f'Создан новый лист: {ws_title}')
                    return ws
            except Exception as ex:
                logger.error(f'Ошибка при получении или создании листа {ws_title}: {ex}')
                raise
                
    def get(self, sh: Spreadsheet, ws_title: str = 'new', rows: int = 100, cols: int = 100, direction: str = 'rtl',
            wipe_if_exist: bool = True) -> None:
        """
        Получение или создание листа Google Таблиц.

        Если `ws_title` равно 'new', создается новый лист.
        Иначе, открывается существующий лист с названием `ws_title`.
        Если лист существует и `wipe_if_exist` True, то лист очищается от старых данных.

        :param sh: Объект Spreadsheet.
        :type sh: Spreadsheet
        :param ws_title: Название листа.
        :type ws_title: str, optional
        :param rows: Количество строк листа.
        :type rows: int, optional
        :param cols: Количество столбцов листа.
        :type cols: int, optional
        :param direction: Направление текста ('rtl' или 'ltr').
        :type direction: str, optional
        :param wipe_if_exist: Очистить лист при открытии, если существует.
        :type wipe_if_exist: bool, optional
        :raises Exception: Если не удалось получить или создать лист.
        """
        try:
            self.ws = self._get_worksheet(sh, ws_title, rows, cols, wipe_if_exist)
        except Exception as ex:
             logger.error(f'Ошибка при получении листа: {ex}')
             return
             
        self.render.set_worksheet_direction(sh.gsh, self.ws, direction)

    def header(self, world_title: str, range: str = 'A1:Z1',
               merge_type: str = 'MERGE_ALL') -> None:
        """
        Установка заголовка листа.

        :param world_title: Текст заголовка.
        :type world_title: str
        :param range: Диапазон ячеек для заголовка.
        :type range: str, optional
        :param merge_type: Тип объединения ячеек.
        :type merge_type: str, optional
        """
        self.render.header(self.ws, world_title, range, merge_type)

    def category(self, ws_category_title: str) -> None:
        """
        Запись заголовка категории.

        :param ws_category_title: Заголовок категории.
        :type ws_category_title: str
        """
        self.render.write_category_title(self, ws_category_title)

    def direction(self, direction: str = 'rtl') -> None:
        """
        Установка направления текста листа.

        :param direction: Направление текста ('rtl' или 'ltr').
        :type direction: str, optional
        """
        self.render.set_worksheet_direction(self.sh.gsh, self.ws, direction)