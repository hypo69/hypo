# Анализ кода модуля `drive.py`

**Качество кода**
**5/10**
-  Плюсы
    - Использование `pathlib` для работы с путями.
    - Применение `google-api-python-client` для взаимодействия с Google Drive API.
    -  Выделение логики работы с Google Drive в отдельный класс `GoogleDriveHandler`.
    - Использование `pickle` для сохранения и загрузки токена авторизации.

-  Минусы
    -  Наличие дублирующегося импорта модулей.
    - Некорректное использование docstring и отсутствие RST разметки.
    - Отсутствие обработки ошибок загрузки файла.
    - Жестко заданные пути к файлу с учетными данными и токену.
    - Несоответствие конвенциям именования: использование snake_case для переменных `SCOPES`.
    - Отсутствие логирования ошибок.
    -  Наличие лишнего кода и комментариев, а также неактуальных заголовков.

**Рекомендации по улучшению**
1.  Удалить дублирующиеся импорты и неиспользуемые импорты.
2.  Переписать docstring в формате reStructuredText (RST).
3.  Добавить обработку ошибок при создании учетных данных и загрузке файлов.
4.  Использовать переменные окружения или конфигурационный файл для хранения путей к файлу с учетными данными и токену.
5.  Использовать snake_case для переменных `SCOPES`.
6.  Добавить логирование ошибок с помощью `src.logger.logger`.
7.  Удалить лишние комментарии и неактуальные заголовки.
8.  Разделить функции на более мелкие и переиспользовать их при необходимости.
9.  Добавить описание к каждому параметру функции и возвращаемому значению.
10.  В блоке `if __name__ == '__main__':` вынести инициализацию класса в отдельную функцию.

**Оптимизированный код**
```python
# -*- coding: utf-8 -*-
"""
Модуль для работы с Google Drive.
=========================================================================================

Этот модуль предоставляет класс :class:`GoogleDriveHandler`, который используется для загрузки файлов
в Google Drive.

Пример использования
--------------------

Пример использования класса `GoogleDriveHandler`:

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
# from google_auth_httplib2 import AuthorizedHttpTransport  # Не используется, удаляем

from src import gs
# from src.utils.printer import pprint  # Не используется, удаляем
from src.logger.logger import logger

MODE = 'dev'


class GoogleDriveHandler:
    """
    Класс для взаимодействия с Google Drive.

    :param folder_name: Название папки в Google Drive, куда будут загружаться файлы.
    """
    def __init__(self, folder_name: str):
        """
        Инициализирует обработчик Google Drive.

        :param folder_name: Название папки в Google Drive, куда будут загружаться файлы.
        """
        self.folder_name = folder_name
        self.creds = self._create_credentials()

    def _create_credentials(self) -> Credentials:
        """
        Получает действительные учетные данные пользователя из хранилища.

        :return: Объект Credentials или None в случае ошибки.
        """
        creds_file: Path = gs.path.secrets / 'hypo69-c32c8736ca62.json'
        scopes: list = ['https://www.googleapis.com/auth/drive']
        creds = None
        token_file = 'token.pickle' # Выносим имя токена в переменную
        # Проверка наличия файла с токеном
        if os.path.exists(token_file):
            try:
                with open(token_file, 'rb') as token:
                    creds = pickle.load(token)
            except Exception as ex:
                logger.error(f'Ошибка загрузки токена из файла: {token_file}', exc_info=ex)
                return None

        # Проверка валидности токена
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
                        str(creds_file), scopes)
                    creds = flow.run_local_server(port=0)
                except Exception as ex:
                   logger.error(f'Ошибка создания токена из файла: {creds_file}', exc_info=ex)
                   return None
                try:
                    with open(token_file, 'wb') as token:
                        pickle.dump(creds, token)
                except Exception as ex:
                   logger.error(f'Ошибка сохранения токена в файл: {token_file}', exc_info=ex)
                   return None
        return creds

    def upload_file(self, file_path: Path) -> bool:
        """
        Загружает файл в указанную папку в Google Drive.

        :param file_path: Путь к файлу для загрузки.
        :return: True в случае успешной загрузки, False в противном случае.
        """
        if not self.creds:
            logger.error('Учетные данные не инициализированы')
            return False
        try:
            service = build('drive', 'v3', credentials=self.creds)
            # Проверяем, существует ли файл
            if not file_path.exists():
                logger.error(f'Файл не найден: {file_path}')
                return False

            # TODO: Проверку на наличие папки и ее создание
            file_metadata = {
                 'name': file_path.name,
                 'parents': [self.folder_name]
                 }
            media = googleapiclient.http.MediaFileUpload(str(file_path),
                                                        mimetype='application/octet-stream',
                                                        resumable=True)
            file = service.files().create(body=file_metadata,
                                                media_body=media,
                                                fields='id').execute()
            logger.info(f'Файл загружен: {file.get("id")}')
            return True
        except Exception as ex:
            logger.error(f'Ошибка загрузки файла: {file_path}', exc_info=ex)
            return False


def main():
    """
    Демонстрирует базовое использование Drive v3 API.
    """
    # Получаем учетные данные
    google_drive_handler = GoogleDriveHandler(folder_name='My Drive Folder')
    creds = google_drive_handler._create_credentials()
    if not creds:
        logger.error('Не удалось получить учетные данные для Google Drive')
        return
    try:
        # Создаем сервис
        service = build('drive', 'v3', credentials=creds)
    
        # Вызываем Drive v3 API
        results = service.files().list(
            pageSize=10, fields="nextPageToken, files(id, name)").execute()
        items = results.get('files', [])

        if not items:
            print('Файлы не найдены.')
        else:
            print('Файлы:')
            for item in items:
                print('{0} ({1})'.format(item['name'], item['id']))
    except Exception as ex:
         logger.error('Ошибка при вызове API Google Drive', exc_info=ex)


if __name__ == '__main__':
    main()
```