# Модуль gworksheets

## Обзор

Модуль `gworksheets` предоставляет инструменты для работы с Google Sheets. Он позволяет создавать, изменять и управлять рабочими листами (worksheet).  Модуль использует классы из `global_settingspread` и `goog.grender` для взаимодействия с Google Sheets API.

## Классы

### `GWorksheet`

**Описание**: Класс `GWorksheet` наследуется от `Worksheet` и предоставляет методы для работы с рабочими листами в Google Sheets.

**Методы**:

- `__init__`: Инициализирует объект `GWorksheet`.

    **Параметры**:
        - `self`: Экземпляр класса `GWorksheet`.
        - `sh`: Объект `Spreadsheet`, представляющий текущую таблицу.
        - `ws_title` (str = 'new'): Название рабочего листа. Если 'new', создает новый лист.
        - `rows` (опционально): Количество строк в листе.
        - `cols` (опционально): Количество столбцов в листе.
        - `direction` (str = 'rtl'): Направление текста в листе.
        - `wipe_if_exist` (bool = True): Удалять данные с листа, если он уже существует.
        - `*args`: Дополнительные параметры.
        - `**kwards`: Дополнительные параметры.

    **Возвращает**:
        - `None`

- `get`: Создает или открывает существующий рабочий лист.

    **Параметры**:
        - `self`: Экземпляр класса `GWorksheet`.
        - `sh`: Объект `Spreadsheet`, представляющий текущую таблицу.
        - `ws_title` (str = 'new'): Название рабочего листа.
        - `rows` (int = 100): Количество строк.
        - `cols` (int = 100): Количество столбцов.
        - `direction` (str = 'rtl'): Направление текста.
        - `wipe_if_exist` (bool = True): Удалять данные, если лист существует.


    **Возвращает**:
        - `None`
    
    **Описание**: Метод создает новый рабочий лист или открывает существующий. Если лист с `ws_title` уже существует и `wipe_if_exist` = True, то данные на листе очищаются. Если лист не существует, он создается. Устанавливает направление текста на листе.
- `header`: Добавляет заголовок на лист.

    **Параметры**:
        - `self`: Экземпляр класса `GWorksheet`.
        - `world_title` (str): Текст заголовка.
        - `range` (str = 'A1:Z1'): Диапазон ячеек для заголовка.
        - `merge_type` (str('MERGE_ALL') | str('MERGE_COLUMNS') | str('MERGE_ROWS') = 'MERGE_ALL'): Тип объединения ячеек.

    **Возвращает**:
        - `None`

- `category`: Записывает заголовок категории на лист.

    **Параметры**:
        - `self`: Экземпляр класса `GWorksheet`.
        - `ws_category_title`: Название категории.

    **Возвращает**:
        - `None`

- `direction`: Устанавливает направление текста на листе.

    **Параметры**:
        - `self`: Экземпляр класса `GWorksheet`.
        - `direction` (str = 'rtl'): Направление текста ('rtl' или 'ltr').

    **Возвращает**:
        - `None`


## Функции

Нет функций в этом модуле.