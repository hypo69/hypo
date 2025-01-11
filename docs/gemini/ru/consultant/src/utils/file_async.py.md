### Анализ кода модуля `file_async`

**Качество кода**:

- **Соответствие стандартам**: 7/10
- **Плюсы**:
    - Асинхронность: Код использует `asyncio` и `aiofiles` для асинхронных операций с файлами, что повышает производительность при работе с IO-операциями.
    - Генераторы: Использование генераторов для чтения файлов позволяет обрабатывать большие файлы, не загружая их целиком в память.
    - Обработка ошибок: Присутствует общая обработка исключений с логированием ошибок.
    - Типизация: Код использует аннотации типов, что улучшает читаемость и помогает выявлять ошибки на ранних этапах.
    - Документация: Функции имеют docstrings с описанием параметров, возвращаемых значений и примерами.
- **Минусы**:
    - Непоследовательное использование кавычек: В коде используются как одинарные, так и двойные кавычки, что нарушает консистентность.
    - Неполное соответствие RST:  Не все docstrings соответствуют стандарту RST, который подразумевает использование `:param:`, `:return:` и т.д.
    - Смешанная обработка ошибок: В коде используется `try-except` и логирование ошибок через `logger.error`, что можно упростить.
    - Избыточный `try-except` в `_read_file_content` и других функциях.
    - Дублирование кода: Есть схожие блоки кода в функциях `read_text_file` и `yield_text_from_files`.
    - Не всегда точные описания: Комментарии не всегда точно описывают действие кода.
    -  Импорт `logger` из `src.logger.logger`.

**Рекомендации по улучшению**:

-   Привести кавычки к единому стилю: Использовать одинарные кавычки для строк в коде, двойные только для вывода.
-   Улучшить docstrings: Привести docstrings к полному соответствию стандартам RST, с использованием `:param:`, `:type:`, `:return:`, `:rtype:`, `:raises:`, и  `:yields:`.
-   Упростить обработку ошибок:  Избегать `try-except` там, где можно обойтись логированием ошибок через `logger.error`.
-   Устранить дублирование кода: Вынести общую логику в отдельные функции или использовать более общие функции.
-   Уточнить комментарии: Использовать более конкретные формулировки в комментариях.
-   Импорт: `from src.logger.logger import logger`
-   Удалить лишние импорты: `import os`, так как не используется напрямую в коде, используется внутри pathlib.

**Оптимизированный код**:

```python
# -*- coding: utf-8 -*-
#! venv/bin/python/python3.12
"""
Модуль для работы с файлами.
=========================================================================================

Модуль содержит набор утилит для выполнения операций с файлами, таких как сохранение, чтение,
и получение списков файлов. Поддерживает обработку больших файлов с использованием генераторов
для экономии памяти.

Пример использования
--------------------

.. code-block:: python

    from pathlib import Path
    from src.utils.file_async import read_text_file, save_text_file

    file_path = Path('example.txt')
    content = await read_text_file(file_path)
    if content:
        print(f'File content: {content[:100]}...')

    await save_text_file(file_path, 'Новый текст')
"""
import asyncio
import json
import fnmatch
import aiofiles
import aiofiles.os
from pathlib import Path
from typing import List, Optional, Union, AsyncGenerator, Generator

from src.logger.logger import logger #  Импорт logger из src.logger


MODE = 'dev'  # Константа режима


async def save_text_file(
    file_path: str | Path,
    data: str | list[str] | dict,
    mode: str = 'w'
) -> bool:
    """
    Асинхронно сохраняет данные в текстовый файл.

    :param file_path: Путь к файлу для сохранения.
    :type file_path: str | Path
    :param data: Данные для записи.
    :type data: str | list[str] | dict
    :param mode: Режим записи ('w' для записи, 'a' для добавления).
    :type mode: str, optional
    :return: True, если файл успешно сохранён, иначе False.
    :rtype: bool
    :raises Exception: В случае ошибки при записи в файл.

    Пример:
        >>> from pathlib import Path
        >>> file_path = Path('example.txt')
        >>> data = 'Пример текста'
        >>> result = await save_text_file(file_path, data)
        >>> print(result)
        True
    """
    try:
        file_path = Path(file_path)
        await aiofiles.os.makedirs(file_path.parent, exist_ok = True)
        async with aiofiles.open(file_path, mode, encoding = 'utf-8') as file: #  Открытие файла для записи
            if isinstance(data, list):
                for line in data:
                  await file.write(f'{line}\\n')
            elif isinstance(data, dict):
                await file.write(json.dumps(data, ensure_ascii = False, indent = 4))
            else:
                await file.write(data)
        return True
    except Exception as ex:
        logger.error(f'Ошибка при сохранении файла {file_path}.', ex) # Логирование ошибки
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

    :param file_path: Путь к файлу или директории.
    :type file_path: str | Path
    :param as_list: Если `True`, то возвращает генератор строк или список строк, в зависимости от типа вывода.
    :type as_list: bool, optional
    :param extensions: Список расширений файлов для включения при чтении директории.
    :type extensions: list[str], optional
    :param chunk_size: Размер чанка для чтения файла в байтах.
    :type chunk_size: int, optional
    :param recursive: Если `True`, то поиск файлов выполняется рекурсивно.
    :type recursive: bool, optional
    :param patterns: Шаблоны для фильтрации файлов при рекурсивном поиске.
    :type patterns: str | list[str], optional
    :return:
            - Если `as_list` is True и `file_path` является файлом, возвращает асинхронный генератор строк.
            - Если `as_list` is True и `file_path` является директорией и `recursive` is True, возвращает список строк.
            - Если `as_list` is False и `file_path` является файлом, возвращает строку.
            - Если `as_list` is False и `file_path` является директорией, возвращает объединенную строку.
            - Возвращает `None` в случае ошибки.
    :rtype: AsyncGenerator[str, None] | str | list[str] | None
    :raises Exception: При возникновении ошибки при чтении файла.

    Пример:
        >>> from pathlib import Path
        >>> file_path = Path('example.txt')
        >>> content = await read_text_file(file_path)
        >>> if content:
        ...    print(f'File content: {content[:100]}...')
        File content: Пример текста...
    Функция read_text_file может возвращать несколько разных типов данных в зависимости от входных параметров:

    Возвращаемые значения:
    ----------------------

    - AsyncGenerator[str, None] (Асинхронный генератор строк):
        Асинхронный генератор при итерации выдаёт строки из файла(ов) по одной. Эффективно для работы с большими файлами, так как они не загружаются полностью в память.
        - Когда:
            file_path – это файл и as_list равен True.
            file_path – это директория, recursive равен True и as_list равен True. При этом в генератор попадают строки из всех найденных файлов.
            file_path – это директория, recursive равен False и as_list равен True. При этом в генератор попадают строки из всех найденных файлов в текущей директории.

    - str (Строка):
        Содержимое файла или объединенное содержимое всех файлов в виде одной строки.
        - Когда:
            file_path – это файл и as_list равен False.
            file_path – это директория, recursive равен False и as_list равен False. При этом возвращается объединенная строка, состоящая из содержимого всех файлов в директории, разделенных символами новой строки (\\n).
            file_path – это директория, recursive равен True и as_list равен False. При этом возвращается объединенная строка, состоящая из содержимого всех файлов в директории и её поддиректориях, разделенных символами новой строки (\\n).

    - list[str] (Список строк):
        Этот тип явно не возвращается функцией, однако когда file_path – это директория, recursive равен True и as_list равен True - функция возвращает генератор, который можно преобразовать в список при помощи list()
        - Когда:
            file_path – не является ни файлом, ни директорией.
            Произошла ошибка при чтении файла или директории (например, файл не найден, ошибка доступа и т.п.).

    Note:
        Если вы хотите прочитать содержимое файла построчно (особенно для больших файлов) используйте as_list = True. В этом случае вы получите генератор строк.
        Если вы хотите получить всё содержимое файла в виде одной строки используйте as_list = False.
        Если вы работаете с директорией, recursive = True будет обходить все поддиректории.
        extensions и patterns позволят вам фильтровать файлы при работе с директорией.
        chunk_size позволяет оптимизировать работу с большими файлами при чтении их по частям.
        None будет возвращён в случае ошибок.

    Важно помнить:
        В случае чтения директории, если as_list=False, функция объединяет все содержимое найденных файлов в одну строку. Это может потребовать много памяти, если файлов много или они большие.
        Функция полагается на другие функции-помощники (_read_file_lines_generator, _read_file_content, recursively_get_file_path, yield_text_from_files), которые здесь не определены и их поведение влияет на результат read_text_file.
    """
    try:
        path = Path(file_path)
        if path.is_file():
            if as_list:
                return _read_file_lines_generator(path, chunk_size = chunk_size)
            else:
                return await _read_file_content(path, chunk_size = chunk_size)
        elif path.is_dir():
            if recursive:
                if patterns:
                    files = await recursively_get_file_path(path, patterns)
                else:
                    files = [
                        p for p in path.rglob('*') if p.is_file() and (not extensions or p.suffix in extensions)
                    ]
                if as_list:
                  return (
                        line
                        async for file in files
                        async for line in yield_text_from_files(file, as_list = True, chunk_size = chunk_size)
                    )

                else:
                   contents = await asyncio.gather(*[read_text_file(p, chunk_size = chunk_size) for p in files])
                   return '\n'.join(filter(None, contents))
            else:
                files = [
                    p for p in path.iterdir() if p.is_file() and (not extensions or p.suffix in extensions)
                ]
                if as_list:
                  return (line async for file in files async for line in read_text_file(file, as_list = True, chunk_size = chunk_size))
                else:
                  contents = await asyncio.gather(*[read_text_file(p, chunk_size = chunk_size) for p in files])
                  return '\n'.join(filter(None, contents))
        else:
            logger.error(f'Путь \'{file_path}\' не является файлом или директорией.') # Логирование ошибки
            return None
    except Exception as ex:
        logger.error(f'Ошибка при чтении файла/директории {file_path}.', ex)  # Логирование ошибки
        return None


async def yield_text_from_files(
    file_path: str | Path,
    as_list: bool = False,
    chunk_size: int = 8192
) -> AsyncGenerator[str, None] | str | None:
    """
    Асинхронно читает содержимое файла и возвращает его в виде генератора строк или одной строки.

    :param file_path: Путь к файлу.
    :type file_path: str | Path
    :param as_list: Если True, возвращает генератор строк.
    :type as_list: bool, optional
    :param chunk_size: Размер чанка для чтения файла в байтах.
    :type chunk_size: int, optional
    :return: Генератор строк, объединенная строка или None в случае ошибки.
    :rtype: AsyncGenerator[str, None] | str | None
    :yields: Строки из файла, если as_list is True.
    :rtype: str

    Пример:
        >>> from pathlib import Path
        >>> file_path = Path('example.txt')
        >>> async for line in yield_text_from_files(file_path, as_list=True):
        ...     print(line)
        Первая строка файла
        Вторая строка файла
    """
    try:
        path = Path(file_path)
        if path.is_file():
            if as_list:
                 async for line in  _read_file_lines_generator(path, chunk_size = chunk_size):
                   yield line
            else:
               yield await _read_file_content(path, chunk_size = chunk_size)
        else:
            logger.error(f'Путь \'{file_path}\' не является файлом.') # Логирование ошибки
    except Exception as ex:
        logger.error(f'Ошибка при чтении файла {file_path}.', ex) # Логирование ошибки


async def _read_file_content(file_path: Path, chunk_size: int) -> str:
    """
    Асинхронно читает содержимое файла по чанкам и возвращает как строку.

    :param file_path: Путь к файлу для чтения.
    :type file_path: Path
    :param chunk_size: Размер чанка для чтения файла в байтах.
    :type chunk_size: int
    :return: Содержимое файла в виде строки.
    :rtype: str
    :raises Exception: При возникновении ошибки при чтении файла.
    """
    content = ''
    try:
      async with aiofiles.open(file_path, 'r', encoding = 'utf-8') as f:
          while True:
              chunk = await f.read(chunk_size)
              if not chunk:
                  break
              content += chunk
      return content
    except Exception as ex:
      logger.error(f'Ошибка при чтении файла {file_path}.', ex) # Логирование ошибки
      return ''


async def _read_file_lines_generator(file_path: Path, chunk_size: int) -> AsyncGenerator[str, None]:
    """
    Асинхронно читает файл по строкам с помощью генератора.

    :param file_path: Путь к файлу для чтения.
    :type file_path: Path
    :param chunk_size: Размер чанка для чтения файла в байтах.
    :type chunk_size: int
    :yields: Строки из файла.
    :rtype: str
    :raises Exception: При возникновении ошибки при чтении файла.
    """
    try:
        async with aiofiles.open(file_path, 'r', encoding='utf-8') as f:
            while True:
                chunk = await f.read(chunk_size)
                if not chunk:
                    break
                lines = chunk.splitlines()
                if len(lines) > 0 and not chunk.endswith('\n'):
                  next_chunk = await f.read(1)
                  if next_chunk != '':
                     lines[-1] = lines[-1] + next_chunk
                  else:
                       for line in lines:
                           yield line
                       break
                for line in lines:
                    yield line

    except Exception as ex:
       logger.error(f'Ошибка при чтении файла {file_path}.', ex) # Логирование ошибки


async def get_filenames_from_directory(
    directory: str | Path, extensions: str | list[str] = '*'
) -> list[str]:
    """
    Асинхронно возвращает список имен файлов в директории, опционально отфильтрованных по расширению.

    :param directory: Путь к директории для поиска.
    :type directory: str | Path
    :param extensions: Расширения для фильтрации. По умолчанию '*'.
    :type extensions: str | list[str], optional
    :return: Список имен файлов, найденных в директории.
    :rtype: list[str]

    Пример:
        >>> from pathlib import Path
        >>> directory = Path('.')
        >>> await get_filenames_from_directory(directory, ['.txt', '.md'])
        ['example.txt', 'readme.md']
    """
    try:
        path = Path(directory)
        if isinstance(extensions, str):
            extensions = [extensions] if extensions != '*' else []
        extensions = [ext if ext.startswith('.') else f'.{ext}' for ext in extensions]
        return [
            file.name
            for file in path.iterdir()
            if file.is_file() and (not extensions or file.suffix in extensions)
        ]
    except Exception as ex:
        logger.error(f'Ошибка при получении списка имен файлов из \'{directory}\'.', ex) # Логирование ошибки
        return []


async def recursively_yield_file_path(
    root_dir: str | Path, patterns: str | list[str] = '*'
) -> AsyncGenerator[Path, None]:
    """
    Асинхронно рекурсивно возвращает пути ко всем файлам, соответствующим заданным шаблонам, в указанной директории.

    :param root_dir: Корневая директория для поиска.
    :type root_dir: str | Path
    :param patterns: Шаблоны для фильтрации файлов.
    :type patterns: str | list[str]
    :yields: Путь к файлу, соответствующему шаблону.
    :rtype: Path

    Пример:
        >>> from pathlib import Path
        >>> root_dir = Path('.')
        >>> async for path in recursively_yield_file_path(root_dir, ['*.txt', '*.md']):
        ...    print(path)
        ./example.txt
        ./readme.md
    """
    try:
        patterns = [patterns] if isinstance(patterns, str) else patterns
        for pattern in patterns:
          for path in Path(root_dir).rglob(pattern):
                yield path
    except Exception as ex:
        logger.error(f'Ошибка при рекурсивном поиске файлов в \'{root_dir}\'.', ex) # Логирование ошибки


async def recursively_get_file_path(
    root_dir: str | Path,
    patterns: str | list[str] = '*'
) -> list[Path]:
    """
    Асинхронно рекурсивно возвращает список путей ко всем файлам, соответствующим заданным шаблонам, в указанной директории.

    :param root_dir: Корневая директория для поиска.
    :type root_dir: str | Path
    :param patterns: Шаблоны для фильтрации файлов.
    :type patterns: str | list[str]
    :return: Список путей к файлам, соответствующим шаблонам.
    :rtype: list[Path]

    Пример:
        >>> from pathlib import Path
        >>> root_dir = Path('.')
        >>> paths = await recursively_get_file_path(root_dir, ['*.txt', '*.md'])
        >>> print(paths)
        [Path('./example.txt'), Path('./readme.md')]
    """
    try:
       file_paths = []
       patterns = [patterns] if isinstance(patterns, str) else patterns
       for pattern in patterns:
         async for path in Path(root_dir).rglob(pattern):
            file_paths.append(path)
       return file_paths
    except Exception as ex:
         logger.error(f'Ошибка при рекурсивном поиске файлов в \'{root_dir}\'.', ex) # Логирование ошибки
         return []


async def recursively_read_text_files(
    root_dir: str | Path,
    patterns: str | list[str],
    as_list: bool = False
) -> list[str]:
    """
    Асинхронно рекурсивно читает текстовые файлы из указанной корневой директории, соответствующие заданным шаблонам.

    :param root_dir: Путь к корневой директории для поиска.
    :type root_dir: str | Path
    :param patterns: Шаблон(ы) имени файла для фильтрации.
             Может быть как одиночным шаблоном (например, '*.txt'), так и списком.
    :type patterns: str | list[str]
    :param as_list: Если True, то возвращает содержимое файла как список строк. По умолчанию `False`.
    :type as_list: bool, optional
    :return: Список содержимого файлов (или список строк, если `as_list=True`), соответствующих заданным шаблонам.
    :rtype: list[str]

    Пример:
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
    root_path = Path(root_dir)

    if not root_path.is_dir():
        logger.debug(f'Корневая директория \'{root_path}\' не существует или не является директорией.') # Логирование ошибки
        return []

    print(f'Поиск в директории: {root_path}')

    if isinstance(patterns, str):
        patterns = [patterns]

    for root, _, files in os.walk(root_path):
        for filename in files:
            if any(fnmatch.fnmatch(filename, pattern) for pattern in patterns):
                file_path = Path(root) / filename
                try:
                    async with aiofiles.open(file_path, 'r', encoding = 'utf-8') as file:
                       if as_list:
                            matches.extend(await file.readlines())
                       else:
                            matches.append(await file.read())
                except Exception as ex:
                   logger.error(f'Ошибка при чтении файла \'{file_path}\'.', ex) # Логирование ошибки
    return matches


async def get_directory_names(directory: str | Path) -> list[str]:
    """
    Асинхронно возвращает список имен директорий из указанной директории.

    :param directory: Путь к директории, из которой нужно получить имена.
    :type directory: str | Path
    :return: Список имен директорий, найденных в указанной директории.
    :rtype: list[str]

    Пример:
        >>> from pathlib import Path
        >>> directory = Path('.')
        >>> await get_directory_names(directory)
        ['dir1', 'dir2']
    """
    try:
        return [entry.name for entry in Path(directory).iterdir() if entry.is_dir()]
    except Exception as ex:
        logger.error(f'Ошибка при получении списка имен директорий из \'{directory}\'.', ex) # Логирование ошибки
        return []


async def remove_bom(path: str | Path) -> None:
    """
    Асинхронно удаляет BOM из текстового файла или из всех файлов Python в директории.

    :param path: Путь к файлу или директории.
    :type path: str | Path

    Пример:
        >>> from pathlib import Path
        >>> file_path = Path('example.txt')
        >>> with open(file_path, 'w', encoding='utf-8') as f:
        ...     f.write('\\ufeffПример текста с BOM')
        >>> await remove_bom(file_path)
        >>> with open(file_path, 'r', encoding='utf-8') as f:
        ...     print(f.read())
        Пример текста с BOM
    """
    path = Path(path)
    if path.is_file():
        try:
            async with aiofiles.open(path, 'r+', encoding = 'utf-8') as file:
                content = await file.read()
                content = content.replace('\ufeff', '')
                await file.seek(0)
                await file.write(content)
                await file.truncate()
        except Exception as ex:
            logger.error(f'Ошибка при удалении BOM из файла {path}.', ex) # Логирование ошибки
    elif path.is_dir():
        for root, _, files in os.walk(path):
             for file in files:
                 if file.endswith('.py'):
                    file_path = Path(root) / file
                    try:
                        async with aiofiles.open(file_path, 'r+', encoding = 'utf-8') as f:
                            content = await f.read()
                            content = content.replace('\ufeff', '')
                            await f.seek(0)
                            await f.write(content)
                            await f.truncate()
                    except Exception as ex:
                       logger.error(f'Ошибка при удалении BOM из файла {file_path}.', ex) # Логирование ошибки
    else:
        logger.error(f'Указанный путь \'{path}\' не является файлом или директорией.') # Логирование ошибки


async def main() -> None:
    """Entry point for BOM removal in Python files."""
    root_dir = Path('..', 'src')
    logger.info(f'Starting BOM removal in {root_dir}')
    await remove_bom(root_dir)


if __name__ == '__main__':
    asyncio.run(main())