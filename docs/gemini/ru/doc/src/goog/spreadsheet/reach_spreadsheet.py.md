# Модуль `reach_spreadsheet`

## Обзор

Модуль `reach_spreadsheet` предоставляет функциональность для взаимодействия с Google Sheets API v4 и Google Drive API v3. Он предназначен для создания, чтения, записи и настройки таблиц Google. Модуль включает в себя классы и методы для работы с таблицами, листами и ячейками, а также для управления правами доступа к таблицам.

## Содержание

- [Классы](#классы)
  - [`SpreadsheetError`](#spreadsheeterror)
  - [`SpreadsheetNotSetError`](#spreadsheetnotseterror)
  - [`SheetNotSetError`](#sheetnotseterror)
  - [`ReachSpreadsheet`](#reachspreadsheet)
- [Функции](#функции)
  - [`htmlColorToJSON`](#htmlcolortojson)
- [Тестовые функции](#тестовые-функции)
    - [`testCreateSpreadsheet`](#testcreatespreadsheet)
    - [`testSetSpreadsheet`](#testsetspreadsheet)
    - [`testAddSheet`](#testaddsheet)
    - [`testSetDimensions`](#testsetdimensions)
    - [`testGridRangeForStr`](#testgridrangeforstr)
    - [`testSetCellStringFormatterormat`](#testsetcellstringformatterormat)
    - [`testPureBlackBorder`](#testpureblackborder)
    - [`testUpdateCellStringFormatterieldsArg`](#testupdatecellstringformatterieldsarg)
    - [`create_pricelist`](#create_pricelist)
    - [`testCreateTimeManagementReport`](#testcreatetimemanagementreport)

## Классы

### `SpreadsheetError`

**Описание**: Базовый класс для ошибок, связанных с работой с таблицами.

### `SpreadsheetNotSetError`

**Описание**: Исключение, возникающее, когда ID таблицы не установлен.

### `SheetNotSetError`

**Описание**: Исключение, возникающее, когда ID листа не установлен.

### `ReachSpreadsheet`

**Описание**: Класс, представляющий собой интерфейс для взаимодействия с Google Sheets API.

**Методы**:

- `__init__(self, debugMode = False)`
  
   **Описание**: Конструктор класса `ReachSpreadsheet`. Инициализирует объект, устанавливает режим отладки, создает credentials и авторизуется в Google API.
   
    **Параметры**:
     - `debugMode` (bool, optional): Флаг для включения режима отладки. По умолчанию `False`.
     
- `create(self, title, sheetTitle, rows = 1000, cols = 26, locale = 'en-US', timeZone = 'Etc/GMT')`
    
    **Описание**: Создает новую таблицу Google.
    
    **Параметры**:
    - `title` (str): Заголовок таблицы.
    - `sheetTitle` (str): Заголовок первого листа.
    - `rows` (int, optional): Количество строк в листе. По умолчанию `1000`.
    - `cols` (int, optional): Количество столбцов в листе. По умолчанию `26`.
    - `locale` (str, optional): Локаль таблицы. По умолчанию `en-US`.
    - `timeZone` (str, optional): Временная зона таблицы. По умолчанию `Etc/GMT`.
    
- `share(self, shareRequestBody)`
    
    **Описание**:  Делится таблицей с указанными правами.
    
    **Параметры**:
     - `shareRequestBody` (dict): Тело запроса на предоставление доступа.
    
    **Вызывает исключения**:
    - `SpreadsheetNotSetError`: Если ID таблицы не установлен.
    
- `shareWithEmailForReading(self, email)`
    
    **Описание**: Предоставляет доступ на чтение к таблице для указанного email.
    
    **Параметры**:
     - `email` (str): Email пользователя, которому предоставляется доступ.
     
- `shareWithEmailForWriting(self, email)`
    
    **Описание**: Предоставляет доступ на запись к таблице для указанного email.
    
    **Параметры**:
    - `email` (str): Email пользователя, которому предоставляется доступ.
     
-  `shareWithAnybodyForReading(self)`
    
    **Описание**: Предоставляет доступ на чтение к таблице для всех пользователей.

- `shareWithAnybodyForWriting(self)`
    
    **Описание**: Предоставляет доступ на запись к таблице для всех пользователей.

- `getSheetURL(self)`
    
    **Описание**: Возвращает URL текущей таблицы.
    
    **Возвращает**:
    - str: URL текущей таблицы.
    
    **Вызывает исключения**:
    - `SpreadsheetNotSetError`: Если ID таблицы не установлен.
    - `SheetNotSetError`: Если ID листа не установлен.
    
- `setSpreadsheetById(self, spreadsheetId)`
    
    **Описание**: Устанавливает текущую таблицу по ее ID.
    
    **Параметры**:
    - `spreadsheetId` (str): ID таблицы.

- `runPrepared(self, valueInputOption = "USER_ENTERED")`
    
    **Описание**: Выполняет подготовленные запросы к таблице.
    
    **Параметры**:
    - `valueInputOption` (str, optional): Опция ввода значений. По умолчанию `"USER_ENTERED"`.
    
    **Возвращает**:
     - `tuple[list[dict], list[dict]]`: Кортеж с результатами выполнения запросов.
     
    **Вызывает исключения**:
    - `SpreadsheetNotSetError`: Если ID таблицы не установлен.
    
- `prepare_addSheet(self, sheetTitle, rows = 1000, cols = 26)`
    
    **Описание**: Подготавливает запрос на добавление нового листа.
    
    **Параметры**:
    - `sheetTitle` (str): Заголовок нового листа.
    - `rows` (int, optional): Количество строк в листе. По умолчанию `1000`.
    - `cols` (int, optional): Количество столбцов в листе. По умолчанию `26`.

- `addSheet(self, sheetTitle, rows = 1000, cols = 26)`
    
    **Описание**: Добавляет новый лист к текущей таблице.
    
    **Параметры**:
    - `sheetTitle` (str): Заголовок нового листа.
    - `rows` (int, optional): Количество строк в листе. По умолчанию `1000`.
    - `cols` (int, optional): Количество столбцов в листе. По умолчанию `26`.
    
    **Возвращает**:
     - `int`: ID добавленного листа.
    
    **Вызывает исключения**:
    - `SpreadsheetNotSetError`: Если ID таблицы не установлен.
    
- `toGridRange(self, cellsRange)`
    
    **Описание**: Преобразует строковый диапазон в объект GridRange.
    
    **Параметры**:
    - `cellsRange` (str | dict): Строковый диапазон (например, `"A3:B4"`) или словарь с настройками диапазона.
    
    **Возвращает**:
     - `dict`: Объект GridRange.
     
    **Вызывает исключения**:
     - `SheetNotSetError`: Если ID листа не установлен.
     
- `prepare_setDimensionPixelSize(self, dimension, startIndex, endIndex, pixelSize)`
    
    **Описание**: Подготавливает запрос на изменение размера столбцов или строк в пикселях.
    
    **Параметры**:
    - `dimension` (str): `"COLUMNS"` или `"ROWS"`.
    - `startIndex` (int): Индекс начала диапазона.
    - `endIndex` (int): Индекс конца диапазона.
    - `pixelSize` (int): Размер в пикселях.
    
    **Вызывает исключения**:
     - `SheetNotSetError`: Если ID листа не установлен.
    
- `prepare_setColumnsWidth(self, startCol, endCol, width)`
    
    **Описание**: Подготавливает запрос на изменение ширины столбцов.
    
    **Параметры**:
    - `startCol` (int): Индекс начала столбца.
    - `endCol` (int): Индекс конца столбца.
    - `width` (int): Ширина столбца в пикселях.
    
- `prepare_setColumnWidth(self, col, width)`
    
    **Описание**: Подготавливает запрос на изменение ширины одного столбца.
    
    **Параметры**:
    - `col` (int): Индекс столбца.
    - `width` (int): Ширина столбца в пикселях.
    
- `prepare_setRowsHeight(self, startRow, endRow, height)`
    
    **Описание**: Подготавливает запрос на изменение высоты строк.
    
    **Параметры**:
    - `startRow` (int): Индекс начала строки.
    - `endRow` (int): Индекс конца строки.
    - `height` (int): Высота строки в пикселях.
    
- `prepare_setRowHeight(self, row, height)`
    
    **Описание**: Подготавливает запрос на изменение высоты одной строки.
    
    **Параметры**:
    - `row` (int): Индекс строки.
    - `height` (int): Высота строки в пикселях.
    
- `prepare_setValues(self, cellsRange, values, majorDimension = "ROWS")`
    
    **Описание**: Подготавливает запрос на установку значений в ячейки.
    
    **Параметры**:
    - `cellsRange` (str): Диапазон ячеек (например, `"A1:B2"`).
    - `values` (list): Список списков значений для ячеек.
    - `majorDimension` (str, optional): Основное измерение для значений. По умолчанию `"ROWS"`.
    
    **Вызывает исключения**:
    - `SheetNotSetError`: Если заголовок листа не установлен.
    
- `prepare_mergeCells(self, cellsRange, mergeType = "MERGE_ALL")`
    
    **Описание**: Подготавливает запрос на объединение ячеек.
    
    **Параметры**:
    - `cellsRange` (str): Диапазон ячеек (например, `"A1:B2"`).
    - `mergeType` (str, optional): Тип объединения. По умолчанию `"MERGE_ALL"`.
    
- `prepare_setCellStringFormatterormat(self, cellsRange, formatJSON, fields = "userEnteredFormat")`
    
    **Описание**: Подготавливает запрос на установку формата ячеек.
    
    **Параметры**:
    - `cellsRange` (str): Диапазон ячеек (например, `"A1:B2"`).
    - `formatJSON` (dict): Словарь с настройками формата.
    - `fields` (str, optional): Поля для обновления. По умолчанию `"userEnteredFormat"`.
    
- `prepare_setCellStringFormatterormats(self, cellsRange, formatsJSON, fields = "userEnteredFormat")`
    
    **Описание**: Подготавливает запрос на установку форматов для нескольких ячеек.
    
    **Параметры**:
    - `cellsRange` (str): Диапазон ячеек (например, `"A1:B2"`).
    - `formatsJSON` (list[list[dict]]): Список списков словарей с настройками формата для каждой ячейки.
    - `fields` (str, optional): Поля для обновления. По умолчанию `"userEnteredFormat"`.

## Функции

### `htmlColorToJSON(htmlColor)`

**Описание**: Преобразует HTML-цвет в формат JSON.

**Параметры**:
- `htmlColor` (str): HTML-код цвета, например, `" #FF0000"` или `"FF0000"`.

**Возвращает**:
- `dict`: JSON-представление цвета в формате `{ "red": float, "green": float, "blue": float }`.

## Тестовые функции

### `testCreateSpreadsheet()`

**Описание**: Тестирует создание новой таблицы.

### `testSetSpreadsheet()`

**Описание**: Тестирует установку текущей таблицы по ее ID.

### `testAddSheet()`

**Описание**: Тестирует добавление нового листа в таблицу.

### `testSetDimensions()`

**Описание**: Тестирует установку размеров столбцов и строк.

### `testGridRangeForStr()`

**Описание**: Тестирует преобразование строковых диапазонов в объекты `GridRange`.

### `testSetCellStringFormatterormat()`

**Описание**: Тестирует установку формата ячеек.

### `testPureBlackBorder()`

**Описание**: Тестирует установку черной границы для ячеек.

### `testUpdateCellStringFormatterieldsArg()`

**Описание**: Тестирует обновление форматов ячеек с указанием полей для обновления.

### `create_pricelist(docTitle, sheetTitle, values: list)`

**Описание**: Создает таблицу с заданными значениями.

**Параметры**:
  - `docTitle` (str): Название документа
  - `sheetTitle` (str): Название листа
  - `values` (list): Список списков значений для ячеек.
  
### `testCreateTimeManagementReport()`

**Описание**: Создает тестовый отчет для управления временем.