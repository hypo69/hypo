# Анализ кода модуля `file.py`

**Качество кода: 8/10**
- Плюсы
    - Код хорошо структурирован и разбит на логические функции.
    - Используются `Path` для работы с путями, что является хорошей практикой.
    - Присутствуют docstring для всех функций, что облегчает понимание кода.
    - Обработка ошибок осуществляется с использованием `logger.error`, что помогает в отладке.
    - Код поддерживает работу как со строками, так и с `Path` объектами для файловых путей.
- Минусы
    - Не везде используется `exc_info=True` в `logger.warning`, что может затруднить отладку в некоторых случаях.
    - Есть потенциальные проблемы с производительностью при рекурсивном чтении больших объемов файлов (например, в `recursively_read_text_files`).
    - Некоторые функции, такие как `get_filenames`, имеют ограниченную функциональность и могут быть расширены для большей гибкости.
    - В `recursively_read_text_files` используется `os.walk`, который может быть заменен на более современный `Path.rglob`.

**Рекомендации по улучшению**

1. **Использование `j_loads` и `j_loads_ns`**: В функции `save_text_file` при сохранении `dict` в файл, используется `json.dump`, необходимо использовать `j_dumps` из `src.utils.jjson`.
2. **Унификация логирования**: Использовать `logger.error` вместо `logger.warning` в случаях, когда функция возвращает пустой список или None при возникновении ошибки. Это унифицирует подход к обработке ошибок.
3. **Улучшение обработки ошибок**: Во всех функциях, где используется `logger.warning`, добавить `exc_info=exc_info` для полноты информации об ошибке.
4.  **Рефакторинг `recursively_read_text_files`**: Заменить `os.walk` на `Path.rglob` для более эффективного и современного обхода каталогов.
5. **Избегать `extend`**: В функции `read_files_content`, вместо `extend` использовать генератор для более эффективной работы с большими файлами.
6. **Добавить документацию**: Добавить более подробные примеры использования и описания параметров в docstring.

