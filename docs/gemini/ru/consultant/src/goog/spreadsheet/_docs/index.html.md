# Анализ кода модуля src.goog.spreadsheet._docs

**Качество кода**
7
 - Плюсы
    - Код содержит подробное описание процесса создания Google Sheets API.
    - Присутствуют примеры использования Google Sheets API v4.
    - Представлена логика создания класса-обёртки `Spreadsheet` для упрощения работы с API.
 - Минусы
    -  Отсутствует описание модуля в формате reStructuredText.
    -  Не используются логирование ошибок через `logger`.
    -  Много вложенных try-finally блоков, которые не обрабатывают ошибки через `logger.error`.
    -  Используются избыточные конструкции типа `if len(list) > 0`, которые можно упростить до `if list`.
    -  Не используется `j_loads` или `j_loads_ns` для чтения файлов, если это необходимо.
    -  Не добавлены комментарии в формате RST к методам класса `Spreadsheet`.

**Рекомендации по улучшению**

1.  **Добавить описание модуля:** В начале файла добавить описание модуля в формате reStructuredText.
2.  **Логирование ошибок:** Использовать `from src.logger.logger import logger` для логирования ошибок вместо `print`.
3.  **Обработка исключений:** Избегать избыточного использования стандартных блоков `try-except`, а использовать `logger.error` для обработки ошибок.
4.  **Упрощение проверок:** Упростить проверки вида `if len(list) > 0` до `if list`.
5.  **Форматирование docstring:** Добавить reStructuredText docstring для функций, методов и классов.
6.  **Использовать `j_loads`**: Заменить `json.load` на `j_loads` из `src.utils.jjson` (если таковой имеется).
7.  **Комментарии к коду**: Добавить подробные комментарии в формате RST для методов класса `Spreadsheet`.

**Оптимизиробанный код**

