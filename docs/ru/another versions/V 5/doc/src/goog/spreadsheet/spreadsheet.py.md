# Модуль для работы с Google Sheets

## Обзор

Модуль `spreadsheet.py` предоставляет класс `SpreadSheet` для взаимодействия с Google Sheets API. Он позволяет создавать, открывать, управлять таблицами и загружать данные из CSV-файлов.

## Подробней

Этот модуль предназначен для упрощения работы с Google Sheets. Он предоставляет удобный интерфейс для выполнения основных операций, таких как создание таблиц, добавление листов, копирование листов и загрузка данных. Класс `SpreadSheet` использует библиотеку `gspread` для взаимодействия с Google Sheets API и требует наличия учетных данных в формате JSON.

## Классы

### `SpreadSheet`

**Описание**: Класс для работы с Google Sheets.

**Как работает класс**:
- Инициализируется с использованием ID существующей таблицы или создает новую таблицу, если ID не указан.
- Использует учетные данные для аутентификации в Google Sheets API.
- Предоставляет методы для создания, открытия, копирования листов и загрузки данных из CSV-файлов.

**Методы**:
- `__init__`: Инициализирует экземпляр класса `SpreadSheet`.
- `_create_credentials`: Создает учетные данные для доступа к Google Sheets API.
- `_authorize_client`: Авторизует клиент для работы с Google Sheets API.
- `get_worksheet`: Получает лист из таблицы по имени.
- `create_worksheet`: Создает новый лист в таблице.
- `copy_worksheet`: Копирует лист в таблице.
- `upload_data_to_sheet`: Загружает данные из CSV-файла в Google Sheets.

**Параметры**:
- `spreadsheet_id` (str | None): ID таблицы Google Sheets. Если указан `None`, создается новая таблица.
- `spreadsheet_name` (str | None): Имя новой таблицы Google Sheets, если `spreadsheet_id` не указан.
- `sheet_name` (str): Имя листа в Google Sheets.
- `credentials` (ServiceAccountCredentials): Учетные данные для доступа к Google Sheets API.
- `client` (gspread.Client): Авторизованный клиент для работы с Google Sheets API.
- `worksheet` (Worksheet): Лист для работы с данными.
- `create_sheet` (bool): Флаг, указывающий, нужно ли создавать новый лист, если он не существует.

**Примеры**
```python
from pathlib import Path

data_file = Path('/mnt/data/google_extracted/your_data_file.csv')  # Замените на актуальный путь к файлу данных
sheet_name = 'Sheet1'  # Замените на актуальное имя листа в Google Sheets

# Создание нового SpreadSheet, если spreadsheet_id не указан
google_sheet_handler = SpreadSheet(
    spreadsheet_id=None,  # Укажите None, чтобы создать новый SpreadSheet
    sheet_name=sheet_name,
    spreadsheet_name='My New Spreadsheet'  # Имя нового SpreadSheet, если spreadsheet_id не указан
)
google_sheet_handler.upload_data_to_sheet()
```

## Функции

### `__init__`

```python
def __init__(self, 
             spreadsheet_id: str, *args, **kwards):
    """ Initialize GoogleSheetHandler with specified credentials and data file.
    
    @param spreadsheet_id ID of the Google Sheets spreadsheet. Specify None to create a new Spreadsheet.
    @param spreadsheet_name Name of the new Spreadsheet if spreadsheet_id is not specified.
    @param sheet_name Name of the sheet in Google Sheets.
    """
```
**Описание**: Инициализирует экземпляр класса `SpreadSheet`.

**Как работает функция**:
- Принимает `spreadsheet_id` для подключения к существующей таблице или создает новую, если `spreadsheet_id` равен `None`.
- Инициализирует учетные данные и авторизует клиент для работы с Google Sheets API.
- Открывает указанную таблицу по ID.

**Параметры**:
- `spreadsheet_id` (str): ID таблицы Google Sheets.

**Вызывает исключения**:
- `gspread.exceptions.SpreadsheetNotFound`: Если таблица с указанным ID не найдена.

**Примеры**:
```python
spreadsheet = SpreadSheet(spreadsheet_id='your_spreadsheet_id')
```

### `_create_credentials`

```python
def _create_credentials(self):
    """ Create credentials from a JSON file.

    Creates credentials for accessing the Google Sheets API based on the key file.
    @return Credentials for accessing Google Sheets.
    """
```

