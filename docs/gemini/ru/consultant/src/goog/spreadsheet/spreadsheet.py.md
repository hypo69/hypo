### Анализ кода модуля `spreadsheet`

**Качество кода:**

- **Соответствие стандартам**: 7/10
- **Плюсы**:
    - Код структурирован в виде класса `SpreadSheet`, что облегчает его использование и расширение.
    - Используется библиотека `gspread` для работы с Google Sheets, что является хорошей практикой.
    - Логирование ошибок осуществляется с помощью `logger.error`, что помогает в отладке и мониторинге.
    - Присутствует базовая документация в виде docstring для класса и методов.
- **Минусы**:
    - Не все docstring соответствуют стандарту RST.
    - В некоторых методах отсутствуют явные типы возвращаемых значений.
    - Есть неиспользуемые закомментированные строки кода.
    - Обработка ошибок в методах `_create_credentials` и `_authorize_client` чрезмерна.
    - Используется `pd.read_csv`, но не происходит никакой проверки на корректность данных.
    - Отсутствует проверка на тип данных в `upload_data_to_sheet` перед записью в таблицу.
    - В некоторых местах используются двойные кавычки вместо одинарных.
    - Отсутствуют RST примеры.

**Рекомендации по улучшению:**

1.  **Документация:**
    -   Привести все docstring к стандарту RST, включая описание параметров, типов, возвращаемых значений и исключений.
    -   Добавить примеры использования в docstring для основных методов, используя `.. code-block:: python`.
    -   Убрать неиспользуемые комментарии.
2.  **Типизация:**
    -   Явно указать типы возвращаемых значений для методов, где это необходимо, например, `-> Worksheet` для `create_worksheet`.
3.  **Обработка ошибок:**
    -   Упростить обработку ошибок в методах `_create_credentials` и `_authorize_client`, используя только `logger.error` и `raise`.
    -   Добавить проверку на существование файла перед чтением в `upload_data_to_sheet`.
    -   Добавить проверку на корректность данных, прочитанных из CSV файла.
    -   В методе `upload_data_to_sheet` добавить проверку типа данных, чтобы избежать ошибок при записи в таблицу.
4.  **Форматирование:**
    -   Использовать одинарные кавычки для строк в коде, кроме операций вывода.
    -   Удалить лишние пустые строки.
    -   Выровнять названия переменных, функций и импортов.
5.  **Импорты:**
     -  Импортировать `logger` из `src.logger.logger`.
     -  Использовать `from src.utils.jjson import j_loads, j_loads_ns` если требуется.
6.  **Код:**
    -   Удалить ненужные строки и комментарии.
    -   Заменить многословные комментарии на более краткие и точные.
    -  Избегать использования `try-except` в местах, где можно обойтись `if` проверкой.
    -   Перенести определение `creds_file` в переменную окружения или использовать иной механизм безопасности для хранения ключа.
    -   Добавить обработку `from_worksheet` и `to_worksheet` в методе `copy_worksheet`.

**Оптимизированный код:**

