# Анализ кода модуля `spreadsheet`

**Качество кода**
8
-  Плюсы
    - Код структурирован в класс `SpreadSheet`, что обеспечивает инкапсуляцию функциональности.
    - Используется библиотека `gspread` для работы с Google Sheets, что упрощает взаимодействие с API.
    - Присутствует логирование ошибок с использованием `src.logger.logger`.
    - Код читаемый, используются понятные имена переменных и функций.
    - Есть docstring для класса и методов.
    - Используется `pandas` для обработки данных, что хорошо подходит для работы с таблицами.
    - Ошибки обрабатываются с использованием `try-except` блоков.
-  Минусы
    - Отсутствуют комментарии в формате reStructuredText (RST) для функций.
    - Не везде используется логирование `logger.debug`.
    -  Обработка ошибок `try-except` не всегда оптимальна, и местами не используется `logger.error(..., exc_info=True)`.
    - Не используется `j_loads` или `j_loads_ns` для чтения файлов, хотя это требование инструкции.
    - Есть недоработки в обработке ошибок в методах `_create_credentials`, `_authorize_client`.
    -  Не во всех методах есть `return` при успешном завершении.
    -  Не реализована часть метода `copy_worksheet`

**Рекомендации по улучшению**

1.  **Документация**: Добавить недостающие docstring в формате RST для всех методов, включая описание параметров и возвращаемых значений.
2.  **Логирование**: Добавить `logger.debug` для важных шагов, чтобы улучшить отладку.
3.  **Обработка ошибок**: Улучшить обработку ошибок с помощью `logger.error(..., exc_info=True)` в блоках `try-except` для получения более подробной информации об ошибках.
4.  **Использование `j_loads`**: Заменить `pd.read_csv()` на использование `j_loads` или `j_loads_ns`, если это необходимо (в данном случае не требуется).
5.  **Контроль параметров**: Добавить проверку входных параметров в функциях, где это необходимо.
6.  **Рефакторинг**: Упростить код, где это возможно. Например, перенести общую логику создания листа в отдельную функцию.
7.  **Завершение функций**: Добавить `return` в конце успешного выполнения функции.
8. **Обработка `None`**: Добавить обработку `None` значений для `self.spreadsheet_id`.
9. **Копирование листа**: Дописать функционал копирования листа.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
Модуль для работы с Google Sheets.
=========================================================================================

Этот модуль предоставляет класс :class:`SpreadSheet` для взаимодействия с Google Sheets API,
создания и управления таблицами, а также загрузки данных из CSV-файлов в Google Sheets.

Пример использования
--------------------

Пример создания и использования класса `SpreadSheet`:

.. code-block:: python

    from pathlib import Path

    data_file = Path('/mnt/data/google_extracted/your_data_file.csv')  # Замените на актуальный путь к файлу
    sheet_name = 'Sheet1'  # Замените на актуальное имя листа в Google Sheets

    # Создание новой таблицы, если spreadsheet_id не указан
    google_sheet_handler = SpreadSheet(
        spreadsheet_id=None,  # Укажите None для создания новой таблицы
        sheet_name=sheet_name,
        spreadsheet_name='My New Spreadsheet'  # Имя новой таблицы, если spreadsheet_id не указан
    )
    google_sheet_handler.upload_data_to_sheet()
