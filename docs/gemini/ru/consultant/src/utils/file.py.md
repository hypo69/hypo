# Анализ кода модуля `file.py`

**Качество кода**
7
-  Плюсы
    - Код содержит подробную документацию в формате docstring для каждой функции, что облегчает понимание и использование модуля.
    - Используются типы в аннотациях, что улучшает читаемость и поддержку кода.
    - Присутствует логирование ошибок с помощью `logger.error`, что помогает отслеживать проблемы.
    - Есть примеры использования функций в docstring.
    - Код разделен на логические блоки, что упрощает его восприятие.

-  Минусы
    - В коде используются стандартные `json.dump` вместо `j_loads` или `j_loads_ns`.
    - Некоторые функции дублируют функциональность (например `read_text_file` и `read_text_file_generator` ,`recursively_get_file_path` и `recursively_yield_file_path`) и требуют рефакторинга.
    - Присутствуют множественные `try-except` блоки, где можно использовать `logger.error` и `...` для упрощения.
    - Используются двойные кавычки в строках кода, где должны быть одинарные.
    - Не всегда корректное использование генераторов.
    - Некоторые блоки кода могут быть упрощены.
    - Используются `print` в коде.
    - Используется `os.walk` в `recursively_read_text_files` и в `remove_bom`, что дублирует функциональность `Path.rglob`.
    - Код местами избыточен.
**Рекомендации по улучшению**
1.  Использовать `j_loads` или `j_loads_ns` из `src.utils.jjson` вместо стандартного `json.dump`.
2.  Удалить дублирование функциональности.
3.  Упростить обработку ошибок, использовать `logger.error` вместо `try-except`.
4.  Заменить двойные кавычки на одинарные в коде.
5.  Упростить логику работы с генераторами и списками.
6.  Удалить `print` из кода.
7.  Использовать `Path.rglob` вместо `os.walk`
8.  Добавить `...` в местах обработки ошибок.
9.  Вместо `if not chunk` использовать `if chunk` для улучшения читаемости кода.
10. Добавить проверку `if not extensions` в `get_filenames_from_directory` чтобы не создавать пустой список в `extensions = [ext if ext.startswith(\'.\') else f\'.{ext}\' for ext in extensions]`.

