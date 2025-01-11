# Анализ кода модуля `google_sample`

**Качество кода**
   -  Соответствие требованиям по оформлению кода: 7/10
   -  Плюсы:
        - Код выполняет базовую задачу чтения данных из Google Sheets.
        - Используются стандартные библиотеки Google API.
        - Присутствуют комментарии, объясняющие некоторые части кода.
   -  Минусы:
        - Не все импорты соответствуют общей структуре проекта (например, `logger`).
        - Отсутствует документация в формате RST для модуля и функций.
        - Используется `print` для вывода, что не соответствует стандартам логирования.
        - Не используется `j_loads` или `j_loads_ns`.
        - Используется двойные кавычки в коде, вместо одинарных

**Рекомендации по улучшению**
1.  **Импорты:**
    - Добавить импорт `from src.logger import logger` для логирования.
    - Убрать неиспользуемые импорты.
2.  **Документация:**
    - Добавить документацию в формате RST для модуля и функции `main`.
3.  **Логирование:**
    - Заменить использование `print` на `logger.info` и `logger.error`.
4.  **Обработка ошибок:**
     -  Заменить `print(err)` на `logger.error(err)`.
5. **Стиль кода:**
    - Использовать одинарные кавычки для строк в коде, кроме операций вывода (`print`, `logger.error` и т.п.)
6. **Путь к файлу**
    - Использовать os.path.join для конструирования пути

**Оптимизированный код**

```python
"""
Модуль для работы с Google Sheets API.
=========================================================================================

Этот модуль демонстрирует базовое использование Sheets API для чтения данных из Google Таблицы.

Пример использования
--------------------

.. code-block:: python

    python google_sample.py
"""
# -*- coding: utf-8 -*-
#! venv/bin/python/python3.12

from __future__ import print_function
import os
# from pathlib import Path #  не используется
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from src.logger import logger # Добавлен импорт logger

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms'
SAMPLE_RANGE_NAME = 'Class Data!A2:E'

ROOT_DIRECTORY = os.getcwd()#Path.cwd().absolute()
path = os.path.join(ROOT_DIRECTORY,'google_api','secrets','client_secret_920776813054-crpf1rcav3uui51kq9q1lis64glkpatj.apps.googleusercontent.com.json')
def main():
    """
    Shows basic usage of the Sheets API.
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
            logger.info('No data found.') # Заменено на logger.info
            return

        logger.info('Name, Major:') # Заменено на logger.info
        for row in values:
            # Print columns A and E, which correspond to indices 0 and 4.
            logger.info('%s, %s' % (row[0], row[4]))# Заменено на logger.info
    except HttpError as err:
        logger.error(err) # Заменено на logger.error


if __name__ == '__main__':
    main()
```