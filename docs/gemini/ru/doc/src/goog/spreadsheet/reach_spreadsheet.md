# Модуль reach_spreadsheet

## Обзор

Этот модуль предоставляет класс `ReachSpreadsheet` для работы с Google Таблицами через API v4. Он позволяет создавать, изменять и получать доступ к данным в таблицах.  Модуль содержит функции для подготовки и выполнения запросов, управления доступом, форматирования ячеек и определения диапазонов.

## Классы

### `SpreadsheetError`

**Описание**: Базовый класс для ошибок, связанных с Google Таблицами.

### `SpreadsheetNotSetError`

**Описание**: Исключение, возникающее, когда не задан идентификатор таблицы (`spreadsheetId`).

### `SheetNotSetError`

**Описание**: Исключение, возникающее, когда не задан идентификатор листа (`sheetId`).

### `ReachSpreadsheet`

**Описание**: Класс для взаимодействия с Google Таблицами.

**Методы**

#### `__init__(self, debugMode=False)`

**Описание**: Инициализирует объект `ReachSpreadsheet`.

**Параметры**:

- `debugMode` (bool, optional): Если `True`, то выводит отладочную информацию. По умолчанию `False`.

**Возвращает**:
-  Не возвращает значение.

**Вызывает исключения**:
- `Exception`: Возникает при ошибке получения учетных данных.


#### `create(self, title, sheetTitle, rows=1000, cols=26, locale='en-US', timeZone='Etc/GMT')`

**Описание**: Создает новую таблицу в Google Таблицах.

**Параметры**:

- `title` (str): Заголовок создаваемой таблицы.
- `sheetTitle` (str): Заголовок создаваемого листа.
- `rows` (int, optional): Количество строк в листе. По умолчанию 1000.
- `cols` (int, optional): Количество столбцов в листе. По умолчанию 26.
- `locale` (str, optional): Локаль таблицы. По умолчанию 'en-US'.
- `timeZone` (str, optional): Временная зона таблицы. По умолчанию 'Etc/GMT'.

**Возвращает**:
- dict: Информация о созданной таблице.

**Вызывает исключения**:
-  Не вызывает исключения.


#### `share(self, shareRequestBody)`

**Описание**: Добавляет разрешения на доступ к таблице.

**Параметры**:

- `shareRequestBody` (dict): Параметры запроса.

**Возвращает**:
- dict: Информация о результате добавления разрешений.

**Вызывает исключения**:
- `SpreadsheetNotSetError`: Если идентификатор таблицы не задан.

#### `shareWithEmailForReading(self, email)`

**Описание**: Добавляет читательские права для указанного email.

**Параметры**:
- `email` (str): Адрес электронной почты.


#### `shareWithEmailForWriting(self, email)`

**Описание**: Добавляет права на запись для указанного email.

**Параметры**:
- `email` (str): Адрес электронной почты.


#### `shareWithAnybodyForReading(self)`

**Описание**: Разрешает доступ для чтения любому пользователю.


#### `shareWithAnybodyForWriting(self)`

**Описание**: Разрешает доступ для записи любому пользователю.


#### `getSheetURL(self)`

**Описание**: Возвращает URL страницы таблицы.

**Возвращает**:
- str: URL страницы таблицы.

**Вызывает исключения**:
- `SpreadsheetNotSetError`: Если идентификатор таблицы не задан.
- `SheetNotSetError`: Если идентификатор листа не задан.

#### `setSpreadsheetById(self, spreadsheetId)`

**Описание**: Устанавливает текущую таблицу по ее идентификатору.

**Параметры**:

- `spreadsheetId` (str): Идентификатор таблицы.

**Возвращает**:
- Не возвращает значение.

**Вызывает исключения**:
- Не вызывает исключения.

#### `runPrepared(self, valueInputOption='USER_ENTERED')`

**Описание**: Выполняет подготовленные запросы к Google Таблицам.

**Параметры**:

- `valueInputOption` (str, optional): Опция для обработки входных данных. По умолчанию 'USER_ENTERED'.

**Возвращает**:
- tuple: Кортеж с результатами выполнения запросов batchUpdate.


#### `prepare_addSheet(self, sheetTitle, rows=1000, cols=26)`

**Описание**: Подготавливает запрос для добавления нового листа.

**Параметры**:

- `sheetTitle` (str): Заголовок нового листа.
- `rows` (int, optional): Количество строк.
- `cols` (int, optional): Количество столбцов.


#### `addSheet(self, sheetTitle, rows=1000, cols=26)`

**Описание**: Добавляет новый лист и устанавливает его как текущий.

**Параметры**:

- `sheetTitle` (str): Заголовок нового листа.
- `rows` (int, optional): Количество строк.
- `cols` (int, optional): Количество столбцов.

**Возвращает**:
- int: Идентификатор добавленного листа.

**Вызывает исключения**:
- `SpreadsheetNotSetError`: Если идентификатор таблицы не задан.


#### `toGridRange(self, cellsRange)`

**Описание**: Преобразует строковый диапазон ячеек в формат `GridRange`.

**Параметры**:

- `cellsRange` (str): Диапазон ячеек в формате "A1:B2".

**Возвращает**:
- dict: Объект `GridRange`.

**Вызывает исключения**:
- `SheetNotSetError`: Если идентификатор листа не задан.


#### `prepare_setDimensionPixelSize(self, dimension, startIndex, endIndex, pixelSize)`

**Описание**: Подготавливает запрос для изменения размера размеров.

**Параметры**:

- `dimension` (str): Размер (ROWS или COLUMNS).
- `startIndex` (int): Начальный индекс.
- `endIndex` (int): Конечный индекс.
- `pixelSize` (int): Размер в пикселях.

#### `prepare_setColumnsWidth(self, startCol, endCol, width)`

#### `prepare_setColumnWidth(self, col, width)`

#### `prepare_setRowsHeight(self, startRow, endRow, height)`

#### `prepare_setRowHeight(self, row, height)`

#### `prepare_setValues(self, cellsRange, values, majorDimension='ROWS')`

#### `prepare_mergeCells(self, cellsRange, mergeType='MERGE_ALL')`

#### `prepare_setCellStringFormatterormat(self, cellsRange, formatJSON, fields='userEnteredFormat')`

#### `prepare_setCellStringFormatterormats(self, cellsRange, formatsJSON, fields='userEnteredFormat')`


## Функции

### `htmlColorToJSON(htmlColor)`

**Описание**: Преобразует HTML цвет в JSON-представление.


## Тесты

Модуль содержит набор тестов для проверки корректности работы класса `ReachSpreadsheet`.


```