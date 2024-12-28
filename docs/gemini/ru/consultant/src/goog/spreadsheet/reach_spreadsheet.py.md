# Анализ кода модуля `reach_spreadsheet.py`

**Качество кода: 7/10**
- **Плюсы:**
    - Код предоставляет функциональность для работы с Google Sheets API, включая создание, совместное использование и форматирование таблиц.
    - Используются классы исключений для обработки ошибок.
    - Присутствует возможность отладки с использованием `debugMode` и `pprint`.
    -  Используется `ServiceAccountCredentials` для аутентификации.
    - Код разбит на логические блоки и функции.
    -  Имеется пример использования с `testCreateTimeManagementReport`.
- **Минусы:**
    -  Отсутствует reStructuredText (RST) документация для модулей, классов и методов.
    -  Не везде используется `logger.error` для обработки исключений.
    -  Много `...` в коде, что может указывать на незавершенные участки кода.
    -  Использование `print` для отладки вместо `logger.debug`.
    -  Код не соответствует PEP8.
    -  Присутствуют избыточные комментарии, например `#! venv/Scripts/python.exe`
    -  Жестко заданный путь к файлу `e-cat-346312-137284f4419e.json`
    -  Не все функции имеют docstring.

**Рекомендации по улучшению**

1.  Добавить reStructuredText (RST) документацию для модуля, классов и методов.
2.  Использовать `logger.error` для обработки ошибок вместо `try-except` и `print`.
3.  Убрать все `...` и завершить начатый код.
4.  Заменить `print` на `logger.debug` для отладочного вывода.
5.  Удалить избыточные комментарии, такие как `#! venv/Scripts/python.exe` и `#! venv/bin/python/python3.12`.
6.  Изменить способ загрузки ключа, чтобы он не был привязан к конкретному пути.
7.  Добавить docstring для всех функций.
8.  Использовать `j_loads_ns` и `j_dumps` из `src.utils.jjson` для работы с JSON.
9.  Привести код в соответствие со стандартами PEP8.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
"""
Модуль для работы с Google Sheets API.
=========================================================================================

Этот модуль предоставляет класс :class:`ReachSpreadsheet` для взаимодействия с Google Sheets API.
Он позволяет создавать, изменять, совместно использовать и форматировать электронные таблицы.

.. module:: src.goog.spreadsheet
   :platform: Windows, Unix
   :synopsis: Модуль для работы с Google Sheets API.

Пример использования
--------------------

.. code-block:: python

    ss = ReachSpreadsheet(debugMode=True)
    ss.create("My New Spreadsheet", "Sheet1")
    ss.shareWithEmailForWriting("user@example.com")
"""

import httplib2
import googleapiclient.discovery
import googleapiclient.errors
from oauth2client.service_account import ServiceAccountCredentials
#import tempfile
#import header # TODO: проверить необходимость импорта
from src import gs
from src.utils.jjson import j_loads_ns, j_dumps
from src.utils.printer import pprint
from src.logger.logger import logger

  # TODO: проверить необходимость этой переменной


def htmlColorToJSON(htmlColor: str) -> dict:
    """
    Конвертирует HTML-цвет в JSON-формат.

    :param htmlColor: HTML-цвет в формате #RRGGBB или RRGGBB.
    :return: JSON-объект, представляющий цвет в формате {'red': red, 'green': green, 'blue': blue}.
    """
    if htmlColor.startswith("#"):
        htmlColor = htmlColor[1:]
    return {"red": int(htmlColor[0:2], 16) / 255.0, "green": int(htmlColor[2:4], 16) / 255.0,
            "blue": int(htmlColor[4:6], 16) / 255.0}


class SpreadsheetError(Exception):
    """
    Базовый класс для ошибок, связанных с электронными таблицами.
    """
    ... # TODO: Проверить использование этого класса


class SpreadsheetNotSetError(SpreadsheetError):
    """
    Исключение, вызываемое, когда не установлена электронная таблица.
    """
    ... # TODO: Проверить использование этого класса


class SheetNotSetError(SpreadsheetError):
    """
    Исключение, вызываемое, когда не установлен лист электронной таблицы.
    """
    ... # TODO: Проверить использование этого класса


