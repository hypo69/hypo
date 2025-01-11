### Анализ кода модуля `ftp`

**Качество кода**:

- **Соответствие стандартам**: 7/10
- **Плюсы**:
    - Код в целом функционален и выполняет задачи по работе с FTP-сервером.
    - Используется `ftplib` для FTP-соединений.
    - Присутствуют docstring для функций, описывающие их назначение и использование.
    - Используется `logger` для регистрации ошибок.
- **Минусы**:
    - Не всегда соблюдается стиль написания кавычек: в коде используются двойные кавычки, тогда как необходимо использовать одинарные, за исключением `print` и `logger`.
    - Конфигурация FTP-соединения определена как глобальная переменная `_connection`, что не является оптимальным подходом, так как это может привести к проблемам при работе с несколькими серверами одновременно.
    - Обработка ошибок чрезмерно использует `try-except`, что делает код менее читаемым.
    - В функции `delete` параметр `source_file_path` не используется, что может запутать пользователей.
    - Нет проверки существования директории при записи и чтении файла.

**Рекомендации по улучшению**:

- **Использование кавычек**: Заменить двойные кавычки на одинарные везде, где это требуется, кроме `print` и `logger`.
- **Конфигурация FTP**: Вынести конфигурацию FTP-соединения в параметры функций, чтобы можно было работать с разными серверами.
- **Обработка ошибок**: Упростить блоки `try-except`, используя `logger.error` для обработки исключений.
- **Параметры функций**: Удалить неиспользуемый параметр `source_file_path` из функции `delete`.
- **Проверка директорий**: Добавить проверку на существование директории на сервере перед выполнением операций записи и чтения.
- **RST-документация**: Добавить **RST** документацию для модуля.
- **Улучшения в оформлении**: Добавить пустую строку перед блоком `try`, после блока `try` и перед `finally`

**Оптимизированный код**:

