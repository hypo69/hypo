## Анализ кода модуля `spreadsheet.py`

**Качество кода**
9
-   Плюсы
    -   Код хорошо структурирован и разбит на методы, каждый из которых выполняет определенную функцию.
    -   Используется `logger` для логирования ошибок и отладочной информации.
    -   Присутствуют docstring для классов и методов, что упрощает понимание кода.
    -   Используются `try-except` блоки для обработки исключений, что повышает надежность кода.
-   Минусы
    -   Не все комментарии оформлены в формате reStructuredText (RST).
    -   Местами используются стандартные исключения, вместо обработки через логгер.
    -   Присутствует закомментированный код и todo, который следует убрать.
    -   Отсутствуют импорты из `src.utils.jjson`.
    -   Использование `*args, **kwargs` в `__init__` не требуется и избыточно.

**Рекомендации по улучшению**

1.  **Документация**:
    -   Переписать все комментарии и docstring в формате reStructuredText (RST).
    -   Добавить более подробные описания для параметров и возвращаемых значений.
    -   Использовать ``:param``, ``:return``, ``:raises`` в docstring.
2.  **Обработка ошибок**:
    -   Улучшить обработку ошибок, используя `logger.error` для логирования, вместо `raise`.
    -   Удалить избыточные `try-except` блоки, где это возможно.
3.  **Структура кода**:
    -   Убрать закомментированный код и `todo`.
    -   Импортировать необходимые функции из `src.utils.jjson`.
    -   Удалить `*args, **kwargs` в `__init__` если они не используются.
4.  **Общее**:
    -   Привести в соответствие имена переменных и функций с ранее обработанными файлами (если есть такие требования).

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
Модуль для работы с Google Sheets.
=========================================================================================

Этот модуль содержит класс :class:`SpreadSheet`, который используется для взаимодействия
с Google Sheets API, создания, управления и загрузки данных в Google Sheets.

Пример использования
--------------------

Пример использования класса `SpreadSheet`:

