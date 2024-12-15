# Анализ кода модуля `ftp.py`

**Качество кода**
8
- Плюсы
    - Код содержит docstring для модуля и каждой функции, что упрощает понимание назначения кода.
    - Используется `logger` для логирования ошибок, что помогает в отладке и мониторинге.
    - Код структурирован и разбит на логические функции.
    - Присутствуют примеры использования функций в docstring.
- Минусы
    - В коде используются стандартные `try-except` блоки.
    - Не используется `j_loads` и `j_loads_ns` для загрузки json файлов.
    - Присутствует избыточное логирование ошибок при закрытии FTP сессии.
    - Параметр `source_file_path` не используется в функции `delete`.

**Рекомендации по улучшению**
1.  Заменить стандартные блоки `try-except` на обработку ошибок с помощью `logger.error`.
2.  Удалить ненужный параметр `source_file_path` из функции `delete`.
3.  Избегать избыточного логирования при закрытии FTP сессии, поскольку это обычно не является критической ошибкой.
4.  Устранить дублирование кода при подключении к FTP серверу в функциях `write`, `read`, `delete`, вынеся его в отдельную функцию.
5.  Переписать все комментарии в формате reStructuredText.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
Модуль для работы с FTP сервером
=========================================================================================

Этот модуль предоставляет интерфейс для взаимодействия с FTP серверами. 
Включает функции для отправки, получения и удаления файлов с FTP сервера.

**Назначение:**
    Позволяет отправлять медиафайлы (изображения, видео), электронные таблицы и другие файлы на FTP сервер и с него.

**Модули:**
    - helpers (local): Локальные вспомогательные утилиты для FTP операций.
    - typing: Подсказки типов для параметров функций и возвращаемых значений.
    - ftplib: Предоставляет возможности клиента протокола FTP.
    - pathlib: Для работы с путями файловой системы.

**Функции:**
    - `write`: Отправляет файл на FTP сервер.
    - `read`: Получает файл с FTP сервера.
    - `delete`: Удаляет файл с FTP сервера.
"""
MODE = 'dev'
from src.logger.logger import logger
from typing import Union
import ftplib
from pathlib import Path

# Connection configuration (предполагается, что определено в другом месте)
_connection = {
    'server': 'ftp.example.com',
    'port': 21,
    'user': 'username',
    'password': 'password'
}

def _connect_ftp() -> ftplib.FTP:
    """
    Устанавливает соединение с FTP сервером.

    :return: Объект FTP сессии.
    :raises Exception: Если не удалось установить соединение с FTP сервером.
    """
    try:
        #  Код устанавливает соединение с FTP сервером
        session = ftplib.FTP(
            _connection['server'],
            _connection['user'],
            _connection['password']
        )
        return session
    except Exception as ex:
        # Код логирует ошибку подключения к FTP серверу
        logger.error(f"Не удалось подключиться к FTP серверу. Ошибка: {ex}")
        raise

def write(source_file_path: str, dest_dir: str, dest_file_name: str) -> bool:
    """
    Отправляет файл на FTP сервер.

    :param source_file_path: Путь к файлу, который нужно отправить.
    :param dest_dir: Каталог назначения на FTP сервере.
    :param dest_file_name: Имя файла на FTP сервере.
    :return: True, если файл успешно отправлен, иначе False.
    
    :Example:
        >>> success = write('local_path/to/file.txt', '/remote/directory', 'file.txt')
        >>> print(success)
        True
    """
    try:
        # Код устанавливает соединение с FTP сервером
        session = _connect_ftp()
        session.cwd(dest_dir)
        # Код открывает файл и отправляет его на FTP сервер
        with open(source_file_path, 'rb') as f:
            session.storbinary(f'STOR {dest_file_name}', f)
        return True
    except Exception as ex:
        # Код логирует ошибку при отправке файла на FTP сервер
        logger.error(f"Не удалось отправить файл на FTP сервер. Ошибка: {ex}")
        return False
    finally:
        # Код закрывает FTP сессию
        try:
           session.quit()
        except Exception:
            pass


def read(source_file_path: str, dest_dir: str, dest_file_name: str) -> Union[str, bytes, None]:
    """
    Получает файл с FTP сервера.

    :param source_file_path: Путь, куда будет сохранен файл локально.
    :param dest_dir: Каталог на FTP сервере, где находится файл.
    :param dest_file_name: Имя файла на FTP сервере.
    :return: Содержимое файла, если успешно получен, иначе None.
    
    :Example:
        >>> content = read('local_path/to/file.txt', '/remote/directory', 'file.txt')
        >>> print(content)
        b'Some file content'
    """
    try:
        # Код устанавливает соединение с FTP сервером
        session = _connect_ftp()
        session.cwd(dest_dir)
         # Код получает файл с FTP сервера
        with open(source_file_path, 'wb') as f:
            session.retrbinary(f'RETR {dest_file_name}', f.write)
        with open(source_file_path, 'rb') as f:
            return f.read()
    except Exception as ex:
        # Код логирует ошибку при получении файла с FTP сервера
        logger.error(f"Не удалось получить файл с FTP сервера. Ошибка: {ex}")
        return None
    finally:
        # Код закрывает FTP сессию
        try:
            session.quit()
        except Exception:
            pass

def delete(dest_dir: str, dest_file_name: str) -> bool:
    """
    Удаляет файл с FTP сервера.

    :param dest_dir: Каталог на FTP сервере, где находится файл.
    :param dest_file_name: Имя файла на FTP сервере.
    :return: True, если файл успешно удален, иначе False.
    
    :Example:
        >>> success = delete('/remote/directory', 'file.txt')
        >>> print(success)
        True
    """
    try:
        # Код устанавливает соединение с FTP сервером
        session = _connect_ftp()
        session.cwd(dest_dir)
        # Код удаляет файл с FTP сервера
        session.delete(dest_file_name)
        return True
    except Exception as ex:
        # Код логирует ошибку при удалении файла с FTP сервера
        logger.error(f"Не удалось удалить файл с FTP сервера. Ошибка: {ex}")
        return False
    finally:
        # Код закрывает FTP сессию
        try:
            session.quit()
        except Exception:
           pass
```