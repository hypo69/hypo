# Анализ кода модуля `gworksheets.py`

**Качество кода**
8
- Плюсы
    - Код структурирован в класс `GWorksheet`, наследующий от `Worksheet`, что способствует организации и переиспользованию кода.
    - Имеется базовая обработка создания и открытия листов.
    - Используется класс `GSRender` для рендеринга данных, что разделяет логику представления от логики управления листами.
    - Есть начальная документация, хотя и требует доработки.
- Минусы
    - Комментарии не соответствуют формату reStructuredText (RST).
    - Отсутствует обработка ошибок.
    - Не используются `j_loads` или `j_loads_ns` для чтения файлов, хотя в коде их нет, но в инструкции есть.
    - Не все функции документированы.
    - Есть неиспользуемый код.
    - Логирование ошибок отсутствует.
    - Есть лишние комментарии `#_ws = sh.add_worksheet()` которые надо удалить.
    - Нарушены PEP8.
    - Функция `direction` не использует переданный параметр `direction`

**Рекомендации по улучшению**

1.  **Документация**:
    -   Переписать все комментарии и docstring в формате reStructuredText (RST).
    -   Добавить подробные описания для всех функций, методов и классов.
    -   Указать типы параметров и возвращаемых значений в docstring.
2.  **Обработка ошибок**:
    -   Использовать `try-except` блоки и `logger.error` для обработки исключений.
    -   Удалить избыточные `try-except` блоки, где это возможно, и использовать логирование ошибок.
3.  **Импорты**:
    -   Добавить необходимые импорты, если они отсутствуют.
4.  **Код**:
    -   Удалить неиспользуемые и закомментированные строки кода.
    -   Исправить ошибки в логике и вызовах функций.
    -   Избегать избыточных комментариев, которые не добавляют понимания коду.
    -   Исправить неточность в функции `direction`
    -   Переименовать переменную `world_title` в `worksheet_title`
5.  **Логирование**:
    -   Использовать `from src.logger.logger import logger` для логирования ошибок.
    -   Логировать важные события и ошибки.

**Оптимизиробанный код**

```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
Модуль для работы с Google Sheets и их листами.
=========================================================================================

Этот модуль содержит класс :class:`GWorksheet`, который наследуется от :class:`Worksheet`
и предоставляет методы для создания, открытия и управления листами в Google Sheets.
Использует :class:`GSRender` для визуализации данных.

Пример использования
--------------------

Пример создания и использования класса `GWorksheet`:

.. code-block:: python

    from src.goog.spreadsheet.bberyakov.gworksheets import GWorksheet
    from src.goog.spreadsheet.bberyakov.global_settingspread import Spreadsheet

    sh = Spreadsheet(...) # Инициализация Spreadsheet
    gws = GWorksheet(sh, ws_title='MySheet', rows=100, cols=20)
    gws.header('Заголовок таблицы', range='A1:C1')
"""
from typing import Union
from src.goog.spreadsheet.bberyakov.global_settingspread import Spreadsheet, Worksheet
from src.goog.grender import GSRender
from src.logger.logger import logger


MODE = 'dev'


class GWorksheet(Worksheet):
    """
    Класс для работы с листами Google Sheets.

    Наследуется от :class:`Worksheet`.

    :ivar sh: Объект Spreadsheet для доступа к таблице.
    :vartype sh: Spreadsheet
    :ivar ws: Объект Worksheet, представляющий лист Google Sheets.
    :vartype ws: Worksheet
    :ivar render: Объект GSRender для рендеринга данных на листе.
    :vartype render: GSRender
    """
    sh = None
    ws: Worksheet = None
    render: GSRender = GSRender()

    def __init__(self, sh: Spreadsheet, ws_title: str = 'new', rows: int = None, cols: int = None,
                 direction: str = 'rtl', wipe_if_exist: bool = True, *args, **kwards) -> None:
        """
        Инициализирует объект GWorksheet.

        :param sh: Объект Spreadsheet.
        :type sh: Spreadsheet
        :param ws_title: Название листа. Если 'new', создает новый лист.
        :type ws_title: str, optional
        :param rows: Количество строк для нового листа.
        :type rows: int, optional
        :param cols: Количество колонок для нового листа.
        :type cols: int, optional
        :param direction: Направление листа ('rtl' или 'ltr').
        :type direction: str, optional
        :param wipe_if_exist: Очищать ли лист, если он уже существует.
        :type wipe_if_exist: bool, optional
        :param *args: Дополнительные аргументы.
        :param **kwards: Дополнительные ключевые аргументы.
        :raises Exception: Если не удалось получить или создать лист.
        """
        self.sh = sh
        try:
            self.get(self.sh, ws_title, rows, cols, direction, wipe_if_exist)
        except Exception as ex:
            logger.error(f'Ошибка при инициализации GWorksheet: {ex}')
            ...

    def get(self, sh: Spreadsheet, ws_title: str = 'new', rows: int = 100, cols: int = 100,
            direction: str = 'rtl', wipe_if_exist: bool = True) -> None:
        """
        Получает или создает лист в Google Sheets.

        Если `ws_title` равен 'new', создает новый лист. Иначе открывает существующий лист по названию.

        :param sh: Объект Spreadsheet.
        :type sh: Spreadsheet
        :param ws_title: Название листа.
        :type ws_title: str, optional
        :param rows: Количество строк для нового листа.
        :type rows: int, optional
        :param cols: Количество колонок для нового листа.
        :type cols: int, optional
        :param direction: Направление листа ('rtl' или 'ltr').
        :type direction: str, optional
        :param wipe_if_exist: Очищать ли лист, если он уже существует.
        :type wipe_if_exist: bool, optional
        :raises Exception: Если не удалось получить или создать лист.
        """
        try:
            if ws_title == 'new':
                self.ws = sh.gsh.get()
            else:
                if ws_title in [_ws.title for _ws in sh.gsh.worksheets()]:
                    logger.debug(f'Лист {ws_title} уже существует!')
                    self.ws = sh.gsh.worksheet(ws_title)
                    if wipe_if_exist:
                        self.ws.clear()
                else:
                    self.ws = sh.gsh.add_worksheet(ws_title, rows, cols)
                    logger.debug(f'Создан новый лист с названием {ws_title}')

            self.render.set_worksheet_direction(sh.gsh, self.ws, direction)
        except Exception as ex:
            logger.error(f'Ошибка при получении или создании листа: {ex}')
            ...

    def header(self, worksheet_title: str, range: str = 'A1:Z1',
               merge_type: str = 'MERGE_ALL') -> None:
        """
        Создает заголовок на листе.

        :param worksheet_title: Текст заголовка.
        :type worksheet_title: str
        :param range: Диапазон ячеек для заголовка.
        :type range: str, optional
        :param merge_type: Тип объединения ячеек.
        :type merge_type: str, optional
        """
        self.render.header(self.ws, worksheet_title, range, merge_type)

    def category(self, ws_category_title: str) -> None:
        """
        Записывает заголовок категории на лист.

        :param ws_category_title: Название категории.
        :type ws_category_title: str
        """
        self.render.write_category_title(self.ws, ws_category_title)

    def direction(self, direction: str = 'rtl') -> None:
        """
        Устанавливает направление листа.

        :param direction: Направление листа ('rtl' или 'ltr').
        :type direction: str, optional
        """
        self.render.set_worksheet_direction(sh=self.sh, ws=self.ws, direction=direction)