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

1. **Инициализация:** Определяет константы `SCOPES`, `SAMPLE_SPREADSHEET_ID`, `SAMPLE_RANGE_NAME`, `ROOT_DIRECTORY` и путь к файлу `client_secret`.
2. **Проверка аутентификации:** Проверяет наличие файла `token.json` с токенами доступа. Если файл существует, то загружает данные из него. В противном случае запускает локальный сервер для авторизации пользователя, сохраняет полученные токены в `token.json`.
3. **Вызов API:** Используя полученные учетные данные, строит объект `service` для работы с Google Sheets API. Выполняет запрос к API для получения данных из указанного листа.
4. **Обработка результатов:** Проверяет наличие данных (`values`). Если данных нет, выводит сообщение об отсутствии данных. В противном случае, итерируется по строкам данных (`values`), выводит столбцы `Name` и `Major` (индексы 0 и 4 соответственно).
5. **Обработка ошибок:** Обрабатывает потенциальные ошибки (`HttpError`) и выводит их сообщение в консоль.

**Пример данных:**

Если `values` содержит данные:

```
[['John Doe', 'Computer Science', 'Junior', '123', 'CS'], ['Jane Doe', 'Physics', 'Senior', '456', 'PHY']]
```

то вывод будет:

```
Name, Major:
John Doe, CS
Jane Doe, PHY
```

# <mermaid>

```mermaid
graph TD
    A[Вызов main()] --> B{Проверка token.json};
    B -- Есть -- C[creds = Credentials.from_authorized_user_file];
    B -- Нет -- D[flow = InstalledAppFlow];
    D --> E[creds = flow.run_local_server];
    E --> F[with open('token.json', 'w')];
    F --> C;
    C --> G[service = build('sheets', 'v4', credentials=creds)];
    G --> H[sheet = service.spreadsheets()];
    H --> I[result = sheet.values().get()];
    I --> J{result.get('values')?};
    J -- Да -- K[for row in values];
    K --> L[print(row[0], row[4])];
    K --> M[No data found];
    J -- Нет -- M;
    M --> N[Возвращение];
    I --> O[except HttpError as err];
    O --> P[print(err)];
    P --> N;
```

**Объяснение диаграммы:**

* `A` - начало выполнения скрипта.
* `B` - проверка существования файла `token.json`.
* `C` - чтение данных из `token.json`.
* `D` - инициализация процесса авторизации.
* `E` - получение токенов через локальный сервер.
* `F` - сохранение токенов в `token.json`.
* `G` - построение объекта `service` для работы с API.
* `H`, `I` - вызов метода `values().get` для получения данных из Google Sheet.
* `J` - проверка наличия данных.
* `K` - цикл обработки строк данных.
* `L` - вывод результатов.
* `M` - вывод сообщения "No data found".
* `O` - блок обработки исключений.
* `N` - завершение выполнения скрипта.

Подключаемые зависимости:

* `pathlib`: для работы с файлами и путями.
* `google-auth-oauthlib`: для аутентификации с использованием OAuth 2.0.
* `google-auth-httplib2`: для работы с HTTP.
* `google-api-python-client`: для доступа к Google Sheets API.
* `google.oauth2.credentials`: для работы с данными авторизации.
* `googleapiclient`: для доступа к API Google.
* `google.auth.transport.requests`: для работы с запросами.

# <explanation>

**Импорты:**

- `os.path`, `pathlib`: стандартные модули для работы с файловой системой.
- `google.auth.transport.requests`: необходим для взаимодействия с Google API.
- `google.oauth2.credentials`: для работы с данными авторизации, полученными из файла token.json.
- `google_auth_oauthlib.flow`: для реализации процесса авторизации через локальный сервер.
- `googleapiclient.discovery`: для работы с API Google.
- `googleapiclient.errors`: для обработки ошибок API.

**Классы:**

- `Credentials`: класс из библиотеки `google-auth-httplib2`,  используется для хранения данных об авторизации и доступа к Google API.
- `InstalledAppFlow`: класс из `google-auth-oauthlib`, необходим для управления процессом авторизации пользователя.

**Функции:**

- `main()`: главная функция программы. Она выполняет все шаги по получению данных из Google Sheets, включая авторизацию, запрос данных и вывод результатов.
- `Credentials.from_authorized_user_file`: чтение данных об авторизации из файла `token.json`.
- `flow.run_local_server`: запуск локального сервера для авторизации пользователя.


**Переменные:**

- `SCOPES`: список разрешений доступа к Google Sheets API.
- `SAMPLE_SPREADSHEET_ID`, `SAMPLE_RANGE_NAME`: идентификатор и диапазон листа в Google Sheets, к которому производится доступ.
- `ROOT_DIRECTORY`, `path`: переменные, используемые для определения пути к файлу `client_secret_*.json`.

**Возможные ошибки/улучшения:**

- **Отсутствие обработки ошибок при создании пути:** В коде нет проверки на валидность переменной `ROOT_DIRECTORY`. Если она не задана правильно, может возникнуть исключение. Нужно добавить проверку или использовать умолчание, если путь недоступен.
- **Необязательное создание пути:** Проверка `path.exists()` и дальнейшие действия с файлом `token.json` должны быть корректными для разных сценариев.
- **Необходимость переделки на использование `requests`:  В зависимости от использования Google API и его версий, может понадобиться переписать код для использования `requests` вместо `httplib2`.**

**Взаимосвязи:**

Код напрямую взаимодействует с Google Sheets API, используя  `googleapiclient` для запроса данных.  Файлы `credentials.json` и `token.json` хранят конфиденциальные данные, связанные с авторизацией пользователя.  Код предполагает наличие этих файлов в соответствующих директориях.