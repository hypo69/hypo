# Анализ кода модуля `src.goog.spreadsheet._docs`

**Качество кода**
6/10
 - Плюсы
    - Код содержит подробное описание процесса создания и настройки Google-таблиц с использованием Google Sheets API v4.
    - Приведены примеры кода для основных операций, таких как создание таблицы, установка ширины столбцов, ввод данных, объединение ячеек и форматирование.
    - Код содержит класс-обертку `Spreadsheet`, который инкапсулирует взаимодействие с Google Sheets API, что упрощает дальнейшее использование.
 - Минусы
    - В коде отсутствуют docstring для функций и классов.
    - Используются стандартные блоки try-except, что затрудняет отслеживание ошибок.
    - Есть избыточное дублирование кода и комментарии, которые можно вынести в docstring.
    - Не все функции и классы имеют описание назначения.
    - В коде присутствуют прямые вызовы к API Google, что может привести к сложностям при изменении версии API.

**Рекомендации по улучшению**

1.  Добавить docstring к модулю, классам и функциям, следуя стандарту Sphinx.
2.  Улучшить обработку ошибок с помощью `logger.error` и избегать использования стандартных блоков `try-except` без необходимости.
3.  Реализовать логирование всех операций, чтобы отслеживать ход выполнения и ошибки.
4.  Использовать константы вместо жёстко заданных значений, чтобы повысить гибкость кода.
5.  Разделить класс `Spreadsheet` на более мелкие классы или функции, чтобы снизить его сложность.
6.  Оптимизировать код для повторного использования, например, создавая общие функции для формирования запросов к API.
7.  Использовать `j_loads` или `j_loads_ns` из `src.utils.jjson` для работы с JSON-файлами.
8.  Избегать прямого использования API Google, создавая абстракции для лучшей масштабируемости и гибкости.
9.  Добавить примеры использования для каждой функции в docstring.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
"""
Модуль для создания и настройки Google Sheets документов.
=========================================================================================

Этот модуль предоставляет функциональность для программного создания и настройки Google Sheets документов,
используя Google Sheets API v4. Он включает класс `Spreadsheet`, который облегчает выполнение операций, таких как
создание документа, настройка ширины столбцов, добавление данных, форматирование ячеек и другие.

Пример использования
--------------------

Пример создания нового документа с форматированием:

.. code-block:: python

    from src.goog.spreadsheet._docs import Spreadsheet
    import httplib2
    from apiclient import discovery
    from oauth2client.service_account import ServiceAccountCredentials

    CREDENTIALS_FILE = 'path/to/your/credentials.json'
    SCOPES = [
        'https://www.googleapis.com/auth/spreadsheets',
        'https://www.googleapis.com/auth/drive'
    ]

    credentials = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILE, SCOPES)
    http_auth = credentials.authorize(httplib2.Http())
    service = discovery.build('sheets', 'v4', http=http_auth)
    drive_service = discovery.build('drive', 'v3', http=http_auth)

    ss = Spreadsheet(service, drive_service)
    ss.create_spreadsheet()
    ss.set_column_width(0, 317)
    ss.set_column_width(1, 200)
    ss.set_columns_width(2, 3, 165)
    ss.set_column_width(4, 100)
    ss.set_values("B2:C3", [["This is B2", "This is C2"], ["This is B3", "This is C3"]])
    ss.set_values("D5:E6", [["This is D5", "This is D6"], ["This is E5", "=5+5"]], major_dimension="COLUMNS")
    ss.run_prepared()
"""
from src.logger.logger import logger
import httplib2
from apiclient import discovery
from oauth2client.service_account import ServiceAccountCredentials
from typing import Any, Dict, List
from pathlib import Path

MODE = 'debug'

