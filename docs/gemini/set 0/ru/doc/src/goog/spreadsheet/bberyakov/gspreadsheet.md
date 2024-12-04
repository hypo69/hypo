# Модуль gspreadsheet.py

## Обзор

Модуль `gspreadsheet.py` предоставляет инструменты для работы с Google Spreadsheets через API gspread. Он позволяет создавать, открывать и управлять электронными таблицами, а также взаимодействовать с ними, используя данные из `global_settingspread`.

## Оглавление

- [Модуль gspreadsheet.py](#модуль-gspreadsheet-py)
- [Обзор](#обзор)
- [Классы](#классы)
    - [Класс `GSpreadsheet`](#класс-gspreadsheet)
- [Функции](#функции)
    - [`get_project_spreadsheets_dict`](#get_project_spreadsheets_dict)
    - [`get_by_title`](#get_by_title)
    - [`get_by_id`](#get_by_id)
    - [`get_all_spreadsheets_for_current_account`](#get_all_spreadsheets_for_current_account)


## Классы

### Класс `GSpreadsheet`

**Описание**: Класс `GSpreadsheet` наследуется от класса `Spreadsheet` и предоставляет методы для работы с Google Spreadsheets. Он хранит информацию о текущей открытой книге (`gsh`) и клиенте Google Sheets (`gclient`).

**Атрибуты**:

- `gsh`: `Spreadsheet`:  Ссылка на текущую открытую книгу.
- `gclient`: `gspread.client`: Объект клиента для работы с Google Spreadsheets.

**Методы**:

- `__init__(self, s_id: str = None, s_title: str = None, *args, **kwards)`:
    **Описание**: Инициализирует объект `GSpreadsheet`. Открывает книгу Google Sheets, используя предоставленный ID или название.
    **Параметры**:
        - `self`: Объект текущего класса.
        - `s_id` (str, необязательно): ID книги.
        - `s_title` (str, необязательно): Название книги.
        - `*args`: Дополнительные аргументы.
        - `**kwards`: Дополнительные ключевые аргументы.

- `get_project_spreadsheets_dict(self) -> dict`:
    **Описание**: Возвращает словарь с данными о проектах Spreadsheets.
    **Параметры**:
        - `self`: Объект текущего класса.
    **Возвращает**:
        - `dict`: Словарь с данными.

- `get_by_title(self, sh_title: str = 'New Spreadsheet')`:
    **Описание**: Открывает или создает книгу Google Sheets с заданным названием.
    **Параметры**:
        - `self`: Объект текущего класса.
        - `sh_title` (str, необязательно): Название книги. По умолчанию 'New Spreadsheet'.
    **Возвращает**:
         -  `Spreadsheet`: Возвращает объект Spreadsheet.
   
- `get_by_id(self, sh_id: str) -> Spreadsheet`:
    **Описание**: Открывает книгу Google Sheets по её ID.
    **Параметры**:
        - `self`: Объект текущего класса.
        - `sh_id` (str): ID книги.
    **Возвращает**:
        - `Spreadsheet`: Объект книги Google Sheets.

- `get_all_spreadsheets_for_current_account(self)`:
    **Описание**: Возвращает список всех книг (spreadsheets) для текущего аккаунта.
    **Параметры**:
        - `self`: Объект текущего класса.
    **Возвращает**:
        - `list`: Список книг.


## Функции

### `get_project_spreadsheets_dict`

**Описание**: Возвращает данные о проектах Spreadsheets, загруженные из файла `goog\\spreadsheets.json`.

**Параметры**:
 - `self`: Объект класса `GSpreadsheet`.

**Возвращает**:
 - `dict`: Словарь с данными о проектах.


### `get_by_title`

**Описание**: Открывает или создает книгу с заданным названием. Если книга с таким названием уже существует, она открывается.

**Параметры**:
 - `self`: Объект класса `GSpreadsheet`.
 - `sh_title`: Название книги.

**Возвращает**:
 - `Spreadsheet`: Объект открытой или созданной книги.



### `get_by_id`

**Описание**: Открывает книгу по предоставленному ID.

**Параметры**:
 - `self`: Объект класса `GSpreadsheet`.
 - `sh_id`: ID книги.

**Возвращает**:
 - `Spreadsheet`: Объект открытой книги.


### `get_all_spreadsheets_for_current_account`

**Описание**: Открывает все книги (spreadsheets) для текущего аккаунта.

**Параметры**:
 - `self`: Объект класса `GSpreadsheet`.

**Возвращает**:
 - `Spreadsheet`: Объект, представляющий список всех книг.