```python
"""
Модуль для работы с FTP-сервером
===================================

Этот модуль предоставляет функции для взаимодействия с FTP-сервером, включая отправку, получение и удаление файлов.

Модули
-------
- :mod:`src.logger.logger`: Модуль для логирования ошибок.
- :mod:`typing`: Модуль для аннотации типов.
- :mod:`ftplib`: Модуль для работы с FTP-протоколом.
- :mod:`pathlib`: Модуль для работы с путями к файлам.

Функции
--------
- :func:`write`: Отправляет файл на FTP-сервер.
- :func:`read`: Получает файл с FTP-сервера.
- :func:`delete`: Удаляет файл с FTP-сервера.

Примеры
--------
.. code-block:: python

   from src.utils.ftp import write, read, delete
   from pathlib import Path

   # Пример записи файла
   file_path = Path('local_file.txt')
   with open(file_path, 'w') as f:
       f.write('Это тестовый файл')

   write(
       source_file_path=str(file_path),
       dest_dir='/remote/dir',
       dest_file_name='file.txt',
       server='ftp.example.com',
       user='user',
       password='password'
   )

   # Пример чтения файла
   content = read(
       source_file_path='local_file_copy.txt',
       dest_dir='/remote/dir',
       dest_file_name='file.txt',
       server='ftp.example.com',
       user='user',
       password='password'
   )

   # Пример удаления файла
   delete(
       dest_dir='/remote/dir',
       dest_file_name='file.txt',
       server='ftp.example.com',
       user='user',
       password='password'
   )

"""
from src.logger.logger import logger  #  Импорт логгера
from typing import Union  #  Импорт для аннотации типов
import ftplib  #  Импорт для работы с FTP
from pathlib import Path  #  Импорт для работы с путями


def write(
    source_file_path: str,
    dest_dir: str,
    dest_file_name: str,
    server: str,
    user: str,
    password: str,
) -> bool:
    """
    Отправляет файл на FTP-сервер.

    :param source_file_path: Путь к файлу, который нужно отправить.
    :type source_file_path: str
    :param dest_dir: Директория на FTP-сервере, куда нужно отправить файл.
    :type dest_dir: str
    :param dest_file_name: Имя файла на FTP-сервере.
    :type dest_file_name: str
    :param server: Адрес FTP-сервера.
    :type server: str
    :param user: Имя пользователя для FTP-сервера.
    :type user: str
    :param password: Пароль для FTP-сервера.
    :type password: str
    :return: True, если файл успешно отправлен, иначе False.
    :rtype: bool
    :raises Exception: Если не удается установить соединение или отправить файл.

    Пример:
        >>> from pathlib import Path
        >>> file_path = Path('local_file.txt')
        >>> with open(file_path, 'w') as f:
        ...    f.write('test')
        >>> result = write(
        ...    source_file_path=str(file_path),
        ...    dest_dir='/remote/dir',
        ...    dest_file_name='file.txt',
        ...    server='ftp.example.com',
        ...    user='user',
        ...    password='password'
        ... )
        >>> print(result)
        True
    """
    try:
        # Устанавливаем соединение с FTP-сервером
        session = ftplib.FTP(server, user, password)
        session.cwd(dest_dir)
    except Exception as ex:
        # Логируем ошибку, если не удалось подключиться к FTP-серверу
        logger.error(f"Failed to connect to FTP server. Error: {ex}")
        return False

    try:
        # Открываем файл и отправляем его на FTP-сервер
        with open(source_file_path, 'rb') as f:
            session.storbinary(f'STOR {dest_file_name}', f)
        return True
    except Exception as ex:
        # Логируем ошибку, если не удалось отправить файл на FTP-сервер
        logger.error(f"Failed to send file to FTP server. Error: {ex}")
        return False
    finally:
        try:
            # Закрываем сессию FTP
            session.quit()
        except Exception as ex:
            # Логируем ошибку, если не удалось закрыть FTP-сессию
            logger.error(f"Failed to close FTP session. Error: {ex}")


def read(
    source_file_path: str,
    dest_dir: str,
    dest_file_name: str,
    server: str,
    user: str,
    password: str,
) -> Union[str, bytes, None]:
    """
    Получает файл с FTP-сервера.

    :param source_file_path: Путь, куда нужно сохранить файл локально.
    :type source_file_path: str
    :param dest_dir: Директория на FTP-сервере, где расположен файл.
    :type dest_dir: str
    :param dest_file_name: Имя файла на FTP-сервере.
    :type dest_file_name: str
    :param server: Адрес FTP-сервера.
    :type server: str
    :param user: Имя пользователя для FTP-сервера.
    :type user: str
    :param password: Пароль для FTP-сервера.
    :type password: str
    :return: Содержимое файла, если успешно получен, иначе None.
    :rtype: Union[str, bytes, None]
    :raises Exception: Если не удается установить соединение или получить файл.

    Пример:
        >>> content = read(
        ...    source_file_path='local_file.txt',
        ...    dest_dir='/remote/dir',
        ...    dest_file_name='file.txt',
        ...    server='ftp.example.com',
        ...    user='user',
        ...    password='password'
        ... )
        >>> print(content)
        b'Some file content'
    """
    try:
        # Устанавливаем соединение с FTP-сервером
        session = ftplib.FTP(server, user, password)
        session.cwd(dest_dir)
    except Exception as ex:
        # Логируем ошибку, если не удалось подключиться к FTP-серверу
        logger.error(f"Failed to connect to FTP server. Error: {ex}")
        return

    try:
        # Получаем файл и сохраняем его локально
        with open(source_file_path, 'wb') as f:
            session.retrbinary(f'RETR {dest_file_name}', f.write)
        with open(source_file_path, 'rb') as f:
            return f.read()
    except Exception as ex:
        # Логируем ошибку, если не удалось получить файл с FTP-сервера
        logger.error(f"Failed to retrieve file from FTP server. Error: {ex}")
        return
    finally:
        try:
            # Закрываем сессию FTP
            session.quit()
        except Exception as ex:
            # Логируем ошибку, если не удалось закрыть FTP-сессию
            logger.error(f"Failed to close FTP session. Error: {ex}")


def delete(
    dest_dir: str,
    dest_file_name: str,
    server: str,
    user: str,
    password: str,
) -> bool:
    """
    Удаляет файл с FTP-сервера.

    :param dest_dir: Директория на FTP-сервере, где расположен файл.
    :type dest_dir: str
    :param dest_file_name: Имя файла на FTP-сервере.
    :type dest_file_name: str
    :param server: Адрес FTP-сервера.
    :type server: str
    :param user: Имя пользователя для FTP-сервера.
    :type user: str
    :param password: Пароль для FTP-сервера.
    :type password: str
    :return: True, если файл успешно удален, иначе False.
    :rtype: bool
    :raises Exception: Если не удается установить соединение или удалить файл.

    Пример:
        >>> result = delete(
        ...    dest_dir='/remote/dir',
        ...    dest_file_name='file.txt',
        ...    server='ftp.example.com',
        ...    user='user',
        ...    password='password'
        ... )
        >>> print(result)
        True
    """
    try:
        # Устанавливаем соединение с FTP-сервером
        session = ftplib.FTP(server, user, password)
        session.cwd(dest_dir)
    except Exception as ex:
        # Логируем ошибку, если не удалось подключиться к FTP-серверу
        logger.error(f"Failed to connect to FTP server. Error: {ex}")
        return False

    try:
        # Удаляем файл с FTP-сервера
        session.delete(dest_file_name)
        return True
    except Exception as ex:
        # Логируем ошибку, если не удалось удалить файл с FTP-сервера
        logger.error(f"Failed to delete file from FTP server. Error: {ex}")
        return False
    finally:
        try:
            # Закрываем сессию FTP
            session.quit()
        except Exception as ex:
            # Логируем ошибку, если не удалось закрыть FTP-сессию
            logger.error(f"Failed to close FTP session. Error: {ex}")