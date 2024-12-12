# Документация модуля hypotez/src/goog/spreadsheet/_docs

## Обзор

Модуль `hypotez/src/goog/spreadsheet/_docs` предоставляет инструменты для работы с Google Sheets API v4.  Он содержит класс-обёртку `Spreadsheet`, позволяющий упрощённо выполнять операции по созданию, обновлению и заполнению данных в Google-таблицах.  Документация описывает процесс работы с API, включая создание сервисного аккаунта, установку необходимых библиотек, а также методы работы с таблицами, такими как: загрузка, сохранение данных, изменение форматирования (ширина столбцов, объединение ячеек, формат отображения, цвет фона, границы).

## Содержание

* [Обзор](#обзор)
* [Класс `Spreadsheet`](#класс-spreadsheet)
    * [`__init__`](#__init__)
    * [`prepare_setColumnWidth`](#prepare_setcolumnwidth)
    * [`prepare_setColumnsWidth`](#prepare_setcolumnswidth)
    * [`prepare_setValues`](#prepare_setvalues)
    * [`runPrepared`](#runprepared)
    * [`toGridRange`](#togridrange)
    * [`prepare_mergeCells`](#prepare_mergecells)
    * [`prepare_setCellsFormat`](#prepare_setcellsformat)
    * [`prepare_setCellsFormats`](#prepare_setcellsformats)
* [Пример использования](#пример-использования)

## Класс `Spreadsheet`

### `__init__`

```python
def __init__(self, service: apiclient.discovery.build, spreadsheet_id: str, sheet_id: int = 0, sheet_title: str = None) -> None:
    """
    Инициализирует объект Spreadsheet.

    Args:
        service (apiclient.discovery.build): Объект, предоставляющий доступ к Google Sheets API.
        spreadsheet_id (str): Идентификатор Google таблицы.
        sheet_id (int, optional): Идентификатор листа. По умолчанию 0 (первый лист).
        sheet_title (str, optional): Название листа. Если не указано, используется sheet_id.
    """
```

### `prepare_setColumnWidth`

```python
def prepare_setColumnWidth(self, col: int, width: int) -> None:
    """
    Добавляет запрос для установки ширины столбца.

    Args:
        col (int): Номер столбца (от 0).
        width (int): Ширина столбца в пикселях.
    """
```

### `prepare_setColumnsWidth`

```python
def prepare_setColumnsWidth(self, startCol: int, endCol: int, width: int) -> None:
    """
    Добавляет запрос для установки ширины нескольких столбцов.

    Args:
        startCol (int): Номер начального столбца (от 0).
        endCol (int): Номер конечного столбца (от 0).
        width (int): Ширина столбцов в пикселях.
    """
```

### `prepare_setValues`

```python
def prepare_setValues(self, cellsRange: str, values: list[list], majorDimension: str = "ROWS") -> None:
    """
    Добавляет запрос для заполнения ячеек.

    Args:
        cellsRange (str): Диапазон ячеек в формате A1 (например, "A1:B2").
        values (list[list]): Данные для заполнения. Внешний список - это строки, внутренние списки - значения в строках.
        majorDimension (str, optional): Направление заполнения ("ROWS" или "COLUMNS"). По умолчанию "ROWS".
    """
```

### `runPrepared`

```python
def runPrepared(self, valueInputOption: str = "USER_ENTERED") -> tuple:
    """
    Выполняет все подготовленные запросы.

    Args:
        valueInputOption (str, optional): Режим ввода данных. По умолчанию "USER_ENTERED".

    Returns:
        tuple: Кортеж из результатов запросов spreadsheets.batchUpdate и spreadsheets.values.batchUpdate.
    """
```

### `toGridRange`

```python
def toGridRange(self, cell_range: str) -> dict:
  """
  Преобразует диапазон ячеек в формате A1 в формат GridRange.

  Args:
      cell_range (str): Диапазон ячеек в формате A1 (например, "A1:B2").

  Returns:
      dict: Словарь с параметрами GridRange.
  """
```

### `prepare_mergeCells`

```python
def prepare_mergeCells(self, range: str) -> None:
    """
    Добавляет запрос для объединения ячеек.

    Args:
      range (str): Диапазон ячеек в формате A1 (например, "A1:E1").
    """
```

### `prepare_setCellsFormat`

```python
def prepare_setCellsFormat(self, range: str, format: dict, fields: str = "userEnteredFormat") -> None:
    """
    Добавляет запрос для форматирования ячеек.

    Args:
        range (str): Диапазон ячеек в формате A1 (например, "A1:B2").
        format (dict): Словарь с параметрами форматирования.
        fields (str, optional): Список полей для обновления. По умолчанию "userEnteredFormat".
    """
```

### `prepare_setCellsFormats`

```python
def prepare_setCellsFormats(self, range: str, formats: list[list[dict]], fields: str = "userEnteredFormat") -> None:
    """
    Добавляет запрос для форматирования ячеек.

    Args:
        range (str): Диапазон ячеек в формате A1 (например, "A1:B2").
        formats (list[list[dict]]): Список списков словарей с параметрами форматирования.
        fields (str, optional): Список полей для обновления. По умолчанию "userEnteredFormat".
    """
```


## Пример использования

```python
# ... (Импорты и инициализация service)

ss = Spreadsheet(service, 'spreadsheet_id')
ss.prepare_setColumnWidth(0, 317)
ss.prepare_setValues("A1:B2", [["Value 1", "Value 2"], ["Value 3", "Value 4"]])
ss.runPrepared()

# ... (Дополнительно: merge cells, format cells, etc.)
```

**Примечание:**  Данный пример упрощён. Полный пример, с полной реализацией класса `Spreadsheet`, доступен по ссылке в документации.