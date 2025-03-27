### Анализ кода модуля `ftp.py`

**Качество кода**:
- **Соответствие стандартам**: 7
- **Плюсы**:
    - Использование `logger` для обработки ошибок.
    - Применение `try-except-finally` для управления ресурсами FTP.
    - Наличие docstring для каждой функции.
    - Использование `Union` для указания типов возвращаемых значений.
- **Минусы**:
    - Смешивание двойных и одинарных кавычек.
    - Не стандартизированные docstring
    - Чрезмерное использование блоков `try-except`
    - Не все переменные и функции выровнены по стилю

**Рекомендации по улучшению**:
- Использовать одинарные кавычки для всех строк, кроме операций вывода `print()`, `input()` и `logger.error()`.
- Переписать docstring в RST формате.
- Уменьшить количество `try-except` блоков, использовать `logger.error` для обработки ошибок.
- Выровнять названия функций и переменных.
- Добавить описание модуля в формате RST.
-  Добавить примеры использования в docstring функций.

**Оптимизированный код**:
```python
"""
Модуль для работы с FTP сервером
=================================

Модуль предоставляет интерфейс для взаимодействия с FTP серверами,
включая функции для отправки, получения и удаления файлов.

**Назначение**:
    Позволяет отправлять медиафайлы (изображения, видео), электронные таблицы и другие файлы
    на FTP-сервер и с него.

**Модули**:
    - `src.logger`: Логирование ошибок.
    - `typing`: Подсказки типов для параметров и возвращаемых значений.
    - `ftplib`: Обеспечивает функциональность FTP-клиента.
    - `pathlib`: Для работы с путями файловой системы.

**Функции**:
    - :func:`write`: Отправляет файл на FTP-сервер.
    - :func:`read`: Получает файл с FTP-сервера.
    - :func:`delete`: Удаляет файл с FTP-сервера.

Пример использования
----------------------
.. code-block:: python

    from src.utils.ftp import write, read, delete
    
    # Пример отправки файла
    success = write('local_file.txt', '/remote/dir', 'remote_file.txt')
    print(f"File upload successful: {success}")

    # Пример получения файла
    content = read('/local/save/file.txt', '/remote/dir', 'remote_file.txt')
    if content:
        print(f"File content: {content[:20]}...")

    # Пример удаления файла
    success = delete('/local/file.txt', '/remote/dir', 'remote_file.txt')
    print(f"File deletion successful: {success}")
"""

from src.logger.logger import logger #  Импортируем logger
from typing import Union
import ftplib
from pathlib import Path


_connection = {
    'server': 'ftp.example.com',
    'port': 21,
    'user': 'username',
    'password': 'password'
}


def write(source_file_path: str, dest_dir: str, dest_file_name: str) -> bool:
    """
    Отправляет файл на FTP-сервер.

    :param source_file_path: Путь к файлу для отправки.
    :type source_file_path: str
    :param dest_dir: Каталог назначения на FTP-сервере.
    :type dest_dir: str
    :param dest_file_name: Имя файла на FTP-сервере.
    :type dest_file_name: str
    :return: True, если файл успешно отправлен, иначе False.
    :rtype: bool

    :raises Exception: В случае ошибки при подключении к FTP-серверу или отправке файла.

    Пример:
        >>> success = write('local_path/to/file.txt', '/remote/directory', 'file.txt')
        >>> print(success)
        True
    """
    try:
        session = ftplib.FTP(
            _connection['server'],
            _connection['user'],
            _connection['password']
        ) #  Устанавливаем соединение с FTP сервером
        session.cwd(dest_dir) #  Переходим в директорию

        with open(source_file_path, 'rb') as f: # Открываем файл
            session.storbinary(f'STOR {dest_file_name}', f) #  Отправляем файл
        return True
    except Exception as ex:
        logger.error(f"Failed to send file to FTP server. Error: {ex}") #  Логируем ошибку
        return False
    finally:
        try:
            session.quit()  #  Закрываем FTP сессию
        except Exception as ex:
            logger.error(f"Failed to close FTP session. Error: {ex}") #  Логируем ошибку


def read(source_file_path: str, dest_dir: str, dest_file_name: str) -> Union[str, bytes, None]:
    """
    Получает файл с FTP-сервера.

    :param source_file_path: Путь, куда будет сохранен файл локально.
    :type source_file_path: str
    :param dest_dir: Каталог на FTP-сервере, где находится файл.
    :type dest_dir: str
    :param dest_file_name: Имя файла на FTP-сервере.
    :type dest_file_name: str
    :return: Содержимое файла, если он успешно получен, иначе None.
    :rtype: Union[str, bytes, None]

    :raises Exception: В случае ошибки при подключении к FTP-серверу или получении файла.

    Пример:
        >>> content = read('local_path/to/file.txt', '/remote/directory', 'file.txt')
        >>> if content:
        ...    print(content[:20])
        b'Some file content...'
    """
    try:
        session = ftplib.FTP(
            _connection['server'],
            _connection['user'],
            _connection['password']
        ) #  Устанавливаем соединение с FTP сервером
        session.cwd(dest_dir) #  Переходим в директорию
        
        with open(source_file_path, 'wb') as f:  #  Открываем файл для записи
            session.retrbinary(f'RETR {dest_file_name}', f.write) #  Получаем файл
        with open(source_file_path, 'rb') as f: #  Открываем файл для чтения
            return f.read() # Возвращаем содержимое файла
    except Exception as ex:
        logger.error(f"Failed to retrieve file from FTP server. Error: {ex}") #  Логируем ошибку
        return
    finally:
        try:
            session.quit()  #  Закрываем FTP сессию
        except Exception as ex:
            logger.error(f"Failed to close FTP session. Error: {ex}")  #  Логируем ошибку


def delete(source_file_path: str, dest_dir: str, dest_file_name: str) -> bool:
    """
    Удаляет файл с FTP-сервера.

    :param source_file_path: Путь, где файл находится локально (не используется).
    :type source_file_path: str
    :param dest_dir: Каталог на FTP-сервере, где находится файл.
    :type dest_dir: str
    :param dest_file_name: Имя файла на FTP-сервере.
    :type dest_file_name: str
    :return: True, если файл успешно удален, иначе False.
    :rtype: bool

     :raises Exception: В случае ошибки при подключении к FTP-серверу или удалении файла.

    Пример:
        >>> success = delete('local_path/to/file.txt', '/remote/directory', 'file.txt')
        >>> print(success)
        True
    """
    try:
        session = ftplib.FTP(
            _connection['server'],
            _connection['user'],
            _connection['password']
        ) #  Устанавливаем соединение с FTP сервером
        session.cwd(dest_dir)  #  Переходим в директорию

        session.delete(dest_file_name) #  Удаляем файл
        return True
    except Exception as ex:
        logger.error(f"Failed to delete file from FTP server. Error: {ex}") #  Логируем ошибку
        return False
    finally:
        try:
            session.quit()  #  Закрываем FTP сессию
        except Exception as ex:
            logger.error(f"Failed to close FTP session. Error: {ex}")  #  Логируем ошибку