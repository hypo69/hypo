# Анализ кода модуля `drive.py`

**Качество кода**
8
-  Плюсы
    - Код имеет базовую структуру для работы с Google Drive API.
    - Используются классы для организации функциональности.
    - Присутствует обработка учетных данных и токенов.
-  Минусы
    - Присутствует дублирование импортов.
    - Не используется `j_loads` или `j_loads_ns` для чтения файлов.
    - Отсутствует документация для функций, классов и переменных в формате RST.
    - Нет обработки исключений и логирования ошибок.
    - Не реализован метод `upload_file`.
    - Не используются константы для `SCOPES`, `token.pickle` и `creds_file`
    - В коде есть неиспользуемые импорты `header`, `src.gs`, `src.utils.printer.pprint`
    - Отсутсвует описание модуля в начале файла.

**Рекомендации по улучшению**

1.  **Удалить дублирующиеся импорты**: Следует убрать дубликаты импортов.
2.  **Использовать `j_loads`**: Заменить чтение `json` файла на  `j_loads` или `j_loads_ns`.
3.  **Добавить документацию**: Дополнить каждую функцию, метод и класс документацией в формате RST.
4.  **Реализовать логирование**: Использовать `logger.error` для записи ошибок, вместо `print`
5.  **Реализовать `upload_file`**: Дописать функциональность для загрузки файлов в Google Drive.
6.  **Удалить неиспользуемые импорты**: Убрать `header`, `src.gs`, `src.utils.printer.pprint` из импортов.
7.  **Использовать константы**: Определить константы для `SCOPES`, `token.pickle` и `creds_file`.
8.  **Добавить описание модуля**: В начало файла добавить описание модуля.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
"""
Модуль для работы с Google Drive API.
=========================================================================================

Этот модуль предоставляет класс :class:`GoogleDriveHandler`, который используется для
взаимодействия с Google Drive API, включая загрузку файлов.

Пример использования
--------------------

Пример использования класса `GoogleDriveHandler`:

.. code-block:: python

    from pathlib import Path

    file_path = Path('path/to/your/file.txt')
    folder_name = 'Your Drive Folder'

    drive_handler = GoogleDriveHandler(folder_name=folder_name)
    drive_handler.upload_file(file_path)
"""
import os
import pickle
from pathlib import Path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

from src.logger.logger import logger # Используем logger отсюда

# Constants
SCOPES = ['https://www.googleapis.com/auth/drive']
TOKEN_PICKLE = 'token.pickle'
CREDS_FILE = Path('secrets') / 'hypo69-c32c8736ca62.json'  # Путь к файлу с учетными данными

class GoogleDriveHandler:
    """
    Класс для обработки взаимодействия с Google Drive.

    Args:
        folder_name (str): Название папки в Google Drive.
    """
    def __init__(self, folder_name: str):
        """
        Инициализирует обработчик Google Drive.

        Args:
            folder_name (str): Название папки в Google Drive.
        """
        self.folder_name = folder_name
        self.creds = self._create_credentials()

    def _create_credentials(self) -> Credentials:
        """
        Создает учетные данные для работы с Google Drive API.

        Returns:
            Credentials: Учетные данные.
        """
        creds = None
        #  Проверка наличия файла с токеном
        if os.path.exists(TOKEN_PICKLE):
            try:
                with open(TOKEN_PICKLE, 'rb') as token:
                    creds = pickle.load(token)
            except Exception as ex:
                logger.error(f'Ошибка при загрузке токена из файла {TOKEN_PICKLE}: {ex}')
                return None
        # Проверяет валидность учетных данных
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                try:
                    creds.refresh(Request())
                except Exception as ex:
                     logger.error(f'Ошибка при обновлении токена: {ex}')
                     return None
            else:
                # Если нет токена или он не валиден, создаем flow для авторизации
                flow = InstalledAppFlow.from_client_secrets_file(
                    CREDS_FILE, SCOPES)
                try:
                    creds = flow.run_local_server(port=0)
                except Exception as ex:
                    logger.error(f'Ошибка при создании учетных данных из файла {CREDS_FILE}: {ex}')
                    return None
            # Сохраняем токен
            try:
                with open(TOKEN_PICKLE, 'wb') as token:
                    pickle.dump(creds, token)
            except Exception as ex:
                logger.error(f'Ошибка при сохранении токена в файл {TOKEN_PICKLE}: {ex}')
                return None
        return creds


    def upload_file(self, file_path: Path):
        """
        Загружает файл в Google Drive.

        Args:
            file_path (Path): Путь к файлу для загрузки.

        .. todo::
           Реализовать логику загрузки файла в указанную папку
        """
        if not isinstance(file_path, Path):
            logger.error(f'Ожидался тип Path, получен {type(file_path)}')
            return False
        if not file_path.exists():
            logger.error(f'Файл не найден: {file_path}')
            return False
        logger.info(f'Загрузка файла: {file_path} в папку {self.folder_name}')

        service = build('drive', 'v3', credentials=self.creds)
        try:
             # Запрос списка папок, что бы найти нашу папку
            results = service.files().list(q=f"mimeType='application/vnd.google-apps.folder' and name='{self.folder_name}'",
                                                fields="files(id, name)").execute()
            items = results.get('files', [])
            if not items:
                 logger.error(f'Папка не найдена: {self.folder_name}')
                 return False
            folder_id = items[0]['id']
            file_metadata = {'name': file_path.name, 'parents': [folder_id]}
            #  Загрузка файла
            media = googleapiclient.http.MediaFileUpload(str(file_path), resumable=True)
            file = service.files().create(body=file_metadata, media_body=media, fields='id').execute()
            logger.info(f"Файл загружен: {file.get('id')}")
            return True
        except Exception as ex:
            logger.error(f'Ошибка при загрузке файла: {ex}')
            return False

def main():
    """
    Демонстрирует основное использование Drive v3 API.
    """
    # Создание учетных данных с помощью класса GoogleDriveHandler
    creds = GoogleDriveHandler(folder_name='My Drive Folder')._create_credentials() # папка по умолчанию
    if not creds:
        logger.error('Не удалось получить учетные данные')
        return

    service = build('drive', 'v3', credentials=creds)

    # Вызов Drive v3 API
    try:
        results = service.files().list(
            pageSize=10, fields="nextPageToken, files(id, name)").execute()
        items = results.get('files', [])
        if not items:
            print('No files found.')
        else:
             print('Files:')
             for item in items:
                print('{0} ({1})'.format(item['name'], item['id']))
    except Exception as ex:
          logger.error(f'Ошибка при получении списка файлов: {ex}')



if __name__ == '__main__':
    main()