## Анализ кода модуля `file.py`

**Качество кода: 7/10**

-   **Плюсы:**
    *   Код содержит docstrings для большинства функций, что улучшает понимание их назначения и использования.
    *   Используется `pathlib.Path` для работы с путями, что делает код более кросс-платформенным.
    *   Присутствует обработка ошибок с использованием `try-except` блоков и логирование с помощью `src.logger.logger`.
    *   Функции достаточно хорошо разделены по ответственности.
    *   Используются `Union` и `Optional` в аннотациях типов.

-   **Минусы:**
    *   Не все функции имеют полные docstring, например, отсутствует описание возвращаемого значения в `get_directory_names`.
    *   Многократное использование `try-except` блоков с `logger.error` делает код немного многословным.
    *   Не везде используется параметр `exc_info` при вызове logger.
    *   В функции `recursively_get_file_path` не используется `yield from`, как в `recursively_yield_file_path`.
    *   В `recursively_read_text_files` используется `os.walk` и `fnmatch`, что делает код менее консистентным с остальными функциями, использующими `Path.rglob`.
    *   Функция `recursively_get_files` не определена.
    *   Не используется `j_loads` или `j_loads_ns` из `src.utils.jjson` для чтения json файлов.

**Рекомендации по улучшению:**

1.  **Унификация логирования:**
    *   Использовать `exc_info=True` во всех вызовах `logger.error` и `logger.warning`.
    *   Удалить избыточные блоки `try-except` и логировать ошибку один раз.
2.  **Использование `j_loads`:**
    *   Использовать `j_loads` или `j_loads_ns` из `src.utils.jjson` для чтения json файлов.
3.  **Улучшение документации:**
    *   Добавить недостающие docstring, включая описание возвращаемых значений.
    *   Уточнить документацию для параметров и возвращаемых значений.
    *   Привести все docstring к стандарту reStructuredText (RST).
4.  **Консистентность:**
    *   Заменить `os.walk` и `fnmatch` в `recursively_read_text_files` на `Path.rglob` для единообразия.
    *   Использовать `yield from` вместо `extend` в `recursively_get_file_path`.
    *   Добавить определение функции `recursively_get_files` или заменить ее вызовы.
5.  **Избегать избыточности:**
    *   Упростить логику там, где это возможно, например, при проверке существования директории.

**Оптимизированный код:**

