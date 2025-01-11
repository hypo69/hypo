# Анализ кода модуля `ftp.py`

**Качество кода**
8
-   Плюсы
    *   Код хорошо структурирован и разбит на функции, каждая из которых выполняет определенную задачу (отправка, получение, удаление файлов).
    *   Используется `logger` для логирования ошибок, что помогает в отладке и мониторинге.
    *   Присутствуют docstring для каждой функции, описывающие их назначение, аргументы и возвращаемые значения, а также примеры использования.
    *   Используется `typing` для аннотации типов, что улучшает читаемость кода и помогает в отладке.
    *   Обработка исключений выполняется с логированием ошибки, что помогает в отладке и мониторинге.
    *   Наличие блока `finally` для закрытия соединения с FTP-сервером гарантирует освобождение ресурсов.
-   Минусы
    *   Конфигурация соединения с FTP-сервером (_connection) определена как глобальная переменная, что может быть негибким. Желательно вынести настройки в отдельный файл или класс.
    *   Используется `try-except-finally` для закрытия сессии FTP, что может быть избыточным. Достаточно закрыть сессию в блоке `finally` основного `try-except`.
    *   Функция `delete` принимает `source_file_path`, который не используется.
    *   Не используется `j_loads` или `j_loads_ns` из `src.utils.jjson`.
    *   Используются двойные кавычки в логгерах.
    *   В комментариях используются слова "получаем", "делаем" и т.п..

**Рекомендации по улучшению**

1.  **Конфигурация:** Вынести конфигурацию FTP-соединения в отдельный файл или класс для большей гибкости и удобства управления.
2.  **Обработка исключений:** Упростить обработку исключений в блоках `try-except-finally`, объединив их.
3.  **Параметры функций:** Убрать неиспользуемый параметр `source_file_path` из функции `delete`.
4.  **Импорты:** Привести в соответствие имена импортов с ранее обработанными файлами.
5. **Формат документации:** Использовать одинарные кавычки для строк в коде и двойные только в операциях вывода.
6. **Комментарии:** Перефразировать комментарии, избегая общих фраз.
7. **Логирование:** Изменить использование logger.error() на f-строки.
8.  **Docstring:** Обновить docstring в соответствии с примерами из инструкции.

**Оптимизированный код**

