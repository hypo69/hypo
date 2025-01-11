# Анализ кода модуля `reach_spreadsheet.py`

**Качество кода**
8
-  Плюсы
    - Код хорошо структурирован и разбит на классы и методы, что улучшает читаемость и повторное использование.
    - Используется библиотека `googleapiclient` для работы с Google Sheets API.
    - Присутствуют обработки исключений, хотя и с использованием `...`
    - Добавлены комментарии, объясняющие назначение основных частей кода.
    - Использование `j_loads_ns` для загрузки данных из json файла.
-  Минусы
    - Не все функции и методы имеют docstring (документацию).
    - Не везде используется логгер для отслеживания ошибок и отладки.
    - Присутствует избыточное использование `try-except` с `...` в блоке `__init__`.
    - Не везде используются одинарные кавычки в коде.
    - Есть неиспользуемый импорт `tempfile`, который нужно удалить.
    - Присутствует неиспользуемый закомментированный код.
    - Не все переменные и функции имеют snake_case.
    - Отсутствует описание модуля в начале файла.

**Рекомендации по улучшению**

1.  **Добавить docstring**: Добавить описание модуля, docstring для всех классов, методов и функций. Использовать формат RST.
2.  **Использовать логгер**: Заменить `print` на `logger.info`, а также использовать `logger.error` для логирования ошибок. Убрать `exc_info=True` из `logger.error`, так как он является избыточным.
3.  **Убрать избыточный try-except**: Избегать использования `try-except` с `...`, заменяя на `logger.error`.
4.  **Исправить кавычки**: Использовать одинарные кавычки (`'`) в коде Python.
5.  **Удалить неиспользуемый импорт**: Удалить импорт `tempfile`, так как он не используется.
6.  **Удалить закомментированный код**: Убрать неиспользуемый закомментированный код.
7.  **Использовать snake_case**: Переименовать переменные и функции в snake_case.
8.  **Удалить debugMode**: Удалить `debugMode`, так как он нигде не используется.
9.  **Убрать устаревший код**: Код `Spreadsheet` переименовать в `ReachSpreadsheet` и удалить `Spreadsheet` из тестов.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
"""
Модуль для работы с Google Sheets API.
=========================================================================================

Этот модуль содержит класс :class:`ReachSpreadsheet`, который используется для
взаимодействия с Google Sheets API v4 и Google Drive API v3.
Модуль предоставляет функциональность для создания, редактирования и обмена
Google Sheets.

Пример использования
--------------------

Пример использования класса `ReachSpreadsheet`:

.. code-block:: python

    spreadsheet = ReachSpreadsheet()
    spreadsheet.create(title='My Spreadsheet', sheet_title='Sheet1')
    spreadsheet.share_with_email_for_writing('user@example.com')
    url = spreadsheet.get_sheet_url()
    print(f'Spreadsheet URL: {url}')
"""

import googleapiclient.discovery
import googleapiclient.errors
import httplib2
from oauth2client.service_account import ServiceAccountCredentials

from src import gs
from src.utils.jjson import j_loads_ns, j_dumps
from src.utils.printer import pprint
from src.logger.logger import logger


def html_color_to_json(html_color):
    """Преобразует HTML-цвет в JSON формат.

    Args:
        html_color (str): HTML-цвет в формате "#RRGGBB".

    Returns:
        dict: JSON представление цвета в формате {"red": r, "green": g, "blue": b}.
    """
    if html_color.startswith('#'):
        html_color = html_color[1:]
    return {
        'red': int(html_color[0:2], 16) / 255.0,
        'green': int(html_color[2:4], 16) / 255.0,
        'blue': int(html_color[4:6], 16) / 255.0,
    }


class SpreadsheetError(Exception):
    """Базовое исключение для ошибок, связанных с Google Sheets."""

    ...


class SpreadsheetNotSetError(SpreadsheetError):
    """Исключение, возникающее, если не установлен идентификатор таблицы."""

    ...


