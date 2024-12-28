# Анализ кода модуля `file.py`

**Качество кода**
8
-  Плюсы
    - Код хорошо структурирован и разбит на отдельные функции, каждая из которых выполняет свою задачу.
    - Используется `pathlib` для работы с путями, что является хорошей практикой.
    - Присутствует логирование ошибок с использованием `src.logger.logger`.
    - Код в целом соответствует PEP8.
    - Присутствует документация к функциям, хотя и не полная, но уже хорошо.
-  Минусы
    - Не используется `j_loads` или `j_loads_ns` из `src.utils.jjson` для чтения файлов.
    - Есть некоторые функции, которые можно улучшить.
    -  Отсутствует docstring для модуля в формате `reStructuredText`.
    - В некоторых местах используется `try-except` без необходимости, можно заменить на более явную обработку ошибок.
    - Есть дублирование кода (например, в `recursively_get_file_path` и `recursively_yield_file_path`)

**Рекомендации по улучшению**

1.  **Документация**:
    - Добавить docstring в начале модуля в формате `reStructuredText`.
    - Полностью переписать docstring для функций в формате `reStructuredText` с описанием параметров, возвращаемых значений, возможных исключений и примерами использования.
2.  **Использование `j_loads`**:
    - Заменить `json.load` на `j_loads` или `j_loads_ns` из `src.utils.jjson` для чтения файлов JSON.
3.  **Обработка ошибок**:
    - Убрать избыточные блоки `try-except`, заменив их на `logger.error` с последующим возвращением значения по умолчанию.
4.  **Рефакторинг**:
    - Объединить `recursively_get_file_path` и `recursively_yield_file_path` в одну функцию.
    - Пересмотреть логику функции `read_text_file` для случаев, когда `path` является директорией и сделать её более читаемой.
5.  **Логирование**:
    - В некоторых местах используется `logger.warning`, когда следует использовать `logger.error`.
    - Добавить логирование для успешных операций, например, когда файл успешно прочитан или сохранен.
6.  **Согласование**:
    - Привести имена функций, переменных и импортов к единому стилю с ранее обработанными файлами.
    - Все переменные, функции, модули должны быть документированы в формате `reStructuredText`.

**Оптимизиробанный код**

