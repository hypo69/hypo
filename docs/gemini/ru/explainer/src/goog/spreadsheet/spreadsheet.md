```MD
# <input code>

```python
## \file hypotez/src/goog/spreadsheet/spreadsheet.py
# -*- coding: utf-8 -*-\
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
.. module: src.goog.spreadsheet 
	:platform: Windows, Unix
	:synopsis: Minimal library for working with Google Sheets.

```python
# Example usage of the class
if __name__ == "__main__":
    from pathlib import Path

    data_file = Path(\'/mnt/data/google_extracted/your_data_file.csv\')  # Replace with actual data file
    sheet_name = \'Sheet1\'  # Replace with actual sheet name in Google Sheets

    # Create a new Spreadsheet if spreadsheet_id is not specified
    google_sheet_handler = SpreadSheet(
        spreadsheet_id=None,  # Specify None to create a new Spreadsheet
        sheet_name=sheet_name,
        spreadsheet_name=\'My New Spreadsheet\'  # Name of the new Spreadsheet if spreadsheet_id is not specified
    )
    google_sheet_handler.upload_data_to_sheet()
```
"""
MODE = 'dev'


from pathlib import Path
import gspread
from gspread import Spreadsheet, Worksheet
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
from src.logger import logger
from src import gs
from src.utils.printer import pprint


class SpreadSheet:
    """ Class for working with Google Sheets.

    This class provides basic methods for accessing the Google Sheets API, creating and managing spreadsheets,
    and uploading data from a CSV file to Google Sheets.
    """

    # Path to the credentials file for accessing Google Sheets.
    #creds_file = gs.path.root / 'secrets' / 'hypo69-c32c8736ca62.json'

    """ оригинал файла хранится в базе данных вместе с паролями
    @todo организовать копирование файла в прогамно созаданом `tmp`,чтобы не хранить файл в физической директории
    """


    spreadsheet_id: str | None
    spreadsheet_name: str | None
    spreadsheet: Spreadsheet
    data_file: Path
    sheet_name: str
    credentials: ServiceAccountCredentials
    client: gspread.Client
    worksheet: Worksheet
    create_sheet: bool

    def __init__(self, 
                 spreadsheet_id: str, *args, **kwards):  # Name of the sheet in Google Sheets
        """ Initialize GoogleSheetHandler with specified credentials and data file.

        @param spreadsheet_id ID of the Google Sheets spreadsheet. Specify None to create a new Spreadsheet.
        @param spreadsheet_name Name of the new Spreadsheet if spreadsheet_id is not specified.
        @param sheet_name Name of the sheet in Google Sheets.
        """
        self.spreadsheet_id = spreadsheet_id
        self.credentials = self._create_credentials()
        self.client = self._authorize_client()

        try:
            self.spreadsheet = self.client.open_by_key(self.spreadsheet_id)
            #logger.debug(f"Opened existing spreadsheet with ID: {self.spreadsheet_id}")
        except gspread.exceptions.SpreadsheetNotFound:
            logger.error(f"Spreadsheet with ID '{self.spreadsheet_id}' does not exist.")
            raise
   
    # ... (rest of the code)
```

# <algorithm>

**Описание алгоритма**

1. **Инициализация:**
   - Создается экземпляр класса `SpreadSheet`.
   - Передаются `spreadsheet_id`, `sheet_name` и `spreadsheet_name` (используются в методе `__init__`).
   - В `_create_credentials()` загружаются учетные данные из файла `e-cat-346312-137284f4419e.json`.
   - В `_authorize_client()` создается и авторизуется клиент `gspread`.
   - В `__init__` проверяется существование файла с `spreadsheet_id`. Если нет, вызывается исключение.


2. **Получение листа:**
   - Если лист не найден, то метод `get_worksheet` пытается создать новый лист с помощью `create_worksheet`.

3. **Загрузка данных:**
   - В `upload_data_to_sheet` считываются данные из CSV файла (с помощью Pandas).
   - Данные преобразуются в формат, подходящий для записи в Google Таблицы.
   - Данные записываются в лист с помощью метода `update`.

**Пример данных, перемещающихся между функциями:**

- **Вход:** Путь к CSV-файлу (`data_file`) и имя листа (`sheet_name`).
- **`_create_credentials`:** Возвращает объект `ServiceAccountCredentials`.
- **`_authorize_client`:** Возвращает объект `gspread.Client`.
- **`get_worksheet`:** Возвращает объект `Worksheet`.
- **`upload_data_to_sheet`:** Данные из CSV, преобразованные в список списков.
- **Выход:** Данные записаны в лист Google Таблиц.


# <mermaid>

```mermaid
graph LR
    A[SpreadSheet(__init__)] --> B(create credentials);
    B --> C{_authorize_client};
    C --> D[open_by_key];
    D -- success --> E{get_worksheet};
    D -- fail --> F[SpreadsheetNotFound];
    F --> G[Error handling];
    E --> H[upload_data_to_sheet];
    H --> I[read_csv];
    I --> J[format data];
    J --> K[update];
    K --> L[Data uploaded];
    subgraph Credentials
        B --> a[ServiceAccountCredentials.from_json];
        a --> d{Credentials};
    end
    subgraph Client authorization
        C --> b[gspread.authorize];
        b --> c{Authorized client};
    end

    subgraph Data handling
        H --> I;
        I --> J;
        J --> K;
        K --> L;
    end
```

# <explanation>

**Импорты:**

- `pathlib`: Для работы с путями к файлам.
- `gspread`: Библиотека для работы с Google Таблицами.
- `Worksheet`, `Spreadsheet`:  Классы из `gspread` для работы с листами и таблицами Google Таблиц.
- `oauth2client.service_account`: Для аутентификации с помощью учетных данных сервисного аккаунта.
- `pandas`: Библиотека для работы с данными, особенно для удобной обработки CSV.
- `logger`:  (из `src.logger`) Логгер для вывода сообщений об ошибках и отладки.
- `gs`: (из `src`) Вероятно, содержит константы или переменные, относящиеся к Google сервисам, вероятно, пути.
- `printer`: (из `src.utils.printer`) Вероятно, содержит функции для красивого вывода информации.


**Классы:**

- `SpreadSheet`: Главный класс для работы с Google Таблицами.
    - `spreadsheet_id`, `spreadsheet_name`, `sheet_name`: Хранят соответствующую информацию.
    - `credentials`: Учетные данные сервисного аккаунта Google.
    - `client`:  Авторизованный клиент `gspread` для доступа к Google Таблицам.
    - `worksheet`: Лист Google Таблиц.
    - `__init__`: Инициализирует объект, открывает таблицу по `spreadsheet_id`.  Обратите внимание на обработку `SpreadsheetNotFound`.
    - `_create_credentials`: Создаёт объект `ServiceAccountCredentials`.
    - `_authorize_client`: Авторизует `gspread` клиента.
    - `get_worksheet`: Получает лист по имени. Обрабатывает случай, когда листа нет, и создаёт его.
    - `create_worksheet`: Создает новый лист.
    - `upload_data_to_sheet`: Загружает данные из CSV файла в лист.


**Функции:**

- `__init__`: Инициализирует объект `SpreadSheet`, открывает таблицу и авторизует клиента.
- `_create_credentials`: Создаёт объект `ServiceAccountCredentials` для доступа к Google Таблицам.
- `_authorize_client`: Авторизует клиента `gspread` с помощью `credentials`.
- `get_worksheet`: Возвращает лист по имени.
- `create_worksheet`: Создает новый лист.
- `upload_data_to_sheet`: Загружает данные из CSV файла в лист.


**Переменные:**

- `MODE`:  Вероятно, константа, определяющая режим работы (например, `dev` или `prod`).
- `data_file`: Путь к файлу CSV.

**Возможные ошибки и улучшения:**

- **Обработка ошибок:** Хорошая обработка исключений (`try...except`) во многих методах.
- **Подключение к базе данных для хранения ключей:** Используется жестко заданный путь к файлу ключей (`gs.path.secrets / 'e-cat-346312-137284f4419e.json'`). Это небезопасно и требует улучшения. Лучше хранить ключи в защищенном месте и получать их через API.
- **Улучшение обработки отсутствия файла:**  Добавьте проверку на существование файла перед чтением.
- **Вариативность обработки данных:**  В `upload_data_to_sheet` использование `pd.read_csv` и преобразование в список списков - хорошее решение. Но может быть, стоит сделать метод с параметрами для различных типов данных.


**Связь с другими частями проекта:**

- `src.logger`: Используется для записи сообщений об ошибках и отладки.
- `src`: Скорее всего, содержит другие модули, связанные с Google сервисами, например, настройки пути к файлам.
- `utils.printer`:  Служит для отладки или вывода данных.


**Общее:** Код написан качественно, с хорошей обработкой исключений, но требует улучшения в части хранения и использования ключей.  Обработка  `SpreadsheetNotFound`  вызывает исключение, но лучше добавить возможность создания новой таблицы, если ее нет.