class SheetNotSetError(SpreadsheetError):
    """Исключение, возникающее, если не установлен идентификатор листа."""

    ...


class ReachSpreadsheet:
    """
    Класс для работы с Google Sheets API.

    Предоставляет методы для создания, редактирования и обмена Google Sheets.
    """

    def __init__(self):
        """Инициализирует объект ReachSpreadsheet, настраивая подключение к Google Sheets API."""
        try:
            json_key_file_name = gs.path.tmp / 'e-cat-346312-137284f4419e.json'

            # Загрузка данных из временного файла для создания credentials
            self.credentials = ServiceAccountCredentials.from_json_keyfile_name(
                json_key_file_name,
                ['https://www.googleapis.com/auth/spreadsheets'],
            )
            logger.info('Credentials created successfully.')
        except Exception as ex:
            logger.error('Error creating credentials.', exc_info=False)
            return

        self.http_auth = self.credentials.authorize(httplib2.Http())
        self.service = googleapiclient.discovery.build(
            'sheets', 'v4', http=self.http_auth
        )
        self.drive_service = googleapiclient.discovery.build(
            'drive', 'v3', http=self.http_auth
        )
        self.spreadsheet_id = None
        self.sheet_id = None
        self.sheet_title = None
        self.requests = []
        self.value_ranges = []

    def create(
        self,
        title,
        sheet_title,
        rows=1000,
        cols=26,
        locale='en-US',
        time_zone='Etc/GMT',
    ):
        """Создает новую таблицу Google Sheets.

        Args:
            title (str): Заголовок таблицы.
            sheet_title (str): Заголовок первого листа.
            rows (int, optional): Количество строк в листе. Defaults to 1000.
            cols (int, optional): Количество столбцов в листе. Defaults to 26.
            locale (str, optional): Локаль таблицы. Defaults to 'en-US'.
            time_zone (str, optional): Временная зона таблицы. Defaults to 'Etc/GMT'.
        """
        spreadsheet = (
            self.service.spreadsheets()
            .create(
                body={
                    'properties': {'title': title},
                    'sheets': [
                        {
                            'properties': {
                                'sheetType': 'GRID',
                                'sheetId': 0,
                                'title': sheet_title,
                                'gridProperties': {
                                    'rowCount': rows,
                                    'columnCount': cols,
                                },
                            }
                        }
                    ],
                }
            )
            .execute()
        )

        logger.info(f'Spreadsheet created: {spreadsheet}')
        self.spreadsheet_id = spreadsheet['spreadsheetId']
        self.sheet_id = spreadsheet['sheets'][0]['properties']['sheetId']
        self.sheet_title = spreadsheet['sheets'][0]['properties']['title']

    def share(self, share_request_body):
        """Предоставляет доступ к таблице Google Sheets.

        Args:
            share_request_body (dict): Тело запроса для предоставления доступа.
        Raises:
            SpreadsheetNotSetError: Если не установлен идентификатор таблицы.
        """
        if self.spreadsheet_id is None:
            raise SpreadsheetNotSetError()
        if self.drive_service is None:
            self.drive_service = googleapiclient.discovery.build(
                'drive', 'v3', http=self.http_auth
            )
        share_res = (
            self.drive_service.permissions()
            .create(
                fileId=self.spreadsheet_id,
                body=share_request_body,
                fields='id',
            )
            .execute()
        )
        logger.info(f'Spreadsheet shared: {share_res}')

    def share_with_email_for_reading(self, email):
        """Предоставляет доступ на чтение к таблице для указанного email.

        Args:
            email (str): Email пользователя.
        """
        self.share({'type': 'user', 'role': 'reader', 'emailAddress': email})

    def share_with_email_for_writing(self, email):
        """Предоставляет доступ на запись к таблице для указанного email.

        Args:
            email (str): Email пользователя.
        """
        self.share({'type': 'user', 'role': 'writer', 'emailAddress': email})

    def share_with_anybody_for_reading(self):
        """Предоставляет публичный доступ на чтение к таблице."""
        self.share({'type': 'anyone', 'role': 'reader'})

    def share_with_anybody_for_writing(self):
        """Предоставляет публичный доступ на запись к таблице."""
        self.share({'type': 'anyone', 'role': 'writer'})

    def get_sheet_url(self):
        """Возвращает URL текущего листа Google Sheets.

        Raises:
            SpreadsheetNotSetError: Если не установлен идентификатор таблицы.
            SheetNotSetError: Если не установлен идентификатор листа.
        Returns:
            str: URL текущего листа.
        """
        if self.spreadsheet_id is None:
            raise SpreadsheetNotSetError()
        if self.sheet_id is None:
            raise SheetNotSetError()
        return (
            f'https://docs.google.com/spreadsheets/d/{self.spreadsheet_id}'
            f'/edit#gid={self.sheet_id}'
        )

    def set_spreadsheet_by_id(self, spreadsheet_id):
        """Устанавливает текущую таблицу по ID.

        Args:
            spreadsheet_id (str): Идентификатор таблицы.
        """
        spreadsheet = (
            self.service.spreadsheets()
            .get(spreadsheetId=spreadsheet_id)
            .execute()
        )
        logger.info(f'Spreadsheet set: {spreadsheet}')
        self.spreadsheet_id = spreadsheet['spreadsheetId']
        self.sheet_id = spreadsheet['sheets'][0]['properties']['sheetId']
        self.sheet_title = spreadsheet['sheets'][0]['properties']['title']

    def run_prepared(self, value_input_option='USER_ENTERED'):
        """Выполняет подготовленные запросы на обновление таблицы.

        Args:
            value_input_option (str, optional): Способ обработки вводимых значений. Defaults to "USER_ENTERED".
        Raises:
            SpreadsheetNotSetError: Если не установлен идентификатор таблицы.
        Returns:
            tuple: Кортеж с ответами на запросы.
        """
        if self.spreadsheet_id is None:
            raise SpreadsheetNotSetError()
        upd1_res = {'replies': []}
        upd2_res = {'responses': []}
        try:
            if len(self.requests) > 0:
                upd1_res = (
                    self.service.spreadsheets()
                    .batchUpdate(
                        spreadsheetId=self.spreadsheet_id,
                        body={'requests': self.requests},
                    )
                    .execute()
                )
                logger.info(f'Batch update 1 result: {upd1_res}')

            if len(self.value_ranges) > 0:
                upd2_res = (
                    self.service.spreadsheets()
                    .values()
                    .batchUpdate(
                        spreadsheetId=self.spreadsheet_id,
                        body={
                            'valueInputOption': value_input_option,
                            'data': self.value_ranges,
                        },
                    )
                    .execute()
                )
                logger.info(f'Batch update 2 result: {upd2_res}')
        finally:
            self.requests = []
            self.value_ranges = []
        return (upd1_res['replies'], upd2_res['responses'])

    def prepare_add_sheet(self, sheet_title, rows=1000, cols=26):
        """Подготавливает запрос на добавление нового листа.

        Args:
            sheet_title (str): Заголовок нового листа.
            rows (int, optional): Количество строк в листе. Defaults to 1000.
            cols (int, optional): Количество столбцов в листе. Defaults to 26.
        """
        self.requests.append(
            {
                'addSheet': {
                    'properties': {
                        'title': sheet_title,
                        'gridProperties': {
                            'rowCount': rows,
                            'columnCount': cols,
                        },
                    }
                }
            }
        )

    def add_sheet(self, sheet_title, rows=1000, cols=26):
        """Добавляет новый лист в текущую таблицу.

        Args:
            sheet_title (str): Заголовок нового листа.
            rows (int, optional): Количество строк в листе. Defaults to 1000.
            cols (int, optional): Количество столбцов в листе. Defaults to 26.

        Raises:
             SpreadsheetNotSetError: Если не установлен идентификатор таблицы.
        Returns:
            int: ID добавленного листа.
        """
        if self.spreadsheet_id is None:
            raise SpreadsheetNotSetError()
        self.prepare_add_sheet(sheet_title, rows, cols)
        added_sheet = self.run_prepared()[0][0]['addSheet']['properties']
        self.sheet_id = added_sheet['sheetId']
        self.sheet_title = added_sheet['title']
        return self.sheet_id

    def to_grid_range(self, cells_range):
        """Преобразует строковый диапазон в GridRange текущего листа.

         Args:
            cells_range (str): Диапазон ячеек, например, "A3:B4" или "A5:B".

        Raises:
             SheetNotSetError: Если не установлен идентификатор листа.
        Returns:
            dict: GridRange текущего листа.
        """
        if self.sheet_id is None:
            raise SheetNotSetError()
        if isinstance(cells_range, str):
            start_cell, end_cell = cells_range.split(':')[0:2]
            cells_range = {}
            range_az = range(ord('A'), ord('Z') + 1)
            if ord(start_cell[0]) in range_az:
                cells_range['startColumnIndex'] = ord(start_cell[0]) - ord('A')
                start_cell = start_cell[1:]
            if ord(end_cell[0]) in range_az:
                cells_range['endColumnIndex'] = ord(end_cell[0]) - ord('A') + 1
                end_cell = end_cell[1:]
            if len(start_cell) > 0:
                cells_range['startRowIndex'] = int(start_cell) - 1
            if len(end_cell) > 0:
                cells_range['endRowIndex'] = int(end_cell)
        cells_range['sheetId'] = self.sheet_id
        return cells_range

    def prepare_set_dimension_pixel_size(
        self, dimension, start_index, end_index, pixel_size
    ):
        """Подготавливает запрос на изменение размера столбцов или строк.

        Args:
            dimension (str): "COLUMNS" или "ROWS".
            start_index (int): Индекс начала.
            end_index (int): Индекс конца.
            pixel_size (int): Размер в пикселях.

        Raises:
            SheetNotSetError: Если не установлен идентификатор листа.
        """
        if self.sheet_id is None:
            raise SheetNotSetError()
        self.requests.append(
            {
                'updateDimensionProperties': {
                    'range': {
                        'sheetId': self.sheet_id,
                        'dimension': dimension,
                        'startIndex': start_index,
                        'endIndex': end_index,
                    },
                    'properties': {'pixelSize': pixel_size},
                    'fields': 'pixelSize',
                }
            }
        )

    def prepare_set_columns_width(self, start_col, end_col, width):
        """Подготавливает запрос на изменение ширины нескольких столбцов.

        Args:
            start_col (int): Индекс начального столбца.
            end_col (int): Индекс конечного столбца.
            width (int): Ширина столбцов в пикселях.
        """
        self.prepare_set_dimension_pixel_size(
            'COLUMNS', start_col, end_col + 1, width
        )

    def prepare_set_column_width(self, col, width):
        """Подготавливает запрос на изменение ширины одного столбца.

        Args:
            col (int): Индекс столбца.
            width (int): Ширина столбца в пикселях.
        """
        self.prepare_set_columns_width(col, col, width)

    def prepare_set_rows_height(self, start_row, end_row, height):
        """Подготавливает запрос на изменение высоты нескольких строк.

        Args:
            start_row (int): Индекс начальной строки.
            end_row (int): Индекс конечной строки.
            height (int): Высота строк в пикселях.
        """
        self.prepare_set_dimension_pixel_size(
            'ROWS', start_row, end_row + 1, height
        )

    def prepare_set_row_height(self, row, height):
        """Подготавливает запрос на изменение высоты одной строки.

        Args:
             row (int): Индекс строки.
             height (int): Высота строки в пикселях.
        """
        self.prepare_set_rows_height(row, row, height)

    def prepare_set_values(self, cells_range, values, major_dimension='ROWS'):
        """Подготавливает запрос на установку значений в ячейки.

        Args:
             cells_range (str): Диапазон ячеек, например "A1:B2".
             values (list): Значения для установки.
             major_dimension (str, optional): "ROWS" или "COLUMNS". Defaults to "ROWS".

         Raises:
              SheetNotSetError: Если не установлен заголовок листа.
        """
        if self.sheet_title is None:
            raise SheetNotSetError()
        self.value_ranges.append(
            {
                'range': self.sheet_title + '!' + cells_range,
                'majorDimension': major_dimension,
                'values': values,
            }
        )

    def prepare_merge_cells(self, cells_range, merge_type='MERGE_ALL'):
        """Подготавливает запрос на объединение ячеек.

        Args:
            cells_range (str): Диапазон ячеек, например "A1:B2".
            merge_type (str, optional): Тип объединения. Defaults to "MERGE_ALL".
        """
        self.requests.append(
            {
                'mergeCells': {
                    'range': self.to_grid_range(cells_range),
                    'mergeType': merge_type,
                }
            }
        )

    def prepare_set_cell_string_formatter(
        self, cells_range, format_json, fields='userEnteredFormat'
    ):
        """Подготавливает запрос на форматирование ячеек.

        Args:
            cells_range (str): Диапазон ячеек, например "A1:B2".
            format_json (dict): JSON с параметрами форматирования.
            fields (str, optional): Поля для обновления. Defaults to "userEnteredFormat".
        """
        self.requests.append(
            {
                'repeatCell': {
                    'range': self.to_grid_range(cells_range),
                    'cell': {'userEnteredFormat': format_json},
                    'fields': fields,
                }
            }
        )

    def prepare_set_cell_string_formatters(
        self, cells_range, formats_json, fields='userEnteredFormat'
    ):
        """Подготавливает запрос на пакетное форматирование ячеек.

        Args:
            cells_range (str): Диапазон ячеек, например "A1:B2".
            formats_json (list): Список JSON-объектов с параметрами форматирования.
            fields (str, optional): Поля для обновления. Defaults to "userEnteredFormat".
        """
        self.requests.append(
            {
                'updateCells': {
                    'range': self.to_grid_range(cells_range),
                    'rows': [
                        {
                            'values': [
                                {'userEnteredFormat': cell_format}
                                for cell_format in row_formats
                            ]
                        }
                        for row_formats in formats_json
                    ],
                    'fields': fields,
                }
            }
        )


