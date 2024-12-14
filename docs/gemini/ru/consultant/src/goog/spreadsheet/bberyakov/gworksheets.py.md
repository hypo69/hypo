# Анализ кода модуля `gworksheets.py`

**Качество кода**
7
-  Плюсы
    - Код структурирован в класс `GWorksheet`, наследующий от `Worksheet`.
    - Имеется базовая функциональность для работы с Google Sheets, включая создание, открытие и очистку листов.
    - Используется класс `GSRender` для отрисовки данных в таблице.
-  Минусы
    - Не все docstring соответствуют стандарту reStructuredText.
    - Отсутствует импорт необходимых модулей (например, `logger` из `src.logger.logger`).
    - Есть дублирование кода и неэффективное использование переменных (например, `sh.gsh` обращение к одному и тому же объекту несколько раз).
    - Некоторые комментарии не полные и не соответствуют reStructuredText.
    -  Отсутствует обработка ошибок.
    -  Не везде используется логирование.
    -  Используются `print` вместо `logger`.

**Рекомендации по улучшению**
1.  **Импорты**: Добавить недостающие импорты, такие как `logger` из `src.logger.logger`.
2.  **Docstrings**: Переписать docstring в формате RST, включая описания параметров и возвращаемых значений, а также модуля и класса.
3.  **Логирование**: Использовать `logger.error` вместо `try-except` и `print` для обработки и логирования ошибок.
4.  **Рефакторинг**: Убрать дублирование кода и оптимизировать обращения к объектам.
5.  **Комментарии**:  Комментарии должны быть информативными, написаны в формате reStructuredText и объяснять назначение следующего за ними блока кода.
6.  **Улучшение функции `get`:** Код можно сделать более читаемым за счет вынесения повторяющихся операций обращения к `sh.gsh` в отдельную переменную.
7.  **Использовать константы:** Для параметров `rtl` лучше использовать константы, вместо дублирования значений.

