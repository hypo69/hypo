# Модуль `hypotez/src/goog/spreadsheet/reach_spreadsheet.py`

## Обзор

Модуль `reach_spreadsheet` предоставляет инструменты для работы с Google Таблицами через API v4. Он позволяет создавать, изменять и получать доступ к таблицам, а также выполнять различные операции с листами и ячейками. Модуль использует библиотеки `googleapiclient`, `oauth2client` для взаимодействия с API.

## Классы

### `SpreadsheetError`

**Описание**: Базовый класс для исключений, связанных с ошибками при работе с Google Таблицами.

### `SpreadsheetNotSetError`

**Описание**: Исключение, возникающее, когда объект Spreadsheet не сконфигурирован или не содержит необходимых данных (ID таблицы).

### `SheetNotSetError`

**Описание**: Исключение, возникающее, когда объект Spreadsheet не содержит необходимых данных (ID листа).

### `ReachSpreadsheet`

**Описание**: Класс для взаимодействия с Google Таблицами.


**Методы**

#### `__init__(self, debugMode=False)`

**Описание**: Конструктор класса.

**Параметры**
- `debugMode` (bool, optional): Флаг отладки. По умолчанию `False`.

**Возвращает**:
-  None


#### `create(self, title, sheetTitle, rows=1000, cols=26, locale='en-US', timeZone='Etc/GMT')`

**Описание**: Создаёт новую таблицу в Google Таблицах.

**Параметры**:
- `title` (str): Заголовок создаваемой таблицы.
- `sheetTitle` (str): Заголовок создаваемого листа.
- `rows` (int, optional): Количество строк в листе. По умолчанию 1000.
- `cols` (int, optional): Количество столбцов в листе. По умолчанию 26.
- `locale` (str, optional): Локаль таблицы. По умолчанию 'en-US'.
- `timeZone` (str, optional): Часовой пояс таблицы. По умолчанию 'Etc/GMT'.

**Возвращает**:
- dict: Объект с данными созданной таблицы.

**Возможные исключения**:
- `googleapiclient.errors.HttpError`: Возникает при ошибке выполнения запроса к API.

#### `share(self, shareRequestBody)`

**Описание**: Разрешает доступ к таблице.

**Параметры**:
- `shareRequestBody` (dict): Данные запроса для разграничения доступа.

**Возвращает**:
- dict: Результат операции разграничения доступа.

**Возможные исключения**:
- `SpreadsheetNotSetError`: Возникает, если ID таблицы не установлен.
- `googleapiclient.errors.HttpError`: Возникает при ошибке выполнения запроса к API.


#### `shareWithEmailForReading(self, email)`

**Описание**: Добавляет пользователя в качестве читателя по email.

**Параметры**:
- `email` (str): Email адресс пользователя.


**Возвращает**:
- None

**Возможные исключения**:
- `SpreadsheetNotSetError`


#### `shareWithEmailForWriting(self, email)`

**Описание**: Добавляет пользователя в качестве писателя по email.

**Параметры**:
- `email` (str): Email адресс пользователя.

**Возвращает**:
- None

**Возможные исключения**:
- `SpreadsheetNotSetError`


#### `shareWithAnybodyForReading(self)`

**Описание**: Разрешает доступ к таблице любому пользователю для чтения.

**Возвращает**:
- None

**Возможные исключения**:
- `SpreadsheetNotSetError`


#### `shareWithAnybodyForWriting(self)`

**Описание**: Разрешает доступ к таблице любому пользователю для записи.

**Возвращает**:
- None

**Возможные исключения**:
- `SpreadsheetNotSetError`

#### `getSheetURL(self)`

**Описание**: Возвращает URL ссылки на таблицу.

**Возвращает**:
- str: URL ссылка на таблицу.


**Возможные исключения**:
- `SpreadsheetNotSetError`: Возникает, если ID таблицы не установлен.
- `SheetNotSetError`: Возникает, если ID листа не установлен.

#### `setSpreadsheetById(self, spreadsheetId)`