class ReachSpreadsheet:
    """
    Класс для работы с Google Sheets API.

    Предоставляет методы для создания, редактирования и совместного доступа к электронным таблицам Google.
    """

    def __init__(self, debugMode: bool = False):
        """
        Инициализирует объект ReachSpreadsheet.

        :param debugMode: Включает режим отладки, если True.
        """
        self.debugMode = debugMode
        try:
            jsonKeyFileName = gs.path.tmp / 'e-cat-346312-137284f4419e.json'  # TODO: Переделать загрузку ключа
            # Загрузка данных из временного файла для создания credentials
            self.credentials = ServiceAccountCredentials.from_json_keyfile_name(
                jsonKeyFileName, ['https://www.googleapis.com/auth/spreadsheets']
            )
            logger.debug("Credentials created successfully.")
        except Exception as ex:
            logger.error("Error creating credentials.", exc_info=True)
            ...  # TODO: Добавить дополнительную логику обработки ошибки
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
               timeZone: str = 'Etc/GMT'):
        """
        Создает новую электронную таблицу.

        :param title: Заголовок электронной таблицы.
        :param sheetTitle: Заголовок первого листа.
        :param rows: Количество строк в листе.
        :param cols: Количество столбцов в листе.
        :param locale: Языковой стандарт электронной таблицы.
        :param timeZone: Временная зона электронной таблицы.
        """
        spreadsheet = self.service.spreadsheets().create(body={
            'properties': {'title': title},
            'sheets': [{'properties': {'sheetType': 'GRID', 'sheetId': 0, 'title': sheetTitle,
                                        'gridProperties': {'rowCount': rows, 'columnCount': cols}}}]
        }).execute()

        if self.debugMode:
            pprint(spreadsheet)
        self.spreadsheetId = spreadsheet['spreadsheetId']
        self.sheetId = spreadsheet['sheets'][0]['properties']['sheetId']
        self.sheetTitle = spreadsheet['sheets'][0]['properties']['title']

    def share(self, shareRequestBody: dict):
        """
        Предоставляет доступ к электронной таблице.

        :param shareRequestBody: JSON-объект с параметрами доступа.
        :raises SpreadsheetNotSetError: Если `spreadsheetId` не установлен.
        """
        if self.spreadsheetId is None:
            raise SpreadsheetNotSetError()
        if self.driveService is None:
            self.driveService = googleapiclient.discovery.build('drive', 'v3', http=self.httpAuth)
        shareRes = self.driveService.permissions().create(
            fileId=self.spreadsheetId,
            body=shareRequestBody,
            fields='id'
        ).execute()
        if self.debugMode:
            pprint(shareRes)

    def shareWithEmailForReading(self, email: str):
        """
        Предоставляет доступ на чтение к электронной таблице для указанного email.

        :param email: Email пользователя, которому предоставляется доступ.
        """
        self.share({'type': 'user', 'role': 'reader', 'emailAddress': email})

    def shareWithEmailForWriting(self, email: str):
        """
        Предоставляет доступ на запись к электронной таблице для указанного email.

        :param email: Email пользователя, которому предоставляется доступ.
        """
        self.share({'type': 'user', 'role': 'writer', 'emailAddress': email})

    def shareWithAnybodyForReading(self):
        """
        Предоставляет публичный доступ на чтение к электронной таблице.
        """
        self.share({'type': 'anyone', 'role': 'reader'})

    def shareWithAnybodyForWriting(self):
        """
         Предоставляет публичный доступ на запись к электронной таблице.
        """
        self.share({'type': 'anyone', 'role': 'writer'})

    def getSheetURL(self) -> str:
        """
        Возвращает URL электронной таблицы.

        :raises SpreadsheetNotSetError: Если `spreadsheetId` не установлен.
        :raises SheetNotSetError: Если `sheetId` не установлен.
        :return: URL электронной таблицы.
        """
        if self.spreadsheetId is None:
            raise SpreadsheetNotSetError()
        if self.sheetId is None:
            raise SheetNotSetError()
        return 'https://docs.google.com/spreadsheets/d/' + self.spreadsheetId + '/edit#gid=' + str(self.sheetId)

    def setSpreadsheetById(self, spreadsheetId: str):
        """
        Устанавливает текущую электронную таблицу по ее ID.

        :param spreadsheetId: ID электронной таблицы.
        """
        spreadsheet = self.service.spreadsheets().get(spreadsheetId=spreadsheetId).execute()
        if self.debugMode:
            pprint(spreadsheet)
        self.spreadsheetId = spreadsheet['spreadsheetId']
        self.sheetId = spreadsheet['sheets'][0]['properties']['sheetId']
        self.sheetTitle = spreadsheet['sheets'][0]['properties']['title']

    def runPrepared(self, valueInputOption: str = "USER_ENTERED") -> tuple:
        """
        Выполняет все подготовленные запросы.

        :param valueInputOption: Параметр для обновления значений.
        :raises SpreadsheetNotSetError: Если `spreadsheetId` не установлен.
        :return: Кортеж с результатами выполнения запросов.
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
        finally:
            self.requests = []
            self.valueRanges = []
        return (upd1Res['replies'], upd2Res['responses'])

    def prepare_addSheet(self, sheetTitle: str, rows: int = 1000, cols: int = 26):
        """
        Подготавливает запрос на добавление нового листа.

        :param sheetTitle: Заголовок нового листа.
        :param rows: Количество строк в новом листе.
        :param cols: Количество столбцов в новом листе.
        """
        self.requests.append(
            {"addSheet": {"properties": {"title": sheetTitle, 'gridProperties': {'rowCount': rows, 'columnCount': cols}}}})

    def addSheet(self, sheetTitle: str, rows: int = 1000, cols: int = 26) -> int:
        """
        Добавляет новый лист в текущую электронную таблицу.

        :param sheetTitle: Заголовок нового листа.
        :param rows: Количество строк в новом листе.
        :param cols: Количество столбцов в новом листе.
        :raises SpreadsheetNotSetError: Если `spreadsheetId` не установлен.
        :return: ID добавленного листа.
        """
        if self.spreadsheetId is None:
            raise SpreadsheetNotSetError()
        self.prepare_addSheet(sheetTitle, rows, cols)
        addedSheet = self.runPrepared()[0][0]['addSheet']['properties']
        self.sheetId = addedSheet['sheetId']
        self.sheetTitle = addedSheet['title']
        return self.sheetId

    def toGridRange(self, cellsRange: str) -> dict:
        """
        Конвертирует строковый диапазон ячеек в GridRange.

        :param cellsRange: Строковый диапазон ячеек, например, "A3:B4".
        :raises SheetNotSetError: Если `sheetId` не установлен.
        :return: GridRange для API Google Sheets.
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

    def prepare_setDimensionPixelSize(self, dimension: str, startIndex: int, endIndex: int, pixelSize: int):
        """
        Подготавливает запрос на изменение размера столбцов/строк.

        :param dimension: "COLUMNS" или "ROWS".
        :param startIndex: Индекс начала диапазона.
        :param endIndex: Индекс конца диапазона.
        :param pixelSize: Размер в пикселях.
        :raises SheetNotSetError: Если `sheetId` не установлен.
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

    def prepare_setColumnsWidth(self, startCol: int, endCol: int, width: int):
        """
        Подготавливает запрос на изменение ширины столбцов.

        :param startCol: Индекс первого столбца.
        :param endCol: Индекс последнего столбца.
        :param width: Ширина в пикселях.
        """
        self.prepare_setDimensionPixelSize("COLUMNS", startCol, endCol + 1, width)

    def prepare_setColumnWidth(self, col: int, width: int):
        """
        Подготавливает запрос на изменение ширины одного столбца.

        :param col: Индекс столбца.
        :param width: Ширина в пикселях.
        """
        self.prepare_setColumnsWidth(col, col, width)

    def prepare_setRowsHeight(self, startRow: int, endRow: int, height: int):
        """
        Подготавливает запрос на изменение высоты строк.

        :param startRow: Индекс первой строки.
        :param endRow: Индекс последней строки.
        :param height: Высота в пикселях.
        """
        self.prepare_setDimensionPixelSize("ROWS", startRow, endRow + 1, height)

    def prepare_setRowHeight(self, row: int, height: int):
        """
        Подготавливает запрос на изменение высоты одной строки.

        :param row: Индекс строки.
        :param height: Высота в пикселях.
        """
        self.prepare_setRowsHeight(row, row, height)

    def prepare_setValues(self, cellsRange: str, values: list, majorDimension: str = "ROWS"):
        """
        Подготавливает запрос на установку значений в ячейки.

        :param cellsRange: Строковый диапазон ячеек, например, "A1:B2".
        :param values: Значения для установки.
        :param majorDimension: "ROWS" или "COLUMNS".
        :raises SheetNotSetError: Если `sheetTitle` не установлен.
        """
        if self.sheetTitle is None:
            raise SheetNotSetError()
        self.valueRanges.append({"range": self.sheetTitle + "!" + cellsRange, "majorDimension": majorDimension, "values": values})

    def prepare_mergeCells(self, cellsRange: str, mergeType: str = "MERGE_ALL"):
        """
        Подготавливает запрос на объединение ячеек.

        :param cellsRange: Строковый диапазон ячеек, например, "A1:B2".
        :param mergeType: Тип объединения, например, "MERGE_ALL".
        """
        self.requests.append({"mergeCells": {"range": self.toGridRange(cellsRange), "mergeType": mergeType}})

    def prepare_setCellStringFormatterormat(self, cellsRange: str, formatJSON: dict, fields: str = "userEnteredFormat"):
        """
        Подготавливает запрос на форматирование ячеек.

        :param cellsRange: Строковый диапазон ячеек, например, "A1:B2".
        :param formatJSON: JSON-объект с параметрами форматирования.
        :param fields: Поля для обновления, например, "userEnteredFormat".
        """
        self.requests.append(
            {"repeatCell": {"range": self.toGridRange(cellsRange), "cell": {"userEnteredFormat": formatJSON},
                            "fields": fields}})

    def prepare_setCellStringFormatterormats(self, cellsRange: str, formatsJSON: list,
                                           fields: str = "userEnteredFormat"):
        """
        Подготавливает запрос на массовое форматирование ячеек.

        :param cellsRange: Строковый диапазон ячеек, например, "A1:B2".
        :param formatsJSON: Список списков JSON-объектов с параметрами форматирования для каждой ячейки.
        :param fields: Поля для обновления, например, "userEnteredFormat".
        """
        self.requests.append({"updateCells": {"range": self.toGridRange(cellsRange),
                                              "rows": [{"values": [{"userEnteredFormat": cellFormat} for cellFormat in
                                                                    rowFormats]} for rowFormats in formatsJSON],
                                              "fields": fields}})


# === Tests for class Spreadsheet ===

def testCreateSpreadsheet():
    """
    Тестирует создание электронной таблицы.
    """
    ss = ReachSpreadsheet(debugMode=True)
    ss.create("Preved medved", "Тестовый лист")
    ss.shareWithEmailForWriting("volkov.ioann@gmail.com")


def testSetSpreadsheet():
    """
    Тестирует установку электронной таблицы по ID.
    """
    ss = ReachSpreadsheet(debugMode=True)
    ss.setSpreadsheetById('19SPK--efwYq9pZ7TvBYtFItxE0gY3zpfR5NykOJ6o7I')
    print(ss.sheetId)


def testAddSheet():
    """
    Тестирует добавление нового листа.
    """
    ss = ReachSpreadsheet(debugMode=True)
    ss.setSpreadsheetById('19SPK--efwYq9pZ7TvBYtFItxE0gY3zpfR5NykOJ6o7I')
    try:
        print(ss.addSheet("Я лолка №1", 500, 11))
    except googleapiclient.errors.HttpError:
        print("Could not add sheet! Maybe sheet with same name already exists!")


def testSetDimensions():
    """
    Тестирует установку размеров столбцов и строк.
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
    Тестирует конвертацию строковых диапазонов в GridRange.
    """
    ss = ReachSpreadsheet(debugMode=True)
    ss.setSpreadsheetById('19SPK--efwYq9pZ7TvBYtFItxE0gY3zpfR5NykOJ6o7I')
    res = [ss.toGridRange("A3:B4"),
           ss.toGridRange("A5:B"),
           ss.toGridRange("A:B")]
    correctRes = [{"sheetId": ss.sheetId, "startRowIndex": 2, "endRowIndex": 4, "startColumnIndex": 0,
                   "endColumnIndex": 2},
                  {"sheetId": ss.sheetId, "startRowIndex": 4, "startColumnIndex": 0, "endColumnIndex": 2},
                  {"sheetId": ss.sheetId, "startColumnIndex": 0, "endColumnIndex": 2}]
    print("GOOD" if res == correctRes else "BAD", res)


def testSetCellStringFormatterormat():
    """
    Тестирует форматирование ячеек.
    """
    ss = ReachSpreadsheet(debugMode=True)
    ss.setSpreadsheetById('19SPK--efwYq9pZ7TvBYtFItxE0gY3zpfR5NykOJ6o7I')
    ss.prepare_setCellStringFormatterormat("B2:E7", {"textFormat": {"bold": True}, "horizontalAlignment": "CENTER"})
    ss.runPrepared()


def testPureBlackBorder():
    """
    Тестирует установку черных границ.
    """
    ss = ReachSpreadsheet(debugMode=True)
    ss.setSpreadsheetById('19SPK--efwYq9pZ7TvBYtFItxE0gY3zpfR5NykOJ6o7I')
    ss.requests.append({"updateBorders": {"range": {"sheetId": ss.sheetId, "startRowIndex": 1, "endRowIndex": 2,
                                                  "startColumnIndex": 0, "endColumnIndex": 3},
                                          "bottom": {"style": "SOLID", "width": 3,
                                                     "color": {"red": 0, "green": 0, "blue": 0}}}})
    ss.requests.append({"updateBorders": {"range": {"sheetId": ss.sheetId, "startRowIndex": 2, "endRowIndex": 3,
                                                  "startColumnIndex": 0, "endColumnIndex": 3},
                                          "bottom": {"style": "SOLID", "width": 3,
                                                     "color": {"red": 0, "green": 0, "blue": 0, "alpha": 1.0}}}})
    ss.requests.append({"updateBorders": {"range": {"sheetId": ss.sheetId, "startRowIndex": 3, "endRowIndex": 4,
                                                  "startColumnIndex": 1, "endColumnIndex": 4},
                                          "bottom": {"style": "SOLID", "width": 3,
                                                     "color": {"red": 0, "green": 0, "blue": 0.001}}}})
    ss.requests.append({"updateBorders": {"range": {"sheetId": ss.sheetId, "startRowIndex": 4, "endRowIndex": 5,
                                                  "startColumnIndex": 2, "endColumnIndex": 5},
                                          "bottom": {"style": "SOLID", "width": 3,
                                                     "color": {"red": 0.001, "green": 0, "blue": 0}}}})
    ss.runPrepared()
    # Reported: https://code.google.com/a/google.com/p/apps-api-issues/issues/detail?id=4696


def testUpdateCellStringFormatterieldsArg():
    """
    Тестирует обновление форматирования ячеек с аргументом fields.
    """
    ss = ReachSpreadsheet(debugMode=True)
    ss.setSpreadsheetById('19SPK--efwYq9pZ7TvBYtFItxE0gY3zpfR5NykOJ6o7I')
    ss.prepare_setCellStringFormatterormat("B2:B2", {"textFormat": {"bold": True}, "horizontalAlignment": "CENTER"},
                                         fields="userEnteredFormat.textFormat,userEnteredFormat.horizontalAlignment")
    ss.prepare_setCellStringFormatterormat("B2:B2", {"backgroundColor": htmlColorToJSON("#00CC00")},
                                         fields="userEnteredFormat.backgroundColor")
    ss.prepare_setCellStringFormatterormats("C4:C4", [[{"textFormat": {"bold": True}, "horizontalAlignment": "CENTER"}]],
                                          fields="userEnteredFormat.textFormat,userEnteredFormat.horizontalAlignment")
    ss.prepare_setCellStringFormatterormats("C4:C4", [[{"backgroundColor": htmlColorToJSON("#00CC00")}]],
                                          fields="userEnteredFormat.backgroundColor")
    pprint(ss.requests)
    ss.runPrepared()
    # Reported: https://code.google.com/a/google.com/p/apps-api-issues/issues/detail?id=4697


def create_pricelist(docTitle: str, sheetTitle: str, values: list):
    """
    Создает прайс-лист в электронной таблице.

    :param docTitle: Заголовок документа.
    :param sheetTitle: Заголовок листа.
    :param values: Значения для заполнения таблицы.
    """
    rowCount = len(values) - 1
    ss = ReachSpreadsheet(debugMode=True)
    ss.create(docTitle, sheetTitle, rows=rowCount + 3, cols=70, locale="en-US", timeZone="Asia/Jerusalem")
    ss.shareWithAnybodyForWriting()
    ss.prepare_setValues("A2:BS" % (rowCount + 3), values)


# This function creates a spreadsheet as https://telegram.me/TimeManagementBot can create, but with manually specified data
def testCreateTimeManagementReport():
    """
    Тестирует создание отчета по тайм-менеджменту.
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
    ss.prepare_setCellStringFormatterormats("A4:E%d" % (rowCount + 3),
                                          [[{"backgroundColor": color}] * 5 for color in rowColors])
    ss.prepare_setCellStringFormatterormat("A4:B%d" % (rowCount + 3), {"numberFormat": {'type': 'TEXT'}},
                                         fields="userEnteredFormat.numberFormat")  # Text format for A4:B* columns
    ss.prepare_setCellStringFormatterormat("E4:E%d" % (rowCount + 3),
                                         {"numberFormat": {'pattern': '[h]:mm:ss', 'type': 'TIME'}},
                                         fields="userEnteredFormat.numberFormat")  # Duration number format for E4:E* column

    # Bottom border for A3:E3 row
    ss.requests.append({"updateBorders": {"range": {"sheetId": ss.sheetId, "startRowIndex": 2, "endRowIndex": 3,
                                                  "startColumnIndex": 0, "endColumnIndex": 5},
                                          "bottom": {"style": "SOLID", "width": 1,
                                                     "color": htmlColorToJSON("#000001")}}})

    ss.prepare_setValues("A1:A1", [[sheetTitle]])
    ss.prepare_setValues("A3:E%d" % (rowCount + 3), values)

    # ss.prepare_setCellStringFormatterormat("D%d:D%d" % (rowCount + 3, rowCount + 3), {"textFormat": {"italic": True}, "horizontalAlignment": "CENTER"},
    #                          fields = "userEnteredFormat.textFormat,userEnteredFormat.horizontalAlignment")  # Italic and center aligment for bottom D* cell

    ss.prepare_setColumnWidth(6, 200)
    ss.prepare_setColumnWidth(7, 100)
    ss.prepare_mergeCells("G1:H1")  # Merge G1:H1

    rowColors2 = [colorStringFormatterorCategories[valueRow[0]] for valueRow in values2[1:]]

    ss.prepare_setCellStringFormatterormat("G1:G1", {"textFormat": {"fontSize": 14}, "horizontalAlignment": "CENTER"})  # Font size 14 and center aligment for G1 cell
    ss.prepare_setCellStringFormatterormat("G3:H3", {"textFormat": {"bold": True}, "horizontalAlignment": "CENTER"})  # Bold and center aligment for G3:H3 row
    ss.prepare_setCellStringFormatterormats("G4:H%d" % (rowCount2 + 3),
                                          [[{"backgroundColor": color}] * 2 for color in rowColors2])
    ss.prepare_setCellStringFormatterormat("G4:G%d" % (rowCount2 + 3), {"numberFormat": {'type': 'TEXT'}},
                                         fields="userEnteredFormat.numberFormat")  # Text format for G4:G* column
    ss.prepare_setCellStringFormatterormat("