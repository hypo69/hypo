# Анализ кода модуля `quickstart`

**Качество кода**
8
- Плюсы
    - Код выполняет свою основную задачу по взаимодействию с Google Apps Script API.
    - Используются библиотеки `google-auth` и `googleapiclient` для авторизации и работы с API.
    - Код структурирован и понятен.
    -  Используется `pathlib` для работы с путями.
- Минусы
    - Отсутствует обработка ошибок с помощью `logger.error`.
    - Не используется `j_loads` или `j_loads_ns` для загрузки `json`.
    - Комментарии не соответствуют формату reStructuredText.
    - Нет подробных docstring для функций и модуля.
    - Используется `print` вместо `logger.info` или `logger.error` для вывода сообщений.
    - Жестко закодированные пути к файлам и `credentials.json`

**Рекомендации по улучшению**
1. Добавить docstring для модуля и функции `main` в формате reStructuredText.
2. Использовать `j_loads` для загрузки данных из `token.json`, если это необходимо.
3. Заменить `print` на `logger.info` или `logger.error` для логирования сообщений и ошибок.
4. Улучшить обработку ошибок, используя `logger.error` вместо `try-except` с `print`.
5.  Переписать все комментарии в формате reStructuredText.
6. Использовать `os.path.join` для построения путей.
7. Перенести хардкод `credentials.json` в конфиг файл или переменную окружения.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
Модуль для быстрого старта работы с Apps Script API.
====================================================

Этот модуль демонстрирует базовое использование Apps Script API для создания нового скрипта,
загрузки файлов в проект и вывода URL скрипта.

:platform: Windows, Unix
:synopsis: Быстрый старт для Apps Script API.

Пример использования
--------------------

.. code-block:: python

   from src.goog import quickstart

   quickstart.main()
"""
import os
from pathlib import Path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient import errors
from googleapiclient.discovery import build

from src.utils.jjson import j_loads # импорт j_loads из src.utils.jjson
from src.logger.logger import logger  # импорт logger
from src import gs

MODE = 'dev'


# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/script.projects']

SAMPLE_CODE = '''
function helloWorld() {
  console.log("Hello, world!");
}
'''.strip()

SAMPLE_MANIFEST = '''
{
  "timeZone": "America/New_York",
  "exceptionLogging": "CLOUD"
}
'''.strip()


def main():
    """
    Вызывает Apps Script API для создания и настройки нового скрипта.

    Эта функция выполняет следующие шаги:
    1. Аутентифицирует пользователя с помощью Google OAuth2.
    2. Создает новый проект Apps Script.
    3. Загружает код и манифест в проект.
    4. Выводит URL для доступа к созданному скрипту.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    # путь к файлу с токеном
    token_path = os.path.join(gs.path.tmp, 'e-cat-346312-137284f4419e.json')
    # проверка существования файла с токеном
    if Path(token_path).exists():
        try:
            # загрузка учетных данных из файла
            creds = Credentials.from_authorized_user_file(token_path, SCOPES)
        except Exception as ex:
           logger.error(f'ошибка загрузки файла {token_path}', exc_info=ex)
           return
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            try:
                # обновление учетных данных
                creds.refresh(Request())
            except Exception as ex:
                logger.error('ошибка обновления учетных данных', exc_info=ex)
                return
        else:
            try:
               # получение учетных данных
               flow = InstalledAppFlow.from_client_secrets_file(
                   'credentials.json', SCOPES) # TODO: перенести в конфиг
               creds = flow.run_local_server(port=0)
            except Exception as ex:
                logger.error('ошибка получения учетных данных', exc_info=ex)
                return
        # Save the credentials for the next run
        try:
            # сохранение учетных данных
            with Path('token.json').open('w') as token:
                 token.write(creds.to_json())
        except Exception as ex:
            logger.error(f'ошибка сохранения token.json', exc_info=ex)
            return

    try:
        # создание сервиса для работы с Apps Script API
        service = build('script', 'v1', credentials=creds)

        # Call the Apps Script API
        # Create a new project
        # запрос на создание проекта
        request = {'title': 'My Script'}
        response = service.projects().create(body=request).execute()
        # запрос на обновление контента проекта
        request = {
            'files': [{
                'name': 'hello',
                'type': 'SERVER_JS',
                'source': SAMPLE_CODE
            }, {
                'name': 'appsscript',
                'type': 'JSON',
                'source': SAMPLE_MANIFEST
            }]
        }
        # обновление контента проекта
        response = service.projects().updateContent(
            body=request,
            scriptId=response['scriptId']).execute()
        # вывод URL проекта
        logger.info(f'https://script.google.com/d/{response["scriptId"]}/edit')
    except errors.HttpError as error:
        # The API encountered a problem.
        logger.error(f'ошибка API: {error.content}')


if __name__ == '__main__':
    main()
```