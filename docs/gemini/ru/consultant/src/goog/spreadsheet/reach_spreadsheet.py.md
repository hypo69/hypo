# Анализ кода модуля `reach_spreadsheet.py`

**Качество кода: 7/10**
-   **Плюсы:**
    -   Код хорошо структурирован и разделен на функции, что облегчает его понимание и поддержку.
    -   Используются классы для представления сущностей (например, `ReachSpreadsheet`, `SpreadsheetError`).
    -   Присутствует обработка исключений, хотя и есть место для улучшений.
    -   Есть базовые тесты для основных функций.
    -   Используется `pprint` для отладочного вывода.
-   **Минусы:**
    -   Многократное использование `try-except` без конкретной обработки исключений.
    -   Отсутствует полная документация в формате RST.
    -   Некоторые импорты могут быть оптимизированы.
    -   Используются устаревшие подходы (например, прямой доступ к элементам словаря с `['ключ']`).
    -   Не используются константы для magic strings.
    -   Не везде используется `logger.error` для логирования ошибок.

**Рекомендации по улучшению**
1.  **Документация**:
    -   Добавить docstring в формате RST для каждого класса, метода и функции.
    -   Описать назначение модуля в начале файла.
2.  **Обработка ошибок**:
    -   Заменить общие блоки `try-except` на использование `logger.error` для более информативного логирования.
    -   Рассмотреть возможность создания кастомных исключений для специфических ситуаций.
3.  **Импорты**:
    -   Импортировать только необходимые модули и функции из библиотек.
4.  **Стиль кода**:
    -   Использовать константы для магических строк, таких как `USER_ENTERED`, `COLUMNS`, `ROWS`, `MERGE_ALL`.
    -   Избегать прямого доступа к элементам словаря, использовать `get()` с значениями по умолчанию, где это уместно.
    -   Переписать все комментарии в формате RST.
5.  **Тесты**:
    -   Улучшить тесты, добавив больше проверок и граничных случаев.
6.  **Логирование**:
    -   Убедиться, что все ошибки и важные события логируются с помощью `logger`.