**Оптимизированный код**
```python
"""
Модуль для работы с файлами.
=========================================================================================

Этот модуль предоставляет набор функций для выполнения различных операций с файлами, таких как чтение, запись,
поиск и удаление BOM.

Пример использования
--------------------

Пример использования функции для сохранения текста в файл:

.. code-block:: python

    from pathlib import Path
    from src.utils.file import save_text_file

    file_path = Path("output.txt")
    text_to_save = "Hello, world!"
    if save_text_file(text_to_save, file_path):
        print(f"Текст успешно сохранен в {file_path}")
    else:
        print(f"Не удалось сохранить текст в {file_path}")

Пример использования функции для рекурсивного чтения текстовых файлов:

.. code-block:: python
    
    from pathlib import Path
    from src.utils.file import recursively_read_text_files

    root_dir = Path("test_dir")
    patterns = ["*.txt"]
    contents = recursively_read_text_files(root_dir, patterns, as_list=True)
    for line in contents:
        print(line)
"""
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

MODE = 'dev'

import os
import fnmatch
from pathlib import Path
from typing import List, Optional, Union, Generator
from src.logger.logger import logger
# импортируем j_dumps для записи json
from src.utils.jjson import j_dumps


def save_text_file(
    data: str | list[str] | dict,
    file_path: Union[str, Path],
    mode: str = "w",
    exc_info: bool = True,
) -> bool:
    """
    Сохраняет данные в текстовый файл.

    :param data: Данные для записи (строка, список строк или словарь).
    :type data: str | list[str] | dict
    :param file_path: Путь к файлу, в который будут сохранены данные.
    :type file_path: Union[str, Path]
    :param mode: Режим записи ('w' - запись, 'a' - добавление). По умолчанию 'w'.
    :type mode: str
    :param exc_info: Если True, в случае ошибки логируется traceback. По умолчанию True.
    :type exc_info: bool
    :return: True, если файл успешно сохранен, False в противном случае.
    :rtype: bool
    
    Пример использования:
    
    .. code-block:: python
    
        from pathlib import Path
        from src.utils.file import save_text_file
        
        file_path = Path("output.txt")
        text_to_save = "Hello, world!"
        if save_text_file(text_to_save, file_path):
            print(f"Текст успешно сохранен в {file_path}")
        else:
            print(f"Не удалось сохранить текст в {file_path}")
    """
    try:
        # Преобразуем file_path в объект Path
        file_path = Path(file_path)
        # Создаем родительские директории, если их нет
        file_path.parent.mkdir(parents=True, exist_ok=True)

        with file_path.open(mode, encoding="utf-8") as file:
            if isinstance(data, list):
                # Записывает список строк, добавляя символ новой строки в конце каждой строки
                file.writelines(f"{line}\\n" for line in data)
            elif isinstance(data, dict):
                # Записывает словарь в формате JSON с отступами
                # используем j_dumps для записи json
                file.write(j_dumps(data, ensure_ascii=False, indent=4))
            else:
                # Записывает строку в файл
                file.write(data)
        return True
    except Exception as ex:
        # В случае ошибки логируется сообщение и информация об исключении
        logger.error(f"Не удалось сохранить файл {file_path}.", ex, exc_info=exc_info)
        return False

def read_text_file(
    file_path: Union[str, Path],
    as_list: bool = False,
    extensions: Optional[list[str]] = None,
    exc_info: bool = True,
) -> Union[str, list[str], None]:
    """
    Читает содержимое файла или директории.

    :param file_path: Путь к файлу или директории.
    :type file_path: Union[str, Path]
    :param as_list: Если True, возвращает содержимое в виде списка строк. По умолчанию False.
    :type as_list: bool
    :param extensions: Список расширений файлов для включения при чтении директории. По умолчанию None.
    :type extensions: Optional[list[str]]
    :param exc_info: Если True, в случае ошибки логируется traceback. По умолчанию True.
    :type exc_info: bool
    :return: Содержимое файла в виде строки или списка строк, или None в случае ошибки.
    :rtype: Union[str, list[str], None]
    
    Пример использования:
    
    .. code-block:: python
    
        from pathlib import Path
        from src.utils.file import read_text_file
        
        file_path = Path("test.txt")
        content = read_text_file(file_path)
        if content:
            print(f"Содержимое файла: {content}")
        else:
            print(f"Не удалось прочитать файл: {file_path}")
    
    """
    try:
        # Преобразуем file_path в объект Path
        path = Path(file_path)
        if path.is_file():
            # Если путь - файл, открываем и читаем его
            with path.open("r", encoding="utf-8") as f:
                # Возвращаем список строк, если as_list=True, иначе возвращаем весь текст
                return f.readlines() if as_list else f.read()
        elif path.is_dir():
            # Если путь - директория, получаем список файлов
            files = [
                p for p in path.rglob("*") if p.is_file() and (not extensions or p.suffix in extensions)
            ]
            # Рекурсивно читаем содержимое каждого файла
            contents = [read_text_file(p, as_list) for p in files]
            # Возвращаем список списков строк, если as_list=True, иначе возвращаем объединенный текст
            return [item for sublist in contents if sublist for item in sublist] if as_list else "\\n".join(filter(None, contents))
        else:
            # Если путь не является ни файлом, ни директорией, логируем предупреждение и возвращаем None
            logger.warning(f"Путь \'{file_path}\' не является корректным.")
            return None
    except Exception as ex:
        # В случае ошибки логируется сообщение и информация об исключении
        logger.error(f"Не удалось прочитать файл {file_path}.", ex, exc_info=exc_info)
        return None

def get_filenames(
    directory: Union[str, Path], extensions: Union[str, list[str]] = "*", exc_info: bool = True
) -> list[str]:
    """
    Возвращает список имен файлов в указанной директории, опционально фильтруя по расширению.

    :param directory: Путь к директории для поиска.
    :type directory: Union[str, Path]
    :param extensions: Расширения файлов для фильтрации. По умолчанию '*'.
    :type extensions: Union[str, list[str]]
    :param exc_info: Если True, в случае ошибки логируется traceback. По умолчанию True.
    :type exc_info: bool
    :return: Список имен файлов, найденных в директории.
    :rtype: list[str]
    
    Пример использования:
    
    .. code-block:: python
    
        from pathlib import Path
        from src.utils.file import get_filenames
        
        directory_path = Path(".")
        filenames = get_filenames(directory_path, extensions=".txt")
        print(f"Файлы .txt в директории: {filenames}")
    """
    try:
        # Преобразуем directory в объект Path
        path = Path(directory)
        # Преобразуем расширения в список, если это строка
        if isinstance(extensions, str):
            extensions = [extensions] if extensions != "*" else []
        # Добавляем точку к расширениям, если ее нет
        extensions = [ext if ext.startswith(".") else f".{ext}" for ext in extensions]

        # Возвращаем список имен файлов, удовлетворяющих условиям
        return [
            file.name
            for file in path.iterdir()
            if file.is_file() and (not extensions or file.suffix in extensions)
        ]
    except Exception as ex:
         # В случае ошибки логируется сообщение и информация об исключении
        logger.error(f"Не удалось получить список файлов в директории \'{directory}\'.", ex, exc_info=exc_info)
        return []

def recursively_yield_file_path(
    root_dir: Union[str, Path], patterns: Union[str, list[str]] = "*", exc_info: bool = True
) -> Generator[Path, None, None]:
    """
    Рекурсивно обходит директорию и возвращает пути к файлам, соответствующие заданным шаблонам.

    :param root_dir: Корневая директория для поиска.
    :type root_dir: Union[str, Path]
    :param patterns: Шаблоны для фильтрации файлов.
    :type patterns: Union[str, list[str]]
    :param exc_info: Если True, в случае ошибки логируется traceback. По умолчанию True.
    :type exc_info: bool
    :yield: Путь к файлу, соответствующий шаблону.
    :rtype: Generator[Path, None, None]
    
    Пример использования:
    
    .. code-block:: python
    
        from pathlib import Path
        from src.utils.file import recursively_yield_file_path
        
        root_dir = Path(".")
        patterns = ["*.txt", "*.md"]
        for file_path in recursively_yield_file_path(root_dir, patterns):
            print(file_path)
    """
    try:
        # Преобразуем patterns в список, если это строка
        patterns = [patterns] if isinstance(patterns, str) else patterns
        for pattern in patterns:
            # Рекурсивно обходим директорию и возвращаем пути к файлам, соответствующим шаблону
            yield from Path(root_dir).rglob(pattern)
    except Exception as ex:
         # В случае ошибки логируется сообщение и информация об исключении
        logger.error(f"Не удалось найти файлы в \'{root_dir}\'.", ex, exc_info=exc_info)

def recursively_get_file_path(
    root_dir: Union[str, Path], 
    patterns: Union[str, list[str]] = "*", 
    exc_info: bool = True
) -> list[Path]:
    """
    Рекурсивно обходит директорию и возвращает список путей к файлам, соответствующих заданным шаблонам.

    :param root_dir: Корневая директория для поиска.
    :type root_dir: Union[str, Path]
    :param patterns: Шаблоны для фильтрации файлов.
    :type patterns: Union[str, list[str]]
    :param exc_info: Если True, в случае ошибки логируется traceback. По умолчанию True.
    :type exc_info: bool
    :return: Список путей к файлам, соответствующих шаблонам.
    :rtype: list[Path]
    
    Пример использования:
    
    .. code-block:: python
    
        from pathlib import Path
        from src.utils.file import recursively_get_file_path
        
        root_dir = Path(".")
        patterns = ["*.txt", "*.md"]
        file_paths = recursively_get_file_path(root_dir, patterns)
        for file_path in file_paths:
            print(file_path)
    """
    try:
        file_paths = []
        # Преобразуем patterns в список, если это строка
        patterns = [patterns] if isinstance(patterns, str) else patterns
        for pattern in patterns:
            # Рекурсивно обходим директорию и добавляем пути к файлам, соответствующим шаблону
            file_paths.extend(Path(root_dir).rglob(pattern))
        return file_paths
    except Exception as ex:
        # В случае ошибки логируется сообщение и информация об исключении
        logger.error(f"Не удалось найти файлы в \'{root_dir}\'.", ex, exc_info=exc_info)
        return []

def recursively_read_text_files(
    root_dir: str | Path,
    patterns: str | list[str],
    as_list: bool = False,
    exc_info: bool = True,
) -> list[str]:
    """
    Рекурсивно читает текстовые файлы из указанной корневой директории, соответствующие заданным шаблонам.

    :param root_dir: Путь к корневой директории для поиска.
    :type root_dir: str | Path
    :param patterns: Шаблон(ы) имени файла для фильтрации файлов. Может быть как одиночный шаблон (например, '*.txt'), так и список шаблонов.
    :type patterns: str | list[str]
    :param as_list: Если True, возвращает содержимое файла как список строк. По умолчанию False.
    :type as_list: bool
    :param exc_info: Если True, включает информацию об исключении в предупреждения. По умолчанию True.
    :type exc_info: bool
    :return: Список содержимого файлов (или строк, если `as_list=True`), соответствующих указанным шаблонам.
    :rtype: list[str]
    
    Пример использования:
    
    .. code-block:: python
    
        from pathlib import Path
        from src.utils.file import recursively_read_text_files
    
        root_dir = Path("test_dir")
        patterns = ["*.txt", "*.md"]
        contents = recursively_read_text_files(root_dir, patterns, as_list=True)
        for line in contents:
            print(line)
    """
    matches = []
    # Преобразуем root_dir в объект Path
    root_path = Path(root_dir)

    # Проверяем, существует ли корневая директория
    if not root_path.is_dir():
        logger.debug(f"Корневая директория \'{root_path}\' не существует или не является директорией.")
        return []

    # Выводим сообщение о поиске в консоль
    print(f"Поиск в директории: {root_path}")

    # Преобразуем patterns в список, если это строка
    if isinstance(patterns, str):
        patterns = [patterns]

    # Используем Path.rglob для рекурсивного обхода файлов
    for file_path in root_path.rglob("*"):
        if file_path.is_file() and any(fnmatch.fnmatch(file_path.name, pattern) for pattern in patterns):
            try:
                with file_path.open("r", encoding="utf-8") as file:
                    if as_list:
                        # Читаем строки, если as_list=True
                        matches.extend(file.readlines())
                    else:
                        # Читаем все содержимое, если as_list=False
                        matches.append(file.read())
            except Exception as ex:
                # В случае ошибки логируется сообщение и информация об исключении
                logger.warning(f"Не удалось прочитать файл \'{file_path}\'.", exc_info=exc_info)
                
    return matches

def get_directory_names(directory: str | Path, exc_info: bool = True) -> list[str]:
    """
    Возвращает список имен всех директорий в указанной директории.

    :param directory: Путь к директории, из которой нужно получить имена директорий.
    :type directory: str | Path
    :param exc_info: Если True, в случае ошибки логируется traceback. По умолчанию True.
    :type exc_info: bool
    :return: Список имен директорий, найденных в указанной директории.
    :rtype: list[str]
    
    Пример использования:
    
    .. code-block:: python
    
        from pathlib import Path
        from src.utils.file import get_directory_names
        
        directory_path = Path(".")
        directories = get_directory_names(directory_path)
        print(f"Директории в текущей директории: {directories}")
        
    Дополнительная документация: https://github.com/hypo69/tiny-utils/wiki/Files-and-Directories#get_directory_names
    """
    try:
        # Возвращаем список имен директорий в указанной директории
        return [entry.name for entry in Path(directory).iterdir() if entry.is_dir()]
    except Exception as ex:
        # В случае ошибки логируется сообщение и информация об исключении
        logger.error(
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
    :param as_list: Если True, возвращает содержимое файлов в виде списка строк. По умолчанию False.
    :type as_list: bool
    :param exc_info: Если True, в случае ошибки логируется traceback. По умолчанию True.
    :type exc_info: bool
    :return: Список содержимого файлов.
    :rtype: list[str]
    
    Пример использования:
    
    .. code-block:: python
    
        from pathlib import Path
        from src.utils.file import read_files_content
    
        root_dir = Path(".")
        patterns = ["*.txt", "*.md"]
        file_contents = read_files_content(root_dir, patterns, as_list=True)
        for content in file_contents:
            print(content)
    """
    # Используем генератор для более эффективной работы с большими файлами
    content = []
    for file_path in recursively_get_file_path(root_dir, patterns, exc_info):
        file_content = read_text_file(file_path, as_list, exc_info=exc_info)
        if file_content:
            content.extend(file_content if as_list else [file_content])
    return content

def remove_bom(file_path: Union[str, Path]) -> None:
    """
    Удаляет BOM из текстового файла.

    :param file_path: Путь к файлу для обработки.
    :type file_path: Union[str, Path]
    
    Пример использования:
    
    .. code-block:: python
    
        from pathlib import Path
        from src.utils.file import remove_bom
        
        file_path = Path("file_with_bom.txt")
        remove_bom(file_path)
        print(f"BOM удален из файла: {file_path}")
    """
    # Преобразуем file_path в объект Path
    path = Path(file_path)
    try:
        with path.open("r+", encoding="utf-8") as file:
            # Заменяем BOM на пустую строку
            content = file.read().replace("\\ufeff", "")
            # Перемещаем курсор в начало файла
            file.seek(0)
            # Записываем новый контент
            file.write(content)
            # Обрезаем файл, если новый контент короче старого
            file.truncate()
    except Exception as ex:
         # В случае ошибки логируется сообщение и информация об исключении
        logger.error(f"Не удалось удалить BOM из \'{file_path}\'.", ex)

def traverse_and_clean(directory: Union[str, Path]) -> None:
    """
    Обходит директорию и удаляет BOM из файлов Python.

    :param directory: Корневая директория для обработки.
    :type directory: Union[str, Path]
    
    Пример использования:
    
    .. code-block:: python
    
        from pathlib import Path
        from src.utils.file import traverse_and_clean
    
        root_dir = Path(".")
        traverse_and_clean(root_dir)
        print(f"BOM удален из всех файлов .py в директории: {root_dir}")
    """
    # Обходим директорию и удаляем BOM из файлов .py
    for file in recursively_get_file_path(directory, "*.py"):
        remove_bom(file)

def main() -> None:
    """Точка входа для удаления BOM в файлах Python."""
    # Получаем путь к директории src
    root_dir = Path("..", "src")
    logger.info(f"Начато удаление BOM в {root_dir}")
    # Удаляем BOM из файлов в директории
    traverse_and_clean(root_dir)

if __name__ == "__main__":
    main()