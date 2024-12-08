# Модуль hypotez/src/goog/quickstart.py

## Обзор

Модуль `quickstart.py` предоставляет пример использования API Google Apps Script на Python. Он демонстрирует создание нового проекта Apps Script, загрузку файлов в проект и вывод URL проекта.  Модуль использует библиотеки `google-auth-oauthlib` и `googleapiclient` для взаимодействия с API.

## Импорты

```python
from pathlib import Path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient import errors
from googleapiclient.discovery import build
import header
from src import gs
```

## Константы

```python
MODE = 'dev'
SCOPES = ['https://www.googleapis.com/auth/script.projects']
SAMPLE_CODE = """function helloWorld() {
  console.log("Hello, world!");
}
""".strip()
SAMPLE_MANIFEST = """{
  "timeZone": "America/New_York",
  "exceptionLogging": "CLOUD"
}
""".strip()
```

## Функции

### `main`

**Описание**: Выполняет основные операции взаимодействия с API Google Apps Script.

**Описание аргументов**: Нет входных аргументов.

**Возвращает**: Нет возвращаемых значений.

**Возможные исключения**:
- `errors.HttpError`: Возникает при ошибках, связанных с выполнением запросов к API.  В этом случае выводится содержимое ошибки.


```python
def main():
    """Calls the Apps Script API."""
    creds = None
    token_path = gs.path.tmp / 'e-cat-346312-137284f4419e.json'
    if token_path.exists():
        creds = Credentials.from_authorized_user_file(token_path, SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with Path('token.json').open('w') as token:
            token.write(creds.to_json())

    try:
        service = build('script', 'v1', credentials=creds)
        request = {'title': 'My Script'}
        response = service.projects().create(body=request).execute()
        request = {
            'files': [
                {'name': 'hello', 'type': 'SERVER_JS', 'source': SAMPLE_CODE},
                {'name': 'appsscript', 'type': 'JSON', 'source': SAMPLE_MANIFEST}
            ]
        }
        response = service.projects().updateContent(
            body=request, scriptId=response['scriptId']).execute()
        print('https://script.google.com/d/' + response['scriptId'] + '/edit')
    except errors.HttpError as error:
        print(error.content)
```
```
```