**Оптимизированный код**
```python
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
    from src.utils.file import read_text_file, save_text_file

    file_path = Path('example.txt')
    content = read_text_file(file_path)
    if content:
        print(f'File content: {content[:100]}...')

    save_text_file(file_path, 'Новый текст')
"""
import os
# import json # стандартная библиотека json больше не используется
import fnmatch
from pathlib import Path
from typing import List, Optional, Union, Generator
from src.logger.logger import logger
#  Импортируем j_loads и j_loads_ns
from src.utils.jjson import j_loads, j_loads_ns

MODE = 'dev'  # Константа режима


def save_text_file(
    file_path: str | Path,
    data: str | list[str] | dict,
    mode: str = 'w'
) -> bool:
    """
    Сохраняет данные в текстовый файл.

    Args:
        file_path (str | Path): Путь к файлу для сохранения.
        data (str | list[str] | dict): Данные для записи. Могут быть строкой, списком строк или словарем.
        mode (str, optional): Режим записи файла ('w' для записи, 'a' для добавления).
    Returns:
        bool: `True`, если файл успешно сохранен, `False` в противном случае.
    Raises:
        Exception: При возникновении ошибки при записи в файл.

    Example:
        >>> from pathlib import Path
        >>> file_path = Path('example.txt')
        >>> data = 'Пример текста'
        >>> result = save_text_file(file_path, data)
        >>> print(result)
        True
    """
    # код исполняет запись данных в файл
    try:
        file_path = Path(file_path)
        file_path.parent.mkdir(parents=True, exist_ok=True)

        with file_path.open(mode, encoding='utf-8') as file:
            if isinstance(data, list):
                file.writelines(f'{line}\\n' for line in data)
            elif isinstance(data, dict):
                #  используем j_loads_ns для записи в файл
                file.write(j_loads_ns(data))
            else:
                file.write(data)
        return True
    except Exception as ex:
        logger.error(f'Ошибка при сохранении файла {file_path}.', ex)
        ...
        return False


def read_text_file_generator(
    file_path: str | Path,
    as_list: bool = False,
    extensions: Optional[list[str]] = None,
    chunk_size: int = 8192,
    recursive: bool = False,
    patterns: Optional[str | list[str]] = None,
) -> Generator[str, None, None] | str | list[str] | None:
    """
    Читает содержимое файла(ов) или директории.

        Args:
            file_path (str | Path): Путь к файлу или директории.
            as_list (bool, optional): Если `True`, то возвращает генератор строк или список строк, в зависимости от типа вывода.
            extensions (list[str], optional): Список расширений файлов для включения при чтении директории.
            chunk_size (int, optional): Размер чанка для чтения файла в байтах.
            recursive (bool, optional): Если `True`, то поиск файлов выполняется рекурсивно.
            patterns (str | list[str], optional): Шаблоны для фильтрации файлов при рекурсивном поиске.

        Returns:
            Generator[str, None, None] | str | list[str] | None:
            - Если `as_list` is True и `file_path` является файлом, возвращает генератор строк.
            - Если `as_list` is True и `file_path` является директорией и `recursive` is True, возвращает список строк.
            - Если `as_list` is False и `file_path` является файлом, возвращает строку.
            - Если `as_list` is False и `file_path` является директорией, возвращает объединенную строку.
            - Возвращает `None` в случае ошибки.
        Raises:
            Exception: При возникновении ошибки при чтении файла.

        Example:
            >>> from pathlib import Path
            >>> file_path = Path('example.txt')
            >>> content = read_text_file(file_path)
            >>> if content:
            ...    print(f'File content: {content[:100]}...')
            File content: Пример текста...
    Функция read_text_file может возвращать несколько разных типов данных в зависимости от входных параметров:

    Возвращаемые значения:
    ----------------------

    - Generator[str, None, None] (Генератор строк):
        Генератор при итерации выдаёт строки из файла(ов) по одной. Эффективно для работы с большими файлами, так как они не загружаются полностью в память.
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
    # код исполняет чтение файла или директории
    try:
        path = Path(file_path)
        if path.is_file():
            if as_list:
                return _read_file_lines_generator(path, chunk_size=chunk_size)
            else:
                return _read_file_content(path, chunk_size=chunk_size)
        elif path.is_dir():
            if recursive:
                files = recursively_get_file_path(path, patterns) if patterns else [
                        p for p in path.rglob('*') if p.is_file() and (not extensions or p.suffix in extensions)
                    ]
                if as_list:
                    return (
                        line
                        for file in files
                        for line in yield_text_from_files(file, as_list=True, chunk_size=chunk_size)
                    )
                else:
                    return '\n'.join(filter(None, [read_text_file(p, chunk_size=chunk_size) for p in files]))
            else:
                files = [
                    p for p in path.iterdir() if p.is_file() and (not extensions or p.suffix in extensions)
                ]
                if as_list:
                    return (line for file in files for line in read_text_file(file, as_list=True, chunk_size=chunk_size))
                else:
                    return '\n'.join(filter(None, [read_text_file(p, chunk_size=chunk_size) for p in files]))
        else:
            logger.error(f'Путь \'{file_path}\' не является файлом или директорией.')
            ...
            return None
    except Exception as ex:
        logger.error(f'Ошибка при чтении файла/директории {file_path}.', ex)
        ...
        return None

def read_text_file(
    file_path: Union[str, Path],
    as_list: bool = False,
    extensions: Optional[list[str]] = None,
    exc_info: bool = True,
) -> str | list[str] | None:
    """
    Читает содержимое файла.

    Args:
        file_path (str | Path): Путь к файлу или директории.
        as_list (bool, optional): Если True, возвращает содержимое как список строк. По умолчанию False.
        extensions (list[str], optional): Список расширений файлов для включения при чтении директории. По умолчанию None.
        exc_info (bool, optional): Если True, логирует трассировку ошибки. По умолчанию True.

    Returns:
        str | list[str] | None: Содержимое файла в виде строки или списка строк, или None, если произошла ошибка.
    """
    # код исполняет чтение файла
    try:
        path = Path(file_path)
        if path.is_file():
            with path.open('r', encoding='utf-8') as f:
                return f.readlines() if as_list else f.read()
        elif path.is_dir():
            files = [
                p for p in path.rglob('*') if p.is_file() and (not extensions or p.suffix in extensions)
            ]
            contents = [read_text_file(p, as_list) for p in files]
            return [item for sublist in contents if sublist for item in sublist] if as_list else '\n'.join(filter(None, contents))
        else:
            logger.warning(f'Path \'{file_path}\' is invalid.')
            return
    except Exception as ex:
        logger.error(f'Failed to read file {file_path}.', ex, exc_info=exc_info)
        return


def yield_text_from_files(
    file_path: str | Path,
    as_list: bool = False,
    chunk_size: int = 8192
) -> Generator[str, None, None] | str | None:
    """
    Читает содержимое файла и возвращает его в виде генератора строк или одной строки.

    Args:
        file_path (str | Path): Путь к файлу.
        as_list (bool, optional): Если True, возвращает генератор строк. По умолчанию False.
        chunk_size (int, optional): Размер чанка для чтения файла в байтах.

    Returns:
        Generator[str, None, None] | str | None: Генератор строк, объединенная строка или None в случае ошибки.

    Yields:
       str: Строки из файла, если as_list is True.

    Example:
        >>> from pathlib import Path
        >>> file_path = Path('example.txt')
        >>> for line in yield_text_from_files(file_path, as_list=True):
        ...     print(line)
        Первая строка файла
        Вторая строка файла
    """
    # код исполняет чтение файла и возвращает генератор или строку
    try:
        path = Path(file_path)
        if path.is_file():
            if as_list:
                yield from _read_file_lines_generator(path, chunk_size=chunk_size)
            else:
                yield _read_file_content(path, chunk_size=chunk_size)
        else:
            logger.error(f'Путь \'{file_path}\' не является файлом.')
            ...
            return None
    except Exception as ex:
        logger.error(f'Ошибка при чтении файла {file_path}.', ex)
        ...
        return None


def _read_file_content(file_path: Path, chunk_size: int) -> str:
    """
    Читает содержимое файла по чанкам и возвращает как строку.

    Args:
        file_path (Path): Путь к файлу для чтения.
        chunk_size (int): Размер чанка для чтения файла в байтах.
    Returns:
        str: Содержимое файла в виде строки.
    Raises:
        Exception: При возникновении ошибки при чтении файла.
    """
    # код исполняет чтение файла по частям
    with file_path.open('r', encoding='utf-8') as f:
        content = ''
        while True:
            chunk = f.read(chunk_size)
            if not chunk:
                break
            content += chunk
        return content


def _read_file_lines_generator(file_path: Path, chunk_size: int) -> Generator[str, None, None]:
    """
    Читает файл по строкам с помощью генератора.

    Args:
        file_path (Path): Путь к файлу для чтения.
        chunk_size (int): Размер чанка для чтения файла в байтах.
    Yields:
        str: Строки из файла.
    Raises:
        Exception: При возникновении ошибки при чтении файла.
    """
    # код исполняет чтение файла по строкам
    with file_path.open('r', encoding='utf-8') as f:
        while True:
            chunk = f.read(chunk_size)
            if not chunk:
                break
            lines = chunk.splitlines()
            # Если чанк не закончился полной строкой, то последнюю строку добавляем к следующему чанку
            if lines and not chunk.endswith('\n'):
                next_chunk = f.read(1)
                if next_chunk:
                    lines[-1] += next_chunk
                else:
                    yield from lines
                    break
            yield from lines


def get_filenames_from_directory(
    directory: str | Path, extensions: str | list[str] = '*'
) -> list[str]:
    """
    Возвращает список имен файлов в директории, опционально отфильтрованных по расширению.

    Args:
        directory (str | Path): Путь к директории для поиска.
        extensions (str | list[str], optional): Расширения для фильтрации.
            По умолчанию '*'.

    Returns:
        list[str]: Список имен файлов, найденных в директории.

    Example:
        >>> from pathlib import Path
        >>> directory = Path('.')
        >>> get_filenames_from_directory(directory, ['.txt', '.md'])
        ['example.txt', 'readme.md']
    """
    # код исполняет получение списка имен файлов в директории
    try:
        path = Path(directory)
        if isinstance(extensions, str):
            extensions = [extensions] if extensions != '*' else []
        if extensions:  #  проверка на пустой список
            extensions = [ext if ext.startswith('.') else f'.{ext}' for ext in extensions]
        return [
            file.name
            for file in path.iterdir()
            if file.is_file() and (not extensions or file.suffix in extensions)
        ]
    except Exception as ex:
        logger.error(f'Ошибка при получении списка имен файлов из \'{directory}\'.', ex)
        return []


def recursively_yield_file_path(
    root_dir: str | Path, patterns: str | list[str] = '*'
) -> Generator[Path, None, None]:
    """
    Рекурсивно возвращает пути ко всем файлам, соответствующим заданным шаблонам, в указанной директории.

    Args:
        root_dir (str | Path): Корневая директория для поиска.
        patterns (str | list[str]): Шаблоны для фильтрации файлов.

    Yields:
        Path: Путь к файлу, соответствующему шаблону.

    Example:
        >>> from pathlib import Path
        >>> root_dir = Path('.')
        >>> for path in recursively_yield_file_path(root_dir, ['*.txt', '*.md']):
        ...    print(path)
        ./example.txt
        ./readme.md
    """
    # код исполняет рекурсивный поиск файлов в директории и возвращает генератор путей
    try:
        patterns = [patterns] if isinstance(patterns, str) else patterns
        for pattern in patterns:
            yield from Path(root_dir).rglob(pattern)
    except Exception as ex:
        logger.error(f'Ошибка при рекурсивном поиске файлов в \'{root_dir}\'.', ex)
        ...


def recursively_get_file_path(
    root_dir: str | Path,
    patterns: str | list[str] = '*'
) -> list[Path]:
    """
    Рекурсивно возвращает список путей ко всем файлам, соответствующим заданным шаблонам, в указанной директории.

    Args:
        root_dir (str | Path): Корневая директория для поиска.
        patterns (str | list[str]): Шаблоны для фильтрации файлов.

    Returns:
        list[Path]: Список путей к файлам, соответствующим шаблонам.

    Example:
        >>> from pathlib import Path
        >>> root_dir = Path('.')
        >>> paths = recursively_get_file_path(root_dir, ['*.txt', '*.md'])
        >>> print(paths)
        [Path('./example.txt'), Path('./readme.md')]
    """
    # код исполняет рекурсивный поиск файлов в директории и возвращает список путей
    try:
        patterns = [patterns] if isinstance(patterns, str) else patterns
        file_paths = []
        for pattern in patterns:
             file_paths.extend(Path(root_dir).rglob(pattern))
        return file_paths
    except Exception as ex:
        logger.error(f'Ошибка при рекурсивном поиске файлов в \'{root_dir}\'.', ex)
        return []


def recursively_read_text_files(
    root_dir: str | Path,
    patterns: str | list[str],
    as_list: bool = False
) -> list[str]:
    """
    Рекурсивно читает текстовые файлы из указанной корневой директории, соответствующие заданным шаблонам.

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
        >>> contents = recursively_read_text_files(root_dir, ['*.txt', '*.md'], as_list=True)
        >>> for line in contents:
        ...     print(line)
        Содержимое example.txt
        Первая строка readme.md
        Вторая строка readme.md
    """
    # код исполняет рекурсивное чтение текстовых файлов
    matches = []
    root_path = Path(root_dir)
    if not root_path.is_dir():
        logger.debug(f'Корневая директория \'{root_path}\' не существует или не является директорией.')
        return []

    if isinstance(patterns, str):
        patterns = [patterns]

    for file_path in recursively_get_file_path(root_path, patterns):
            try:
                with file_path.open('r', encoding='utf-8') as file:
                    if as_list:
                         matches.extend(file.readlines())
                    else:
                         matches.append(file.read())
            except Exception as ex:
                logger.error(f'Ошибка при чтении файла \'{file_path}\'.', ex)
    return matches


def get_directory_names(directory: str | Path) -> list[str]:
    """
    Возвращает список имен директорий из указанной директории.

    Args:
        directory (str | Path): Путь к директории, из которой нужно получить имена.

    Returns:
        list[str]: Список имен директорий, найденных в указанной директории.

    Example:
        >>> from pathlib import Path
        >>> directory = Path('.')
        >>> get_directory_names(directory)
        ['dir1', 'dir2']
    """
    # код исполняет получение списка имен директорий
    try:
        return [entry.name for entry in Path(directory).iterdir() if entry.is_dir()]
    except Exception as ex:
        logger.error(f'Ошибка при получении списка имен директорий из \'{directory}\'.', ex)
        return []


def remove_bom(path: str | Path) -> None:
    """
    Удаляет BOM из текстового файла или из всех файлов Python в директории.

    Args:
        path (str | Path): Путь к файлу или директории.

    Example:
        >>> from pathlib import Path
        >>> file_path = Path('example.txt')
        >>> with open(file_path, 'w', encoding='utf-8') as f:
        ...     f.write('\\ufeffПример текста с BOM')
        >>> remove_bom(file_path)
        >>> with open(file_path, 'r', encoding='utf-8') as f:
        ...     print(f.read())
        Пример текста с BOM
    """
    # код исполняет удаление BOM из файла или директории
    path = Path(path)
    if path.is_file():
        try:
            with path.open('r+', encoding='utf-8') as file:
                content = file.read().replace('\ufeff', '')
                file.seek(0)
                file.write(content)
                file.truncate()
        except Exception as ex:
            logger.error(f'Ошибка при удалении BOM из файла {path}.', ex)
            ...
    elif path.is_dir():
        for file_path in recursively_get_file_path(path, '*.py'):
            try:
                 with file_path.open('r+', encoding='utf-8') as f:
                    content = f.read().replace('\ufeff', '')
                    f.seek(0)
                    f.write(content)
                    f.truncate()
            except Exception as ex:
                logger.error(f'Ошибка при удалении BOM из файла {file_path}.', ex)
                ...
    else:
        logger.error(f'Указанный путь \'{path}\' не является файлом или директорией.')
        ...


def main() -> None:
    """Entry point for BOM removal in Python files."""
    #  удаляем BOM из всех файлов python в директории src
    root_dir = Path('..', 'src')
    logger.info(f'Starting BOM removal in {root_dir}')
    remove_bom(root_dir)


if __name__ == '__main__':
    main()
```