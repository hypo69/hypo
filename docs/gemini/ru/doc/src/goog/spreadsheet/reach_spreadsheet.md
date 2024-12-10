# Модуль reach_spreadsheet

## Обзор

Модуль `reach_spreadsheet` предоставляет класс `ReachSpreadsheet` для взаимодействия с Google Sheets API v4. Он позволяет создавать, изменять и получать доступ к данным в Google Таблицах. Класс упрощает работу с API, предоставляя методы для создания таблиц, добавления листов, настройки размеров ячеек, форматирования и записи данных. Также модуль включает в себя методы для настройки прав доступа к таблице и получения ссылки на нее.

## Классы

### `ReachSpreadsheet`

**Описание**: Класс `ReachSpreadsheet` представляет собой обертку над Google Sheets API v4, упрощающую взаимодействие с Google Таблицами.

**Атрибуты**:

- `debugMode` (bool): Флаг, указывающий на режим отладки. Если `True`, то информация о результатах запросов к API выводится в консоль. По умолчанию `False`.
- `credentials` (ServiceAccountCredentials): Объект авторизации для доступа к Google Sheets API.
- `httpAuth` (httplib2.Http): Объект для авторизации HTTP запросов.
- `service` (googleapiclient.discovery.Resource): Объект для взаимодействия с Google Sheets API.
- `driveService` (googleapiclient.discovery.Resource): Объект для взаимодействия с Google Drive API (для управления доступом).
- `spreadsheetId` (str): Идентификатор текущей таблицы.
- `sheetId` (str): Идентификатор текущего листа.
- `sheetTitle` (str): Название текущего листа.
- `requests` (list): Список запросов для `batchUpdate`.
- `valueRanges` (list): Список данных для `batchUpdate`.


**Методы**:

#### `__init__(self, debugMode = False)`

**Описание**: Конструктор класса. Инициализирует атрибуты класса и подключается к API.

**Параметры**:
- `debugMode` (bool, optional): Флаг, указывающий на режим отладки. По умолчанию `False`.

**Возвращает**:
-  Не имеет возвращаемого значения.


#### `create(self, title, sheetTitle, rows = 1000, cols = 26, locale = 'en-US', timeZone = 'Etc/GMT')`

**Описание**: Создает новую Google Таблицу и лист.

**Параметры**:
- `title` (str): Название таблицы.
- `sheetTitle` (str): Название листа.
- `rows` (int, optional): Количество строк в листе. По умолчанию 1000.
- `cols` (int, optional): Количество столбцов в листе. По умолчанию 26.
- `locale` (str, optional): Локаль таблицы. По умолчанию 'en-US'.
- `timeZone` (str, optional): Часовой пояс таблицы. По умолчанию 'Etc/GMT'.

**Возвращает**:
- dict: Словарь с информацией о созданной таблице.

**Вызывает исключения**:
- `SpreadsheetError`: Общее исключение для ошибок, связанных с таблицей.



#### `share(self, shareRequestBody)`

**Описание**: Устанавливает права доступа к таблице.

**Параметры**:
- `shareRequestBody` (dict): Запрос для установки прав доступа.

**Возвращает**:
- dict: Результат запроса.


#### `shareWithEmailForReading(self, email)`

**Описание**: Делит доступ к таблице для чтения с указанным электронным адресом.

**Параметры**:
- `email` (str): Электронный адрес получателя.

**Возвращает**:
- Не имеет возвращаемого значения.



#### `shareWithEmailForWriting(self, email)`

**Описание**: Делит доступ к таблице для записи с указанным электронным адресом.

**Параметры**:
- `email` (str): Электронный адрес получателя.

**Возвращает**:
- Не имеет возвращаемого значения.


#### `shareWithAnybodyForReading(self)`

**Описание**: Делит доступ к таблице для чтения всем.


**Возвращает**:
- Не имеет возвращаемого значения.



#### `shareWithAnybodyForWriting(self)`

**Описание**: Делит доступ к таблице для записи всем.


**Возвращает**:
- Не имеет возвращаемого значения.



#### `getSheetURL(self)`

**Описание**: Возвращает URL ссылки на текущий лист.

**Возвращает**:
- str: URL ссылки на текущий лист.

**Вызывает исключения**:
- `SpreadsheetNotSetError`: Если `spreadsheetId` не установлен.
- `SheetNotSetError`: Если `sheetId` не установлен.



#### `setSpreadsheetById(self, spreadsheetId)`

**Описание**: Устанавливает текущую таблицу по ее ID.

