# Анализ кода модуля `google_sample.py`

**Качество кода**
    8
 -  Плюсы
        - Код выполняет поставленную задачу по чтению данных из Google Sheets.
        - Используется `google-api-python-client` для взаимодействия с Google Sheets API.
        - Есть обработка случаев, когда нет сохраненных учетных данных, и выполняется запрос на новые.
        - Код разбит на функции для лучшей читаемости.

 -  Минусы
    - Отсутствует  подробная документация в формате reStructuredText (RST).
    - Не используется кастомный логгер.
    - Используется стандартный `print` вместо `logger` для логирования ошибок и вывода информации.
    - Жестко задан путь к файлу `client_secret_920776813054-crpf1rcav3uui51kq9q1lis64glkpatj.apps.googleusercontent.com.json` и файлу `token.json`.
    - Файл `credentials.json` также жестко задан.
    - Не используются `j_loads` и `j_loads_ns` из `src.utils.jjson`
    - Не обрабатываются возможные исключения, которые могут возникнуть при чтении файлов `credentials.json` и `token.json`
    - Нет описания констант.
    - Отсутствует описание модуля и использования модуля.

**Рекомендации по улучшению**

1.  **Документация:**
    - Добавить docstring к модулю с описанием его назначения,  подробное описание класса, функций.
    - Добавить docstring к функции `main` с описанием ее работы.
    - Добавить комментарии в формате reStructuredText (RST) к константам, переменным.

2.  **Логирование:**
    - Заменить `print` на `logger.info`, `logger.debug` и `logger.error` для вывода информации, отладочных сообщений и ошибок.
    - Добавить обработку исключений с использованием `logger.error` вместо стандартного `try-except` для более информативного логирования.

3.  **Управление учетными данными:**
    - Использовать `j_loads` или `j_loads_ns` из `src.utils.jjson` для загрузки конфигурационных файлов (`client_secret_920776813054-crpf1rcav3uui51kq9q1lis64glkpatj.apps.googleusercontent.com.json`, `credentials.json` и `token.json`)

4.  **Конфигурация:**
    - Использовать переменные окружения или конфигурационный файл для хранения путей к файлам учетных данных.
    - Перенести `SAMPLE_SPREADSHEET_ID` и `SAMPLE_RANGE_NAME` в конфигурационный файл или переменные окружения.

5. **Обработка ошибок**:
    - Обработать исключения при чтении файлов `credentials.json` и `token.json`.

6. **Структура проекта**:
  -  Добавить описание модуля.
  -  Добавить описание использования модуля.

**Оптимизированный код**

```python
"""
Модуль для взаимодействия с Google Sheets API.
=========================================================================================

Этот модуль содержит функции для получения данных из Google Sheets.
Использует google-api-python-client для взаимодействия с Google Sheets API.

Пример использования
--------------------

.. code-block:: python

   from src.goog.spreadsheet._examples import google_sample

   google_sample.main()
"""
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

import os.path
from pathlib import Path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
# from src.utils.jjson import j_loads # TODO: переделать на кастомный лоадер
from src.logger.logger import logger #  Используем кастомный логгер

# Определение режима работы (например, 'dev' или 'prod').
MODE = 'dev'

# Область доступа к Google Sheets API.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

# ID и диапазон образцовой таблицы.
SAMPLE_SPREADSHEET_ID = '1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms'
SAMPLE_RANGE_NAME = 'Class Data!A2:E'

# Получение абсолютного пути к текущей директории.
ROOT_DIRECTORY = Path.cwd().absolute()
# Определение пути к файлу с учетными данными.
path = Path(ROOT_DIRECTORY,'google_api','secrets','client_secret_920776813054-crpf1rcav3uui51kq9q1lis64glkpatj.apps.googleusercontent.com.json')

def main():
    """
    Основная функция для взаимодействия с Google Sheets API.

    Загружает учетные данные, подключается к Google Sheets API и выводит данные из указанного диапазона.
    """
    creds = None
    # Проверка наличия файла с токенами.
    if os.path.exists(path):
         # Загрузка учетных данных из файла.
        creds = Credentials.from_authorized_user_file(path, SCOPES)
    # Если нет учетных данных или они недействительны, то запрашиваем новые.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
             # Обновление токена доступа.
            creds.refresh(Request())
        else:
            # Загрузка учетных данных из файла 'credentials.json'.
            try:
                # TODO:  with open('credentials.json', 'r') as f:
                # TODO:  credentials = j_loads(f)

                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', SCOPES)
                creds = flow.run_local_server(port=0)
            except Exception as ex:
                logger.error('Ошибка загрузки файла credentials.json', exc_info=ex)
                return
        # Сохранение полученных учетных данных в файл 'token.json'.
        try:
           with open('token.json', 'w') as token:
               token.write(creds.to_json())
        except Exception as ex:
                logger.error('Ошибка сохранения токена в файл token.json', exc_info=ex)
                return

    try:
        # Создание сервиса для работы с Google Sheets API.
        service = build('sheets', 'v4', credentials=creds)

        # Вызов API для получения данных из таблицы.
        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                    range=SAMPLE_RANGE_NAME).execute()
        values = result.get('values', [])
        # Проверка наличия данных.
        if not values:
            logger.info('No data found.')
            return

        logger.info('Name, Major:')
        # Вывод данных.
        for row in values:
            # Вывод столбцов A и E, которые соответствуют индексам 0 и 4.
            logger.info('%s, %s' % (row[0], row[4]))
    except HttpError as err:
        logger.error(f'An error occurred: {err}')

if __name__ == '__main__':
    main()
```