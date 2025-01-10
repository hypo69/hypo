# Анализ кода модуля `quickstart.py`

**Качество кода**
7
-   Плюсы
    -   Код выполняет поставленную задачу по созданию и обновлению скрипта Google Apps Script.
    -   Используется библиотека `google-api-python-client` для взаимодействия с API Google.
    -   Код обрабатывает аутентификацию и сохраняет токен.
    -   Присутствует обработка ошибок при взаимодействии с API.
-   Минусы
    -   Не хватает документации в формате RST для модуля и функций.
    -   Используется стандартный `print` для вывода, вместо `logger`.
    -   Используется  `json.load` вместо `j_loads` или `j_loads_ns`.
    -   Используются двойные кавычки в коде, хотя в инструкциях требуется одинарные.
    -   Не все импорты соответствуют ранее обработанным файлам.
    -   Отсутствует описание модуля.
    -   Не все переменные и функции соответствуют принятым соглашениям об именовании.
    -   Файл `token.json` создается в корне проекта, что не очень удобно.

**Рекомендации по улучшению**

1.  Добавить описание модуля в начале файла в формате RST.
2.  Добавить документацию к функции `main` в формате RST.
3.  Использовать `j_loads` или `j_loads_ns` из `src.utils.jjson` вместо `json.load`.
4.  Использовать `logger` из `src.logger.logger` для логирования ошибок и вывода информации.
5.  Переименовать переменные и функции в соответствии с принятыми соглашениями об именовании (например, использовать snake_case).
6.  Использовать одинарные кавычки в коде, где это требуется.
7.  Перенести файл `token.json` в директорию с временными файлами.
8.  Добавить более подробные комментарии к блокам кода.
9.  Удалить неиспользуемый импорт `header`.
10. Добавить обработку ошибок при создании и обновлении скрипта более подробно.
11.  Обрамить `SAMPLE_CODE` и `SAMPLE_MANIFEST` в тройные кавычки с префиксом `'''` для корректной работы с многострочными строками

**Оптимизированный код**

```python
"""
Модуль для взаимодействия с Google Apps Script API.
=========================================================================================

Этот модуль содержит функцию :func:`main`, которая используется для создания нового скрипта
Google Apps Script, загрузки файлов в проект и вывода URL-адреса скрипта.

Пример использования
--------------------

Пример использования функции `main`:

.. code-block:: python

    from src.goog.quickstart import main
    main()
"""

# -*- coding: utf-8 -*-

#! venv/bin/python/python3.12

from pathlib import Path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient import errors
from googleapiclient.discovery import build
from src.logger.logger import logger #  Импортируем logger
from src.utils.jjson import j_loads # Импорт j_loads
from src import gs

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/script.projects'] #  Список необходимых scopes

SAMPLE_CODE = '''
function helloWorld() {
  console.log("Hello, world!");
}
'''.strip() #  Код примера скрипта

SAMPLE_MANIFEST = '''
{
  "timeZone": "America/New_York",
  "exceptionLogging": "CLOUD"
}
'''.strip() #  Манифест примера скрипта


def main():
    """
    Выполняет взаимодействие с Apps Script API.

    Создает новый проект Apps Script, загружает в него файлы и выводит URL-адрес скрипта.

    Raises:
        googleapiclient.errors.HttpError: При возникновении ошибки при взаимодействии с API.
    """
    creds = None
    # Файл token.json хранит токены доступа пользователя, обновляется автоматически при первой
    # авторизации.
    token_path = gs.path.tmp / 'e-cat-346312-137284f4419e.json' #  Путь к файлу с токеном
    if token_path.exists():
        #  Проверяем существует ли файл с токеном
        try:
            creds = Credentials.from_authorized_user_file(str(token_path), SCOPES)
        except Exception as ex:
            logger.error(f'Ошибка при загрузке токена из файла: {token_path}', exc_info=ex)
            return

    # Если нет действительных учетных данных, предоставляем пользователю возможность войти.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            #  Если токен устарел, то обновляем его
            try:
                creds.refresh(Request())
            except Exception as ex:
                logger.error('Ошибка при обновлении токена', exc_info=ex)
                return
        else:
            # Если нет токена, то запускаем процесс авторизации
            try:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', SCOPES)
                creds = flow.run_local_server(port=0)
            except Exception as ex:
                 logger.error('Ошибка при авторизации', exc_info=ex)
                 return
        # Сохраняем учетные данные для следующего запуска.
        try:
            with (gs.path.tmp / 'token.json').open('w') as token:
               token.write(creds.to_json())
        except Exception as ex:
             logger.error('Ошибка при записи токена', exc_info=ex)
             return


    try:
        #  Создаем экземпляр сервиса для работы с Google Apps Script API
        service = build('script', 'v1', credentials=creds)

        # Вызываем Apps Script API
        # Создаем новый проект
        request = {'title': 'My Script'} #  Запрос на создание нового проекта
        try:
            response = service.projects().create(body=request).execute() #  Отправляем запрос на создание проекта
        except errors.HttpError as error:
            logger.error('Ошибка при создании проекта', exc_info=error)
            return
        # Загружаем два файла в проект
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
        } # Запрос на обновление проекта
        try:
            response = service.projects().updateContent(
                body=request,
                scriptId=response['scriptId']).execute() # Отправляем запрос на обновление проекта
        except errors.HttpError as error:
             logger.error('Ошибка при обновлении контента проекта', exc_info=error)
             return
        logger.info(f'https://script.google.com/d/{response["scriptId"]}/edit') #  Выводим URL скрипта

    except errors.HttpError as error:
        # API столкнулся с проблемой
        logger.error('API столкнулся с проблемой', exc_info=error)


if __name__ == '__main__':
    main()
```