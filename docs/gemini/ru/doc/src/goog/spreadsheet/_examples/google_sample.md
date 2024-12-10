# Модуль `hypotez/src/goog/spreadsheet/_examples/google_sample.py`

## Обзор

Этот модуль предоставляет пример использования Google Sheets API для чтения данных из таблицы Google. Модуль реализует процесс авторизации, получения доступа к данным и вывода данных в консоль.

## Переменные

### `MODE`

**Описание**: Строковая переменная, хранящая значение режима работы (например, 'dev').

### `SCOPES`

**Описание**: Список строк, представляющих разрешения, необходимые для доступа к Google Sheets API.

### `SAMPLE_SPREADSHEET_ID`

**Описание**: Строковая переменная, содержащая идентификатор таблицы Google Sheets.

### `SAMPLE_RANGE_NAME`

**Описание**: Строковая переменная, содержащая диапазон данных в таблице Google Sheets для чтения.

### `ROOT_DIRECTORY`

**Описание**: Путь к корневому каталогу проекта.

### `path`

**Описание**: Путь к файлу `client_secret.json` для авторизации.

## Функции

### `main`

**Описание**: Функция, которая демонстрирует базовый способ использования Google Sheets API для чтения данных из таблицы. Она выполняет авторизацию, запрашивает данные и выводит их в консоль.

**Код**:

```python
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
```

**Параметры**:

Нет входных параметров.

**Возвращает**:

Нет возвращаемого значения.

**Вызывает исключения**:

- `HttpError`: Возникает при ошибках во взаимодействии с Google Sheets API.
```