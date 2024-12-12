## Improved Code
```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12
"""
Модуль для работы с Google Sheets API.
====================================================

Этот модуль демонстрирует базовое использование Google Sheets API для чтения данных из электронной таблицы.

Пример использования
--------------------

Пример запуска скрипта:

.. code-block:: python

    python google_sample.py
"""
from __future__ import print_function

import os.path
from pathlib import Path
from typing import List

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from src.logger.logger import logger

MODE = 'dev'

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms'
SAMPLE_RANGE_NAME = 'Class Data!A2:E'

ROOT_DIRECTORY = Path.cwd().absolute()
path = Path(ROOT_DIRECTORY, 'google_api', 'secrets', 'client_secret_920776813054-crpf1rcav3uui51kq9q1lis64glkpatj.apps.googleusercontent.com.json')


def main():
    """
    Выполняет основную логику для чтения данных из Google Sheets.
    
    Инициализирует учетные данные, подключается к API Google Sheets,
    считывает данные из указанной таблицы и выводит их.
    
    """
    creds = None
    # Файл token.json хранит токены доступа и обновления пользователя.
    # Он создается автоматически при первой успешной авторизации.
    if os.path.exists(path):
        creds = Credentials.from_authorized_user_file(path, SCOPES)
    # Если нет доступных (действительных) учетных данных, пользователю предлагается войти.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Сохраняет учетные данные для следующего запуска.
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        # Код создает сервис для работы с Google Sheets API.
        service = build('sheets', 'v4', credentials=creds)

        # Код вызывает Sheets API.
        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                    range=SAMPLE_RANGE_NAME).execute()
        values: List[List[str]] = result.get('values', [])

        if not values:
            print('No data found.')
            return

        print('Name, Major:')
        for row in values:
            # Код выводит столбцы A и E, соответствующие индексам 0 и 4.
            print('%s, %s' % (row[0], row[4]))
    except HttpError as err:
        # Код логирует ошибку HTTP
        logger.error('Ошибка при работе с Google Sheets API', exc_info=err)


if __name__ == '__main__':
    main()
```
## Changes Made

-   Добавлен RST docstring к модулю.
-   Добавлены импорты `List` и `logger` из `src.logger.logger`.
-   Добавлен RST docstring к функции `main`.
-   В блоке `try-except` заменено `print(err)` на `logger.error('Ошибка при работе с Google Sheets API', exc_info=err)` для логирования ошибок.
-   Добавлена аннотация типа `List[List[str]]` к переменной `values`.
-   Добавлены комментарии, объясняющие назначение каждого блока кода.

## FULL Code
```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12
"""
Модуль для работы с Google Sheets API.
====================================================

Этот модуль демонстрирует базовое использование Google Sheets API для чтения данных из электронной таблицы.

Пример использования
--------------------

Пример запуска скрипта:

.. code-block:: python

    python google_sample.py
"""
from __future__ import print_function

import os.path
from pathlib import Path
from typing import List

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from src.logger.logger import logger

MODE = 'dev'

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms'
SAMPLE_RANGE_NAME = 'Class Data!A2:E'

ROOT_DIRECTORY = Path.cwd().absolute()
path = Path(ROOT_DIRECTORY, 'google_api', 'secrets', 'client_secret_920776813054-crpf1rcav3uui51kq9q1lis64glkpatj.apps.googleusercontent.com.json')


def main():
    """
    Выполняет основную логику для чтения данных из Google Sheets.
    
    Инициализирует учетные данные, подключается к API Google Sheets,
    считывает данные из указанной таблицы и выводит их.
    
    """
    creds = None
    # Файл token.json хранит токены доступа и обновления пользователя.
    # Он создается автоматически при первой успешной авторизации.
    if os.path.exists(path):
        creds = Credentials.from_authorized_user_file(path, SCOPES)
    # Если нет доступных (действительных) учетных данных, пользователю предлагается войти.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Сохраняет учетные данные для следующего запуска.
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        # Код создает сервис для работы с Google Sheets API.
        service = build('sheets', 'v4', credentials=creds)

        # Код вызывает Sheets API.
        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                    range=SAMPLE_RANGE_NAME).execute()
        values: List[List[str]] = result.get('values', [])

        if not values:
            print('No data found.')
            return

        print('Name, Major:')
        for row in values:
            # Код выводит столбцы A и E, соответствующие индексам 0 и 4.
            print('%s, %s' % (row[0], row[4]))
    except HttpError as err:
        # Код логирует ошибку HTTP
        logger.error('Ошибка при работе с Google Sheets API', exc_info=err)


if __name__ == '__main__':
    main()