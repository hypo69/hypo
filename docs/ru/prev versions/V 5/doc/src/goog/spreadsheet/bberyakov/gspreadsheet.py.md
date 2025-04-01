# Модуль для работы с Google Sheets (gspreadsheet.py)

## Обзор

Модуль `gspreadsheet.py` предназначен для работы с Google Sheets. Он предоставляет класс `GSpreadsheet`, который упрощает создание, открытие и управление таблицами Google Sheets. Модуль использует библиотеку `gspread` для взаимодействия с API Google Sheets.

## Подробней

Этот модуль обеспечивает удобный интерфейс для выполнения операций с Google Sheets, таких как создание новых таблиц, открытие существующих по ID или названию, а также получение списка всех таблиц, доступных для текущего аккаунта. Он также включает функциональность для установки прав доступа к таблицам.  Модуль `GSpreadsheet` наследуется от класса `Spreadsheet` и использует файл `goog/onela-hypotez-1aafa5e5d1b5.json` для аутентификации в Google Cloud Platform.

## Классы

### `GSpreadsheet`

**Описание**: Класс для работы с Google Sheets.

**Как работает класс**:
Класс `GSpreadsheet` предоставляет методы для создания, открытия и управления таблицами Google Sheets. Он инициализируется с использованием ID или названия таблицы.  Класс использует файл учетных данных (`goog/onela-hypotez-1aafa5e5d1b5.json`) для аутентификации и авторизации доступа к Google Sheets API.  Метод `__init__` выполняет аутентификацию и получает доступ к указанной таблице, а другие методы предоставляют функциональность для выполнения различных операций с таблицей.

**Методы**:
- `__init__`: Инициализирует экземпляр класса `GSpreadsheet`.
- `get_project_spreadsheets_dict`: Возвращает словарь с информацией о таблицах проекта.
- `get_by_title`: Открывает таблицу по названию.
- `get_by_id`: Открывает таблицу по ID.
- `get_all_spreadsheets_for_current_account`: Возвращает все таблицы, доступные для текущего аккаунта.

**Параметры**:
- `s_id` (str, optional): ID таблицы. По умолчанию `None`.
- `s_title` (str, optional): Название таблицы. По умолчанию `None`.

**Примеры**:

```python
from src.goog.spreadsheet.bberyakov.gspreadsheet import GSpreadsheet

# Инициализация по ID
gs = GSpreadsheet(s_id='1ZcK74BCgWKVr4kODjPmSvjp5IyO0OxhXdbeHKWzLQiM')

# Инициализация по названию
# gs = GSpreadsheet(s_title='My Spreadsheet')
```

## Функции

### `__init__`

```python
def __init__(self, s_id: str = None, s_title: str = None, *args, **kwards):
    """
    Книга google spreadsheet
    """
    ...
```

**Описание**: Инициализирует экземпляр класса `GSpreadsheet`.

**Как работает функция**:
Функция `__init__` инициализирует объект `GSpreadsheet`, подключаясь к Google Sheets API с использованием учетных данных из файла `goog/onela-hypotez-1aafa5e5d1b5.json`. Если указан `s_id`, функция пытается открыть таблицу по ID. Если указан `s_title`, функция пытается открыть таблицу по названию.

**Параметры**:
- `s_id` (str, optional): ID таблицы. По умолчанию `None`.
- `s_title` (str, optional): Название таблицы. По умолчанию `None`.
- `*args`: Произвольные позиционные аргументы.
- `**kwards`: Произвольные именованные аргументы.

**Примеры**:
```python
# Инициализация с указанием ID таблицы
gs = GSpreadsheet(s_id='1ZcK74BCgWKVr4kODjPmSvjp5IyO0OxhXdbeHKWzLQiM')

# Инициализация с указанием названия таблицы
gs = GSpreadsheet(s_title='My Spreadsheet')
```

### `get_project_spreadsheets_dict`

```python
def get_project_spreadsheets_dict(self) -> dict:
    ...
```

**Описание**: Возвращает словарь с информацией о таблицах проекта.

**Как работает функция**:
Функция `get_project_spreadsheets_dict` считывает и возвращает содержимое JSON-файла `goog/spreadsheets.json`, который предположительно содержит словарь с информацией о таблицах, используемых в проекте.

**Возвращает**:
- `dict`: Словарь с информацией о таблицах проекта.

**Примеры**:
```python
gs = GSpreadsheet()
info = gs.get_project_spreadsheets_dict()
print(info)
```

### `get_by_title`

```python
def get_by_title (self, sh_title: str = 'New Spreadsheet'):
    ...
```

**Описание**: Открывает таблицу по названию.

**Как работает функция**:
Функция `get_by_title` пытается открыть Google Sheet с указанным именем. Если таблица с таким именем не найдена, она создает новую таблицу, предоставляет доступ для `d07708766@gmail.com` с правами записи.
    Функция проверяет, существует ли таблица с указанным названием, и если нет, создает её. Затем она предоставляет доступ пользователю `d07708766@gmail.com` с правами на запись.

**Параметры**:
- `sh_title` (str, optional): Название таблицы. По умолчанию `'New Spreadsheet'`.

**Примеры**:
```python
gs = GSpreadsheet()
gs.get_by_title('My New Spreadsheet')
```

### `get_by_id`

```python
def get_by_id (self, sh_id: str) -> Spreadsheet:
    ...
```

**Описание**: Открывает таблицу по ID.

**Как работает функция**:
Функция `get_by_id` открывает Google Sheet с указанным ID.

**Параметры**:
- `sh_id` (str): ID таблицы.

**Возвращает**:
- `Spreadsheet`: Объект `Spreadsheet`, представляющий открытую таблицу.

**Примеры**:
```python
gs = GSpreadsheet()
spreadsheet = gs.get_by_id('1ZcK74BCgWKVr4kODjPmSvjp5IyO0OxhXdbeHKWzLQiM')
print(spreadsheet.title)
```

### `get_all_spreadsheets_for_current_account`

```python
def get_all_spreadsheets_for_current_account (self):
    ...
```

**Описание**: Возвращает все таблицы, доступные для текущего аккаунта.

**Как работает функция**:
Функция `get_all_spreadsheets_for_current_account` возвращает список всех Google Sheets, доступных для текущего аккаунта, используя метод `openall()` из библиотеки `gspread`.

**Возвращает**:
- Список всех таблиц (spreadsheets) аккаунта.

**Примеры**:
```python
gs = GSpreadsheet()
all_spreadsheets = gs.get_all_spreadsheets_for_current_account()
for spreadsheet in all_spreadsheets:
    print(spreadsheet.title)