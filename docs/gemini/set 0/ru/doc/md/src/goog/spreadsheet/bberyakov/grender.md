# Модуль grender

## Обзор

Данный модуль предоставляет классы и функции для форматирования и рендеринга Google Таблиц.  Он позволяет управлять стилями ячеек, объединять ячейки, устанавливать направление текста и добавлять заголовки и категории.

## Классы

### `GSRender`

**Описание**: Класс `GSRender` отвечает за рендеринг Google Таблиц. Он предоставляет методы для форматирования ячеек, объединения ячеек, установки направления текста и добавления заголовков и категорий.

**Методы**:

- `__init__(self, *args, **kwards)`:
    **Описание**: Конструктор класса.
    **Параметры**:
        - `self`: Экземпляр класса.
        - `*args`: Переменное количество аргументов.
        - `**kwards`: Переменное количество именованных аргументов.
    **Возвращает**:
        - `None`

- `render_header(self, ws: Worksheet, world_title: str, range: str = 'A1:Z1', merge_type: str('MERGE_ALL') | str('MERGE_COLUMNS') | str('MERGE_ROWS') = 'MERGE_ALL') -> None`:
    **Описание**: Рисует заголовок таблицы в первой строке.
    **Параметры**:
        - `self`: Экземпляр класса.
        - `ws` (Worksheet): Объект Worksheet, представляющий таблицу.
        - `world_title` (str): Заголовок Google таблицы.
        - `range` (str, опционально): Диапазон ячеек для форматирования (по умолчанию 'A1:Z1').
        - `merge_type` (str('MERGE_ALL') | str('MERGE_COLUMNS') | str('MERGE_ROWS'), опционально): Тип объединения ячеек (по умолчанию 'MERGE_ALL').
    **Возвращает**:
        - `None`

- `merge_range(self, ws: Worksheet, range: str, merge_type: str('MERGE_ALL') | str('MERGE_COLUMNS') | str('MERGE_ROWS') = 'MERGE_ALL') -> None`:
    **Описание**: Объединяет ячейки в указанном диапазоне.
    **Параметры**:
        - `self`: Экземпляр класса.
        - `ws` (Worksheet): Объект Worksheet, представляющий таблицу.
        - `range` (str): Диапазон ячеек для объединения.
        - `merge_type` (str('MERGE_ALL') | str('MERGE_COLUMNS') | str('MERGE_ROWS'), опционально): Тип объединения (по умолчанию 'MERGE_ALL').
    **Возвращает**:
        - `None`

- `set_worksheet_direction(self, sh: Spreadsheet, ws: Worksheet, direction: str('ltr') | str('rtl') = 'rtl')`:
    **Описание**: Устанавливает направление текста в листе.
    **Параметры**:
        - `self`: Экземпляр класса.
        - `sh` (Spreadsheet): Объект Spreadsheet, представляющий книгу.
        - `ws` (Worksheet): Объект Worksheet, представляющий таблицу.
        - `direction` (str('ltr') | str('rtl'), опционально): Направление текста (по умолчанию 'rtl').
    **Возвращает**:
        - `None`

- `header(self, ws: Worksheet, ws_header: str | list, row: int = None)`:
    **Описание**: Добавляет заголовок в таблицу.
    **Параметры**:
        - `self`: Экземпляр класса.
        - `ws` (Worksheet): Объект Worksheet, представляющий таблицу.
        - `ws_header` (str | list): Заголовок (строка или список значений).
        - `row` (int, опционально): Номер строки для добавления заголовка.
    **Возвращает**:
        - `None`

- `write_category_title(self, ws: Worksheet, ws_category_title: str | list, row: int = None)`:
    **Описание**: Добавляет категорию в таблицу.
    **Параметры**:
        - `self`: Экземпляр класса.
        - `ws` (Worksheet): Объект Worksheet, представляющий таблицу.
        - `ws_category_title` (str | list): Название категории (строка или список значений).
        - `row` (int, опционально): Номер строки для добавления категории.
    **Возвращает**:
        - `None`

- `get_first_empty_row(self, ws: Worksheet, by_col: int = None) -> int`:
    **Описание**: Возвращает номер первой пустой строки в таблице.
    **Параметры**:
        - `self`: Экземпляр класса.
        - `ws` (Worksheet): Объект Worksheet, представляющий таблицу.
        - `by_col` (int, опционально): Номер колонки для поиска пустой строки.
    **Возвращает**:
        - `int`: Номер строки.


## Функции

(Список функций, если они есть, добавьте их сюда)