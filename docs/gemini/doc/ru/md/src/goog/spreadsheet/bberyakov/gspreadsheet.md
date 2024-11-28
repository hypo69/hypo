# Модуль gspreadsheet.py

## Обзор

Этот модуль предоставляет инструменты для работы с Google Spreadsheets через API gspread. Он содержит класс `GSpreadsheet`, который наследуется от класса `Spreadsheet` и реализует методы для работы с книгами (spreadsheets) Google Sheets, включая создание, открытие и получение списка всех книг аккаунта.

## Оглавление

- [Модуль gspreadsheet.py](#модуль-gspreadsheetpy)
- [Обзор](#обзор)
- [Классы](#классы)
    - [Класс `GSpreadsheet`](#класс-gspreadsheet)
        - [Метод `__init__`](#метод-init)
        - [Метод `get_project_spreadsheets_dict`](#метод-get_project_spreadsheets_dict)
        - [Метод `get_by_title`](#метод-get_by_title)
        - [Метод `get_by_id`](#метод-get_by_id)
        - [Метод `get_all_spreadsheets_for_current_account`](#метод-get_all_spreadsheets_for_current_account)


## Классы

### Класс `GSpreadsheet`

**Описание**: Класс `GSpreadsheet` представляет собой объект для работы с книгами Google Sheets. Он наследуется от класса `Spreadsheet`.

**Методы**:

#### Метод `__init__`

**Описание**: Конструктор класса `GSpreadsheet`. Инициализирует объект для работы с Google Sheets, используя предоставленный `s_id` или `s_title`.

**Параметры**:
- `self`: Экземпляр класса `GSpreadsheet`.
- `s_id` (str, необязательно): Идентификатор книги.
- `s_title` (str, необязательно): Название книги. Если указаны оба `s_id` и `s_title`, используется `s_id`.
- `*args`: Дополнительные аргументы.
- `**kwards`: Дополнительные ключевые аргументы.

**Возвращает**:
- None

#### Метод `get_project_spreadsheets_dict`

**Описание**: Возвращает словарь, загруженный из файла `goog\\spreadsheets.json`.

**Параметры**:
- `self`: Экземпляр класса `GSpreadsheet`.

**Возвращает**:
- `dict`: Словарь, загруженный из файла.

#### Метод `get_by_title`

**Описание**: Создает или открывает книгу Google Sheets по заданному названию.

**Параметры**:
- `self`: Экземпляр класса `GSpreadsheet`.
- `sh_title` (str, по умолчанию 'New Spreadsheet'): Название книги.

**Возвращает**:
- None


#### Метод `get_by_id`

**Описание**: Открывает книгу Google Sheets по заданному идентификатору.

**Параметры**:
- `self`: Экземпляр класса `GSpreadsheet`.
- `sh_id` (str): Идентификатор книги.

**Возвращает**:
- `Spreadsheet`: Объект `Spreadsheet`, представляющий открытую книгу.


#### Метод `get_all_spreadsheets_for_current_account`

**Описание**: Открывает все книги (spreadsheets) текущего аккаунта.

**Параметры**:
- `self`: Экземпляр класса `GSpreadsheet`.

**Возвращает**:
- None