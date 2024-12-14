# Анализ кода модуля `ftp`

**Качество кода**
8
-  Плюсы
    - Код содержит docstring для модуля и каждой функции, что улучшает понимание.
    - Используются `logger.error` для логирования ошибок.
    - Код структурирован и выполняет поставленные задачи.
    - Присутствуют примеры использования функций в docstring.
    - Обработка ошибок осуществляется через блоки `try-except`.
 -  Минусы
    -  Не используется `j_loads` или `j_loads_ns` из `src.utils.jjson` для чтения файлов. (В данном случае нет чтения файлов)
    -  Используются лишние блоки `try-except` для закрытия сессий FTP в блоке `finally`. Это можно упростить.
    -  Не используется `Path` для работы с путями.
    -  Используется глобальная переменная `_connection`, которую лучше сделать настраиваемой.
    -  В функции `delete` параметр `source_file_path` не используется.

**Рекомендации по улучшению**

1.  Удалить неиспользуемый параметр `source_file_path` из функции `delete`.
2.  Использовать `Path` для работы с путями.
3.  Упростить блок `finally`, объединив логирование и закрытие сессии.
4.  Перенести настройки соединения в параметры функций.
5.  Применить форматирование f-строк более последовательно.
6.  Обновить docstrings в соответствии с reStructuredText.
7.  Добавить проверку на существование файла перед его чтением в функции `read`.

**Оптимизированный код**