**Оптимизированный код**
```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
Модуль для работы с Google Sheets Worksheet.
=====================================================

Этот модуль предоставляет класс :class:`GWorksheet`, который наследует от :class:`Worksheet`
и используется для управления листами (worksheets) в Google Sheets.

Он включает функции для создания, открытия и очистки листов, а также для установки
направления текста и форматирования заголовков.

Пример использования:
--------------------

.. code-block:: python

    sh = ... # экземпляр Spreadsheet
    ws = GWorksheet(sh, ws_title='MySheet', rows=100, cols=20, wipe_if_exist=True)
    ws.header('Заголовок таблицы')
"""
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12
MODE = 'dev'

from global_settingspread import Spreadsheet, Worksheet
from goog.grender import GSRender
from typing import Union
from src.logger.logger import logger  # Импорт logger

RTL = 'rtl'

class GWorksheet(Worksheet):
    """
    Класс для управления листами в Google Sheets.

    Наследует от :class:`Worksheet` и предоставляет методы для создания, открытия,
    очистки, установки направления текста и форматирования заголовков листов.

    :ivar sh: Экземпляр Spreadsheet.
    :vartype sh: Spreadsheet
    :ivar ws: Экземпляр Worksheet.
    :vartype ws: Worksheet
    :ivar render: Экземпляр GSRender для отрисовки данных.
    :vartype render: GSRender
    """
    sh = None
    ws: Worksheet = None
    render: GSRender = GSRender()

    def __init__(self, sh, ws_title: str = 'new', rows: int = None, cols: int = None, direction: str = RTL, wipe_if_exist: bool = True, *args, **kwards) -> None:
        """
        Инициализирует объект GWorksheet.

        :param sh: Экземпляр Spreadsheet.
        :type sh: Spreadsheet
        :param ws_title: Название листа. По умолчанию 'new'.
        :type ws_title: str
        :param rows: Количество строк. По умолчанию None.
        :type rows: int
        :param cols: Количество столбцов. По умолчанию None.
        :type cols: int
        :param direction: Направление текста. По умолчанию 'rtl'.
        :type direction: str
        :param wipe_if_exist: Очищать ли лист, если он существует. По умолчанию True.
        :type wipe_if_exist: bool
        :param args: Произвольные позиционные аргументы.
        :type args: tuple
        :param kwards: Произвольные именованные аргументы.
        :type kwards: dict
        :raises Exception: Если возникает ошибка при инициализации.
        """
        try:
            self.sh = sh
            self.get(self.sh, ws_title, rows, cols, direction, wipe_if_exist)
            ...
        except Exception as ex:
            logger.error(f'Ошибка при инициализации GWorksheet: {ex}')
            ...

    def get(self, sh, ws_title: str = 'new', rows: int = 100, cols: int = 100, direction: str = RTL, wipe_if_exist: bool = True):
        """
        Получает или создает лист в Google Sheets.

        Если `ws_title` равен 'new', создает новый лист.
        В противном случае, открывает существующий лист или создает новый,
        если такого листа нет.

        :param sh: Экземпляр Spreadsheet.
        :type sh: Spreadsheet
        :param ws_title: Название листа. По умолчанию 'new'.
        :type ws_title: str
        :param rows: Количество строк для нового листа. По умолчанию 100.
        :type rows: int
        :param cols: Количество столбцов для нового листа. По умолчанию 100.
        :type cols: int
        :param direction: Направление текста. По умолчанию 'rtl'.
        :type direction: str
        :param wipe_if_exist: Очищать ли лист, если он существует. По умолчанию True.
        :type wipe_if_exist: bool
        :raises Exception: Если возникает ошибка при получении листа.
        """
        try:
            gsh = sh.gsh # Сохранение объекта gsh в переменную для избежания повторных обращений.
            if ws_title == 'new':
                self.ws = gsh.get() # Создание нового листа, если ws_title равен 'new'
            else:
                if ws_title in [_ws.title for _ws in gsh.worksheets()]:  # Проверка на существование листа
                    logger.info(f'Лист {ws_title} уже существует!')
                    self.ws = gsh.worksheet(ws_title)  # Открываем существующий лист
                    if wipe_if_exist:
                        self.ws.clear() # Очищаем лист, если wipe_if_exist установлен в True
                else:
                    self.ws = gsh.add_worksheet(ws_title, rows, cols) # Создание нового листа, если лист с таким именем не существует
                    logger.info(f'Создан новый лист с именем {ws_title}!')

            self.render.set_worksheet_direction(gsh, self.ws, RTL) # Установка направления текста для листа
        except Exception as ex:
            logger.error(f'Ошибка при получении листа: {ex}')
            ...


    def header(self, world_title: str, range: str = 'A1:Z1', merge_type: str = 'MERGE_ALL') -> None:
        """
        Устанавливает заголовок для листа.

        :param world_title: Текст заголовка.
        :type world_title: str
        :param range: Диапазон ячеек для заголовка. По умолчанию 'A1:Z1'.
        :type range: str
        :param merge_type: Тип объединения ячеек. По умолчанию 'MERGE_ALL'.
        :type merge_type: str
        """
        try:
            self.render.header(self.ws, world_title, range, merge_type) # Вызов метода render для установки заголовка
        except Exception as ex:
            logger.error(f'Ошибка при установке заголовка: {ex}')
            ...

    def category(self, ws_category_title):
        """
        Устанавливает заголовок категории.

        :param ws_category_title: Текст заголовка категории.
        :type ws_category_title: str
        :raises Exception: Если возникает ошибка при записи заголовка категории.
        """
        try:
            self.render.write_category_title(self.ws, ws_category_title) # Вызов метода render для записи заголовка категории
        except Exception as ex:
             logger.error(f'Ошибка при установке категории: {ex}')
             ...

    def direction(self, direction: str = RTL):
        """
        Устанавливает направление текста для листа.

        :param direction: Направление текста. По умолчанию 'rtl'.
        :type direction: str
        :raises Exception: Если возникает ошибка при установке направления.
        """
        try:
            self.render.set_worksheet_direction(sh = self.sh, ws = self.ws, direction = direction) # Вызов метода render для установки направления текста
        except Exception as ex:
            logger.error(f'Ошибка при установке направления текста: {ex}')
            ...