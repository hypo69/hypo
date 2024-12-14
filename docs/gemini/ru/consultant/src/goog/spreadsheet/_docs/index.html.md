# Анализ кода модуля `index.html`

**Качество кода**
7/10
-  Плюсы
    - Код содержит подробное описание процесса создания Google-таблицы через API v4.
    -  Приведены примеры использования API с пояснениями.
    -  Представлен класс-обертка `Spreadsheet`, упрощающий взаимодействие с API.
 -  Минусы
    -   Код представляет собой HTML-документ, а не Python.
    -   Отсутствует структурированная документация в формате reStructuredText (RST).
    -   В коде не используются логирование ошибок с помощью `logger.error`.
    -   Не используются `j_loads` или `j_loads_ns` для загрузки JSON.
    -   Присутствует избыточное количество блоков try-finally.

**Рекомендации по улучшению**

1.  **Переписать код на Python:** Необходимо перенести логику создания и управления таблицами в файл Python.
2.  **Добавить RST-документацию:** Необходимо добавить docstring в формате RST для всех функций, методов и классов.
3.  **Использовать логирование:** Необходимо использовать `from src.logger.logger import logger` для логирования ошибок и заменить блоки `try-finally` на обработку ошибок через `logger.error`.
4.  **Использовать `j_loads`:** При загрузке JSON-файлов использовать `j_loads` или `j_loads_ns` из `src.utils.jjson`.
5.  **Улучшить структуру класса `Spreadsheet`:** Разбить методы класса на более мелкие и атомарные.
6.  **Упростить код:** Избавиться от избыточных проверок и лишних переменных.
7.  **Добавить примеры использования:** Добавить примеры использования класса `Spreadsheet` с документацией RST.

