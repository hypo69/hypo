# Анализ кода модуля `file_async.py`

**Качество кода:**

-   **Соответствие требованиям:** 7/10
    -   **Плюсы:**
        -   Код хорошо структурирован, функции имеют docstring.
        -   Используется `asyncio` и `aiofiles` для асинхронных операций.
        -   Есть обработка ошибок с использованием `logger.error`.
        -   Используются генераторы для чтения файлов.
        -   Много полезных функций для работы с файлами и директориями.
    -   **Минусы:**
        -   Не используется `j_loads` или `j_loads_ns` из `src.utils.jjson`.
        -   Не везде используется `from src.logger.logger import logger`.
        -   Есть избыточное использование `try-except` в некоторых местах.
        -   В docstring есть неточности в описании возвращаемых типов данных.
        -   Используется `os.walk`, что не соответствует асинхронной природе модуля.
        -   Не везде в функциях есть проверка на то, является ли путь файлом или директорией.

**Рекомендации по улучшению:**

1.  **Импорты:**
    -   Добавить импорт `from src.utils.jjson import j_loads` или `j_loads_ns`, где это необходимо.
    -   Использовать `from src.logger.logger import logger` для логирования.

2.  **Обработка JSON:**
    -   Использовать `j_loads` или `j_loads_ns` вместо `json.loads` при чтении JSON файлов.

3.  **Логирование:**
    -   Удалить избыточные `try-except` блоки и использовать `logger.error` для обработки ошибок.

4.  **Документация:**
    -   Уточнить docstring для функций `read_text_file`, `yield_text_from_files`, `recursively_read_text_files`, `recursively_get_file_path`,  указав корректные возвращаемые значения.
    -   Добавить примеры использования для всех функций.
    -   Добавить описание исключений, которые могут быть выброшены.

5.  **Асинхронность:**
    -   Заменить `os.walk` на `asyncio.gather` в функции `recursively_read_text_files`, для асинхронной работы.

6.  **Код:**
    -   Добавить проверки на то, является ли путь файлом или директорией, там где это необходимо.

7. **Общее:**
    - Привести в соответствие имена функций, переменных и импортов с ранее обработанными файлами.
    - Переписать комментарии для соответствия гайдлайну.

**Оптимизированный код:**