**Параметры**:
- `spreadsheetId` (str): Идентификатор таблицы.

**Возвращает**:
- Не имеет возвращаемого значения.



#### `runPrepared(self, valueInputOption = "USER_ENTERED")`

**Описание**: Выполняет подготовленные запросы к Google Sheets API.

**Параметры**:
- `valueInputOption` (str, optional):  Тип ввода данных. По умолчанию "USER_ENTERED".

**Возвращает**:
- tuple: Кортеж из двух списков: `replies` (ответы на запросы `batchUpdate`) и `responses` (ответы на запросы `values.batchUpdate`).

**Вызывает исключения**:
- `SpreadsheetNotSetError`: Если `spreadsheetId` не установлен.



#### `prepare_addSheet(self, sheetTitle, rows = 1000, cols = 26)`

**Описание**: Подготавливает запрос на добавление нового листа.

**Параметры**:
- `sheetTitle` (str): Название листа.
- `rows` (int, optional): Количество строк в листе. По умолчанию 1000.
- `cols` (int, optional): Количество столбцов в листе. По умолчанию 26.

**Возвращает**:
- Не имеет возвращаемого значения.


#### `addSheet(self, sheetTitle, rows = 1000, cols = 26)`

**Описание**: Добавляет новый лист в текущую таблицу, устанавливает его как текущий и возвращает его ID.

**Параметры**:
- `sheetTitle` (str): Название листа.
- `rows` (int, optional): Количество строк в листе. По умолчанию 1000.
- `cols` (int, optional): Количество столбцов в листе. По умолчанию 26.

**Возвращает**:
- int: ID добавленного листа.

**Вызывает исключения**:
- `SpreadsheetNotSetError`: Если `spreadsheetId` не установлен.



#### `toGridRange(self, cellsRange)`

**Описание**: Преобразует строковое представление диапазона ячеек в объект GridRange.

**Параметры**:
- `cellsRange` (str): Строковое представление диапазона ячеек.


**Возвращает**:
- dict: Словарь, описывающий диапазон ячеек.

**Вызывает исключения**:
- `SheetNotSetError`: Если `sheetId` не установлен.



#### `prepare_setDimensionPixelSize(self, dimension, startIndex, endIndex, pixelSize)`

**Описание**: Подготавливает запрос на изменение размера столбцов или строк.

**Параметры**:
- `dimension` (str): Тип размерности ("COLUMNS" или "ROWS").
- `startIndex` (int): Начальный индекс.
- `endIndex` (int): Конечный индекс.
- `pixelSize` (int): Размер.

**Возвращает**:
- Не имеет возвращаемого значения.

**Вызывает исключения**:
- `SheetNotSetError`: Если `sheetId` не установлен.



#### `prepare_setColumnsWidth(self, startCol, endCol, width)`

#### `prepare_setColumnWidth(self, col, width)`

#### `prepare_setRowsHeight(self, startRow, endRow, height)`

#### `prepare_setRowHeight(self, row, height)`

**Описание**: Методы для подготовки запросов на изменение ширины столбцов и высоты строк.


#### `prepare_setValues(self, cellsRange, values, majorDimension = "ROWS")`

#### `prepare_mergeCells(self, cellsRange, mergeType = "MERGE_ALL")`

#### `prepare_setCellStringFormatterormat(self, cellsRange, formatJSON, fields = "userEnteredFormat")`

#### `prepare_setCellStringFormatterormats(self, cellsRange, formatsJSON, fields = "userEnteredFormat")`

**Описание**: Методы для подготовки запросов на запись данных, слияние ячеек и форматирование ячеек.

## Функции

### `htmlColorToJSON(htmlColor)`

**Описание**: Преобразует HTML-код цвета в JSON-формат.

**Параметры**:
- `htmlColor` (str): HTML-код цвета.


**Возвращает**:
- dict: Словарь с компонентами цвета (red, green, blue).


### `testCreateSpreadsheet()`, `testSetSpreadsheet()`, `testAddSheet()`, ...

**Описание**: Тестовые функции для проверки работы класса `ReachSpreadsheet`.


## Исключения

### `SpreadsheetError`

**Описание**: Базовое исключение для ошибок, связанных с Google Таблицами.

### `SpreadsheetNotSetError`

**Описание**: Исключение, генерируемое при попытке использования метода, требующего установленной таблицы, без ее предварительной установки.

### `SheetNotSetError`

**Описание**: Исключение, генерируемое при попытке использования метода, требующего установленного листа, без его предварительной установки.


```