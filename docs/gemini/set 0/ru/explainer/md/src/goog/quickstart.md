```MD
# <input code>

```python
## \file hypotez/src/goog/quickstart.py
# -*- coding: utf-8 -*-\
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
.. module: src.goog 
	:platform: Windows, Unix
	:synopsis:

"""
MODE = 'dev'


"""
Shows basic usage of the Apps Script API.
Call the Apps Script API to create a new script project, upload a file to the
project, and log the script's URL to the user.

https://developers.google.com/apps-script/api/quickstart/python
"""


from pathlib import Path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient import errors
from googleapiclient.discovery import build

import header
from src import gs

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/script.projects']

SAMPLE_CODE = """
function helloWorld() {
  console.log("Hello, world!");
}
""".strip()

SAMPLE_MANIFEST = """
{
  "timeZone": "America/New_York",
  "exceptionLogging": "CLOUD"
}
""".strip()


def main():
    """Calls the Apps Script API."""
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    token_path = gs.path.tmp / 'e-cat-346312-137284f4419e.json'
    if token_path.exists():
        creds = Credentials.from_authorized_user_file(token_path, SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with Path('token.json').open('w') as token:
            token.write(creds.to_json())

    try:
        service = build('script', 'v1', credentials=creds)

        # Call the Apps Script API
        # Create a new project
        request = {'title': 'My Script'}
        response = service.projects().create(body=request).execute()

        # Upload two files to the project
        request = {
            'files': [
                {'name': 'hello', 'type': 'SERVER_JS', 'source': SAMPLE_CODE},
                {'name': 'appsscript', 'type': 'JSON', 'source': SAMPLE_MANIFEST}
            ]
        }
        response = service.projects().updateContent(
            body=request,
            scriptId=response['scriptId']).execute()
        print('https://script.google.com/d/' + response['scriptId'] + '/edit')
    except errors.HttpError as error:
        # The API encountered a problem.
        print(error.content)


if __name__ == '__main__':
    main()
```

# <algorithm>

**Шаг 1:** Инициализация переменных.  `creds` устанавливается в `None`, `token_path` содержит путь к файлу `token.json`.


**Шаг 2:** Проверка наличия файла `token.json`. Если он существует, то загружаются данные из файла и сохраняются в `creds`.


**Шаг 3:** Проверка валидности токена. Если `creds` невалидный или просроченный, запускается авторизация с помощью `InstalledAppFlow`. Серверная часть приложения GoogleAppsScript авторизуется.


**Шаг 4:** Сохранение токена. Создаётся файл `token.json` и сохраняется новый токен.


**Шаг 5:** Вызов API. Создается экземпляр сервиса `service` с помощью `build`.


**Шаг 6:** Создание проекта. Функция `projects().create()` вызывается для создания нового проекта Google Apps Script с именем 'My Script'  и сохраняет результат в `response`.


**Шаг 7:** Загрузка файлов. Функция `projects().updateContent()` загружает скрипт (`SAMPLE_CODE`) и манифест (`SAMPLE_MANIFEST`) в новый проект.


**Шаг 8:** Вывод ссылки. Выводится ссылка на созданный проект в Google Apps Script.


**Шаг 9:** Обработка ошибок. Обрабатывается исключение `errors.HttpError`, если произошла ошибка при взаимодействии с API.


# <mermaid>

```mermaid
graph TD
    A[main()] --> B{creds = None};
    B -- token.json exists --> C[creds = Credentials.from_authorized_user_file];
    B -- !token.json --> D{creds = None or not creds.valid};
    D -- creds.expired --> E[creds.refresh(Request())];
    D -- !creds.expired --> F[flow = InstalledAppFlow];
    F --> G[creds = flow.run_local_server];
    G --> H[token.write(creds.to_json())];
    C --> I[service = build()];
    I --> J[request = {'title': 'My Script'}];
    J --> K[response = service.projects().create()];
    K --> L[request = {'files': [...]}];
    L --> M[response = service.projects().updateContent()];
    M --> N[print URL];
    D -- error --> O[error.content];
```

# <explanation>

**Импорты:**

- `pathlib`: для работы с путями файлов.
- `google.auth.transport.requests`: для работы с запросами к Google API.
- `google.oauth2.credentials`: для работы с учетными данными доступа.
- `google_auth_oauthlib.flow`: для авторизации приложения.
- `googleapiclient.errors`: для обработки ошибок при взаимодействии с Google API.
- `googleapiclient.discovery`: для построения запросов к Google API.
- `header`: предполагается, что содержит вспомогательные функции для текущего модуля.
- `gs`: предположительно, часть проекта, содержащая вспомогательные функции, возможно, для работы с хранилищем Google Cloud Storage.


**Классы:**

- `Credentials`: хранит учетные данные доступа к API Google. Используется для аутентификации.
- `InstalledAppFlow`: используется для автоматической авторизации приложения.


**Функции:**

- `main()`:  Основная функция, выполняющая все действия по созданию и загрузке файлов в проект Google Apps Script.
- `build('script', 'v1', credentials=creds)`: Создаёт объект для работы с API Google Apps Script. `credentials` - данные авторизации.
- `Credentials.from_authorized_user_file()`: Загружает данные авторизации из файла.
- `creds.refresh()`: Обновляет данные авторизации, если они просрочены.
- `InstalledAppFlow.from_client_secrets_file()`: Создаёт объект для запуска авторизации через браузер.
- `flow.run_local_server()`: Запускает сервер для авторизации в Google Apps Script.
- `response.execute()`: Выполняет запрос к API Google Apps Script и возвращает результат.


**Переменные:**

- `SCOPES`: Список требуемых разрешений для доступа к API.
- `SAMPLE_CODE`, `SAMPLE_MANIFEST`: Примеры кода и манифеста для добавления в проект.
- `creds`: Хранит данные авторизации.
- `token_path`: Путь к файлу `token.json`.
- `service`: Объект для работы с API Google Apps Script.


**Возможные ошибки и улучшения:**

- **Обработка ошибок:** Обработка ошибок более подробная. Например, можно ловить исключения `FileNotFoundError` для случая, если файл `credentials.json` не найден.
- **Локализация:** Приложение может быть некорректно работать, если timezone в `SAMPLE_MANIFEST` не соответствует часовому поясу, используемому пользователем.


**Взаимосвязи с другими частями проекта:**

- Модуль `gs` явно используется для получения пути к временной папке. Это указывает на то, что этот модуль предоставляет функционал для работы с файловой системой или хранилищем.  `gs.path.tmp` - это важный компонент проекта, показывающий, как приложения Google Apps Script интегрируются с базовой инфраструктурой.

```