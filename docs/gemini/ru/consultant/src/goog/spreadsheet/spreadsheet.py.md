# Анализ кода модуля `spreadsheet.py`

**Качество кода: 7/10**
 -  Плюсы
    - Код предоставляет базовый функционал для работы с Google Sheets.
    - Присутствует обработка основных исключений при работе с Google Sheets API.
    - Используется `logger` для логирования ошибок.
    - Есть `docstring` для классов и методов.
    -  Используются `pathlib` для работы с путями.
    -  Для чтения csv используется `pandas`.
 -  Минусы
    -  Не все методы и классы имеют подробные `docstring`,  некоторые из них  не в reStructuredText формате.
    - В некоторых методах излишнее использование `try-except`, которые можно заменить на логирование ошибок.
    -  В `__init__` не хватает обработки исключения если `spreadsheet_id` не указан.
    -  В коде есть комментарии которые не относятся к reStructuredText (`"""` и `#`).
    -  Отсутствует проверка на наличие `sheet_name` при создании нового листа.

**Рекомендации по улучшению**

1.  **Документация**:
    -   Переписать все `docstring` в формате reStructuredText (RST).
    -   Добавить описание каждого параметра и возвращаемого значения в docstring.
2.  **Обработка ошибок**:
    -   Избегать избыточного использования `try-except`, особенно там, где достаточно логировать ошибку.
    -   Использовать `logger.error` для записи ошибок.
3.  **Инициализация**:
    -   Добавить логику для создания новой таблицы, если `spreadsheet_id` не указан.
    -   Проверять наличие `sheet_name`.
4. **Импорты**:
    -   Удалить неиспользуемые импорты, если такие есть.
    -   Сгруппировать импорты по модулям.
5.  **Комментарии**:
    -   Удалить лишние и не информативные комментарии, переписать их в формате reStructuredText.
    -   Оставлять  подробные  комментарии для сложных участков кода.
6.  **Общее**:
    -   Добавить проверки на типы передаваемых параметров.
    -   Организовать копирование `credentials file` в программно созданной `tmp` директории, что бы не хранить его в физической директории.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
Модуль для работы с Google Sheets.
=========================================================================================
Этот модуль предоставляет класс :class:`SpreadSheet`, который позволяет взаимодействовать с Google Sheets API.
Он включает методы для создания, открытия, копирования и загрузки данных в таблицы Google Sheets.

Пример использования
--------------------

