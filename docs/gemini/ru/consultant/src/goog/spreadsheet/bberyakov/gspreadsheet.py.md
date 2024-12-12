# Анализ кода модуля `gspreadsheet`

**Качество кода**

7/10
-   **Плюсы**
    *   Код структурирован в класс `GSpreadsheet`, наследующий от `Spreadsheet`, что способствует организации и повторному использованию кода.
    *   Используются аннотации типов, что улучшает читаемость и облегчает отладку.
    *   Используется библиотека `gspread` для взаимодействия с Google Sheets, что является хорошей практикой для работы с Google таблицами.
    *   Присутствует базовая документация в виде docstring для классов и методов.
    *   Код подключает файл с учетными данными Google сервисного аккаунта, что безопасно.

-   **Минусы**
    *   Не все комментарии соответствуют стандарту reStructuredText (RST), что затрудняет автоматическую генерацию документации.
    *   Некоторые комментарии дублируют друг друга и не несут дополнительной смысловой нагрузки.
    *   Отсутствует обработка исключений при работе с Google Sheets, что может привести к неожиданным сбоям.
    *   Использование `json.loads` напрямую из файла не соответствует требованиям инструкции, необходимо использовать `j_loads`.
    *   Много закомментированного кода, который следует убрать, так как он не добавляет ценности и только затрудняет чтение.
    *   Не везде реализовано логирование ошибок.
    *   Импорт `Spreadsheet` и `service_account` осуществляется через `global_settingspread`, не ясно откуда он берется.
    *   Необходимо добавить логирование.
    *   Отсутствует проверка на то, является ли `self.gsh` валидным объектом, перед тем как с ним взаимодействовать.
    *   Переопределение `self.gclient` в `__init__` может вызвать неочевидные проблемы, лучше инициализировать его один раз.

**Рекомендации по улучшению**

1.  **Документация**:
    *   Переписать все docstring и комментарии в формате RST.
    *   Добавить более подробные описания для каждого метода, класса, модуля и параметра.

2.  **Импорты**:
    *   Проверить и добавить необходимые импорты.
    *   Удалить неиспользуемые импорты.
    *   Импортировать `j_loads` или `j_loads_ns` из `src.utils.jjson`.
    *   Импортировать `logger` из `src.logger.logger`.

3.  **Обработка ошибок**:
    *   Добавить обработку исключений при работе с Google Sheets, логируя их с помощью `logger.error`.
    *   Избегать общих `try-except` блоков, ловить конкретные исключения.

4.  **Работа с JSON**:
    *   Использовать `j_loads` из `src.utils.jjson` для чтения JSON файлов.

5.  **Улучшение кода**:
    *   Удалить закомментированный код.
    *   Добавить проверки на валидность данных.
    *   Инициализировать `self.gclient` только один раз.
    *   Добавить логирование действий.

6. **Структура кода**:
    *  Удалить лишние комментарии, типа `[Class\'s description]`, которые не несут никакой информации
    *  Удалить повторяющиеся коментарии и описания.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
Модуль для работы с Google Sheets.
=========================================================================================

Этот модуль предоставляет класс :class:`GSpreadsheet`, который используется для взаимодействия
с Google Sheets API. Он позволяет создавать, открывать и управлять таблицами Google Sheets.

Пример использования
--------------------

Пример использования класса `GSpreadsheet`:

.. code-block:: python

    from src.goog.spreadsheet.bberyakov.gspreadsheet import GSpreadsheet

    spreadsheet = GSpreadsheet(s_id='your_spreadsheet_id')
    # Или
    spreadsheet = GSpreadsheet(s_title='Your Spreadsheet Title')