# === Tests for class Spreadsheet ===


def test_create_spreadsheet():
    """Тестирует создание таблицы."""
    ss = ReachSpreadsheet()
    ss.create('Preved medved', 'Тестовый лист')
    ss.share_with_email_for_writing('volkov.ioann@gmail.com')


def test_set_spreadsheet():
    """Тестирует установку таблицы по ID."""
    ss = ReachSpreadsheet()
    ss.set_spreadsheet_by_id('19SPK--efwYq9pZ7TvBYtFItxE0gY3zpfR5NykOJ6o7I')
    print(ss.sheet_id)


def test_add_sheet():
    """Тестирует добавление листа."""
    ss = ReachSpreadsheet()
    ss.set_spreadsheet_by_id('19SPK--efwYq9pZ7TvBYtFItxE0gY3zpfR5NykOJ6o7I')
    try:
        print(ss.add_sheet('Я лолка №1', 500, 11))
    except googleapiclient.errors.HttpError:
        print('Could not add sheet! Maybe sheet with same name already exists!')


def test_set_dimensions():
    """Тестирует установку размеров столбцов и строк."""
    ss = ReachSpreadsheet()
    ss.set_spreadsheet_by_id('19SPK--efwYq9pZ7TvBYtFItxE0gY3zpfR5NykOJ6o7I')
    ss.prepare_set_column_width(0, 500)
    ss.prepare_set_column_width(1, 100)
    ss.prepare_set_columns_width(2, 4, 150)
    ss.prepare_set_row_height(6, 230)
    ss.run_prepared()