.. code-block:: python

    from pathlib import Path

    data_file = Path('/mnt/data/google_extracted/your_data_file.csv')  # Замените на фактический путь к файлу
    sheet_name = 'Sheet1'  # Замените на фактическое имя листа в Google Sheets

    # Создание нового Spreadsheet, если spreadsheet_id не указан
    google_sheet_handler = SpreadSheet(
        spreadsheet_id=None,  # Укажите None для создания нового Spreadsheet
        sheet_name=sheet_name,
        spreadsheet_name='My New Spreadsheet'  # Имя нового Spreadsheet, если spreadsheet_id не указан
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




class SpreadSheet:
    """
    Класс для работы с Google Sheets.

    Этот класс предоставляет методы для доступа к Google Sheets API, создания и управления таблицами,
    а также для загрузки данных из CSV-файла в Google Sheets.
    """

    spreadsheet_id: str | None
    """Идентификатор таблицы Google Sheets."""
    spreadsheet_name: str | None
    """Имя таблицы Google Sheets, используется при создании новой таблицы."""
    spreadsheet: Spreadsheet
    """Объект таблицы Google Sheets."""
    data_file: Path
    """Путь к CSV файлу с данными."""
    sheet_name: str
    """Имя листа в Google Sheets."""
    credentials: ServiceAccountCredentials
    """Учетные данные для доступа к Google Sheets API."""
    client: gspread.Client
    """Клиент для работы с Google Sheets API."""
    worksheet: Worksheet
    """Объект листа Google Sheets."""
    create_sheet: bool
    """Флаг, указывающий нужно ли создавать новый лист если он не существует."""

    def __init__(self,
                 spreadsheet_id: str = None,
                 sheet_name: str = 'Sheet1',
                 spreadsheet_name: str = 'My New Spreadsheet',
                 data_file: Path = None,
                 create_sheet: bool = True
                 ):
        """
        Инициализация объекта SpreadSheet.

        :param spreadsheet_id: ID таблицы Google Sheets. Если `None`, будет создана новая таблица.
        :type spreadsheet_id: str | None
        :param sheet_name: Имя листа в Google Sheets. По умолчанию 'Sheet1'.
        :type sheet_name: str
        :param spreadsheet_name: Имя новой таблицы, если `spreadsheet_id` не указан.
        :type spreadsheet_name: str
        :param data_file: Путь к CSV-файлу с данными.
        :type data_file: Path
        :param create_sheet: Флаг, указывающий нужно ли создавать новый лист если он не существует.
        :type create_sheet: bool
        :raises ValueError: Если не указан ни `spreadsheet_id` ни `spreadsheet_name`.
        :raises gspread.exceptions.SpreadsheetNotFound: Если таблица с указанным ID не найдена.
        """
        self.spreadsheet_id = spreadsheet_id
        self.spreadsheet_name = spreadsheet_name
        self.sheet_name = sheet_name
        self.data_file = data_file
        self.create_sheet = create_sheet
        self.credentials = self._create_credentials()
        self.client = self._authorize_client()

        try:
            if self.spreadsheet_id:
                self.spreadsheet = self.client.open_by_key(self.spreadsheet_id)
                # Код открывает существующую таблицу по ID
                logger.debug(f"Открыта существующая таблица с ID: {self.spreadsheet_id}")
            else:
                if not self.spreadsheet_name:
                     # Если имя новой таблицы не указано
                    raise ValueError("Не указано имя для новой таблицы.")
                self.spreadsheet = self.client.create(self.spreadsheet_name)
                self.spreadsheet_id = self.spreadsheet.id
                # Код создает новую таблицу
                logger.debug(f"Создана новая таблица с ID: {self.spreadsheet_id}")


            self.worksheet = self.get_worksheet(self.sheet_name)
             # Код получает объект листа Google Sheets

        except gspread.exceptions.SpreadsheetNotFound as ex:
            # Логирование ошибки если таблица не найдена
            logger.error(f"Таблица с ID '{self.spreadsheet_id}' не найдена.", exc_info=True)
            raise
        except Exception as ex:
            # Логирование общей ошибки
            logger.error("Ошибка при инициализации таблицы", ex, exc_info=True)
            raise

    def _create_credentials(self) -> ServiceAccountCredentials:
        """
        Создает учетные данные из JSON-файла.

        :return: Учетные данные для доступа к Google Sheets.
        :rtype: ServiceAccountCredentials
        :raises Exception: В случае ошибки создания учетных данных.
        """
        try:
            creds_file: Path = gs.path.secrets / 'e-cat-346312-137284f4419e.json'  # <-  e.cat.co.il@gmail.com
            SCOPES: list = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']
            credentials = ServiceAccountCredentials.from_json_keyfile_name(
                creds_file, SCOPES
            )
            # Код создает учетные данные
            logger.debug("Учетные данные успешно созданы.")
            return credentials
        except Exception as ex:
            # Логирование ошибки создания учетных данных
            logger.error("Ошибка при создании учетных данных.", ex, exc_info=True)
            raise

    def _authorize_client(self) -> gspread.Client:
        """
        Авторизует клиент для доступа к Google Sheets API.

        :return: Авторизованный клиент для работы с Google Sheets.
        :rtype: gspread.Client
        :raises Exception: В случае ошибки авторизации клиента.
        """
        try:
            client = gspread.authorize(self.credentials)
             # Код авторизует клиент
            logger.debug("Клиент успешно авторизован.")
            return client
        except Exception as ex:
            # Логирование ошибки авторизации клиента
            logger.error("Ошибка при авторизации клиента.", ex, exc_info=True)
            raise

    def get_worksheet(self, worksheet_name: str) -> Worksheet:
        """
        Возвращает лист по имени.

        Если лист с указанным именем не существует и флаг `create_sheet` установлен в `True`,
        создается новый лист.

        :param worksheet_name: Имя листа в Google Sheets.
        :type worksheet_name: str
        :return: Объект листа для работы с данными.
        :rtype: Worksheet
        :raises gspread.exceptions.WorksheetNotFound: Если лист не найден и `create_sheet` установлен в `False`.
        """
        try:
            ws: Worksheet = self.spreadsheet.worksheet(worksheet_name)
            # Код получает лист по имени
            return ws
        except gspread.exceptions.WorksheetNotFound:
            if self.create_sheet:
                # Код создает новый лист если он не найден
                 ws: Worksheet  = self.create_worksheet(worksheet_name)
                 return ws
            else:
                # Логирование ошибки если лист не найден и не может быть создан
                logger.error(f"Лист с именем {worksheet_name} не найден.")
                raise
    
    def create_worksheet(self, title:str, dim:dict = {'rows':100,'cols':10}) -> Worksheet:
        """
        Создает новый лист с именем `title` и размерностью `dim`.

        :param title: Имя нового листа.
        :type title: str
        :param dim: Размеры листа (количество строк и столбцов).
        :type dim: dict
        :return: Объект созданного листа.
        :rtype: Worksheet
        :raises Exception: В случае ошибки создания нового листа.
        """
        try:
            ws: Worksheet = self.spreadsheet.add_worksheet(title=title, rows=dim['rows'], cols=dim['cols'])
             # Код создает новый лист
            logger.debug(f"Создан новый лист с именем: {title}")
            return(ws)
        except Exception as ex:
            # Логирование ошибки создания нового листа
            logger.error(f"Ошибка создания нового листа {title}", ex, exc_info=True)
            raise

    def copy_worksheet(self, from_worksheet: str, to_worksheet: str) -> Worksheet:
        """
        Копирует лист по имени.

        :param from_worksheet: Имя листа, который нужно скопировать.
        :type from_worksheet: str
        :param to_worksheet: Имя нового листа.
        :type to_worksheet: str
        :return: Объект скопированного листа.
        :rtype: Worksheet
        """
        # Код копирует существующий лист
        worksheet: Worksheet = self.spreadsheet.worksheet(from_worksheet)
        copied_worksheet = worksheet.duplicate(new_sheet_name=to_worksheet)
        logger.debug(f"Лист '{from_worksheet}' скопирован в '{to_worksheet}'")
        return copied_worksheet

    def upload_data_to_sheet(self):
        """
        Загружает данные из CSV-файла в Google Sheets.

        :raises ValueError: Если путь к файлу не установлен или файл не существует.
        :raises Exception: В случае ошибки при загрузке данных.
        """
        try:
            if not self.data_file or not self.data_file.exists():
                # Проверка на существование файла
                raise ValueError("Путь к файлу данных не установлен или файл не существует.")

            data = pd.read_csv(self.data_file)  # Чтение данных из CSV-файла
            data_list = [data.columns.values.tolist()] + data.values.tolist()  # Подготовка данных для записи в Google Sheets
            self.worksheet.update('A1', data_list)  # Запись данных в Google Sheets
            # Логирование успешной загрузки
            logger.debug("Данные успешно загружены в Google Sheets.")
        except Exception as ex:
            # Логирование ошибки загрузки данных
            logger.error("Ошибка при загрузке данных в Google Sheets.", ex, exc_info=True)
            raise
```