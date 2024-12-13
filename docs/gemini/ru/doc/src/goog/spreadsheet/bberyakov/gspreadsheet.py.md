# Модуль `gspreadsheet`

## Обзор

Модуль `gspreadsheet` предоставляет класс `GSpreadsheet` для работы с Google Sheets API. Он позволяет создавать, открывать и управлять Google-таблицами, а также предоставляет методы для получения данных из них.

## Содержание

- [Классы](#Классы)
  - [`GSpreadsheet`](#GSpreadsheet)
- [Функции](#Функции)
  - [`get_project_spreadsheets_dict`](#get_project_spreadsheets_dict)
  - [`get_by_title`](#get_by_title)
  - [`get_by_id`](#get_by_id)
  - [`get_all_spreadsheets_for_current_account`](#get_all_spreadsheets_for_current_account)

## Классы

### `GSpreadsheet`

**Описание**: Класс для работы с Google Sheets API.

**Наследует**:
- `Spreadsheet`: Базовый класс для работы с таблицами.

**Методы**:
- [`__init__`](#__init__)
- [`get_project_spreadsheets_dict`](#get_project_spreadsheets_dict)
- [`get_by_title`](#get_by_title)
- [`get_by_id`](#get_by_id)
- [`get_all_spreadsheets_for_current_account`](#get_all_spreadsheets_for_current_account)

#### `__init__`

**Описание**: Инициализирует экземпляр класса `GSpreadsheet`.

**Параметры**:
- `s_id` (str, optional): Идентификатор таблицы. По умолчанию `None`.
- `s_title` (str, optional): Название таблицы. По умолчанию `None`.
- `*args`: Произвольные позиционные аргументы.
- `**kwards`: Произвольные именованные аргументы.

#### `gsh`
- **Описание**: Экземпляр класса `Spreadsheet`, представляющий книгу Google Sheets.

#### `gclient`
- **Описание**: Экземпляр клиента gspread для взаимодействия с Google Sheets API.

## Функции

### `get_project_spreadsheets_dict`

**Описание**: Возвращает словарь с настройками таблиц из файла `goog\\spreadsheets.json`.

**Параметры**:
- `self`: Экземпляр класса `GSpreadsheet`.

**Возвращает**:
- `dict`: Словарь с настройками таблиц.

### `get_by_title`

**Описание**: Открывает таблицу по её названию или создает новую, если такой таблицы нет.

**Параметры**:
- `self`: Экземпляр класса `GSpreadsheet`.
- `sh_title` (str, optional): Название таблицы. По умолчанию `New Spreadsheet`.

### `get_by_id`

**Описание**: Открывает таблицу по её идентификатору.

**Параметры**:
- `self`: Экземпляр класса `GSpreadsheet`.
- `sh_id` (str): Идентификатор таблицы.

**Возвращает**:
- `Spreadsheet`: Экземпляр таблицы `Spreadsheet`.

### `get_all_spreadsheets_for_current_account`

**Описание**: Возвращает все таблицы текущего аккаунта.

**Параметры**:
- `self`: Экземпляр класса `GSpreadsheet`.

**Возвращает**:
- `list`: Список всех таблиц.