# Анализ кода модуля `file_async.py`

**Качество кода**
7
-   Плюсы
    - Код хорошо структурирован и разбит на множество асинхронных функций, что способствует лучшей читаемости и обслуживаемости.
    -  Присутствует подробная документация для каждой функции, включая примеры использования и описание типов возвращаемых значений.
    -  Используется асинхронный ввод/вывод (aiofiles, asyncio), что обеспечивает неблокирующую работу с файловой системой.
    -  Код поддерживает как чтение и запись отдельных файлов, так и рекурсивный обход директорий.
    -   Обработка ошибок выполняется с использованием `try-except` блоков, а ошибки логируются с помощью `logger.error`.
    -   Есть функция для удаления BOM из файлов.
 - Минусы
    -  Используется стандартный `json.dumps` для записи JSON, хотя в инструкциях указано использовать `j_dumps`.
    -  В некоторых местах код можно упростить, сделав его более читабельным (например,  в функциях `recursively_get_file_path` и `recursively_read_text_files`).
    -  Функция `recursively_read_text_files` использует `os.walk`, который не является асинхронным, в асинхронном коде, что может привести к блокировкам.
    -  В некоторых функциях используется `if not chunk: break` для чтения файла, что можно заменить на более Pythonic `while chunk := await f.read(chunk_size):`.
    -  Функция `read_text_file`  использует рекурсивный вызов `read_text_file`,  что может привести к проблемам с производительностью при глубокой рекурсии.
   -  В цикле  `remove_bom`  можно использовать `os.scandir` вместо `os.walk`,  чтобы не генерировать списки для каждого уровня подкаталогов.


**Рекомендации по улучшению**

1.  **Использовать `j_dumps`:** Заменить `json.dumps` на `j_dumps` из `src.utils.jjson`.
2.  **Упрощение кода:** Упростить логику в функциях `recursively_get_file_path` и `recursively_read_text_files`.
3.  **Использовать `os.scandir`:** Заменить `os.walk` на `os.scandir` в `remove_bom` для повышения производительности.
4.  **Упростить чтение файлов:** Использовать `while chunk := await f.read(chunk_size):` для чтения файлов.
5.  **Избегать рекурсии:** Избегать рекурсивного вызова `read_text_file` в `read_text_file` для оптимизации.
6.  **Улучшить обработку ошибок:** Более точно обрабатывать ошибки и предоставлять информативные сообщения в логах.
7.  **Добавить описание модуля и документацию:**
    -   Добавить описание модуля в начале файла.
    -   Добавить документацию для каждой функции, метода и переменной.
    -   Соблюдать стандарты оформления docstring в Python (для Sphinx).
8. **Использовать `from src.utils.jjson import j_dumps`**
9. **Использовать `from src.utils.jjson import j_loads`**

