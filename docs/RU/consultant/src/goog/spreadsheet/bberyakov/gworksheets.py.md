# Анализ кода модуля gworksheets

**Качество кода**

-  Соответствие требованиям по оформлению кода: 7/10
    -   Плюсы
        -   Используются docstring для описания классов и функций.
        -   Присутствует описание модуля.
        -   Используются type hints для параметров функций.
    -   Минусы
        -   Не используются одинарные кавычки в коде.
        -   Не все функции имеют полное описание в формате RST.
        -   Не используется `from src.logger.logger import logger` для логирования.
        -   Не везде используется `...` для обозначения точек остановки.
        -   Не все комментарии соответствуют требованию "подробное объяснение следующего блока кода"
        -   Используется `print` вместо `logger`.
        -   Импорт из `global_settingspread` не соответствует шаблону именования.
        -   Не все docstring соответсвуют стандарту.

**Рекомендации по улучшению**

1.  **Исправить кавычки**: Заменить двойные кавычки на одинарные в коде, за исключением операций вывода.
2.  **Добавить недостающие импорты**: Импортировать `logger` из `src.logger`.
3.  **Улучшить docstring**: Добавить полное описание в формате RST для всех функций и методов, включая описание параметров и возвращаемых значений.
4.  **Использовать `logger`**: Заменить `print` на `logger.info` или `logger.debug` для вывода сообщений.
5.  **Уточнить комментарии**: Комментарии должны более точно описывать, что делает код.
6.  **Удалить лишние комментарии**:  Удалить дублирующие комментарии которые не несут смысловой нагрузки.
7. **Согласовать импорт**: приведение импорта в соответсвие с ранее обработанными файлами.
8. **Соблюдать стандарты**: Привести имена переменных и функций в соответсвие с PEP8
9. **Улучшить форматирование**: Сделать отступы в соответствии со стандартом PEP8

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-

"""
Модуль для работы с Google Sheets через класс GWorksheet.
=========================================================================================

Этот модуль предоставляет класс `GWorksheet`, который расширяет функциональность
класса `Worksheet` и предоставляет инструменты для работы с Google Sheets.

Модуль включает в себя методы для создания, открытия, очистки и управления
листами Google Sheets, а также для установки направления текста и заголовков.

Пример использования
--------------------

Пример использования класса `GWorksheet`:

.. code-block:: python

    from src.goog.spreadsheet.bberyakov.gworksheets import GWorksheet
    from src.goog.gspreadsheet import GSpreadsheet

    # Инициализация объекта GSpreadsheet
    g_spreadsheet = GSpreadsheet(title='My Spreadsheet')

    # Инициализация объекта GWorksheet
    g_worksheet = GWorksheet(sh=g_spreadsheet, ws_title='My Worksheet')

    # Запись заголовка
    g_worksheet.header(world_title='Заголовок таблицы')

"""
from src.global_settingspread import Spreadsheet, Worksheet
from src.goog.grender import GSRender
from typing import Union
from src.logger.logger import logger  # Импорт logger


