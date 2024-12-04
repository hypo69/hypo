# Модуль hypotez/src/goog/spreadsheet/spreadsheet.py

## Обзор

Этот модуль предоставляет минимальную библиотеку для работы с Google Таблицами. Он позволяет создавать новые таблицы, управлять существующими, и загружать данные из CSV-файлов в таблицы Google Таблиц.

## Классы

### `SpreadSheet`

**Описание**: Класс для работы с Google Таблицами.  Обеспечивает базовые методы доступа к API Google Таблиц, создания и управления таблицами, а также загрузки данных из CSV-файла в Google Таблицы.

**Атрибуты**:

- `spreadsheet_id` (str | None): ID таблицы Google Таблиц.  Устанавливает `None`, чтобы создать новую таблицу.
- `spreadsheet_name` (str | None): Имя новой таблицы, если `spreadsheet_id` не указан.
- `spreadsheet` (Spreadsheet): Объект `Spreadsheet` для работы с таблицей.
- `data_file` (Path): Путь к файлу данных CSV.
- `sheet_name` (str): Имя листа в Google Таблицах.
- `credentials` (ServiceAccountCredentials): Объект аутентификации для доступа к API.
- `client` (gspread.Client): Авторизованный клиент для работы с Google Таблицами.
- `worksheet` (Worksheet): Объект `Worksheet` для работы с листом.
- `create_sheet` (bool): Флаг для создания нового листа, если он отсутствует.

**Методы**:

#### `__init__(self, spreadsheet_id: str, *args, **kwards)`

**Описание**: Инициализирует обработчик Google Таблиц с указанными учетными данными и файлом данных.

**Параметры**:

- `spreadsheet_id` (str): ID таблицы Google Таблиц. Укажите `None`, чтобы создать новую таблицу.
- `spreadsheet_name` (str): Имя новой таблицы, если `spreadsheet_id` не указан.
- `sheet_name` (str): Имя листа в Google Таблицах.

**Возвращает**:
- Не имеет возвращаемого значения.

#### `_create_credentials(self)`

**Описание**: Создает учетные данные из JSON-файла. Создает учетные данные для доступа к API Google Таблиц на основе файла ключа.

**Возвращает**:
- `Credentials` для доступа к Google Таблицам.

**Обрабатывает исключения**:
- `Exception`: Возникает при ошибке создания учетных данных.

#### `_authorize_client(self)`

**Описание**: Авторизует клиент для доступа к API Google Таблиц. Создает и авторизует клиента для API Google Таблиц на основе предоставленных учетных данных.

**Возвращает**:
- Авторизованный клиент для работы с Google Таблицами.

**Обрабатывает исключения**:
- `Exception`: Возникает при ошибке авторизации клиента.

#### `get_worksheet(self, worksheet_name: str | Worksheet) -> Worksheet | None`

**Описание**: Получает лист по имени. Если лист с указанным именем не существует и флаг `create_if_not_present` установлен в `True`, создается новый лист.

**Параметры**:

- `worksheet_name` (str | Worksheet): Имя листа в Google Таблицах.
- `create_if_not_present` (bool, необязательно): Флаг для создания нового листа, если он не существует. По умолчанию `False`.

**Возвращает**:
- `Worksheet` для работы с данными.
- `None` если возникла ошибка.

**Обрабатывает исключения**:
- `gspread.exceptions.WorksheetNotFound`: Возникает, если лист не найден.

#### `create_worksheet(self, title: str, dim: dict = {'rows': 100, 'cols': 10}) -> Worksheet | None`

**Описание**: Функция создает новый лист с именем `title` и размерностью `dim`.

**Параметры**:
- `title` (str): Название нового листа.
- `dim` (dict, необязательно): Словарь с размерами листа (`rows`, `cols`). По умолчанию: 100 строк, 10 столбцов.

**Возвращает**:
- `Worksheet`: Созданный лист.
- `None`: Возвращает `None` при ошибке создания листа.

**Обрабатывает исключения**:
- `Exception`: Обработка любых исключений при создании листа.

#### `copy_worksheet(self, from_worksheet: str, to_worksheet: str)`

**Описание**: Копирует лист по имени.

**Параметры**:
- `from_worksheet`: Имя листа для копирования.
- `to_worksheet`: Имя нового листа.


#### `upload_data_to_sheet(self)`

**Описание**: Загружает данные из CSV-файла в Google Таблицы. Загружает данные из CSV-файла, указанного в `self.data_file`, в указанный лист в Google Таблицах.

**Обрабатывает исключения**:
- `ValueError`: Возникает, если путь к файлу данных не задан или файл не существует.
- `Exception`: Возникает при любой другой ошибке во время загрузки данных.


## Функции

(Нет функций в этом модуле, только классы)


## Пример использования

```python
from pathlib import Path
from hypotez.src.goog.spreadsheet.spreadsheet import SpreadSheet

data_file = Path('/mnt/data/google_extracted/your_data_file.csv')  # Замените на реальный путь
sheet_name = 'Sheet1'  # Замените на реальное имя листа

google_sheet_handler = SpreadSheet(
    spreadsheet_id=None,
    sheet_name=sheet_name,
    spreadsheet_name='My New Spreadsheet'
)
google_sheet_handler.upload_data_to_sheet()
```
```