def test_grid_range_for_str():
    """Тестирует преобразование строковых диапазонов в GridRange."""
    ss = ReachSpreadsheet()
    ss.set_spreadsheet_by_id('19SPK--efwYq9pZ7TvBYtFItxE0gY3zpfR5NykOJ6o7I')
    res = [
        ss.to_grid_range('A3:B4'),
        ss.to_grid_range('A5:B'),
        ss.to_grid_range('A:B'),
    ]
    correct_res = [
        {
            'sheetId': ss.sheet_id,
            'startRowIndex': 2,
            'endRowIndex': 4,
            'startColumnIndex': 0,
            'endColumnIndex': 2,
        },
        {
            'sheetId': ss.sheet_id,
            'startRowIndex': 4,
            'startColumnIndex': 0,
            'endColumnIndex': 2,
        },
        {'sheetId': ss.sheet_id, 'startColumnIndex': 0, 'endColumnIndex': 2},
    ]
    print('GOOD' if res == correct_res else 'BAD', res)


def test_set_cell_string_formatter():
    """Тестирует установку форматирования ячеек."""
    ss = ReachSpreadsheet()
    ss.set_spreadsheet_by_id('19SPK--efwYq9pZ7TvBYtFItxE0gY3zpfR5NykOJ6o7I')
    ss.prepare_set_cell_string_formatter(
        'B2:E7', {'textFormat': {'bold': True}, 'horizontalAlignment': 'CENTER'}
    )
    ss.run_prepared()


