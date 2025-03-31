# src.goog.spreadsheet.bberyakov.grender

## Обзор

Модуль `src.goog.spreadsheet.bberyakov.grender` предназначен для рендеринга (отображения и стилизации) данных в Google Sheets. Он предоставляет функциональность для форматирования заголовков, объединения ячеек и установки направления текста на листе.

## Подробней

Этот модуль является частью проекта `hypotez` и используется для улучшения представления данных, хранящихся в Google Sheets. Он предоставляет классы и методы для стилизации таблиц, что делает информацию более читаемой и организованной. Модуль включает в себя методы для настройки внешнего вида ячеек, такие как цвет фона, выравнивание текста, а также для объединения ячеек и задания направления текста.

## Классы

### `GSRender`

**Описание**: Класс `GSRender` предназначен для отрисовки таблиц в Google Sheets. Он содержит методы для стилизации заголовков, объединения ячеек и установки направления текста.

**Как работает класс**:
Класс `GSRender` инициализируется без параметров, но предназначен для управления внешним видом таблиц в Google Sheets. Он предоставляет методы для форматирования и стилизации данных, включая установку заголовков, объединение ячеек и изменение направления текста.

**Методы**:
- `__init__(self, *args, **kwards)`: Инициализирует экземпляр класса `GSRender`.
- `render_header(self, ws: Worksheet, world_title: str, range: str = 'A1:Z1', merge_type: str('MERGE_ALL') | str('MERGE_COLUMNS') | str('MERGE_ROWS') = 'MERGE_ALL')`: Рисует заголовок таблицы в первой строке.
- `merge_range(self, ws: Worksheet, range: str, merge_type: str('MERGE_ALL') | str('MERGE_COLUMNS') | str('MERGE_ROWS') = 'MERGE_ALL')`: Объединяет ячейки в указанном диапазоне.
- `set_worksheet_direction(self, sh: Spreadsheet, ws: Worksheet, direction: str ('ltr') | str ('rtl') = 'rtl')`: Устанавливает направление текста на листе (слева направо или справа налево).
- `header(self, ws: Worksheet, ws_header: str | list, row: int = None)`: Добавляет заголовок к таблице.
- `write_category_title(self, ws: Worksheet, ws_category_title: str | list, row: int = None)`: Записывает заголовок категории в таблицу.
- `get_first_empty_row(self, ws: Worksheet, by_col: int = None)`: Возвращает номер первой пустой строки в указанном листе.

#### `__init__`
```python
def __init__ (self, *args, **kwards) -> None:
    """
    Args:
        *args: Произвольные позиционные аргументы.
        **kwards: Произвольные именованные аргументы.

    Returns:
        None: Функция ничего не возвращает.

    """
```
**Описание**: Инициализирует экземпляр класса `GSRender`.

**Как работает функция**:
Конструктор класса `GSRender`, который в данный момент не выполняет никаких действий, кроме принятия произвольных аргументов.

**Параметры**:
- `*args`: Произвольные позиционные аргументы.
- `**kwards`: Произвольные именованные аргументы.

**Возвращает**:
- `None`: Функция ничего не возвращает.

#### `render_header`
```python
def render_header (self, ws: Worksheet, world_title: str, range: str = 'A1:Z1', merge_type: str('MERGE_ALL') | str('MERGE_COLUMNS') | str('MERGE_ROWS') = 'MERGE_ALL' ) -> None:
    """
    Args:
        ws (Worksheet): Таблица в книге.
        world_title (str): Заголовок гугл таблицы.
        range (str): Диапазон ячеек. По умолчанию 'A1:Z1'.
        merge_type (str): Тип объединения ячеек ('MERGE_ALL', 'MERGE_COLUMNS', 'MERGE_ROWS'). По умолчанию 'MERGE_ALL'.

    Returns:
        None: Функция ничего не возвращает.

    """
```
**Описание**: Рисует заголовок таблицы в первой строке.

**Как работает функция**:
Метод `render_header` устанавливает стили для заголовка таблицы в Google Sheets. Он принимает объект `Worksheet`, заголовок таблицы (`world_title`), диапазон ячеек (`range`) и тип объединения ячеек (`merge_type`). Метод задает цвет фона, выравнивание текста, направление текста и стиль текста (жирный, размер шрифта, цвет) для указанного диапазона ячеек. Затем он применяет форматирование к ячейкам и объединяет их в соответствии с указанным типом.

**Параметры**:
- `ws` (Worksheet): Таблица в книге.
- `world_title` (str): Заголовок гугл таблицы.
- `range` (str): Диапазон ячеек. По умолчанию `'A1:Z1'`.
- `merge_type` (str): Тип объединения ячеек (`'MERGE_ALL'`, `'MERGE_COLUMNS'`, `'MERGE_ROWS'`). По умолчанию `'MERGE_ALL'`.

**Возвращает**:
- `None`: Функция ничего не возвращает.

