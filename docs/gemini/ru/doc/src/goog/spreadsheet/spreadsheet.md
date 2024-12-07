# Модуль hypotez/src/goog/spreadsheet/spreadsheet.py

## Обзор

Этот модуль предоставляет минимальную библиотеку для работы с Google Таблицами. Он позволяет создавать новые таблицы, загружать данные из CSV-файлов и управлять листами.  Модуль использует библиотеку `gspread` для взаимодействия с Google Таблицами и `pandas` для работы с CSV-данными.


## Классы

### `SpreadSheet`

**Описание**: Класс для работы с Google Таблицами. Предоставляет базовые методы для доступа к API Google Таблиц, создания и управления таблицами, а также загрузки данных из CSV-файла в Google Таблицы.

**Атрибуты**:

- `spreadsheet_id`: ID Google Таблицы. Может быть `None`, если необходимо создать новую таблицу.
- `spreadsheet_name`: Название новой таблицы, если `spreadsheet_id` не задан.
- `spreadsheet`: Экземпляр класса `gspread.Spreadsheet`.
- `data_file`: Путь к файлу CSV.
- `sheet_name`: Название листа в Google Таблицах.
- `credentials`: Объект `ServiceAccountCredentials`.
- `client`: Авторизованный клиент `gspread.Client`.
- `worksheet`: Объект `gspread.Worksheet`.
- `create_sheet`: Флаг для создания нового листа.

**Методы**:

#### `__init__(self, spreadsheet_id: str, *args, **kwards)`

**Описание**: Инициализирует обработчик Google Таблиц с указанными учетными данными и файлом данных.

**Параметры**:

- `spreadsheet_id` (str): ID Google Таблицы.  Укажите `None`, чтобы создать новую таблицу.
- `spreadsheet_name` (str): Название новой таблицы, если `spreadsheet_id` не задан.
- `sheet_name` (str): Название листа в Google Таблицах.


#### `_create_credentials(self)`

**Описание**: Создаёт учетные данные из JSON-файла.

**Возвращает**: Объект `ServiceAccountCredentials`.

**Возможные исключения**:  Возможные исключения при работе с файлом или авторизацией,  подробности в логах.


#### `_authorize_client(self)`

**Описание**: Авторизует клиента для доступа к API Google Таблиц.

**Возвращает**: Авторизованный клиент `gspread.Client`.

**Возможные исключения**:  Возможные исключения при работе с учетными данными или авторизацией,  подробности в логах.


#### `get_worksheet(self, worksheet_name: str | Worksheet) -> Worksheet | None`

**Описание**: Возвращает лист по имени. Если лист не существует, и флаг `create_if_not_present` не установлен, то генерируется исключение.  Если лист не найден и `create_if_not_present` установлен, то создаётся новый лист.


**Параметры**:

- `worksheet_name` (str | Worksheet): Название листа.


**Возвращает**: Объект `gspread.Worksheet`.


**Возможные исключения**: `gspread.exceptions.WorksheetNotFound`.


#### `create_worksheet(self, title:str, dim:dict = {\'rows\':100,\'cols\':10}) -> Worksheet | None`

**Описание**: Функция создает новый лист с именем `title` и заданными размерами.

**Параметры**:
- `title`: Имя создаваемого листа.
- `dim`: Словарь с размерами листа (строки и колонки).


**Возвращает**: Объект `gspread.Worksheet` или `None` в случае ошибки.


#### `copy_worksheet(self, from_worksheet: str, to_worksheet: str)`

**Описание**: Копирует лист. (Не реализовано в текущем коде).

#### `upload_data_to_sheet(self)`

**Описание**: Загружает данные из CSV-файла в Google Таблицы.

**Возможные исключения**:
- `ValueError`: Если файл данных не задан или не существует.
- Общие исключения при работе с файлами, библиотеками или API. Подробности в логах.



## Функции

(Нет функций в этом модуле, кроме, возможно, вспомогательных функций внутри класса `SpreadSheet`)


## Пример использования


```python
# Пример использования класса
if __name__ == "__main__":
    from pathlib import Path

    data_file = Path('/mnt/data/google_extracted/your_data_file.csv')  # Замените на фактический файл
    sheet_name = 'Sheet1'  # Замените на фактическое имя листа в Google Таблицах

    # Создание новой таблицы, если spreadsheet_id не указан
    google_sheet_handler = SpreadSheet(
        spreadsheet_id=None,  # Укажите None, чтобы создать новую таблицу
        sheet_name=sheet_name,
        spreadsheet_name='My New Spreadsheet'  # Название новой таблицы, если spreadsheet_id не указан
    )
    google_sheet_handler.upload_data_to_sheet()
```