class GWorksheet(Worksheet):
    """
    Класс для работы с листами Google Sheets.

    :ivar sh: Объект Spreadsheet.
    :vartype sh: Spreadsheet
    :ivar ws: Объект Worksheet.
    :vartype ws: Worksheet
    :ivar render: Объект GSRender для отрисовки элементов листа.
    :vartype render: GSRender
    """
    sh: Spreadsheet = None
    ws: Worksheet = None
    render: GSRender = GSRender()

    def __init__(self, sh: Spreadsheet, ws_title: str = 'new', rows: int = None, cols: int = None,
                 direction: str = 'rtl', wipe_if_exist: bool = True, *args, **kwargs) -> None:
        """
        Инициализирует объект GWorksheet.

        :param sh: Объект Spreadsheet.
        :type sh: Spreadsheet
        :param ws_title: Название листа, defaults to 'new'.
        :type ws_title: str, optional
        :param rows: Количество строк, defaults to None.
        :type rows: int, optional
        :param cols: Количество колонок, defaults to None.
        :type cols: int, optional
        :param direction: Направление текста, defaults to 'rtl'.
        :type direction: str, optional
        :param wipe_if_exist: Очистить лист при открытии, defaults to True.
        :type wipe_if_exist: bool, optional
        :param args: Произвольные позиционные аргументы.
        :type args: tuple
        :param kwargs: Произвольные именованные аргументы.
        :type kwargs: dict
        :raises Exception: Если возникает ошибка при получении листа.
        """
        self.sh = sh
        #  Код вызывает метод get для получения или создания листа
        self.get(self.sh, ws_title, rows, cols, direction, wipe_if_exist)
        ...

    def get(self, sh: Spreadsheet, ws_title: str = 'new', rows: int = 100, cols: int = 100, direction: str = 'rtl',
            wipe_if_exist: bool = True) -> None:
        """
        Получает или создает лист в Google Sheets.

        Если `ws_title` равен 'new', создается новый лист.
        В противном случае, открывается существующий лист, или создается новый, если такой не существует.

        :param sh: Объект Spreadsheet.
        :type sh: Spreadsheet
        :param ws_title: Название листа, defaults to 'new'.
        :type ws_title: str, optional
        :param rows: Количество строк, defaults to 100.
        :type rows: int, optional
        :param cols: Количество колонок, defaults to 100.
        :type cols: int, optional
        :param direction: Направление текста, defaults to 'rtl'.
        :type direction: str, optional
        :param wipe_if_exist: Очистить лист при открытии, defaults to True.
        :type wipe_if_exist: bool, optional
        :raises Exception: Если возникает ошибка при работе с листом.
        """
        # Проверка, нужно ли создать новый лист
        if ws_title == 'new':
            # Код получает новый лист из объекта gsh
            self.ws = sh.gsh.get()
        else:
            # Код проверяет наличие листа с заданным именем
            if ws_title in [_ws.title for _ws in sh.gsh.worksheets()]:
                logger.info(f'worksheet {ws_title} already exist !')
                #  Код получает существующий лист из объекта gsh
                self.ws = sh.gsh.worksheet(ws_title)
                # Проверка, нужно ли очистить данные на листе
                if wipe_if_exist:
                    # Код очищает данные на листе
                    self.ws.clear()
            else:
                 # Код создает новый лист с заданными параметрами
                self.ws = sh.gsh.add_worksheet(ws_title, rows, cols)
                #  Комментарий: Новый лист с заданным именем создан

        # Код устанавливает направление текста на листе
        self.render.set_worksheet_direction(sh.gsh, self.ws, 'rtl')

    def header(self, world_title: str, range: str = 'A1:Z1',
               merge_type: str = 'MERGE_ALL') -> None:
        """
        Устанавливает заголовок на листе.

        :param world_title: Текст заголовка.
        :type world_title: str
        :param range: Диапазон ячеек для заголовка, defaults to 'A1:Z1'.
        :type range: str, optional
        :param merge_type: Тип объединения ячеек, defaults to 'MERGE_ALL'.
        :type merge_type: str, optional
        """
        # Код вызывает метод render для установки заголовка
        self.render.header(self.ws, world_title)

    def category(self, ws_category_title: str) -> None:
        """
        Записывает заголовок категории на листе.

        :param ws_category_title: Текст заголовка категории.
        :type ws_category_title: str
        """
        # Код вызывает метод render для записи заголовка категории
        self.render.write_category_title(self, ws_category_title)

    def direction(self, direction: str = 'rtl') -> None:
        """
        Устанавливает направление текста на листе.

        :param direction: Направление текста, defaults to 'rtl'.
        :type direction: str, optional
        """
        # Код устанавливает направление текста на листе
        self.render.set_worksheet_direction(sh=self.sh, ws=self, direction='rtl')