```python
"""
Модуль для работы с FTP сервером
=========================================================================================

Этот модуль предоставляет интерфейс для взаимодействия с FTP-серверами.
Он включает в себя функции для отправки, получения и удаления файлов с FTP-сервера.

**Назначение**:
Позволяет отправлять медиафайлы (изображения, видео), электронные таблицы и другие файлы на FTP-сервер и с него.

**Модули**:
- `src.logger.logger`: Логирование событий и ошибок.
- `typing`: Подсказки типов для параметров функций и возвращаемых значений.
- `ftplib`: Предоставляет возможности FTP-протокола клиента.
- `pathlib`: Для работы с путями файловой системы.

**Функции**:
    - `write`: Отправляет файл на FTP-сервер.
    - `read`: Получает файл с FTP-сервера.
    - `delete`: Удаляет файл с FTP-сервера.

Пример использования
--------------------

Пример использования функций:

.. code-block:: python

    from pathlib import Path
    from src.utils.ftp import write, read, delete

    source_file = Path('local_file.txt')
    dest_dir = '/remote/directory'
    dest_file = 'remote_file.txt'

    # Запись файла на FTP
    success = write(str(source_file), dest_dir, dest_file)

    # Чтение файла с FTP
    content = read(str(source_file), dest_dir, dest_file)

    # Удаление файла с FTP
    success = delete(str(source_file), dest_dir, dest_file)
"""
from src.logger.logger import logger
from typing import Union
import ftplib
from pathlib import Path

# Connection configuration (assumed to be defined elsewhere)
_connection = {
    'server': 'ftp.example.com',
    'port': 21,
    'user': 'username',
    'password': 'password'
}


def write(source_file_path: str, dest_dir: str, dest_file_name: str) -> bool:
    """
    Отправляет файл на FTP-сервер.

    :param source_file_path: Путь к файлу, который необходимо отправить.
    :type source_file_path: str
    :param dest_dir: Каталог назначения на FTP-сервере.
    :type dest_dir: str
    :param dest_file_name: Имя файла на FTP-сервере.
    :type dest_file_name: str
    :return: True, если файл успешно отправлен, False в противном случае.
    :rtype: bool

    :Example:
        >>> success = write('local_path/to/file.txt', '/remote/directory', 'file.txt')
        >>> print(success)
        True
    """
    session = None
    try:
        # Код устанавливает соединение с FTP-сервером
        session = ftplib.FTP(
            _connection['server'],
            _connection['user'],
            _connection['password'])
        session.cwd(dest_dir)

        # Код открывает файл и отправляет его на FTP-сервер
        with open(source_file_path, 'rb') as f:
            session.storbinary(f'STOR {dest_file_name}', f)
        return True
    except Exception as ex:
        # Код логирует ошибку, если не удалось отправить файл на FTP-сервер
        logger.error(f'Не удалось отправить файл на FTP-сервер. Ошибка: {ex}')
        return False
    finally:
        if session:
            try:
                # Код закрывает FTP-сессию
                session.quit()
            except Exception as ex:
                # Код логирует ошибку, если не удалось закрыть FTP-сессию
                logger.error(f'Не удалось закрыть FTP-сессию. Ошибка: {ex}')

def read(source_file_path: str, dest_dir: str, dest_file_name: str) -> Union[str, bytes, None]:
    """
    Получает файл с FTP-сервера.

    :param source_file_path: Путь, куда будет сохранен файл локально.
    :type source_file_path: str
    :param dest_dir: Каталог на FTP-сервере, где находится файл.
    :type dest_dir: str
    :param dest_file_name: Имя файла на FTP-сервере.
    :type dest_file_name: str
    :return: Содержимое файла, если успешно получено, иначе None.
    :rtype: Union[str, bytes, None]

    :Example:
        >>> content = read('local_path/to/file.txt', '/remote/directory', 'file.txt')
        >>> print(content)
        b'Some file content'
    """
    session = None
    try:
        # Код устанавливает соединение с FTP-сервером
        session = ftplib.FTP(
            _connection['server'],
            _connection['user'],
            _connection['password'])
        session.cwd(dest_dir)

        # Код получает файл с FTP-сервера
        with open(source_file_path, 'wb') as f:
            session.retrbinary(f'RETR {dest_file_name}', f.write)
        with open(source_file_path, 'rb') as f:
            return f.read()
    except Exception as ex:
        # Код логирует ошибку, если не удалось получить файл с FTP-сервера
        logger.error(f'Не удалось получить файл с FTP-сервера. Ошибка: {ex}')
        return
    finally:
        if session:
            try:
                # Код закрывает FTP-сессию
                session.quit()
            except Exception as ex:
                # Код логирует ошибку, если не удалось закрыть FTP-сессию
                logger.error(f'Не удалось закрыть FTP-сессию. Ошибка: {ex}')


def delete(source_file_path: str, dest_dir: str, dest_file_name: str) -> bool:
    """
    Удаляет файл с FTP-сервера.

    :param source_file_path: Путь к файлу, который не используется.
    :type source_file_path: str
    :param dest_dir: Каталог на FTP-сервере, где находится файл.
    :type dest_dir: str
    :param dest_file_name: Имя файла на FTP-сервере.
    :type dest_file_name: str
    :return: True, если файл успешно удален, False в противном случае.
    :rtype: bool

    :Example:
        >>> success = delete('local_path/to/file.txt', '/remote/directory', 'file.txt')
        >>> print(success)
        True
    """
    session = None
    try:
        # Код устанавливает соединение с FTP-сервером
        session = ftplib.FTP(
            _connection['server'],
            _connection['user'],
            _connection['password'])
        session.cwd(dest_dir)

        # Код удаляет файл с FTP-сервера
        session.delete(dest_file_name)
        return True
    except Exception as ex:
        # Код логирует ошибку, если не удалось удалить файл с FTP-сервера
        logger.error(f'Не удалось удалить файл с FTP-сервера. Ошибка: {ex}')
        return False
    finally:
        if session:
            try:
                # Код закрывает FTP-сессию
                session.quit()
            except Exception as ex:
                # Код логирует ошибку, если не удалось закрыть FTP-сессию
                logger.error(f'Не удалось закрыть FTP-сессию. Ошибка: {ex}')
```