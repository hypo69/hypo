# Модуль gspreadsheet.py

## Обзор

Модуль `gspreadsheet.py` предоставляет класс `GSpreadsheet` для работы с Google Spreadsheets. Он позволяет получать доступ к существующим таблицам, создавать новые, а также управлять правами доступа.  Модуль использует библиотеку `gspread` для взаимодействия с Google API.

## Оглавление

* [Классы](#классы)
    * [GSpreadsheet](#gspreadsheet)
* [Функции](#функции)
    * [get_project_spreadsheets_dict](#get_project_spreadsheets_dict)
    * [get_by_title](#get_by_title)
    * [get_by_id](#get_by_id)
    * [get_all_spreadsheets_for_current_account](#get_all_spreadsheets_for_current_account)

## Классы

### `GSpreadsheet`

**Описание**:  Класс `GSpreadsheet` наследуется от класса `Spreadsheet` и предоставляет методы для работы с Google Spreadsheets. Он хранит в себе текущую открытую таблицу.

**Атрибуты**:

- `gsh`: `Spreadsheet`: Объект, представляющий текущую открытую таблицу.
- `gclient`: `gspread.client`: Клиент для работы с Google Spreadsheets.

**Методы**:

#### `__init__`

**Описание**: Конструктор класса `GSpreadsheet`.  Инициализирует соединение с Google Sheets API и открывает таблицу по идентификатору или названию.

**Параметры**:

- `s_id` (str, необязательно): Идентификатор таблицы Google Sheets.
- `s_title` (str, необязательно): Название таблицы Google Sheets.
- `*args`: Аргументы.
- `**kwards`: Именованные аргументы.

#### `get_project_spreadsheets_dict`

**Описание**: Возвращает данные о проекте, загруженные из файла `spreadsheets.json`.

**Параметры**:

- `self`: Объект класса `GSpreadsheet`.

**Возвращает**:

- `dict`: Словарь, содержащий данные о проекте.

#### `get_by_title`

**Описание**: Получает доступ к таблице по названию, создаёт её если её нет.

**Параметры**:

- `self`: Объект класса `GSpreadsheet`.
- `sh_title` (str, по умолчанию 'New Spreadsheet'): Название таблицы.


#### `get_by_id`

**Описание**: Получает доступ к таблице по идентификатору.

**Параметры**:

- `self`: Объект класса `GSpreadsheet`.
- `sh_id` (str): Идентификатор таблицы.

**Возвращает**:

- `Spreadsheet`: Объект, представляющий открытую таблицу.


#### `get_all_spreadsheets_for_current_account`

**Описание**: Возвращает все таблицы пользователя.

**Параметры**:

- `self`: Объект класса `GSpreadsheet`.

**Возвращает**:

- Возвращает все открытые таблицы.



## Функции

(Нет функций, кроме методов класса)