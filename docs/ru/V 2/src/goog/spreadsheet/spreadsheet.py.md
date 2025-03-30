# Модуль `spreadsheet.py`

## Обзор

Модуль `spreadsheet.py` предоставляет класс `SpreadSheet` для работы с Google Sheets. Он включает методы для создания, открытия и управления электронными таблицами, а также для загрузки данных из CSV-файлов.

## Оглавление

1.  [Классы](#классы)
    -   [`SpreadSheet`](#spreadsheet)
2.  [Функции](#функции)
    -   [`_create_credentials`](#_create_credentials)
    -   [`_authorize_client`](#_authorize_client)
    -   [`get_worksheet`](#get_worksheet)
    -   [`create_worksheet`](#create_worksheet)
    -    [`copy_worksheet`](#copy_worksheet)
    -   [`upload_data_to_sheet`](#upload_data_to_sheet)

## Классы

### `SpreadSheet`

**Описание**: Класс для работы с Google Sheets.
Предоставляет базовые методы для доступа к API Google Sheets, создания и управления таблицами, а также загрузки данных из CSV-файла в Google Sheets.

**Методы**:

-   `__init__`: Инициализирует `GoogleSheetHandler` с заданными учетными данными и файлом данных.
-   `_create_credentials`: Создает учетные данные из JSON-файла.
-   `_authorize_client`: Авторизует клиента для доступа к API Google Sheets.
-   `get_worksheet`: Получает рабочий лист по имени.
-   `create_worksheet`: Создает новый рабочий лист с заданными параметрами.
-   `copy_worksheet`: Копирует рабочий лист по имени.
-   `upload_data_to_sheet`: Загружает данные из CSV-файла в Google Sheets.

**Параметры**:
-   `spreadsheet_id` (str): ID таблицы Google Sheets. Укажите `None` для создания новой таблицы.
-   `spreadsheet_name` (str): Имя новой таблицы, если `spreadsheet_id` не указан.
-   `sheet_name` (str): Имя листа в Google Sheets.

## Функции

### `_create_credentials`

**Описание**: Создает учетные данные из JSON-файла.

**Возвращает**:
- `ServiceAccountCredentials`: Учетные данные для доступа к Google Sheets.

**Вызывает исключения**:
-   `Exception`: При ошибке создания учетных данных.

### `_authorize_client`

**Описание**: Авторизует клиента для доступа к API Google Sheets.

**Возвращает**:
-  `gspread.Client`: Авторизованный клиент для работы с Google Sheets.

**Вызывает исключения**:
-   `Exception`: При ошибке авторизации клиента.

### `get_worksheet`

**Описание**: Получает рабочий лист по имени.
Если лист с указанным именем не существует и флаг `create_if_not_present` установлен в `True`, создается новый лист.

**Параметры**:
-   `worksheet_name` (str | Worksheet): Имя листа в Google Sheets.

**Возвращает**:
-   `Worksheet | None`: Рабочий лист для работы с данными.

**Вызывает исключения**:
-  `gspread.exceptions.WorksheetNotFound`: Если рабочий лист не найден и `create_if_not_present` установлен в `False`.

### `create_worksheet`

**Описание**: Создает новый рабочий лист с именем `title` и размерностью `dim`.

**Параметры**:
-   `title` (str): Название нового рабочего листа.
-   `dim` (dict): Размеры нового рабочего листа, по умолчанию `{'rows':100,'cols':10}`.

**Возвращает**:
-   `Worksheet | None`: Созданный рабочий лист.

**Вызывает исключения**:
-   `Exception`: При ошибке создания нового листа.

### `copy_worksheet`

**Описание**: Копирует рабочий лист по имени.

**Параметры**:
-   `from_worksheet` (str): Имя рабочего листа, который нужно скопировать.
-   `to_worksheet` (str): Имя нового рабочего листа.

**Возвращает**:
-   `Worksheet`: Скопированный рабочий лист.

### `upload_data_to_sheet`

**Описание**: Загружает данные из CSV-файла в Google Sheets.

**Вызывает исключения**:
-   `ValueError`: Если путь к файлу данных не установлен или файл не существует.
-    `Exception`: При ошибке загрузки данных в Google Sheets.