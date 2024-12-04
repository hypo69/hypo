# Модуль reach_spreadsheet

## Обзор

Этот модуль предоставляет класс `ReachSpreadsheet` для взаимодействия с Google Sheets API v4.  Он позволяет создавать, редактировать и получать данные из электронных таблиц Google.  Модуль включает функции для создания листов, изменения размеров ячеек, форматирования, добавления и удаления строк,  а также для совместной работы с таблицей.

## Классы

### `SpreadsheetError`

**Описание**: Базовый класс для исключений, связанных с работой с электронными таблицами.


### `SpreadsheetNotSetError`

**Описание**: Исключение, которое возникает, если электронная таблица не выбрана.


### `SheetNotSetError`

**Описание**: Исключение, которое возникает, если лист не выбран.


### `ReachSpreadsheet`

**Описание**: Класс для работы с электронными таблицами Google.


**Методы**

#### `__init__(self, debugMode=False)`

**Описание**: Инициализирует объект `ReachSpreadsheet`.

**Параметры**:

- `debugMode` (bool, optional):  Флаг отладки. По умолчанию `False`.

**Возвращает**:

-  Не имеет возвращаемого значения.

**Вызывает исключения**:

-  Любое исключение, которое возникает при создании `ServiceAccountCredentials` или при вызове `googleapiclient.discovery.build`.


#### `create(self, title, sheetTitle, rows=1000, cols=26, locale='en-US', timeZone='Etc/GMT')`

**Описание**: Создает новую электронную таблицу с заданным названием и заголовком листа.

**Параметры**:

- `title` (str): Название электронной таблицы.
- `sheetTitle` (str): Название листа.
- `rows` (int, optional): Количество строк в листе. По умолчанию 1000.
- `cols` (int, optional): Количество столбцов в листе. По умолчанию 26.
- `locale` (str, optional): Локаль таблицы. По умолчанию 'en-US'.
- `timeZone` (str, optional): Часовой пояс таблицы. По умолчанию 'Etc/GMT'.


**Возвращает**:

-  Словарь, содержащий данные о созданной таблице.

**Вызывает исключения**:

-  Любое исключение, которое возникает при вызове `self.service.spreadsheets().create()`.


#### `share(self, shareRequestBody)`

**Описание**: Делит таблицу.

**Параметры**:

- `shareRequestBody` (dict): Данные о том, с кем и как делится таблица.


**Возвращает**:

-  Словарь, содержащий данные о результатах разделения таблицы.


**Вызывает исключения**:

- `SpreadsheetNotSetError`: Если `self.spreadsheetId` не задан.
-  Любое исключение, которое возникает при вызове `self.driveService.permissions().create()`.


#### `shareWithEmailForReading(self, email)`

**Описание**: Делит таблицу для чтения с заданным email.


**Параметры**:

- `email` (str): Email адресс пользователя.


**Возвращает**:

-  Не имеет возвращаемого значения.


**Вызывает исключения**:

-  Исключения метода `share`.


#### `shareWithEmailForWriting(self, email)`

**Описание**: Делит таблицу для записи с заданным email.


**Параметры**:

- `email` (str): Email адресс пользователя.


**Возвращает**:

-  Не имеет возвращаемого значения.


**Вызывает исключения**:

-  Исключения метода `share`.


#### `shareWithAnybodyForReading(self)`

**Описание**: Делит таблицу для чтения всем пользователям.

**Возвращает**:

-  Не имеет возвращаемого значения.


**Вызывает исключения**:

-  Исключения метода `share`.


#### `shareWithAnybodyForWriting(self)`

**Описание**: Делит таблицу для записи всем пользователям.

**Возвращает**:

-  Не имеет возвращаемого значения.


**Вызывает исключения**:

-  Исключения метода `share`.



#### `getSheetURL(self)`

**Описание**: Возвращает URL страницы электронной таблицы.

**Возвращает**:

-  str: URL страницы электронной таблицы.

**Вызывает исключения**:

- `SpreadsheetNotSetError`: Если `self.spreadsheetId` не задан.
- `SheetNotSetError`: Если `self.sheetId` не задан.