def test_pure_black_border():
    """Тестирует установку черных границ ячеек."""
    ss = ReachSpreadsheet()
    ss.set_spreadsheet_by_id('19SPK--efwYq9pZ7TvBYtFItxE0gY3zpfR5NykOJ6o7I')
    ss.requests.append(
        {
            'updateBorders': {
                'range': {
                    'sheetId': ss.sheet_id,
                    'startRowIndex': 1,
                    'endRowIndex': 2,
                    'startColumnIndex': 0,
                    'endColumnIndex': 3,
                },
                'bottom': {
                    'style': 'SOLID',
                    'width': 3,
                    'color': {'red': 0, 'green': 0, 'blue': 0},
                },
            }
        }
    )
    ss.requests.append(
        {
            'updateBorders': {
                'range': {
                    'sheetId': ss.sheet_id,
                    'startRowIndex': 2,
                    'endRowIndex': 3,
                    'startColumnIndex': 0,
                    'endColumnIndex': 3,
                },
                'bottom': {
                    'style': 'SOLID',
                    'width': 3,
                    'color': {'red': 0, 'green': 0, 'blue': 0, 'alpha': 1.0},
                },
            }
        }
    )
    ss.requests.append(
        {
            'updateBorders': {
                'range': {
                    'sheetId': ss.sheet_id,
                    'startRowIndex': 3,
                    'endRowIndex': 4,
                    'startColumnIndex': 1,
                    'endColumnIndex': 4,
                },
                'bottom': {
                    'style': 'SOLID',
                    'width': 3,
                    'color': {'red': 0, 'green': 0, 'blue': 0.001},
                },
            }
        }
    )
    ss.requests.append(
        {
            'updateBorders': {
                'range': {
                    'sheetId': ss.sheet_id,
                    'startRowIndex': 4,
                    'endRowIndex': 5,
                    'startColumnIndex': 2,
                    'endColumnIndex': 5,
                },
                'bottom': {
                    'style': 'SOLID',
                    'width': 3,
                    'color': {'red': 0.001, 'green': 0, 'blue': 0},
                },
            }
        }
    )
    ss.run_prepared()


