# Анализ кода модуля `_docs`

**Качество кода: 6/10**
-   **Плюсы:**
    - Код предоставляет подробное руководство по использованию Google Sheets API v4 для создания и форматирования таблиц.
    - Содержит разбор терминологии и основных концепций API.
    -  Представлены примеры кода, демонстрирующие создание сервисного объекта, настройку доступа к документу, установку ширины столбцов, заполнение ячеек данными и форматирование ячеек.
    -  Используется класс-обертка Spreadsheet, который упрощает работу с API.
-   **Минусы:**
    -   Код представляет собой HTML-документ, а не Python.
    -   Отсутствуют docstring и комментарии в формате reStructuredText (RST).
    -   Не используется логгирование ошибок с помощью `src.logger.logger`.
    -   Присутствует избыточное использование `try-except` блоков.
    -   Не используется `j_loads` или `j_loads_ns` для чтения файлов (хотя в данном коде нет операций чтения).
    -   Не все переменные и функции имеют описательные имена, соответствующие ранее обработанным файлам.

**Рекомендации по улучшению:**

1.  **Преобразование в Python**: Необходимо преобразовать HTML-код в исполняемый Python-код, разбив его на модули и классы.
2.  **Документация в RST**: Добавить docstring в формате reStructuredText (RST) для всех модулей, классов, методов и функций.
3.  **Логгирование**: Использовать `from src.logger.logger import logger` для логирования ошибок и предупреждений.
4.  **Обработка ошибок**: Избегать избыточного использования `try-except`, предпочтительно логирование ошибок с помощью `logger.error`.
5.  **Именование**: Привести в соответствие имена функций, переменных и импортов с ранее обработанными файлами.
6. **Файловый ввод/вывод**: Использовать `j_loads` или `j_loads_ns` при работе с файлами (если требуется).

