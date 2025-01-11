## Анализ кода модуля gspreadsheet

**Качество кода**
9
-  Плюсы
    - Код структурирован в класс `GSpreadsheet`, наследующий `Spreadsheet`, что способствует модульности.
    - Присутствует начальная документация модуля и классов, хоть и не полная.
    - Используется `service_account` для аутентификации, что является безопасным способом.
    - Код соответствует PEP8.
    - Использованы комментарии.
-  Минусы
    -  Отсутствует docstring для методов.
    -  Некорректное использование тройных кавычек для docstring внутри модуля.
    -  Не используются `j_loads` или `j_loads_ns` для чтения JSON.
    -  Присутствуют лишние импорты и неиспользуемые переменные.
    -  Не используется `from src.logger.logger import logger`.
    -  Дублирование комментариев `[Function's description]`.

**Рекомендации по улучшению**

1. **Документация**:
    - Добавить docstring в формате RST для всех методов и класса `GSpreadsheet`.
    - Использовать более конкретные описания для параметров и возвращаемых значений.
    - Избавиться от дублирования комментариев `[Function's description]`.
2. **Импорты**:
    - Удалить неиспользуемые импорты `gs` и `from global_settings import GWorksheet`.
    - Использовать `from src.utils.jjson import j_loads` для чтения JSON файла.
    -  Использовать `from src.logger.logger import logger` для логирования.
3. **Логирование**:
    - Добавить обработку ошибок с помощью `logger.error`, там где это необходимо.
4. **Структура кода**:
    - Инициализация `self.gsh` и `self.gclient` должна быть в `__init__`.
    -  Упростить проверку существования файла, исключив чтение из json
5. **Форматирование**:
    - Использовать одинарные кавычки для строк в коде, двойные только для вывода.
    -  Исправить docstring, удалить лишние символы и комментарии.
6. **Использование**
    - Исключить инициализацию `self.gsh = None` при объявлении класса.
    - Исключить использование `print` использовать `logger`.

**Оптимизиробанный код**

```python
# -*- coding: utf-8 -*-

#! venv/bin/python/python3.12

"""
Модуль для работы с Google Sheets API.
=========================================================================================

Этот модуль предоставляет класс :class:`GSpreadsheet`, который используется для
взаимодействия с Google Sheets API для выполнения операций с электронными таблицами.
Включает методы для создания, открытия и управления таблицами, а также для
получения информации об аккаунте.

Пример использования
--------------------

Пример создания и открытия таблицы:

.. code-block:: python

    from src.goog.spreadsheet.bberyakov.gspreadsheet import GSpreadsheet

    spreadsheet = GSpreadsheet(s_title='My New Spreadsheet')
    #или
    spreadsheet = GSpreadsheet(s_id = '1ZcK74BCgWKVr4kODjPmSvjp5IyO0OxhXdbeHKWzLQiM')
"""

from global_settingspread import Spreadsheet, service_account
import gspread
from typing import List, Type, Union
from src.utils.jjson import j_loads
from src.logger.logger import logger
import os


class GSpreadsheet(Spreadsheet):
    """
    Класс для работы с Google Sheets.

    Предоставляет методы для создания, открытия и управления таблицами Google Sheets.

    Args:
        s_id (str, optional): Идентификатор таблицы.
        s_title (str, optional): Название таблицы.

    Attributes:
        gsh (gspread.Spreadsheet): Объект таблицы Google Sheets.
        gclient (gspread.Client): Клиент Google Sheets API.
    """
    gclient: gspread.client = None
    
    def __init__(self, s_id: str = None, s_title: str = None, *args, **kwards):
        """
        Инициализирует объект GSpreadsheet.

        Args:
            s_id (str, optional): Идентификатор таблицы.
            s_title (str, optional): Название таблицы.
            *args: Произвольные позиционные аргументы.
            **kwards: Произвольные ключевые аргументы.
        """
        #  Инициализация клиента Google Sheets API с использованием сервисного аккаунта
        secret_file = f'goog/onela-hypotez-1aafa5e5d1b5.json'
        self.gclient = service_account(filename = secret_file)
        
        if s_id:
             # Получение таблицы по идентификатору, если он передан
            self.gsh = self.get_by_id(s_id)
        elif s_title:
            # Получение таблицы по названию, если оно передано
            self.gsh = self.get_by_title(s_title)

    def get_project_spreadsheets_dict(self) -> dict:
        """
        Получает словарь с данными о таблицах из JSON файла.

        Returns:
            dict: Словарь с данными о таблицах.
        """
        # Получение пути к файлу с настройками таблиц
        file_path = 'goog/spreadsheets.json'
        
        # Проверка существования файла
        if not os.path.exists(file_path):
            logger.error(f"Файл настроек '{file_path}' не найден")
            return {}

        # Чтение данных из JSON файла с помощью j_loads
        try:
            with open(file_path, 'r', encoding = 'utf-8') as file:
                 return j_loads(file)
        except Exception as ex:
              logger.error(f"Ошибка чтения файла '{file_path}'", exc_info=True)
              return {}

    def get_by_title(self, sh_title: str = 'New Spreadsheet'):
        """
        Открывает или создает таблицу по ее названию.

        Если таблица с указанным названием существует, открывает ее.
        Если не существует, создает новую таблицу с указанным названием
        и предоставляет доступ для редактирования пользователю 'd07708766@gmail.com'.

        Args:
            sh_title (str, optional): Название таблицы. По умолчанию 'New Spreadsheet'.
        """
        # Проверяет, существует ли таблица с указанным названием среди всех таблиц
        if sh_title not in [sh.title for sh in self.gclient.openall()]:
            # Создание новой таблицы с заданным именем
            try:
                self.gsh = self.gclient.create(sh_title)
                # Предоставление доступа для редактирования пользователю
                self.gsh.share('d07708766@gmail.com', perm_type='user', role='writer')
                logger.info(f"Таблица '{sh_title}' успешно создана.")
            except Exception as ex:
               logger.error(f"Ошибка при создании таблицы '{sh_title}'", exc_info=True)
        else:
            # Открытие существующей таблицы с заданным именем
            try:
               self.gsh = self.gclient.open(sh_title)
               logger.info(f"Таблица '{sh_title}' успешно открыта.")
            except Exception as ex:
                logger.error(f"Ошибка при открытии таблицы '{sh_title}'", exc_info=True)


    def get_by_id(self, sh_id: str) -> gspread.Spreadsheet:
        """
        Открывает таблицу по ее идентификатору.

        Args:
            sh_id (str): Идентификатор таблицы.

        Returns:
            gspread.Spreadsheet: Объект открытой таблицы.
        """
        #  Открывает таблицу по ее идентификатору и возвращает объект таблицы
        try:
            return self.gclient.open_by_key(sh_id)
        except Exception as ex:
            logger.error(f"Ошибка при открытии таблицы с id '{sh_id}'", exc_info = True)
            return None

    def get_all_spreadsheets_for_current_account(self) -> List[gspread.Spreadsheet]:
        """
        Получает список всех таблиц текущего аккаунта.

        Returns:
            List[gspread.Spreadsheet]: Список всех таблиц аккаунта.
        """
        # Возвращает список всех таблиц текущего аккаунта
        try:
            return self.gclient.openall()
        except Exception as ex:
            logger.error("Ошибка при получении списка всех таблиц аккаунта", exc_info = True)
            return []