#### `merge_range`
```python
def merge_range (self, ws: Worksheet, range: str, merge_type: str('MERGE_ALL') | str('MERGE_COLUMNS') | str('MERGE_ROWS') =  'MERGE_ALL') -> None:
    """
    Args:
        ws (Worksheet): Таблица (worksheet).
        range (str): Диапазон ячеек для объединения.
        merge_type (str): Тип объединения ('MERGE_ALL', 'MERGE_COLUMNS', 'MERGE_ROWS'). По умолчанию 'MERGE_ALL'.

    Returns:
        None: Функция ничего не возвращает.

    """
```
**Описание**: Объединяет ячейки в указанном диапазоне.

**Как работает функция**:
Метод `merge_range` объединяет ячейки в Google Sheets. Он принимает объект `Worksheet`, диапазон ячеек (`range`) и тип объединения (`merge_type`).

**Параметры**:
- `ws` (Worksheet): Таблица (worksheet).
- `range` (str): Диапазон ячеек для объединения.
- `merge_type` (str): Тип объединения (`'MERGE_ALL'`, `'MERGE_COLUMNS'`, `'MERGE_ROWS'`). По умолчанию `'MERGE_ALL'`.

**Возвращает**:
- `None`: Функция ничего не возвращает.

#### `set_worksheet_direction`
```python
def set_worksheet_direction (self, sh: Spreadsheet, ws: Worksheet, direction: str ('ltr') | str ('rtl') = 'rtl' ):
    """
    Args:
        sh (Spreadsheet): Объект Spreadsheet.
        ws (Worksheet): Объект Worksheet.
        direction (str): Направление текста ('ltr' - слева направо, 'rtl' - справа налево). По умолчанию 'rtl'.

    """
```
**Описание**: Устанавливает направление текста на листе (слева направо или справа налево).

**Как работает функция**:
Метод `set_worksheet_direction` устанавливает направление текста на листе Google Sheets. Он принимает объекты `Spreadsheet` и `Worksheet`, а также направление текста (`direction`). Метод формирует запрос на изменение свойств листа и отправляет его в Google Sheets API для обновления направления текста.

**Параметры**:
- `sh` (Spreadsheet): Объект Spreadsheet.
- `ws` (Worksheet): Объект Worksheet.
- `direction` (str): Направление текста (`'ltr'` - слева направо, `'rtl'` - справа налево). По умолчанию `'rtl'`.

#### `header`
```python
def header(self, ws: Worksheet, ws_header: str | list, row: int = None):
    """
    Args:
        ws (Worksheet): Объект Worksheet.
        ws_header (str | list): Заголовок листа (строка или список строк).
        row (int, optional): Номер строки для заголовка. Если не указан, используется первая пустая строка.

    """
```
**Описание**: Добавляет заголовок к таблице.

**Как работает функция**:
Метод `header` добавляет заголовок к таблице в Google Sheets. Он принимает объект `Worksheet`, заголовок (`ws_header`) и номер строки (`row`). Если номер строки не указан, метод определяет первую пустую строку и использует ее для заголовка. Затем он добавляет заголовок в указанную строку и применяет стилизацию с помощью метода `render_header`.

**Параметры**:
- `ws` (Worksheet): Объект Worksheet.
- `ws_header` (str | list): Заголовок листа (строка или список строк).
- `row` (int, optional): Номер строки для заголовка. Если не указан, используется первая пустая строка.

#### `write_category_title`
```python
def write_category_title (self, ws: Worksheet, ws_category_title: str | list, row: int = None):
    """
    Args:
        ws (Worksheet): Объект Worksheet.
        ws_category_title (str | list): Заголовок категории (строка или список строк).
        row (int, optional): Номер строки для заголовка. Если не указан, используется первая пустая строка.

    """
```
**Описание**: Записывает заголовок категории в таблицу.

**Как работает функция**:
Метод `write_category_title` записывает заголовок категории в таблицу Google Sheets. Он принимает объект `Worksheet`, заголовок категории (`ws_category_title`) и номер строки (`row`). Если номер строки не указан, метод определяет первую пустую строку и использует ее для заголовка. Затем он добавляет заголовок категории в указанную строку и объединяет ячейки.

**Параметры**:
- `ws` (Worksheet): Объект Worksheet.
- `ws_category_title` (str | list): Заголовок категории (строка или список строк).
- `row` (int, optional): Номер строки для заголовка. Если не указан, используется первая пустая строка.

#### `get_first_empty_row`
```python
def get_first_empty_row (self, ws: Worksheet, by_col: int = None) -> int:
    """
    Args:
        ws (Worksheet): Таблица (worksheet).
        by_col (int, optional): Номер колонки для проверки. Если не указан, проверяется вся таблица.

    Returns:
        int: Номер первой пустой строки.

    """
```
**Описание**: Возвращает номер первой пустой строки в указанном листе.

**Как работает функция**:
Метод `get_first_empty_row` возвращает номер первой пустой строки в Google Sheets. Он принимает объект `Worksheet` и номер колонки (`by_col`). Если номер колонки указан, метод проверяет только указанную колонку. Иначе, он проверяет всю таблицу.

**Параметры**:
- `ws` (Worksheet): Таблица (worksheet).
- `by_col` (int, optional): Номер колонки для проверки. Если не указан, проверяется вся таблица.

**Возвращает**:
- `int`: Номер первой пустой строки.