def test_update_cell_string_formatter_fields_arg():
    """Тестирует обновление форматирования ячеек с аргументом fields."""
    ss = ReachSpreadsheet()
    ss.set_spreadsheet_by_id('19SPK--efwYq9pZ7TvBYtFItxE0gY3zpfR5NykOJ6o7I')
    ss.prepare_set_cell_string_formatter(
        'B2:B2',
        {'textFormat': {'bold': True}, 'horizontalAlignment': 'CENTER'},
        fields='userEnteredFormat.textFormat,userEnteredFormat.horizontalAlignment',
    )
    ss.prepare_set_cell_string_formatter(
        'B2:B2',
        {'backgroundColor': html_color_to_json('#00CC00')},
        fields='userEnteredFormat.backgroundColor',
    )
    ss.prepare_set_cell_string_formatters(
        'C4:C4',
        [[{'textFormat': {'bold': True}, 'horizontalAlignment': 'CENTER'}]],
        fields='userEnteredFormat.textFormat,userEnteredFormat.horizontalAlignment',
    )
    ss.prepare_set_cell_string_formatters(
        'C4:C4',
        [[{'backgroundColor': html_color_to_json('#00CC00')}]],
        fields='userEnteredFormat.backgroundColor',
    )
    pprint(ss.requests)
    ss.run_prepared()


