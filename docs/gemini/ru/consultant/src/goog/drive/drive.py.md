# Анализ кода модуля `drive.py`

**Качество кода**
8
-  Плюсы
    - Код структурирован в класс `GoogleDriveHandler`, что обеспечивает инкапсуляцию функциональности.
    - Используются необходимые библиотеки для работы с Google Drive API.
    - Присутствует базовая обработка аутентификации через `token.pickle`.
    - Есть пример использования в `if __name__ == '__main__':`.
-  Минусы
    - Отсутствует полная реализация логики загрузки файлов.
    - Использованы глобальные константы, которые не объявлены в начале модуля.
    - Не все функции и методы имеют docstring.
    - Код содержит дублирование импортов.
    - Используется  `print` вместо `logger`.
    - `_create_credentials` не является статическим методом класса
     - Отсутствует проверка на существование директории `token.pickle`, из за чего при первом запуске может упасть.
    - Не хватает описания назначения переменных и аргументов.
    - Не используется `j_loads` или `j_loads_ns`.

**Рекомендации по улучшению**

1.  Добавить docstring для модуля, класса и методов с использованием reStructuredText (RST).
2.  Убрать дублирующиеся импорты.
3.  Использовать `logger` для вывода сообщений вместо `print`.
4.  Реализовать логику загрузки файла в методе `upload_file`.
5.  Устранить неиспользуемые переменные `MODE`.
6.  Уточнить работу с файлом `creds_file`
7.   Добавить `try-except` для обработки ошибок аутентификации и загрузки файлов.
8.   Перенести константы в начало модуля.
9.   Сделать метод `_create_credentials` статическим.
10.  Добавить обработку исключений для случаев, когда `token.pickle` отсутствует.
11. Убрать неиспользуемые комментарии и `#!`.
12. Добавить проверку на существование каталога для `token.pickle`.
13.   Добавить полное описание  переменных и аргументов

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
"""
Модуль для работы с Google Drive API.
========================================================

Этот модуль предоставляет класс :class:`GoogleDriveHandler` для загрузки файлов в Google Drive.
Аутентификация выполняется через файл `token.pickle`, в котором хранятся учетные данные пользователя.

Пример использования
--------------------

Пример загрузки файла в Google Drive:

.. code-block:: python

    from pathlib import Path

    file_path = Path('/mnt/data/google_extracted/sample_file.txt')
    folder_name = 'My Drive Folder'

    google_drive_handler = GoogleDriveHandler(folder_name=folder_name)
    google_drive_handler.upload_file(file_path)
"""

import os
import pickle
from pathlib import Path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

from src import gs
from src.logger.logger import logger

# Определяем константы
SCOPES = ['https://www.googleapis.com/auth/drive']
TOKEN_FILE = 'token.pickle'
SECRETS_FILE = gs.path.secrets / 'hypo69-c32c8736ca62.json'


class GoogleDriveHandler:
    """
    Класс для взаимодействия с Google Drive.

    :param folder_name: Имя папки в Google Drive, куда будут загружаться файлы.
    :type folder_name: str
    """

    def __init__(self, folder_name: str):
        """
        Инициализация обработчика Google Drive.

        :param folder_name: Имя папки в Google Drive.
        :type folder_name: str
        """
        self.folder_name = folder_name
        self.creds = self._create_credentials()
        self.service = build('drive', 'v3', credentials=self.creds)

    @staticmethod
    def _create_credentials():
        """
        Получает действительные учетные данные пользователя из хранилища.

        Метод проверяет наличие файла `token.pickle`. Если он есть, загружает учетные данные из него.
        Если файла нет или учетные данные недействительны, выполняется процесс аутентификации.
        Результатом является объект `Credentials` для работы с Google API.

        :return: Учетные данные Google Drive.
        :rtype: google.oauth2.credentials.Credentials
        """
        creds = None
        if os.path.exists(TOKEN_FILE):
            try:
                with open(TOKEN_FILE, 'rb') as token:
                    creds = pickle.load(token)
            except Exception as ex:
                logger.error(f'Ошибка загрузки токена из файла {TOKEN_FILE}', exc_info=ex)
                return None

        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                try:
                    creds.refresh(Request())
                except Exception as ex:
                     logger.error('Ошибка обновления токена', exc_info=ex)
                     return None
            else:
                 try:
                    flow = InstalledAppFlow.from_client_secrets_file(
                        str(SECRETS_FILE), SCOPES
                    )
                    creds = flow.run_local_server(port=0)
                 except Exception as ex:
                     logger.error('Ошибка создания flow для аутентификации', exc_info=ex)
                     return None
            try:
                with open(TOKEN_FILE, 'wb') as token:
                    pickle.dump(creds, token)
            except Exception as ex:
                 logger.error(f'Ошибка сохранения токена в файл {TOKEN_FILE}', exc_info=ex)
                 return None
        return creds

    def upload_file(self, file_path: Path):
        """
        Загружает файл в указанную папку Google Drive.

        :param file_path: Путь к файлу, который нужно загрузить.
        :type file_path: pathlib.Path
        """
        if not self.creds:
            logger.error('Отсутствуют учетные данные для Google Drive.')
            return

        try:
             # Проверяем, существует ли папка с указанным именем
            folder_id = self._get_folder_id()
            if not folder_id:
                logger.error(f'Папка с именем {self.folder_name} не найдена.')
                return

            # Загрузка файла
            file_metadata = {'name': file_path.name, 'parents': [folder_id]}
            media =  googleapiclient.http.MediaFileUpload(str(file_path), mimetype='application/octet-stream', resumable=True)
            file = self.service.files().create(body=file_metadata, media_body=media, fields='id').execute()
            logger.info(f'Файл {file_path.name} успешно загружен в Google Drive, id файла: {file.get("id")}')
        except Exception as ex:
            logger.error(f'Ошибка загрузки файла {file_path.name} в Google Drive', exc_info=ex)

    def _get_folder_id(self) -> str | None:
        """
        Получает ID папки в Google Drive по ее имени.

        :return: ID папки, если она найдена, иначе None.
        :rtype: str | None
        """
        try:
            # Поиск папки по имени
            query = f"mimeType='application/vnd.google-apps.folder' and name='{self.folder_name}'"
            results = self.service.files().list(q=query, fields="files(id)").execute()
            items = results.get('files', [])
            if items:
                return items[0].get('id')
            return None
        except Exception as ex:
            logger.error(f'Ошибка поиска папки {self.folder_name} в Google Drive', exc_info=ex)
            return None

def main():
    """Показывает базовое использование Drive v3 API."""
    # Инициализация GoogleDriveHandler
    google_drive = GoogleDriveHandler(folder_name='My Drive Folder')
    if not google_drive.creds:
        logger.error('Не удалось получить учетные данные Google Drive')
        return
    try:
        # Вызов Drive v3 API
        results = google_drive.service.files().list(pageSize=10, fields="nextPageToken, files(id, name)").execute()
        items = results.get('files', [])

        if not items:
            logger.info('Файлы не найдены.')
        else:
            logger.info('Файлы:')
            for item in items:
                logger.info(f'{item["name"]} ({item["id"]})')

    except Exception as ex:
        logger.error('Ошибка при обращении к Google Drive API', exc_info=ex)

if __name__ == '__main__':
    main()
```