**Оптимизированный код**
```python
"""
Модуль для работы с Google Sheets API v4.
========================================

Этот модуль предоставляет класс `Spreadsheet` для создания, форматирования и
манипуляции Google-таблицами. Он включает в себя методы для настройки
ширины столбцов, объединения ячеек, заполнения данными, применения
форматирования, и других операций.

Пример использования
--------------------

.. code-block:: python

    from src.goog.spreadsheet._docs.spreadsheet import Spreadsheet
    from src.utils.jjson import j_loads
    from src.logger.logger import logger
    from oauth2client.service_account import ServiceAccountCredentials
    import httplib2
    import apiclient.discovery


    # Загрузка учетных данных
    CREDENTIALS_FILE = 'path/to/your/credentials.json'
    credentials = ServiceAccountCredentials.from_json_keyfile_name(
        CREDENTIALS_FILE,
        ['https://www.googleapis.com/auth/spreadsheets',
         'https://www.googleapis.com/auth/drive']
    )
    http_auth = credentials.authorize(httplib2.Http())
    service = apiclient.discovery.build('sheets', 'v4', http=http_auth)
    drive_service = apiclient.discovery.build('drive', 'v3', http=http_auth)

    # Создание экземпляра класса Spreadsheet
    spreadsheet = Spreadsheet(service=service, drive_service=drive_service)
    spreadsheet.create_spreadsheet(title='Test Document', locale='ru_RU')


    # Настройка ширины столбцов
    spreadsheet.prepare_set_column_width(0, 317)
    spreadsheet.prepare_set_column_width(1, 200)
    spreadsheet.prepare_set_columns_width(2, 3, 165)
    spreadsheet.prepare_set_column_width(4, 100)

    # Заполнение ячеек данными
    spreadsheet.prepare_set_values("B2:C3", [["This is B2", "This is C2"], ["This is B3", "This is C3"]])
    spreadsheet.prepare_set_values("D5:E6", [["This is D5", "This is D6"], ["This is E5", "=5+5"]], "COLUMNS")

    # Объединение ячеек
    spreadsheet.prepare_merge_cells('A1:E1')

    # Форматирование ячеек
    spreadsheet.prepare_set_cells_format('A3:E3', {'horizontalAlignment': 'CENTER', 'textFormat': {'bold': True}})
    spreadsheet.prepare_set_cells_format('E4:E8', {'numberFormat': {'pattern': '[h]:mm:ss', 'type': 'TIME'}}, fields='userEnteredFormat.numberFormat')
    spreadsheet.prepare_set_cells_formats('B4:C5', [[{'backgroundColor': {'red': 1, 'green': 0, 'blue': 0}},
                                      {'backgroundColor': {'red': 0, 'green': 1, 'blue': 0}}],
                                     [{'backgroundColor': {'red': 0, 'green': 0, 'blue': 1}},
                                      {'backgroundColor': {'red': 1, 'green': 1, 'blue': 0}}]])

    # Настройка границ
    spreadsheet.prepare_set_borders('A3:E3', bottom={'style': 'SOLID', 'width': 1, 'color': {'red': 0, 'green': 0, 'blue': 0, 'alpha': 1}})
    # Выполнение подготовленных запросов
    spreadsheet.run_prepared()

"""
from src.utils.jjson import j_loads
from src.logger.logger import logger
from typing import Any, Dict, List, Tuple
import httplib2
import apiclient.discovery
# from oauth2client.service_account import ServiceAccountCredentials # убрали так как импорт в примере использования

MODE = 'debug'


class Spreadsheet:
    """
    Класс для управления Google-таблицами через Google Sheets API v4.

    :param service: Сервисный объект Google Sheets API.
    :param drive_service: Сервисный объект Google Drive API.
    :param spreadsheet_id: Идентификатор Google-таблицы.
    :param sheet_id: Идентификатор листа в Google-таблице.
    :param sheet_title: Название листа в Google-таблице.
    """
    def __init__(self, service: Any, drive_service: Any, spreadsheet_id: str = None, sheet_id: int = 0, sheet_title: str = 'Sheet1'):
        """
        Инициализирует объект Spreadsheet.
        """
        self.service = service
        self.drive_service = drive_service
        self.spreadsheetId = spreadsheet_id
        self.sheetId = sheet_id
        self.sheetTitle = sheet_title
        self.requests = []
        self.valueRanges = []


    def create_spreadsheet(self, title: str, locale: str = 'ru_RU', row_count: int = 8, column_count: int = 5) -> None:
        """
        Создает новую Google-таблицу.

        :param title: Название Google-таблицы.
        :param locale: Локаль Google-таблицы.
        :param row_count: Количество строк в листе.
        :param column_count: Количество столбцов в листе.
        """
        try:
            spreadsheet = self.service.spreadsheets().create(body={
                'properties': {'title': title, 'locale': locale},
                'sheets': [{'properties': {'sheetType': 'GRID',
                                           'sheetId': self.sheetId,
                                           'title': self.sheetTitle,
                                           'gridProperties': {'rowCount': row_count, 'columnCount': column_count}}}]
            }).execute()
            self.spreadsheetId = spreadsheet['spreadsheetId']
            self.share_spreadsheet()
        except Exception as ex:
            logger.error('Ошибка создания Google-таблицы', ex)


    def share_spreadsheet(self, email: str = None, role: str = 'reader') -> None:
        """
        Настраивает доступ к Google-таблице.

        :param email: Email пользователя для предоставления доступа.
                    Если не указан, предоставляет доступ на чтение всем.
        :param role: Роль пользователя (reader или writer).
        """
        try:
            if email:
                body = {'type': 'user', 'role': role, 'emailAddress': email}
            else:
                body = {'type': 'anyone', 'role': role}
            self.drive_service.permissions().create(
                fileId=self.spreadsheetId,
                body=body,
                fields='id'
            ).execute()
        except Exception as ex:
           logger.error('Ошибка предоставления доступа к Google-таблице', ex)


    def prepare_set_dimension_pixel_size(self, dimension: str, start_index: int, end_index: int, pixel_size: int) -> None:
         """
         Подготавливает запрос на установку размера столбца или строки в пикселях.
         :param dimension: Тип измерения (COLUMNS или ROWS).
         :param start_index: Индекс начала диапазона.
         :param end_index: Индекс конца диапазона (не включая).
         :param pixel_size: Размер в пикселях.
         """
         self.requests.append({
             "updateDimensionProperties": {
                 "range": {
                     "sheetId": self.sheetId,
                     "dimension": dimension,
                     "startIndex": start_index,
                     "endIndex": end_index
                 },
                 "properties": {
                     "pixelSize": pixel_size
                 },
                 "fields": "pixelSize"
             }
         })


    def prepare_set_columns_width(self, start_col: int, end_col: int, width: int) -> None:
        """
        Подготавливает запрос на установку ширины нескольких столбцов.

        :param start_col: Индекс первого столбца.
        :param end_col: Индекс последнего столбца.
        :param width: Ширина в пикселях.
        """
        self.prepare_set_dimension_pixel_size("COLUMNS", start_col, end_col + 1, width)


    def prepare_set_column_width(self, col: int, width: int) -> None:
        """
        Подготавливает запрос на установку ширины одного столбца.

        :param col: Индекс столбца.
        :param width: Ширина в пикселях.
        """
        self.prepare_set_columns_width(col, col, width)


    def prepare_set_values(self, cells_range: str, values: List[List[Any]], major_dimension: str = "ROWS") -> None:
        """
        Подготавливает запрос на установку значений в диапазоне ячеек.

        :param cells_range: Диапазон ячеек (например, "A1:B2").
        :param values: Список значений для записи в ячейки.
        :param major_dimension: Направление записи (ROWS или COLUMNS).
        """
        self.valueRanges.append({
            "range": self.sheetTitle + "!" + cells_range,
            "majorDimension": major_dimension,
            "values": values
        })


    def prepare_merge_cells(self, cells_range: str, merge_type: str = 'MERGE_ALL') -> None:
        """
        Подготавливает запрос на объединение ячеек.

        :param cells_range: Диапазон ячеек для объединения (например, "A1:C3").
        :param merge_type: Тип объединения (MERGE_ALL, MERGE_COLUMNS, MERGE_ROWS).
        """
        grid_range = self.to_grid_range(cells_range)
        self.requests.append({
            'mergeCells': {
                'range': grid_range,
                'mergeType': merge_type
            }
        })


    def prepare_set_cells_format(self, cells_range: str, cell_format: Dict, fields: str = 'userEnteredFormat') -> None:
        """
         Подготавливает запрос на форматирование ячеек.

         :param cells_range: Диапазон ячеек для форматирования.
         :param cell_format: Словарь с параметрами форматирования.
         :param fields: Поля для обновления в формате (например,
                         'userEnteredFormat' или 'userEnteredFormat.numberFormat').
         """
        grid_range = self.to_grid_range(cells_range)
        self.requests.append({
            'repeatCell': {
                'range': grid_range,
                'cell': {
                    'userEnteredFormat': cell_format
                },
                'fields': fields
            }
        })


    def prepare_set_cells_formats(self, cells_range: str, formats: List[List[Dict]], fields: str = 'userEnteredFormat') -> None:
         """
         Подготавливает запрос на индивидуальное форматирование каждой ячейки в диапазоне.

         :param cells_range: Диапазон ячеек (например, "A1:B2").
         :param formats: Двумерный список словарей с параметрами форматирования
                       для каждой ячейки.
         :param fields: Поля для обновления в формате (например, 'userEnteredFormat').
         """
         grid_range = self.to_grid_range(cells_range)
         rows = [{'values': [{'userEnteredFormat': fmt} for fmt in row]} for row in formats]
         self.requests.append({
             'updateCells': {
                 'range': grid_range,
                 'rows': rows,
                 'fields': fields
             }
         })


    def prepare_set_borders(self, cells_range: str,
                            top: Dict = None,
                            bottom: Dict = None,
                            left: Dict = None,
                            right: Dict = None) -> None:
        """
         Подготавливает запрос на установку границ ячеек.

         :param cells_range: Диапазон ячеек.
         :param top: Параметры верхней границы.
         :param bottom: Параметры нижней границы.
         :param left: Параметры левой границы.
         :param right: Параметры правой границы.
         """
        grid_range = self.to_grid_range(cells_range)
        borders = {}
        if top:
            borders['top'] = top
        if bottom:
            borders['bottom'] = bottom
        if left:
            borders['left'] = left
        if right:
             borders['right'] = right
        self.requests.append({
             'updateBorders': {
                 'range': grid_range,
                 **borders
              }
         })


    def run_prepared(self, value_input_option: str = "USER_ENTERED") -> Tuple[List[Dict], List[Dict]]:
        """
        Выполняет подготовленные запросы к Google Sheets API.

        :param value_input_option: Опция интерпретации вводимых значений
                                    (USER_ENTERED или RAW).
        :return: Кортеж, содержащий ответы от batchUpdate и batchUpdate values.
        """
        upd1_res = {'replies': []}
        upd2_res = {'responses': []}
        try:
             if len(self.requests) > 0:
                 upd1_res = self.service.spreadsheets().batchUpdate(
                     spreadsheetId=self.spreadsheetId,
                     body={"requests": self.requests}
                 ).execute()
             if len(self.valueRanges) > 0:
                 upd2_res = self.service.spreadsheets().values().batchUpdate(
                     spreadsheetId=self.spreadsheetId,
                     body={"valueInputOption": value_input_option,
                           "data": self.valueRanges}
                 ).execute()
        except Exception as ex:
            logger.error('Ошибка при выполнении запросов к Google Sheets API', ex)
        finally:
             self.requests = []
             self.valueRanges = []
        return upd1_res.get('replies', []), upd2_res.get('responses', [])


    def to_grid_range(self, cells_range: str) -> Dict:
         """
         Преобразует диапазон ячеек в формат GridRange.

         :param cells_range: Диапазон ячеек (например, "A1:B2").
         :return: Словарь, представляющий GridRange.
         """
         parts = cells_range.split('!')
         if len(parts) > 1:
              cells = parts[1]
         else:
            cells = parts[0]
         start_cell, end_cell = cells.split(':')
         start_col = ord(start_cell[0].upper()) - ord('A')
         start_row = int(start_cell[1:]) - 1
         end_col = ord(end_cell[0].upper()) - ord('A')
         end_row = int(end_cell[1:])
         return {
             'sheetId': self.sheetId,
             'startRowIndex': start_row,
             'endRowIndex': end_row,
             'startColumnIndex': start_col,
             'endColumnIndex': end_col + 1
         }