```python
"""
Модуль для работы с FTP сервером
=========================================================================================

Этот модуль предоставляет интерфейс для взаимодействия с FTP-серверами.
Он включает функции для отправки, получения и удаления файлов с FTP-сервера.

**Назначение**:
Позволяет отправлять медиафайлы (изображения, видео), электронные таблицы и другие файлы на FTP-сервер и получать их с него.

**Модули**:
- helpers (локальный): Локальные вспомогательные утилиты для операций FTP.
- typing: Подсказки типов для параметров функций и возвращаемых значений.
- ftplib: Предоставляет возможности клиента протокола FTP.
- pathlib: Для обработки путей файловой системы.

Функции:
    - `write`: Отправляет файл на FTP-сервер.
    - `read`: Получает файл с FTP-сервера.
    - `delete`: Удаляет файл с FTP-сервера.
"""
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12
MODE = 'dev'
from src.logger.logger import logger
from typing import Union, Dict
import ftplib
from pathlib import Path

def write(
    source_file_path: str,
    dest_dir: str,
    dest_file_name: str,
    connection: Dict = None
    ) -> bool:
    """
    Отправляет файл на FTP-сервер.

    :param source_file_path: Путь к файлу для отправки.
    :type source_file_path: str
    :param dest_dir: Целевой каталог на FTP-сервере.
    :type dest_dir: str
    :param dest_file_name: Имя файла на FTP-сервере.
    :type dest_file_name: str
    :param connection: Параметры подключения к FTP-серверу.
        Defaults to a predefined connection configuration if none is provided.
        Example:
            >>> connection = {
            ...     'server': 'ftp.example.com',
            ...     'port': 21,
            ...     'user': 'username',
            ...     'password': 'password'
            ... }
        :type connection: dict, optional
    :return: True, если файл успешно отправлен, иначе False.
    :rtype: bool

    :Example:
        >>> success = write('local_path/to/file.txt', '/remote/directory', 'file.txt')
        >>> print(success)
        True
    """
    if not connection:
        connection = {
            'server': 'ftp.example.com',
            'port': 21,
            'user': 'username',
            'password': 'password'
        }
    try:
        # Код устанавливает соединение с FTP-сервером
        session = ftplib.FTP(
            connection['server'],
            connection['user'],
            connection['password'])
        session.cwd(dest_dir)
    except Exception as ex:
        # Код записывает ошибку, если не удалось подключиться к FTP-серверу
        logger.error(f"Не удалось подключиться к FTP-серверу. Ошибка: {ex}")
        return False

    try:
        # Код открывает файл и отправляет его на FTP-сервер
        with open(source_file_path, 'rb') as f:
            session.storbinary(f'STOR {dest_file_name}', f)
        return True
    except Exception as ex:
        # Код записывает ошибку, если не удалось отправить файл на FTP-сервер
        logger.error(f"Не удалось отправить файл на FTP-сервер. Ошибка: {ex}")
        return False
    finally:
        # Код закрывает FTP-сессию и записывает ошибку если не удалось
        try:
            session.quit()
        except Exception as ex:
            logger.error(f"Не удалось закрыть FTP-сессию. Ошибка: {ex}")


def read(
    source_file_path: str,
    dest_dir: str,
    dest_file_name: str,
    connection: Dict = None
    ) -> Union[str, bytes, None]:
    """
    Получает файл с FTP-сервера.

    :param source_file_path: Путь, куда будет сохранен файл локально.
    :type source_file_path: str
    :param dest_dir: Каталог на FTP-сервере, где расположен файл.
    :type dest_dir: str
    :param dest_file_name: Имя файла на FTP-сервере.
    :type dest_file_name: str
    :param connection: Параметры подключения к FTP-серверу.
        Defaults to a predefined connection configuration if none is provided.
        Example:
            >>> connection = {
            ...     'server': 'ftp.example.com',
            ...     'port': 21,
            ...     'user': 'username',
            ...     'password': 'password'
            ... }
        :type connection: dict, optional
    :return: Содержимое файла, если файл успешно получен, иначе None.
    :rtype: Union[str, bytes, None]

    :Example:
        >>> content = read('local_path/to/file.txt', '/remote/directory', 'file.txt')
        >>> print(content)
        b'Some file content'
    """
    if not connection:
        connection = {
            'server': 'ftp.example.com',
            'port': 21,
            'user': 'username',
            'password': 'password'
        }

    try:
        # Код устанавливает соединение с FTP-сервером
        session = ftplib.FTP(
            connection['server'],
            connection['user'],
            connection['password'])
        session.cwd(dest_dir)

        # Проверка на существование файла
        try:
             session.size(dest_file_name)
        except Exception as ex:
             logger.error(f"Файл {dest_file_name} не найден на FTP-сервере. Ошибка: {ex}")
             return None
        # Код получает файл
        with open(source_file_path, 'wb') as f:
             session.retrbinary(f'RETR {dest_file_name}', f.write)
        with open(source_file_path, 'rb') as f:
             return f.read()
    except Exception as ex:
        # Код записывает ошибку, если не удалось получить файл с FTP-сервера
        logger.error(f"Не удалось получить файл с FTP-сервера. Ошибка: {ex}")
        return None
    finally:
        # Код закрывает FTP-сессию и записывает ошибку если не удалось
        try:
            session.quit()
        except Exception as ex:
            logger.error(f"Не удалось закрыть FTP-сессию. Ошибка: {ex}")

def delete(
    dest_dir: str,
    dest_file_name: str,
    connection: Dict = None
    ) -> bool:
    """
    Удаляет файл с FTP-сервера.

    :param dest_dir: Каталог на FTP-сервере, где расположен файл.
    :type dest_dir: str
    :param dest_file_name: Имя файла на FTP-сервере.
    :type dest_file_name: str
    :param connection: Параметры подключения к FTP-серверу.
        Defaults to a predefined connection configuration if none is provided.
        Example:
            >>> connection = {
            ...     'server': 'ftp.example.com',
            ...     'port': 21,
            ...     'user': 'username',
            ...     'password': 'password'
            ... }
        :type connection: dict, optional
    :return: True, если файл успешно удален, иначе False.
    :rtype: bool

    :Example:
        >>> success = delete('/remote/directory', 'file.txt')
        >>> print(success)
        True
    """
    if not connection:
        connection = {
            'server': 'ftp.example.com',
            'port': 21,
            'user': 'username',
            'password': 'password'
        }
    try:
        # Код устанавливает соединение с FTP-сервером
        session = ftplib.FTP(
            connection['server'],
            connection['user'],
            connection['password'])
        session.cwd(dest_dir)

        # Код удаляет файл
        session.delete(dest_file_name)
        return True
    except Exception as ex:
        # Код записывает ошибку, если не удалось удалить файл с FTP-сервера
        logger.error(f"Не удалось удалить файл с FTP-сервера. Ошибка: {ex}")
        return False
    finally:
        # Код закрывает FTP-сессию и записывает ошибку если не удалось
        try:
            session.quit()
        except Exception as ex:
            logger.error(f"Не удалось закрыть FTP-сессию. Ошибка: {ex}")
```