#### `setSpreadsheetById(self, spreadsheetId)`

**Описание**: Устанавливает текущую электронную таблицу по ее ID.

**Параметры**:

- `spreadsheetId` (str): ID электронной таблицы.

**Возвращает**:

-  Не имеет возвращаемого значения.

**Вызывает исключения**:

-  Любое исключение, возникающее при вызове `self.service.spreadsheets().get()`.


#### `runPrepared(self, valueInputOption='USER_ENTERED')`

**Описание**: Выполняет подготовленные запросы к Google Sheets.

**Параметры**:

- `valueInputOption` (str, optional): Способ ввода значений. По умолчанию 'USER_ENTERED'.

**Возвращает**:

- Tuple[list, list]: Кортеж с двумя списками, содержащими результаты выполнения `batchUpdate`.


**Вызывает исключения**:

- `SpreadsheetNotSetError`: Если `self.spreadsheetId` не задан.


#### `prepare_addSheet(self, sheetTitle, rows=1000, cols=26)`

**Описание**: Подготавливает запрос на добавление нового листа.

**Параметры**:

- `sheetTitle` (str): Название листа.
- `rows` (int, optional): Количество строк.
- `cols` (int, optional): Количество столбцов.


**Возвращает**:

- Не имеет возвращаемого значения.


#### `addSheet(self, sheetTitle, rows=1000, cols=26)`

**Описание**: Добавляет новый лист к текущей электронной таблице.

**Параметры**:

- `sheetTitle` (str): Название листа.
- `rows` (int, optional): Количество строк.
- `cols` (int, optional): Количество столбцов.

**Возвращает**:

- int: ID добавленного листа.

**Вызывает исключения**:

- `SpreadsheetNotSetError`: Если `self.spreadsheetId` не задан.


#### `toGridRange(self, cellsRange)`

**Описание**: Преобразует строковое представление диапазона ячеек в словарь GridRange.

**Параметры**:

- `cellsRange` (str | dict):  Строковое представление диапазона ячеек (например, "A1:B2") или словарь GridRange.


**Возвращает**:

- dict: Словарь GridRange.


**Вызывает исключения**:

- `SheetNotSetError`: Если `self.sheetId` не задан.


#### `prepare_setDimensionPixelSize(self, dimension, startIndex, endIndex, pixelSize)`

**Описание**: Подготавливает запрос на изменение размера dimension (строки/столбцы).

**Параметры**:

- `dimension` (str): Тип dimension ("ROWS" или "COLUMNS").
- `startIndex` (int): Начальный индекс dimension.
- `endIndex` (int): Конечный индекс dimension.
- `pixelSize` (int): Размер dimension в пикселях.


**Возвращает**:

- Не имеет возвращаемого значения.


**Вызывает исключения**:

- `SheetNotSetError`: Если `self.sheetId` не задан.


#### `prepare_setColumnsWidth(self, startCol, endCol, width)`

#### `prepare_setColumnWidth(self, col, width)`

#### `prepare_setRowsHeight(self, startRow, endRow, height)`

#### `prepare_setRowHeight(self, row, height)`

(Описания остальных методов аналогично, используя стандартный шаблон Markdown)

#### `prepare_setValues(self, cellsRange, values, majorDimension='ROWS')`

#### `prepare_mergeCells(self, cellsRange, mergeType='MERGE_ALL')`

#### `prepare_setCellStringFormatterormat(self, cellsRange, formatJSON, fields='userEnteredFormat')`

#### `prepare_setCellStringFormatterormats(self, cellsRange, formatsJSON, fields='userEnteredFormat')`



## Функции

### `htmlColorToJSON(htmlColor)`

**Описание**: Преобразует HTML цвет в JSON-формат.

**Параметры**:

- `htmlColor` (str): HTML цвет (например, "#FF0000").

**Возвращает**:

- dict: JSON-формат цвета.


## Тесты (Функции)

(Описания функций-тестов аналогично, используя стандартный шаблон Markdown. Пример: `testCreateSpreadsheet()`, `testSetSpreadsheet()`, ...)


```