# Анализ кода модуля `google_sample.py`

**Качество кода**
1.  Соответствие требованиям по оформлению кода: 7/10
    -   Плюсы
        -   Импорты в начале файла.
        -   Используются `pathlib` для работы с путями.
        -   Наличие блока `if __name__ == '__main__':`.
    -   Минусы
        -   Отсутствует docstring модуля.
        -   Отсутствуют docstring для функций.
        -   Используются устаревшие способы форматирования строк (например, `%s`).
        -   Используется `print` вместо логирования.
        -   Не используется `j_loads` или `j_loads_ns`.

**Рекомендации по улучшению**

1.  Добавить docstring модуля в формате RST.
2.  Добавить docstring для функции `main` в формате RST.
3.  Использовать f-строки вместо `%s` для форматирования строк.
4.  Заменить `print` на логирование с помощью `logger`.
5.  Обрабатывать ошибки `HttpError` с использованием `logger.error`.
6.  Изменить способ получения пути к файлу `credentials.json` на более гибкий, например, через переменные окружения или аргументы командной строки.
7.  Перенести логику загрузки credentials в отдельную функцию.
8.  Удалить лишние комментарии, которые не несут смысловой нагрузки.
9.  Удалить неиспользуемые shebangs.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
"""
Модуль для демонстрации работы с Google Sheets API.
==================================================

Этот модуль демонстрирует базовое использование Google Sheets API для чтения данных из электронной таблицы.
Он аутентифицируется с использованием учетных данных пользователя и извлекает значения из указанного диапазона.

Пример использования
--------------------

.. code-block:: python

    python google_sample.py
"""

import os.path
from pathlib import Path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from src.logger.logger import logger
from src.utils.jjson import j_loads

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms'
SAMPLE_RANGE_NAME = 'Class Data!A2:E'

ROOT_DIRECTORY = Path.cwd().absolute()
CREDENTIALS_PATH = Path(ROOT_DIRECTORY, 'google_api', 'secrets',
                       'client_secret_920776813054-crpf1rcav3uui51kq9q1lis64glkpatj.apps.googleusercontent.com.json')
TOKEN_PATH = 'token.json'

def load_credentials():
    """
    Загружает учетные данные пользователя для работы с Google Sheets API.

    Пытается загрузить учетные данные из файла `token.json`. Если файл не существует или
    учетные данные недействительны, запускается процесс авторизации и сохраняются новые учетные данные.

    :return: Объект `Credentials` или None в случае ошибки.
    :rtype: google.oauth2.credentials.Credentials | None
    """
    creds = None
    if os.path.exists(TOKEN_PATH):
        creds = Credentials.from_authorized_user_file(TOKEN_PATH, SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            try:
                flow = InstalledAppFlow.from_client_secrets_file(
                    CREDENTIALS_PATH, SCOPES)
                creds = flow.run_local_server(port=0)
            except Exception as ex:
                logger.error(f'Ошибка при загрузке учетных данных: {ex}')
                return None
        # Save the credentials for the next run
        with open(TOKEN_PATH, 'w') as token:
            token.write(creds.to_json())
    return creds

def main():
    """
    Демонстрирует базовое использование Sheets API.
    Выводит значения из примера электронной таблицы.
    """
    creds = load_credentials()
    if not creds:
        logger.error('Не удалось загрузить учетные данные.')
        return

    try:
        service = build('sheets', 'v4', credentials=creds)

        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                    range=SAMPLE_RANGE_NAME).execute()
        values = result.get('values', [])

        if not values:
            logger.info('No data found.')
            return

        logger.info('Name, Major:')
        for row in values:
            logger.info(f'{row[0]}, {row[4]}')
    except HttpError as err:
        logger.error(f'Произошла ошибка HTTP: {err}')
    except Exception as ex:
        logger.error(f'Произошла непредвиденная ошибка: {ex}')

if __name__ == '__main__':
    main()
```