### Анализ кода модуля `src.utils.file`

**Качество кода**:
   - **Соответствие стандартам**: 7/10
   - **Плюсы**:
     - Хорошая структурированность модуля, разделение на функции.
     - Использование `Pathlib` для работы с путями.
     - Наличие подробных docstring для большинства функций.
     - Использование генераторов для эффективной работы с файлами.
     - Логирование ошибок через `logger.error`.
   - **Минусы**:
     - Смешивание одинарных и двойных кавычек в коде.
     - Использование стандартного `json.dump` вместо `j_dumps` из `src.utils.jjson`.
     - Не везде используется `logger.error` для обработки ошибок, местами `...` и `return None`.
     - Использование стандартного `open` вместо `Path.open` для чтения файла в некоторых функциях.
     - Есть дублирование логики и кода (например, чтение файлов).
     - Комментарии не всегда соответствуют стандарту RST.
     -  Не все функции имеют `example` в `docstring`.

**Рекомендации по улучшению**:
   - Необходимо унифицировать использование кавычек: одинарные кавычки для строк кода, двойные — для вывода и логгирования.
   - Заменить `json.dump` на `j_dumps` из `src.utils.jjson`.
   - Везде использовать `logger.error` для обработки ошибок и исключений.
   - Использовать `Path.open` везде, где это возможно.
   - Рефакторинг кода для устранения дублирования и упрощения логики (например, общие функции для чтения и обработки файлов).
   - Привести `docstring` к стандарту RST.
   - Добавить `example` во все `docstring`.
   - Добавить `rtype` во все `docstring`.
   - В функции `remove_bom` использовать `Path.rglob` вместо `os.walk` для более эффективной работы с файлами.
   - Использовать `from src.logger.logger import logger` для явного импорта логгера.
   - Добавить  `try-except` в `recursively_yield_file_path`.
   - Переписать `recursively_read_text_files` с использованием `pathlib`, чтобы не использовать `os.walk`.
   - Добавить возможность фильтрации по расширениям в `recursively_read_text_files`.

**Оптимизированный код**:

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
import os #  import os
import fnmatch #  import fnmatch
from pathlib import Path #  from pathlib import Path
from typing import List, Optional, Union, Generator # from typing import List, Optional, Union, Generator
from src.logger.logger import logger # from src.logger.logger import logger
from src.utils.jjson import j_dumps #  импорт j_dumps
MODE = 'dev' # Константа режима # MODE = 'dev'


