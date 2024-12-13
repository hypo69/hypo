# Модуль `grender.py`

## Обзор

Модуль `grender.py` предназначен для работы с Google Sheets API, а именно для форматирования и рендеринга таблиц. Он включает в себя классы и функции для создания заголовков, объединения ячеек, установки направления текста и других операций, связанных с визуальным оформлением таблиц в Google Sheets.

## Содержание

- [Классы](#Классы)
    - [`GSRender`](#GSRender)
- [Функции](#Функции)
    - [`__init__`](#__init__)
    - [`render_header`](#render_header)
    - [`merge_range`](#merge_range)
    - [`set_worksheet_direction`](#set_worksheet_direction)
    - [`header`](#header)
    - [`write_category_title`](#write_category_title)
    - [`get_first_empty_row`](#get_first_empty_row)

## Классы

### `GSRender`

**Описание**: Класс `GSRender` предназначен для рендеринга и форматирования таблиц в Google Sheets.

**Методы**:

- [`__init__`](#__init__)
- [`render_header`](#render_header)
- [`merge_range`](#merge_range)
- [`set_worksheet_direction`](#set_worksheet_direction)
- [`header`](#header)
- [`write_category_title`](#write_category_title)
- [`get_first_empty_row`](#get_first_empty_row)

## Функции

### `__init__`

**Описание**: Инициализатор класса `GSRender`.

**Параметры**:
-   `self` :  Экземпляр класса.
-   `*args` : Произвольное количество позиционных аргументов.
-   `**kwards` : Произвольное количество именованных аргументов.

**Возвращает**:
-   `None`

### `render_header`

**Описание**: Рисует заголовок таблицы в первой строке.

**Параметры**:
- `self` : Экземпляр класса.
- `ws` (Worksheet): Таблица в книге.
- `world_title` (str): Заголовок гугл таблицы.
- `range` (str, optional): Диапазон ячеек. По умолчанию `'A1:Z1'`.
- `merge_type` (str, optional): Тип объединения ячеек. Возможные значения: `'MERGE_ALL'`, `'MERGE_COLUMNS'`, `'MERGE_ROWS'`. По умолчанию `'MERGE_ALL'`.

**Возвращает**:
- `None`

### `merge_range`

**Описание**: Объединяет ячейки в указанном диапазоне.

**Параметры**:
-   `self` : Экземпляр класса.
-   `ws` (Worksheet): Таблица (worksheet).
-   `range` (str): Диапазон ячеек для объединения.
-   `merge_type` (str, optional): Тип объединения ячеек. Возможные значения: `'MERGE_ALL'`, `'MERGE_COLUMNS'`, `'MERGE_ROWS'`. По умолчанию `'MERGE_ALL'`.

**Возвращает**:
- `None`

### `set_worksheet_direction`

**Описание**: Устанавливает направление текста в таблице.

**Параметры**:
- `self` : Экземпляр класса.
- `sh` (Spreadsheet):  Экземпляр таблицы.
- `ws` (Worksheet): Таблица (worksheet).
- `direction` (str, optional): Направление текста (`'ltr'` - слева направо, `'rtl'` - справа налево). По умолчанию `'rtl'`.

**Возвращает**:
- `None`

### `header`

**Описание**: Функция для добавления заголовка таблицы.

**Параметры**:
- `self` : Экземпляр класса.
- `ws` (Worksheet): Таблица (worksheet).
- `ws_header` (str | list): Заголовок таблицы (строка или список строк).
- `row` (int, optional): Номер строки, в которую нужно вставить заголовок. Если не указан, используется первая пустая строка.

**Возвращает**:
- `None`

### `write_category_title`

**Описание**: Функция для записи заголовка категории в таблицу.

**Параметры**:
- `self` : Экземпляр класса.
- `ws` (Worksheet): Таблица (worksheet).
- `ws_category_title` (str | list): Заголовок категории (строка или список строк).
- `row` (int, optional): Номер строки, в которую нужно вставить заголовок. Если не указан, используется первая пустая строка.

**Возвращает**:
- `None`

### `get_first_empty_row`

**Описание**: Возвращает номер первой пустой строки в таблице.

**Параметры**:
- `self` : Экземпляр класса.
- `ws` (Worksheet): Таблица (worksheet).
- `by_col` (int, optional): Номер колонки для проверки пустых строк. Если не указан, проверка ведется по всей таблице.

**Возвращает**:
- `int`: Номер первой пустой строки.