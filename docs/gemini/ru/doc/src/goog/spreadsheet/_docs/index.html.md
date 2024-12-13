# Документация для `src.goog.spreadsheet._docs`

## Обзор

Данный модуль представляет собой HTML-документ, описывающий процесс программного создания и настройки Google Sheets с использованием Python и Google Sheets API v4. Документ содержит подробное руководство по созданию, настройке и заполнению таблиц, включая примеры кода и объяснения ключевых концепций.

## Содержание

- [Постановка задачи](#постановка-задачи)
- [Решение](#решение)
    - [Шаг 1. Создать сервисный аккаунт](#шаг-1-создать-сервисный-аккаунт)
    - [Шаг 2. Установить необходимые библиотеки](#шаг-2-установить-необходимые-библиотеки)
    - [Шаг 3. Кодить](#шаг-3-кодить)
        - [3.1. Service-объект](#31-service-объект)
        - [3.2. Термины и id'шники](#32-термины-и-idшники)
        - [3.3. Новый spreadsheet](#33-новый-spreadsheet)
        - [3.4. Доступ к новому документу](#34-доступ-к-новому-документу)
        - [3.5. Ещё немного теории](#35-ещё-немного-теории)
        - [3.6. Ширина столбцов](#36-ширина-столбцов)
        - [3.7. Логика класса-обёртки](#37-логика-класса-обёртки)
        - [3.8. Заполнение ячеек данными](#38-заполнение-ячеек-данными)
        - [3.9. Объединение ячеек, настройка жирности, формата отображения, цвета фона и прочего](#39-объединение-ячеек-настройка-жирности-формата-отображения-цвета-фона-и-прочего)
- [Некоторые тонкости](#некоторые-тонкости)
- [Заключение](#заключение)

## Постановка задачи

Документ описывает процесс создания таблицы Google Sheets программно на Python. Требуется создать таблицу, обладающую следующими характеристиками:
*   заданная ширина столбцов;
*   объединённая верхняя ячейка (A1:E1);
*   настройка формата отображения, размера шрифта, жирности, выравнивания текста и цвета фона для некоторых ячеек;
*   вычисление значений в последнем столбце по формулам;
*   граница под ячейками A3:E3.

## Решение

### Шаг 1. Создать сервисный аккаунт

Для доступа к Google Sheets API v4 требуется сервисный аккаунт:
1.  Создайте новый проект в [Google Developers Console](https://console.developers.google.com/project).
2.  Включите Drive API и Sheets API для проекта.
3.  Создайте учётные данные и сохраните закрытый ключ (JSON-файл).

### Шаг 2. Установить необходимые библиотеки

Необходимо установить библиотеку `google-api-python-client` с помощью `pip`:

```bash
pip install --upgrade google-api-python-client
```
Эта библиотека включает в себя `oauth2client` и другие необходимые зависимости.

### Шаг 3. Кодить

#### 3.1. Service-объект

Импортируем необходимые модули:

```python
import httplib2
import apiclient.discovery
from oauth2client.service_account import ServiceAccountCredentials
```

Создаём Service-объект для работы с Google-таблицами:
```python
CREDENTIALS_FILE = 'test-proj-for-habr-article-1ab131d98a6b.json'  # имя файла с закрытым ключом
credentials = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILE, 
                                                                ['https://www.googleapis.com/auth/spreadsheets',
                                                                'https://www.googleapis.com/auth/drive'])
httpAuth = credentials.authorize(httplib2.Http())
service = apiclient.discovery.build('sheets', 'v4', http = httpAuth)
```

#### 3.2. Термины и id'шники

*   **spreadsheet** (документ) – Google-документ с таблицами. Имеет `spreadsheetId` (например, `1kygOW5wSSVqwf26M-OCT72i0FX0olZAz4duT2i6psp4`).
*   **sheet** (лист) – вкладка с одной из таблиц. Имеет `sheetId`, являющийся числом (id первого листа в документе равен 0). Все листы имеют разные id и названия.

Ссылка на конкретный лист имеет вид: `https://docs.google.com/spreadsheets/d/<spreadsheetId>/edit#gid=<sheetId>`

#### 3.3. Новый spreadsheet

Для создания нового spreadsheet используем метод `spreadsheets.create` объекта `service`.
```python
spreadsheet = service.spreadsheets().create(body = {
    'properties': {'title': 'Сие есть название документа', 'locale': 'ru_RU'},
    'sheets': [{'properties': {'sheetType': 'GRID',
                               'sheetId': 0,
                               'title': 'Сие есть название листа',
                               'gridProperties': {'rowCount': 8, 'columnCount': 5}}}]
}).execute()
```
В результате получаем объект `Spreadsheet` со всеми заполненными параметрами, включая `spreadsheetId`.

#### 3.4. Доступ к новому документу

Google Sheets API не имеет метода для настройки доступа к документу, поэтому используется Google Drive API v3:

```python
driveService = apiclient.discovery.build('drive', 'v3', http = httpAuth)
shareRes = driveService.permissions().create(
    fileId = spreadsheet['spreadsheetId'],
    body = {'type': 'anyone', 'role': 'reader'},  # доступ на чтение кому угодно
    fields = 'id'
).execute()
```

Для доступа к редактированию пользователю `user@example.com`:
```python
body = {'type': 'user', 'role': 'writer', 'emailAddress': 'user@example.com'}
```

#### 3.5. Ещё немного теории

Используется функция `spreadsheets.batchUpdate` для применения нескольких изменений к документу.

#### 3.6. Ширина столбцов

Для задания ширины столбцов используется `UpdateDimensionPropertiesRequest`:

```python
results = service.spreadsheets().batchUpdate(spreadsheetId = spreadsheet['spreadsheetId'], body = {
  "requests": [
    {
      "updateDimensionProperties": {
        "range": {
          "sheetId": 0,
          "dimension": "COLUMNS",
          "startIndex": 0,
          "endIndex": 1
        },
        "properties": {
          "pixelSize": 317
        },
        "fields": "pixelSize"
      }
    },
    {
      "updateDimensionProperties": {
        "range": {
          "sheetId": 0,
          "dimension": "COLUMNS",
          "startIndex": 1,
          "endIndex": 2
        },
        "properties": {
          "pixelSize": 200
        },
        "fields": "pixelSize"
      }
    },
    {
      "updateDimensionProperties": {
        "range": {
          "sheetId": 0,
          "dimension": "COLUMNS",
          "startIndex": 2,
          "endIndex": 4
        },
        "properties": {
          "pixelSize": 165
        },
        "fields": "pixelSize"
      }
    },
    {
      "updateDimensionProperties": {
        "range": {
          "sheetId": 0,
          "dimension": "COLUMNS",
          "startIndex": 4,
          "endIndex": 5
        },
        "properties": {
          "pixelSize": 100
        },
        "fields": "pixelSize"
      }
    }
  ]
}).execute()
```

#### 3.7. Логика класса-обёртки

Создан класс `Spreadsheet`, который хранит список `requests` и в методе `runPrepared` передает его функции `spreadsheets.batchUpdate`.
Методы `prepare_setColumnWidth` и `prepare_setColumnsWidth` добавляют элементы в этот список:

```python
class Spreadsheet:
    def prepare_setDimensionPixelSize(self, dimension, startIndex, endIndex, pixelSize):
        self.requests.append({"updateDimensionProperties": {
            "range": {"sheetId": self.sheetId,
                      "dimension": dimension,
                      "startIndex": startIndex,
                      "endIndex": endIndex},
            "properties": {"pixelSize": pixelSize},
            "fields": "pixelSize"}})

    def prepare_setColumnsWidth(self, startCol, endCol, width):
        self.prepare_setDimensionPixelSize("COLUMNS", startCol, endCol + 1, width)

    def prepare_setColumnWidth(self, col, width):
        self.prepare_setColumnsWidth(col, col, width)
```
Использование класса-обёртки:
```python
ss.prepare_setColumnWidth(0, 317)
ss.prepare_setColumnWidth(1, 200)
ss.prepare_setColumnsWidth(2, 3, 165)
ss.prepare_setColumnWidth(4, 100)
ss.runPrepared()
```

#### 3.8. Заполнение ячеек данными

Для заполнения ячеек используется `spreadsheets.values.batchUpdate`.  Принимает параметр `ValueInputOption`: `USER_ENTERED` для интерпретации данных или `RAW` для сохранения в сыром виде.

Пример без использования класса-обёртки:
```python
results = service.spreadsheets().values().batchUpdate(spreadsheetId = spreadsheet['spreadsheetId'], body = {
    "valueInputOption": "USER_ENTERED",
    "data": [
        {"range": "Сие есть название листа!B2:C3",
         "majorDimension": "ROWS",
         "values": [["This is B2", "This is C2"], ["This is B3", "This is C3"]]},
        {"range": "Сие есть название листа!D5:E6",
         "majorDimension": "COLUMNS",
         "values": [["This is D5", "This is D6"], ["This is E5", "=5+5"]]}
    ]
}).execute()
```

Метод `prepare_setValues` добавляет прямоугольник и данные в список `valueRanges`, который передается в `spreadsheets.values.batchUpdate` при вызове `runPrepared`:
```python
class Spreadsheet:
    def prepare_setValues(self, cellsRange, values, majorDimension = "ROWS"):
        self.valueRanges.append({"range": self.sheetTitle + "!" + cellsRange, "majorDimension": majorDimension, "values": values})

    def runPrepared(self, valueInputOption = "USER_ENTERED"):
        upd1Res = {'replies': []}
        upd2Res = {'responses': []}
        try:
            if len(self.requests) > 0:
                upd1Res = self.service.spreadsheets().batchUpdate(spreadsheetId = self.spreadsheetId,
                                                                  body = {"requests": self.requests}).execute()
            if len(self.valueRanges) > 0:
                upd2Res = self.service.spreadsheets().values().batchUpdate(spreadsheetId = self.spreadsheetId,
                                                                           body = {"valueInputOption": valueInputOption,
                                                                                   "data": self.valueRanges}).execute()
        finally:
            self.requests = []
            self.valueRanges = []
        return (upd1Res['replies'], upd2Res['responses'])
```
Использование с классом-обёрткой:
```python
ss.prepare_setValues("B2:C3", [["This is B2", "This is C2"], ["This is B3", "This is C3"]])
ss.prepare_setValues("D5:E6", [["This is D5", "This is D6"], ["This is E5", "=5+5"]], "COLUMNS")
ss.runPrepared()
```

#### 3.9. Объединение ячеек, настройка жирности, формата отображения, цвета фона и прочего

*   `MergeCellsRequest` – объединение ячеек.
    ```python
    ss.prepare_mergeCells('A1:E1')
    ```
*   `RepeatCellRequest` – применение одинаковых изменений к ячейкам в указанном диапазоне.
    ```python
    ss.prepare_setCellsFormat('A3:E3', {'horizontalAlignment': 'CENTER', 'textFormat': {'bold': True}})
    ss.prepare_setCellsFormat('E4:E8', {'numberFormat': {'pattern': '[h]:mm:ss', 'type': 'TIME'}},
                              fields = 'userEnteredFormat.numberFormat')
    ```
*   `UpdateCellsRequest` – применение изменений для каждой ячейки в указанном диапазоне.
    ```python
    ss.prepare_setCellsFormats('B4:C5', [[{'backgroundColor': {'red': 1, 'green': 0, 'blue': 0}},
                                      {'backgroundColor': {'red': 0, 'green': 1, 'blue': 0}}],
                                     [{'backgroundColor': {'red': 0, 'green': 0, 'blue': 1}},
                                      {'backgroundColor': {'red': 1, 'green': 1, 'blue': 0}}]])
    ```
*   `UpdateBordersRequest` – задание границы ячеек.

## Некоторые тонкости

*   **Q1:** Зачем `locale` = `ru_RU`?
    *   **A1:** Для распознавания дат и времени таблицей.
*   **Q2:** Откуда формат "продолжительность"?
    *   **A2:** Установлен вручную, затем получен через API.
*   **Q3:** Разный формат `range` в `spreadsheets.batchUpdate` и `spreadsheets.values.batchUpdate`?
    *   **A3:** `GridRange` и A1 notation.
*   **Q4:** Пикачу посажен программно?
    *   **A4:** Нет, вручную.
*   **Q5:** Ограничения API?
    *   **A5:** Квоты, за которыми можно следить в Google Developers Console.

## Заключение

Документ предоставляет подробное руководство по программному созданию и настройке таблиц Google Sheets с использованием Python и Google Sheets API v4.

Важные ссылки:
*   [Google Sheets API v4](https://developers.google.com/sheets/)
*   [Google Developers Console](https://console.developers.google.com/)
*   [Класс-обёртка Spreadsheet и примеры его использования](https://github.com/Tsar/Spreadsheet/blob/master/Spreadsheet.py)