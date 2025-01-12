# Модуль `gspreadsheet`

## Обзор

Модуль `gspreadsheet.py` предназначен для работы с Google Sheets API с использованием библиотеки `gspread`. Он предоставляет класс `GSpreadsheet`, который наследуется от `Spreadsheet` и позволяет выполнять операции с Google-таблицами, такие как создание, открытие, получение доступа и управление ими.

## Содержание

- [Классы](#классы)
    - [`GSpreadsheet`](#gspreadsheet)
- [Функции](#функции)
    - [`__init__`](#__init__)
    - [`get_project_spreadsheets_dict`](#get_project_spreadsheets_dict)
    - [`get_by_title`](#get_by_title)
    - [`get_by_id`](#get_by_id)
    - [`get_all_spreadsheets_for_current_account`](#get_all_spreadsheets_for_current_account)

## Классы

### `GSpreadsheet`

**Описание**: Класс для работы с Google Sheets, наследуется от `Spreadsheet`.

**Наследует**:
- `Spreadsheet`

**Атрибуты**:
- `gsh` (`Spreadsheet`): Текущая открытая книга Google Sheets.
- `gclient` (`gspread.client`): Клиент Google Sheets API.

#### `__init__`

**Описание**: Инициализирует объект `GSpreadsheet`, устанавливает соединение с Google Sheets API и открывает таблицу по id или по имени.

**Параметры**:
- `s_id` (`str`, optional): Идентификатор Google Sheets. По умолчанию `None`.
- `s_title` (`str`, optional): Название Google Sheets. По умолчанию `None`.
- `*args`:  Произвольные позиционные аргументы.
- `**kwards`: Произвольные ключевые аргументы.

#### `get_project_spreadsheets_dict`

**Описание**: Возвращает словарь с настройками Google Sheets.

**Параметры**:
- `self`: Объект класса.

**Возвращает**:
- `dict`: Словарь с настройками.

#### `get_by_title`

**Описание**: Открывает таблицу по имени, или создает ее если не существует.

**Параметры**:
- `self`: Объект класса.
- `sh_title` (`str`, optional): Название Google Sheets. По умолчанию 'New Spreadsheet'.

#### `get_by_id`

**Описание**: Открывает таблицу по идентификатору.

**Параметры**:
- `self`: Объект класса.
- `sh_id` (`str`): Идентификатор Google Sheets.

**Возвращает**:
- `Spreadsheet`: Объект Google Sheets.

#### `get_all_spreadsheets_for_current_account`

**Описание**: Возвращает все Google Sheets текущего аккаунта.

**Параметры**:
- `self`: Объект класса.

**Возвращает**:
- Список открытых таблиц.

## Функции

### `__init__`

**Описание**: Инициализирует объект `GSpreadsheet`, устанавливает соединение с Google Sheets API и открывает таблицу по id или по имени.

**Параметры**:
- `s_id` (`str`, optional): Идентификатор Google Sheets. По умолчанию `None`.
- `s_title` (`str`, optional): Название Google Sheets. По умолчанию `None`.
- `*args`: Произвольные позиционные аргументы.
- `**kwards`: Произвольные ключевые аргументы.

### `get_project_spreadsheets_dict`

**Описание**: Возвращает словарь с настройками Google Sheets.

**Параметры**:
- `self`: Объект класса.

**Возвращает**:
- `dict`: Словарь с настройками.

### `get_by_title`

**Описание**: Открывает таблицу по имени, или создает ее если не существует.

**Параметры**:
- `self`: Объект класса.
- `sh_title` (`str`, optional): Название Google Sheets. По умолчанию 'New Spreadsheet'.

### `get_by_id`

**Описание**: Открывает таблицу по идентификатору.

**Параметры**:
- `self`: Объект класса.
- `sh_id` (`str`): Идентификатор Google Sheets.

**Возвращает**:
- `Spreadsheet`: Объект Google Sheets.

### `get_all_spreadsheets_for_current_account`

**Описание**: Возвращает все Google Sheets текущего аккаунта.

**Параметры**:
- `self`: Объект класса.

**Возвращает**:
- Список открытых таблиц.