**Описание**: Создает учетные данные для доступа к Google Sheets API из JSON-файла.

**Как работает функция**:
- Определяет путь к файлу учетных данных JSON.
- Устанавливает область доступа к Google Sheets API.
- Создает учетные данные с использованием файла JSON и области доступа.

**Возвращает**:
- `ServiceAccountCredentials`: Учетные данные для доступа к Google Sheets API.

**Вызывает исключения**:
- `Exception`: Если возникает ошибка при создании учетных данных.

**Примеры**:
```python
credentials = self._create_credentials()
```

### `_authorize_client`

```python
def _authorize_client(self):
    """ Authorize client to access the Google Sheets API.

    Creates and authorizes a client for the Google Sheets API based on the provided credentials.
    @return Authorized client for working with Google Sheets.
    """
```

**Описание**: Авторизует клиент для доступа к Google Sheets API.

**Как работает функция**:
- Авторизует клиент `gspread` с использованием предоставленных учетных данных.

**Возвращает**:
- `gspread.Client`: Авторизованный клиент для работы с Google Sheets API.

**Вызывает исключения**:
- `Exception`: Если возникает ошибка при авторизации клиента.

**Примеры**:
```python
client = self._authorize_client()
```

### `get_worksheet`

```python
def get_worksheet(self, worksheet_name: str | Worksheet) -> Worksheet | None:
    """ Get the worksheet by name.

    If the sheet with the specified name does not exist and the `create_if_not_present` flag is set to True, a new sheet is created.

    @param worksheet Name of the sheet in Google Sheets.
    @param create_if_not_present Flag to create a new sheet if it does not exist. If False and the sheet does not exist, an exception is raised.
    @return Worksheet for working with data.
    """
```

**Описание**: Получает лист из таблицы по имени.

**Как работает функция**:
- Пытается получить лист из таблицы по указанному имени.
- Если лист не найден, вызывает метод `create_worksheet` для создания нового листа.

**Параметры**:
- `worksheet_name` (str | Worksheet): Имя листа в Google Sheets.

**Возвращает**:
- `Worksheet | None`: Лист для работы с данными.

**Примеры**:
```python
worksheet = self.get_worksheet(worksheet_name='Sheet1')
```

### `create_worksheet`

```python
def create_worksheet(self, title:str, dim:dict = {'rows':100,'cols':10}) -> Worksheet | None:
    """ функция создает новую страницу с именем `title` и размерностью `dim`"""
```

**Описание**: Создает новый лист в таблице.

**Как работает функция**:
- Добавляет новый лист в таблицу с указанным именем и размерами.

**Параметры**:
- `title` (str): Имя нового листа.
- `dim` (dict): Размеры нового листа (количество строк и столбцов).

**Возвращает**:
- `Worksheet | None`: Новый лист.

**Вызывает исключения**:
- `Exception`: Если возникает ошибка при создании нового листа.

**Примеры**:
```python
worksheet = self.create_worksheet(title='New Sheet', dim={'rows': 100, 'cols': 10})
```

### `copy_worksheet`

```python
def copy_worksheet(self, from_worksheet: str, to_worksheet: str):
    """ Copy worksheet by name."""
    ...
```

**Описание**: Копирует лист в таблице.

**Как работает функция**:
- Копирует лист с именем `from_worksheet` и создает его копию с именем `to_worksheet`.

**Параметры**:
- `from_worksheet` (str): Имя листа, который нужно скопировать.
- `to_worksheet` (str): Имя нового листа (копии).

**Возвращает**:
- `Worksheet`: Новый лист (копия).

**Примеры**:
```python
worksheet = self.copy_worksheet(from_worksheet='Sheet1', to_worksheet='Sheet1 Copy')
```

### `upload_data_to_sheet`

```python
def upload_data_to_sheet(self):
    """ Upload data from a CSV file to Google Sheets.

    Uploads data from the CSV file specified in `self.data_file` to the specified sheet in Google Sheets.
    """
```

**Описание**: Загружает данные из CSV-файла в Google Sheets.

**Как работает функция**:
- Читает данные из CSV-файла, указанного в `self.data_file`.
- Подготавливает данные для записи в Google Sheets.
- Записывает данные в указанный лист Google Sheets.

**Вызывает исключения**:
- `ValueError`: Если путь к файлу данных не указан или файл не существует.
- `Exception`: Если возникает ошибка при загрузке данных в Google Sheets.

**Примеры**:
```python
self.upload_data_to_sheet()