# Анализ кода модуля `ftp.py`

**Качество кода**
7
- Плюсы
    - Код имеет docstring для модуля и каждой функции, что соответствует требованиям.
    - Используется `logger` для логирования ошибок.
    - Присутствуют type hints для параметров функций.
    - Код разделен на функции `write`, `read` и `delete`, каждая из которых выполняет свою задачу.
- Минусы
    - Конфигурация FTP-соединения `_connection` жестко задана и не может быть легко изменена.
    - Повторяющийся код для установки и закрытия FTP-соединения.
    - Функция `delete` принимает `source_file_path`, но не использует его.
    - Избыточное использование try-except блоков.
    - Отсутствует проверка наличия файла на локальной системе в функциях `read` и `write`.

**Рекомендации по улучшению**
1.  **Улучшение конфигурации**: Вынести конфигурацию FTP-соединения в отдельный файл или сделать ее настраиваемой через параметры функций, чтобы повысить гибкость и управляемость.
2.  **Рефакторинг повторяющегося кода**: Создать вспомогательную функцию для открытия и закрытия FTP-соединения, чтобы избежать дублирования кода.
3.  **Удаление лишнего параметра**: Убрать неиспользуемый параметр `source_file_path` из функции `delete`.
4.  **Обработка ошибок**: Использовать `try-except` блоки более рационально и обрабатывать только специфичные исключения.
5.  **Добавить проверку файла**: В функциях `read` и `write` перед открытием файла проверять его наличие на локальной системе.
6.  **Обновление docstring**: Пересмотреть docstring для соответствия reStructuredText.
7.  **Добавить импорты**: Добавить все необходимые импорты.

**Оптимизированный код**
```python
"""
Модуль для работы с FTP-серверами
=========================================================================================

Этот модуль предоставляет интерфейс для взаимодействия с FTP-серверами.
Он включает в себя функции для отправки, получения и удаления файлов с FTP-сервера.

**Назначение**:
Позволяет отправлять медиафайлы (изображения, видео), электронные таблицы и другие файлы на FTP-сервер и получать их с него.

**Модули**:
- `src.logger.logger`: Логирование ошибок и событий.
- `typing`: Подсказки типов для параметров и возвращаемых значений.
- `ftplib`: Предоставляет возможности клиента FTP-протокола.
- `pathlib`: Для обработки путей файловой системы.

Функции:
    - `write`: Отправляет файл на FTP-сервер.
    - `read`: Получает файл с FTP-сервера.
    - `delete`: Удаляет файл с FTP-сервера.
"""
# -*- coding: utf-8 -*-

#! venv/bin/python/python3.12
import ftplib
from pathlib import Path
from typing import Union
from src.logger.logger import logger
import os



# Connection configuration (assumed to be defined elsewhere)
_connection = {
    'server': 'ftp.example.com',
    'port': 21,
    'user': 'username',
    'password': 'password'
}


def _ftp_connect():
    """
    Устанавливает соединение с FTP-сервером.

    :return: Объект FTP-соединения.
    :rtype: ftplib.FTP
    :raises ftplib.all_errors: Если не удается установить соединение.
    """
    try:
        session = ftplib.FTP(
            _connection['server'],
            _connection['user'],
            _connection['password']
        )
        return session
    except Exception as ex:
        logger.error(f"Не удалось установить соединение с FTP-сервером. Ошибка: {ex}")
        raise


def _ftp_close(session: ftplib.FTP):
    """
    Закрывает FTP-соединение.

    :param session: Объект FTP-соединения.
    :type session: ftplib.FTP
    """
    try:
        session.quit()
    except Exception as ex:
        logger.error(f"Не удалось закрыть FTP-сессию. Ошибка: {ex}")


def write(source_file_path: str, dest_dir: str, dest_file_name: str) -> bool:
    """
    Отправляет файл на FTP-сервер.

    :param source_file_path: Путь к файлу, который необходимо отправить.
    :type source_file_path: str
    :param dest_dir: Целевая директория на FTP-сервере.
    :type dest_dir: str
    :param dest_file_name: Имя файла на FTP-сервере.
    :type dest_file_name: str
    :return: True, если файл успешно отправлен, иначе False.
    :rtype: bool

    Пример::

        >>> success = write('local_path/to/file.txt', '/remote/directory', 'file.txt')
        >>> print(success)
        True
    """
    # Проверка наличия файла перед открытием
    if not os.path.exists(source_file_path):
        logger.error(f"Файл не найден: {source_file_path}")
        return False
    session = None
    try:
        # Устанавливает соединение с FTP-сервером
        session = _ftp_connect()
        session.cwd(dest_dir)
        # Открывает файл и отправляет его на FTP-сервер
        with open(source_file_path, 'rb') as f:
            session.storbinary(f'STOR {dest_file_name}', f)
        return True
    except Exception as ex:
        # Логирует ошибку, если не удается отправить файл на FTP-сервер
        logger.error(f"Не удалось отправить файл на FTP-сервер. Ошибка: {ex}")
        return False
    finally:
        # Закрывает FTP-сессию
        if session:
            _ftp_close(session)

def read(source_file_path: str, dest_dir: str, dest_file_name: str) -> Union[str, bytes, None]:
    """
    Получает файл с FTP-сервера.

    :param source_file_path: Путь, по которому будет сохранен файл локально.
    :type source_file_path: str
    :param dest_dir: Директория на FTP-сервере, где находится файл.
    :type dest_dir: str
    :param dest_file_name: Имя файла на FTP-сервере.
    :type dest_file_name: str
    :return: Содержимое файла, если он успешно получен, иначе None.
    :rtype: Union[str, bytes, None]

    Пример::

        >>> content = read('local_path/to/file.txt', '/remote/directory', 'file.txt')
        >>> print(content)
        b'Some file content'
    """
    session = None
    try:
        # Устанавливает соединение с FTP-сервером
        session = _ftp_connect()
        session.cwd(dest_dir)

        # Получает файл
        with open(source_file_path, 'wb') as f:
            session.retrbinary(f'RETR {dest_file_name}', f.write)
        with open(source_file_path, 'rb') as f:
            return f.read()
    except Exception as ex:
        # Логирует ошибку, если не удается получить файл с FTP-сервера
        logger.error(f"Не удалось получить файл с FTP-сервера. Ошибка: {ex}")
        return None
    finally:
        # Закрывает FTP-сессию
        if session:
            _ftp_close(session)


def delete(dest_dir: str, dest_file_name: str) -> bool:
    """
    Удаляет файл с FTP-сервера.

    :param dest_dir: Директория на FTP-сервере, где находится файл.
    :type dest_dir: str
    :param dest_file_name: Имя файла на FTP-сервере.
    :type dest_file_name: str
    :return: True, если файл успешно удален, иначе False.
    :rtype: bool

    Пример::

        >>> success = delete('/remote/directory', 'file.txt')
        >>> print(success)
        True
    """
    session = None
    try:
        # Устанавливает соединение с FTP-сервером
        session = _ftp_connect()
        session.cwd(dest_dir)

        # Удаляет файл
        session.delete(dest_file_name)
        return True
    except Exception as ex:
        # Логирует ошибку, если не удается удалить файл с FTP-сервера
        logger.error(f"Не удалось удалить файл с FTP-сервера. Ошибка: {ex}")
        return False
    finally:
        # Закрывает FTP-сессию
        if session:
            _ftp_close(session)
```