**Оптимизированный код**
```python
# -*- coding: utf-8 -*-
#! venv/bin/python/python3.12
"""
Модуль для работы с файлами.
=========================================================================================

Этот модуль содержит набор асинхронных утилит для выполнения файловых операций,
таких как сохранение, чтение и поиск файлов. Поддерживает обработку больших файлов
с использованием генераторов для экономии памяти.

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
import os
import asyncio
import aiofiles
import aiofiles.os
import fnmatch
from pathlib import Path
from typing import List, Optional, Union, AsyncGenerator
from src.logger.logger import logger
from src.utils.jjson import j_dumps, j_loads # импортируем j_dumps и j_loads

MODE = 'dev' # Константа режима

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
        file_path = Path(file_path)
        await aiofiles.os.makedirs(file_path.parent, exist_ok = True)
        async with aiofiles.open(file_path, mode, encoding = 'utf-8') as file:
            if isinstance(data, list):
                for line in data:
                  await file.write(f'{line}\n')
            elif isinstance(data, dict):
                await file.write(j_dumps(data, ensure_ascii = False, indent = 4)) # используем j_dumps
            else:
                await file.write(data)
        return True
    except Exception as ex:
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
        as_list (bool, optional): Если `True`, возвращает асинхронный генератор строк или список строк.
        extensions (list[str], optional): Список расширений файлов для включения при чтении директории.
        chunk_size (int, optional): Размер чанка для чтения файла в байтах.
        recursive (bool, optional): Если `True`, поиск файлов выполняется рекурсивно.
        patterns (str | list[str], optional): Шаблоны для фильтрации файлов при рекурсивном поиске.

    Returns:
        AsyncGenerator[str, None] | str | list[str] | None:
        - Если `as_list` is True и `file_path` является файлом, возвращает асинхронный генератор строк.
        - Если `as_list` is True и `file_path` является директорией и `recursive` is True, возвращает список строк.
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
            file_path – это директория, recursive равен False и as_list равен False. При этом возвращается объединенная строка, состоящая из содержимого всех файлов в директории, разделенных символами новой строки (\n).
            file_path – это директория, recursive равен True и as_list равен False. При этом возвращается объединенная строка, состоящая из содержимого всех файлов в директории и её поддиректориях, разделенных символами новой строки (\n).

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
                files = await recursively_get_file_path(path, patterns, extensions) # передаем extensions
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
                  return (line async for file in files async for line in yield_text_from_files(file, as_list = True, chunk_size = chunk_size))
                else:
                  contents = await asyncio.gather(*[read_text_file(p, chunk_size = chunk_size) for p in files])
                  return '\n'.join(filter(None, contents))
        else:
            logger.error(f'Путь \'{file_path}\' не является файлом или директорией.')
            return None
    except Exception as ex:
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
        as_list (bool, optional): Если True, возвращает генератор строк. По умолчанию False.
        chunk_size (int, optional): Размер чанка для чтения файла в байтах.

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
        path = Path(file_path)
        if path.is_file():
            if as_list:
                 async for line in  _read_file_lines_generator(path, chunk_size = chunk_size):
                   yield line
            else:
               yield await _read_file_content(path, chunk_size = chunk_size)
        else:
            logger.error(f'Путь \'{file_path}\' не является файлом.')
    except Exception as ex:
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
    content = ''
    try:
       async with aiofiles.open(file_path, 'r', encoding = 'utf-8') as f:
            while chunk := await f.read(chunk_size): # используем while chunk := await f.read(chunk_size)
                content += chunk
       return content
    except Exception as ex:
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
        async with aiofiles.open(file_path, 'r', encoding = 'utf-8') as f:
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
        patterns = [patterns] if isinstance(patterns, str) else patterns
        for pattern in patterns:
          for path in Path(root_dir).rglob(pattern):
                yield path
    except Exception as ex:
        logger.error(f'Ошибка при рекурсивном поиске файлов в \'{root_dir}\'.', ex)


async def recursively_get_file_path(
    root_dir: str | Path,
    patterns: str | list[str] = '*',
    extensions: Optional[list[str]] = None, # добавили extensions
) -> list[Path]:
    """
    Асинхронно рекурсивно возвращает список путей ко всем файлам, соответствующим заданным шаблонам, в указанной директории.

    Args:
        root_dir (str | Path): Корневая директория для поиска.
        patterns (str | list[str]): Шаблоны для фильтрации файлов.
        extensions (list[str], optional): Список расширений файлов для включения при поиске директории.

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
       patterns = [patterns] if isinstance(patterns, str) else patterns
       for pattern in patterns:
          async for path in recursively_yield_file_path(root_dir, pattern):
                if not extensions or path.suffix in extensions: # фильтрация по расширению
                   file_paths.append(path)
       return file_paths
    except Exception as ex:
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
    root_path = Path(root_dir)

    if not root_path.is_dir():
        logger.debug(f'Корневая директория \'{root_path}\' не существует или не является директорией.')
        return []

    logger.debug(f'Поиск в директории: {root_path}')

    if isinstance(patterns, str):
        patterns = [patterns]

    for root, _, files in os.walk(root_path): # TODO: заменить на os.scandir
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
                   logger.error(f'Ошибка при чтении файла \'{file_path}\'.', ex)
    return matches


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
        return [entry.name for entry in Path(directory).iterdir() if entry.is_dir()]
    except Exception as ex:
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
            logger.error(f'Ошибка при удалении BOM из файла {path}.', ex)
    elif path.is_dir():
        for entry in os.scandir(path): # используем os.scandir вместо os.walk
            if entry.is_file() and entry.name.endswith('.py'):
              file_path = Path(entry.path)
              try:
                  async with aiofiles.open(file_path, 'r+', encoding = 'utf-8') as f:
                      content = await f.read()
                      content = content.replace('\ufeff', '')
                      await f.seek(0)
                      await f.write(content)
                      await f.truncate()
              except Exception as ex:
                  logger.error(f'Ошибка при удалении BOM из файла {file_path}.', ex)

    else:
        logger.error(f'Указанный путь \'{path}\' не является файлом или директорией.')



async def main() -> None:
    """Entry point for BOM removal in Python files."""
    root_dir = Path('..', 'src')
    logger.info(f'Starting BOM removal in {root_dir}')
    await remove_bom(root_dir)


if __name__ == '__main__':
    asyncio.run(main())
```