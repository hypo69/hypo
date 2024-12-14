# Анализ кода модуля `quickstart`

**Качество кода**
7
- Плюсы
    - Код выполняет основную функцию - взаимодействие с Google Apps Script API.
    - Используется `pathlib` для работы с путями.
    - Применяется `google-api-python-client` для работы с API Google.
    - Присутствует обработка токенов и их сохранения.
- Минусы
    - Отсутствует обработка ошибок с использованием `logger`.
    - Нет документации в формате RST.
    - Некоторые переменные и функции не соответствуют стандартам именования.
    - Стандартный `json.load` используется вместо `j_loads` или `j_loads_ns`.
    - Присутствуют избыточные комментарии.

**Рекомендации по улучшению**
1. Добавить  документацию в формате RST для модуля, функций и переменных.
2. Использовать `j_loads` или `j_loads_ns` из `src.utils.jjson` для чтения файлов.
3. Внедрить логирование ошибок с помощью `src.logger.logger` вместо стандартного `print` для ошибок.
4. Использовать более понятные имена для переменных.
5. Избавиться от избыточных комментариев.
6. Добавить обработку ошибок при работе с файлами.
7.  Улучшить читаемость кода, добавляя разрывы в сложных блоках.

**Оптимизированный код**
```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
Модуль для быстрого старта работы с Google Apps Script API.
===========================================================

Этот модуль предоставляет функциональность для создания нового скриптового проекта,
загрузки файлов в проект и вывода URL скрипта.

.. module:: src.goog.quickstart
    :platform: Windows, Unix
    :synopsis: Быстрый старт для работы с Google Apps Script API.

Пример использования
--------------------

.. code-block:: python

    from src.goog.quickstart import main

    if __name__ == '__main__':
        main()
"""
import os # импортируем модуль os

from pathlib import Path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient import errors
from googleapiclient.discovery import build

from src.logger.logger import logger # подключаем logger
from src.utils.jjson import j_loads # подключаем j_loads
from src import gs # подключаем gs


MODE = 'dev'  # Режим работы приложения


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
    Выполняет основные действия по работе с Apps Script API.

    Функция включает в себя:
        - Авторизацию в Google API.
        - Создание нового скриптового проекта.
        - Загрузку кода и манифеста в проект.
        - Вывод URL созданного скрипта.
    """
    creds = None
    token_path = gs.path.tmp / 'e-cat-346312-137284f4419e.json'
    # Проверяем наличие файла с токеном
    if token_path.exists():
        try:
            # Код исполняет загрузку учетных данных из файла токена
            creds = Credentials.from_authorized_user_file(token_path, SCOPES)
        except Exception as ex:
            logger.error(f'Ошибка при загрузке токена из файла: {token_path}', exc_info=True)
            return # Код возвращает управление при возникновении ошибки
    # Проверяем валидность учетных данных
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            try:
                # Код исполняет обновление токена
                creds.refresh(Request())
            except Exception as ex:
                logger.error(f'Ошибка при обновлении токена', exc_info=True)
                return # Код возвращает управление при возникновении ошибки
        else:
            try:
                # Код исполняет получение учетных данных из файла credentials.json
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', SCOPES)
                creds = flow.run_local_server(port=0)
            except Exception as ex:
                logger.error(f'Ошибка при получении учетных данных', exc_info=True)
                return # Код возвращает управление при возникновении ошибки

            try:
                # Код исполняет сохранение полученных учетных данных в файл
                with Path('token.json').open('w') as token:
                    token.write(creds.to_json())
            except Exception as ex:
                logger.error(f'Ошибка при сохранении токена в файл', exc_info=True)
                return # Код возвращает управление при возникновении ошибки

    try:
        # Код исполняет создание сервиса для работы с Google Apps Script API
        service = build('script', 'v1', credentials=creds)

        # Код исполняет создание нового проекта
        request_body = {'title': 'My Script'}
        response = service.projects().create(body=request_body).execute()

        # Код исполняет загрузку файлов в проект
        request_body = {
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
        response = service.projects().updateContent(
            body=request_body,
            scriptId=response['scriptId']
        ).execute()
        # Код выводит URL созданного скрипта
        print('https://script.google.com/d/' + response['scriptId'] + '/edit')
    except errors.HttpError as error:
        # Код логирует ошибку, если API столкнулся с проблемой
        logger.error(f'Ошибка API: {error.content}', exc_info=True)
    except Exception as ex:
        logger.error(f'Произошла непредвиденная ошибка: {ex}', exc_info=True)

if __name__ == '__main__':
    main()
```