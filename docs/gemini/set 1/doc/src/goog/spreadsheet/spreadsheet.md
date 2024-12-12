# Модуль hypotez/src/goog/spreadsheet/spreadsheet.py

## Обзор

Модуль `hypotez/src/goog/spreadsheet/spreadsheet.py` предоставляет минимальную библиотеку для работы с Google Таблицами.  Он позволяет создавать новые таблицы, авторизовываться с помощью учетных данных сервисного аккаунта, получать доступ к листам, и загружать данные из CSV-файлов.

## Классы

### `SpreadSheet`

**Описание**: Класс `SpreadSheet` предназначен для работы с Google Таблицами.  Он предоставляет методы для доступа к API Google Таблиц, создания и управления таблицами, а также загрузки данных из CSV-файла в Google Таблицы.


**Атрибуты**:

- `spreadsheet_id`: ID таблицы Google Таблиц (строка). `None` для создания новой таблицы.
- `spreadsheet_name`: Название новой таблицы, если `spreadsheet_id` равен `None`.
- `spreadsheet`: Объект `gspread.Spreadsheet`, представляющий таблицу Google Таблиц.
- `data_file`: Путь к CSV-файлу (объект `pathlib.Path`).
- `sheet_name`: Имя листа в Google Таблицах (строка).
- `credentials`: Объект `oauth2client.service_account.ServiceAccountCredentials`, используемые для авторизации.
- `client`: Объект `gspread.Client` для авторизованного доступа к Google Таблицам.
- `worksheet`: Объект `gspread.Worksheet` для работы с конкретным листом.
- `create_sheet`: Флаг, определяющий необходимость создания листа, если он не существует.


**Методы**:

#### `__init__(self, spreadsheet_id: str, *args, **kwards)`

**Описание**: Инициализирует объект `SpreadSheet` с заданными учетными данными и файлом данных.

**Параметры**:

- `spreadsheet_id` (str): ID таблицы Google Таблиц. `None` для создания новой таблицы.
- `spreadsheet_name` (str): Название новой таблицы, если `spreadsheet_id` равен `None`.
- `sheet_name` (str): Название листа в Google Таблицах.

**Возвращает**:
    - None


#### `_create_credentials(self)`

**Описание**: Создает учетные данные для доступа к API Google Таблиц из файла JSON.

**Возвращает**:
    - `oauth2client.service_account.ServiceAccountCredentials`: Учетные данные для доступа к API.

**Возможные исключения**:
- `Exception`: В случае ошибки при создании учетных данных.


#### `_authorize_client(self)`

**Описание**: Авторизует клиента для доступа к API Google Таблиц на основе предоставленных учетных данных.

**Возвращает**:
    - `gspread.Client`: Авторизованный клиент для работы с Google Таблицами.

**Возможные исключения**:
- `Exception`: В случае ошибки авторизации.


#### `get_worksheet(self, worksheet_name: str | Worksheet) -> Worksheet | None`

**Описание**: Получает лист по имени. Если лист не существует, и флаг `create_if_not_present` установлен в `True`, создается новый лист.

**Параметры**:
- `worksheet_name` (str | Worksheet): Имя листа.

**Возвращает**:
    - `gspread.Worksheet`: Объект Worksheet, если лист существует или был создан.
    - `None`: Если лист не найден и `create_if_not_present` равен `False`.


#### `create_worksheet(self, title:str, dim:dict = {\'rows\':100,\'cols\':10}) -> Worksheet | None`

**Описание**: Функция создает новый лист с именем `title` и размерностью `dim`.

**Параметры**:

- `title` (str): Название листа.
- `dim` (dict, опционально): Словарь с параметрами размера листа (rows, cols).


**Возвращает**:
    - `gspread.Worksheet`: Объект Worksheet, если лист был создан.
    - `None`: В случае ошибки.


#### `copy_worksheet(self, from_worksheet: str, to_worksheet: str)`

**Описание**: Копирует лист.


#### `upload_data_to_sheet(self)`

**Описание**: Загружает данные из CSV-файла в Google Таблицы.

**Возможные исключения**:
- `ValueError`: Если путь к файлу не указан или файл не существует.
- `Exception`: В случае ошибки при загрузке данных.



## Функции

Нет функций в данном модуле.