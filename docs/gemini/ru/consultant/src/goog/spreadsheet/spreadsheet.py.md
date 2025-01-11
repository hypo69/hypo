# Анализ кода модуля `spreadsheet.py`

**Качество кода**
8
-  Плюсы
    -  Код имеет базовую структуру для работы с Google Sheets API.
    -  Используется библиотека `gspread` для взаимодействия с Google Sheets.
    -  Присутствует обработка исключений с использованием логгера.
    -  Есть методы для создания, получения и копирования листов, а также загрузки данных из CSV.
-  Минусы
    -  Не все методы имеют подробную документацию в формате RST.
    -  В некоторых местах используется обработка исключений `try-except` без конкретного логирования ошибки.
    -  Отсутствует проверка аргументов.
    -  Не используется `j_loads` или `j_loads_ns` для чтения данных.
    -  Не везде используется f-строки.
    -  Не используются статические переменные, `SCOPES` должна быть `tuple`.
    -  В инициализаторе нет обработки `spreadsheet_name` если не указан `spreadsheet_id`
    -  Не используются аннотации типов для всех переменных.

**Рекомендации по улучшению**
1. Добавить недостающие импорты и убедиться, что все импорты соответствуют ранее обработанным файлам.
2. Переписать все docstring в соответствии с форматом RST.
3. Уточнить обработку ошибок, добавляя более подробные сообщения в логгер.
4. Избавиться от избыточных `try-except` блоков, используя `logger.error` там, где это уместно.
5. Добавить валидацию аргументов при инициализации.
6. Использовать `j_loads` или `j_loads_ns` при чтении файлов, если это требуется.
7. Привести имена переменных и функций в соответствие с остальным кодом.
8. Добавить статические переменные.
9. Добавить аннотацию типов.
10. Добавить f-строки.
11. Добавить обработку `spreadsheet_name` если не указан `spreadsheet_id`

