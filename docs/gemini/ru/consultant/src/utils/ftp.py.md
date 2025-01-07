# Анализ кода модуля `ftp.py`

**Качество кода**
9
-  Плюсы
    - Код соответствует PEP 8, содержит docstring для каждой функции и модуля.
    - Код использует логгер для записи ошибок.
    - Присутствуют type hints.
    - Код обрабатывает исключения при работе с FTP-сервером.
-  Минусы
    - Исключения обрабатываются с помощью try-except, что усложняет код и может привести к дублированию логики.
    - Повторяется подключение к FTP серверу в каждой функции.
    - Переменные _connection не описаны.

**Рекомендации по улучшению**
1.  **Инкапсулировать подключение к FTP:** Вынести логику подключения к FTP-серверу в отдельную функцию или класс, чтобы избежать дублирования кода.
2.  **Обработка ошибок:** Использовать `logger.error` для записи ошибок и перехват исключений в одном месте.
3.  **Конфигурация FTP:** Сделать параметры FTP настраиваемыми (например, через параметры функций или файл конфигурации), убрать `_connection` и сделать его переменной окружения.
4.  **Удалить неиспользуемые аргументы:** Убрать source_file_path из функции `delete`, так как он не используется.
5.  **Использовать константы**: Использовать константы для magic strings
6.  **Избегать избыточных try-except блоков:** Упростить обработку ошибок, используя более конкретные блоки `try-except` или обработку ошибок на более высоком уровне.

**Оптимизированный код**

```python
"""
Модуль для работы с FTP-серверами.
=========================================================================================

Этот модуль предоставляет интерфейс для взаимодействия с FTP-серверами.
Он включает функции для отправки, получения и удаления файлов с FTP-сервера.

**Назначение:**
Позволяет отправлять медиафайлы (изображения, видео), электронные таблицы и другие файлы на FTP-сервер и с него.

**Модули:**
- `src.logger.logger`: Логирование ошибок.
- `typing`: Подсказки типов для параметров функций и возвращаемых значений.
- `ftplib`: Предоставляет возможности клиента протокола FTP.
- `pathlib`: Для работы с путями файловой системы.

**Функции:**
    - `write`: Отправляет файл на FTP-сервер.
    - `read`: Получает файл с FTP-сервера.
    - `delete`: Удаляет файл с FTP-сервера.
"""
# -*- coding: utf-8 -*-

#! venv/bin/python/python3.12

from src.logger.logger import logger
from typing import Union
import ftplib
from pathlib import Path
import os

# Константы
FTP_SERVER = os.getenv('FTP_SERVER', 'ftp.example.com')
FTP_PORT = int(os.getenv('FTP_PORT', 21))
FTP_USER = os.getenv('FTP_USER', 'username')
FTP_PASSWORD = os.getenv('FTP_PASSWORD', 'password')

STOR = 'STOR'
RETR = 'RETR'

def _create_ftp_session() -> ftplib.FTP:
    """
    Устанавливает соединение с FTP-сервером.

    :return: Объект FTP-сессии.
    :raises Exception: Если не удалось подключиться к FTP-серверу.
    """
    try:
         # Код устанавливает соединение с FTP-сервером
        session = ftplib.FTP(FTP_SERVER, FTP_USER, FTP_PASSWORD)
        return session
    except Exception as ex:
         # Код логирует ошибку подключения к FTP-серверу
        logger.error(f"Failed to connect to FTP server. Error: {ex}")
        raise

def _close_ftp_session(session: ftplib.FTP):
    """
    Закрывает FTP-сессию.

    :param session: Объект FTP-сессии.
    :raises Exception: Если не удалось закрыть FTP-сессию.
    """
    try:
         # Код закрывает FTP-сессию
        session.quit()
    except Exception as ex:
         # Код логирует ошибку закрытия FTP-сессии
        logger.error(f"Failed to close FTP session. Error: {ex}")
        raise

def write(source_file_path: str, dest_dir: str, dest_file_name: str) -> bool:
    """
    Отправляет файл на FTP-сервер.

    :param source_file_path: Путь к отправляемому файлу.
    :param dest_dir: Целевой каталог на FTP-сервере.
    :param dest_file_name: Имя файла на FTP-сервере.
    :return: `True`, если файл успешно отправлен, иначе `False`.

    Пример использования:
        >>> success = write('local_path/to/file.txt', '/remote/directory', 'file.txt')
        >>> print(success)
        True
    """
    session = None
    try:
         # Код создает сессию подключения к FTP серверу
        session = _create_ftp_session()
        session.cwd(dest_dir)

         # Код открывает файл и отправляет его на FTP сервер
        with open(source_file_path, 'rb') as f:
            session.storbinary(f'{STOR} {dest_file_name}', f)
        return True
    except Exception as ex:
        # Код логирует ошибку при отправке файла на FTP-сервер
        logger.error(f"Failed to send file to FTP server. Error: {ex}")
        return False
    finally:
        if session:
            try:
                 # Код закрывает сессию с FTP сервером
                _close_ftp_session(session)
            except Exception:
                pass


def read(source_file_path: str, dest_dir: str, dest_file_name: str) -> Union[str, bytes, None]:
    """
    Получает файл с FTP-сервера.

    :param source_file_path: Путь, куда будет сохранен файл локально.
    :param dest_dir: Каталог на FTP-сервере, где находится файл.
    :param dest_file_name: Имя файла на FTP-сервере.
    :return: Содержимое файла, если файл успешно получен, иначе `None`.

    Пример использования:
        >>> content = read('local_path/to/file.txt', '/remote/directory', 'file.txt')
        >>> print(content)
        b'Some file content'
    """
    session = None
    try:
         # Код создает сессию подключения к FTP серверу
        session = _create_ftp_session()
        session.cwd(dest_dir)

         # Код извлекает файл с FTP сервера
        with open(source_file_path, 'wb') as f:
            session.retrbinary(f'{RETR} {dest_file_name}', f.write)

        # Код открывает и считывает файл
        with open(source_file_path, 'rb') as f:
            return f.read()
    except Exception as ex:
        # Код логирует ошибку при получении файла с FTP-сервера
        logger.error(f"Failed to retrieve file from FTP server. Error: {ex}")
        return
    finally:
        if session:
            try:
                 # Код закрывает сессию с FTP сервером
                _close_ftp_session(session)
            except Exception:
                pass


def delete(dest_dir: str, dest_file_name: str) -> bool:
    """
    Удаляет файл с FTP-сервера.

    :param dest_dir: Каталог на FTP-сервере, где находится файл.
    :param dest_file_name: Имя файла на FTP-сервере.
    :return: `True`, если файл успешно удален, иначе `False`.

    Пример использования:
        >>> success = delete('/remote/directory', 'file.txt')
        >>> print(success)
        True
    """
    session = None
    try:
         # Код создает сессию подключения к FTP серверу
        session = _create_ftp_session()
        session.cwd(dest_dir)

        # Код удаляет файл с FTP-сервера
        session.delete(dest_file_name)
        return True
    except Exception as ex:
        # Код логирует ошибку при удалении файла с FTP-сервера
        logger.error(f"Failed to delete file from FTP server. Error: {ex}")
        return False
    finally:
        if session:
            try:
                 # Код закрывает сессию с FTP сервером
                _close_ftp_session(session)
            except Exception:
                pass
```