```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe

"""
Модуль для описания работы с Google Sheets API.
=========================================================================================

Этот модуль содержит HTML-документацию с примерами кода для работы с Google Sheets API v4.
Включает в себя создание сервисного аккаунта, установку необходимых библиотек, создание и
настройку Google-таблиц. Также содержит примеры кода для работы с API, включая создание
таблиц, настройку ширины столбцов, заполнение ячеек данными, объединение ячеек и
настройку форматирования.
"""
import httplib2
import apiclient.discovery
from oauth2client.service_account import ServiceAccountCredentials
from src.logger.logger import logger # импортируем logger

MODE = 'debug'

class Spreadsheet:
    """
    Класс для управления Google Spreadsheet.

    Предоставляет методы для подготовки и выполнения запросов к Google Sheets API.
    Включает в себя методы для установки ширины столбцов, заполнения ячеек данными,
    объединения ячеек и настройки форматирования.

    :param service: Экземпляр сервиса Google Sheets API.
    :param driveService: Экземпляр сервиса Google Drive API.
    :param spreadsheetId: Идентификатор Google Spreadsheet.
    :param sheetId: Идентификатор листа Google Spreadsheet.
    :param sheetTitle: Название листа Google Spreadsheet.
    """
    def __init__(self, service, driveService, spreadsheetId, sheetId = 0, sheetTitle = 'Сие есть название листа'):
        """
        Инициализация объекта Spreadsheet.

        :param service: Экземпляр сервиса Google Sheets API.
        :param driveService: Экземпляр сервиса Google Drive API.
        :param spreadsheetId: Идентификатор Google Spreadsheet.
        :param sheetId: Идентификатор листа Google Spreadsheet.
        :param sheetTitle: Название листа Google Spreadsheet.
        """
        self.service = service
        self.driveService = driveService
        self.spreadsheetId = spreadsheetId
        self.sheetId = sheetId
        self.sheetTitle = sheetTitle
        self.requests = []
        self.valueRanges = []

    def toGridRange(self, cellsRange):
        """
        Преобразует A1 нотацию в GridRange.

        :param cellsRange: Строка A1 нотации (например, "A1:B2").
        :return: Объект GridRange для использования в запросах API.
        """
        start_cell, end_cell = cellsRange.split(':') if ':' in cellsRange else (cellsRange, cellsRange)
        start_col = ord(start_cell[0].upper()) - ord('A')
        end_col = ord(end_cell[0].upper()) - ord('A')
        start_row = int(start_cell[1:]) - 1
        end_row = int(end_cell[1:])
        return {
            'sheetId': self.sheetId,
            'startRowIndex': start_row,
            'endRowIndex': end_row,
            'startColumnIndex': start_col,
            'endColumnIndex': end_col + 1
        }

    def prepare_setDimensionPixelSize(self, dimension, startIndex, endIndex, pixelSize):
        """
        Подготавливает запрос для установки размера столбцов или строк.

        :param dimension: 'COLUMNS' для столбцов или 'ROWS' для строк.
        :param startIndex: Индекс начального столбца/строки.
        :param endIndex: Индекс конечного столбца/строки (не включительно).
        :param pixelSize: Размер в пикселях.
        """
        self.requests.append({
            "updateDimensionProperties": {
                "range": {
                    "sheetId": self.sheetId,
                    "dimension": dimension,
                    "startIndex": startIndex,
                    "endIndex": endIndex
                },
                "properties": {
                    "pixelSize": pixelSize
                },
                "fields": "pixelSize"
            }
        })

    def prepare_setColumnsWidth(self, startCol, endCol, width):
        """
        Подготавливает запрос для установки ширины нескольких столбцов.

        :param startCol: Индекс начального столбца.
        :param endCol: Индекс конечного столбца.
        :param width: Ширина столбцов в пикселях.
        """
        self.prepare_setDimensionPixelSize("COLUMNS", startCol, endCol + 1, width)

    def prepare_setColumnWidth(self, col, width):
        """
        Подготавливает запрос для установки ширины одного столбца.

        :param col: Индекс столбца.
        :param width: Ширина столбца в пикселях.
        """
        self.prepare_setColumnsWidth(col, col, width)

    def prepare_setValues(self, cellsRange, values, majorDimension="ROWS"):
        """
        Подготавливает запрос для заполнения ячеек данными.

        :param cellsRange: Диапазон ячеек в A1 нотации (например, "A1:B2").
        :param values: Список списков значений для записи в ячейки.
        :param majorDimension: "ROWS" для записи по рядам или "COLUMNS" для записи по столбцам.
        """
        self.valueRanges.append({
            "range": self.sheetTitle + "!" + cellsRange,
            "majorDimension": majorDimension,
            "values": values
        })

    def prepare_mergeCells(self, cellsRange, mergeType="MERGE_ALL"):
        """
        Подготавливает запрос для объединения ячеек.

        :param cellsRange: Диапазон ячеек в A1 нотации (например, "A1:B2").
        :param mergeType: Тип объединения ячеек (по умолчанию "MERGE_ALL").
        """
        self.requests.append({
            "mergeCells": {
                "range": self.toGridRange(cellsRange),
                "mergeType": mergeType
            }
        })

    def prepare_setCellsFormat(self, cellsRange, cellFormat, fields='userEnteredFormat'):
        """
        Подготавливает запрос для форматирования ячеек в диапазоне.

        :param cellsRange: Диапазон ячеек в A1 нотации (например, "A1:B2").
        :param cellFormat: Словарь с параметрами форматирования ячеек.
        :param fields: Поля для обновления.
        """
        self.requests.append({
            "repeatCell": {
                "range": self.toGridRange(cellsRange),
                "cell": {
                    "userEnteredFormat": cellFormat
                },
                "fields": fields
            }
        })

    def prepare_setCellsFormats(self, cellsRange, rows, fields = "userEnteredFormat"):
        """
        Подготавливает запрос для форматирования ячеек в указанном диапазоне.

        :param cellsRange: Диапазон ячеек в A1 нотации (например, "A1:B2").
        :param rows: Список списков словарей форматирования для каждой ячейки.
        :param fields: Поля для обновления.
        """
        self.requests.append({
            "updateCells": {
                "range": self.toGridRange(cellsRange),
                "rows": [{"values": [{"userEnteredFormat": f} for f in row]} for row in rows],
                "fields": fields
            }
        })

    def prepare_setBorders(self, cellsRange, borders):
        """
        Подготавливает запрос для установки границ ячеек.

        :param cellsRange: Диапазон ячеек в A1 нотации (например, "A1:B2").
        :param borders: Словарь с параметрами границ.
        """
        self.requests.append({
            "updateBorders": {
                "range": self.toGridRange(cellsRange),
                **borders
            }
        })

    def runPrepared(self, valueInputOption="USER_ENTERED"):
        """
        Выполняет подготовленные запросы к Google Sheets API.

        :param valueInputOption: Способ интерпретации входных данных, "USER_ENTERED" или "RAW".
        :return: Кортеж со списками ответов от `batchUpdate` и `values.batchUpdate`.
        """
        upd1Res = {'replies': []}
        upd2Res = {'responses': []}
        try:
            if self.requests: # Проверка, что список запросов не пустой
                upd1Res = self.service.spreadsheets().batchUpdate(
                    spreadsheetId=self.spreadsheetId,
                    body={"requests": self.requests}
                ).execute()
            if self.valueRanges: # Проверка, что список диапазонов значений не пустой
                 upd2Res = self.service.spreadsheets().values().batchUpdate(
                    spreadsheetId=self.spreadsheetId,
                    body={"valueInputOption": valueInputOption, "data": self.valueRanges}
                ).execute()
        except Exception as ex:
            logger.error('Ошибка при выполнении запросов к Google Sheets API', ex) # Логируем ошибку
            ... # Точка остановки
            return [],[] # Возвращаем пустые списки при ошибке
        finally:
            self.requests = [] # Очистка списка запросов
            self.valueRanges = [] # Очистка списка диапазонов значений
        return upd1Res.get('replies',[]), upd2Res.get('responses',[]) # возвращаем результаты, обрабатывая случай отсутствия ключа

if __name__ == '__main__':
    CREDENTIALS_FILE = 'test-proj-for-habr-article-1ab131d98a6b.json'  # имя файла с закрытым ключом

    credentials = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILE, [
        'https://www.googleapis.com/auth/spreadsheets',
        'https://www.googleapis.com/auth/drive'
    ])
    httpAuth = credentials.authorize(httplib2.Http())
    service = apiclient.discovery.build('sheets', 'v4', http=httpAuth)
    driveService = apiclient.discovery.build('drive', 'v3', http=httpAuth)

    spreadsheet = service.spreadsheets().create(body={
        'properties': {'title': 'Сие есть название документа', 'locale': 'ru_RU'},
        'sheets': [{
            'properties': {
                'sheetType': 'GRID',
                'sheetId': 0,
                'title': 'Сие есть название листа',
                'gridProperties': {'rowCount': 8, 'columnCount': 5}
            }
        }]
    }).execute()

    driveService.permissions().create(
        fileId=spreadsheet['spreadsheetId'],
        body={'type': 'anyone', 'role': 'reader'},
        fields='id'
    ).execute()

    ss = Spreadsheet(service, driveService, spreadsheet['spreadsheetId'])

    ss.prepare_setColumnWidth(0, 317)
    ss.prepare_setColumnWidth(1, 200)
    ss.prepare_setColumnsWidth(2, 3, 165)
    ss.prepare_setColumnWidth(4, 100)

    ss.prepare_setValues("A1", [["Отчёт"]], majorDimension="ROWS")
    ss.prepare_mergeCells("A1:E1")

    ss.prepare_setValues("A3:E3", [["Дата", "Задача", "Затрачено", "Осталось", "Итого"]], majorDimension="ROWS")
    ss.prepare_setCellsFormat("A3:E3", {'horizontalAlignment': 'CENTER', 'textFormat': {'bold': True}})
    ss.prepare_setBorders('A3:E3', {'bottom': {'style': 'SOLID', 'width': 1, 'color': {'red': 0, 'green': 0, 'blue': 0, 'alpha': 1}}})

    ss.prepare_setValues("A4:A8", [
            ["2 июл 2016 17:57:52", ],
            ["2 июл 2016 17:58:02", ],
            ["2 июл 2016 18:01:02", ],
            ["2 июл 2016 18:04:02", ],
            ["2 июл 2016 18:14:02", ]
        ], majorDimension="ROWS")
    ss.prepare_setValues("B4:B8", [
            ["Задача 1", ],
            ["Задача 2", ],
            ["Задача 3", ],
            ["Задача 4", ],
            ["Задача 5", ]
        ], majorDimension="ROWS")
    ss.prepare_setValues("C4:C8", [
            ["0:00:08", ],
            ["0:00:02", ],
            ["0:02:40", ],
            ["0:01:00", ],
            ["0:05:00", ]
        ], majorDimension="ROWS")
    ss.prepare_setValues("D4:D8", [
            ["0:00:10", ],
            ["0:00:03", ],
            ["0:03:00", ],
            ["0:01:05", ],
            ["0:05:10", ]
        ], majorDimension="ROWS")
    ss.prepare_setValues("E4:E8", [
            ["=D4-C4", ],
            ["=D5-C5", ],
            ["=D6-C6", ],
            ["=D7-C7", ],
            ["=D8-C8", ]
        ], majorDimension="ROWS")
    ss.prepare_setCellsFormat('E4:E8', {'numberFormat': {'pattern': '[h]:mm:ss', 'type': 'TIME'}},
                          fields = 'userEnteredFormat.numberFormat')
    ss.runPrepared()