**Оптимизированный код**
```python
# -*- coding: utf-8 -*-
"""
Модуль для работы с Google Sheets.
=========================================================================================

Этот модуль содержит класс :class:`SpreadSheet`, который используется для взаимодействия с Google Sheets API,
создания и управления электронными таблицами, а также загрузки данных из CSV-файлов.

Пример использования
--------------------

Пример использования класса `SpreadSheet`:

.. code-block:: python

    from pathlib import Path

    data_file = Path('/mnt/data/google_extracted/your_data_file.csv')  # Замените на путь к вашему файлу
    sheet_name = 'Sheet1'  # Замените на имя листа в Google Sheets

    # Создание нового документа Google Sheets, если spreadsheet_id не указан
    google_sheet_handler = SpreadSheet(
        spreadsheet_id=None,  # Укажите None для создания нового
        sheet_name=sheet_name,
        spreadsheet_name='My New Spreadsheet'  # Имя нового документа Google Sheets
    )
    google_sheet_handler.upload_data_to_sheet()
"""
from pathlib import Path
import gspread
from gspread import Spreadsheet, Worksheet
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
from src.logger.logger import logger
from src import gs
from src.utils.printer import pprint
from typing import  Any


class SpreadSheet:
    """
    Класс для работы с Google Sheets.

    Этот класс предоставляет основные методы для доступа к Google Sheets API, создания и управления таблицами,
    а также загрузки данных из CSV-файла в Google Sheets.

    :ivar spreadsheet_id: ID таблицы Google Sheets.
    :vartype spreadsheet_id: str | None
    :ivar spreadsheet_name: Имя новой таблицы Google Sheets.
    :vartype spreadsheet_name: str | None
    :ivar spreadsheet: Объект таблицы Google Sheets.
    :vartype spreadsheet: Spreadsheet
    :ivar data_file: Путь к CSV файлу с данными.
    :vartype data_file: Path
    :ivar sheet_name: Имя листа в Google Sheets.
    :vartype sheet_name: str
    :ivar credentials: Учетные данные для доступа к Google Sheets API.
    :vartype credentials: ServiceAccountCredentials
    :ivar client: Клиент для работы с Google Sheets API.
    :vartype client: gspread.Client
    :ivar worksheet: Рабочий лист Google Sheets.
    :vartype worksheet: Worksheet
    :ivar create_sheet: Флаг для создания нового листа.
    :vartype create_sheet: bool
    """
    SCOPES: tuple = ('https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive')
    #creds_file = gs.path.root / 'secrets' / 'hypo69-c32c8736ca62.json'
    #  оригинал файла хранится в базе данных вместе с паролями
    #  @todo организовать копирование файла в прогамно созаданом `tmp`,чтобы не хранить файл в физической директории
    # Class variable declarations
    spreadsheet_id: str | None
    spreadsheet_name: str | None
    spreadsheet: Spreadsheet
    data_file: Path | None
    sheet_name: str
    credentials: ServiceAccountCredentials
    client: gspread.Client
    worksheet: Worksheet
    create_sheet: bool

    def __init__(self,
                 spreadsheet_id: str | None,
                 sheet_name: str,
                 spreadsheet_name: str | None = None,
                 data_file: Path | None = None,
                 *args,
                 **kwards) -> None:
        """
        Инициализирует объект SpreadSheet.

        :param spreadsheet_id: ID таблицы Google Sheets. Укажите None для создания новой таблицы.
        :type spreadsheet_id: str | None
        :param sheet_name: Имя листа в Google Sheets.
        :type sheet_name: str
        :param spreadsheet_name: Имя новой таблицы Google Sheets, если `spreadsheet_id` не указан.
        :type spreadsheet_name: str | None
        :param data_file: Путь к CSV файлу с данными.
        :type data_file: Path | None
        :raises ValueError: Если `sheet_name` не указан.
        :raises gspread.exceptions.SpreadsheetNotFound: Если таблица с указанным `spreadsheet_id` не найдена.
        """
        if not sheet_name:
            raise ValueError("sheet_name cannot be None.")

        self.spreadsheet_id = spreadsheet_id
        self.spreadsheet_name = spreadsheet_name
        self.sheet_name = sheet_name
        self.data_file = data_file
        self.credentials = self._create_credentials()
        self.client = self._authorize_client()

        try:
            if self.spreadsheet_id:
                self.spreadsheet = self.client.open_by_key(self.spreadsheet_id)
                logger.debug(f"Opened existing spreadsheet with ID: {self.spreadsheet_id}")
            else:
                if not self.spreadsheet_name:
                     raise ValueError("spreadsheet_name cannot be None if spreadsheet_id is None")
                self.spreadsheet = self.client.create(self.spreadsheet_name)
                self.spreadsheet_id = self.spreadsheet.id
                logger.debug(f"Created new spreadsheet with ID: {self.spreadsheet_id}")
                
        except gspread.exceptions.SpreadsheetNotFound:
            logger.error(f"Spreadsheet with ID '{self.spreadsheet_id}' does not exist.", exc_info=True)
            raise
        except Exception as ex:
            logger.error(f"Error during spreadsheet initialization. {ex}", exc_info=True)
            raise
        
        self.worksheet = self.get_worksheet(self.sheet_name)


    def _create_credentials(self) -> ServiceAccountCredentials:
        """
        Создает учетные данные из JSON-файла.

        :return: Учетные данные для доступа к Google Sheets.
        :rtype: ServiceAccountCredentials
        :raises Exception: Если произошла ошибка при создании учетных данных.
        """
        try:
            creds_file: Path = gs.path.secrets / 'e-cat-346312-137284f4419e.json'  # <-  e.cat.co.il@gmail.com
            credentials = ServiceAccountCredentials.from_json_keyfile_name(
                creds_file, self.SCOPES
            )
            logger.debug("Credentials created successfully.")
            return credentials
        except Exception as ex:
            logger.error(f"Error creating credentials. {ex}", exc_info=True)
            raise

    def _authorize_client(self) -> gspread.Client:
        """
        Авторизует клиент для доступа к Google Sheets API.

        :return: Авторизованный клиент для работы с Google Sheets.
        :rtype: gspread.Client
        :raises Exception: Если произошла ошибка при авторизации клиента.
        """
        try:
            client = gspread.authorize(self.credentials)
            logger.debug("Client authorized successfully.")
            return client
        except Exception as ex:
            logger.error(f"Error authorizing client. {ex}", exc_info=True)
            raise

    def get_worksheet(self, worksheet_name: str | Worksheet) -> Worksheet | None:
        """
        Получает рабочий лист по имени.

        Если лист с указанным именем не существует, он будет создан.
        :param worksheet_name: Имя листа в Google Sheets.
        :type worksheet_name: str | Worksheet
        :return: Рабочий лист для работы с данными.
        :rtype: Worksheet | None
        """
        try:
            ws: Worksheet = self.spreadsheet.worksheet(worksheet_name)
        except gspread.exceptions.WorksheetNotFound:
            ws: Worksheet = self.create_worksheet(worksheet_name)
        return ws

    def create_worksheet(self, title: str, dim: dict = {'rows': 100, 'cols': 10}) -> Worksheet | None:
        """
        Создает новый рабочий лист с именем `title` и размерностью `dim`.

        :param title: Имя нового листа.
        :type title: str
        :param dim: Размеры нового листа в виде словаря с ключами 'rows' и 'cols'.
        :type dim: dict
        :return: Созданный рабочий лист.
        :rtype: Worksheet | None
        """
        try:
            ws: Worksheet = self.spreadsheet.add_worksheet(title=title, rows=dim['rows'], cols=dim['cols'])
            return ws
        except Exception as ex:
            logger.error(f"Error creating new worksheet {title}. {ex}", exc_info=True)
            return None
    def copy_worksheet(self, from_worksheet: str, to_worksheet: str) -> Worksheet:
        """
        Копирует рабочий лист по имени.

        :param from_worksheet: Имя листа, который нужно скопировать.
        :type from_worksheet: str
        :param to_worksheet: Имя нового листа, в который будет скопирован исходный лист.
        :type to_worksheet: str
        :return: Скопированный рабочий лист.
        :rtype: Worksheet
        """
        worksheet: Worksheet = self.spreadsheet.worksheet(from_worksheet)
        worksheet.duplicate(new_sheet_name=to_worksheet)
        return worksheet

    def upload_data_to_sheet(self) -> None:
        """
        Загружает данные из CSV-файла в Google Sheets.

        Загружает данные из CSV-файла, указанного в `self.data_file`, в указанный лист Google Sheets.

        :raises ValueError: Если путь к файлу данных не установлен или файл не существует.
        :raises Exception: Если произошла ошибка при загрузке данных в Google Sheets.
        """
        try:
            if not self.data_file or not self.data_file.exists():
                raise ValueError("Data file path is not set or the file does not exist.")

            data = pd.read_csv(self.data_file)  # Чтение данных из CSV-файла
            data_list = [data.columns.values.tolist()] + data.values.tolist()  # Подготовка данных для записи в Google Sheets
            self.worksheet.update('A1', data_list)  # Запись данных в Google Sheets
            logger.debug("Data has been uploaded to Google Sheets successfully.")
        except ValueError as ve:
            logger.error(f"ValueError during data upload: {ve}", exc_info=True)
            raise
        except Exception as ex:
            logger.error(f"Error uploading data to Google Sheets: {ex}", exc_info=True)
            raise

if __name__ == "__main__":
    from pathlib import Path
    
    data_file = Path('/mnt/data/google_extracted/your_data_file.csv')  # Замените на путь к вашему файлу
    sheet_name = 'Sheet1'  # Замените на имя листа в Google Sheets

    # Создание нового документа Google Sheets, если spreadsheet_id не указан
    google_sheet_handler = SpreadSheet(
        spreadsheet_id=None,  # Укажите None для создания нового
        sheet_name=sheet_name,
        spreadsheet_name='My New Spreadsheet',  # Имя нового документа Google Sheets
        data_file=data_file
    )
    google_sheet_handler.upload_data_to_sheet()
```