"""

from src.global_settingspread import Spreadsheet, service_account
from typing import List, Type, Union
from src.utils.jjson import j_loads
from src.logger.logger import logger
import gspread


MODE = 'dev'


class GSpreadsheet(Spreadsheet):
    """
    Класс для управления Google Sheets.

    :param s_id: ID таблицы Google Sheets.
    :type s_id: str, optional
    :param s_title: Заголовок таблицы Google Sheets.
    :type s_title: str, optional
    """

    gsh: Spreadsheet = None
    gclient = None

    def __init__(self, s_id: str = None, s_title: str = None, *args, **kwards):
        """
        Инициализация экземпляра класса GSpreadsheet.

        :param s_id: ID таблицы Google Sheets.
        :type s_id: str, optional
        :param s_title: Заголовок таблицы Google Sheets.
        :type s_title: str, optional
        :param \*args: Произвольные позиционные аргументы.
        :param \*\*kwards: Произвольные именованные аргументы.
        """
        secret_file = 'goog/onela-hypotez-1aafa5e5d1b5.json'
        try:
            # Код инициализирует клиента Google Sheets API с использованием сервисного аккаунта
            self.gclient = service_account(filename=secret_file)
        except Exception as ex:
            # Код логирует ошибку инициализации клиента Google Sheets API
            logger.error(f'Ошибка инициализации клиента Google Sheets API: {ex}')
            return

        if s_id:
            try:
                # Код получает таблицу по ее ID
                self.gsh = self.get_by_id(s_id)
            except Exception as ex:
                # Код логирует ошибку при получении таблицы по ID
                logger.error(f'Ошибка получения таблицы по ID: {s_id} - {ex}')
        if s_title:
            try:
                # Код получает таблицу по ее заголовку
                self.gsh = self.get_by_title(s_title)
            except Exception as ex:
                # Код логирует ошибку при получении таблицы по заголовку
                logger.error(f'Ошибка получения таблицы по заголовку: {s_title} - {ex}')

    def get_project_spreadsheets_dict(self) -> dict:
        """
        Загружает словарь с настройками таблиц из JSON файла.

        :return: Словарь с настройками таблиц.
        :rtype: dict
        """
        try:
            # Код загружает JSON файл со списком таблиц.
            # TODO: Заменить на `j_loads`
            with open('goog/spreadsheets.json', 'r', encoding='utf-8') as f:
                data = j_loads(f)
            return data
        except Exception as ex:
            # Код логирует ошибку при загрузке словаря с настройками таблиц
            logger.error(f'Ошибка загрузки словаря с настройками таблиц: {ex}')
            return {}

    def get_by_title(self, sh_title: str = 'New Spreadsheet'):
        """
        Создает или открывает таблицу Google Sheets по ее заголовку.

        :param sh_title: Заголовок таблицы.
        :type sh_title: str
        """
        if not self.gclient:
            logger.error('Клиент Google Sheets не инициализирован')
            return

        try:
            # Код проверяет, существует ли таблица с указанным именем
            all_spreadsheets = self.gclient.openall()
            if sh_title not in [sh.title for sh in all_spreadsheets]:
                # Код создает новую таблицу если ее не существует
                new_spreadsheet = self.gclient.create(sh_title)
                # Код делится правами на таблицу с указанным пользователем
                new_spreadsheet.share('d07708766@gmail.com', perm_type='user', role='writer')
                self.gsh = new_spreadsheet
                logger.info(f'Создана новая таблица с именем: {sh_title}')
            else:
                # Код открывает существующую таблицу
                self.gsh = self.gclient.open(sh_title)
                logger.info(f'Таблица с именем {sh_title} уже существует')
        except Exception as ex:
             # Код логирует ошибку при открытии или создании таблицы
            logger.error(f'Ошибка при создании или открытии таблицы {sh_title}: {ex}')

    def get_by_id(self, sh_id: str) -> Spreadsheet:
        """
        Открывает таблицу Google Sheets по ее ID.

        :param sh_id: ID таблицы.
        :type sh_id: str
        :return: Объект Spreadsheet.
        :rtype: Spreadsheet
        """
        if not self.gclient:
            logger.error('Клиент Google Sheets не инициализирован')
            return None
        try:
            # Код открывает таблицу по ее ID
            spreadsheet = self.gclient.open_by_key(sh_id)
            return spreadsheet
        except Exception as ex:
            # Код логирует ошибку при открытии таблицы по ID
            logger.error(f'Ошибка при открытии таблицы по ID {sh_id}: {ex}')
            return None

    def get_all_spreadsheets_for_current_account(self):
        """
        Получает все таблицы Google Sheets текущего аккаунта.

        :return: Список объектов Spreadsheet.
        :rtype: list
        """
        if not self.gclient:
            logger.error('Клиент Google Sheets не инициализирован')
            return []
        try:
            # Код получает список всех таблиц аккаунта
            return self.gclient.openall()
        except Exception as ex:
             # Код логирует ошибку при получении списка таблиц
            logger.error(f'Ошибка при получении списка таблиц: {ex}')
            return []