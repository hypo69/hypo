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
path = Path(ROOT_DIRECTORY, 'google_api', 'secrets', 'client_secret_920776813054-crpf1rcav3uui51kq9q1lis64glkpatj.apps.googleusercontent.com.json')
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

```mermaid
graph TD
    A[Start] --> B{Check if token.json exists};
    B -- Yes --> C[Load creds from token.json];
    B -- No --> D[Get client_secret];
    C --> E[Check creds validity];
    E -- Valid --> F[Build Sheets API service];
    E -- Invalid --> G{Refresh token?};
    G -- Yes --> H[Refresh creds];
    G -- No --> I[Authenticate user];
    H --> F;
    I --> J[Save creds to token.json];
    J --> F;
    F --> K[Get spreadsheet values];
    K --> L{Check if values are empty?};
    L -- Yes --> M[Print "No data found" and exit];
    L -- No --> N[Print headers];
    N --> O[Iterate through rows];
    O --> P[Print name and major];
    O --> O;
    P --> Q[End of loop];
    Q --> R[End];
    M --> R;
    K -- Error --> S[Handle HttpError];
    S --> R;
```

**Пример данных:**

Предположим, `token.json` содержит валидные данные.  
При запуске программы, данные из `SAMPLE_SPREADSHEET_ID` (например, из Google Таблицы) извлекаются.  
Функция `main()` выводит данные в формате "Name, Major",  выводя  соответствующие значения из столбцов A и E.

# <mermaid>

```mermaid
graph LR
    subgraph Google Sheets API Interaction
        A[main()] --> B(creds = None);
        B -- if os.path.exists(path) --> C[Credentials.from_authorized_user_file];
        C --> D[Check creds validity];
        D -- Valid --> E[build('sheets', 'v4', credentials=creds)];
        D -- Invalid --> F(creds and creds.expired and creds.refresh_token);
        F -- True --> G[creds.refresh(Request())];
        F -- False --> H[InstalledAppFlow.from_client_secrets_file];
        H --> I[flow.run_local_server];
        I --> J[Save creds to token.json];
        G --> E;
        I --> E;
        E --> K[service.spreadsheets().values().get];
        K --> L[result = sheet.values().get()];
        L --> M{if not values:};
        M -- True --> N[print('No data found')];
        M -- False --> O[Iterate through rows];
        O --> P[print('%s, %s' % (row[0], row[4]))];
    end
    subgraph Error Handling
        K --> Q{except HttpError};
        Q --> R[print(err)];
    end
    subgraph Dependencies
        B -.-> google.oauth2.credentials;
        B -.-> google.auth.transport.requests;
        C -.-> google_auth_oauthlib.flow;
        E -.-> googleapiclient.discovery;
        K -.-> googleapiclient.errors;
        K -.-> os.path;
        K -.-> pathlib;
    end
```

# <explanation>

**Импорты:**

- `from __future__ import print_function`:  Указывает на использование `print()`-функции в стиле Python 3, что важно для совместимости с кодом.
- `import os.path`:  Для работы с путями к файлам, в частности, проверка их существования (`os.path.exists`).
- `from pathlib import Path`: Используется класс `Path` для более удобного и переносимого управления путями файлов.
- `from google.auth.transport.requests import Request`:  Для взаимодействия с аутентификацией Google.
- `from google.oauth2.credentials import Credentials`: Класс для работы с учетными данными OAuth2.
- `from google_auth_oauthlib.flow import InstalledAppFlow`: Для управления процессом авторизации Google Apps Script.
- `from googleapiclient.discovery import build`:  Для создания объекта API клиента Google Sheets.
- `from googleapiclient.errors import HttpError`: Для обработки ошибок HTTP-запросов к Google Sheets API.

**Классы:**

- `Credentials`: Представляет учетные данные пользователя для доступа к Google Sheets API.  Атрибуты: `valid`, `expired`, `refresh_token`. Методы: `refresh` для обновления токенов.
- `InstalledAppFlow`:  Управляет процессом авторизации для установки приложения.  Методы:  `run_local_server` для запуска диалога авторизации.


**Функции:**

- `main()`: Основная функция программы. Загружает учетные данные, проверяет их, строит API-клиент Google Sheets, извлекает данные, выводит результат, обрабатывает исключения.
- `Credentials.from_authorized_user_file()`: Загружает учетные данные из файла.
- `creds.refresh()`: Обновляет токены доступа к API Google Sheets.
- `build('sheets', 'v4', credentials=creds)`: Создает объект API-клиента Google Sheets с предоставленными учетными данными.


**Переменные:**

- `SCOPES`: Список разрешений, необходимых для доступа к Google Sheets API.
- `SAMPLE_SPREADSHEET_ID`: ID таблицы в Google Sheets.
- `SAMPLE_RANGE_NAME`: Диапазон ячеек для извлечения.
- `ROOT_DIRECTORY`: Абсолютный путь к корневому каталогу текущего проекта.
- `path`: Путь к файлу `client_secret.json`.
- `creds`: Объект `Credentials`, хранящий учетные данные пользователя.


**Возможные ошибки и улучшения:**

- **Обработка ошибок**: Код хорошо обрабатывает `HttpError`. Можно добавить более подробную обработку других возможных ошибок (например, проблемы с файлом `token.json`).
- **Улучшение читаемости**: Можно добавить комментарии к ключевым строкам кода, объясняя их назначение.
- **Работа с тайм-аутами**: При работе с API желательно добавить обработку тайм-аутов, чтобы программа не зависала при долгом ответе от сервера Google Sheets.


**Связь с другими частями проекта:**

Код зависит от наличия файла `credentials.json`, содержащего секретные ключи для доступа к API Google Sheets.  Также, он использует другие библиотеки для работы с Google API, что подразумевает наличие необходимых зависимостей.  `ROOT_DIRECTORY`, `path` и `client_secret_920776813054-...json` предполагают определённую структуру проекта `hypotez` для хранения конфигурационных файлов.