"""
MODE = 'dev'


from pathlib import Path
import gspread
from gspread import Spreadsheet, Worksheet
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
from src.logger.logger import logger
from src import gs
from src.utils.printer import pprint


class SpreadSheet:
    """
    Класс для работы с Google Sheets.

    Предоставляет основные методы для доступа к API Google Sheets, создания и управления таблицами,
    а также загрузки данных из CSV-файла в Google Sheets.
    """

    spreadsheet_id: str | None
    """ID таблицы Google Sheets."""
    spreadsheet_name: str | None
    """Имя таблицы Google Sheets."""
    spreadsheet: Spreadsheet
    """Объект таблицы Google Sheets."""
    data_file: Path
    """Путь к файлу данных CSV."""
    sheet_name: str
    """Имя листа в Google Sheets."""
    credentials: ServiceAccountCredentials
    """Учетные данные для доступа к Google Sheets."""
    client: gspread.Client
    """Клиент для работы с Google Sheets API."""
    worksheet: Worksheet
    """Объект рабочего листа Google Sheets."""
    create_sheet: bool
    """Флаг создания нового листа."""

    def __init__(self,
                 spreadsheet_id: str | None,
                 sheet_name: str,
                 spreadsheet_name: str | None = None,
                 data_file: Path | None = None
                 ):
        """
        Инициализация объекта SpreadSheet.

        :param spreadsheet_id: ID таблицы Google Sheets. Если None, создается новая таблица.
        :param sheet_name: Имя листа в Google Sheets.
        :param spreadsheet_name: Имя новой таблицы, если spreadsheet_id не указан.
        :param data_file: Путь к файлу данных CSV (опционально).
        """
        self.spreadsheet_id = spreadsheet_id
        self.spreadsheet_name = spreadsheet_name
        self.sheet_name = sheet_name
        self.data_file = data_file
        self.credentials = self._create_credentials()
        self.client = self._authorize_client()

        if self.spreadsheet_id:
             try:
                 self.spreadsheet = self.client.open_by_key(self.spreadsheet_id)
                 logger.debug(f"Открыта существующая таблица с ID: {self.spreadsheet_id}")
             except gspread.exceptions.SpreadsheetNotFound:
                 logger.error(f"Таблица с ID '{self.spreadsheet_id}' не найдена.", exc_info=True)
                 raise
        else:
            if not self.spreadsheet_name:
                logger.error(f"Не указано имя для новой таблицы, при создании")
                raise ValueError("Не указано имя для новой таблицы.")
            self.spreadsheet = self.client.create(self.spreadsheet_name)
            logger.info(f"Создана новая таблица с именем: {self.spreadsheet_name}, id: {self.spreadsheet.id}")

        self.worksheet = self.get_worksheet(self.sheet_name)
        if self.worksheet is None:
              logger.error(f"Не удалось получить доступ к листу: {self.sheet_name}")
              raise ValueError(f"Не удалось получить доступ к листу: {self.sheet_name}")
        #logger.debug(f"Рабочий лист установлен: {self.worksheet.title}")


    def _create_credentials(self) -> ServiceAccountCredentials:
        """
        Создание учетных данных из JSON-файла.

        :return: Учетные данные для доступа к Google Sheets.
        """
        try:
            creds_file: Path = gs.path.secrets / 'e-cat-346312-137284f4419e.json' # <-  e.cat.co.il@gmail.com
            SCOPES: list = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']
            credentials = ServiceAccountCredentials.from_json_keyfile_name(
                creds_file, SCOPES
            )
            logger.debug("Учетные данные успешно созданы.")
            return credentials
        except Exception as ex:
            logger.error("Ошибка создания учетных данных.", ex, exc_info=True)
            raise

    def _authorize_client(self) -> gspread.Client:
        """
        Авторизация клиента для доступа к Google Sheets API.

        :return: Авторизованный клиент для работы с Google Sheets.
        """
        try:
            client = gspread.authorize(self.credentials)
            logger.debug("Клиент успешно авторизован.")
            return client
        except Exception as ex:
            logger.error("Ошибка авторизации клиента.", ex, exc_info=True)
            raise

    def get_worksheet(self, worksheet_name: str) -> Worksheet | None:
        """
        Получение рабочего листа по имени.

        Если лист с указанным именем не существует, создается новый лист.

        :param worksheet_name: Имя листа в Google Sheets.
        :return: Рабочий лист для работы с данными.
        """
        try:
             ws: Worksheet = self.spreadsheet.worksheet(worksheet_name)
             logger.debug(f"Лист '{worksheet_name}' найден.")
             return ws
        except gspread.exceptions.WorksheetNotFound:
            logger.debug(f"Лист '{worksheet_name}' не найден, будет создан новый.")
            ws: Worksheet = self.create_worksheet(worksheet_name)
            return ws
        except Exception as ex:
            logger.error(f"Ошибка при получении листа: {worksheet_name}", ex, exc_info=True)
            return None


    def create_worksheet(self, title: str, dim: dict = {'rows': 100, 'cols': 10}) -> Worksheet | None:
        """
        Создание нового листа с указанным именем и размерами.

        :param title: Имя нового листа.
        :param dim: Словарь с параметрами 'rows' и 'cols', задающие размерность нового листа.
        :return: Новый рабочий лист или None в случае ошибки.
        """
        try:
            ws: Worksheet = self.spreadsheet.add_worksheet(title=title, rows=dim['rows'], cols=dim['cols'])
            logger.debug(f"Создан новый лист: {title}")
            return ws
        except Exception as ex:
            logger.error(f"Ошибка создания нового листа {title}", ex, exc_info=True)
            return None

    def copy_worksheet(self, from_worksheet: str, to_worksheet: str) -> Worksheet | None:
        """
        Копирование рабочего листа по имени.

        :param from_worksheet: Имя исходного листа.
        :param to_worksheet: Имя нового листа.
        :return: Новый рабочий лист или None в случае ошибки.
        """
        try:
            worksheet: Worksheet = self.spreadsheet.worksheet(from_worksheet)
            new_worksheet = worksheet.duplicate(new_sheet_name=to_worksheet)
            logger.debug(f"Лист '{from_worksheet}' скопирован в '{to_worksheet}'.")
            return new_worksheet
        except Exception as ex:
             logger.error(f"Ошибка копирования листа '{from_worksheet}' в '{to_worksheet}'", ex, exc_info=True)
             return None

    def upload_data_to_sheet(self):
        """
        Загрузка данных из CSV-файла в Google Sheets.
        """
        try:
            if not self.data_file or not self.data_file.exists():
                raise ValueError("Путь к файлу данных не установлен или файл не существует.")

            data = pd.read_csv(self.data_file)
            data_list = [data.columns.values.tolist()] + data.values.tolist()
            self.worksheet.update('A1', data_list)
            logger.debug("Данные успешно загружены в Google Sheets.")
        except Exception as ex:
            logger.error("Ошибка загрузки данных в Google Sheets.", ex, exc_info=True)
            raise


if __name__ == "__main__":
    from pathlib import Path
    data_file = Path('/mnt/data/google_extracted/your_data_file.csv')  # Замените на фактический путь к файлу данных
    sheet_name = 'Sheet1'  # Замените на фактическое имя листа в Google Sheets
    # Пример использования:
    google_sheet_handler = SpreadSheet(
        spreadsheet_id=None,  # Укажите None для создания новой таблицы
        sheet_name=sheet_name,
        spreadsheet_name='My New Spreadsheet', # Укажите имя новой таблицы
        data_file=data_file # Путь к файлу данных CSV
    )
    google_sheet_handler.upload_data_to_sheet()

```