```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
Модуль для работы с файловой системой.
=====================================

Этот модуль предоставляет набор функций для выполнения операций с файлами и директориями,
таких как чтение, запись, поиск и обработка файлов.

.. module:: src.utils.file
   :platform: Windows, Unix
   :synopsis: Module for file operations

"""
MODE = 'dev'

import os
import json
import fnmatch
from pathlib import Path
from typing import List, Optional, Union, Generator
from src.logger.logger import logger
from src.utils.jjson import j_loads #  Импорт j_loads из src.utils.jjson

def save_text_file(
    data: Union[str, list[str], dict],
    file_path: Union[str, Path],
    mode: str = "w",
    exc_info: bool = True,
) -> bool:
    """
    Сохраняет данные в текстовый файл.

    :param data: Данные для записи (строка, список строк или словарь).
    :type data: Union[str, list[str], dict]
    :param file_path: Путь к файлу, в который нужно сохранить данные.
    :type file_path: Union[str, Path]
    :param mode: Режим записи ('w' для записи, 'a' для добавления). По умолчанию 'w'.
    :type mode: str, optional
    :param exc_info: Если True, добавляет информацию об исключении в журнал. По умолчанию True.
    :type exc_info: bool, optional
    :return: True, если файл успешно сохранен, иначе False.
    :rtype: bool
    """
    file_path = Path(file_path)
    try:
        #  Код создает родительские директории, если их нет
        file_path.parent.mkdir(parents=True, exist_ok=True)
        with file_path.open(mode, encoding="utf-8") as file:
            if isinstance(data, list):
                #  Код записывает список строк в файл
                file.writelines(f"{line}\n" for line in data)
            elif isinstance(data, dict):
                 # Код записывает словарь в файл в формате json
                json.dump(data, file, ensure_ascii=False, indent=4)
            else:
                 # Код записывает строку в файл
                file.write(data)
        return True
    except Exception as ex:
        #  Код регистрирует ошибку, если не удалось сохранить файл
        logger.error(f"Не удалось сохранить файл {file_path}.", ex, exc_info=exc_info)
        return False


def read_text_file(
    file_path: Union[str, Path],
    as_list: bool = False,
    extensions: Optional[list[str]] = None,
    exc_info: bool = True,
) -> Union[str, list[str], None]:
    """
    Читает содержимое файла.

    :param file_path: Путь к файлу или директории.
    :type file_path: Union[str, Path]
    :param as_list: Если True, возвращает содержимое в виде списка строк. По умолчанию False.
    :type as_list: bool, optional
    :param extensions: Список расширений файлов для включения при чтении директории. По умолчанию None.
    :type extensions: Optional[list[str]], optional
    :param exc_info: Если True, добавляет информацию об исключении в журнал. По умолчанию True.
    :type exc_info: bool, optional
    :return: Содержимое файла в виде строки или списка строк, или None в случае ошибки.
    :rtype: Union[str, list[str], None]
    """
    path = Path(file_path)
    try:
        if path.is_file():
            #  Код открывает и считывает содержимое файла
            with path.open("r", encoding="utf-8") as f:
                return f.readlines() if as_list else f.read()
        elif path.is_dir():
            # Код формирует список файлов с учетом расширений
            files = [
                p for p in path.rglob("*") if p.is_file() and (not extensions or p.suffix in extensions)
            ]
            #  Код читает содержимое каждого файла в списке
            contents = [read_text_file(p, as_list, exc_info=exc_info) for p in files]
            #  Код возвращает список строк или объединенную строку содержимого файлов
            return [item for sublist in contents if sublist for item in sublist] if as_list else "\n".join(filter(None, contents))
        else:
            # Код регистрирует предупреждение, если путь не является файлом или директорией
            logger.warning(f"Путь \'{file_path}\' не является допустимым.", exc_info=exc_info)
            return None
    except Exception as ex:
        # Код регистрирует ошибку, если не удалось прочитать файл
        logger.error(f"Не удалось прочитать файл {file_path}.", ex, exc_info=exc_info)
        return None


def get_filenames(
    directory: Union[str, Path], extensions: Union[str, list[str]] = "*", exc_info: bool = True
) -> list[str]:
    """
    Получает список имен файлов в директории, отфильтрованных по расширению.

    :param directory: Путь к директории для поиска.
    :type directory: Union[str, Path]
    :param extensions: Расширения файлов для фильтрации. По умолчанию '*'.
    :type extensions: Union[str, list[str]], optional
    :param exc_info: Если True, добавляет информацию об исключении в журнал. По умолчанию True.
    :type exc_info: bool, optional
    :return: Список имен файлов, найденных в директории.
    :rtype: list[str]
    """
    try:
        path = Path(directory)
        if isinstance(extensions, str):
             # Код преобразует строку расширений в список
            extensions = [extensions] if extensions != "*" else []
        # Код обеспечивает корректный формат расширений
        extensions = [ext if ext.startswith(".") else f".{ext}" for ext in extensions]

        # Код возвращает список имен файлов, удовлетворяющих условиям
        return [
            file.name
            for file in path.iterdir()
            if file.is_file() and (not extensions or file.suffix in extensions)
        ]
    except Exception as ex:
        # Код регистрирует предупреждение, если не удалось получить список файлов
        logger.warning(f"Не удалось получить список имен файлов в \'{directory}\'.", ex, exc_info=exc_info)
        return []


def recursively_yield_file_path(
    root_dir: Union[str, Path], patterns: Union[str, list[str]] = "*", exc_info: bool = True
) -> Generator[Path, None, None]:
    """
    Рекурсивно генерирует пути к файлам, соответствующие заданным шаблонам.

    :param root_dir: Корневая директория для поиска.
    :type root_dir: Union[str, Path]
    :param patterns: Шаблоны для фильтрации файлов.
    :type patterns: Union[str, list[str]], optional
    :param exc_info: Если True, добавляет информацию об исключении в журнал. По умолчанию True.
    :type exc_info: bool, optional
    :yield: Путь к файлу, соответствующему шаблону.
    :rtype: Generator[Path, None, None]
    """
    try:
        patterns = [patterns] if isinstance(patterns, str) else patterns
        #  Код генерирует пути к файлам, соответствующим шаблонам
        for pattern in patterns:
            yield from Path(root_dir).rglob(pattern)
    except Exception as ex:
        #  Код регистрирует ошибку, если не удалось выполнить поиск файлов
        logger.error(f"Не удалось выполнить поиск файлов в \'{root_dir}\'.", ex, exc_info=exc_info)

def recursively_get_file_path(
    root_dir: Union[str, Path], 
    patterns: Union[str, list[str]] = "*", 
    exc_info: bool = True
) -> list[Path]:
    """
    Рекурсивно получает список путей к файлам, соответствующих заданным шаблонам.

    :param root_dir: Корневая директория для поиска.
    :type root_dir: Union[str, Path]
    :param patterns: Шаблоны для фильтрации файлов.
    :type patterns: Union[str, list[str]], optional
    :param exc_info: Если True, добавляет информацию об исключении в журнал. По умолчанию True.
    :type exc_info: bool, optional
    :return: Список путей к файлам, соответствующим шаблонам.
    :rtype: list[Path]
    """
    try:
        file_paths = []
        patterns = [patterns] if isinstance(patterns, str) else patterns
        # Код получает список путей к файлам
        for pattern in patterns:
            file_paths.extend(Path(root_dir).rglob(pattern))
        return file_paths
    except Exception as ex:
        # Код регистрирует ошибку, если не удалось выполнить поиск файлов
        logger.error(f"Не удалось выполнить поиск файлов в \'{root_dir}\'.", ex, exc_info=exc_info)
        return []


def recursively_read_text_files(
    root_dir: Union[str, Path],
    patterns: Union[str, list[str]],
    as_list: bool = False,
    exc_info: bool = True,
) -> list[str]:
    """
    Рекурсивно считывает текстовые файлы из указанной корневой директории, которые соответствуют заданным шаблонам.

    :param root_dir: Путь к корневой директории для поиска.
    :type root_dir: Union[str, Path]
    :param patterns: Шаблон(ы) имен файлов для фильтрации файлов. Может быть как один шаблон (например, '*.txt'), так и список шаблонов.
    :type patterns: Union[str, list[str]]
    :param as_list: Если True, возвращает содержимое файла в виде списка строк. По умолчанию False.
    :type as_list: bool, optional
    :param exc_info: Если True, включает информацию об исключении в предупреждения. По умолчанию True.
    :type exc_info: bool, optional
    :return: Список содержимого файлов (или строк, если `as_list=True`), которые соответствуют заданным шаблонам.
    :rtype: list[str]
    :Example:
        >>> contents = recursively_read_text_files("/path/to/root", ["*.txt", "*.md"], as_list=True)
        >>> for line in contents:
        ...     print(line)
        Это напечатает каждую строку из всех соответствующих текстовых файлов в указанной директории.
    """
    matches = []
    root_path = Path(root_dir)

    # Проверка существования корневой директории
    if not root_path.is_dir():
        logger.debug(f"Корневая директория \'{root_path}\' не существует или не является директорией.")
        return []

    # Код нормализует шаблоны в список, если это одна строка
    patterns = [patterns] if isinstance(patterns, str) else patterns

    # Код обходит все файлы в директории рекурсивно, используя Path.rglob
    for file_path in Path(root_dir).rglob("*"):
      if file_path.is_file() and any(fnmatch.fnmatch(file_path.name, pattern) for pattern in patterns):
        try:
          with file_path.open("r", encoding="utf-8") as file:
              if as_list:
                   # Код читает строки, если `as_list=True`
                  matches.extend(file.readlines())
              else:
                  #  Код читает все содержимое в противном случае
                  matches.append(file.read())
        except Exception as ex:
          #  Код регистрирует предупреждение, если не удалось прочитать файл
          logger.warning(f"Не удалось прочитать файл \'{file_path}\'.", ex, exc_info=exc_info)
    return matches


def get_directory_names(directory: Union[str, Path], exc_info: bool = True) -> list[str]:
    """
    Извлекает все имена директорий из указанной директории.

    :param directory: Путь к директории, из которой нужно извлечь имена директорий.
    :type directory: Union[str, Path]
    :param exc_info: Если True, добавляет информацию об исключении в журнал в случае ошибки. По умолчанию True.
    :type exc_info: bool, optional
    :return: Список имен директорий, найденных в указанной директории.
    :rtype: list[str]
    :Example:
        >>> directories: list[str] = get_directory_names(directory=".")
        >>> print(directories)
        ['dir1', 'dir2']

    .. seealso::
        https://github.com/hypo69/tiny-utils/wiki/Files-and-Directories#get_directory_names
    """
    try:
        #  Код возвращает список имен директорий
        return [entry.name for entry in Path(directory).iterdir() if entry.is_dir()]
    except Exception as ex:
        # Код регистрирует предупреждение, если не удалось получить имена директорий
        logger.warning(
            f"Не удалось получить имена директорий из \'{directory}\'.",
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
    :type root_dir: Union[str, Path]
    :param patterns: Шаблоны файлов для поиска.
    :type patterns: Union[str, list[str]]
    :param as_list: Если True, возвращает содержимое как список строк. По умолчанию False.
    :type as_list: bool, optional
    :param exc_info: Если True, добавляет информацию об исключении в журнал. По умолчанию True.
    :type exc_info: bool, optional
    :return: Список содержимого файлов.
    :rtype: list[str]
    """
    content = []
    #  Код получает пути к файлам и считывает их содержимое
    for file_path in recursively_get_file_path(root_dir, patterns, exc_info):
        file_content = read_text_file(file_path, as_list, exc_info=exc_info)
        if file_content:
            content.extend(file_content if as_list else [file_content])
    return content


def remove_bom(file_path: Union[str, Path]) -> None:
    """
    Удаляет BOM из текстового файла.

    :param file_path: Файл для обработки.
    :type file_path: Union[str, Path]
    """
    path = Path(file_path)
    try:
        #  Код открывает файл, удаляет BOM и перезаписывает содержимое
        with path.open("r+", encoding="utf-8") as file:
            content = file.read().replace("\ufeff", "")
            file.seek(0)
            file.write(content)
            file.truncate()
    except Exception as ex:
        #  Код регистрирует ошибку, если не удалось удалить BOM
        logger.error(f"Не удалось удалить BOM из \'{file_path}\'.", ex, exc_info=True)


def traverse_and_clean(directory: Union[str, Path]) -> None:
    """
    Обходит директорию и удаляет BOM из Python файлов.

    :param directory: Корневая директория для обработки.
    :type directory: Union[str, Path]
    """
    #  Код получает список файлов и удаляет BOM из каждого
    for file in recursively_get_file_path(directory, "*.py"):
        remove_bom(file)


def main() -> None:
    """Точка входа для удаления BOM в Python файлах."""
    root_dir = Path("..", "src")
    logger.info(f"Начало удаления BOM в {root_dir}")
    traverse_and_clean(root_dir)


if __name__ == "__main__":
    main()