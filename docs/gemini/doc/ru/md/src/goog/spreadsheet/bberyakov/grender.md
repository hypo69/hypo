# Модуль grender

## Обзор

Этот модуль предоставляет инструменты для форматирования и рендеринга данных в Google Таблицах. Он включает функции для создания заголовков, обработки стилей ячеек, управления объединением ячеек и добавления данных в таблицу.


## Классы

### `GSRender`

**Описание**: Класс `GSRender` предназначен для рендеринга данных в Google Таблицах. Он содержит методы для форматирования ячеек, объединения ячеек, управления направлением текста и добавления данных.

**Методы**:

- `__init__(*args, **kwards)`:
    **Описание**: Инициализирует экземпляр класса `GSRender`.
    **Параметры**:
        - `*args`: Аргументы.
        - `**kwards`: Ключевые аргументы.
    **Возвращает**:
        - `None`
- `render_header(ws: Worksheet, world_title: str, range: str = 'A1:Z1', merge_type: str('MERGE_ALL') | str('MERGE_COLUMNS') | str('MERGE_ROWS') = 'MERGE_ALL') -> None`:
    **Описание**: Рисует заголовок таблицы в первой строке.
    **Параметры**:
        - `ws` (Worksheet): Объект Worksheet, представляющий таблицу.
        - `world_title` (str): Заголовок Google таблицы.
        - `range` (str, optional): Диапазон ячеек для форматирования. По умолчанию 'A1:Z1'.
        - `merge_type` (str('MERGE_ALL') | str('MERGE_COLUMNS') | str('MERGE_ROWS'), optional): Тип объединения ячеек. По умолчанию 'MERGE_ALL'.
    **Возвращает**:
        - `None`
- `merge_range(ws: Worksheet, range: str, merge_type: str('MERGE_ALL') | str('MERGE_COLUMNS') | str('MERGE_ROWS') = 'MERGE_ALL') -> None`:
    **Описание**: Объединяет ячейки в заданном диапазоне.
    **Параметры**:
        - `ws` (Worksheet): Объект Worksheet, представляющий таблицу.
        - `range` (str): Диапазон ячеек для объединения.
        - `merge_type` (str('MERGE_ALL') | str('MERGE_COLUMNS') | str('MERGE_ROWS'), optional): Тип объединения ячеек. По умолчанию 'MERGE_ALL'.
    **Возвращает**:
        - `None`
- `set_worksheet_direction(sh: Spreadsheet, ws: Worksheet, direction: str('ltr') | str('rtl') = 'rtl')`:
    **Описание**: Устанавливает направление текста в таблице.
    **Параметры**:
        - `sh` (Spreadsheet): Объект Spreadsheet, представляющий книгу.
        - `ws` (Worksheet): Объект Worksheet, представляющий таблицу.
        - `direction` (str('ltr') | str('rtl'), optional): Направление текста. По умолчанию 'rtl'.
    **Возвращает**:
        - `None`
- `header(self, ws: Worksheet, ws_header: str | list, row: int = None)`:
    **Описание**: Добавляет заголовок в таблицу.
    **Параметры**:
        - `ws` (Worksheet): Объект Worksheet, представляющий таблицу.
        - `ws_header` (str | list): Заголовок в виде строки или списка.
        - `row` (int, optional): Номер строки для добавления заголовка.
    **Возвращает**:
        - `None`
- `write_category_title(self, ws: Worksheet, ws_category_title: str | list, row: int = None)`:
    **Описание**: Добавляет заголовок категории в таблицу.
    **Параметры**:
        - `ws` (Worksheet): Объект Worksheet, представляющий таблицу.
        - `ws_category_title` (str | list): Заголовок категории в виде строки или списка.
        - `row` (int, optional): Номер строки для добавления заголовка категории.
    **Возвращает**:
        - `None`
- `get_first_empty_row(self, ws: Worksheet, by_col: int = None) -> int`:
    **Описание**: Возвращает номер первой пустой строки в таблице.
    **Параметры**:
        - `ws` (Worksheet): Объект Worksheet, представляющий таблицу.
        - `by_col` (int, optional): Номер столбца для поиска пустой строки.
    **Возвращает**:
        - `int`: Номер первой пустой строки.


## Функции

(Здесь будут описания функций, если они есть в модуле)


## Импорты

(Этот раздел может быть полезен для понимания зависимостей)

```