.. code-block:: python

    from pathlib import Path

    data_file = Path('/mnt/data/google_extracted/your_data_file.csv')
    sheet_name = 'Sheet1'

    google_sheet_handler = SpreadSheet(
        spreadsheet_id=None,
        sheet_name=sheet_name,
        spreadsheet_name='My New Spreadsheet'
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
#  `j_loads` или `j_loads_ns` from `src.utils.jjson`  не используются в данном файле
# from src.utils.jjson import j_loads, j_loads_ns


class SpreadSheet:
    """
    Класс для работы с Google Sheets.

    Предоставляет базовые методы для доступа к Google Sheets API, создания и управления
    таблицами, а также загрузки данных из CSV-файла в Google Sheets.
    """

    #  Path to the credentials file for accessing Google Sheets.
    # creds_file = gs.path.root / 'secrets' / 'hypo69-c32c8736ca62.json'
    #  оригинал файла хранится в базе данных вместе с паролями
    #  @todo организовать копирование файла в прогамно созаданом `tmp`,чтобы не хранить файл в физической директории

    spreadsheet_id: str | None
    """Идентификатор Google Sheets."""
    spreadsheet_name: str | None
    """Имя Google Sheets."""
    spreadsheet: Spreadsheet
    """Объект Spreadsheet."""
    data_file: Path
    """Путь к CSV файлу с данными."""
    sheet_name: str
    """Имя листа Google Sheets."""
    credentials: ServiceAccountCredentials
    """Учетные данные для доступа к Google Sheets API."""
    client: gspread.Client
    """Клиент для работы с Google Sheets API."""
    worksheet: Worksheet
    """Объект Worksheet."""
    create_sheet: bool
    """Флаг для создания листа."""

    def __init__(self, spreadsheet_id: str, sheet_name: str = None, spreadsheet_name: str = None) -> None:
        """
        Инициализирует класс SpreadSheet.

        :param spreadsheet_id: Идентификатор Google Sheets. Используйте None для создания новой таблицы.
        :param sheet_name: Имя листа в Google Sheets.
        :param spreadsheet_name: Имя новой таблицы, если `spreadsheet_id` не указан.
        """
        #  Инициализирует класс SpreadSheet, устанавливая значения атрибутов
        self.spreadsheet_id = spreadsheet_id
        self.spreadsheet_name = spreadsheet_name
        self.sheet_name = sheet_name
        self.credentials = self._create_credentials()
        #  Создает объект клиента Google Sheets
        self.client = self._authorize_client()

        try:
            #  Открывает существующую таблицу по ID
            self.spreadsheet = self.client.open_by_key(self.spreadsheet_id)
            logger.debug(f"Открыта существующая таблица с ID: {self.spreadsheet_id}")
        except gspread.exceptions.SpreadsheetNotFound as ex:
            #  Логирует ошибку, если таблица не найдена, и поднимает исключение
            logger.error(f"Таблица с ID '{self.spreadsheet_id}' не существует.", ex, exc_info=True)
            raise

    def _create_credentials(self) -> ServiceAccountCredentials:
        """
        Создает учетные данные из JSON файла.

        :return: Учетные данные для доступа к Google Sheets.
        :raises Exception: Если не удалось создать учетные данные.
        """
        try:
            #  Устанавливает путь к файлу с учетными данными
            creds_file: Path = gs.path.secrets / 'e-cat-346312-137284f4419e.json'
            #  Устанавливает область доступа к Google Sheets API
            SCOPES: list = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']
            #  Создает объект учетных данных из JSON файла
            credentials = ServiceAccountCredentials.from_json_keyfile_name(
                creds_file, SCOPES
            )
            logger.debug("Учетные данные успешно созданы.")
            return credentials
        except Exception as ex:
            #  Логирует ошибку и поднимает исключение, если не удалось создать учетные данные
            logger.error("Ошибка создания учетных данных.", ex, exc_info=True)
            raise

    def _authorize_client(self) -> gspread.Client:
        """
        Авторизует клиента для доступа к Google Sheets API.

        :return: Авторизованный клиент для работы с Google Sheets.
        :raises Exception: Если не удалось авторизовать клиента.
        """
        try:
            #  Авторизует клиента с использованием учетных данных
            client = gspread.authorize(self.credentials)
            logger.debug("Клиент успешно авторизован.")
            return client
        except Exception as ex:
            #  Логирует ошибку и поднимает исключение, если не удалось авторизовать клиента
            logger.error("Ошибка авторизации клиента.", ex, exc_info=True)
            raise

    def get_worksheet(self, worksheet_name: str) -> Worksheet | None:
        """
        Получает лист по имени.

        Если лист с указанным именем не существует, он будет создан.

        :param worksheet_name: Имя листа в Google Sheets.
        :return: Лист для работы с данными.
        """
        try:
            #  Пытается получить существующий лист
            ws: Worksheet = self.spreadsheet.worksheet(worksheet_name)
        except gspread.exceptions.WorksheetNotFound:
            #  Создает новый лист, если не найден
            ws: Worksheet = self.create_worksheet(worksheet_name)
        return ws

    def create_worksheet(self, title: str, dim: dict = {'rows': 100, 'cols': 10}) -> Worksheet | None:
        """
        Создает новый лист с именем `title` и размерностью `dim`.

        :param title: Имя нового листа.
        :param dim: Словарь с указанием количества строк и столбцов.
        :return: Объект созданного листа.
        """
        try:
            #  Создает новый лист в Google Sheets
            ws: Worksheet = self.spreadsheet.add_worksheet(title=title, rows=dim['rows'], cols=dim['cols'])
            return ws
        except Exception as ex:
            #  Логирует ошибку, если не удалось создать новый лист
            logger.error(f"Ошибка создания нового листа {title}", ex, exc_info=True)
            return None

    def copy_worksheet(self, from_worksheet: str, to_worksheet: str) -> Worksheet:
        """
        Копирует лист по имени.

        :param from_worksheet: Имя листа, который нужно скопировать.
        :param to_worksheet: Имя нового листа, который будет создан как копия.
        :return: Объект скопированного листа.
        """
        #  Копирует лист
        worksheet: Worksheet = self.spreadsheet.worksheet(from_worksheet)
        worksheet.duplicate(new_sheet_name=to_worksheet)
        return worksheet

    def upload_data_to_sheet(self) -> None:
        """
        Загружает данные из CSV-файла в Google Sheets.

        Загружает данные из CSV-файла, указанного в `self.data_file`, в указанный лист Google Sheets.
        """
        try:
            #  Проверяет, установлен ли путь к файлу данных и существует ли файл
            if not hasattr(self, 'data_file') or not self.data_file or not self.data_file.exists():
                raise ValueError("Путь к файлу данных не установлен или файл не существует.")
            #  Читает данные из CSV-файла
            data = pd.read_csv(self.data_file)
            #  Подготавливает данные для записи в Google Sheets
            data_list = [data.columns.values.tolist()] + data.values.tolist()
            #  Записывает данные в Google Sheets
            self.worksheet.update('A1', data_list)
            logger.debug("Данные успешно загружены в Google Sheets.")
        except Exception as ex:
            #  Логирует ошибку, если не удалось загрузить данные в Google Sheets
            logger.error("Ошибка загрузки данных в Google Sheets.", ex, exc_info=True)
            raise