def create_pricelist(doc_title, sheet_title, values: list):
    """Создает таблицу с прайс-листом."""
    row_count = len(values) - 1
    ss = ReachSpreadsheet()
    ss.create(
        doc_title,
        sheet_title,
        rows=row_count + 3,
        cols=70,
        locale='en-US',
        time_zone='Asia/Jerusalem',
    )
    ss.share_with_anybody_for_writing()
    ss.prepare_set_values('A2:BS' % (row_count + 3), values)


def test_create_time_management_report():
    """Тестирует создание отчета по управлению временем."""
    doc_title = 'Тестовый документ'
    sheet_title = 'Тестовая таблица действий'
    values = [
        [
            'Действие',
            'Категория полезности',
            'Начато',
            'Завершено',
            'Потрачено',
        ],  # header row
        [
            'Обедаю',
            'Еда',
            '2 июл 2016 17:57:52',
            '2 июл 2016 18:43:45',
            '=D4-C4',
        ],
        [
            'Лёг полежать',
            'Отдых',
            '2 июл 2016 18:43:47',
            '2 июл 2016 18:53:36',
            '=D5-C5',
        ],
        [
            'Пью чай',
            'Еда',
            '2 июл 2016 18:53:39',
            '2 июл 2016 19:00:49',
            '=D6-C6',
        ],
        [
            'Пилю и шлифую большие щиты',
            'Ремонт',
            '2 июл 2016 19:00:52',
            '2 июл 2016 19:52:36',
            '=D7-C7',
        ],
        [
            'Собираю дверь шкафа',
            'Ремонт',
            '2 июл 2016 19:52:38',
            '2 июл 2016 21:11:21',
            '=D8-C8',
        ],
    ]
    row_count = len(values) - 1
    color_string_formatter_categories = {
        'Еда': html_color_to_json('#FFCCCC'),
        'Отдых': html_color_to_json('#CCFFCC'),
        'Ремонт': html_color_to_json('#CCCCFF'),
    }

    values2 = [
        ['Категория полезности', 'Потрачено'],  # header row
        ['Ремонт', '=E7+E8'],
        ['Еда', '=E4+E6'],
        ['Отдых', '=E5'],
    ]
    row_count2 = len(values2) - 1

    ss = ReachSpreadsheet()
    ss.create(
        doc_title,
        sheet_title,
        rows=row_count + 3,
        cols=8,
        locale='ru-RU',
        time_zone='Europe/Moscow',
    )
    ss.share_with_anybody_for_writing()

    ss.prepare_set_column_width(0, 400)
    ss.prepare_set_column_width(1, 200)
    ss.prepare_set_columns_width(2, 3, 165)
    ss.prepare_set_column_width(4, 100)
    ss.prepare_merge_cells('A1:E1')  # Merge A1:E1

    row_colors = [
        color_string_formatter_categories[value_row[1]]
        for value_row in values[1:]
    ]

    ss.prepare_set_cell_string_formatter(
        'A1:A1',
        {'textFormat': {'fontSize': 14}, 'horizontalAlignment': 'CENTER'},
    )  # Font size 14 and center aligment for A1 cell
    ss.prepare_set_cell_string_formatter(
        'A3:E3',
        {'textFormat': {'bold': True}, 'horizontalAlignment': 'CENTER'},
    )