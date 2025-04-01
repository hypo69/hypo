# Модуль: `src.goog.spreadsheet._experiments.google_sample`

## Обзор

Модуль представляет собой пример работы с Google Sheets API через протокол `oauth2`. Он демонстрирует, как получить доступ к таблице Google, прочитать данные из указанного диапазона и вывести их в консоль.

## Подробней

Этот модуль предназначен для демонстрации базового взаимодействия с Google Sheets API. Он использует учетные данные пользователя для аутентификации и авторизации, а затем выполняет запрос на чтение данных из таблицы. Модуль полезен для ознакомления с процессом аутентификации и получения данных из Google Sheets.

## Классы

В данном модуле классы отсутствуют.

## Функции

### `main`

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

**Описание**: Основная функция модуля, демонстрирующая использование Google Sheets API для чтения данных из таблицы.

**Как работает функция**:
1.  Инициализирует переменную `creds` значением `None`.
2.  Проверяет наличие файла с сохраненными учетными данными (`token.json`). Если файл существует, пытается загрузить учетные данные из этого файла.
3.  Если учетные данные отсутствуют или недействительны, запускает процесс аутентификации пользователя через `InstalledAppFlow`. Этот процесс открывает локальный сервер, чтобы получить учетные данные от пользователя.
4.  После успешной аутентификации сохраняет полученные учетные данные в файл `token.json` для последующего использования.
5.  Создает сервис Google Sheets API с использованием полученных учетных данных.
6.  Выполняет запрос к таблице Google для получения данных из указанного диапазона (`SAMPLE_RANGE_NAME`).
7.  Обрабатывает полученные данные и выводит в консоль значения из столбцов A и E каждой строки.
8.  Обрабатывает исключение `HttpError`, которое может возникнуть при взаимодействии с API, и выводит сообщение об ошибке.

**Параметры**:
-   Отсутствуют

**Возвращает**:
-   Отсутствует

**Вызывает исключения**:
-   `HttpError`: Возникает при ошибках HTTP-запросов к Google Sheets API.

**Примеры**:

При первом запуске:

```python
main() # потребуется аутентификация в браузере
```

При последующих запусках (если файл `token.json` существует):

```python
main() # данные будут выведены в консоль без повторной аутентификации
```