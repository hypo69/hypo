# Анализ кода модуля `quickstart.py`

**Качество кода**
7
- Плюсы
    - Код в целом структурирован и выполняет свою задачу - создание и обновление скриптов Google Apps Script.
    - Используются стандартные библиотеки для работы с Google API.
    - Присутствует обработка ошибок HTTP.
- Минусы
    - Отсутствуют docstring для модуля и функции `main`.
    - Жестко заданы пути к файлам `token.json` и `credentials.json`.
    - Не используется `logger` для логирования ошибок.
    - Не используется `j_loads` для работы с `json`.

**Рекомендации по улучшению**

1.  Добавить docstring для модуля и функции `main`.
2.  Использовать `src.utils.jjson` для загрузки `json`.
3.  Использовать `logger` для логирования ошибок и отладки.
4.  Вынести пути к файлам в переменные или настройки, чтобы их можно было легко менять.
5.  Улучшить обработку ошибок, используя logger.error вместо простого вывода в консоль.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
"""
Модуль для быстрого запуска Apps Script API.
=========================================================================================

Этот модуль демонстрирует базовое использование Apps Script API для создания нового
скриптового проекта, загрузки файла в проект и вывода URL-адреса скрипта для пользователя.

https://developers.google.com/apps-script/api/quickstart/python

"""
import os
from pathlib import Path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient import errors
from googleapiclient.discovery import build

from src.utils.jjson import j_loads
from src.logger.logger import logger
from src import gs



# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/script.projects']

SAMPLE_CODE = """
function helloWorld() {
  console.log("Hello, world!");
}
""".strip()

SAMPLE_MANIFEST = """
{
  "timeZone": "America/New_York",
  "exceptionLogging": "CLOUD"
}
""".strip()

CREDENTIALS_FILE = 'credentials.json'
TOKEN_FILE = 'token.json'


def main():
    """
    Вызывает Apps Script API для создания и обновления скрипта.

    Функция выполняет следующие шаги:
        1.  Загружает учетные данные пользователя из файла `token.json` или выполняет авторизацию.
        2.  Создает новый скриптовый проект.
        3.  Загружает файлы кода и манифеста в проект.
        4.  Выводит URL-адрес созданного скрипта.
        5.  Логирует ошибки через `logger.error`
    """
    creds = None
    # Путь к файлу с токеном
    token_path = gs.path.tmp / 'e-cat-346312-137284f4419e.json' #  Определение пути к файлу с токеном.
    if token_path.exists():
        try:
            creds = Credentials.from_authorized_user_file(str(token_path), SCOPES) # Загрузка токена из файла.
        except Exception as e:
             logger.error(f'Ошибка загрузки токена из файла {token_path}', exc_info=True) # Логирование ошибки загрузки токена.
             return
    # Проверка наличия (валидных) учетных данных
    if not creds or not creds.valid: # Код проверяет, есть ли действительные учетные данные.
        if creds and creds.expired and creds.refresh_token: # Код проверяет, истек ли срок действия токена.
            try:
                creds.refresh(Request())  # Обновление токена.
            except Exception as e:
                 logger.error('Ошибка обновления токена', exc_info=True) # Логирование ошибки обновления токена.
                 return
        else:
            try:
                flow = InstalledAppFlow.from_client_secrets_file(
                    CREDENTIALS_FILE, SCOPES) # Создание потока аутентификации.
                creds = flow.run_local_server(port=0)  # Запуск локального сервера для авторизации.
            except Exception as e:
                 logger.error(f'Ошибка авторизации {CREDENTIALS_FILE=}', exc_info=True) # Логирование ошибки авторизации.
                 return
        # Сохранение учетных данных для следующего запуска
        try:
            with Path(TOKEN_FILE).open('w') as token: #  Открытие файла для записи токена.
                token.write(creds.to_json()) #  Запись токена в файл.
        except Exception as e:
             logger.error(f'Ошибка сохранения токена в файл {TOKEN_FILE}', exc_info=True) # Логирование ошибки сохранения токена.
             return
    try:
        service = build('script', 'v1', credentials=creds) #  Создание сервиса для работы с Apps Script API.
        # Вызов Apps Script API
        # Создание нового проекта
        request = {'title': 'My Script'}  #  Создание запроса на создание нового проекта.
        response = service.projects().create(body=request).execute() #  Отправка запроса на создание проекта.

        # Загрузка двух файлов в проект
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
        response = service.projects().updateContent(
            body=request,
            scriptId=response['scriptId']).execute() # Отправка запроса на обновление содержимого проекта.
        print('https://script.google.com/d/' + response['scriptId'] + '/edit') # Вывод URL созданного скрипта.

    except errors.HttpError as error:  # Обработка ошибок HTTP.
         logger.error(f'Ошибка HTTP при работе с Google Apps Script API: {error.content}', exc_info=True) # Логирование ошибки HTTP.
    except Exception as e:
        logger.error(f'Произошла ошибка: {e}', exc_info=True) # Логирование всех остальных ошибок.


if __name__ == '__main__':
    main()
```