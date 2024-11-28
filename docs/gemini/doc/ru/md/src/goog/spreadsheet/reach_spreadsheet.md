# Модуль reach_spreadsheet

## Обзор

Модуль `reach_spreadsheet` предоставляет инструменты для взаимодействия с Google Sheets API v4.  Он позволяет создавать, изменять и получать доступ к данным электронных таблиц. Модуль реализует класс `ReachSpreadsheet`, упрощающий взаимодействие с API.  Поддерживаются операции создания листов, изменения ширины колонок/высоты строк,  заполнение ячеек значениями, объединение ячеек и форматирование ячеек (включая цвет фона и шрифта).  Модуль также включает обработку ошибок и логирование.

## Оглавление

- [Модуль reach_spreadsheet](#модуль-reach_spreadsheet)
- [Обзор](#обзор)
- [Классы](#классы)
    - [ReachSpreadsheet](#reachspreadsheet)
        - [`__init__`](#init)
        - [`create`](#create)
        - [`share`](#share)
        - [`shareWithEmailForReading`](#shareWithEmailForReading)
        - [`shareWithEmailForWriting`](#shareWithEmailForWriting)
        - [`shareWithAnybodyForReading`](#shareWithAnybodyForReading)
        - [`shareWithAnybodyForWriting`](#shareWithAnybodyForWriting)
        - [`getSheetURL`](#getSheetURL)
        - [`setSpreadsheetById`](#setSpreadsheetById)
        - [`runPrepared`](#runPrepared)
        - [`prepare_addSheet`](#prepare_addSheet)
        - [`addSheet`](#addSheet)
        - [`toGridRange`](#toGridRange)
        - [`prepare_setDimensionPixelSize`](#prepare_setDimensionPixelSize)
        - [`prepare_setColumnsWidth`](#prepare_setColumnsWidth)
        - [`prepare_setColumnWidth`](#prepare_setColumnWidth)
        - [`prepare_setRowsHeight`](#prepare_setRowsHeight)
        - [`prepare_setRowHeight`](#prepare_setRowHeight)
        - [`prepare_setValues`](#prepare_setValues)
        - [`prepare_mergeCells`](#prepare_mergeCells)
        - [`prepare_setCellStringFormatterormat`](#prepare_setCellStringFormatterormat)
        - [`prepare_setCellStringFormatterormats`](#prepare_setCellStringFormatterormats)
- [Функции](#функции)
    - [`htmlColorToJSON`](#htmlcolortojson)
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

### `ReachSpreadsheet`

**Описание**: Класс для взаимодействия с Google Sheets API.  Позволяет создавать, изменять и получать доступ к данным электронных таблиц.

#### `__init__`

**Описание**: Инициализирует объект `ReachSpreadsheet`.

**Параметры**:
- `debugMode` (bool, optional): Флаг отладки. По умолчанию `False`.

**Возвращает**:
- `None`

**Вызывает исключения**:
- `Exception`: Возникает при ошибках при создании `credentials`.


#### `create`

**Описание**: Создает новую электронную таблицу.

**Параметры**:
- `title` (str): Заголовок электронной таблицы.
- `sheetTitle` (str): Заголовок листа.
- `rows` (int, optional): Количество строк в листе. По умолчанию `1000`.
- `cols` (int, optional): Количество столбцов в листе. По умолчанию `26`.
- `locale` (str, optional): Локаль. По умолчанию `'en-US'`.
- `timeZone` (str, optional): Часовой пояс. По умолчанию `'Etc/GMT'`.


**Возвращает**:
- `dict`: Данные созданной электронной таблицы.

**Вызывает исключения**:
- `SpreadsheetNotSetError`: Если spreadsheetId не задан.


#### `share` и другие методы `share...`

**Описание**: Методы для настройки доступа к электронной таблице.


#### `getSheetURL`

**Описание**: Возвращает URL для доступа к электронной таблице.

**Параметры**:
- `None`


**Возвращает**:
- `str`: URL электронной таблицы.


**Вызывает исключения**:
- `SpreadsheetNotSetError`: Если spreadsheetId не задан.
- `SheetNotSetError`: Если sheetId не задан.


#### `setSpreadsheetById`

**Описание**: Устанавливает текущую электронную таблицу по её идентификатору.

**Параметры**:
- `spreadsheetId` (str): Идентификатор электронной таблицы.

**Возвращает**:
- `None`

**Вызывает исключения**:
- `SpreadsheetNotSetError`: Если spreadsheetId не задан.


#### `runPrepared`

**Описание**: Выполняет подготовленные запросы к электронной таблице.


#### `prepare_addSheet`, `addSheet`, `prepare...`

**Описание**: Методы для подготовки и выполнения операций изменения электронной таблицы.



## Функции

(Описание функций аналогично описанию методов, сосредоточившись на параметрах, возвращаемых значениях и вызываемых исключениях).

```