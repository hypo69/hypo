# Модуль `spreadsheet`

## Обзор

Модуль `spreadsheet` предоставляет класс `SpreadSheet` для работы с Google Sheets API. Он позволяет создавать, управлять и загружать данные из CSV-файлов в Google Sheets.

## Оглавление

1. [Класс `SpreadSheet`](#класс-spreadsheet)
    - [Описание](#описание)
    - [Метод `__init__`](#метод-__init__)
    - [Метод `_create_credentials`](#метод-_create_credentials)
    - [Метод `_authorize_client`](#метод-_authorize_client)
    - [Метод `get_worksheet`](#метод-get_worksheet)
    - [Метод `create_worksheet`](#метод-create_worksheet)
    -  [Метод `copy_worksheet`](#метод-copy_worksheet)
    -  [Метод `upload_data_to_sheet`](#метод-upload_data_to_sheet)
    

## Класс `SpreadSheet`

### Описание

Класс `SpreadSheet` предназначен для работы с Google Sheets API. Он предоставляет методы для аутентификации, создания, открытия и управления таблицами, а также загрузки данных из CSV-файлов.

### Метод `__init__`

**Описание**: Инициализирует экземпляр класса `SpreadSheet` с заданными учетными данными и ID таблицы.

**Параметры**:
- `spreadsheet_id` (str | None): ID таблицы Google Sheets. Если `None`, то будет создана новая таблица.
- `*args`: Дополнительные неименованные аргументы.
- `**kwards`: Дополнительные именованные аргументы.
    

### Метод `_create_credentials`

**Описание**: Создает учетные данные для доступа к Google Sheets API из JSON-файла.

**Возвращает**:
- `ServiceAccountCredentials`: Учетные данные для доступа к Google Sheets.

**Вызывает исключения**:
- `Exception`: В случае ошибки создания учетных данных.

### Метод `_authorize_client`

**Описание**: Авторизует клиента для доступа к Google Sheets API.

**Возвращает**:
- `gspread.Client`: Авторизованный клиент для работы с Google Sheets.

**Вызывает исключения**:
- `Exception`: В случае ошибки авторизации клиента.

### Метод `get_worksheet`

**Описание**: Получает лист (worksheet) по имени.

**Параметры**:
- `worksheet_name` (str | Worksheet): Имя или объект листа.
- `create_if_not_present` (bool, optional): Флаг для создания нового листа, если он не существует. По умолчанию `False`.

**Возвращает**:
- `Worksheet | None`: Объект листа (worksheet) для работы с данными.

### Метод `create_worksheet`

**Описание**: Создает новый лист в Google Sheets.

**Параметры**:
- `title` (str): Название нового листа.
- `dim` (dict, optional): Размеры нового листа (количество строк и столбцов). По умолчанию `{'rows': 100, 'cols': 10}`.

**Возвращает**:
- `Worksheet | None`: Объект нового листа (worksheet).

**Вызывает исключения**:
- `Exception`: В случае ошибки создания нового листа.

### Метод `copy_worksheet`

**Описание**: Копирует лист по имени.

**Параметры**:
- `from_worksheet` (str): Имя копируемого листа.
- `to_worksheet` (str): Имя нового листа.

**Возвращает**:
- `Worksheet`: Объект скопированного листа (worksheet).

### Метод `upload_data_to_sheet`

**Описание**: Загружает данные из CSV-файла в Google Sheets.

**Вызывает исключения**:
- `ValueError`: Если путь к файлу с данными не указан или файл не существует.
- `Exception`: В случае ошибки при загрузке данных в Google Sheets.