def save_text_file(
    file_path: str | Path,
    data: str | list[str] | dict,
    mode: str = 'w'
) -> bool:
    """
    Сохраняет данные в текстовый файл.

    :param file_path: Путь к файлу для сохранения.
    :type file_path: str | Path
    :param data: Данные для записи. Могут быть строкой, списком строк или словарем.
    :type data: str | list[str] | dict
    :param mode: Режим записи файла ('w' для записи, 'a' для добавления).
    :type mode: str, optional
    :return: True, если файл успешно сохранен, False в противном случае.
    :rtype: bool
    :raises Exception: При возникновении ошибки при записи в файл.

    Пример:
        >>> from pathlib import Path
        >>> file_path = Path('example.txt')
        >>> data = 'Пример текста'
        >>> result = save_text_file(file_path, data)
        >>> print(result)
        True
    """
    try:
        file_path = Path(file_path) #  file_path = Path(file_path)
        file_path.parent.mkdir(parents = True, exist_ok = True) #  file_path.parent.mkdir(parents=True, exist_ok=True)

        with file_path.open(mode, encoding = 'utf-8') as file: # with file_path.open(mode, encoding='utf-8') as file:
            if isinstance(data, list): # if isinstance(data, list):
                file.writelines(f'{line}\n' for line in data) # file.writelines(f'{line}\\n' for line in data)
            elif isinstance(data, dict): #  elif isinstance(data, dict):
                json.dump(data, file, ensure_ascii = False, indent = 4) # j_dumps(data, file, ensure_ascii = False, indent = 4) # json.dump(data, file, ensure_ascii=False, indent=4)
            else: # else:
                file.write(data) # file.write(data)
        return True # return True
    except Exception as ex: #  except Exception as ex:
        logger.error(f'Ошибка при сохранении файла {file_path}.', exc_info = ex) # logger.error(f'Ошибка при сохранении файла {file_path}.', ex)
        return False # return False
    

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
        :return: Генератор строк, строка, список строк или None в случае ошибки.
        :rtype: Generator[str, None, None] | str | list[str] | None
        :raises Exception: При возникновении ошибки при чтении файла.

    Example:
        >>> from pathlib import Path
        >>> file_path = Path('example.txt')
        >>> content = read_text_file(file_path)
        >>> if content:
        ...    print(f'File content: {content[:100]}...')
        File content: Пример текста...

    Функция `read_text_file` может возвращать несколько разных типов данных в зависимости от входных параметров:

    Возвращаемые значения:
    ----------------------

    - Generator[str, None, None] (Генератор строк):
        Генератор при итерации выдаёт строки из файла(ов) по одной. Эффективно для работы с большими файлами, так как они не загружаются полностью в память.
        - Когда:
            `file_path` – это файл и `as_list` равен `True`.
            `file_path` – это директория, `recursive` равен `True` и `as_list` равен `True`. При этом в генератор попадают строки из всех найденных файлов.
            `file_path` – это директория, `recursive` равен `False` и `as_list` равен `True`. При этом в генератор попадают строки из всех найденных файлов в текущей директории.

    - str (Строка):
        Содержимое файла или объединенное содержимое всех файлов в виде одной строки.
        - Когда:
            `file_path` – это файл и `as_list` равен `False`.
            `file_path` – это директория, `recursive` равен `False` и `as_list` равен `False`. При этом возвращается объединенная строка, состоящая из содержимого всех файлов в директории, разделенных символами новой строки (`\n`).
            `file_path` – это директория, `recursive` равен `True` и `as_list` равен `False`. При этом возвращается объединенная строка, состоящая из содержимого всех файлов в директории и её поддиректориях, разделенных символами новой строки (`\n`).

    - list[str] (Список строк):
        Этот тип явно не возвращается функцией, однако когда `file_path` – это директория, `recursive` равен `True` и `as_list` равен `True` - функция возвращает генератор, который можно преобразовать в список при помощи `list()`
        - Когда:
            `file_path` – не является ни файлом, ни директорией.
            Произошла ошибка при чтении файла или директории (например, файл не найден, ошибка доступа и т.п.).

    Note:
        Если вы хотите прочитать содержимое файла построчно (особенно для больших файлов) используйте `as_list = True`. В этом случае вы получите генератор строк.
        Если вы хотите получить всё содержимое файла в виде одной строки используйте `as_list = False`.
        Если вы работаете с директорией, `recursive = True` будет обходить все поддиректории.
        `extensions` и `patterns` позволят вам фильтровать файлы при работе с директорией.
        `chunk_size` позволяет оптимизировать работу с большими файлами при чтении их по частям.
        `None` будет возвращён в случае ошибок.

    Важно помнить:
        В случае чтения директории, если `as_list=False`, функция объединяет все содержимое найденных файлов в одну строку. Это может потребовать много памяти, если файлов много или они большие.
        Функция полагается на другие функции-помощники (`_read_file_lines_generator`, `_read_file_content`, `recursively_get_file_path`, `yield_text_from_files`), которые здесь не определены и их поведение влияет на результат `read_text_file`.
    """
    try:
        path = Path(file_path) # path = Path(file_path)
        if path.is_file(): # if path.is_file():
            if as_list: # if as_list:
                return _read_file_lines_generator(path, chunk_size = chunk_size) # return _read_file_lines_generator(path, chunk_size=chunk_size)
            else: # else:
                return _read_file_content(path, chunk_size = chunk_size) # return _read_file_content(path, chunk_size=chunk_size)
        elif path.is_dir(): # elif path.is_dir():
            if recursive: # if recursive:
                if patterns: #  if patterns:
                    files = recursively_get_file_path(path, patterns) # files = recursively_get_file_path(path, patterns)
                else: # else:
                    files = [ # files = [
                        p for p in path.rglob('*') if p.is_file() and (not extensions or p.suffix in extensions) # p for p in path.rglob('*') if p.is_file() and (not extensions or p.suffix in extensions)
                    ] # ]
                if as_list: # if as_list:
                    return ( # return (
                        line # line
                        for file in files # for file in files
                        for line in yield_text_from_files(file, as_list = True, chunk_size = chunk_size) # for line in yield_text_from_files(file, as_list=True, chunk_size=chunk_size)
                    ) # )
                else: # else:
                    return '\n'.join(filter(None, [read_text_file(p, chunk_size = chunk_size) for p in files])) # return '\\n'.join(filter(None, [read_text_file(p, chunk_size=chunk_size) for p in files]))
            else: # else:
                files = [ # files = [
                    p for p in path.iterdir() if p.is_file() and (not extensions or p.suffix in extensions) # p for p in path.iterdir() if p.is_file() and (not extensions or p.suffix in extensions)
                ] # ]
                if as_list: # if as_list:
                    return (line for file in files for line in read_text_file(file, as_list = True, chunk_size = chunk_size) ) # return (line for file in files for line in read_text_file(file, as_list=True, chunk_size=chunk_size) )
                else: # else:
                    return '\n'.join(filter(None, [read_text_file(p, chunk_size = chunk_size) for p in files])) # return '\\n'.join(filter(None, [read_text_file(p, chunk_size=chunk_size) for p in files]))
        else: # else:
            logger.error(f'Путь \'{file_path}\' не является файлом или директорией.') # logger.error(f'Путь \'{file_path}\' не является файлом или директорией.')
            return None # return None
    except Exception as ex: # except Exception as ex:
        logger.error(f'Ошибка при чтении файла/директории {file_path}.', exc_info = ex) # logger.error(f'Ошибка при чтении файла/директории {file_path}.', ex)
        return None # return None
    

def read_text_file(
    file_path: Union[str, Path],
    as_list: bool = False,
    extensions: Optional[list[str]] = None,
    exc_info: bool = True,
) -> str | list[str] | None:
    """
    Читает содержимое файла.

    :param file_path: Путь к файлу или директории.
    :type file_path: str | Path
    :param as_list: Если True, возвращает содержимое в виде списка строк.
    :type as_list: bool, optional
    :param extensions: Список расширений файлов для включения при чтении директории.
    :type extensions: list[str], optional
    :param exc_info: Если True, логирует traceback при ошибке.
    :type exc_info: bool, optional
    :return: Содержимое файла как строка или список строк, или None, если произошла ошибка.
    :rtype: str | list[str] | None
    :raises Exception: При возникновении ошибки при чтении файла.
    
    Example:
        >>> from pathlib import Path
        >>> file_path = Path('example.txt')
        >>> content = read_text_file(file_path)
        >>> if content:
        ...    print(f'File content: {content[:100]}...')
        File content: Пример текста...

        >>> file_path = Path('example.txt')
        >>> content_list = read_text_file(file_path, as_list = True)
        >>> print(content_list)
        ['Пример текста\\n']

    """
    try:
        path = Path(file_path) # path = Path(file_path)
        if path.is_file(): # if path.is_file():
            with path.open('r', encoding = 'utf-8') as f: # with path.open('r', encoding='utf-8') as f:
                return f.readlines() if as_list else f.read() # return f.readlines() if as_list else f.read()
        elif path.is_dir(): # elif path.is_dir():
            files = [ # files = [
                p for p in path.rglob('*') if p.is_file() and (not extensions or p.suffix in extensions) # p for p in path.rglob('*') if p.is_file() and (not extensions or p.suffix in extensions)
            ] # ]
            contents = [read_text_file(p, as_list) for p in files] # contents = [read_text_file(p, as_list) for p in files]
            return [item for sublist in contents if sublist for item in sublist] if as_list else '\n'.join(filter(None, contents)) # return [item for sublist in contents if sublist for item in sublist] if as_list else "\\n".join(filter(None, contents))
        else: # else:
            logger.warning(f'Path \'{file_path}\' is invalid.') # logger.warning(f"Path '{file_path}' is invalid.")
            return None # return
    except Exception as ex: # except Exception as ex:
        logger.error(f'Failed to read file {file_path}.', exc_info = ex) # logger.error(f"Failed to read file {file_path}.", ex, exc_info=exc_info)
        return None # return
    

def yield_text_from_files(
    file_path: str | Path,
    as_list: bool = False,
    chunk_size: int = 8192
) -> Generator[str, None, None] | str | None:
    """
    Читает содержимое файла и возвращает его в виде генератора строк или одной строки.

    :param file_path: Путь к файлу.
    :type file_path: str | Path
    :param as_list: Если True, возвращает генератор строк.
    :type as_list: bool, optional
    :param chunk_size: Размер чанка для чтения файла в байтах.
    :type chunk_size: int, optional
    :return: Генератор строк, объединенная строка или None в случае ошибки.
    :rtype: Generator[str, None, None] | str | None
    :raises Exception: При возникновении ошибки при чтении файла.
    
    :yield: Строки из файла, если `as_list` is `True`.
    :rtype: str
    
    
    Пример:
        >>> from pathlib import Path
        >>> file_path = Path('example.txt')
        >>> for line in yield_text_from_files(file_path, as_list=True):
        ...     print(line)
        Первая строка файла
        Вторая строка файла
    """
    try:
        path = Path(file_path) # path = Path(file_path)
        if path.is_file(): # if path.is_file():
            if as_list: # if as_list:
                 yield from  _read_file_lines_generator(path, chunk_size = chunk_size) # yield from  _read_file_lines_generator(path, chunk_size=chunk_size)
            else: # else:
                yield _read_file_content(path, chunk_size = chunk_size) # yield _read_file_content(path, chunk_size=chunk_size)
        else: # else:
             logger.error(f'Путь \'{file_path}\' не является файлом.') # logger.error(f'Путь \'{file_path}\' не является файлом.')
             return None # return None
    except Exception as ex: # except Exception as ex:
        logger.error(f'Ошибка при чтении файла {file_path}.', exc_info = ex) # logger.error(f'Ошибка при чтении файла {file_path}.', ex)
        return None # return None
    

def _read_file_content(file_path: Path, chunk_size: int) -> str:
    """
    Читает содержимое файла по чанкам и возвращает как строку.

    :param file_path: Путь к файлу для чтения.
    :type file_path: Path
    :param chunk_size: Размер чанка для чтения файла в байтах.
    :type chunk_size: int
    :return: Содержимое файла в виде строки.
    :rtype: str
    :raises Exception: При возникновении ошибки при чтении файла.
    """
    with file_path.open('r', encoding = 'utf-8') as f: # with file_path.open('r', encoding='utf-8') as f:
        content = '' # content = ''
        while True: # while True:
            chunk = f.read(chunk_size) # chunk = f.read(chunk_size)
            if not chunk: # if not chunk:
                break # break
            content += chunk # content += chunk
        return content # return content
    

def _read_file_lines_generator(file_path: Path, chunk_size: int) -> Generator[str, None, None]:
    """
    Читает файл по строкам с помощью генератора.

    :param file_path: Путь к файлу для чтения.
    :type file_path: Path
    :param chunk_size: Размер чанка для чтения файла в байтах.
    :type chunk_size: int
    :yield: Строки из файла.
    :rtype: str
    :raises Exception: При возникновении ошибки при чтении файла.
    """
    with file_path.open('r', encoding = 'utf-8') as f: # with file_path.open('r', encoding='utf-8') as f:
         while True: # while True:
                chunk = f.read(chunk_size) # chunk = f.read(chunk_size)
                if not chunk: # if not chunk:
                    break # break
                lines = chunk.splitlines() # lines = chunk.splitlines()
                # Если чанк не закончился полной строкой, то последнюю строку добавляем к следующему чанку
                if len(lines)>0 and not chunk.endswith('\n'): # if len(lines) > 0 and not chunk.endswith('\\n'):
                     next_chunk = f.read(1) # next_chunk = f.read(1)
                     if next_chunk != '': # if next_chunk != '':
                        lines[-1] = lines[-1] + next_chunk # lines[-1] = lines[-1] + next_chunk
                     else: # else:
                        yield from lines # yield from lines
                        break # break
                
                yield from lines # yield from lines
    

def get_filenames_from_directory(
    directory: str | Path, extensions: str | list[str] = '*'
) -> list[str]:
    """
    Возвращает список имен файлов в директории, опционально отфильтрованных по расширению.

    :param directory: Путь к директории для поиска.
    :type directory: str | Path
    :param extensions: Расширения для фильтрации. По умолчанию '*'.
    :type extensions: str | list[str], optional
    :return: Список имен файлов, найденных в директории.
    :rtype: list[str]
    :raises Exception: При возникновении ошибки при получении списка имен файлов.

    Пример:
        >>> from pathlib import Path
        >>> directory = Path('.')
        >>> get_filenames_from_directory(directory, ['.txt', '.md'])
        ['example.txt', 'readme.md']
    """
    try:
        path = Path(directory) # path = Path(directory)
        if isinstance(extensions, str): # if isinstance(extensions, str):
            extensions = [extensions] if extensions != '*' else [] # extensions = [extensions] if extensions != '*' else []
        extensions = [ext if ext.startswith('.') else f'.{ext}' for ext in extensions] # extensions = [ext if ext.startswith('.') else f'.{ext}' for ext in extensions]

        return [ # return [
            file.name # file.name
            for file in path.iterdir() # for file in path.iterdir()
            if file.is_file() and (not extensions or file.suffix in extensions) # if file.is_file() and (not extensions or file.suffix in extensions)
        ] # ]
    except Exception as ex: # except Exception as ex:
        logger.error(f'Ошибка при получении списка имен файлов из \'{directory}\'.', exc_info = ex) # logger.error(f'Ошибка при получении списка имен файлов из \'{directory}\'.', ex)
        return [] # return []
    

def recursively_yield_file_path(
    root_dir: str | Path, patterns: str | list[str] = '*'
) -> Generator[Path, None, None]:
    """
    Рекурсивно возвращает пути ко всем файлам, соответствующим заданным шаблонам, в указанной директории.

    :param root_dir: Корневая директория для поиска.
    :type root_dir: str | Path
    :param patterns: Шаблоны для фильтрации файлов.
    :type patterns: str | list[str], optional
    :yield: Путь к файлу, соответствующему шаблону.
    :rtype: Path
    :raises Exception: При возникновении ошибки при рекурсивном поиске файлов.
   
    Пример:
        >>> from pathlib import Path
        >>> root_dir = Path('.')
        >>> for path in recursively_yield_file_path(root_dir, ['*.txt', '*.md']):
        ...    print(path)
        ./example.txt
        ./readme.md
    """
    try:
        patterns = [patterns] if isinstance(patterns, str) else patterns # patterns = [patterns] if isinstance(patterns, str) else patterns
        for pattern in patterns: # for pattern in patterns:
            yield from Path(root_dir).rglob(pattern) # yield from Path(root_dir).rglob(pattern)
    except Exception as ex: # except Exception as ex:
         logger.error(f'Ошибка при рекурсивном поиске файлов в \'{root_dir}\'.', exc_info = ex) # logger.error(f'Ошибка при рекурсивном поиске файлов в \'{root_dir}\'.', ex)
    

def recursively_get_file_path(
    root_dir: str | Path,
    patterns: str | list[str] = '*'
) -> list[Path]:
    """
    Рекурсивно возвращает список путей ко всем файлам, соответствующим заданным шаблонам, в указанной директории.

    :param root_dir: Корневая директория для поиска.
    :type root_dir: str | Path
    :param patterns: Шаблоны для фильтрации файлов.
    :type patterns: str | list[str], optional
    :return: Список путей к файлам, соответствующим шаблонам.
    :rtype: list[Path]
    :raises Exception: При возникновении ошибки при рекурсивном поиске файлов.
    
    Пример:
        >>> from pathlib import Path
        >>> root_dir = Path('.')
        >>> paths = recursively_get_file_path(root_dir, ['*.txt', '*.md'])
        >>> print(paths)
        [Path('./example.txt'), Path('./readme.md')]
    """
    try:
        file_paths = [] # file_paths = []
        patterns = [patterns] if isinstance(patterns, str) else patterns # patterns = [patterns] if isinstance(patterns, str) else patterns
        for pattern in patterns: # for pattern in patterns:
            file_paths.extend(Path(root_dir).rglob(pattern)) # file_paths.extend(Path(root_dir).rglob(pattern))
        return file_paths # return file_paths
    except Exception as ex: # except Exception as ex:
        logger.error(f'Ошибка при рекурсивном поиске файлов в \'{root_dir}\'.', exc_info = ex) # logger.error(f'Ошибка при рекурсивном поиске файлов в \'{root_dir}\'.', ex)
        return [] # return []
    

def recursively_read_text_files(
    root_dir: str | Path,
    patterns: str | list[str],
    as_list: bool = False,
    extensions: Optional[list[str]] = None,
) -> list[str]:
    """
    Рекурсивно читает текстовые файлы из указанной корневой директории, соответствующие заданным шаблонам.
    
    :param root_dir: Путь к корневой директории для поиска.
    :type root_dir: str | Path
    :param patterns: Шаблон(ы) имени файла для фильтрации. Может быть как одиночным шаблоном (например, '*.txt'), так и списком.
    :type patterns: str | list[str]
    :param as_list: Если True, то возвращает содержимое файла как список строк. По умолчанию `False`.
    :type as_list: bool, optional
    :param extensions: Список расширений файлов для включения при чтении директории.
    :type extensions: list[str], optional
    :return: Список содержимого файлов (или список строк, если `as_list=True`), соответствующих заданным шаблонам.
    :rtype: list[str]
    :raises Exception: При возникновении ошибки при чтении файла.
   
    Пример:
        >>> from pathlib import Path
        >>> root_dir = Path('.')
        >>> contents = recursively_read_text_files(root_dir, ['*.txt', '*.md'], as_list=True)
        >>> for line in contents:
        ...     print(line)
        Содержимое example.txt
        Первая строка readme.md
        Вторая строка readme.md
    """
    matches = [] # matches = []
    root_path = Path(root_dir) # root_path = Path(root_dir)

    if not root_path.is_dir(): # if not root_path.is_dir():
        logger.debug(f'Корневая директория \'{root_path}\' не существует или не является директорией.') # logger.debug(f'Корневая директория \'{root_path}\' не существует или не является директорией.')
        return [] # return []

    print(f'Поиск в директории: {root_path}') # print(f'Поиск в директории: {root_path}')

    if isinstance(patterns, str): # if isinstance(patterns, str):
        patterns = [patterns] # patterns = [patterns]

    for file_path in recursively_get_file_path(root_path, patterns):  #  используем  recursively_get_file_path
        try:
            with file_path.open('r', encoding='utf-8') as file: # with file_path.open('r', encoding='utf-8') as file:
                if as_list: # if as_list:
                    matches.extend(file.readlines()) # matches.extend(file.readlines())
                else: # else:
                    matches.append(file.read()) # matches.append(file.read())
        except Exception as ex: # except Exception as ex:
            logger.error(f'Ошибка при чтении файла \'{file_path}\'.', exc_info=ex) # logger.error(f'Ошибка при чтении файла \'{file_path}\'.', ex)

    return matches # return matches
    

def get_directory_names(directory: str | Path) -> list[str]:
    """
    Возвращает список имен директорий из указанной директории.

    :param directory: Путь к директории, из которой нужно получить имена.
    :type directory: str | Path
    :return: Список имен директорий, найденных в указанной директории.
    :rtype: list[str]
    :raises Exception: При возникновении ошибки при получении списка имен директорий.

    Пример:
        >>> from pathlib import Path
        >>> directory = Path('.')
        >>> get_directory_names(directory)
        ['dir1', 'dir2']
    """
    try:
        return [entry.name for entry in Path(directory).iterdir() if entry.is_dir()] # return [entry.name for entry in Path(directory).iterdir() if entry.is_dir()]
    except Exception as ex: # except Exception as ex:
        logger.error(f'Ошибка при получении списка имен директорий из \'{directory}\'.', exc_info = ex) # logger.error(f'Ошибка при получении списка имен директорий из \'{directory}\'.', ex)
        return [] # return []
    

def remove_bom(path: str | Path) -> None:
    """
    Удаляет BOM из текстового файла или из всех файлов Python в директории.

    :param path: Путь к файлу или директории.
    :type path: str | Path
    :raises Exception: При возникновении ошибки при удалении BOM из файла.
   
    Пример:
        >>> from pathlib import Path
        >>> file_path = Path('example.txt')
        >>> with open(file_path, 'w', encoding='utf-8') as f:
        ...     f.write('\\ufeffПример текста с BOM')
        >>> remove_bom(file_path)
        >>> with open(file_path, 'r', encoding='utf-8') as f:
        ...     print(f.read())
        Пример текста с BOM
    """
    path = Path(path) # path = Path(path)
    if path.is_file(): # if path