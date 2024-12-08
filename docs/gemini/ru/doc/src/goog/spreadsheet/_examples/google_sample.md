# Модуль hypotez/src/goog/spreadsheet/_examples/google_sample.py

## Обзор

Этот модуль предоставляет пример использования Google Sheets API для чтения данных из таблицы. Он демонстрирует процесс авторизации, получение доступа к данным и вывод данных в консоль.

## Функции

### `main`

**Описание**: Функция `main` является точкой входа программы. Она выполняет авторизацию, запрашивает данные из Google Sheets и выводит их в консоль.

**Параметры**:
Нет параметров.

**Возвращает**:
Нет значения возврата.

**Вызывает исключения**:
- `HttpError`: Возникает в случае ошибки при обращении к Google Sheets API.  Подробное сообщение об ошибке выводится на консоль.


## Постоянные значения

### `SCOPES`

**Описание**: Список разрешений доступа к Google Sheets API.

**Значение**: `['https://www.googleapis.com/auth/spreadsheets.readonly']`


### `SAMPLE_SPREADSHEET_ID`

**Описание**: ID таблицы Google Sheets, из которой будут считываться данные.

**Значение**: `'1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms'`


### `SAMPLE_RANGE_NAME`

**Описание**: Диапазон ячеек в таблице Google Sheets, из которого будут считываться данные.

**Значение**: `'Class Data!A2:E'`


### `ROOT_DIRECTORY`

**Описание**: Абсолютный путь к корневому каталогу проекта.

**Значение**: `Path.cwd().absolute()`


### `path`

**Описание**: Путь к файлу `client_secret.json`.

**Значение**:  `Path(ROOT_DIRECTORY, 'google_api', 'secrets', 'client_secret_920776813054-crpf1rcav3uui51kq9q1lis64glkpatj.apps.googleusercontent.com.json')`

### `MODE`

**Описание**: Режим работы приложения (например, 'dev', 'prod').

**Значение**: `'dev'`


## Дополнительные пояснения

- Файл `token.json` используется для хранения токенов доступа.
- Функция `main` использует `Credentials.from_authorized_user_file` для загрузки данных из `token.json`, если они существуют.
- Если токен устарел или отсутствует, функция выполняет авторизацию через `InstalledAppFlow`.
-  Обратите внимание на обработку ошибок (`try...except HttpError`).


## Использование

1. Установите необходимые библиотеки:
   ```bash
   pip install google-api-python-client google-auth-httplib2 google-auth-oauthlib
   ```
2. Замените `client_secret_920776813054-crpf1rcav3uui51kq9q1lis64glkpatj.apps.googleusercontent.com.json` на правильный путь к вашему файлу секретов.
3. Запустите скрипт.


```
```
```