```python
# -*- coding: utf-8 -*-
#! venv/bin/python/python3.12
"""
Модуль для работы с файлами.
=========================================================================================

Модуль содержит набор утилит для выполнения асинхронных операций с файлами, таких как сохранение, чтение,
и получение списков файлов. Поддерживает обработку больших файлов с использованием генераторов
для экономии памяти.

Пример использования
--------------------

.. code-block:: python

    from pathlib import Path
    from src.utils.file_async import read_text_file, save_text_file
    from src.logger.logger import logger

    file_path = Path('example.txt')
    content = await read_text_file(file_path)
    if content:
        print(f'File content: {content[:100]}...')

    await save_text_file(file_path, 'Новый текст')
"""
import os
import fnmatch
import asyncio
import aiofiles
import aiofiles.os
from pathlib import Path
from typing import List, Optional, Union, AsyncGenerator
from src.logger.logger import logger
from src.utils.jjson import j_loads  # Импорт j_loads

MODE = 'dev'  # Константа режима


async def save_text_file(
    file_path: str | Path,
    data: str | list[str] | dict,
    mode: str = 'w'
) -> bool:
    """
    Асинхронно сохраняет данные в текстовый файл.

    Args:
        file_path (str | Path): Путь к файлу для сохранения.
        data (str | list[str] | dict): Данные для записи.
        mode (str, optional): Режим записи файла ('w' для записи, 'a' для добавления).
            Defaults to 'w'.

    Returns:
        bool: True, если файл успешно сохранен, False в противном случае.

    Raises:
        Exception: При возникновении ошибки при записи в файл.

    Example:
        >>> from pathlib import Path
        >>> file_path = Path('example.txt')
        >>> data = 'Пример текста'
        >>> result = await save_text_file(file_path, data)
        >>> print(result)
        True
    """
    try:
        # Преобразование пути к типу Path
        file_path = Path(file_path)
        # Создание родительской директории, если она не существует
        await aiofiles.os.makedirs(file_path.parent, exist_ok=True)
        # Открытие файла для записи
        async with aiofiles.open(file_path, mode, encoding='utf-8') as file:
            # Код обрабатывает список строк для записи
            if isinstance(data, list):
                for line in data:
                  await file.write(f'{line}\n')
            # Код обрабатывает словарь для записи в формате JSON
            elif isinstance(data, dict):
                await file.write(j_loads(data, ensure_ascii=False, indent=4))
            # Код обрабатывает строку для записи
            else:
                await file.write(data)
        return True
    except Exception as ex:
        #  Логирование ошибки при сохранении файла
        logger.error(f'Ошибка при сохранении файла {file_path}.', ex)
        return False


async def read_text_file(
    file_path: str | Path,
    as_list: bool = False,
    extensions: Optional[list[str]] = None,
    chunk_size: int = 8192,
    recursive: bool = False,
    patterns: Optional[str | list[str]] = None,
) -> AsyncGenerator[str, None] | str | list[str] | None:
    """
    Асинхронно читает содержимое файла(ов) или директории.

    Args:
        file_path (str | Path): Путь к файлу или директории.
        as_list (bool, optional): Если `True`, то возвращает генератор строк или список строк, в зависимости от типа вывода.
            Defaults to False.
        extensions (list[str], optional): Список расширений файлов для включения при чтении директории.
            Defaults to None.
        chunk_size (int, optional): Размер чанка для чтения файла в байтах.
            Defaults to 8192.
        recursive (bool, optional): Если `True`, то поиск файлов выполняется рекурсивно.
            Defaults to False.
        patterns (str | list[str], optional): Шаблоны для фильтрации файлов при рекурсивном поиске.
            Defaults to None.

    Returns:
         AsyncGenerator[str, None] | str | list[str] | None:
         - Если `as_list` is True и `file_path` является файлом, возвращает асинхронный генератор строк.
         - Если `as_list` is True и `file_path` является директорией и `recursive` is True, возвращает асинхронный генератор строк.
         - Если `as_list` is False и `file_path` является файлом, возвращает строку.
         - Если `as_list` is False и `file_path` является директорией, возвращает объединенную строку.
         - Возвращает `None` в случае ошибки.

    Raises:
         Exception: При возникновении ошибки при чтении файла.

    Example:
        >>> from pathlib import Path
        >>> file_path = Path('example.txt')
        >>> content = await read_text_file(file_path)
        >>> if content:
        ...    print(f'File content: {content[:100]}...')
        File content: Пример текста...

    """
    try:
        # Преобразование пути к типу Path
        path = Path(file_path)
        # Проверка, является ли путь файлом
        if path.is_file():
            # Код возвращает генератор строк, если as_list=True
            if as_list:
                return _read_file_lines_generator(path, chunk_size=chunk_size)
            # Код возвращает содержимое файла в виде строки
            else:
                return await _read_file_content(path, chunk_size=chunk_size)
        # Проверка, является ли путь директорией
        elif path.is_dir():
            # Код обрабатывает рекурсивный поиск файлов
            if recursive:
                if patterns:
                    files = await recursively_get_file_path(path, patterns)
                else:
                    files = [
                        p for p in path.rglob('*') if p.is_file() and (not extensions or p.suffix in extensions)
                    ]
                # Код возвращает генератор строк из всех файлов
                if as_list:
                  return (
                        line
                        async for file in files
                        async for line in yield_text_from_files(file, as_list=True, chunk_size=chunk_size)
                    )
                # Код возвращает объединенную строку из всех файлов
                else:
                   contents = await asyncio.gather(*[read_text_file(p, chunk_size=chunk_size) for p in files])
                   return '\n'.join(filter(None, contents))
            # Код обрабатывает нерекурсивный поиск файлов
            else:
                files = [
                    p for p in path.iterdir() if p.is_file() and (not extensions or p.suffix in extensions)
                ]
                # Код возвращает генератор строк из файлов текущей директории
                if as_list:
                  return (line async for file in files async for line in read_text_file(file, as_list=True, chunk_size=chunk_size))
                # Код возвращает объединенную строку из файлов текущей директории
                else:
                  contents = await asyncio.gather(*[read_text_file(p, chunk_size=chunk_size) for p in files])
                  return '\n'.join(filter(None, contents))
        else:
            # Логирование ошибки, если путь не является файлом или директорией
            logger.error(f'Путь \'{file_path}\' не является файлом или директорией.')
            return None
    except Exception as ex:
        # Логирование ошибки при чтении файла/директории
        logger.error(f'Ошибка при чтении файла/директории {file_path}.', ex)
        return None


async def yield_text_from_files(
    file_path: str | Path,
    as_list: bool = False,
    chunk_size: int = 8192
) -> AsyncGenerator[str, None] | str | None:
    """
    Асинхронно читает содержимое файла и возвращает его в виде генератора строк или одной строки.

    Args:
        file_path (str | Path): Путь к файлу.
        as_list (bool, optional): Если True, возвращает генератор строк. Defaults to False.
        chunk_size (int, optional): Размер чанка для чтения файла в байтах. Defaults to 8192.

    Returns:
        AsyncGenerator[str, None] | str | None: Генератор строк, объединенная строка или None в случае ошибки.

    Yields:
        str: Строки из файла, если as_list is True.

    Example:
        >>> from pathlib import Path
        >>> file_path = Path('example.txt')
        >>> async for line in yield_text_from_files(file_path, as_list=True):
        ...     print(line)
        Первая строка файла
        Вторая строка файла
    """
    try:
        # Преобразование пути к типу Path
        path = Path(file_path)
         # Проверка, является ли путь файлом
        if path.is_file():
            # Код возвращает генератор строк, если as_list=True
            if as_list:
                 async for line in  _read_file_lines_generator(path, chunk_size=chunk_size):
                   yield line
            # Код возвращает содержимое файла в виде строки
            else:
               yield await _read_file_content(path, chunk_size=chunk_size)
        else:
            # Логирование ошибки, если путь не является файлом
            logger.error(f'Путь \'{file_path}\' не является файлом.')
    except Exception as ex:
        # Логирование ошибки при чтении файла
        logger.error(f'Ошибка при чтении файла {file_path}.', ex)


async def _read_file_content(file_path: Path, chunk_size: int) -> str:
    """
    Асинхронно читает содержимое файла по чанкам и возвращает как строку.

    Args:
        file_path (Path): Путь к файлу для чтения.
        chunk_size (int): Размер чанка для чтения файла в байтах.

    Returns:
        str: Содержимое файла в виде строки.

    Raises:
        Exception: При возникновении ошибки при чтении файла.
    """
    try:
        content = ''
        # Открытие файла для чтения
        async with aiofiles.open(file_path, 'r', encoding='utf-8') as f:
            # Код читает файл по чанкам
            while True:
                chunk = await f.read(chunk_size)
                if not chunk:
                    break
                content += chunk
        return content
    except Exception as ex:
         # Логирование ошибки при чтении файла
         logger.error(f'Ошибка при чтении файла {file_path}.', ex)
         return ''


async def _read_file_lines_generator(file_path: Path, chunk_size: int) -> AsyncGenerator[str, None]:
    """
    Асинхронно читает файл по строкам с помощью генератора.

    Args:
        file_path (Path): Путь к файлу для чтения.
        chunk_size (int): Размер чанка для чтения файла в байтах.

    Yields:
        str: Строки из файла.

    Raises:
        Exception: При возникновении ошибки при чтении файла.
    """
    try:
        # Открытие файла для чтения
        async with aiofiles.open(file_path, 'r', encoding='utf-8') as f:
             # Код читает файл по чанкам
            while True:
                chunk = await f.read(chunk_size)
                # Если чанк пустой, чтение закончено
                if not chunk:
                    break
                 # Разделение чанка на строки
                lines = chunk.splitlines()
                 # Код проверяет, не является ли конец чанка концом строки
                if len(lines) > 0 and not chunk.endswith('\n'):
                  next_chunk = await f.read(1)
                  # Если есть следующий чанк, добавляем символ в последнюю строку
                  if next_chunk != '':
                     lines[-1] = lines[-1] + next_chunk
                  # Код отправляет строки из чанка
                  else:
                       for line in lines:
                           yield line
                       break
                 # Код отправляет строки из чанка
                for line in lines:
                    yield line

    except Exception as ex:
       # Логирование ошибки при чтении файла
       logger.error(f'Ошибка при чтении файла {file_path}.', ex)


async def get_filenames_from_directory(
    directory: str | Path, extensions: str | list[str] = '*'
) -> list[str]:
    """
    Асинхронно возвращает список имен файлов в директории, опционально отфильтрованных по расширению.

    Args:
        directory (str | Path): Путь к директории для поиска.
        extensions (str | list[str], optional): Расширения для фильтрации.
            По умолчанию '*'.

    Returns:
        list[str]: Список имен файлов, найденных в директории.

    Example:
        >>> from pathlib import Path
        >>> directory = Path('.')
        >>> await get_filenames_from_directory(directory, ['.txt', '.md'])
        ['example.txt', 'readme.md']
    """
    try:
        # Преобразование пути к типу Path
        path = Path(directory)
        # Код обрабатывает расширения для фильтрации файлов
        if isinstance(extensions, str):
            extensions = [extensions] if extensions != '*' else []
        extensions = [ext if ext.startswith('.') else f'.{ext}' for ext in extensions]
        # Код возвращает список имен файлов
        return [
            file.name
            for file in path.iterdir()
            if file.is_file() and (not extensions or file.suffix in extensions)
        ]
    except Exception as ex:
        # Логирование ошибки при получении списка имен файлов
        logger.error(f'Ошибка при получении списка имен файлов из \'{directory}\'.', ex)
        return []


async def recursively_yield_file_path(
    root_dir: str | Path, patterns: str | list[str] = '*'
) -> AsyncGenerator[Path, None]:
    """
    Асинхронно рекурсивно возвращает пути ко всем файлам, соответствующим заданным шаблонам, в указанной директории.

    Args:
        root_dir (str | Path): Корневая директория для поиска.
        patterns (str | list[str]): Шаблоны для фильтрации файлов.

    Yields:
        Path: Путь к файлу, соответствующему шаблону.

    Example:
        >>> from pathlib import Path
        >>> root_dir = Path('.')
        >>> async for path in recursively_yield_file_path(root_dir, ['*.txt', '*.md']):
        ...    print(path)
        ./example.txt
        ./readme.md
    """
    try:
        # Код обрабатывает шаблоны для поиска
        patterns = [patterns] if isinstance(patterns, str) else patterns
        # Код возвращает пути к файлам по шаблонам
        for pattern in patterns:
          for path in Path(root_dir).rglob(pattern):
                yield path
    except Exception as ex:
        # Логирование ошибки при рекурсивном поиске файлов
        logger.error(f'Ошибка при рекурсивном поиске файлов в \'{root_dir}\'.', ex)


async def recursively_get_file_path(
    root_dir: str | Path,
    patterns: str | list[str] = '*'
) -> list[Path]:
    """
    Асинхронно рекурсивно возвращает список путей ко всем файлам, соответствующим заданным шаблонам, в указанной директории.

    Args:
        root_dir (str | Path): Корневая директория для поиска.
        patterns (str | list[str]): Шаблоны для фильтрации файлов.

    Returns:
        list[Path]: Список путей к файлам, соответствующим шаблонам.

    Example:
        >>> from pathlib import Path
        >>> root_dir = Path('.')
        >>> paths = await recursively_get_file_path(root_dir, ['*.txt', '*.md'])
        >>> print(paths)
        [Path('./example.txt'), Path('./readme.md')]
    """
    try:
       file_paths = []
       # Код обрабатывает шаблоны для поиска
       patterns = [patterns] if isinstance(patterns, str) else patterns
       # Код собирает пути к файлам по шаблонам
       for pattern in patterns:
         async for path in Path(root_dir).rglob(pattern):
            file_paths.append(path)
       return file_paths
    except Exception as ex:
        # Логирование ошибки при рекурсивном поиске файлов
         logger.error(f'Ошибка при рекурсивном поиске файлов в \'{root_dir}\'.', ex)
         return []


async def recursively_read_text_files(
    root_dir: str | Path,
    patterns: str | list[str],
    as_list: bool = False
) -> list[str]:
    """
    Асинхронно рекурсивно читает текстовые файлы из указанной корневой директории, соответствующие заданным шаблонам.

    Args:
        root_dir (str | Path): Путь к корневой директории для поиска.
        patterns (str | list[str]): Шаблон(ы) имени файла для фильтрации.
             Может быть как одиночным шаблоном (например, '*.txt'), так и списком.
        as_list (bool, optional): Если True, то возвращает содержимое файла как список строк.
             По умолчанию `False`.

    Returns:
        list[str]: Список содержимого файлов (или список строк, если `as_list=True`),
         соответствующих заданным шаблонам.

    Example:
        >>> from pathlib import Path
        >>> root_dir = Path('.')
        >>> contents = await recursively_read_text_files(root_dir, ['*.txt', '*.md'], as_list=True)
        >>> for line in contents:
        ...     print(line)
        Содержимое example.txt
        Первая строка readme.md
        Вторая строка readme.md
    """
    matches = []
    # Преобразование пути к типу Path
    root_path = Path(root_dir)
    # Проверка, является ли путь директорией
    if not root_path.is_dir():
        # Логирование ошибки, если путь не является директорией
        logger.debug(f'Корневая директория \'{root_path}\' не существует или не является директорией.')
        return []

    print(f'Поиск в директории: {root_path}')
     # Код обрабатывает шаблоны для поиска
    if isinstance(patterns, str):
        patterns = [patterns]
    # Код собирает пути к файлам по шаблонам
    files = await recursively_get_file_path(root_path, patterns)
    contents = await asyncio.gather(*[read_text_file(p, as_list=as_list) for p in files])

    return list(filter(None, contents))

async def get_directory_names(directory: str | Path) -> list[str]:
    """
    Асинхронно возвращает список имен директорий из указанной директории.

    Args:
        directory (str | Path): Путь к директории, из которой нужно получить имена.

    Returns:
        list[str]: Список имен директорий, найденных в указанной директории.

    Example:
        >>> from pathlib import Path
        >>> directory = Path('.')
        >>> await get_directory_names(directory)
        ['dir1', 'dir2']
    """
    try:
        # Код возвращает список имен директорий
        return [entry.name for entry in Path(directory).iterdir() if entry.is_dir()]
    except Exception as ex:
         # Логирование ошибки при получении списка имен директорий
        logger.error(f'Ошибка при получении списка имен директорий из \'{directory}\'.', ex)
        return []


async def remove_bom(path: str | Path) -> None:
    """
    Асинхронно удаляет BOM из текстового файла или из всех файлов Python в директории.

    Args:
        path (str | Path): Путь к файлу или директории.

    Example:
        >>> from pathlib import Path
        >>> file_path = Path('example.txt')
        >>> with open(file_path, 'w', encoding='utf-8') as f:
        ...     f.write('\\ufeffПример текста с BOM')
        >>> await remove_bom(file_path)
        >>> with open(file_path, 'r', encoding='utf-8') as f:
        ...     print(f.read())
        Пример текста с BOM
    """
    # Преобразование пути к типу Path
    path = Path(path)
    # Проверка, является ли путь файлом
    if path.is_file():
        try:
            # Открытие файла для чтения и записи
            async with aiofiles.open(path, 'r+', encoding='utf-8') as file:
                # Код удаляет BOM из файла
                content = await file.read()
                content = content.replace('\ufeff', '')
                await file.seek(0)
                await file.write(content)
                await file.truncate()
        except Exception as ex:
             # Логирование ошибки при удалении BOM из файла
            logger.error(f'Ошибка при удалении BOM из файла {path}.', ex)
    # Проверка, является ли путь директорией
    elif path.is_dir():
         # Код обрабатывает все файлы .py в директории
        async def process_file(file_path):
             try:
                async with aiofiles.open(file_path, 'r+', encoding='utf-8') as f:
                    content = await f.read()
                    content = content.replace('\ufeff', '')
                    await f.seek(0)
                    await f.write(content)
                    await f.truncate()
             except Exception as ex:
                 logger.error(f'Ошибка при удалении BOM из файла {file_path}.', ex)
        # Код обрабатывает все файлы .py в директории
        files = [
            p for p in path.rglob('*') if p.is_file() and p.suffix == '.py'
        ]
        await asyncio.gather(*[process_file(file) for file in files])
    else:
        # Логирование ошибки, если путь не является файлом или директорией
        logger.error(f'Указанный путь \'{path}\' не является файлом или директорией.')


async def main() -> None:
    """Entry point for BOM removal in Python files."""
    root_dir = Path('..', 'src')
    logger.info(f'Starting BOM removal in {root_dir}')
    await remove_bom(root_dir)


if __name__ == '__main__':
    asyncio.run(main())
```