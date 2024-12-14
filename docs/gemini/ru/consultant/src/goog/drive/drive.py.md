# Анализ кода модуля `drive.py`

**Качество кода**
7
-  Плюсы
    - Код использует  библиотеку `googleapiclient` для работы с Google Drive API.
    - Присутствует  базовая структура для загрузки файла на Google Drive.
    - Используется `pickle` для сохранения и загрузки токена доступа, что позволяет избежать повторной авторизации.
    - Код использует `Path` из библиотеки `pathlib` для работы с путями файлов.
-  Минусы
    -  Отсутствует обработка ошибок при загрузке файла.
    -  Не используется `logger` для отладки и логирования ошибок.
    -  Код содержит неиспользуемые импорты и дубликаты импортов.
    -  Файл содержит избыточные комментарии в начале, которые не имеют отношения к описанию модуля.
    -  Отсутствует описание в формате reStructuredText для модуля, классов и методов.
    -  Метод `upload_file` не реализован, а содержит лишь комментарий-заглушку.
    -  Используется прямой `print` вместо `logger` для вывода информации о файлах.
    - Имя `creds_file` не определено. Предположительно, должно использовать `creds_file = gs.path.secrets  / 'hypo69-c32c8736ca62.json'` но  `self.creds_file` используется в методе `_create_credentials` до его определения.
    - Не используется `j_loads` или `j_loads_ns` из `src.utils.jjson`.

**Рекомендации по улучшению**

1.  Добавить docstring в формате reStructuredText для модуля, класса `GoogleDriveHandler` и его методов.
2.  Реализовать метод `upload_file` с корректной загрузкой файла в Google Drive.
3.  Заменить `print` на `logger` для вывода информации о файлах.
4.  Использовать `logger` для логирования ошибок и отладки.
5.  Удалить дублирующиеся импорты и неиспользуемые импорты.
6.  Использовать `j_loads` или `j_loads_ns` из `src.utils.jjson` вместо стандартного `pickle.load` для чтения файла с токеном, если это необходимо.
7.  Обрабатывать ошибки при загрузке файла, используя `try-except` и логирование ошибок через `logger.error`.
8.  Исправить ошибку с `creds_file` и правильно передавать его в метод `_create_credentials`.
9.  Добавить проверку наличия токена перед попыткой его загрузки.
10.  Избегать использования `...` в коде, за исключением мест, где это действительно необходимо как указание на точку остановки.
11. Добавить проверку, что файл для загрузки существует.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
"""
Модуль для работы с Google Drive.
=========================================================================================

Этот модуль предоставляет класс :class:`GoogleDriveHandler` для управления файлами в Google Drive.
Он позволяет загружать файлы на Google Drive, используя API Google Drive v3.

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
from googleapiclient.discovery import build
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow

from src import gs
from src.logger.logger import logger
from src.utils.jjson import j_loads_ns


class GoogleDriveHandler:
    """
    Класс для управления файлами в Google Drive.

    :param folder_name: Имя папки в Google Drive, в которую будут загружаться файлы.
    """
    def __init__(self, folder_name: str):
        """
        Инициализирует обработчик Google Drive.
        """
        self.folder_name = folder_name
        self.creds = self._create_credentials()

    def _create_credentials(self) -> Credentials:
        """
        Создает или загружает учетные данные для доступа к Google Drive API.

        :return: Объект Credentials с учетными данными.
        """
        creds_file: Path = gs.path.secrets / 'hypo69-c32c8736ca62.json'
        SCOPES: list = ['https://www.googleapis.com/auth/drive']
        creds = None
        # Проверяем существует ли файл с токеном
        if os.path.exists('token.pickle'):
             # Пытаемся загрузить токен
            try:
                with open('token.pickle', 'rb') as token:
                    creds = pickle.load(token)
            except Exception as ex:
                 # Если не удалось загрузить токен, логируем ошибку
                logger.error(f'Ошибка при загрузке токена из файла token.pickle: {ex}')
                return None

        # Проверяем, валидны ли учетные данные
        if not creds or not creds.valid:
            # Если учетные данные есть, но они истекли, пытаемся их обновить
            if creds and creds.expired and creds.refresh_token:
                try:
                    creds.refresh(Request())
                except Exception as ex:
                    # Если обновление не удалось, логируем ошибку
                    logger.error(f'Ошибка при обновлении токена: {ex}')
                    return None
            else:
                # Если учетных данных нет или они недействительны, запускаем процесс аутентификации
                flow = InstalledAppFlow.from_client_secrets_file(
                    str(creds_file), SCOPES)
                try:
                    creds = flow.run_local_server(port=0)
                except Exception as ex:
                    # Если аутентификация не удалась, логируем ошибку
                    logger.error(f'Ошибка при аутентификации: {ex}')
                    return None
                # Сохраняем новые учетные данные
                try:
                    with open('token.pickle', 'wb') as token:
                        pickle.dump(creds, token)
                except Exception as ex:
                    # Если не удалось сохранить токен, логируем ошибку
                    logger.error(f'Ошибка при сохранении токена в файл token.pickle: {ex}')
                    return None
        return creds

    def upload_file(self, file_path: Path):
        """
        Загружает файл на Google Drive в указанную папку.

        :param file_path: Путь к файлу, который нужно загрузить.
        """
        if not file_path.exists():
            logger.error(f'Файл не найден: {file_path}')
            return
        service = build('drive', 'v3', credentials=self.creds)
        file_metadata = {'name': file_path.name,
                         'parents': [self.folder_name]} #TODO реализовать поиск папки по имени
        try:
            # Открываем файл для чтения в бинарном режиме
            with open(file_path, 'rb') as file_content:
                 # Загружаем файл в Google Drive
                 file = service.files().create(body=file_metadata,
                                                     media_body=file_content).execute()
            logger.info(f'Файл "{file_path.name}" успешно загружен на Google Drive. ID файла: {file.get("id")}')
        except Exception as ex:
              # Логируем ошибку, если не удалось загрузить файл
            logger.error(f'Ошибка при загрузке файла "{file_path}": {ex}')


def main():
    """
    Демонстрирует базовое использование Drive v3 API.
    """
    #  Создаём экземпляр GoogleDriveHandler
    drive_handler = GoogleDriveHandler(folder_name='My Drive Folder') #TODO заменить на получение имени папки
    # Получаем учетные данные
    creds = drive_handler.creds
    # Создаем сервис Google Drive API
    service = build('drive', 'v3', credentials=creds)

    try:
       #  Получаем список файлов
        results = service.files().list(
            pageSize=10, fields="nextPageToken, files(id, name)").execute()
        items = results.get('files', [])
        # Проверяем, есть ли файлы
        if not items:
            logger.info('Файлы не найдены.')
        else:
            logger.info('Файлы:')
            # Выводим список файлов
            for item in items:
                logger.info(f'{item["name"]} ({item["id"]})')

    except Exception as ex:
          #  Логируем ошибку при работе с API
        logger.error(f'Ошибка при работе с Google Drive API: {ex}')


if __name__ == '__main__':
    main()
```