class Spreadsheet:
    """
    Класс для работы с Google Sheets API v4.

    Предоставляет методы для создания, настройки и управления Google Sheets документами.
    Инкапсулирует взаимодействие с API Google Sheets.

    Attributes:
        service (googleapiclient.discovery.Resource): Сервис Google Sheets API.
        drive_service (googleapiclient.discovery.Resource): Сервис Google Drive API.
        spreadsheet_id (str): Идентификатор Google Sheets документа.
        sheet_id (int): Идентификатор листа.
        sheet_title (str): Название листа.
        requests (list): Список запросов для выполнения через batchUpdate.
        value_ranges (list): Список диапазонов значений для записи через batchUpdate.
    """
    def __init__(self, service: discovery.Resource, drive_service: discovery.Resource, spreadsheet_id: str = None, sheet_id: int = 0, sheet_title: str = 'Sheet1'):
        """
        Инициализирует объект Spreadsheet.

        Args:
            service (googleapiclient.discovery.Resource): Сервис Google Sheets API.
            drive_service (googleapiclient.discovery.Resource): Сервис Google Drive API.
            spreadsheet_id (str, optional): Идентификатор Google Sheets документа. Defaults to None.
            sheet_id (int, optional): Идентификатор листа. Defaults to 0.
            sheet_title (str, optional): Название листа. Defaults to 'Sheet1'.
        """
        self.service = service
        self.drive_service = drive_service
        self.spreadsheet_id = spreadsheet_id
        self.sheet_id = sheet_id
        self.sheet_title = sheet_title
        self.requests: List[Dict[str, Any]] = []
        self.value_ranges: List[Dict[str, Any]] = []
    def create_spreadsheet(self, title: str = 'New Spreadsheet', locale: str = 'ru_RU', row_count: int = 8, column_count: int = 5, sheet_title: str = 'Sheet1') -> None:
        """
        Создает новый Google Spreadsheet документ.

        Args:
            title (str, optional): Название документа. Defaults to 'New Spreadsheet'.
            locale (str, optional): Локаль документа. Defaults to 'ru_RU'.
            row_count (int, optional): Количество строк в листе. Defaults to 8.
            column_count (int, optional): Количество столбцов в листе. Defaults to 5.
            sheet_title (str, optional): Название листа. Defaults to 'Sheet1'.
        """
        try:
            spreadsheet = self.service.spreadsheets().create(body={
                'properties': {'title': title, 'locale': locale},
                'sheets': [{
                    'properties': {
                        'sheetType': 'GRID',
                        'sheetId': 0,
                        'title': sheet_title,
                        'gridProperties': {'rowCount': row_count, 'columnCount': column_count}
                    }
                }]
            }).execute()
            self.spreadsheet_id = spreadsheet['spreadsheetId']
            logger.info(f'Документ {self.spreadsheet_id} успешно создан.')
            self.share_document()
        except Exception as ex:
            logger.error(f'Ошибка создания документа', exc_info=ex)
            ...
    def share_document(self, permission_type: str = 'anyone', role: str = 'reader', email: str = None) -> None:
        """
        Предоставляет доступ к созданному документу.

        Args:
            permission_type (str, optional): Тип доступа ('anyone' или 'user'). Defaults to 'anyone'.
            role (str, optional): Роль пользователя ('reader' или 'writer'). Defaults to 'reader'.
            email (str, optional): Email пользователя, если permission_type='user'. Defaults to None.
        """
        try:
            if permission_type == 'anyone':
                body = {'type': 'anyone', 'role': role}
            elif permission_type == 'user' and email:
                body = {'type': 'user', 'role': role, 'emailAddress': email}
            else:
                 logger.error(f'Некорректные параметры для предоставления доступа')
                 return

            self.drive_service.permissions().create(
                fileId=self.spreadsheet_id,
                body=body,
                fields='id'
            ).execute()
            logger.info(f'Доступ к документу {self.spreadsheet_id} успешно предоставлен.')

        except Exception as ex:
            logger.error(f'Ошибка предоставления доступа к документу {self.spreadsheet_id}', exc_info=ex)
            ...

    def _prepare_set_dimension_pixel_size(self, dimension: str, start_index: int, end_index: int, pixel_size: int) -> None:
        """
        Подготавливает запрос на изменение ширины столбца или высоты строки.

        Args:
            dimension (str): 'COLUMNS' для столбцов, 'ROWS' для строк.
            start_index (int): Индекс начала диапазона.
            end_index (int): Индекс конца диапазона (не включая).
            pixel_size (int): Ширина в пикселях.
        """
        self.requests.append({
            'updateDimensionProperties': {
                'range': {'sheetId': self.sheet_id, 'dimension': dimension, 'startIndex': start_index, 'endIndex': end_index},
                'properties': {'pixelSize': pixel_size},
                'fields': 'pixelSize'
            }
        })

    def set_columns_width(self, start_col: int, end_col: int, width: int) -> None:
        """
        Устанавливает ширину для нескольких столбцов.

        Args:
            start_col (int): Индекс первого столбца.
            end_col (int): Индекс последнего столбца.
            width (int): Ширина столбцов в пикселях.
        """
        self._prepare_set_dimension_pixel_size('COLUMNS', start_col, end_col + 1, width)

    def set_column_width(self, col: int, width: int) -> None:
         """
        Устанавливает ширину для одного столбца.

        Args:
            col (int): Индекс столбца.
            width (int): Ширина столбца в пикселях.
        """
        self.set_columns_width(col, col, width)

    def _prepare_set_values(self, cells_range: str, values: List[List[Any]], major_dimension: str = 'ROWS') -> None:
         """
        Подготавливает запрос на запись данных в ячейки.

        Args:
            cells_range (str): Диапазон ячеек (например, 'A1:B2').
            values (List[List[Any]]): Данные для записи в виде списка списков.
            major_dimension (str, optional): 'ROWS' или 'COLUMNS'. Defaults to 'ROWS'.
        """
        self.value_ranges.append({'range': self.sheet_title + '!' + cells_range, 'majorDimension': major_dimension, 'values': values})

    def set_values(self, cells_range: str, values: List[List[Any]], major_dimension: str = 'ROWS') -> None:
        """
        Записывает данные в указанный диапазон ячеек.

        Args:
            cells_range (str): Диапазон ячеек (например, 'A1:B2').
            values (List[List[Any]]): Данные для записи в виде списка списков.
            major_dimension (str, optional): 'ROWS' или 'COLUMNS'. Defaults to 'ROWS'.
        """
        self._prepare_set_values(cells_range, values, major_dimension)

    def _prepare_merge_cells(self, cells_range: str) -> None:
        """
        Подготавливает запрос на объединение ячеек.

        Args:
            cells_range (str): Диапазон ячеек для объединения (например, 'A1:B2').
        """
        grid_range = self._to_grid_range(cells_range)
        self.requests.append({'mergeCells': {'range': grid_range, 'mergeType': 'MERGE_ALL'}})

    def merge_cells(self, cells_range: str) -> None:
         """
        Объединяет указанный диапазон ячеек.

        Args:
            cells_range (str): Диапазон ячеек для объединения (например, 'A1:B2').
        """
        self._prepare_merge_cells(cells_range)

    def _prepare_set_cells_format(self, cells_range: str, cell_format: Dict[str, Any], fields: str = 'userEnteredFormat') -> None:
         """
        Подготавливает запрос на форматирование ячеек.

        Args:
            cells_range (str): Диапазон ячеек для форматирования (например, 'A1:B2').
            cell_format (Dict[str, Any]): Словарь с параметрами форматирования.
            fields (str, optional): Поле для форматирования. Defaults to 'userEnteredFormat'.
        """
        grid_range = self._to_grid_range(cells_range)
        self.requests.append({
            'repeatCell': {
                'range': grid_range,
                'cell': {'userEnteredFormat': cell_format},
                'fields': fields
            }
        })
    def set_cells_format(self, cells_range: str, cell_format: Dict[str, Any], fields: str = 'userEnteredFormat') -> None:
        """
        Устанавливает формат для диапазона ячеек.

        Args:
            cells_range (str): Диапазон ячеек для форматирования (например, 'A1:B2').
            cell_format (Dict[str, Any]): Словарь с параметрами форматирования.
            fields (str, optional): Поле для форматирования. Defaults to 'userEnteredFormat'.
        """
        self._prepare_set_cells_format(cells_range, cell_format, fields)

    def _prepare_set_cells_formats(self, cells_range: str, cell_formats: List[List[Dict[str, Any]]], fields: str = 'userEnteredFormat') -> None:
        """
        Подготавливает запрос на установку формата для каждой ячейки в указанном диапазоне.

        Args:
            cells_range (str): Диапазон ячеек для форматирования (например, 'A1:B2').
            cell_formats (List[List[Dict[str, Any]]]): Список списков словарей с параметрами форматирования.
            fields (str, optional): Поле для форматирования. Defaults to 'userEnteredFormat'.
         """
        grid_range = self._to_grid_range(cells_range)
        rows = [{'values': [{'userEnteredFormat': fmt} for fmt in row]} for row in cell_formats]
        self.requests.append({
            'updateCells': {
                'range': grid_range,
                'rows': rows,
                'fields': fields
            }
        })
    def set_cells_formats(self, cells_range: str, cell_formats: List[List[Dict[str, Any]]], fields: str = 'userEnteredFormat') -> None:
        """
        Устанавливает формат для каждой ячейки в указанном диапазоне.

        Args:
            cells_range (str): Диапазон ячеек для форматирования (например, 'A1:B2').
            cell_formats (List[List[Dict[str, Any]]]): Список списков словарей с параметрами форматирования.
            fields (str, optional): Поле для форматирования. Defaults to 'userEnteredFormat'.
        """
        self._prepare_set_cells_formats(cells_range, cell_formats, fields)

    def _prepare_set_borders(self, cells_range: str, border_style: Dict[str, Any]) -> None:
        """
        Подготавливает запрос на установку границ ячеек.

        Args:
            cells_range (str): Диапазон ячеек (например, 'A1:B2').
            border_style (Dict[str, Any]): Параметры границ.
        """
        grid_range = self._to_grid_range(cells_range)
        self.requests.append({'updateBorders': {'range': grid_range, **border_style}})

    def set_borders(self, cells_range: str, border_style: Dict[str, Any]) -> None:
        """
        Устанавливает границы для диапазона ячеек.

        Args:
             cells_range (str): Диапазон ячеек (например, 'A1:B2').
             border_style (Dict[str, Any]): Параметры границ.
        """
        self._prepare_set_borders(cells_range, border_style)
    def _to_grid_range(self, cells_range: str) -> Dict[str, int]:
        """
        Преобразует строковый диапазон ячеек в объект GridRange.

        Args:
            cells_range (str): Строковый диапазон ячеек (например, 'A1:B2').

        Returns:
            Dict[str, int]: Объект GridRange.
        """
        try:
            parts = cells_range.split('!')[-1].split(':')
            start_col, start_row = self._excel_to_int(parts[0])
            end_col, end_row = self._excel_to_int(parts[1]) if len(parts) > 1 else (start_col, start_row)
            return {
                'sheetId': self.sheet_id,
                'startRowIndex': start_row - 1,
                'endRowIndex': end_row,
                'startColumnIndex': start_col - 1,
                'endColumnIndex': end_col
            }
        except Exception as ex:
            logger.error(f'Ошибка преобразования диапазона ячеек {cells_range} в GridRange', exc_info=ex)
            ...
            return {}

    def _excel_to_int(self, cell: str) -> tuple[int, int]:
        """
        Преобразует адрес ячейки в Excel-стиле в числовые координаты.

        Args:
            cell (str): Адрес ячейки в Excel-стиле (например, 'A1').

        Returns:
            tuple[int, int]: Кортеж с номером столбца и номером строки.
        """
        col_str = ''
        row_str = ''
        for char in cell:
            if char.isalpha():
                col_str += char.upper()
            elif char.isdigit():
                row_str += char
        col = 0
        for i, char in enumerate(reversed(col_str)):
            col += (ord(char) - ord('A') + 1) * (26 ** i)
        row = int(row_str) if row_str else 0
        return col, row

    def run_prepared(self, value_input_option: str = 'USER_ENTERED') -> tuple[list, list]:
        """
        Выполняет все подготовленные запросы к Google Sheets API.

        Args:
            value_input_option (str, optional): Опция ввода значений. Defaults to 'USER_ENTERED'.

        Returns:
            tuple[list, list]: Кортеж с результатами выполнения batchUpdate и batchUpdate значений.
        """
        upd1_res = {'replies': []}
        upd2_res = {'responses': []}
        try:
            if self.requests:
                upd1_res = self.service.spreadsheets().batchUpdate(
                    spreadsheetId=self.spreadsheet_id,
                    body={'requests': self.requests}
                ).execute()
                logger.debug(f'Результат batchUpdate: {upd1_res}')
            if self.value_ranges:
                upd2_res = self.service.spreadsheets().values().batchUpdate(
                    spreadsheetId=self.spreadsheet_id,
                    body={'valueInputOption': value_input_option, 'data': self.value_ranges}
                ).execute()
                logger.debug(f'Результат batchUpdate values: {upd2_res}')
        except Exception as ex:
             logger.error(f'Ошибка выполнения запросов к документу {self.spreadsheet_id}', exc_info=ex)
             ...
        finally:
            self.requests = []
            self.value_ranges = []
        return upd1_res['replies'], upd2_res['responses']