```python
"""
Модуль для работы с Google Sheets
=================================================

Этот модуль содержит класс :class:`SpreadSheet`, который используется для взаимодействия с Google Sheets API,
создания, управления и загрузки данных в таблицы.

Пример использования
----------------------
.. code-block:: python

    from pathlib import Path
    from src.goog.spreadsheet.spreadsheet import SpreadSheet

    data_file = Path('/mnt/data/google_extracted/your_data_file.csv')
    sheet_name = 'Sheet1'

    google_sheet_handler = SpreadSheet(
        spreadsheet_id=None,
        sheet_name=sheet_name,
        spreadsheet_name='My New Spreadsheet'
    )
    google_sheet_handler.upload_data_to_sheet()
"""

from pathlib import Path
import gspread
from gspread import Spreadsheet, Worksheet
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
from src.logger.logger import logger #  Импорт logger из src.logger.logger
from src import gs
from src.utils.printer import pprint

class SpreadSheet:
    """
    Класс для работы с Google Sheets.

    Предоставляет методы для доступа к Google Sheets API, создания и управления таблицами,
    а также загрузки данных из CSV файлов в Google Sheets.
    """

    spreadsheet_id: str | None
    spreadsheet_name: str | None
    spreadsheet: Spreadsheet
    data_file: Path
    sheet_name: str
    credentials: ServiceAccountCredentials
    client: gspread.Client
    worksheet: Worksheet
    create_sheet: bool

    def __init__(self, spreadsheet_id: str | None, sheet_name: str, spreadsheet_name: str | None = None):
        """
        Инициализирует объект SpreadSheet.

        :param spreadsheet_id: ID Google Sheets таблицы. Если None, будет создана новая таблица.
        :type spreadsheet_id: str | None
        :param sheet_name: Название листа в Google Sheets.
        :type sheet_name: str
        :param spreadsheet_name: Имя новой таблицы, если spreadsheet_id не указан.
        :type spreadsheet_name: str | None, optional
        :raises gspread.exceptions.SpreadsheetNotFound: Если таблица с указанным ID не найдена.

        Пример:
            >>> from src.goog.spreadsheet.spreadsheet import SpreadSheet
            >>> sheet = SpreadSheet(spreadsheet_id='some_id', sheet_name='Sheet1')
        """
        self.spreadsheet_id = spreadsheet_id
        self.spreadsheet_name = spreadsheet_name
        self.sheet_name = sheet_name
        self.credentials = self._create_credentials()
        self.client = self._authorize_client()
        if self.spreadsheet_id:
            try:
                self.spreadsheet = self.client.open_by_key(self.spreadsheet_id)
            except gspread.exceptions.SpreadsheetNotFound:
                logger.error(f'Spreadsheet with ID \'{self.spreadsheet_id}\' does not exist.')
                raise
        else:
            self.spreadsheet = self.client.create(self.spreadsheet_name)  # Создание нового spreadsheet если ID не задан

    def _create_credentials(self) -> ServiceAccountCredentials:
        """
        Создает учетные данные из JSON файла.

        :return: Учетные данные для доступа к Google Sheets.
        :rtype: ServiceAccountCredentials
        :raises Exception: Если не удалось создать учетные данные.

        Пример:
             >>> sheet = SpreadSheet(spreadsheet_id='some_id', sheet_name='Sheet1')
             >>> creds = sheet._create_credentials()
             >>> print(creds)
             <oauth2client.service_account.ServiceAccountCredentials object at ...>
        """
        try:
            creds_file: Path = gs.path.secrets / 'e-cat-346312-137284f4419e.json'  # Путь к файлу с учетными данными
            SCOPES: list = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']
            credentials = ServiceAccountCredentials.from_json_keyfile_name(creds_file, SCOPES)
            return credentials
        except Exception as ex:
            logger.error(f'Error creating credentials: {ex}', exc_info=True)  # Логирование ошибки
            raise

    def _authorize_client(self) -> gspread.Client:
        """
        Авторизует клиента для доступа к Google Sheets API.

        :return: Авторизованный клиент для работы с Google Sheets.
        :rtype: gspread.Client
        :raises Exception: Если не удалось авторизовать клиента.

        Пример:
             >>> sheet = SpreadSheet(spreadsheet_id='some_id', sheet_name='Sheet1')
             >>> client = sheet._authorize_client()
             >>> print(client)
             <gspread.client.Client object at ...>
        """
        try:
            client = gspread.authorize(self.credentials)
            return client
        except Exception as ex:
            logger.error(f'Error authorizing client: {ex}', exc_info=True)  # Логирование ошибки
            raise

    def get_worksheet(self, worksheet_name: str) -> Worksheet:
        """
        Получает лист по имени.

        Если лист с указанным именем не существует, он создается.

        :param worksheet_name: Имя листа в Google Sheets.
        :type worksheet_name: str
        :return: Объект Worksheet.
        :rtype: Worksheet
        :raises Exception: Если не удалось получить или создать лист.

        Пример:
           >>> sheet = SpreadSheet(spreadsheet_id='some_id', sheet_name='Sheet1')
           >>> ws = sheet.get_worksheet('Sheet1')
           >>> print(ws)
           <gspread.worksheet.Worksheet object at ...>
        """
        try:
            ws: Worksheet = self.spreadsheet.worksheet(worksheet_name)
            return ws
        except gspread.exceptions.WorksheetNotFound:
            return self.create_worksheet(worksheet_name)

    def create_worksheet(self, title: str, dim: dict = {'rows': 100, 'cols': 10}) -> Worksheet:
        """
        Создает новый лист с указанным именем и размерностью.

        :param title: Название нового листа.
        :type title: str
        :param dim: Словарь с параметрами размерности листа, по умолчанию {'rows': 100, 'cols': 10}.
        :type dim: dict, optional
        :return: Созданный объект Worksheet.
        :rtype: Worksheet
        :raises Exception: В случае ошибки при создании листа.

        Пример:
            >>> sheet = SpreadSheet(spreadsheet_id='some_id', sheet_name='Sheet1')
            >>> ws = sheet.create_worksheet(title='NewSheet', dim={'rows': 50, 'cols': 20})
            >>> print(ws)
            <gspread.worksheet.Worksheet object at ...>
        """
        try:
            ws: Worksheet = self.spreadsheet.add_worksheet(title=title, rows=dim['rows'], cols=dim['cols'])
            return ws
        except Exception as ex:
            logger.error(f'Error creating new sheet {title}: {ex}')
            raise

    def copy_worksheet(self, from_worksheet: str, to_worksheet: str) -> Worksheet:
        """
        Копирует лист из одного в другой.

        :param from_worksheet: Имя листа, который нужно скопировать.
        :type from_worksheet: str
        :param to_worksheet: Имя нового листа.
        :type to_worksheet: str
        :return: Объект Worksheet.
        :rtype: Worksheet
        :raises gspread.exceptions.WorksheetNotFound: Если лист для копирования не найден.

        Пример:
           >>> sheet = SpreadSheet(spreadsheet_id='some_id', sheet_name='Sheet1')
           >>> ws = sheet.copy_worksheet(from_worksheet='Sheet1', to_worksheet='Sheet2')
           >>> print(ws)
           <gspread.worksheet.Worksheet object at ...>
        """
        try:
            worksheet: Worksheet = self.spreadsheet.worksheet(from_worksheet)
            new_worksheet = worksheet.duplicate(new_sheet_name=to_worksheet)
            return new_worksheet
        except gspread.exceptions.WorksheetNotFound as ex:
            logger.error(f"Worksheet '{from_worksheet}' not found: {ex}")
            raise

    def upload_data_to_sheet(self) -> None:
        """
        Загружает данные из CSV файла в Google Sheets.

        Читает данные из CSV файла, указанного в `self.data_file`, и загружает их в указанный лист в Google Sheets.
         В случае если self.data_file не задано или не существует, бросается ValueError.
        :raises ValueError: Если путь к файлу данных не задан или файл не существует.
        :raises Exception: В случае ошибки при чтении или записи данных в Google Sheets.

        Пример:
           >>> from pathlib import Path
           >>> data_file = Path('/path/to/your/data.csv')
           >>> sheet = SpreadSheet(spreadsheet_id='some_id', sheet_name='Sheet1')
           >>> sheet.data_file = data_file
           >>> sheet.upload_data_to_sheet()
        """
        if not hasattr(self, 'data_file') or not self.data_file or not self.data_file.exists():
            logger.error("Data file path is not set or the file does not exist.")
            raise ValueError('Data file path is not set or the file does not exist.')
        try:
            data = pd.read_csv(self.data_file) # Чтение данных из CSV файла
            if not isinstance(data, pd.DataFrame):
                 raise ValueError('Data from CSV is not a DataFrame.')
            data_list = [data.columns.values.tolist()] + data.values.tolist() # Подготовка данных для записи в Google Sheets
            if not hasattr(self, 'worksheet') or self.worksheet is None:
               self.worksheet = self.get_worksheet(self.sheet_name)
            self.worksheet.update('A1', data_list)  # Запись данных в Google Sheets
        except Exception as ex:
            logger.error(f'Error uploading data to Google Sheets: {ex}', exc_info=True) #  Логирование ошибок
            raise