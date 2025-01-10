# Анализ кода модуля `ftp.py`

**Качество кода**
9
- Плюсы
    - Код имеет подробную документацию к модулю и каждой функции.
    - Используется `logger` для логирования ошибок.
    - Присутствуют примеры использования функций.
    - Используются `type hints`.
    - Код достаточно читабельный и понятный.

- Минусы
    - Не используется `Path` из `pathlib` для `file_path` в функциях `write`, `read`, `delete`.
    -  Многократное использование блока `try-except` для закрытия сессии FTP.
    - `source_file_path` в функции `delete` не используется, это может запутать.

**Рекомендации по улучшению**
1.  Используйте `Path` для `file_path`.
2.  Вынесите код закрытия сессии FTP в отдельную функцию для уменьшения дублирования кода.
3.  Используйте `f-string` для форматирования строк логов, для лучшей читаемости.
4.  Удалите неиспользуемый параметр `source_file_path` из функции `delete` или явно укажите, что он не используется.

**Оптимизированный код**
```python
"""
Модуль для работы с FTP сервером
=========================================================================================

Этот модуль предоставляет интерфейс для взаимодействия с FTP серверами.
Включает функции для отправки, получения и удаления файлов с FTP-сервера.

**Назначение**:
Позволяет отправлять медиафайлы (изображения, видео), электронные таблицы и другие файлы
на FTP-сервер и с него.

**Модули**:
- helpers (local): Локальные вспомогательные утилиты для операций с FTP.
- typing: Подсказки типов для параметров функций и возвращаемых значений.
- ftplib: Предоставляет возможности FTP-клиента.
- pathlib: Для обработки путей файловой системы.

Функции:
    - `write`: Отправляет файл на FTP-сервер.
    - `read`: Получает файл с FTP-сервера.
    - `delete`: Удаляет файл с FTP-сервера.

Пример использования
--------------------

Пример использования функций модуля:

.. code-block:: python

    from pathlib import Path
    from src.utils import ftp
    file_path = Path('example.txt')
    with open(file_path, 'w') as f:
        f.write('example file')

    ftp.write(file_path, '/remote/directory', 'example.txt')
    content = ftp.read(file_path, '/remote/directory', 'example.txt')
    print(content)
    ftp.delete(file_path, '/remote/directory', 'example.txt')
"""
from src.logger.logger import logger
from typing import Union
import ftplib
from pathlib import Path

# Connection configuration (предполагается, что определена в другом месте)
_connection = {
    'server': 'ftp.example.com',
    'port': 21,
    'user': 'username',
    'password': 'password'
}

def _close_ftp_session(session: ftplib.FTP) -> None:
    """
    Закрывает FTP сессию и обрабатывает возможные ошибки.

    Args:
        session (ftplib.FTP): FTP сессия для закрытия.
    """
    try:
        session.quit()
    except Exception as ex:
        logger.error(f"Failed to close FTP session. Error: {ex}")


def write(source_file_path: str | Path, dest_dir: str, dest_file_name: str) -> bool:
    """
    Отправляет файл на FTP-сервер.

    Args:
        source_file_path (str | Path): Путь к файлу для отправки.
        dest_dir (str): Целевая директория на FTP-сервере.
        dest_file_name (str): Имя файла на FTP-сервере.

    Returns:
        bool: True, если файл успешно отправлен, иначе False.

    Example:
        >>> success = write('local_path/to/file.txt', '/remote/directory', 'file.txt')
        >>> print(success)
        True
    """
    try:
        # Код устанавливает соединение с FTP-сервером
        session = ftplib.FTP(
            _connection['server'],
            _connection['user'],
            _connection['password'])
        session.cwd(dest_dir)
    except Exception as ex:
        # Логирует ошибку, если не удалось установить соединение с FTP-сервером
        logger.error(f"Failed to connect to FTP server. Error: {ex}")
        return False

    try:
        # Код открывает файл и отправляет его на FTP-сервер
        with open(source_file_path, 'rb') as f:
            session.storbinary(f'STOR {dest_file_name}', f)
        return True
    except Exception as ex:
        # Логирует ошибку, если не удалось отправить файл на FTP-сервер
        logger.error(f"Failed to send file to FTP server. Error: {ex}")
        return False
    finally:
        # Код закрывает FTP-сессию
        _close_ftp_session(session)


def read(source_file_path: str | Path, dest_dir: str, dest_file_name: str) -> Union[str, bytes, None]:
    """
    Получает файл с FTP-сервера.

    Args:
        source_file_path (str | Path): Путь для сохранения файла локально.
        dest_dir (str): Директория на FTP-сервере, где находится файл.
        dest_file_name (str): Имя файла на FTP-сервере.

    Returns:
        Union[str, bytes, None]: Содержимое файла, если он успешно получен, иначе None.

    Example:
        >>> content = read('local_path/to/file.txt', '/remote/directory', 'file.txt')
        >>> print(content)
        b'Some file content'
    """
    try:
        # Код устанавливает соединение с FTP-сервером
        session = ftplib.FTP(
            _connection['server'],
            _connection['user'],
            _connection['password'])
        session.cwd(dest_dir)
        # Код получает файл
        with open(source_file_path, 'wb') as f:
            session.retrbinary(f'RETR {dest_file_name}', f.write)
        with open(source_file_path, 'rb') as f:
            return f.read()
    except Exception as ex:
        # Логирует ошибку, если не удалось получить файл с FTP-сервера
        logger.error(f"Failed to retrieve file from FTP server. Error: {ex}")
        return
    finally:
        # Код закрывает FTP-сессию
        _close_ftp_session(session)


def delete(dest_dir: str, dest_file_name: str) -> bool:
    """
    Удаляет файл с FTP-сервера.

    Args:
        dest_dir (str): Директория на FTP-сервере, где находится файл.
        dest_file_name (str): Имя файла на FTP-сервере.

    Returns:
        bool: True, если файл успешно удален, иначе False.

    Example:
        >>> success = delete('/remote/directory', 'file.txt')
        >>> print(success)
        True
    """
    try:
        # Код устанавливает соединение с FTP-сервером
        session = ftplib.FTP(
            _connection['server'],
            _connection['user'],
            _connection['password'])
        session.cwd(dest_dir)
        # Код удаляет файл
        session.delete(dest_file_name)
        return True
    except Exception as ex:
        # Логирует ошибку, если не удалось удалить файл с FTP-сервера
        logger.error(f"Failed to delete file from FTP server. Error: {ex}")
        return False
    finally:
        # Код закрывает FTP-сессию
        _close_ftp_session(session)
```