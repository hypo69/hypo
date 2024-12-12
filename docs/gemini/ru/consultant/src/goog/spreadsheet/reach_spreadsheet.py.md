# Анализ кода модуля `reach_spreadsheet.py`

**Качество кода: 6/10**

- **Плюсы:**
    - Код структурирован в класс `ReachSpreadsheet`, что способствует организации и повторному использованию.
    - Используются `ServiceAccountCredentials` для аутентификации, что является хорошей практикой для серверных приложений.
    - Присутствуют методы для основных операций с Google Sheets, такие как создание, публикация, добавление листов, форматирование ячеек.
    - Используется `logger` для обработки ошибок.
    - Есть примеры использования основных функций.
- **Минусы:**
    - Код местами недостаточно документирован.
    - Присутствуют стандартные блоки `try-except`, которые лучше заменить на `logger.error`.
    - Используются не все возможности для форматирования кода (например, отсутствуют docstring).
    - Не все переменные и функции имеют описание в формате RST.
    - Использование `print` для отладки вместо `logger.debug`.
    - В некоторых местах используется f-строки, хотя это не обязательно, поскольку переменные уже существуют.

**Рекомендации по улучшению:**

1.  **Документация:**
    -   Добавить docstring к классу `ReachSpreadsheet`, всем методам и функциям, используя формат reStructuredText (RST).
    -   Переписать комментарии в формате RST.
2.  **Обработка ошибок:**
    -   Заменить блоки `try-except` на использование `logger.error` для обработки исключений.
3.  **Логирование:**
    -   Использовать `logger.debug` для отладочного вывода вместо `print`.
4.  **Импорты:**
    -   Проверить и добавить необходимые импорты.
5.  **Рефакторинг:**
    -   Упростить код там, где это возможно. Например, избавиться от избыточных переменных.
6.  **Стандартизация:**
    -   Привести в соответствие имена функций, переменных и импортов с ранее обработанными файлами.
    -   Использовать одинарные кавычки `'` для строк в коде.

**Оптимизированный код:**

