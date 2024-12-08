# Документация модуля hypotez/src/goog/spreadsheet/_docs

## Обзор

Этот модуль предоставляет класс-обертку для работы с Google Sheets API v4. Он упрощает взаимодействие с Google Таблицами, предоставляя методы для создания, обновления, заполнения и форматирования таблиц.  Модуль предназначен для автоматизированного управления данными в Google Таблицах из Python-кода.  Он включает методы для настройки параметров таблиц, таких как ширина столбцов, объединение ячеек, форматирование, цвета фона и прочих элементов.

## Классы

### `Spreadsheet`

**Описание**: Класс-обёртка для работы с Google Sheets API v4.  Обеспечивает удобный интерфейс для выполнения различных операций с Google Таблицами.

**Атрибуты**:

- `service`: Экземпляр `apiclient.discovery.build`, необходимый для взаимодействия с API.
- `spreadsheetId`: Идентификатор Google Таблицы.
- `sheetId`: Идентификатор листа.
- `sheetTitle`: Название листа.
- `requests`: Список запросов для `spreadsheets.batchUpdate`.
- `valueRanges`: Список запросов для `spreadsheets.values.batchUpdate`.

**Методы**:

- `prepare_setColumnWidth(col: int, width: int)`: Подготавливает запрос для изменения ширины указанного столбца.
- `prepare_setColumnsWidth(startCol: int, endCol: int, width: int)`: Подготавливает запрос для изменения ширины столбцов в указанном диапазоне.
- `prepare_mergeCells(cellsRange: str)`: Подготавливает запрос для объединения ячеек.
- `prepare_setCellsFormat(cellsRange: str, format: dict, fields: Optional[str] = None)`: Подготавливает запрос для форматирования ячеек.
- `prepare_setCellsFormats(cellsRange: str, formatValues: list, fields: Optional[str] = None)`: Подготавливает запрос для форматирования ячеек (применение разных форматов к разным ячейкам в диапазоне).
- `prepare_setValues(cellsRange: str, values: list, majorDimension: Optional[str] = "ROWS")`: Подготавливает запрос для заполнения ячеек значениями.
- `runPrepared(valueInputOption: Optional[str] = "USER_ENTERED")`: Выполняет все подготовленные запросы.  Возвращает результаты batchUpdate.


## Функции

В этом модуле нет явно определённых функций, но есть класс `Spreadsheet`, предоставляющий все необходимые операции.


```