if __name__ == '__main__':
    # Пример использования
    CREDENTIALS_FILE = 'test-proj-for-habr-article-1ab131d98a6b.json' # имя файла с закрытым ключом
    SCOPES = [
        'https://www.googleapis.com/auth/spreadsheets',
        'https://www.googleapis.com/auth/drive'
    ]

    credentials = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILE, SCOPES)
    http_auth = credentials.authorize(httplib2.Http())
    service = discovery.build('sheets', 'v4', http=http_auth)
    drive_service = discovery.build('drive', 'v3', http=http_auth)

    ss = Spreadsheet(service, drive_service)
    ss.create_spreadsheet(title='Таблица для хабра', sheet_title='Лист1')
    ss.set_column_width(0, 317)
    ss.set_column_width(1, 200)
    ss.set_columns_width(2, 3, 165)
    ss.set_column_width(4, 100)
    ss.set_values("A1", [["Пример таблицы"]])
    ss.merge_cells("A1:E1")
    ss.set_values("A3:E3", [["Дата", "Название", "Длительность", "Продолжительность", "Разница"]], major_dimension="ROWS")
    ss.set_cells_format("A3:E3", {'horizontalAlignment': 'CENTER', 'textFormat': {'bold': True}})
    ss.set_borders("A3:E3", {'bottom': {'style': 'SOLID', 'width': 1, 'color': {'red': 0, 'green': 0, 'blue': 0, 'alpha': 1}}})
    ss.set_values("A4:A8", [["2 июл 2016 17:57:52"], ["2 июл 2016 18:00:33"], ["2 июл 2016 18:04:40"], ["2 июл 2016 18:06:52"], ["2 июл 2016 18:10:00"]])
    ss.set_values("B4:B8", [["Работа", "Работа", "Работа", "Работа", "Работа"]])
    ss.set_values("C4:C8", [["0:01:00"], ["0:02:00"], ["0:04:00"], ["0:02:00"], ["0:02:00"]])
    ss.set_values("D4:D8", [["=A4-A3"], ["=A5-A4"], ["=A6-A5"], ["=A7-A6"], ["=A8-A7"]])
    ss.set_values("E4:E8", [["=D4-C4"], ["=D5-C5"], ["=D6-C6"], ["=D7-C7"], ["=D8-C8"]])
    ss.set_cells_format("E4:E8", {'numberFormat': {'pattern': '[h]:mm:ss', 'type': 'TIME'}}, fields='userEnteredFormat.numberFormat')
    ss.set_cells_formats("B4:C5", [[{'backgroundColor': {'red': 1, 'green': 0, 'blue': 0}},
                                     {'backgroundColor': {'red': 0, 'green': 1, 'blue': 0}}],
                                    [{'backgroundColor': {'red': 0, 'green': 0, 'blue': 1}},
                                     {'backgroundColor': {'red': 1, 'green': 1, 'blue': 0}}]])

    ss.run_prepared()