```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
Модуль для работы с файлами и директориями
=========================================================================================

Этот модуль предоставляет набор функций для выполнения различных операций с файлами и директориями,
таких как чтение, запись, поиск, удаление BOM и т.д.

Пример использования
--------------------

Пример использования функции :func:`save_text_file`:

.. code-block:: python

    from pathlib import Path
    from src.utils.file import save_text_file
    
    file_path = Path("example.txt")
    data = "Пример текста для записи в файл"
    save_text_file(data, file_path)

    
Пример использования функции :func:`read_text_file`:

.. code-block:: python

    from pathlib import Path
    from src.utils.file import read_text_file
    
    file_path = Path("example.txt")
    content = read_text_file(file_path)
    print(content)
"""


import os
import fnmatch
from pathlib import Path
from typing import List, Optional, Union, Generator
from src.logger.logger import logger
from src.utils.jjson import j_loads  # corrected import


def save_text_file(
    data: str | list[str] | dict,
    file_path: Union[str, Path],
    mode: str = 'w',
    exc_info: bool = True,
) -> bool:
    """
    Сохраняет данные в текстовый файл.

    :param data: Данные для записи (строка, список строк или словарь).
    :type data: str | list[str] | dict
    :param file_path: Путь к файлу, куда будут сохранены данные.
    :type file_path: str | Path
    :param mode: Режим записи (``'w'`` для записи, ``'a'`` для добавления). По умолчанию ``'w'``.
    :type mode: str
    :param exc_info: Если ``True``, то информация об ошибке будет добавлена в лог. По умолчанию ``True``.
    :type exc_info: bool
    :raises Exception: Если произошла ошибка при сохранении файла.
    :return: Возвращает ``True``, если файл успешно сохранен, иначе ``False``.
    :rtype: bool

    :Example:
    
    .. code-block:: python
    
        from pathlib import Path
        from src.utils.file import save_text_file
    
        file_path = Path("example.txt")
        data = "Пример текста для записи в файл"
        save_text_file(data, file_path)
    """
    try:
        # Преобразует путь к файлу в объект Path
        file_path = Path(file_path)
        # Создает родительские директории, если они не существуют
        file_path.parent.mkdir(parents=True, exist_ok=True)

        # Открывает файл в указанном режиме
        with file_path.open(mode, encoding='utf-8') as file:
            # Проверяет, является ли data списком
            if isinstance(data, list):
                # Записывает каждую строку из списка в файл с новой строки
                file.writelines(f'{line}\n' for line in data)
            # Проверяет, является ли data словарем
            elif isinstance(data, dict):
                 # Записывает словарь в файл в формате JSON
                j_loads(data, file, ensure_ascii=False, indent=4)
            # В противном случае записывает данные как строку
            else:
                file.write(data)
        logger.info(f"Файл успешно сохранен в {file_path}")
        return True
    except Exception as ex:
        # Логирует ошибку с информацией о файле и исключении
        logger.error(f'Ошибка сохранения файла {file_path}.', ex, exc_info=exc_info)
        return False

def read_text_file(
    file_path: Union[str, Path],
    as_list: bool = False,
    extensions: Optional[list[str]] = None,
    exc_info: bool = True,
) -> Union[str, list[str], None]:
    """
    Читает содержимое файла или нескольких файлов в директории.

    :param file_path: Путь к файлу или директории.
    :type file_path: str | Path
    :param as_list: Если ``True``, возвращает содержимое файла в виде списка строк. По умолчанию ``False``.
    :type as_list: bool
    :param extensions: Список расширений файлов для чтения из директории. По умолчанию ``None``.
    :type extensions: list[str], optional
    :param exc_info: Если ``True``, то информация об ошибке будет добавлена в лог. По умолчанию ``True``.
    :type exc_info: bool
    :return: Содержимое файла в виде строки или списка строк, или ``None`` в случае ошибки.
    :rtype: str | list[str] | None

    :Example:
    
    .. code-block:: python
    
        from pathlib import Path
        from src.utils.file import read_text_file
    
        file_path = Path("example.txt")
        content = read_text_file(file_path)
        print(content)
    """
    path = Path(file_path)
    try:
        # Проверяет, является ли путь файлом
        if path.is_file():
            # Открывает файл для чтения и возвращает содержимое
            with path.open('r', encoding='utf-8') as f:
                logger.info(f"Файл успешно прочитан: {file_path}")
                return f.readlines() if as_list else f.read()
        # Проверяет, является ли путь директорией
        elif path.is_dir():
            # Получает список всех файлов в директории, включая поддиректории, с учетом расширений
            files = [
                p for p in path.rglob('*') if p.is_file() and (not extensions or p.suffix in extensions)
            ]
            # Рекурсивно читает содержимое каждого файла
            contents = [read_text_file(p, as_list, exc_info=exc_info) for p in files]
            # Возвращает список строк, если as_list True, иначе возвращает строку
            if as_list:
                return [item for sublist in contents if sublist for item in sublist]
            else:
                return '\n'.join(filter(None, contents))
        else:
            logger.warning(f"Путь \'{file_path}\' не является файлом или директорией.")
            return None
    except Exception as ex:
        # Логирует ошибку и возвращает None
        logger.error(f'Ошибка чтения файла {file_path}.', ex, exc_info=exc_info)
        return None

def get_filenames(
    directory: Union[str, Path],
    extensions: Union[str, list[str]] = '*',
    exc_info: bool = True,
) -> list[str]:
    """
    Получает список имен файлов в указанной директории.

    :param directory: Путь к директории.
    :type directory: str | Path
    :param extensions: Расширения файлов для фильтрации. Может быть строкой или списком. По умолчанию ``'*'`` (все файлы).
    :type extensions: str | list[str]
    :param exc_info: Если ``True``, то информация об ошибке будет добавлена в лог. По умолчанию ``True``.
    :type exc_info: bool
    :return: Список имен файлов в директории.
    :rtype: list[str]

     :Example:
    
    .. code-block:: python
    
        from pathlib import Path
        from src.utils.file import get_filenames
    
        directory = Path(".")
        filenames = get_filenames(directory)
        print(filenames)
    """
    try:
         # Преобразует путь к директории в объект Path
        path = Path(directory)
        # Преобразует расширения в список, если это строка
        if isinstance(extensions, str):
            extensions = [extensions] if extensions != '*' else []
        # Добавляет точку к расширениям, если ее нет
        extensions = [ext if ext.startswith('.') else f'.{ext}' for ext in extensions]

        # Возвращает список имен файлов в директории, удовлетворяющих условиям
        return [
            file.name
            for file in path.iterdir()
            if file.is_file() and (not extensions or file.suffix in extensions)
        ]
    except Exception as ex:
        # Логирует ошибку и возвращает пустой список
        logger.warning(f'Ошибка получения имен файлов в директории \'{directory}\'.', ex, exc_info=exc_info)
        return []

def recursively_get_file_paths(
    root_dir: Union[str, Path],
    patterns: Union[str, list[str]] = '*',
    exc_info: bool = True,
) -> list[Path]:
    """
    Рекурсивно получает список путей к файлам, соответствующих заданным шаблонам.

    :param root_dir: Корневая директория для поиска.
    :type root_dir: str | Path
    :param patterns: Шаблоны для фильтрации файлов. Может быть строкой или списком. По умолчанию ``'*'`` (все файлы).
    :type patterns: str | list[str]
    :param exc_info: Если ``True``, то информация об ошибке будет добавлена в лог. По умолчанию ``True``.
    :type exc_info: bool
    :return: Список путей к файлам, соответствующих заданным шаблонам.
    :rtype: list[Path]

    :Example:
    
    .. code-block:: python
    
        from pathlib import Path
        from src.utils.file import recursively_get_file_paths
    
        root_dir = Path(".")
        patterns = ["*.txt", "*.md"]
        file_paths = recursively_get_file_paths(root_dir, patterns)
        print(file_paths)
    """
    try:
        # Преобразует шаблоны в список, если это строка
        patterns = [patterns] if isinstance(patterns, str) else patterns
        file_paths = []
        # Для каждого шаблона добавляет пути файлов в список
        for pattern in patterns:
            file_paths.extend(Path(root_dir).rglob(pattern))
        logger.info(f"Успешно найдены файлы в: {root_dir},  по паттерну {patterns}")
        return file_paths
    except Exception as ex:
        # Логирует ошибку и возвращает пустой список
        logger.error(f'Ошибка поиска файлов в директории \'{root_dir}\'.', ex, exc_info=exc_info)
        return []
    
def recursively_yield_file_path(
    root_dir: Union[str, Path],
    patterns: Union[str, list[str]] = '*',
    exc_info: bool = True,
) -> Generator[Path, None, None]:
    """
    Рекурсивно генерирует пути к файлам, соответствующих заданным шаблонам.

    :param root_dir: Корневая директория для поиска.
    :type root_dir: str | Path
    :param patterns: Шаблоны для фильтрации файлов. Может быть строкой или списком. По умолчанию ``'*'`` (все файлы).
    :type patterns: str | list[str]
    :param exc_info: Если ``True``, то информация об ошибке будет добавлена в лог. По умолчанию ``True``.
    :type exc_info: bool
    :yield: Путь к файлу, соответствующий заданным шаблонам.
    :rtype: Generator[Path, None, None]

    :Example:
    
    .. code-block:: python
    
        from pathlib import Path
        from src.utils.file import recursively_yield_file_path
    
        root_dir = Path(".")
        patterns = ["*.txt", "*.md"]
        for file_path in recursively_yield_file_path(root_dir, patterns):
            print(file_path)
    """
    try:
        # Преобразует шаблоны в список, если это строка
        patterns = [patterns] if isinstance(patterns, str) else patterns
        # Для каждого шаблона генерирует пути файлов
        for pattern in patterns:
            yield from Path(root_dir).rglob(pattern)
    except Exception as ex:
        # Логирует ошибку
        logger.error(f'Ошибка поиска файлов в директории \'{root_dir}\'.', ex, exc_info=exc_info)

def recursively_read_text_files(
    root_dir: str | Path,
    patterns: str | list[str],
    as_list: bool = False,
    exc_info: bool = True,
) -> list[str]:
    """
    Рекурсивно читает текстовые файлы, соответствующие заданным шаблонам.

    :param root_dir: Корневая директория для поиска.
    :type root_dir: str | Path
    :param patterns: Шаблоны для фильтрации файлов. Может быть строкой или списком.
    :type patterns: str | list[str]
    :param as_list: Если ``True``, возвращает содержимое файла в виде списка строк. По умолчанию ``False``.
    :type as_list: bool
    :param exc_info: Если ``True``, то информация об ошибке будет добавлена в лог. По умолчанию ``True``.
    :type exc_info: bool
    :return: Список содержимого файлов (или строк, если ``as_list=True``), соответствующих заданным шаблонам.
    :rtype: list[str]
    
    :Example:

    .. code-block:: python

        from pathlib import Path
        from src.utils.file import recursively_read_text_files
        
        root_dir = Path(".")
        patterns = ["*.txt", "*.md"]
        content = recursively_read_text_files(root_dir, patterns, as_list=True)
        for line in content:
            print(line)
    """
    matches = []
    root_path = Path(root_dir)

    # Проверяет, является ли путь директорией
    if not root_path.is_dir():
        logger.debug(f"Директория \'{root_path}\' не существует или не является директорией.")
        return []

    logger.info(f"Поиск в директории: {root_path}")

    # Нормализует шаблоны в список
    if isinstance(patterns, str):
        patterns = [patterns]

    # Проходит по всем файлам в директории и ее поддиректориях
    for root, _, files in os.walk(root_path):
        for filename in files:
            # Проверяет, соответствует ли имя файла одному из шаблонов
            if any(fnmatch.fnmatch(filename, pattern) for pattern in patterns):
                file_path = Path(root) / filename

                try:
                     # Открывает файл для чтения
                    with file_path.open('r', encoding='utf-8') as file:
                        if as_list:
                            # Добавляет строки в список, если as_list True
                            matches.extend(file.readlines())
                        else:
                            # Добавляет все содержимое файла в список
                            matches.append(file.read())
                    logger.info(f"Файл успешно прочитан: {file_path}")
                except Exception as ex:
                    # Логирует ошибку чтения файла
                    logger.error(f'Ошибка чтения файла \'{file_path}\'.', ex, exc_info=exc_info)

    return matches

def get_directory_names(directory: str | Path, exc_info: bool = True) -> list[str]:
    """
    Получает список имен поддиректорий в указанной директории.

    :param directory: Путь к директории.
    :type directory: str | Path
    :param exc_info: Если ``True``, то информация об ошибке будет добавлена в лог. По умолчанию ``True``.
    :type exc_info: bool
    :return: Список имен поддиректорий в директории.
    :rtype: list[str]

    :Example:
    
    .. code-block:: python
    
        from pathlib import Path
        from src.utils.file import get_directory_names
    
        directory = Path(".")
        directories = get_directory_names(directory)
        print(directories)

    .. seealso::
       https://github.com/hypo69/tiny-utils/wiki/Files-and-Directories#get_directory_names
    """
    try:
        # Возвращает список имен поддиректорий
        return [entry.name for entry in Path(directory).iterdir() if entry.is_dir()]
    except Exception as ex:
        # Логирует ошибку
        logger.warning(
            f'Ошибка получения имен директорий из \'{directory}\'.',
            ex,
            exc_info=exc_info,
        )
        return []

def read_files_content(
    root_dir: Union[str, Path],
    patterns: Union[str, list[str]],
    as_list: bool = False,
    exc_info: bool = True,
) -> list[str]:
    """
    Читает содержимое файлов, соответствующих заданным шаблонам.

    :param root_dir: Корневая директория для поиска.
    :type root_dir: str | Path
    :param patterns: Шаблоны для фильтрации файлов. Может быть строкой или списком.
    :type patterns: str | list[str]
    :param as_list: Если ``True``, возвращает содержимое файла в виде списка строк. По умолчанию ``False``.
    :type as_list: bool
    :param exc_info: Если ``True``, то информация об ошибке будет добавлена в лог. По умолчанию ``True``.
    :type exc_info: bool
    :return: Список содержимого файлов.
    :rtype: list[str]

    :Example:
    
    .. code-block:: python
    
        from pathlib import Path
        from src.utils.file import read_files_content
    
        root_dir = Path(".")
        patterns = ["*.txt", "*.md"]
        content = read_files_content(root_dir, patterns)
        print(content)
    """
    content = []
    # Итерируется по файлам, найденным с помощью recursively_get_files
    for file_path in recursively_get_file_paths(root_dir, patterns, exc_info):
        # Читает содержимое файла
        file_content = read_text_file(file_path, as_list, exc_info=exc_info)
        # Добавляет содержимое в список
        if file_content:
            content.extend(file_content if as_list else [file_content])
    return content

def remove_bom(file_path: Union[str, Path]) -> None:
    """
    Удаляет BOM из текстового файла.

    :param file_path: Путь к файлу.
    :type file_path: str | Path

    :Example:
    
    .. code-block:: python
    
        from pathlib import Path
        from src.utils.file import remove_bom
    
        file_path = Path("example.txt")
        remove_bom(file_path)
    """
    path = Path(file_path)
    try:
        # Открывает файл для чтения и записи
        with path.open('r+', encoding='utf-8') as file:
            # Читает содержимое и удаляет BOM
            content = file.read().replace('\ufeff', '')
            # Возвращает курсор в начало файла
            file.seek(0)
            # Записывает измененное содержимое
            file.write(content)
            # Обрезает файл до новой длины
            file.truncate()
        logger.info(f"BOM успешно удален из файла: {file_path}")
    except Exception as ex:
        # Логирует ошибку
        logger.error(f'Ошибка удаления BOM из файла \'{file_path}\'.', ex)

def traverse_and_clean(directory: Union[str, Path]) -> None:
    """
    Обходит директорию и удаляет BOM из всех Python файлов.

    :param directory: Путь к директории.
    :type directory: str | Path

     :Example:
    
    .. code-block:: python
    
        from pathlib import Path
        from src.utils.file import traverse_and_clean
    
        directory = Path(".")
        traverse_and_clean(directory)
    """
    # Итерируется по файлам .py и удаляет BOM
    for file in recursively_get_file_paths(directory, '*.py'):
        remove_bom(file)

def main() -> None:
    """Точка входа для удаления BOM из Python файлов."""
    root_dir = Path('..', 'src')
    logger.info(f'Начало удаления BOM в {root_dir}')
    traverse_and_clean(root_dir)

if __name__ == '__main__':
    main()
```