**Оптимизированный код**
```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
Модуль для работы с Google Sheets API v4.
=========================================================================================

Этот модуль предоставляет класс :class:`ReachSpreadsheet`,
который используется для взаимодействия с Google Sheets API v4.
Модуль позволяет создавать, читать, изменять и предоставлять доступ к электронным таблицам Google.

.. code-block:: python

    # Пример использования
    ss = ReachSpreadsheet(debugMode=True)
    ss.create("My New Spreadsheet", "Sheet1")
    ss.shareWithEmailForWriting("user@example.com")
"""

import httplib2
import googleapiclient.discovery
import googleapiclient.errors
from oauth2client.service_account import ServiceAccountCredentials

import tempfile
#from header import header #TODO: not using header class
from src import gs
from src.utils.jjson import j_loads_ns, j_dumps
from src.utils.printer import pprint
from src.logger.logger import logger

MODE = 'dev'
"""Режим работы модуля."""

USER_ENTERED = "USER_ENTERED"
"""Константа для опции ввода данных в Google Sheets."""
COLUMNS = "COLUMNS"
"""Константа для столбцов."""
ROWS = "ROWS"
"""Константа для строк."""
MERGE_ALL = "MERGE_ALL"
"""Константа для типа слияния ячеек."""


def htmlColorToJSON(htmlColor: str) -> dict:
    """
    Преобразует HTML цвет в JSON формат для Google Sheets API.

    :param htmlColor: HTML цвет в формате `#RRGGBB` или `RRGGBB`.
    :return: JSON представление цвета в формате `{'red': float, 'green': float, 'blue': float}`.

    Пример:
    htmlColorToJSON("#FF0000") -> {"red": 1.0, "green": 0.0, "blue": 0.0}
    """
    if htmlColor.startswith("#"):
        htmlColor = htmlColor[1:]
    return {"red": int(htmlColor[0:2], 16) / 255.0, "green": int(htmlColor[2:4], 16) / 255.0, "blue": int(htmlColor[4:6], 16) / 255.0}


class SpreadsheetError(Exception):
    """Базовый класс для ошибок, связанных с электронными таблицами."""
    ...


class SpreadsheetNotSetError(SpreadsheetError):
    """Исключение, которое выбрасывается, если не установлен ID электронной таблицы."""
    ...


class SheetNotSetError(SpreadsheetError):
    """Исключение, которое выбрасывается, если не установлен ID листа."""
    ...


class ReachSpreadsheet:
    """
    Класс для работы с Google Sheets API.
    
    Этот класс предоставляет интерфейс для создания, чтения, обновления и
    управления электронными таблицами Google.
    
    :param debugMode: Флаг для включения режима отладки (вывод дополнительной информации).

    .. code-block:: python

        ss = ReachSpreadsheet(debugMode=True)
    """
    def __init__(self, debugMode: bool = False):
        """
        Инициализирует объект ReachSpreadsheet.

        :param debugMode: Флаг для включения режима отладки (вывод дополнительной информации).
        """
        self.debugMode = debugMode

        try:
            jsonKeyFileName = gs.path.tmp / 'e-cat-346312-137284f4419e.json'
            # загрузка данных из временного файла для создания credentials
            self.credentials = ServiceAccountCredentials.from_json_keyfile_name(
                jsonKeyFileName, ['https://www.googleapis.com/auth/spreadsheets']
            )
            print("Credentials created successfully.")
        except Exception as ex:
            logger.error("Error creating credentials.", ex, exc_info=True)
            ...
            return

        self.httpAuth = self.credentials.authorize(httplib2.Http())
        self.service = googleapiclient.discovery.build('sheets', 'v4', http=self.httpAuth)
        self.driveService = googleapiclient.discovery.build('drive', 'v3', http=self.httpAuth)
        self.spreadsheetId = None
        self.sheetId = None
        self.sheetTitle = None
        self.requests = []
        self.valueRanges = []

    def create(self, title: str, sheetTitle: str, rows: int = 1000, cols: int = 26, locale: str = 'en-US',
               timeZone: str = 'Etc/GMT') -> None:
        """
        Создает новую электронную таблицу.

        :param title: Название электронной таблицы.
        :param sheetTitle: Название первого листа.
        :param rows: Количество строк в листе.
        :param cols: Количество столбцов в листе.
        :param locale: Локаль.
        :param timeZone: Временная зона.
        """
        spreadsheet = self.service.spreadsheets().create(body={
            'properties': {'title': title},
            'sheets': [{'properties': {'sheetType': 'GRID', 'sheetId': 0, 'title': sheetTitle,
                                      'gridProperties': {'rowCount': rows, 'columnCount': cols}}}]
        }).execute()

        if self.debugMode:
            pprint(spreadsheet)
        self.spreadsheetId = spreadsheet.get('spreadsheetId')
        self.sheetId = spreadsheet.get('sheets', [{}])[0].get('properties', {}).get('sheetId')
        self.sheetTitle = spreadsheet.get('sheets', [{}])[0].get('properties', {}).get('title')

    def share(self, shareRequestBody: dict) -> None:
        """
        Предоставляет доступ к электронной таблице.

        :param shareRequestBody: Запрос на предоставление доступа.
        """
        if self.spreadsheetId is None:
            raise SpreadsheetNotSetError()
        if self.driveService is None:
            self.driveService = googleapiclient.discovery.build('drive', 'v3', http=self.httpAuth)
        try:
            shareRes = self.driveService.permissions().create(
                fileId=self.spreadsheetId,
                body=shareRequestBody,
                fields='id'
            ).execute()
            if self.debugMode:
                pprint(shareRes)
        except Exception as ex:
            logger.error(f"Error sharing spreadsheet {self.spreadsheetId}.", ex, exc_info=True)

    def shareWithEmailForReading(self, email: str) -> None:
        """
        Предоставляет доступ на чтение к электронной таблице для указанного email.

        :param email: Email пользователя, которому предоставляется доступ.
        """
        self.share({'type': 'user', 'role': 'reader', 'emailAddress': email})

    def shareWithEmailForWriting(self, email: str) -> None:
        """
        Предоставляет доступ на запись к электронной таблице для указанного email.

        :param email: Email пользователя, которому предоставляется доступ.
        """
        self.share({'type': 'user', 'role': 'writer', 'emailAddress': email})

    def shareWithAnybodyForReading(self) -> None:
        """
        Предоставляет публичный доступ на чтение к электронной таблице.
        """
        self.share({'type': 'anyone', 'role': 'reader'})

    def shareWithAnybodyForWriting(self) -> None:
        """
        Предоставляет публичный доступ на запись к электронной таблице.
        """
        self.share({'type': 'anyone', 'role': 'writer'})

    def getSheetURL(self) -> str:
        """
        Возвращает URL текущего листа.

        :return: URL текущего листа.
        """
        if self.spreadsheetId is None:
            raise SpreadsheetNotSetError()
        if self.sheetId is None:
            raise SheetNotSetError()
        return 'https://docs.google.com/spreadsheets/d/' + self.spreadsheetId + '/edit#gid=' + str(self.sheetId)

    def setSpreadsheetById(self, spreadsheetId: str) -> None:
        """
        Устанавливает текущую электронную таблицу по её ID.

        :param spreadsheetId: ID электронной таблицы.
        """
        try:
            spreadsheet = self.service.spreadsheets().get(spreadsheetId=spreadsheetId).execute()
            if self.debugMode:
                pprint(spreadsheet)
            self.spreadsheetId = spreadsheet.get('spreadsheetId')
            self.sheetId = spreadsheet.get('sheets', [{}])[0].get('properties', {}).get('sheetId')
            self.sheetTitle = spreadsheet.get('sheets', [{}])[0].get('properties', {}).get('title')
        except Exception as ex:
            logger.error(f"Error getting spreadsheet by id {spreadsheetId}.", ex, exc_info=True)

    def runPrepared(self, valueInputOption: str = USER_ENTERED) -> tuple:
        """
        Выполняет подготовленные запросы на обновление электронной таблицы.

        :param valueInputOption: Опция ввода данных.
        :return: Кортеж из двух списков: результаты batchUpdate и batchUpdate values.
        """
        if self.spreadsheetId is None:
            raise SpreadsheetNotSetError()
        upd1Res = {'replies': []}
        upd2Res = {'responses': []}
        try:
            if len(self.requests) > 0:
                upd1Res = self.service.spreadsheets().batchUpdate(spreadsheetId=self.spreadsheetId,
                                                                  body={"requests": self.requests}).execute()
                if self.debugMode:
                    pprint(upd1Res)
            if len(self.valueRanges) > 0:
                upd2Res = self.service.spreadsheets().values().batchUpdate(spreadsheetId=self.spreadsheetId,
                                                                         body={"valueInputOption": valueInputOption,
                                                                               "data": self.valueRanges}).execute()
                if self.debugMode:
                    pprint(upd2Res)
        except Exception as ex:
            logger.error(f"Error running prepared requests for spreadsheet {self.spreadsheetId}.", ex, exc_info=True)
        finally:
            self.requests = []
            self.valueRanges = []
        return (upd1Res.get('replies', []), upd2Res.get('responses', []))

    def prepare_addSheet(self, sheetTitle: str, rows: int = 1000, cols: int = 26) -> None:
        """
        Подготавливает запрос на добавление нового листа.

        :param sheetTitle: Название нового листа.
        :param rows: Количество строк в новом листе.
        :param cols: Количество столбцов в новом листе.
        """
        self.requests.append({"addSheet": {"properties": {"title": sheetTitle,
                                                          'gridProperties': {'rowCount': rows,
                                                                            'columnCount': cols}}}})

    def addSheet(self, sheetTitle: str, rows: int = 1000, cols: int = 26) -> int:
        """
        Добавляет новый лист в текущую электронную таблицу.

        :param sheetTitle: Название нового листа.
        :param rows: Количество строк в новом листе.
        :param cols: Количество столбцов в новом листе.
        :return: ID нового листа.
        """
        if self.spreadsheetId is None:
            raise SpreadsheetNotSetError()
        self.prepare_addSheet(sheetTitle, rows, cols)
        try:
            addedSheet = self.runPrepared()[0][0]['addSheet']['properties']
            self.sheetId = addedSheet['sheetId']
            self.sheetTitle = addedSheet['title']
            return self.sheetId
        except Exception as ex:
             logger.error(f"Error adding sheet {sheetTitle} to spreadsheet {self.spreadsheetId}.", ex, exc_info=True)
             return None
    def toGridRange(self, cellsRange: str) -> dict:
        """
        Конвертирует строковый диапазон ячеек в GridRange.

        :param cellsRange: Строковый диапазон ячеек, например "A3:B4" или "A5:B".
        :return: Словарь GridRange.
        """
        if self.sheetId is None:
            raise SheetNotSetError()
        if isinstance(cellsRange, str):
            startCell, endCell = cellsRange.split(":")[0:2]
            cellsRange = {}
            rangeAZ = range(ord('A'), ord('Z') + 1)
            if ord(startCell[0]) in rangeAZ:
                cellsRange["startColumnIndex"] = ord(startCell[0]) - ord('A')
                startCell = startCell[1:]
            if ord(endCell[0]) in rangeAZ:
                cellsRange["endColumnIndex"] = ord(endCell[0]) - ord('A') + 1
                endCell = endCell[1:]
            if len(startCell) > 0:
                cellsRange["startRowIndex"] = int(startCell) - 1
            if len(endCell) > 0:
                cellsRange["endRowIndex"] = int(endCell)
        cellsRange["sheetId"] = self.sheetId
        return cellsRange

    def prepare_setDimensionPixelSize(self, dimension: str, startIndex: int, endIndex: int, pixelSize: int) -> None:
        """
        Подготавливает запрос на изменение размера измерения (строки или столбца).

        :param dimension: Измерение, "COLUMNS" или "ROWS".
        :param startIndex: Начальный индекс.
        :param endIndex: Конечный индекс.
        :param pixelSize: Размер в пикселях.
        """
        if self.sheetId is None:
            raise SheetNotSetError()
        self.requests.append({"updateDimensionProperties": {
            "range": {"sheetId": self.sheetId,
                      "dimension": dimension,
                      "startIndex": startIndex,
                      "endIndex": endIndex},
            "properties": {"pixelSize": pixelSize},
            "fields": "pixelSize"}})

    def prepare_setColumnsWidth(self, startCol: int, endCol: int, width: int) -> None:
        """
        Подготавливает запрос на изменение ширины столбцов.

        :param startCol: Начальный столбец.
        :param endCol: Конечный столбец.
        :param width: Ширина в пикселях.
        """
        self.prepare_setDimensionPixelSize(COLUMNS, startCol, endCol + 1, width)

    def prepare_setColumnWidth(self, col: int, width: int) -> None:
        """
        Подготавливает запрос на изменение ширины одного столбца.

        :param col: Номер столбца.
        :param width: Ширина в пикселях.
        """
        self.prepare_setColumnsWidth(col, col, width)

    def prepare_setRowsHeight(self, startRow: int, endRow: int, height: int) -> None:
        """
        Подготавливает запрос на изменение высоты строк.

        :param startRow: Начальная строка.
        :param endRow: Конечная строка.
        :param height: Высота в пикселях.
        """
        self.prepare_setDimensionPixelSize(ROWS, startRow, endRow + 1, height)

    def prepare_setRowHeight(self, row: int, height: int) -> None:
        """
         Подготавливает запрос на изменение высоты одной строки.

        :param row: Номер строки.
        :param height: Высота в пикселях.
        """
        self.prepare_setRowsHeight(row, row, height)

    def prepare_setValues(self, cellsRange: str, values: list, majorDimension: str = ROWS) -> None:
        """
        Подготавливает запрос на установку значений в ячейки.

        :param cellsRange: Диапазон ячеек, например "A1:B2".
        :param values: Значения для установки.
        :param majorDimension: Главное измерение "ROWS" или "COLUMNS".
        """
        if self.sheetTitle is None:
            raise SheetNotSetError()
        self.valueRanges.append({"range": self.sheetTitle + "!" + cellsRange, "majorDimension": majorDimension, "values": values})

    def prepare_mergeCells(self, cellsRange: str, mergeType: str = MERGE_ALL) -> None:
        """
        Подготавливает запрос на слияние ячеек.

        :param cellsRange: Диапазон ячеек для слияния, например "A1:B2".
        :param mergeType: Тип слияния (по умолчанию "MERGE_ALL").
        """
        self.requests.append({"mergeCells": {"range": self.toGridRange(cellsRange), "mergeType": mergeType}})

    def prepare_setCellStringFormatterormat(self, cellsRange: str, formatJSON: dict, fields: str = "userEnteredFormat") -> None:
        """
        Подготавливает запрос на установку формата ячеек.

        :param cellsRange: Диапазон ячеек, например "A1:B2".
        :param formatJSON: JSON с форматом для ячеек.
        :param fields: Поля для применения формата.
        """
        self.requests.append({"repeatCell": {"range": self.toGridRange(cellsRange), "cell": {"userEnteredFormat": formatJSON}, "fields": fields}})

    def prepare_setCellStringFormatterormats(self, cellsRange: str, formatsJSON: list, fields: str = "userEnteredFormat") -> None:
        """
        Подготавливает запрос на установку форматов для нескольких ячеек.

        :param cellsRange: Диапазон ячеек, например "A1:B2".
        :param formatsJSON: Список списков JSON с форматами для каждой ячейки.
        :param fields: Поля для применения формата.
        """
        self.requests.append({"updateCells": {"range": self.toGridRange(cellsRange),
                                              "rows": [{"values": [{"userEnteredFormat": cellFormat} for cellFormat in rowFormats]}
                                                       for rowFormats in formatsJSON],
                                              "fields": fields}})


# === Tests for class Spreadsheet ===
def testCreateSpreadsheet():
    """
    Тест для создания электронной таблицы.
    """
    ss = ReachSpreadsheet(debugMode=True)
    ss.create("Preved medved", "Тестовый лист")
    ss.shareWithEmailForWriting("volkov.ioann@gmail.com")

def testSetSpreadsheet():
    """
    Тест для установки электронной таблицы по ID.
    """
    ss = ReachSpreadsheet(debugMode=True)
    ss.setSpreadsheetById('19SPK--efwYq9pZ7TvBYtFItxE0gY3zpfR5NykOJ6o7I')
    print(ss.sheetId)

def testAddSheet():
    """
    Тест для добавления листа в электронную таблицу.
    """
    ss = ReachSpreadsheet(debugMode=True)
    ss.setSpreadsheetById('19SPK--efwYq9pZ7TvBYtFItxE0gY3zpfR5NykOJ6o7I')
    try:
        print(ss.addSheet("Я лолка №1", 500, 11))
    except googleapiclient.errors.HttpError:
        print("Could not add sheet! Maybe sheet with same name already exists!")

def testSetDimensions():
    """
    Тест для изменения размеров столбцов и строк.
    """
    ss = ReachSpreadsheet(debugMode=True)
    ss.setSpreadsheetById('19SPK--efwYq9pZ7TvBYtFItxE0gY3zpfR5NykOJ6o7I')
    ss.prepare_setColumnWidth(0, 500)
    ss.prepare_setColumnWidth(1, 100)
    ss.prepare_setColumnsWidth(2, 4, 150)
    ss.prepare_setRowHeight(6, 230)
    ss.runPrepared()

def testGridRangeForStr():
    """
    Тест для преобразования строкового диапазона ячеек в GridRange.
    """
    ss = ReachSpreadsheet(debugMode=True)
    ss.setSpreadsheetById('19SPK--efwYq9pZ7TvBYtFItxE0gY3zpfR5NykOJ6o7I')
    res = [ss.toGridRange("A3:B4"),
           ss.toGridRange("A5:B"),
           ss.toGridRange("A:B")]
    correctRes = [{"sheetId": ss.sheetId, "startRowIndex": 2, "endRowIndex": 4, "startColumnIndex": 0, "endColumnIndex": 2},
                  {"sheetId": ss.sheetId, "startRowIndex": 4, "startColumnIndex": 0, "endColumnIndex": 2},
                  {"sheetId": ss.sheetId, "startColumnIndex": 0, "endColumnIndex": 2}]
    print("GOOD" if res == correctRes else "BAD", res)

def testSetCellStringFormatterormat():
    """
    Тест для установки формата ячеек.
    """
    ss = ReachSpreadsheet(debugMode=True)
    ss.setSpreadsheetById('19SPK--efwYq9pZ7TvBYtFItxE0gY3zpfR5NykOJ6o7I')
    ss.prepare_setCellStringFormatterormat("B2:E7", {"textFormat": {"bold": True}, "horizontalAlignment": "CENTER"})
    ss.runPrepared()

def testPureBlackBorder():
    """
    Тест для установки черных границ ячеек.
    """
    ss = ReachSpreadsheet(debugMode=True)
    ss.setSpreadsheetById('19SPK--efwYq9pZ7TvBYtFItxE0gY3zpfR5NykOJ6o7I')
    ss.requests.append({"updateBorders": {"range": {"sheetId": ss.sheetId, "startRowIndex": 1, "endRowIndex": 2, "startColumnIndex": 0, "endColumnIndex": 3},
                                          "bottom": {"style": "SOLID", "width": 3, "color": {"red": 0, "green": 0, "blue": 0}}}})
    ss.requests.append({"updateBorders": {"range": {"sheetId": ss.sheetId, "startRowIndex": 2, "endRowIndex": 3, "startColumnIndex": 0, "endColumnIndex": 3},
                                          "bottom": {"style": "SOLID", "width": 3, "color": {"red": 0, "green": 0, "blue": 0, "alpha": 1.0}}}})
    ss.requests.append({"updateBorders": {"range": {"sheetId": ss.sheetId, "startRowIndex": 3, "endRowIndex": 4, "startColumnIndex": 1, "endColumnIndex": 4},
                                          "bottom": {"style": "SOLID", "width": 3, "color": {"red": 0, "green": 0, "blue": 0.001}}}})
    ss.requests.append({"updateBorders": {"range": {"sheetId": ss.sheetId, "startRowIndex": 4, "endRowIndex": 5, "startColumnIndex": 2, "endColumnIndex": 5},
                                          "bottom": {"style": "SOLID", "width": 3, "color": {"red": 0.001, "green": 0, "blue": 0}}}})
    ss.runPrepared()

def testUpdateCellStringFormatterieldsArg():
    """
    Тест для обновления формата ячеек с использованием аргумента fields.
    """
    ss = ReachSpreadsheet(debugMode=True)
    ss.setSpreadsheetById('19SPK--efwYq9pZ7TvBYtFItxE0gY3zpfR5NykOJ6o7I')
    ss.prepare_setCellStringFormatterormat("B2:B2", {"textFormat": {"bold": True}, "horizontalAlignment": "CENTER"}, fields="userEnteredFormat.textFormat,userEnteredFormat.horizontalAlignment")
    ss.prepare_setCellStringFormatterormat("B2:B2", {"backgroundColor": htmlColorToJSON("#00CC00")}, fields="userEnteredFormat.backgroundColor")
    ss.prepare_setCellStringFormatterormats("C4:C4", [[{"textFormat": {"bold": True}, "horizontalAlignment": "CENTER"}]], fields="userEnteredFormat.textFormat,userEnteredFormat.horizontalAlignment")
    ss.prepare_setCellStringFormatterormats("C4:C4", [[{"backgroundColor": htmlColorToJSON("#00CC00")}]], fields="userEnteredFormat.backgroundColor")
    pprint(ss.requests)
    ss.runPrepared()

def create_pricelist(docTitle: str, sheetTitle: str, values: list) -> None:
    """
    Создает электронную таблицу с заданными данными (прайс-лист).

    :param docTitle: Название электронной таблицы.
    :param sheetTitle: Название листа.
    :param values: Данные для записи в таблицу.
    """
    rowCount = len(values) - 1
    ss = ReachSpreadsheet(debugMode=True)
    ss.create(docTitle, sheetTitle, rows=rowCount + 3, cols=70, locale="en-US", timeZone="Asia/Jerusalem")
    ss.shareWithAnybodyForWriting()
    ss.prepare_setValues("A2:BS", values) #TODO: % (rowCount + 3) не нужен в строке

def testCreateTimeManagementReport():
    """
    Создает тестовый отчет по управлению временем в электронной таблице.
    """
    docTitle = "Тестовый документ"
    sheetTitle = "Тестовая таблица действий"
    values = [["Действие", "Категория полезности", "Начато", "Завершено", "Потрачено"],  # header row
              ["Обедаю", "Еда", "2 июл 2016 17:57:52", "2 июл 2016 18:43:45", "=D4-C4"],
              ["Лёг полежать", "Отдых", "2 июл 2016 18:43:47", "2 июл 2016 18:53:36", "=D5-C5"],
              ["Пью чай", "Еда", "2 июл 2016 18:53:39", "2 июл 2016 19:00:49", "=D6-C6"],
              ["Пилю и шлифую большие щиты", "Ремонт", "2 июл 2016 19:00:52", "2 июл 2016 19:52:36", "=D7-C7"],
              ["Собираю дверь шкафа", "Ремонт", "2 июл 2016 19:52:38", "2 июл 2016 21:11:21", "=D8-C8"]]
    rowCount = len(values) - 1
    colorStringFormatterorCategories = {"Еда": htmlColorToJSON("#FFCCCC"),
                           "Отдых": htmlColorToJSON("#CCFFCC"),
                           "Ремонт": htmlColorToJSON("#CCCCFF")}

    values2 = [["Категория полезности", "Потрачено"],  # header row
               ["Ремонт", "=E7+E8"],
               ["Еда", "=E4+E6"],
               ["Отдых", "=E5"]]
    rowCount2 = len(values2) - 1

    ss = ReachSpreadsheet(debugMode=True)
    ss.create(docTitle, sheetTitle, rows=rowCount + 3, cols=8, locale="ru-RU", timeZone="Europe/Moscow")
    ss.shareWithAnybodyForWriting()

    ss.prepare_setColumnWidth(0, 400)
    ss.prepare_setColumnWidth(1, 200)
    ss.prepare_setColumnsWidth(2, 3, 165)
    ss.prepare_setColumnWidth(4, 100)
    ss.prepare_mergeCells("A1:E1")  # Merge A1:E1

    rowColors = [colorStringFormatterorCategories[valueRow[1]] for valueRow in values[1:]]

    ss.prepare_setCellStringFormatterormat("A1:A1", {"textFormat": {"fontSize": 14}, "horizontalAlignment": "CENTER"})  # Font size 14 and center aligment for A1 cell
    ss.prepare_setCellStringFormatterormat("A3:E3", {"textFormat": {"bold": True}, "horizontalAlignment": "CENTER"})  # Bold and center aligment for A3:E3 row
    ss.prepare_setCellStringFormatterormats("A4:E%d" % (rowCount + 3), [[{"backgroundColor": color}] * 5 for color in rowColors])
    ss.prepare_setCellStringFormatterormat("A4:B%d" % (rowCount + 3), {"numberFormat": {'type': 'TEXT'}}, fields="userEnteredFormat.numberFormat")  # Text format for A4:B* columns
    ss.prepare_setCellStringFormatterormat("E4:E%d" % (rowCount + 3), {"numberFormat": {'pattern': '[h]:mm:ss', 'type': 'TIME'}}, fields="userEnteredFormat.numberFormat")  # Duration number format for E4:E* column

    # Bottom border for A3:E3 row
    ss.requests.append({"updateBorders": {"range": {"sheetId": ss.sheetId, "startRowIndex": 2, "endRowIndex": 3, "startColumnIndex": 0, "endColumnIndex": 5},
                                          "bottom": {"style": "SOLID", "width": 1, "color": htmlColorToJSON("#000001")}}})

    ss.prepare_setValues("A1:A1", [[sheetTitle]])
    ss.prepare_setValues("A3:E%d" % (rowCount + 3), values)


    ss.prepare_setColumnWidth(6, 200)
    ss.prepare_setColumnWidth(7, 100)
    ss.prepare_mergeCells("G1:H1")  # Merge G1:H1

    rowColors2 = [colorStringFormatterorCategories[valueRow[0]] for valueRow in values2[1:]]

    ss.prepare_setCellStringFormatterormat("G1:G1", {"textFormat": {"fontSize": 14}, "horizontalAlignment": "CENTER"})  # Font size 14 and center aligment for G1 cell
    ss.prepare_setCellStringFormatterormat("G3:H3", {"textFormat": {"bold": True}, "horizontalAlignment": "CENTER"})  # Bold and center aligment for G3:H3 row
    ss.prepare_setCellStringFormatterormats("G4:H%d" % (rowCount2 + 3), [[{"backgroundColor": color}] * 2 for color in rowColors2])
    ss.prepare_setCellStringFormatterormat("G4:G%d" % (rowCount2 + 3), {"numberFormat": {'type': 'TEXT'}}, fields="userEnteredFormat.numberFormat")  # Text format for G4:G* column
    ss.prepare_setCellStringFormatterormat("H4:H%d" % (rowCount2 + 3