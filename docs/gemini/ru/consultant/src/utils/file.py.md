# Анализ кода модуля `file.py`

**Качество кода: 7/10**

-   **Плюсы:**
    *   Код хорошо структурирован, функции имеют четкое назначение.
    *   Используется `pathlib` для работы с путями, что является хорошей практикой.
    *   Присутствует логирование ошибок с использованием `logger`.
    *   Есть docstring для каждой функции, что облегчает понимание их назначения.
    *   Обработка ошибок с помощью `try-except` блоков присутствует, но ее необходимо оптимизировать.

-   **Минусы:**
    *   Не используются `j_loads` или `j_loads_ns` для чтения json файлов, что не соответствует требованиям.
    *   Избыточное использование `try-except` блоков, где можно использовать `logger.error` для обработки ошибок.
    *   Не все функции используют `exc_info=True` для логирования ошибок, что делает отладку сложнее.
    *   Комментарии в docstring не соответствуют reStructuredText (RST).

**Рекомендации по улучшению**

1.  **Использовать `j_loads`:** В функции `read_text_file`, при чтении json файлов, следует использовать `j_loads` или `j_loads_ns` из `src.utils.jjson` вместо `json.load`.
2.  **Упростить обработку ошибок:**  Вместо использования `try-except` с последующим `return None`, нужно использовать `logger.error` и позволить функции вернуть `None` по умолчанию.
3.  **Добавить `exc_info=True`:** Во все функции, которые используют `logger`, добавить `exc_info=True`, чтобы при ошибках видеть стек вызовов.
4.  **Форматирование docstring:** Привести все docstring к формату reStructuredText (RST).
5.  **Использовать `from src.utils.jjson import j_loads, j_loads_ns`:** Добавить импорт необходимых функций для работы с json.
6. **Переименовать `recursively_get_file_path`**: Переименовать функцию в `recursively_get_files`, т.к.  она возвращает именно файлы, а не пути.
7. **Переименовать `read_files_content`**: Переименовать функцию в `recursively_read_files`, т.к.  она производит рекурсивное чтение.
8. **Исправить логику `recursively_read_text_files`**: Функция `recursively_read_text_files` некорректно обрабатывает вложенные директории, необходимо использовать `rglob` как в других функциях.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
Модуль для работы с файлами
=========================================================================================

Этот модуль предоставляет набор функций для выполнения различных операций с файлами и директориями.
Включает чтение, запись, поиск и обработку файлов.

Примеры использования:
---------------------

Чтение файла:

.. code-block:: python

    content = read_text_file('file.txt')

Сохранение данных в файл:

.. code-block:: python

    save_text_file('data', 'output.txt')
