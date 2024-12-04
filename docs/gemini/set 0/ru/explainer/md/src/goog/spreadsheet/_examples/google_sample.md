# <input code>

```python
## \file hypotez/src/goog/spreadsheet/_examples/google_sample.py
# -*- coding: utf-8 -*-\
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
.. module: src.goog.spreadsheet._examples 
	:platform: Windows, Unix
	:synopsis:

"""
MODE = 'dev'


from __future__ import print_function

import os.path
from pathlib import Path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms'
SAMPLE_RANGE_NAME = 'Class Data!A2:E'

ROOT_DIRECTORY = Path.cwd().absolute()
path = Path(ROOT_DIRECTORY,'google_api','secrets','client_secret_920776813054-crpf1rcav3uui51kq9q1lis64glkpatj.apps.googleusercontent.com.json')
def main():
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists(path):
        creds = Credentials.from_authorized_user_file(path, SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        service = build('sheets', 'v4', credentials=creds)

        # Call the Sheets API
        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                    range=SAMPLE_RANGE_NAME).execute()
        values = result.get('values', [])

        if not values:
            print('No data found.')
            return

        print('Name, Major:')
        for row in values:
            # Print columns A and E, which correspond to indices 0 and 4.
            print('%s, %s' % (row[0], row[4]))
    except HttpError as err:
        print(err)

if __name__ == '__main__':
    main()
```

# <algorithm>

**Шаг 1:** Импортирование библиотек.

*   `os.path`, `pathlib`: для работы с файловой системой.
*   `google.auth`: для аутентификации Google API.
*   `google_auth_oauthlib`: для работы с токенами авторизации.
*   `googleapiclient`: для взаимодействия с Google Sheets API.

**Шаг 2:** Определение констант.

*   `SCOPES`: список разрешений для доступа к Google Sheets.
*   `SAMPLE_SPREADSHEET_ID`: ID целевого листа Google Sheets.
*   `SAMPLE_RANGE_NAME`: диапазон ячеек для извлечения данных.

**Шаг 3:** Получение учетных данных.

*   Проверяет наличие файла `token.json` с токенами.
*   Если файл существует, то загружает данные из него в `creds`.
*   Если файл не существует или токен устарел, то запускает авторизацию через браузер и сохраняет новые токен в `token.json`.

**Шаг 4:** Обработка API вызовов.

*   Создает объект `service` для взаимодействия с Google Sheets API.
*   Вызывает метод `values().get()` для чтения данных из листа.
*   Проверяет наличие данных в `values`.
*   Выводит заголовки таблицы `Name, Major:`.
*   Выводит данные в указанном формате `Name, Major:`

**Шаг 5:** Обработка ошибок.

*   `try...except`: Блок для обработки ошибок при взаимодействии с API.

**Пример данных:**

Вход: данные из листа Google Sheets.


Выход: вывод в консоль строк `Name, Major:` в формате `Name, Major:`.



# <mermaid>

```mermaid
graph LR
    A[main()] --> B{Проверка существования token.json};
    B -- Да --> C[creds = Credentials.from_authorized_user_file];
    B -- Нет --> D[flow = InstalledAppFlow];
    D --> E[creds = flow.run_local_server];
    E --> F{creds.valid?};
    F -- Да --> G[service = build()];
    F -- Нет --> H[Выход из программы];
    C --> F;
    G --> I[sheet = service.spreadsheets()];
    I --> J[result = sheet.values().get()];
    J --> K{values пуст?};
    K -- Да --> L[print('No data found')];
    K -- Нет --> M[Вывод данных];
    M --> N[Конец программы];
    L --> N;

    subgraph Google API
        J --> O[Google Sheets API];
        O --> J;
    end

    style F fill:#f9f,stroke:#333,stroke-width:2px;
```

# <explanation>

**Импорты:**

*   `os.path`, `pathlib`: для работы с файловой системой.
*   `google.auth`, `google.oauth2`, `google_auth_oauthlib`: для аутентификации и работы с токенами Google API.
*   `googleapiclient`: для работы с Google Sheets API.


**Классы:**

*   `Credentials`: класс для хранения и работы с учетными данными.
*   `InstalledAppFlow`: класс для процесса авторизации приложений.
*   Нет других значимых классов.

**Функции:**

*   `main()`: функция, которая выполняет основной поток программы.
    *   `creds = None`: Инициализация переменной для хранения учетных данных.
    *   `if os.path.exists(path): ...`: Проверка наличия файла `token.json`, загрузка данных из него.
    *   `if not creds or not creds.valid: ...`: Если файл не существует или токен недействителен, то выполняется процедура авторизации.
    *   `service = build('sheets', 'v4', credentials=creds)`: Создание объекта `service` для взаимодействия с Google Sheets API.
    *   `result = sheet.values().get(...)`: Вызов метода для получения данных из Google Sheets.
    *   `values = result.get('values', [])`: Получение данных в формате list.
    *   `if not values: ...`: Проверка на пустоту.
    *   `for row in values: ...`: Цикл для обработки каждой строки данных.
    *   `print('%s, %s' % (row[0], row[4]))`: Вывод столбцов A и E каждой строки.
*   Возможные ошибки обрабатываются в блоке `try...except`.


**Переменные:**

*   `SCOPES`: список разрешений для доступа к Google Sheets.
*   `SAMPLE_SPREADSHEET_ID`: ID целевого листа.
*   `SAMPLE_RANGE_NAME`: диапазон ячеек.
*   `ROOT_DIRECTORY`: Путь к текущей директории.
*   `path`: Путь к файлу с секретами приложения.
*   `creds`: переменная для хранения учетных данных.


**Возможные ошибки и улучшения:**

*   Отсутствие обработки ошибок при работе с файловой системой (например, исключения `FileNotFoundError`).
*   Недостаточно ясное сообщение об ошибке в случае `HttpError`.
*   Не обрабатывается ситуация, когда файл `credentials.json` отсутствует.


**Взаимосвязи с другими частями проекта:**

Код использует библиотеки Google API для взаимодействия с внешним сервисом (Google Sheets).  Для корректной работы необходимо наличие файла `credentials.json` с секретами приложения, и этот файл, вероятно, хранится в определенной структуре проекта.