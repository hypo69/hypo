# Модуль hypotez/src/goog/spreadsheet/spreadsheet.py

## Обзор

Этот модуль предоставляет минимальную библиотеку для работы с Google Таблицами.  Он позволяет создавать новые таблицы, авторизовываться с использованием учетных данных сервисного аккаунта, загружать данные из CSV-файлов в Google Таблицы, и работать с листами.

## Классы

### `SpreadSheet`

**Описание**: Класс для работы с Google Таблицами.  Предоставляет базовые методы для доступа к API Google Таблиц, создания и управления таблицами, а также загрузки данных из CSV-файла в Google Таблицы.

**Атрибуты**:

- `spreadsheet_id`: ID Google Таблицы (строка или None). `None` для создания новой таблицы.
- `spreadsheet_name`: Имя новой таблицы, если `spreadsheet_id` равен `None`.
- `spreadsheet`: Объект `gspread.Spreadsheet`.
- `data_file`: Путь к файлу CSV (объект `pathlib.Path`).
- `sheet_name`: Имя листа в Google Таблицах (строка).
- `credentials`: Объект `oauth2client.service_account.ServiceAccountCredentials`.
- `client`: Объект `gspread.Client`.
- `worksheet`: Объект `gspread.Worksheet`.
- `create_sheet`: Флаг (булево значение), указывающий, нужно ли создавать лист, если он не существует.


**Методы**:

#### `__init__(self, spreadsheet_id: str, *args, **kwards)`

**Описание**: Инициализирует объект `SpreadSheet` с заданными учетными данными и файлом данных.

**Параметры**:

- `spreadsheet_id` (строка или None): ID Google Таблицы. Укажите `None`, чтобы создать новую таблицу.
- `spreadsheet_name` (строка): Имя новой таблицы, если `spreadsheet_id` равен `None`.
- `sheet_name` (строка): Имя листа в Google Таблицах.


**Вызывает исключения**:

- `gspread.exceptions.SpreadsheetNotFound`: Если таблица с указанным `spreadsheet_id` не найдена.



#### `_create_credentials(self)`

**Описание**: Создает учетные данные из файла JSON.

**Возвращает**:

- `oauth2client.service_account.ServiceAccountCredentials`: Учетные данные для доступа к Google Таблицам.

**Вызывает исключения**:

- Любые исключения, возникающие при работе с файлом ключей.


#### `_authorize_client(self)`

**Описание**: Авторизует клиента для доступа к Google Таблицам.

**Возвращает**:

- `gspread.Client`: Авторизованный клиент для работы с Google Таблицами.

**Вызывает исключения**:

- Любые исключения, возникающие при авторизации.


#### `get_worksheet(self, worksheet_name: str | Worksheet) -> Worksheet | None`

**Описание**: Возвращает лист по имени. Если лист не существует, создаёт новый.

**Параметры**:

- `worksheet_name` (строка или объект Worksheet): Имя листа.

**Возвращает**:

- `gspread.Worksheet` : Лист в Google Таблицах.
- `None` : Если возникла ошибка.



#### `create_worksheet(self, title: str, dim: dict = {'rows': 100, 'cols': 10}) -> Worksheet | None`

**Описание**: Создает новый лист в таблице с заданным именем и размерами.

**Параметры**:
- `title` (строка): Имя листа.
- `dim` (словарь): Словарь с количеством строк и столбцов (по умолчанию 100 строк и 10 столбцов).


**Возвращает**:
- `gspread.Worksheet`: Созданный лист.
- `None` : Если произошла ошибка.

#### `copy_worksheet(self, from_worksheet: str, to_worksheet: str)`

**Описание**: Копирует лист из одной таблицы в другую.

**Параметры**:

- `from_worksheet` (строка): Имя исходного листа.
- `to_worksheet` (строка): Имя целевого листа.



#### `upload_data_to_sheet(self)`

**Описание**: Загружает данные из CSV-файла в Google Таблицы.

**Вызывает исключения**:

- `ValueError`: Если путь к файлу данных не установлен или файл не существует.
- Любые исключения, возникающие при работе с файлом или API Google Таблиц.


## Функции

(Здесь могут быть функции, если они есть в файле)


## Пример использования

```python
# Пример использования класса
if __name__ == "__main__":
    from pathlib import Path

    data_file = Path('/mnt/data/google_extracted/your_data_file.csv')  # Замените на ваш файл
    sheet_name = 'Sheet1'  # Замените на имя листа в Google Таблицах

    # Создание новой таблицы
    google_sheet_handler = SpreadSheet(
        spreadsheet_id=None,
        sheet_name=sheet_name,
        spreadsheet_name='Моя новая таблица'
    )
    google_sheet_handler.upload_data_to_sheet()
```