**Описание**: Устанавливает текущую таблицу по ее ID.

**Параметры**:
- `spreadsheetId` (str): ID таблицы.

**Возвращает**:
- None

**Возможные исключения**:
- `googleapiclient.errors.HttpError`: Возникает при ошибке выполнения запроса к API.

#### `runPrepared(self, valueInputOption='USER_ENTERED')`

**Описание**: Выполняет подготовленные операции с таблицей.

**Параметры**:
- `valueInputOption` (str, optional): Опция для обработки данных в ячейках. По умолчанию 'USER_ENTERED'.

**Возвращает**:
- tuple: Кортеж, содержащий результаты операций `batchUpdate` и `values.batchUpdate`.

**Возможные исключения**:
- `SpreadsheetNotSetError`: Возникает, если ID таблицы не установлен.
- `googleapiclient.errors.HttpError`: Возникает при ошибке выполнения запроса к API.


#### `prepare_addSheet(self, sheetTitle, rows=1000, cols=26)`

**Описание**: Подготавливает запрос на добавление нового листа.

**Параметры**:
- `sheetTitle` (str): Заголовок нового листа.
- `rows` (int, optional): Количество строк в листе. По умолчанию 1000.
- `cols` (int, optional): Количество столбцов в листе. По умолчанию 26.

**Возвращает**:
- None


#### `addSheet(self, sheetTitle, rows=1000, cols=26)`

**Описание**: Добавляет новый лист к текущей таблице.

**Параметры**:
- `sheetTitle` (str): Заголовок нового листа.
- `rows` (int, optional): Количество строк в листе. По умолчанию 1000.
- `cols` (int, optional): Количество столбцов в листе. По умолчанию 26.

**Возвращает**:
- int: ID добавленного листа.

**Возможные исключения**:
- `SpreadsheetNotSetError`: Возникает, если ID таблицы не установлен.
- `googleapiclient.errors.HttpError`: Возникает при ошибке выполнения запроса к API.

#### `toGridRange(self, cellsRange)`

**Описание**: Преобразует строковое представление диапазона ячеек в словарь `GridRange`.

**Параметры**:
- `cellsRange` (str | dict): Строковое представление диапазона ячеек или словарь `GridRange`.


**Возвращает**:
- dict: Словарь `GridRange`.

**Возможные исключения**:
- `SheetNotSetError`: Возникает, если ID листа не установлен.


#### `prepare_setDimensionPixelSize(self, dimension, startIndex, endIndex, pixelSize)`

**Описание**: Подготавливает запрос для изменения размера размерности.

**Параметры**:
- `dimension` (str): Тип размерности (ROWS или COLUMNS).
- `startIndex` (int): Индекс начала.
- `endIndex` (int): Индекс конца.
- `pixelSize` (int): Размер.

**Возвращает**:
- None



#### `prepare_setColumnsWidth(self, startCol, endCol, width)`

#### `prepare_setColumnWidth(self, col, width)`

#### `prepare_setRowsHeight(self, startRow, endRow, height)`

#### `prepare_setRowHeight(self, row, height)`

**Описание**: Подготавливает запросы для изменения ширины/высоты столбцов/строк.


#### `prepare_setValues(self, cellsRange, values, majorDimension='ROWS')`

**Описание**: Подготавливает запрос для добавления значений в ячейки.


#### `prepare_mergeCells(self, cellsRange, mergeType='MERGE_ALL')`

#### `prepare_setCellStringFormatterormat(self, cellsRange, formatJSON, fields='userEnteredFormat')`

#### `prepare_setCellStringFormatterormats(self, cellsRange, formatsJSON, fields='userEnteredFormat')`

**Описание**: Подготавливает запросы для форматирования ячеек.


## Функции

### `htmlColorToJSON(htmlColor)`

**Описание**: Преобразует HTML-цвет в JSON-представление.

**Параметры**:
- `htmlColor` (str): HTML-цвет в формате #RRGGBB.

**Возвращает**:
- dict: Словарь с компонентами цвета.


```