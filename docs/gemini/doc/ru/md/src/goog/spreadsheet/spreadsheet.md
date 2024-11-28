# Модуль hypotez/src/goog/spreadsheet/spreadsheet.py

## Обзор

Модуль `hypotez/src/goog/spreadsheet/spreadsheet.py` предоставляет минимальную библиотеку для работы с Google Таблицами. Он позволяет создавать, открывать, и загружать данные из CSV файлов в Google Таблицы. Модуль использует библиотеку `gspread` для взаимодействия с Google Sheets API.

## Классы

### `SpreadSheet`

**Описание**: Класс для работы с Google Таблицами. Предоставляет базовые методы для доступа к API Google Таблиц, создания и управления таблицами, а также загрузки данных из CSV файла в Google Таблицы.

**Атрибуты**:

- `spreadsheet_id`: ID Google таблицы. Может быть `None` для создания новой таблицы.
- `spreadsheet_name`: Имя новой таблицы, если `spreadsheet_id` не указан.
- `spreadsheet`: Объект `gspread.Spreadsheet` для работы с таблицей.
- `data_file`: Путь к CSV файлу с данными.
- `sheet_name`: Имя листа в Google Таблицах.
- `credentials`: Объект `oauth2client.service_account.ServiceAccountCredentials` для авторизации.
- `client`: Объект `gspread.Client` для авторизации доступа.
- `worksheet`: Объект `gspread.Worksheet` для работы с листом.
- `create_sheet`: Флаг, определяющий нужно ли создавать лист, если его нет.


**Методы**:

#### `__init__(self, spreadsheet_id: str, *args, **kwards)`

**Описание**: Инициализирует обработчик Google Таблиц с указанными учетными данными и файлом данных.

**Параметры**:

- `spreadsheet_id (str)`: ID Google таблицы. Укажите `None`, чтобы создать новую таблицу.
- `spreadsheet_name (str)`: Имя новой таблицы, если `spreadsheet_id` не указан.
- `sheet_name (str)`: Имя листа в Google Таблицах.


**Вызывает исключения**:

- `gspread.exceptions.SpreadsheetNotFound`: Если таблица с указанным `spreadsheet_id` не найдена.


#### `_create_credentials(self)`

**Описание**: Создает учетные данные из JSON файла.

**Возвращает**:

- `oauth2client.service_account.ServiceAccountCredentials`: Учетные данные для доступа к Google Таблицам.


**Вызывает исключения**:

- `Exception`: Если возникла ошибка при создании учетных данных.


#### `_authorize_client(self)`

**Описание**: Авторизует клиента для доступа к API Google Таблиц.

**Возвращает**:

- `gspread.Client`: Авторизованный клиент для работы с Google Таблицами.


**Вызывает исключения**:

- `Exception`: Если возникла ошибка при авторизации клиента.


#### `get_worksheet(self, worksheet_name: str | Worksheet) -> Worksheet | None`

**Описание**: Получает лист по имени. Если лист не существует, создает его.

**Параметры**:

- `worksheet_name (str | Worksheet)`: Имя листа.

**Возвращает**:

- `gspread.Worksheet`: Объект листа для работы с данными.


**Вызывает исключения**:

- `gspread.exceptions.WorksheetNotFound`: Если лист не найден.

#### `create_worksheet(self, title: str, dim: dict = {'rows': 100, 'cols': 10}) -> Worksheet | None`

**Описание**: Создает новый лист с заданным названием и размерами.

**Параметры**:

- `title (str)`: Название листа.
- `dim (dict)`: Словарь с размерами листа.


**Возвращает**:

- `gspread.Worksheet`: Объект созданного листа.

**Вызывает исключения**:

- `Exception`: Если возникла ошибка при создании листа.



#### `copy_worksheet(self, from_worksheet: str, to_worksheet: str)`

**Описание**: Копирует лист.

**Параметры**:

- `from_worksheet (str)`: Имя исходного листа.
- `to_worksheet (str)`: Имя нового листа.


**Возвращает**:

- `gspread.Worksheet`: Объект скопированного листа.


#### `upload_data_to_sheet(self)`

**Описание**: Загружает данные из CSV файла в Google Таблицы.

**Вызывает исключения**:

- `ValueError`: Если путь к файлу не задан или файл не существует.
- `Exception`: Если возникла ошибка при загрузке данных.


## Функции

(Нет функций в этом модуле, только класс)


## Примеры


```python
# Пример использования класса
if __name__ == "__main__":
    from pathlib import Path

    data_file = Path('/mnt/data/google_extracted/your_data_file.csv')  # Замените на реальный путь
    sheet_name = 'Sheet1'  # Замените на реальное имя листа в Google Таблицах

    # Создайте новую таблицу, если spreadsheet_id не указан
    google_sheet_handler = SpreadSheet(
        spreadsheet_id=None,
        sheet_name=sheet_name,
        spreadsheet_name='My New Spreadsheet'  # Имя новой таблицы
    )
    google_sheet_handler.upload_data_to_sheet()
```