"""
MODE = 'dev'

import os
import fnmatch
from pathlib import Path
from typing import List, Optional, Union, Generator
from src.logger.logger import logger
from src.utils.jjson import j_loads, j_loads_ns # импорт из файла jjson


def save_text_file(
    data: str | list[str] | dict,
    file_path: Union[str, Path],
    mode: str = "w",
    exc_info: bool = True,
) -> bool:
    """Сохраняет данные в текстовый файл.

        :param data: Данные для записи (строка, список строк или словарь).
        :type data: str | list[str] | dict
        :param file_path: Путь к файлу для сохранения.
        :type file_path: str | Path
        :param mode: Режим записи ('w' - запись, 'a' - добавление). По умолчанию 'w'.
        :type mode: str
        :param exc_info: Если True, выводит traceback при ошибке. По умолчанию True.
        :type exc_info: bool
        :return: True, если файл успешно сохранен, иначе False.
        :rtype: bool
    """
    try:
        # Преобразует путь к файлу в объект Path
        file_path = Path(file_path)
        # Создает родительские директории, если их нет
        file_path.parent.mkdir(parents=True, exist_ok=True)

        # Открывает файл в заданном режиме и кодировке utf-8
        with file_path.open(mode, encoding="utf-8") as file:
            # Проверяет тип данных и записывает их в файл
            if isinstance(data, list):
                # Записывает каждую строку из списка с символом новой строки
                file.writelines(f"{line}\n" for line in data)
            elif isinstance(data, dict):
                # Записывает словарь в формате JSON
                j_loads(data, file, ensure_ascii=False, indent=4)
            else:
                # Записывает строковые данные в файл
                file.write(data)
        return True
    except Exception as ex:
        # Логирует ошибку, если не удалось сохранить файл
        logger.error(f"Не удалось сохранить файл {file_path}.", ex, exc_info=exc_info)
        return False


def read_text_file(
    file_path: Union[str, Path],
    as_list: bool = False,
    extensions: Optional[list[str]] = None,
    exc_info: bool = True,
) -> Union[str, list[str], None]:
    """Читает содержимое файла.

        :param file_path: Путь к файлу или директории.
        :type file_path: str | Path
        :param as_list: Если True, возвращает содержимое как список строк. По умолчанию False.
        :type as_list: bool
        :param extensions: Список расширений файлов для включения при чтении директории. По умолчанию None.
        :type extensions: Optional[list[str]]
        :param exc_info: Если True, выводит traceback при ошибке. По умолчанию True.
        :type exc_info: bool
        :return: Содержимое файла как строка или список строк, или None в случае ошибки.
        :rtype: Union[str, list[str], None]
    """
    try:
        # Преобразует путь к файлу в объект Path
        path = Path(file_path)
        # Проверяет, является ли путь файлом
        if path.is_file():
            # Открывает файл для чтения и возвращает его содержимое
            with path.open("r", encoding="utf-8") as f:
                # Возвращает содержимое файла как список строк или как строку
                return f.readlines() if as_list else f.read()
        # Проверяет, является ли путь директорией
        elif path.is_dir():
            # Получает список всех файлов в директории, отфильтрованных по расширению
            files = [
                p for p in path.rglob("*") if p.is_file() and (not extensions or p.suffix in extensions)
            ]
            # Читает содержимое каждого файла
            contents = [read_text_file(p, as_list, exc_info=exc_info) for p in files]
            # Возвращает содержимое как список или строку
            return [item for sublist in contents if sublist for item in sublist] if as_list else "\n".join(filter(None, contents))
        else:
            # Логирует предупреждение, если путь не является файлом или директорией
            logger.warning(f"Путь \'{file_path}\' не является валидным.")
            return None
    except Exception as ex:
        # Логирует ошибку, если не удалось прочитать файл
        logger.error(f"Не удалось прочитать файл {file_path}.", ex, exc_info=exc_info)
        return None


def get_filenames(
    directory: Union[str, Path], extensions: Union[str, list[str]] = "*", exc_info: bool = True
) -> list[str]:
    """Возвращает список имен файлов в директории, отфильтрованный по расширениям.

        :param directory: Директория для поиска.
        :type directory: str | Path
        :param extensions: Расширения для фильтрации. По умолчанию '*'.
        :type extensions: Union[str, list[str]]
        :param exc_info: Если True, выводит traceback при ошибке. По умолчанию True.
        :type exc_info: bool
        :return: Список имен файлов в директории.
        :rtype: list[str]
    """
    try:
        # Преобразует путь в объект Path
        path = Path(directory)
        # Преобразует расширения в список, если они заданы как строка
        if isinstance(extensions, str):
            extensions = [extensions] if extensions != "*" else []
        # Добавляет точку перед расширением, если ее нет
        extensions = [ext if ext.startswith(".") else f".{ext}" for ext in extensions]

        # Возвращает список имен файлов в директории, отфильтрованных по расширениям
        return [
            file.name
            for file in path.iterdir()
            if file.is_file() and (not extensions or file.suffix in extensions)
        ]
    except Exception as ex:
        # Логирует предупреждение, если не удалось получить список имен файлов
        logger.warning(f"Не удалось получить список имен файлов в \'{directory}\'.", ex, exc_info=exc_info)
        return []


def recursively_yield_file_path(
    root_dir: Union[str, Path], patterns: Union[str, list[str]] = "*", exc_info: bool = True
) -> Generator[Path, None, None]:
    """Рекурсивно возвращает пути к файлам, соответствующие заданным шаблонам.

        :param root_dir: Корневая директория для поиска.
        :type root_dir: str | Path
        :param patterns: Шаблоны для фильтрации файлов.
        :type patterns: Union[str, list[str]]
        :param exc_info: Если True, выводит traceback при ошибке. По умолчанию True.
        :type exc_info: bool
        :yield: Путь к файлу, соответствующему шаблону.
        :rtype: Generator[Path, None, None]
    """
    try:
        # Преобразует шаблоны в список, если они заданы как строка
        patterns = [patterns] if isinstance(patterns, str) else patterns
        # Итерируется по каждому шаблону
        for pattern in patterns:
            # Возвращает путь к файлу, соответствующему шаблону
            yield from Path(root_dir).rglob(pattern)
    except Exception as ex:
        # Логирует ошибку, если не удалось найти файлы
        logger.error(f"Не удалось найти файлы в \'{root_dir}\'.", ex, exc_info=exc_info)

def recursively_get_files(
    root_dir: Union[str, Path],
    patterns: Union[str, list[str]] = "*",
    exc_info: bool = True
) -> list[Path]:
    """Рекурсивно получает список путей к файлам, соответствующих заданным шаблонам.

        :param root_dir: Корневая директория для поиска.
        :type root_dir: str | Path
        :param patterns: Шаблоны для фильтрации файлов.
        :type patterns: Union[str, list[str]]
        :param exc_info: Если True, выводит traceback при ошибке. По умолчанию True.
        :type exc_info: bool
        :return: Список путей к файлам, соответствующим шаблонам.
        :rtype: list[Path]
    """
    try:
        # Инициализирует пустой список для хранения путей к файлам
        file_paths = []
        # Преобразует шаблоны в список, если они заданы как строка
        patterns = [patterns] if isinstance(patterns, str) else patterns
        # Итерируется по каждому шаблону
        for pattern in patterns:
            # Добавляет пути к файлам, соответствующим шаблону в список
            file_paths.extend(Path(root_dir).rglob(pattern))
        # Возвращает список путей к файлам
        return file_paths
    except Exception as ex:
        # Логирует ошибку, если не удалось найти файлы
        logger.error(f"Не удалось найти файлы в \'{root_dir}\'.", ex, exc_info=exc_info)
        return []

def recursively_read_text_files(
    root_dir: str | Path,
    patterns: str | list[str],
    as_list: bool = False,
    exc_info: bool = True,
) -> list[str]:
    """Рекурсивно читает текстовые файлы, соответствующие заданным шаблонам.

        :param root_dir: Корневая директория для поиска.
        :type root_dir: str | Path
        :param patterns: Шаблоны для фильтрации файлов.
        :type patterns: str | list[str]
        :param as_list: Если True, возвращает содержимое файла как список строк. По умолчанию False.
        :type as_list: bool
        :param exc_info: Если True, выводит traceback при ошибке. По умолчанию True.
        :type exc_info: bool
        :return: Список содержимого файлов (или строк, если as_list=True), соответствующих шаблонам.
        :rtype: list[str]
    
        :Example:
            >>> contents = recursively_read_text_files("/path/to/root", ["*.txt", "*.md"], as_list=True)
            >>> for line in contents:
            ...     print(line)
            # Выведет каждую строку из всех соответствующих текстовых файлов в указанной директории.
    """
    matches = []
    root_path = Path(root_dir)
    # Проверяет, является ли путь директорией
    if not root_path.is_dir():
        # Логирует сообщение об ошибке, если путь не является директорией
        logger.debug(f"Корневая директория \'{root_path}\' не существует или не является директорией.")
        return []

    # Логирует сообщение о начале поиска
    print(f"Поиск в директории: {root_path}")
    # Преобразует шаблоны в список, если они заданы как строка
    if isinstance(patterns, str):
        patterns = [patterns]
    # Итерируется по всем файлам, найденным в директории
    for file_path in recursively_get_files(root_path, patterns, exc_info=exc_info):
         try:
             with file_path.open("r", encoding="utf-8") as file:
                 if as_list:
                     # Читает строки, если as_list=True
                     matches.extend(file.readlines())
                 else:
                    # Читает весь контент, иначе
                    matches.append(file.read())
         except Exception as ex:
             # Логирует предупреждение, если не удалось прочитать файл
             logger.warning(f"Не удалось прочитать файл \'{file_path}\'.", exc_info=exc_info)

    return matches



def get_directory_names(directory: str | Path, exc_info: bool = True) -> list[str]:
    """Возвращает список имен директорий из указанной директории.

        :param directory: Путь к директории, из которой необходимо получить имена директорий.
        :type directory: str | Path
        :param exc_info: Если True, выводит traceback при ошибке. По умолчанию True.
        :type exc_info: bool
        :return: Список имен директорий, найденных в указанной директории.
        :rtype: list[str]

        :Example:
            >>> directories: list[str] = get_directory_names(directory=".")
            >>> print(directories)
            ['dir1', 'dir2']
    
        :More Documentation: https://github.com/hypo69/tiny-utils/wiki/Files-and-Directories#get_directory_names
    """
    try:
        # Возвращает список имен директорий в указанной директории
        return [entry.name for entry in Path(directory).iterdir() if entry.is_dir()]
    except Exception as ex:
        # Логирует предупреждение, если не удалось получить список имен директорий
        logger.warning(
            f"Не удалось получить список имен директорий из \'{directory}\'.",
            ex,
            exc_info=exc_info,
        )
        return []


def recursively_read_files(
    root_dir: Union[str, Path],
    patterns: Union[str, list[str]],
    as_list: bool = False,
    exc_info: bool = True,
) -> list[str]:
    """Рекурсивно читает содержимое файлов, соответствующих заданным шаблонам.

        :param root_dir: Корневая директория для поиска.
        :type root_dir: str | Path
        :param patterns: Шаблоны для фильтрации файлов.
        :type patterns: Union[str, list[str]]
        :param as_list: Если True, возвращает содержимое файла как список строк. По умолчанию False.
        :type as_list: bool
        :param exc_info: Если True, выводит traceback при ошибке. По умолчанию True.
        :type exc_info: bool
        :return: Список содержимого файлов.
        :rtype: list[str]
    """
    content = []
    # Итерируется по путям к файлам
    for file_path in recursively_get_files(root_dir, patterns, exc_info=exc_info):
        # Читает содержимое файла
        file_content = read_text_file(file_path, as_list, exc_info=exc_info)
        # Добавляет содержимое файла в список
        if file_content:
            content.extend(file_content if as_list else [file_content])
    # Возвращает список содержимого файлов
    return content


def remove_bom(file_path: Union[str, Path]) -> None:
    """Удаляет BOM из текстового файла.

        :param file_path: Путь к файлу для обработки.
        :type file_path: str | Path
    """
    # Преобразует путь в объект Path
    path = Path(file_path)
    try:
        # Открывает файл для чтения и записи
        with path.open("r+", encoding="utf-8") as file:
            # Заменяет BOM на пустую строку
            content = file.read().replace("\ufeff", "")
            # Перемещает курсор в начало файла
            file.seek(0)
            # Записывает измененное содержимое файла
            file.write(content)
            # Обрезает файл до размера измененного содержимого
            file.truncate()
    except Exception as ex:
        # Логирует ошибку, если не удалось удалить BOM
        logger.error(f"Не удалось удалить BOM из \'{file_path}\'.", ex, exc_info=True)


def traverse_and_clean(directory: Union[str, Path]) -> None:
    """Обходит директорию и удаляет BOM из файлов Python.

        :param directory: Корневая директория для обработки.
        :type directory: str | Path
    """
    # Итерируется по путям к файлам Python в директории
    for file in recursively_get_files(directory, "*.py"):
        # Удаляет BOM из файла
        remove_bom(file)


def main() -> None:
    """Точка входа для удаления BOM из файлов Python."""
    # Определяет корневую директорию
    root_dir = Path("..", "src")
    # Логирует сообщение о начале удаления BOM
    logger.info(f"Начало удаления BOM в {root_dir}")
    # Выполняет обход директории и удаление BOM
    traverse_and_clean(root_dir)


if __name__ == "__main__":
    # Выполняет функцию main при запуске скрипта
    main()
```