```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
Модуль для работы с Google Sheets API v4.
======================================

Этот модуль предоставляет класс :class:`ReachSpreadsheet` для взаимодействия с Google Sheets API v4 и Google Drive API v3.
Он включает функции для создания, совместного использования, управления листами и форматирования данных в Google Sheets.

:platform: Windows, Unix
:synopsis: Модуль для взаимодействия с Google Sheets API.

Пример использования
--------------------
.. code-block:: python

    spreadsheet = ReachSpreadsheet(debugMode=True)
    spreadsheet.create("My Spreadsheet", "Sheet1")
    spreadsheet.shareWithEmailForWriting("test@example.com")
    url = spreadsheet.getSheetURL()

"""

import httplib2
import googleapiclient.discovery
import googleapiclient.errors
from oauth2client.service_account import ServiceAccountCredentials

import tempfile
from src import gs
from src.utils.jjson import j_loads_ns, j_dumps # используем j_loads_ns
from src.utils.printer import pprint
from src.logger.logger import logger

MODE = 'dev'


def htmlColorToJSON(htmlColor: str) -> dict:
    """
    Преобразует HTML цвет в формат JSON.

    :param htmlColor: HTML цвет в формате #RRGGBB или RRGGBB.
    :return: JSON объект, представляющий цвет в формате {'red': float, 'green': float, 'blue': float}.
    """
    if htmlColor.startswith('#'):
        htmlColor = htmlColor[1:]
    return {'red': int(htmlColor[0:2], 16) / 255.0, 'green': int(htmlColor[2:4], 16) / 255.0,
            'blue': int(htmlColor[4:6], 16) / 255.0}


class SpreadsheetError(Exception):
    """
    Базовое исключение для ошибок, связанных с Google Sheets.
    """
    ...


class SpreadsheetNotSetError(SpreadsheetError):
    """
    Исключение, возникающее, когда идентификатор таблицы не установлен.
    """
    ...


class SheetNotSetError(SpreadsheetError):
    """
    Исключение, возникающее, когда идентификатор листа не установлен.
    """
    ...


class ReachSpreadsheet:
    """
    Класс для взаимодействия с Google Sheets API.

    :param debugMode: Флаг отладки. Если True, то будет выводиться дополнительная информация.
    """
    def __init__(self, debugMode=False):
        """
        Инициализирует объект ReachSpreadsheet.

        :param debugMode: Флаг отладки.
        """
        self.debugMode = debugMode

        try:
            jsonKeyFileName = gs.path.tmp / 'e-cat-346312-137284f4419e.json'

            # загрузка данных из временного файла для создания credentials
            self.credentials = ServiceAccountCredentials.from_json_keyfile_name(
                jsonKeyFileName, ['https://www.googleapis.com/auth/spreadsheets']
            )
            print('Credentials created successfully.')
        except Exception as ex:
            logger.error('Error creating credentials.', ex, exc_info=True)
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
               timeZone: str = 'Etc/GMT'):
        """
        Создает новую Google таблицу.

        :param title: Название таблицы.
        :param sheetTitle: Название первого листа.
        :param rows: Количество строк в листе.
        :param cols: Количество столбцов в листе.
        :param locale: Локаль таблицы.
        :param timeZone: Временная зона таблицы.
        """
        # spreadsheet = self.service.spreadsheets().create(body = {
        #     'properties': {'title': title, 'locale': locale, 'timeZone': timeZone},
        #     'sheets': [{'properties': {'sheetType': 'GRID', 'sheetId': 0, 'title': sheetTitle, 'gridProperties': {'rowCount': rows, 'columnCount': cols}}}]
        # }).execute()
        # Код создает новую таблицу с указанными параметрами.
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
        Предоставляет доступ к Google таблице.

        :param shareRequestBody: Тело запроса для предоставления доступа.
        :raises SpreadsheetNotSetError: Если идентификатор таблицы не установлен.
        """
        if self.spreadsheetId is None:
            raise SpreadsheetNotSetError()
        if self.driveService is None:
            self.driveService = googleapiclient.discovery.build('drive', 'v3', http=self.httpAuth)
        # Код отправляет запрос на предоставление доступа к таблице.
        shareRes = self.driveService.permissions().create(
            fileId=self.spreadsheetId,
            body=shareRequestBody,
            fields='id'
        ).execute()
        if self.debugMode:
            pprint(shareRes)

    def shareWithEmailForReading(self, email: str):
        """
        Предоставляет доступ на чтение к таблице для указанного email.

        :param email: Email пользователя.
        """
        self.share({'type': 'user', 'role': 'reader', 'emailAddress': email})

    def shareWithEmailForWriting(self, email: str):
        """
        Предоставляет доступ на запись к таблице для указанного email.

        :param email: Email пользователя.
        """
        self.share({'type': 'user', 'role': 'writer', 'emailAddress': email})

    def shareWithAnybodyForReading(self):
        """
        Предоставляет доступ на чтение к таблице для всех.
        """
        self.share({'type': 'anyone', 'role': 'reader'})

    def shareWithAnybodyForWriting(self):
        """
        Предоставляет доступ на запись к таблице для всех.
        """
        self.share({'type': 'anyone', 'role': 'writer'})

    def getSheetURL(self) -> str:
        """
        Возвращает URL текущего листа таблицы.

        :return: URL текущего листа таблицы.
        :raises SpreadsheetNotSetError: Если идентификатор таблицы не установлен.
        :raises SheetNotSetError: Если идентификатор листа не установлен.
        """
        if self.spreadsheetId is None:
            raise SpreadsheetNotSetError()
        if self.sheetId is None:
            raise SheetNotSetError()
        return 'https://docs.google.com/spreadsheets/d/' + self.spreadsheetId + '/edit#gid=' + str(self.sheetId)

    def setSpreadsheetById(self, spreadsheetId: str):
        """
        Устанавливает текущую таблицу по идентификатору.

        :param spreadsheetId: Идентификатор таблицы.
        """
        # Код получает таблицу по id и устанавливает ее как текущую.
        spreadsheet = self.service.spreadsheets().get(spreadsheetId=spreadsheetId).execute()
        if self.debugMode:
            pprint(spreadsheet)
        self.spreadsheetId = spreadsheet['spreadsheetId']
        self.sheetId = spreadsheet['sheets'][0]['properties']['sheetId']
        self.sheetTitle = spreadsheet['sheets'][0]['properties']['title']

    def runPrepared(self, valueInputOption: str = 'USER_ENTERED') -> tuple:
        """
        Выполняет подготовленные запросы.

        :param valueInputOption: Параметр ввода значений.
        :return: Кортеж из ответов на запросы (upd1Res, upd2Res).
        :raises SpreadsheetNotSetError: Если идентификатор таблицы не установлен.
        """
        if self.spreadsheetId is None:
            raise SpreadsheetNotSetError()
        upd1Res = {'replies': []}
        upd2Res = {'responses': []}
        try:
            if len(self.requests) > 0:
                # Код отправляет запрос на batchUpdate
                upd1Res = self.service.spreadsheets().batchUpdate(spreadsheetId=self.spreadsheetId,
                                                                 body={'requests': self.requests}).execute()
                if self.debugMode:
                    pprint(upd1Res)
            if len(self.valueRanges) > 0:
                # Код отправляет запрос на batchUpdate для значений
                upd2Res = self.service.spreadsheets().values().batchUpdate(spreadsheetId=self.spreadsheetId,
                                                                         body={'valueInputOption': valueInputOption,
                                                                               'data': self.valueRanges}).execute()
                if self.debugMode:
                    pprint(upd2Res)
        finally:
            self.requests = []
            self.valueRanges = []
        return upd1Res['replies'], upd2Res['responses']

    def prepare_addSheet(self, sheetTitle: str, rows: int = 1000, cols: int = 26):
        """
        Подготавливает запрос на добавление нового листа.

        :param sheetTitle: Название нового листа.
        :param rows: Количество строк в листе.
        :param cols: Количество столбцов в листе.
        """
        # Код подготавливает запрос на добавление листа.
        self.requests.append({'addSheet': {'properties': {'title': sheetTitle, 'gridProperties': {'rowCount': rows,
                                                                                                'columnCount': cols}}}})

    def addSheet(self, sheetTitle: str, rows: int = 1000, cols: int = 26) -> int:
        """
        Добавляет новый лист в текущую таблицу.

        :param sheetTitle: Название нового листа.
        :param rows: Количество строк в листе.
        :param cols: Количество столбцов в листе.
        :return: Идентификатор добавленного листа.
        :raises SpreadsheetNotSetError: Если идентификатор таблицы не установлен.
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
        Преобразует строковый диапазон ячеек в GridRange.

        :param cellsRange: Строковый диапазон ячеек (например, "A3:B4").
        :return:  GridRange текущего листа.
        :raises SheetNotSetError: Если идентификатор листа не установлен.
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

    def prepare_setDimensionPixelSize(self, dimension: str, startIndex: int, endIndex: int, pixelSize: int):
        """
        Подготавливает запрос на установку размера в пикселях для строк или столбцов.

        :param dimension: Тип измерения ("COLUMNS" или "ROWS").
        :param startIndex: Индекс начала.
        :param endIndex: Индекс конца.
        :param pixelSize: Размер в пикселях.
        :raises SheetNotSetError: Если идентификатор листа не установлен.
        """
        if self.sheetId is None:
            raise SheetNotSetError()
         # Код подготавливает запрос на изменение размера столбцов или строк.
        self.requests.append({'updateDimensionProperties': {
            'range': {'sheetId': self.sheetId,
                      'dimension': dimension,
                      'startIndex': startIndex,
                      'endIndex': endIndex},
            'properties': {'pixelSize': pixelSize},
            'fields': 'pixelSize'}})

    def prepare_setColumnsWidth(self, startCol: int, endCol: int, width: int):
        """
        Подготавливает запрос на установку ширины столбцов.

        :param startCol: Индекс начального столбца.
        :param endCol: Индекс конечного столбца.
        :param width: Ширина в пикселях.
        """
        self.prepare_setDimensionPixelSize('COLUMNS', startCol, endCol + 1, width)

    def prepare_setColumnWidth(self, col: int, width: int):
        """
        Подготавливает запрос на установку ширины одного столбца.

        :param col: Индекс столбца.
        :param width: Ширина в пикселях.
        """
        self.prepare_setColumnsWidth(col, col, width)

    def prepare_setRowsHeight(self, startRow: int, endRow: int, height: int):
        """
        Подготавливает запрос на установку высоты строк.

        :param startRow: Индекс начальной строки.
        :param endRow: Индекс конечной строки.
        :param height: Высота в пикселях.
        """
        self.prepare_setDimensionPixelSize('ROWS', startRow, endRow + 1, height)

    def prepare_setRowHeight(self, row: int, height: int):
        """
        Подготавливает запрос на установку высоты одной строки.

        :param row: Индекс строки.
        :param height: Высота в пикселях.
        """
        self.prepare_setRowsHeight(row, row, height)

    def prepare_setValues(self, cellsRange: str, values: list, majorDimension: str = 'ROWS'):
        """
        Подготавливает запрос на установку значений в ячейки.

        :param cellsRange: Строковый диапазон ячеек (например, "A1:B2").
        :param values: Значения для установки.
        :param majorDimension:  Главное измерение ("ROWS" или "COLUMNS").
        :raises SheetNotSetError: Если заголовок листа не установлен.
        """
        if self.sheetTitle is None:
            raise SheetNotSetError()
        # Код подготавливает запрос на установку значений в ячейки
        self.valueRanges.append({'range': self.sheetTitle + '!' + cellsRange, 'majorDimension': majorDimension, 'values': values})

    def prepare_mergeCells(self, cellsRange: str, mergeType: str = 'MERGE_ALL'):
        """
        Подготавливает запрос на объединение ячеек.

        :param cellsRange: Строковый диапазон ячеек (например, "A1:B2").
        :param mergeType: Тип объединения ("MERGE_ALL", "MERGE_COLUMNS", "MERGE_ROWS").
        """
        # Код подготавливает запрос на объединение ячеек
        self.requests.append({'mergeCells': {'range': self.toGridRange(cellsRange), 'mergeType': mergeType}})

    def prepare_setCellStringFormatterormat(self, cellsRange: str, formatJSON: dict, fields: str = 'userEnteredFormat'):
        """
        Подготавливает запрос на форматирование ячеек.

        :param cellsRange: Строковый диапазон ячеек (например, "A1:B2").
        :param formatJSON:  JSON объект с форматом ячеек.
        :param fields: Поля для обновления.
        """
        # Код подготавливает запрос на форматирование ячеек
        self.requests.append({'repeatCell': {'range': self.toGridRange(cellsRange), 'cell': {'userEnteredFormat': formatJSON},
                                          'fields': fields}})

    def prepare_setCellStringFormatterormats(self, cellsRange: str, formatsJSON: list, fields: str = 'userEnteredFormat'):
        """
        Подготавливает запрос на форматирование нескольких ячеек.

        :param cellsRange: Строковый диапазон ячеек (например, "A1:B2").
        :param formatsJSON: Список списков с JSON объектами формата ячеек.
        :param fields: Поля для обновления.
        """
         # Код подготавливает запрос на обновление формата ячеек
        self.requests.append({'updateCells': {'range': self.toGridRange(cellsRange),
                                              'rows': [{'values': [{'userEnteredFormat': cellFormat} for cellFormat in rowFormats]}
                                                       for rowFormats in formatsJSON],
                                              'fields': fields}})


# === Tests for class Spreadsheet ===

def testCreateSpreadsheet():
    """
    Тест для создания таблицы.
    """
    ss = ReachSpreadsheet(debugMode=True)
    ss.create('Preved medved', 'Тестовый лист')
    ss.shareWithEmailForWriting('volkov.ioann@gmail.com')


def testSetSpreadsheet():
    """
    Тест для установки таблицы по ID.
    """
    ss = ReachSpreadsheet(debugMode=True)
    ss.setSpreadsheetById('19SPK--efwYq9pZ7TvBYtFItxE0gY3zpfR5NykOJ6o7I')
    print(ss.sheetId)


def testAddSheet():
    """
    Тест для добавления нового листа.
    """
    ss = ReachSpreadsheet(debugMode=True)
    ss.setSpreadsheetById('19SPK--efwYq9pZ7TvBYtFItxE0gY3zpfR5NykOJ6o7I')
    try:
        print(ss.addSheet('Я лолка №1', 500, 11))
    except googleapiclient.errors.HttpError:
        print('Could not add sheet! Maybe sheet with same name already exists!')


def testSetDimensions():
    """
    Тест для установки размеров столбцов и строк.
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
    Тест для преобразования диапазона ячеек.
    """
    ss = ReachSpreadsheet(debugMode=True)
    ss.setSpreadsheetById('19SPK--efwYq9pZ7TvBYtFItxE0gY3zpfR5NykOJ6o7I')
    res = [ss.toGridRange('A3:B4'),
           ss.toGridRange('A5:B'),
           ss.toGridRange('A:B')]
    correctRes = [{'sheetId': ss.sheetId, 'startRowIndex': 2, 'endRowIndex': 4, 'startColumnIndex': 0, 'endColumnIndex': 2},
                  {'sheetId': ss.sheetId, 'startRowIndex': 4, 'startColumnIndex': 0, 'endColumnIndex': 2},
                  {'sheetId': ss.sheetId, 'startColumnIndex': 0, 'endColumnIndex': 2}]
    print('GOOD' if res == correctRes else 'BAD', res)


def testSetCellStringFormatterormat():
    """
    Тест для установки формата ячеек.
    """
    ss = ReachSpreadsheet(debugMode=True)
    ss.setSpreadsheetById('19SPK--efwYq9pZ7TvBYtFItxE0gY3zpfR5NykOJ6o7I')
    ss.prepare_setCellStringFormatterormat('B2:E7', {'textFormat': {'bold': True}, 'horizontalAlignment': 'CENTER'})
    ss.runPrepared()


def testPureBlackBorder():
    """
    Тест для добавления черной границы.
    """
    ss = ReachSpreadsheet(debugMode=True)
    ss.setSpreadsheetById('19SPK--efwYq9pZ7TvBYtFItxE0gY3zpfR5NykOJ6o7I')
    ss.requests.append({'updateBorders': {'range': {'sheetId': ss.sheetId, 'startRowIndex': 1, 'endRowIndex': 2,
                                                  'startColumnIndex': 0, 'endColumnIndex': 3},
                                          'bottom': {'style': 'SOLID', 'width': 3,
                                                     'color': {'red': 0, 'green': 0, 'blue': 0}}}})
    ss.requests.append({'updateBorders': {'range': {'sheetId': ss.sheetId, 'startRowIndex': 2, 'endRowIndex': 3,
                                                  'startColumnIndex': 0, 'endColumnIndex': 3},
                                          'bottom': {'style': 'SOLID', 'width': 3,
                                                     'color': {'red': 0, 'green': 0, 'blue': 0, 'alpha': 1.0}}}})
    ss.requests.append({'updateBorders': {'range': {'sheetId': ss.sheetId, 'startRowIndex': 3, 'endRowIndex': 4,
                                                  'startColumnIndex': 1, 'endColumnIndex': 4},
                                          'bottom': {'style': 'SOLID', 'width': 3,
                                                     'color': {'red': 0, 'green': 0, 'blue': 0.001}}}})
    ss.requests.append({'updateBorders': {'range': {'sheetId': ss.sheetId, 'startRowIndex': 4, 'endRowIndex': 5,
                                                  'startColumnIndex': 2, 'endColumnIndex': 5},
                                          'bottom': {'style': 'SOLID', 'width': 3,
                                                     'color': {'red': 0.001, 'green': 0, 'blue': 0}}}})
    ss.runPrepared()
    # Reported: https://code.google.com/a/google.com/p/apps-api-issues/issues/detail?id=4696


def testUpdateCellStringFormatterieldsArg():
    """
    Тест для обновления форматов ячеек.
    """
    ss = ReachSpreadsheet(debugMode=True)
    ss.setSpreadsheetById('19SPK--efwYq9pZ7TvBYtFItxE0gY3zpfR5NykOJ6o7I')
    ss.prepare_setCellStringFormatterormat('B2:B2', {'textFormat': {'bold': True}, 'horizontalAlignment': 'CENTER'},
                                          fields='userEnteredFormat.textFormat,userEnteredFormat.horizontalAlignment')
    ss.prepare_setCellStringFormatterormat('B2:B2', {'backgroundColor': htmlColorToJSON('#00CC00')},
                                          fields='userEnteredFormat.backgroundColor')
    ss.prepare_setCellStringFormatterormats('C4:C4', [[{'textFormat': {'bold': True}, 'horizontalAlignment': 'CENTER'}]],
                                           fields='userEnteredFormat.textFormat,userEnteredFormat.horizontalAlignment')
    ss.prepare_setCellStringFormatterormats('C4:C4', [[{'backgroundColor': htmlColorToJSON('#00CC00')}]],
                                           fields='userEnteredFormat.backgroundColor')
    pprint(ss.requests)
    ss.runPrepared()
    # Reported: https://code.google.com/a/google.com/p/apps-api-issues/issues/detail?id=4697


def create_pricelist(docTitle: str, sheetTitle: str, values: list):
    """
    Создает таблицу с ценами.

    :param docTitle: Название документа.
    :param sheetTitle: Название листа.
    :param values: Список значений.
    """
    rowCount = len(values) - 1
    ss = ReachSpreadsheet(debugMode=True)
    ss.create(docTitle, sheetTitle, rows=rowCount + 3, cols=70, locale='en-US', timeZone='Asia/Jerusalem')
    ss.shareWithAnybodyForWriting()
    ss.prepare_setValues('A2:BS' % (rowCount + 3), values)


def testCreateTimeManagementReport():
    """
    Тест для создания отчета по тайм-менеджменту.
    """
    docTitle = 'Тестовый документ'
    sheetTitle = 'Тестовая таблица действий'
    values = [['Действие', 'Категория полезности', 'Начато', 'Завершено', 'Потрачено'],  # header row
              ['Обедаю', 'Еда', '2 июл 2016 17:57:52', '2 июл 2016 18:43:45', '=D4-C4'],
              ['Лёг полежать', 'Отдых', '2 июл 2016 18:43:47', '2 июл 2016 18:53:36', '=D5-C5'],
              ['Пью чай', 'Еда', '2 июл 2016 18:53:39', '2 июл 2016 19:00:49', '=D6-C6'],
              ['Пилю и шлифую большие щиты', 'Ремонт', '2 июл 2016 19:00:52', '2 июл 2016 19:52:36', '=D7-C7'],
              ['Собираю дверь шкафа', 'Ремонт', '2 июл 2016 19:52:38', '2 июл 2016 21:11:21', '=D8-C8']]
    rowCount = len(values) - 1
    colorStringFormatterorCategories = {'Еда': htmlColorToJSON('#FFCCCC'),
                                       'Отдых': htmlColorToJSON('#CCFFCC'),
                                       'Ремонт': htmlColorToJSON('#CCCCFF')}

    values2 = [['Категория полезности', 'Потрачено'],  # header row
               ['Ремонт', '=E7+E8'],
               ['Еда', '=E4+E6'],
               ['Отдых', '=E5']]
    rowCount2 = len(values2) - 1

    ss = ReachSpreadsheet(debugMode=True)
    ss.create(docTitle, sheetTitle, rows=rowCount + 3, cols=8, locale='ru-RU', timeZone='Europe/Moscow')
    ss.shareWithAnybodyForWriting()

    ss.prepare_setColumnWidth(0, 400)
    ss.prepare_setColumnWidth(1, 200)
    ss.prepare_setColumnsWidth(2, 3, 165)
    ss.prepare_setColumnWidth(4, 100)
    ss.prepare_mergeCells('A1:E1')  # Merge A1:E1

    rowColors = [colorStringFormatterorCategories[valueRow[1]] for valueRow in values[1:]]

    ss.prepare_setCellStringFormatterormat('A1:A1', {'textFormat': {'fontSize': 14}, 'horizontalAlignment': 'CENTER'})  # Font size 14 and center aligment for A1 cell
    ss.prepare_setCellStringFormatterormat('A3:E3', {'textFormat': {'bold': True}, 'horizontalAlignment': 'CENTER'})  # Bold and center aligment for A3:E3 row
    ss.prepare_setCellStringFormatterormats('A4:E%d' % (rowCount + 3), [[{'backgroundColor': color}] * 5 for color in rowColors])
    ss.prepare_setCellStringFormatterormat('A4:B%d' % (rowCount + 3), {'numberFormat': {'type': 'TEXT'}}, fields='userEnteredFormat.numberFormat')  # Text format for A4:B* columns
    ss.prepare_setCellStringFormatterormat('E4:E%d' % (rowCount + 3), {'numberFormat': {'pattern': '[h]:mm:ss', 'type': 'TIME'}}, fields='userEnteredFormat.numberFormat')  # Duration number format for E4:E* column

    # Bottom border for A3:E3 row
    ss.requests.append({'updateBorders': {'range': {'sheetId': ss.sheetId, 'startRowIndex': 2, 'endRowIndex': 3,
                                                  'startColumnIndex': 0, 'endColumnIndex': 5},
                                          'bottom': {'style': 'SOLID', 'width': 1,
                                                     'color': htmlColorToJSON('#000001')}}})

    ss.prepare_setValues('A1:A1', [[sheetTitle]])
    ss.prepare_setValues('A3:E%d' % (rowCount + 3), values)


    ss.prepare_setColumnWidth(6, 200)
    ss.prepare_setColumnWidth(7, 100)
    ss.prepare_mergeCells('G1:H1')  # Merge G1:H1

    rowColors2 = [colorStringFormatterorCategories[valueRow[0]] for valueRow in values2[1:]]

    ss.prepare_setCellStringFormatterormat('G1:G1', {'textFormat': {'fontSize': 14}, 'horizontalAlignment': 'CENTER'})  # Font size 14 and center aligment for G1 cell
    ss.prepare_setCellStringFormatterormat('G3:H3', {'textFormat': {'bold': True}, 'horizontalAlignment': 'CENTER'})  # Bold and center aligment for G3:H3 row
    ss.prepare_setCellStringFormatterormats('G4:H%d' % (rowCount2 + 3), [[{'backgroundColor': color}] * 2 for color in rowColors2])
    ss.prepare_setCellStringFormatterormat('G4:G%d' % (rowCount2 + 3), {'numberFormat': {'type': 'TEXT'}}, fields='userEnteredFormat.numberFormat')  # Text format for G4:G* column
    ss.prepare_setCellStringFormatterormat('H4: