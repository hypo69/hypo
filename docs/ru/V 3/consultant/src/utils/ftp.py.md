## Анализ кода модуля `ftp`

**Качество кода:**

- **Соответствие стандартам**: 7/10
- **Плюсы**:
  - Код хорошо документирован, есть примеры использования.
  - Используется модуль `logger` для логирования ошибок.
  - Функции достаточно простые и выполняют одну конкретную задачу.
- **Минусы**:
  - Параметры соединения FTP-сервера заданы как глобальная переменная `_connection`, что не является хорошей практикой.
  - В функции `delete` параметр `source_file_path` не используется, что может ввести в заблуждение.
  - Отсутствует обработка специфичных исключений `ftplib`, что может затруднить отладку.
  - Использование `Union` для возвращаемого значения функции `read`.
  - В блоках `except` не передается `exc_info=True` в `logger.error`, что не позволяет получить traceback ошибки.

**Рекомендации по улучшению:**

1. **Конфигурация FTP-соединения**:
   - Перенести параметры соединения FTP-сервера в конфигурационный файл (например, JSON) и читать их с помощью `j_loads` или `j_loads_ns`.
   - Реализовать класс для управления FTP-соединением, чтобы избежать дублирования кода.

2. **Обработка исключений**:
   - Добавить обработку специфичных исключений `ftplib` (например, `ftplib.error_perm`, `ftplib.error_temp`, `ftplib.error_proto`).
   - Добавить `exc_info=True` в `logger.error` для получения полной информации об ошибке.

3. **Улучшение функции `delete`**:
   - Убрать неиспользуемый параметр `source_file_path` из функции `delete`.

4. **Типизация**:
   - Заменить `Union[str, bytes, None]` в функции `read` на `str | bytes | None`.

5. **Документация**:
   - Добавить примеры обработки исключений в документацию функций.

**Оптимизированный код:**

```python
## \file /src/utils/ftp.py
# -*- coding: utf-8 -*-
#! .pyenv/bin/python3

"""
Модуль для взаимодействия с FTP серверами.
=================================================

Модуль предоставляет интерфейс для взаимодействия с FTP серверами, включая функции для отправки, получения и удаления файлов.

**Назначение:**
Позволяет отправлять и получать медиафайлы (изображения, видео), электронные таблицы и другие файлы с FTP сервера.

**Модули:**
- src.logger.logger: Модуль логирования.
- typing: Type hints для параметров функций и возвращаемых значений.
- ftplib: Предоставляет возможности FTP клиента.
- pathlib: Для работы с путями файловой системы.

Функции:
    - `write`: Отправляет файл на FTP сервер.
    - `read`: Получает файл с FTP сервера.
    - `delete`: Удаляет файл с FTP сервера.

Пример использования:
----------------------

>>> from pathlib import Path
>>> config = {'server': 'ftp.example.com', 'port': 21, 'user': 'username', 'password': 'password'}
>>> ftp_client = FTPClient(config)
>>> success = ftp_client.write('local_path/to/file.txt', '/remote/directory', 'file.txt')
>>> print(success)
True
"""

from src.logger.logger import logger
from typing import Optional
import ftplib
from pathlib import Path
from src.utils.jjson import j_loads

class FTPClient:
    """
    Класс для управления FTP-соединением.
    """
    def __init__(self, config_path: str | Path):
        """
        Инициализирует FTP клиент с параметрами из конфигурационного файла.

        Args:
            config_path (str | Path): Путь к конфигурационному файлу в формате JSON.
        """
        self._connection = j_loads(config_path)
        self.session: Optional[ftplib.FTP] = None # Объявление атрибута session

    def connect(self) -> None:
        """
        Устанавливает соединение с FTP сервером.
        """
        try:
            self.session = ftplib.FTP(
                self._connection['server'],
                self._connection['user'],
                self._connection['password'])
        except Exception as ex:
            logger.error(f'Failed to connect to FTP server. Error: {ex}', exc_info=True)
            raise

    def disconnect(self) -> None:
        """
        Закрывает соединение с FTP сервером.
        """
        try:
            if self.session:
                self.session.quit()
        except Exception as ex:
            logger.error(f'Failed to close FTP session. Error: {ex}', exc_info=True)

    def write(self, source_file_path: str, dest_dir: str, dest_file_name: str) -> bool:
        """
        Отправляет файл на FTP сервер.

        Args:
            source_file_path (str): Путь к файлу, который нужно отправить.
            dest_dir (str): Директория на FTP сервере, куда нужно отправить файл.
            dest_file_name (str): Имя файла на FTP сервере.

        Returns:
            bool: True, если файл успешно отправлен, False в противном случае.

        Raises:
            ftplib.error_perm: Если отсутствует доступ к директории или файлу.
            ftplib.error_temp: В случае временной ошибки соединения.
            Exception: В случае других ошибок.

        Example:
            >>> config = {'server': 'ftp.example.com', 'port': 21, 'user': 'username', 'password': 'password'}
            >>> ftp_client = FTPClient(config)
            >>> success = ftp_client.write('local_path/to/file.txt', '/remote/directory', 'file.txt')
            >>> print(success)
            True
        """
        try:
            self.connect()
            self.session.cwd(dest_dir)
            with open(source_file_path, 'rb') as f:
                self.session.storbinary(f'STOR {dest_file_name}', f)
            return True
        except ftplib.error_perm as ex:
            logger.error(f'Permission error while sending file to FTP server. Error: {ex}', exc_info=True)
            return False
        except ftplib.error_temp as ex:
            logger.error(f'Temporary error while sending file to FTP server. Error: {ex}', exc_info=True)
            return False
        except Exception as ex:
            logger.error(f'Failed to send file to FTP server. Error: {ex}', exc_info=True)
            return False
        finally:
            self.disconnect()

    def read(self, source_file_path: str, dest_dir: str, dest_file_name: str) -> str | bytes | None:
        """
        Получает файл с FTP сервера.

        Args:
            source_file_path (str): Путь, куда нужно сохранить полученный файл.
            dest_dir (str): Директория на FTP сервере, где находится файл.
            dest_file_name (str): Имя файла на FTP сервере.

        Returns:
            str | bytes | None: Содержимое файла, если успешно получен, None в противном случае.

        Raises:
            ftplib.error_perm: Если отсутствует доступ к директории или файлу.
            ftplib.error_temp: В случае временной ошибки соединения.
            Exception: В случае других ошибок.

        Example:
            >>> config = {'server': 'ftp.example.com', 'port': 21, 'user': 'username', 'password': 'password'}
            >>> ftp_client = FTPClient(config)
            >>> content = ftp_client.read('local_path/to/file.txt', '/remote/directory', 'file.txt')
            >>> print(content)
            b'Some file content'
        """
        try:
            self.connect()
            self.session.cwd(dest_dir)
            with open(source_file_path, 'wb') as f:
                self.session.retrbinary(f'RETR {dest_file_name}', f.write)
            with open(source_file_path, 'rb') as f:
                return f.read()
        except ftplib.error_perm as ex:
            logger.error(f'Permission error while retrieving file from FTP server. Error: {ex}', exc_info=True)
            return None
        except ftplib.error_temp as ex:
            logger.error(f'Temporary error while retrieving file from FTP server. Error: {ex}', exc_info=True)
            return None
        except Exception as ex:
            logger.error(f'Failed to retrieve file from FTP server. Error: {ex}', exc_info=True)
            return None
        finally:
            self.disconnect()

    def delete(self, dest_dir: str, dest_file_name: str) -> bool:
        """
        Удаляет файл с FTP сервера.

        Args:
            dest_dir (str): Директория на FTP сервере, где находится файл.
            dest_file_name (str): Имя файла на FTP сервере, который нужно удалить.

        Returns:
            bool: True, если файл успешно удален, False в противном случае.

        Raises:
            ftplib.error_perm: Если отсутствует доступ к директории или файлу.
            ftplib.error_temp: В случае временной ошибки соединения.
            Exception: В случае других ошибок.

        Example:
            >>> config = {'server': 'ftp.example.com', 'port': 21, 'user': 'username', 'password': 'password'}
            >>> ftp_client = FTPClient(config)
            >>> success = ftp_client.delete('/remote/directory', 'file.txt')
            >>> print(success)
            True
        """
        try:
            self.connect()
            self.session.cwd(dest_dir)
            self.session.delete(dest_file_name)
            return True
        except ftplib.error_perm as ex:
            logger.error(f'Permission error while deleting file from FTP server. Error: {ex}', exc_info=True)
            return False
        except ftplib.error_temp as ex:
            logger.error(f'Temporary error while deleting file from FTP server. Error: {ex}', exc_info=True)
            return False
        except Exception as ex:
            logger.error(f'Failed to delete file from FTP server. Error: {ex}', exc_info=True)
            return False
        finally:
            self.disconnect()

# Пример использования
if __name__ == '__main__':
    # Загрузка конфигурации из файла
    config_path = 'ftp_config.json'  # Укажите путь к вашему файлу конфигурации
    ftp_client = FTPClient(config_path)

    # Пример отправки файла
    source_file = 'local_file.txt'
    dest_dir = '/remote/directory'
    dest_file = 'remote_file.txt'
    try:
        success = ftp_client.write(source_file, dest_dir, dest_file)
        if success:
            print(f'File {source_file} successfully sent to {dest_dir}/{dest_file}')
        else:
            print(f'Failed to send file {source_file} to {dest_dir}/{dest_file}')

        # Пример получения файла
        local_file = 'local_received_file.txt'
        content = ftp_client.read(local_file, dest_dir, dest_file)
        if content:
            print(f'File {dest_dir}/{dest_file} successfully retrieved and saved to {local_file}')
        else:
            print(f'Failed to retrieve file {dest_dir}/{dest_file}')

        # Пример удаления файла
        success = ftp_client.delete(dest_dir, dest_file)
        if success:
            print(f'File {dest_dir}/{dest_file} successfully deleted')
        else:
            print(f'Failed to delete file {dest_dir}/{dest_file}')
    except Exception as ex:
        logger.error(f"An unexpected error occurred: {ex}", exc_info=True)
```
```json
# ftp_config.json
{
    "server": "ftp.example.com",
    "port": 21,
    "user": "username",
    "password": "password"
}