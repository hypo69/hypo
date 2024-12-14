# Анализ кода модуля `google_sample.py`

**Качество кода**
6
-  Плюсы
    - Код выполняет базовую функциональность для чтения данных из Google Sheets API.
    - Используется `pathlib` для работы с путями.
    - Есть обработка ошибок HTTP.
-  Минусы
    - Не хватает документации в формате reStructuredText.
    - Используется стандартный `print` вместо логирования.
    - Путь к файлу `client_secret_920776813054-crpf1rcav3uui51kq9q1lis64glkpatj.apps.googleusercontent.com.json` задан жестко в коде.
    - Жестко задан путь к `token.json`, что может привести к проблемам.
    - Отсутствует обработка исключений при чтении токена из файла.
    - Отсутствует использование `j_loads` или `j_loads_ns` из `src.utils.jjson`.
    - Не используются константы для магических значений и строк.

**Рекомендации по улучшению**

1.  Добавить reStructuredText документацию для модуля и функции `main`.
2.  Заменить `print` на `logger` для вывода сообщений об ошибках и отладочных данных.
3.  Изменить способ хранения пути к `client_secret.json` и токену, использовать переменные окружения или конфиги.
4.  Использовать `j_loads` или `j_loads_ns` для загрузки файла `credentials.json`.
5.  Добавить обработку исключений при работе с файлами `token.json`.
6.  Использовать константы для магических строк, например, `SAMPLE_SPREADSHEET_ID`, `SAMPLE_RANGE_NAME`,  `TOKEN_FILE`, `CLIENT_SECRET_FILE`.
7.  Удалить лишние шебанги.
8.  Пересмотреть способ получения `client_secret_920776813054-crpf1rcav3uui51kq9q1lis64glkpatj.apps.googleusercontent.com.json`.

**Оптимизированный код**
```python
# -*- coding: utf-8 -*-
"""
Модуль для работы с Google Sheets API.
=========================================================================================

Этот модуль содержит пример кода для чтения данных из Google Sheets.
Использует Google Sheets API для доступа к данным электронной таблицы и вывода
содержимого.

Пример использования
--------------------

.. code-block:: python

   from src.goog.spreadsheet._examples.google_sample import main

   if __name__ == '__main__':
       main()
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
TOKEN_FILE = 'token.json'
CLIENT_SECRET_FILE = 'credentials.json'


ROOT_DIRECTORY = Path.cwd().absolute()
# Path к секретному файлу.
CREDENTIALS_PATH = Path(ROOT_DIRECTORY, 'google_api', 'secrets',
                       'client_secret_920776813054-crpf1rcav3uui51kq9q1lis64glkpatj.apps.googleusercontent.com.json')

def main():
    """
    Выполняет чтение данных из Google Sheets API и выводит их в консоль.

    Функция использует Google Sheets API для доступа к данным из указанной
    электронной таблицы, извлекает значения из заданного диапазона и выводит их.
    """
    creds = None
    # Проверяет наличие файла с токенами доступа.
    if os.path.exists(TOKEN_FILE):
        try:
             # Загрузка токена из файла.
            creds = Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)
        except Exception as ex:
            logger.error(f'Ошибка при чтении файла токена {TOKEN_FILE}: {ex}')
            return

    # Если нет действительных учетных данных, пытается их получить.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            # Обновляет токен, если он истек.
            creds.refresh(Request())
        else:
            try:
                # Получение токенов при помощи файла с учетными данными.
                flow = InstalledAppFlow.from_client_secrets_file(
                    CLIENT_SECRET_FILE, SCOPES)
                creds = flow.run_local_server(port=0)
            except Exception as ex:
                 logger.error(f'Ошибка при создании потока аутентификации {CLIENT_SECRET_FILE}: {ex}')
                 return
            # Сохранение полученных токенов.
        try:
            with open(TOKEN_FILE, 'w') as token:
                token.write(creds.to_json())
        except Exception as ex:
             logger.error(f'Ошибка при сохранении токена в файл {TOKEN_FILE}: {ex}')
             return

    try:
        # Создание сервиса для работы с Google Sheets API.
        service = build('sheets', 'v4', credentials=creds)

        # Вызов Sheets API для получения данных.
        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                    range=SAMPLE_RANGE_NAME).execute()
        values = result.get('values', [])

        if not values:
            logger.info('Данные не найдены.')
            return

        logger.info('Name, Major:')
        for row in values:
            # Вывод колонок A и E, которые соответствуют индексам 0 и 4.
            logger.info('%s, %s' % (row[0], row[4]))
    except HttpError as err:
        logger.error(f'Ошибка HTTP при работе с Google Sheets API: {err}')
    except Exception as ex:
        logger.error(f'Неизвестная ошибка при работе с Google Sheets API: {ex}')


if __name__ == '__main__':
    main()
```