**Оптимизированный код**
```python
"""
Модуль для работы с Google Sheets API.
=========================================================================================

Этот модуль предоставляет класс :class:`Spreadsheet` для создания и управления Google-таблицами
через Google Sheets API v4.

Класс позволяет автоматизировать настройку ширины столбцов, заполнение ячеек данными,
объединение ячеек, настройку формата отображения, цвета фона и границ ячеек.

Пример использования
--------------------

Пример создания и настройки Google-таблицы с помощью класса `Spreadsheet`:

.. code-block:: python

    from src.goog.spreadsheet._docs.index import Spreadsheet
    import httplib2
    import apiclient.discovery
    from oauth2client.service_account import ServiceAccountCredentials
    from src.utils.jjson import j_loads_ns

    CREDENTIALS_FILE = 'test-proj-for-habr-article-1ab131d98a6b.json'

    credentials = ServiceAccountCredentials.from_json_keyfile_name(
        CREDENTIALS_FILE,
        ['https://www.googleapis.com/auth/spreadsheets',
         'https://www.googleapis.com/auth/drive']
    )
    httpAuth = credentials.authorize(httplib2.Http())
    service = apiclient.discovery.build('sheets', 'v4', http=httpAuth)
    drive_service = apiclient.discovery.build('drive', 'v3', http=httpAuth)


    spreadsheet = service.spreadsheets().create(body={
        'properties': {'title': 'Сие есть название документа', 'locale': 'ru_RU'},
        'sheets': [{'properties': {'sheetType': 'GRID',
                                   'sheetId': 0,
                                   'title': 'Сие есть название листа',
                                   'gridProperties': {'rowCount': 8, 'columnCount': 5}}}]
    }).execute()


    share_res = drive_service.permissions().create(
        fileId=spreadsheet['spreadsheetId'],
        body={'type': 'anyone', 'role': 'reader'},
        fields='id'
    ).execute()


    ss = Spreadsheet(service, spreadsheet['spreadsheetId'], 0, "Сие есть название листа")
    ss.prepare_setColumnWidth(0, 317)
    ss.prepare_setColumnWidth(1, 200)
    ss.prepare_setColumnsWidth(2, 3, 165)
    ss.prepare_setColumnWidth(4, 100)
    ss.prepare_mergeCells('A1:E1')
    ss.prepare_setValues('A1', [['Пример таблицы']])
    ss.prepare_setCellsFormat('A1', {'horizontalAlignment': 'CENTER', 'textFormat': {'fontSize': 14, 'bold': True}})
    ss.prepare_setValues('A3:E3', [['Дата', 'Операция', 'Время', 'Длительность', 'Осталось']])
    ss.prepare_setCellsFormat('A3:E3', {'horizontalAlignment': 'CENTER', 'textFormat': {'bold': True}})
    ss.prepare_setValues('A4:D8', [
        ['2 июл 2016 17:57:52', 'Запуск программы', '17:57:52', '00:00:00'],
        ['2 июл 2016 18:00:01', 'Открытие документа', '18:00:01', '00:02:09'],
        ['2 июл 2016 18:05:12', 'Импорт данных', '18:05:12', '00:05:11'],
        ['2 июл 2016 18:05:38', 'Сохранение документа', '18:05:38', '00:00:26'],
        ['2 июл 2016 18:06:01', 'Закрытие программы', '18:06:01', '00:00:23'],
    ])
    ss.prepare_setValues('E4', [['=D4-C4']])
    ss.prepare_setValues('E5', [['=D5-C5']])
    ss.prepare_setValues('E6', [['=D6-C6']])
    ss.prepare_setValues('E7', [['=D7-C7']])
    ss.prepare_setValues('E8', [['=D8-C8']])

    ss.prepare_setCellsFormat('E4:E8', {'numberFormat': {'pattern': '[h]:mm:ss', 'type': 'TIME'}},
                            fields='userEnteredFormat.numberFormat')
    ss.prepare_setBorders('A3:E3', 'bottom')

    ss.runPrepared()

"""
import httplib2
import apiclient.discovery
from oauth2client.service_account import ServiceAccountCredentials
from typing import List, Dict, Any, Tuple
from src.logger.logger import logger


class Spreadsheet:
    """
    Класс для работы с Google Sheets API.
    
    Предоставляет методы для настройки ширины столбцов, заполнения ячеек данными,
    объединения ячеек, настройки формата отображения, цвета фона и границ ячеек.
    """
    def __init__(self, service: apiclient.discovery.Resource, spreadsheet_id: str, sheet_id: int, sheet_title: str):
        """
        Инициализирует объект Spreadsheet.

        :param service: Объект сервиса Google Sheets API.
        :param spreadsheet_id: ID Google-таблицы.
        :param sheet_id: ID листа.
        :param sheet_title: Название листа.
        """
        self.service = service
        self.spreadsheetId = spreadsheet_id
        self.sheetId = sheet_id
        self.sheetTitle = sheet_title
        self.requests: List[Dict] = []
        self.valueRanges: List[Dict] = []

    def prepare_setDimensionPixelSize(self, dimension: str, start_index: int, end_index: int, pixel_size: int):
        """
        Подготавливает запрос на изменение размера столбца или строки.

        :param dimension: Тип измерения ("COLUMNS" или "ROWS").
        :param start_index: Индекс начала диапазона.
        :param end_index: Индекс конца диапазона (не включительно).
        :param pixel_size: Размер в пикселях.
        """
        self.requests.append({
            "updateDimensionProperties": {
                "range": {"sheetId": self.sheetId,
                          "dimension": dimension,
                          "startIndex": start_index,
                          "endIndex": end_index},
                "properties": {"pixelSize": pixel_size},
                "fields": "pixelSize"
            }
        })

    def prepare_setColumnsWidth(self, start_col: int, end_col: int, width: int):
        """
        Подготавливает запрос на изменение ширины нескольких столбцов.

        :param start_col: Индекс начального столбца.
        :param end_col: Индекс конечного столбца.
        :param width: Ширина в пикселях.
        """
        self.prepare_setDimensionPixelSize("COLUMNS", start_col, end_col + 1, width)

    def prepare_setColumnWidth(self, col: int, width: int):
        """
        Подготавливает запрос на изменение ширины одного столбца.

        :param col: Индекс столбца.
        :param width: Ширина в пикселях.
        """
        self.prepare_setColumnsWidth(col, col, width)

    def toGridRange(self, cells_range: str) -> Dict:
        """
        Преобразует A1-нотацию в GridRange.

        :param cells_range: Строка с диапазоном ячеек в формате A1.
        :return: Словарь с GridRange.
        """
        try:
            start_cell, end_cell = cells_range.split(":")
            start_col = self._excel_col_to_int(start_cell[0].upper())
            start_row = int(start_cell[1:]) - 1
            end_col = self._excel_col_to_int(end_cell[0].upper())
            end_row = int(end_cell[1:])
            return {
                    "sheetId": self.sheetId,
                    "startRowIndex": start_row,
                    "endRowIndex": end_row,
                    "startColumnIndex": start_col,
                    "endColumnIndex": end_col + 1
                }
        except Exception as e:
            logger.error(f"Ошибка преобразования диапазона ячеек {cells_range} в GridRange", exc_info=True)
            return {}
            

    def prepare_mergeCells(self, cells_range: str):
        """
        Подготавливает запрос на объединение ячеек.

        :param cells_range: Диапазон ячеек в формате A1.
        """
        grid_range = self.toGridRange(cells_range)
        if grid_range:
             self.requests.append({"mergeCells": {"range": grid_range, "mergeType": "MERGE_ALL"}})

    def prepare_setValues(self, cells_range: str, values: List[List[Any]], major_dimension: str = "ROWS"):
        """
        Подготавливает запрос на запись значений в ячейки.

        :param cells_range: Диапазон ячеек в формате A1.
        :param values: Список значений для записи.
        :param major_dimension: Направление записи ("ROWS" или "COLUMNS").
        """
        self.valueRanges.append({
            "range": f"{self.sheetTitle}!{cells_range}",
            "majorDimension": major_dimension,
            "values": values
        })

    def prepare_setCellsFormat(self, cells_range: str, cell_format: Dict, fields: str = "userEnteredFormat"):
        """
        Подготавливает запрос на форматирование ячеек.

        :param cells_range: Диапазон ячеек в формате A1.
        :param cell_format: Словарь с параметрами форматирования.
        :param fields: Поля для изменения.
        """
        grid_range = self.toGridRange(cells_range)
        if grid_range:
            self.requests.append({
            "repeatCell": {
                "range": grid_range,
                "cell": {"userEnteredFormat": cell_format},
                "fields": fields
            }
        })


    def prepare_setCellsFormats(self, cells_range: str, rows: List[List[Dict]]):
        """
        Подготавливает запрос на форматирование ячеек.

        :param cells_range: Диапазон ячеек в формате A1.
        :param rows: Список списков, где каждый внутренний список задает форматирование для строки.
        """
        grid_range = self.toGridRange(cells_range)
        if grid_range:
            self.requests.append({
                "updateCells": {
                "range": grid_range,
                "rows": [{"values": [{"userEnteredFormat": cell} for cell in row]} for row in rows],
                "fields": "userEnteredFormat"
                }
            })

    def prepare_setBorders(self, cells_range: str, border_position: str, style: str = "SOLID", width: int = 1,
                             color: Dict = {"red": 0, "green": 0, "blue": 0, "alpha": 1}):
        """
        Подготавливает запрос на установку границ ячеек.

        :param cells_range: Диапазон ячеек в формате A1.
        :param border_position: Положение границы ("top", "bottom", "left", "right").
        :param style: Стиль границы.
        :param width: Ширина границы.
        :param color: Цвет границы в формате RGB.
        """
        grid_range = self.toGridRange(cells_range)
        if grid_range:
            border = {
                "style": style,
                "width": width,
                "color": color
            }
            self.requests.append({
                "updateBorders": {
                    "range": grid_range,
                    border_position: border
                }
            })

    def runPrepared(self, value_input_option: str = "USER_ENTERED") -> Tuple[List[Dict], List[Dict]]:
        """
        Исполняет все подготовленные запросы.

        :param value_input_option: Параметр для spreadsheets.values.batchUpdate ("USER_ENTERED" или "RAW").
        :return: Кортеж с ответами на batchUpdate и batchUpdate values.
        """
        upd1_res:Dict = {'replies': []}
        upd2_res:Dict = {'responses': []}
        try:
            if self.requests:
                upd1_res = self.service.spreadsheets().batchUpdate(
                    spreadsheetId=self.spreadsheetId,
                    body={"requests": self.requests}
                ).execute()
            if self.valueRanges:
                upd2_res = self.service.spreadsheets().values().batchUpdate(
                    spreadsheetId=self.spreadsheetId,
                    body={"valueInputOption": value_input_option, "data": self.valueRanges}
                ).execute()
        except Exception as ex:
            logger.error(f"Ошибка при выполнении запросов к таблице {self.spreadsheetId}", exc_info=True)
        finally:
            self.requests = []
            self.valueRanges = []
        return upd1_res['replies'], upd2_res['responses']

    def _excel_col_to_int(self, col: str) -> int:
      """
      Преобразует буквенное обозначение столбца в целое число.

      :param col: Буквенное обозначение столбца, например "A" или "AA".
      :return: Целое число, представляющее столбец (A=0, B=1, ... AA=26).
      """
      result = 0
      for char in col:
          result = result * 26 + (ord(char) - ord('A'))
      return result