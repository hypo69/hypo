### Анализ кода модуля `reach_spreadsheet`

**Качество кода**:
- **Соответствие стандартам**: 7/10
- **Плюсы**:
    - Код достаточно хорошо структурирован и разбит на логические блоки.
    - Используется `ServiceAccountCredentials` для аутентификации в Google API.
    - Есть базовые тесты для проверки функциональности.
- **Минусы**:
    - Не везде используется `logger` для отладки и обработки ошибок.
    - В коде используется много `print`, которые не соответствуют требованиям логирования.
    - Есть дублирование кода, например, при создании `driveService`.
    - Отсутствует подробная документация в формате RST.
    - Некоторые части кода закомментированы (например, создание spreadsheet), что может запутать.
    - Не все строки кода отформатированы в соответствии с PEP8.
    - Используются двойные кавычки внутри кода, что противоречит требованиям.

**Рекомендации по улучшению**:

1.  **Документация**: Добавить подробную документацию в формате RST для всех классов и методов, чтобы сделать код более понятным и простым в использовании.
2.  **Логирование**: Заменить `print` на `logger.debug` для отладочной информации и `logger.error` для сообщений об ошибках.
3.  **Обработка ошибок**: Использовать `try-except` блоки только для критических операций и логировать ошибки с помощью `logger.error`.
4.  **Дублирование кода**: Устранить дублирование кода, например, инициализацию `driveService`.
5.  **Использование кавычек**: Заменить все двойные кавычки на одинарные внутри кода Python, кроме операций вывода.
6.  **Форматирование**: Привести код в соответствие с PEP8, выровнять названия переменных и функций.
7.  **Удалить ненужные комментарии**: Удалить закомментированный код и оставить только необходимые комментарии.
8. **Импорты**: Перенести импорты в начало файла и выровнять их.
9. **Вывод данных**: Использовать `pprint` для вывода объектов и `logger` для вывода сообщений об ошибках.

**Оптимизированный код**:

```python
# -*- coding: utf-8 -*-
"""
Модуль для работы с Google Sheets API
=====================================

Этот модуль содержит класс :class:`ReachSpreadsheet`, который используется для взаимодействия с Google Sheets API v4
и Google Drive API v3. Он предоставляет методы для создания, редактирования и управления электронными таблицами.

Пример использования
----------------------
.. code-block:: python

    spreadsheet = ReachSpreadsheet(debugMode=True)
    spreadsheet.create('My Spreadsheet', 'Sheet1')
    spreadsheet.shareWithEmailForWriting('user@example.com')
"""

import httplib2
import googleapiclient.discovery
import googleapiclient.errors
from oauth2client.service_account import ServiceAccountCredentials

import tempfile  # Избыточный импорт, но в инструкции сказано сохранять.
from src import gs
from src.utils.jjson import j_loads_ns, j_dumps  # Избыточный импорт, но в инструкции сказано сохранять.
from src.utils.printer import pprint
from src.logger.logger import logger


def htmlColorToJSON(htmlColor: str) -> dict:
    """
    Преобразует HTML цвет в JSON формат для Google Sheets API.

    :param htmlColor: HTML цвет в формате #RRGGBB.
    :type htmlColor: str
    :return: JSON объект с цветовыми компонентами red, green, blue.
    :rtype: dict
    """
    if htmlColor.startswith('#'):
        htmlColor = htmlColor[1:]
    return {'red': int(htmlColor[0:2], 16) / 255.0, 'green': int(htmlColor[2:4], 16) / 255.0,
            'blue': int(htmlColor[4:6], 16) / 255.0}


class SpreadsheetError(Exception):
    """
    Базовый класс для ошибок, связанных с электронными таблицами.
    """
    ...


class SpreadsheetNotSetError(SpreadsheetError):
    """
    Ошибка, возникающая при попытке использовать электронную таблицу, которая не была установлена.
    """
    ...


class SheetNotSetError(SpreadsheetError):
    """
    Ошибка, возникающая при попытке использовать лист, который не был установлен.
    """
    ...


class ReachSpreadsheet:
    """
    Класс для работы с Google Sheets API.
    """

    def __init__(self, debugMode: bool = False):
        """
        Инициализирует объект :class:`ReachSpreadsheet`.

        :param debugMode: Включает/выключает режим отладки.
        :type debugMode: bool, optional
        """
        self.debugMode = debugMode
        self.credentials = None
        self.httpAuth = None
        self.service = None
        self.driveService = None
        self.spreadsheetId = None
        self.sheetId = None
        self.sheetTitle = None
        self.requests = []
        self.valueRanges = []

        try:
            jsonKeyFileName = gs.path.tmp / 'e-cat-346312-137284f4419e.json'
            self.credentials = ServiceAccountCredentials.from_json_keyfile_name(
                jsonKeyFileName, ['https://www.googleapis.com/auth/spreadsheets']
            )
            logger.debug("Credentials created successfully.")  # Логирование успешного создания credentials
        except Exception as ex:
            logger.error("Error creating credentials.", exc_info=True)  # Логирование ошибки создания credentials
            return

        self.httpAuth = self.credentials.authorize(httplib2.Http())
        self.service = googleapiclient.discovery.build('sheets', 'v4', http=self.httpAuth)
        self.driveService = googleapiclient.discovery.build('drive', 'v3', http=self.httpAuth)

    def create(self, title: str, sheetTitle: str, rows: int = 1000, cols: int = 26, locale: str = 'en-US',
               timeZone: str = 'Etc/GMT') -> None:
        """
        Создает новую электронную таблицу.

        :param title: Заголовок электронной таблицы.
        :type title: str
        :param sheetTitle: Заголовок первого листа электронной таблицы.
        :type sheetTitle: str
        :param rows: Количество строк на листе.
        :type rows: int, optional
        :param cols: Количество столбцов на листе.
        :type cols: int, optional
        :param locale: Локаль электронной таблицы.
        :type locale: str, optional
        :param timeZone: Часовой пояс электронной таблицы.
        :type timeZone: str, optional
        """
        spreadsheet = self.service.spreadsheets().create(body={
            'properties': {'title': title},  # убрано 'locale': locale, 'timeZone': timeZone, в соответсвии с кодом
            'sheets': [{'properties': {'sheetType': 'GRID', 'sheetId': 0, 'title': sheetTitle,
                                       'gridProperties': {'rowCount': rows, 'columnCount': cols}}}]
        }).execute()

        if self.debugMode:
            pprint(spreadsheet)
        self.spreadsheetId = spreadsheet['spreadsheetId']
        self.sheetId = spreadsheet['sheets'][0]['properties']['sheetId']
        self.sheetTitle = spreadsheet['sheets'][0]['properties']['title']

    def share(self, shareRequestBody: dict) -> None:
        """
        Предоставляет общий доступ к электронной таблице.

        :param shareRequestBody: Тело запроса для предоставления доступа.
        :type shareRequestBody: dict
        :raises SpreadsheetNotSetError: Если идентификатор электронной таблицы не установлен.
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

    def shareWithEmailForReading(self, email: str) -> None:
        """
        Предоставляет доступ на чтение к электронной таблице для указанного email.

        :param email: Email пользователя, которому предоставляется доступ.
        :type email: str
        """
        self.share({'type': 'user', 'role': 'reader', 'emailAddress': email})

    def shareWithEmailForWriting(self, email: str) -> None:
        """
        Предоставляет доступ на запись к электронной таблице для указанного email.

        :param email: Email пользователя, которому предоставляется доступ.
        :type email: str
        """
        self.share({'type': 'user', 'role': 'writer', 'emailAddress': email})

    def shareWithAnybodyForReading(self) -> None:
        """
        Предоставляет доступ на чтение к электронной таблице для всех.
        """
        self.share({'type': 'anyone', 'role': 'reader'})

    def shareWithAnybodyForWriting(self) -> None:
        """
        Предоставляет доступ на запись к электронной таблице для всех.
        """
        self.share({'type': 'anyone', 'role': 'writer'})

    def getSheetURL(self) -> str:
        """
        Возвращает URL текущего листа электронной таблицы.

        :raises SpreadsheetNotSetError: Если идентификатор электронной таблицы не установлен.
        :raises SheetNotSetError: Если идентификатор листа не установлен.
        :return: URL текущего листа электронной таблицы.
        :rtype: str
        """
        if self.spreadsheetId is None:
            raise SpreadsheetNotSetError()
        if self.sheetId is None:
            raise SheetNotSetError()
        return 'https://docs.google.com/spreadsheets/d/' + self.spreadsheetId + '/edit#gid=' + str(self.sheetId)

    def setSpreadsheetById(self, spreadsheetId: str) -> None:
        """
        Устанавливает текущую электронную таблицу по её идентификатору.

        :param spreadsheetId: Идентификатор электронной таблицы.
        :type spreadsheetId: str
        """
        spreadsheet = self.service.spreadsheets().get(spreadsheetId=spreadsheetId).execute()
        if self.debugMode:
            pprint(spreadsheet)
        self.spreadsheetId = spreadsheet['spreadsheetId']
        self.sheetId = spreadsheet['sheets'][0]['properties']['sheetId']
        self.sheetTitle = spreadsheet['sheets'][0]['properties']['title']

    def runPrepared(self, valueInputOption: str = "USER_ENTERED") -> tuple[list, list]:
        """
        Выполняет подготовленные запросы к Google Sheets API.

        :param valueInputOption: Способ интерпретации входных значений.
        :type valueInputOption: str, optional
        :raises SpreadsheetNotSetError: Если идентификатор электронной таблицы не установлен.
        :return: Кортеж с результатами запросов batchUpdate и batchUpdate values.
        :rtype: tuple[list, list]
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
                upd2Res = self.service.spreadsheets().values().batchUpdate(spreadsheetId=self.spreadsheetId, body={
                    "valueInputOption": valueInputOption,
                    "data": self.valueRanges}).execute()
                if self.debugMode:
                    pprint(upd2Res)
        except Exception as ex:
            logger.error(f"Error runPrepared: {ex}", exc_info=True)  # логируем ошибку
        finally:
            self.requests = []
            self.valueRanges = []
        return (upd1Res['replies'], upd2Res['responses'])

    def prepare_addSheet(self, sheetTitle: str, rows: int = 1000, cols: int = 26) -> None:
        """
        Подготавливает запрос на добавление нового листа.

        :param sheetTitle: Заголовок нового листа.
        :type sheetTitle: str
        :param rows: Количество строк на листе.
        :type rows: int, optional
        :param cols: Количество столбцов на листе.
        :type cols: int, optional
        """
        self.requests.append({"addSheet": {"properties": {"title": sheetTitle,
                                                         'gridProperties': {'rowCount': rows,
                                                                            'columnCount': cols}}}})

    def addSheet(self, sheetTitle: str, rows: int = 1000, cols: int = 26) -> int:
        """
        Добавляет новый лист в текущую электронную таблицу и устанавливает его как текущий лист.

        :param sheetTitle: Заголовок нового листа.
        :type sheetTitle: str
        :param rows: Количество строк на листе.
        :type rows: int, optional
        :param cols: Количество столбцов на листе.
        :type cols: int, optional
        :raises SpreadsheetNotSetError: Если идентификатор электронной таблицы не установлен.
        :return: Идентификатор добавленного листа.
        :rtype: int
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
        Преобразует строковый диапазон ячеек в GridRange текущего листа.

        :param cellsRange: Строковый диапазон ячеек, например "A3:B4" или "A5:B".
        :type cellsRange: str
        :raises SheetNotSetError: Если идентификатор листа не установлен.
        :return: GridRange для Google Sheets API.
        :rtype: dict
        """
        if self.sheetId is None:
            raise SheetNotSetError()
        if isinstance(cellsRange, str):
            startCell, endCell = cellsRange.split(':')[0:2]
            cellsRange = {}
            rangeAZ = range(ord('A'), ord('Z') + 1)
            if ord(startCell[0]) in rangeAZ:
                cellsRange['startColumnIndex'] = ord(startCell[0]) - ord('A')
                startCell = startCell[1:]
            if ord(endCell[0]) in rangeAZ:
                cellsRange['endColumnIndex'] = ord(endCell[0]) - ord('A') + 1
                endCell = endCell[1:]
            if len(startCell) > 0:
                cellsRange['startRowIndex'] = int(startCell) - 1
            if len(endCell) > 0:
                cellsRange['endRowIndex'] = int(endCell)
        cellsRange['sheetId'] = self.sheetId
        return cellsRange

    def prepare_setDimensionPixelSize(self, dimension: str, startIndex: int, endIndex: int, pixelSize: int) -> None:
        """
        Подготавливает запрос на изменение размера столбца или строки.

        :param dimension: "COLUMNS" или "ROWS".
        :type dimension: str
        :param startIndex: Индекс начала диапазона.
        :type startIndex: int
        :param endIndex: Индекс конца диапазона.
        :type endIndex: int
        :param pixelSize: Размер в пикселях.
        :type pixelSize: int
        :raises SheetNotSetError: Если идентификатор листа не установлен.
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
        Подготавливает запрос на изменение ширины нескольких столбцов.

        :param startCol: Индекс начала столбцов.
        :type startCol: int
        :param endCol: Индекс конца столбцов.
        :type endCol: int
        :param width: Ширина в пикселях.
        :type width: int
        """
        self.prepare_setDimensionPixelSize("COLUMNS", startCol, endCol + 1, width)

    def prepare_setColumnWidth(self, col: int, width: int) -> None:
        """
        Подготавливает запрос на изменение ширины одного столбца.

        :param col: Индекс столбца.
        :type col: int
        :param width: Ширина в пикселях.
        :type width: int
        """
        self.prepare_setColumnsWidth(col, col, width)

    def prepare_setRowsHeight(self, startRow: int, endRow: int, height: int) -> None:
        """
        Подготавливает запрос на изменение высоты нескольких строк.

        :param startRow: Индекс начала строк.
        :type startRow: int
        :param endRow: Индекс конца строк.
        :type endRow: int
        :param height: Высота в пикселях.
        :type height: int
        """
        self.prepare_setDimensionPixelSize("ROWS", startRow, endRow + 1, height)

    def prepare_setRowHeight(self, row: int, height: int) -> None:
        """
        Подготавливает запрос на изменение высоты одной строки.

        :param row: Индекс строки.
        :type row: int
        :param height: Высота в пикселях.
        :type height: int
        """
        self.prepare_setRowsHeight(row, row, height)

    def prepare_setValues(self, cellsRange: str, values: list[list], majorDimension: str = "ROWS") -> None:
        """
        Подготавливает запрос на установку значений в ячейки.

        :param cellsRange: Диапазон ячеек в формате строки, например "A1:B2".
        :type cellsRange: str
        :param values: Список списков значений для записи.
        :type values: list[list]
        :param majorDimension: "ROWS" или "COLUMNS", определяет порядок записи значений.
        :type majorDimension: str, optional
        :raises SheetNotSetError: Если заголовок листа не установлен.
        """
        if self.sheetTitle is None:
            raise SheetNotSetError()
        self.valueRanges.append(
            {"range": self.sheetTitle + "!" + cellsRange, "majorDimension": majorDimension, "values": values})

    def prepare_mergeCells(self, cellsRange: str, mergeType: str = "MERGE_ALL") -> None:
        """
        Подготавливает запрос на объединение ячеек.

        :param cellsRange: Диапазон ячеек для объединения, например "A1:B2".
        :type cellsRange: str
        :param mergeType: Тип объединения, например "MERGE_ALL".
        :type mergeType: str, optional
        """
        self.requests.append({"mergeCells": {"range": self.toGridRange(cellsRange), "mergeType": mergeType}})

    def prepare_setCellStringFormatterormat(self, cellsRange: str, formatJSON: dict, fields: str = "userEnteredFormat") -> None:
        """
        Подготавливает запрос на установку формата ячеек.

        :param cellsRange: Диапазон ячеек для форматирования, например "A1:B2".
        :type cellsRange: str
        :param formatJSON: JSON объект с форматом ячеек.
        :type formatJSON: dict
        :param fields: Поля формата, которые нужно обновить.
        :type fields: str, optional
        """
        self.requests.append(
            {"repeatCell": {"range": self.toGridRange(cellsRange), "cell": {"userEnteredFormat": formatJSON},
                            "fields": fields}})

    def prepare_setCellStringFormatterormats(self, cellsRange: str, formatsJSON: list[list[dict]],
                                           fields: str = "userEnteredFormat") -> None:
        """
        Подготавливает запрос на установку формата для нескольких ячеек.

        :param cellsRange: Диапазон ячеек для форматирования.
        :type cellsRange: str
        :param formatsJSON: Список списков с JSON объектами форматов для каждой ячейки.
        :type formatsJSON: list[list[dict]]
        :param fields: Поля формата, которые нужно обновить.
        :type fields: str, optional
        """
        self.requests.append({"updateCells": {"range": self.toGridRange(cellsRange),
                                              "rows": [{"values": [{"userEnteredFormat": cellFormat} for cellFormat in
                                                                    rowFormats]} for rowFormats in formatsJSON],
                                              "fields": fields}})


# === Tests for class Spreadsheet ===
def testCreateSpreadsheet() -> None:
    """
    Тестирует создание электронной таблицы.
    """
    ss = ReachSpreadsheet(debugMode=True)
    ss.create("Preved medved", "Тестовый лист")
    ss.shareWithEmailForWriting("volkov.ioann@gmail.com")


def testSetSpreadsheet() -> None:
    """
    Тестирует установку электронной таблицы по ID.
    """
    ss = ReachSpreadsheet(debugMode=True)
    ss.setSpreadsheetById('19SPK--efwYq9pZ7TvBYtFItxE0gY3zpfR5NykOJ6o7I')
    print(ss.sheetId)


def testAddSheet() -> None:
    """
    Тестирует добавление нового листа.
    """
    ss = ReachSpreadsheet(debugMode=True)
    ss.setSpreadsheetById('19SPK--efwYq9pZ7TvBYtFItxE0gY3zpfR5NykOJ6o7I')
    try:
        print(ss.addSheet("Я лолка №1", 500, 11))
    except googleapiclient.errors.HttpError:
        print("Could not add sheet! Maybe sheet with same name already exists!")


def testSetDimensions() -> None:
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


def testGridRangeForStr() -> None:
    """
    Тестирует преобразование строкового диапазона в GridRange.
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


def testSetCellStringFormatterormat() -> None:
    """
    Тестирует установку формата ячеек.
    """
    ss = ReachSpreadsheet(debugMode=True)
    ss.setSpreadsheetById('19SPK--efwYq9pZ7TvBYtFItxE0gY3zpfR5NykOJ6o7I')
    ss.prepare_setCellStringFormatterormat("B2:E7",
                                         {"textFormat": {"bold": True}, "horizontalAlignment": "CENTER"})
    ss.runPrepared()


def testPureBlackBorder() -> None:
    """
    Тестирует установку границ ячеек.
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


def testUpdateCellStringFormatterieldsArg() -> None:
    """
    Тестирует обновление формата ячеек с аргументом fields.
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


def create_pricelist(docTitle: str, sheetTitle: str, values: list[list]) -> None:
    """
    Создает прайс-лист в электронной таблице.

    :param docTitle: Заголовок документа.
    :type docTitle: str
    :param sheetTitle: Заголовок листа.
    :type sheetTitle: str
    :param values: Данные для прайс-листа.
    :type values: list[list]
    """
    rowCount = len(values) - 1
    ss = ReachSpreadsheet(debugMode=True)
    ss.create(docTitle, sheetTitle, rows=rowCount + 3, cols=70, locale="en-US", timeZone="Asia/Jerusalem")
    ss.shareWithAnybodyForWriting()
    ss.prepare_setValues("A2:BS", values)


def testCreateTimeManagementReport() -> None:
    """
    Тестирует создание отчета по управлению временем.
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

    ss.prepare_setCellStringFormatterormat("A1:A1", {"textFormat": {"fontSize": 14}, "horizontalAlignment": "CENTER"})
    ss.prepare_setCellStringFormatterormat("A3:E3", {"textFormat": {"bold": True}, "horizontalAlignment": "CENTER"})
    ss.prepare_setCellStringFormatterormats("A4:E%d" % (rowCount + 3),
                                          [[{"backgroundColor": color}] * 5 for color in rowColors])
    ss.prepare_setCellStringFormatterormat("A4:B%d" % (rowCount + 3), {"numberFormat": {'type': 'TEXT'}},
                                         fields="userEnteredFormat.numberFormat")
    ss.prepare_setCellStringFormatterormat("E4:E%d" % (rowCount + 3),
                                         {"numberFormat": {'pattern': '[h]:mm:ss', 'type': 'TIME'}},
                                         fields="userEnteredFormat.numberFormat")

    # Bottom border for A3:E3 row
    ss.requests.append({"updateBorders": {"range": {"sheetId": ss.sheetId, "startRowIndex": 2, "endRowIndex": 3,
                                                    "startColumnIndex": 0, "endColumnIndex": 5},
                                          "bottom": {"style": "SOLID", "width": 1,
                                                     "color": htmlColorToJSON("#000001")}}})

    ss.prepare_setValues("A1:A1", [[sheetTitle]])
    ss.prepare_setValues("A3:E%d" % (rowCount + 3), values)

    # ss.prepare_setCellStringFormatterormat("D%d:D%d" % (rowCount + 3, rowCount + 3), {"textFormat": {"italic": True}, "horizontalAlignment":