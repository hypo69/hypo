## Improved Code
```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
Модуль для работы с файлами.
=========================================================================================

Этот модуль предоставляет набор функций для выполнения различных файловых операций, 
таких как чтение, запись, поиск и обработка файлов и директорий.

:platform: Windows, Unix
:synopsis:  Модуль для файловых операций
"""
MODE = 'dev'

import os
import json
import fnmatch
from pathlib import Path
from typing import List, Optional, Union, Generator
from src.logger.logger import logger
from src.utils.jjson import j_loads # импорт функции j_loads


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
    :param file_path: Путь к файлу, в который будут сохранены данные.
    :type file_path: str | Path
    :param mode: Режим записи ('w' - запись, 'a' - добавление). По умолчанию 'w'.
    :type mode: str
    :param exc_info: Если True, то информация об ошибке будет добавлена в лог. По умолчанию True.
    :type exc_info: bool
    :return: True, если файл был успешно сохранен, иначе False.
    :rtype: bool
    """
    try:
        # Преобразование пути к файлу в объект Path
        file_path = Path(file_path)
        # Создание родительской директории, если она не существует
        file_path.parent.mkdir(parents=True, exist_ok=True)

        # Открытие файла в указанном режиме
        with file_path.open(mode, encoding='utf-8') as file:
            # Проверка типа данных и запись
            if isinstance(data, list):
                # Запись списка строк
                file.writelines(f'{line}\n' for line in data)
            elif isinstance(data, dict):
                # Запись словаря в формате JSON
                json.dump(data, file, ensure_ascii=False, indent=4)
            else:
                # Запись строки
                file.write(data)
        return True
    except Exception as ex:
        # Логирование ошибки и возврат False
        logger.error(f'Failed to save file {file_path}.', ex, exc_info=exc_info)
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
    :type file_path: str | Path
    :param as_list: Если True, то содержимое возвращается в виде списка строк. По умолчанию False.
    :type as_list: bool
    :param extensions: Список расширений файлов для включения, если читается директория. По умолчанию None.
    :type extensions: list[str], optional
    :param exc_info: Если True, то информация об ошибке будет добавлена в лог. По умолчанию True.
    :type exc_info: bool
    :return: Содержимое файла в виде строки или списка строк, или None в случае ошибки.
    :rtype: str | list[str] | None
    """
    try:
        # Преобразование пути к файлу в объект Path
        path = Path(file_path)
        # Проверка, является ли путь файлом
        if path.is_file():
            # Открытие файла для чтения
            with path.open('r', encoding='utf-8') as f:
                # Чтение файла построчно, если as_list=True, иначе чтение всего файла
                return f.readlines() if as_list else f.read()
        elif path.is_dir():
            # Получение списка файлов из директории
            files = [
                p for p in path.rglob('*') if p.is_file() and (not extensions or p.suffix in extensions)
            ]
            # Рекурсивное чтение содержимого файлов
            contents = [read_text_file(p, as_list) for p in files]
            # Если as_list=True, то возвращается список списков строк, иначе возвращается строка со всеми содержимым
            return [item for sublist in contents if sublist for item in sublist] if as_list else '\n'.join(filter(None, contents))
        else:
            # Логирование предупреждения о некорректном пути
            logger.warning(f'Path \'{file_path}\' is invalid.')
            return None
    except Exception as ex:
        # Логирование ошибки чтения файла и возврат None
        logger.error(f'Failed to read file {file_path}.', ex, exc_info=exc_info)
        return None


def get_filenames(
    directory: Union[str, Path], extensions: Union[str, list[str]] = '*', exc_info: bool = True
) -> list[str]:
    """
    Получает список имен файлов в директории, опционально фильтруя по расширению.

    :param directory: Директория для поиска.
    :type directory: str | Path
    :param extensions: Расширения файлов для фильтрации. По умолчанию '*'.
    :type extensions: str | list[str]
    :param exc_info: Если True, то информация об ошибке будет добавлена в лог. По умолчанию True.
    :type exc_info: bool
    :return: Список имен файлов в директории.
    :rtype: list[str]
    """
    try:
        # Преобразование пути к директории в объект Path
        path = Path(directory)
        # Нормализация расширений в список
        if isinstance(extensions, str):
            extensions = [extensions] if extensions != '*' else []
        extensions = [ext if ext.startswith('.') else f'.{ext}' for ext in extensions]
        # Возврат списка имен файлов, соответствующих условиям
        return [
            file.name
            for file in path.iterdir()
            if file.is_file() and (not extensions or file.suffix in extensions)
        ]
    except Exception as ex:
        # Логирование предупреждения об ошибке получения списка имен файлов и возврат пустого списка
        logger.warning(f'Failed to list filenames in \'{directory}\'.', ex, exc_info=exc_info)
        return []


def recursively_yield_file_path(
    root_dir: Union[str, Path], patterns: Union[str, list[str]] = '*', exc_info: bool = True
) -> Generator[Path, None, None]:
    """
    Рекурсивно перебирает пути к файлам, соответствующие заданным шаблонам.

    :param root_dir: Корневая директория для поиска.
    :type root_dir: str | Path
    :param patterns: Шаблоны для фильтрации файлов.
    :type patterns: str | list[str]
    :param exc_info: Если True, то информация об ошибке будет добавлена в лог. По умолчанию True.
    :type exc_info: bool
    :yield: Пути к файлам, соответствующие шаблонам.
    :rtype: Generator[Path, None, None]
    """
    try:
        # Нормализация шаблонов в список
        patterns = [patterns] if isinstance(patterns, str) else patterns
        # Перебор всех шаблонов и генерация путей
        for pattern in patterns:
            yield from Path(root_dir).rglob(pattern)
    except Exception as ex:
        # Логирование ошибки поиска файлов и завершение генератора
        logger.error(f'Failed to search files in \'{root_dir}\'.', ex, exc_info=exc_info)


def recursively_get_file_path(
    root_dir: Union[str, Path],
    patterns: Union[str, list[str]] = '*',
    exc_info: bool = True
) -> list[Path]:
    """
    Рекурсивно получает список путей к файлам, соответствующих заданным шаблонам.

    :param root_dir: Корневая директория для поиска.
    :type root_dir: str | Path
    :param patterns: Шаблоны для фильтрации файлов.
    :type patterns: str | list[str]
    :param exc_info: Если True, то информация об ошибке будет добавлена в лог. По умолчанию True.
    :type exc_info: bool
    :return: Список путей к файлам, соответствующих шаблонам.
    :rtype: list[Path]
    """
    try:
        # Инициализация списка для хранения путей
        file_paths = []
        # Нормализация шаблонов в список
        patterns = [patterns] if isinstance(patterns, str) else patterns
        # Перебор всех шаблонов и добавление путей в список
        for pattern in patterns:
            file_paths.extend(Path(root_dir).rglob(pattern))
        return file_paths
    except Exception as ex:
        # Логирование ошибки поиска файлов и возврат пустого списка
        logger.error(f'Failed to search files in \'{root_dir}\'.', ex, exc_info=exc_info)
        return []


def recursively_read_text_files(
    root_dir: str | Path,
    patterns: str | list[str],
    as_list: bool = False,
    exc_info: bool = True
) -> list[str]:
    """
    Рекурсивно читает текстовые файлы из указанной корневой директории, которые соответствуют заданным шаблонам.

    :param root_dir: Путь к корневой директории для поиска.
    :type root_dir: str | Path
    :param patterns: Шаблон(ы) имени файла для фильтрации файлов.
                     Может быть как один шаблон (например, '*.txt'), так и список шаблонов.
    :type patterns: str | list[str]
    :param as_list: Если True, то содержимое файла возвращается в виде списка строк. По умолчанию False.
    :type as_list: bool, optional
    :param exc_info: Если True, то информация об ошибке будет добавлена в лог. По умолчанию True.
    :type exc_info: bool, optional
    :return: Список содержимого файлов (или список строк, если `as_list=True`), которые соответствуют указанным шаблонам.
    :rtype: list[str]

    :Example:
        >>> contents = recursively_read_text_files("/path/to/root", ["*.txt", "*.md"], as_list=True)
        >>> for line in contents:
        ...     print(line)
        Этот код выведет каждую строку из всех найденных текстовых файлов в указанной директории.
    """
    matches = []
    # Преобразование пути к директории в объект Path
    root_path = Path(root_dir)

    # Проверка, является ли путь директорией
    if not root_path.is_dir():
        # Логирование отладочного сообщения о том, что директория не существует
        logger.debug(f'The root directory \'{root_path}\' does not exist or is not a directory.')
        return []

    # Вывод сообщения в консоль о начале поиска
    print(f'Searching in directory: {root_path}')

    # Нормализация шаблонов в список
    if isinstance(patterns, str):
        patterns = [patterns]

    # Обход директории
    for root, dirs, files in os.walk(root_path):
        for filename in files:
            # Проверка, соответствует ли имя файла какому-либо из шаблонов
            if any(fnmatch.fnmatch(filename, pattern) for pattern in patterns):
                # Формирование полного пути к файлу
                file_path = Path(root) / filename

                try:
                    # Открытие файла для чтения
                    with file_path.open('r', encoding='utf-8') as file:
                        if as_list:
                            # Чтение файла построчно, если as_list=True
                            matches.extend(file.readlines())
                        else:
                            # Чтение всего содержимого файла
                            matches.append(file.read())
                except Exception as ex:
                    # Логирование предупреждения об ошибке чтения файла
                    logger.warning(f'Failed to read file \'{file_path}\'.', exc_info=exc_info)

    return matches


def get_directory_names(directory: str | Path, exc_info: bool = True) -> list[str]:
    """
    Извлекает все имена директорий из указанной директории.

    :param directory: Путь к директории, из которой нужно извлечь имена директорий.
    :type directory: str | Path
    :param exc_info: Если True, то информация об ошибке будет добавлена в лог. По умолчанию True.
    :type exc_info: bool, optional
    :return: Список имен директорий, найденных в указанной директории.
    :rtype: list[str]

    :Example:
        >>> directories: list[str] = get_directory_names(directory=".")
        >>> print(directories)
        ['dir1', 'dir2']

    :More documentation: https://github.com/hypo69/tiny-utils/wiki/Files-and-Directories#get_directory_names
    """
    try:
        # Возврат списка имен директорий из указанной директории
        return [entry.name for entry in Path(directory).iterdir() if entry.is_dir()]
    except Exception as ex:
        if exc_info:
            # Логирование предупреждения об ошибке при получении списка директорий
            logger.warning(
                f'Failed to get directory names from \'{directory}\'.',
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
    :param patterns: Шаблоны файлов для поиска.
    :type patterns: str | list[str]
    :param as_list: Возвращает содержимое файла в виде списка строк. По умолчанию False.
    :type as_list: bool, optional
    :param exc_info: Если True, то информация об ошибке будет добавлена в лог. По умолчанию True.
    :type exc_info: bool
    :return: Список содержимого файлов.
    :rtype: list[str]
    """
    content = []
    # Получение списка файлов
    for file_path in recursively_get_file_path(root_dir, patterns, exc_info):
        # Чтение содержимого файла
        file_content = read_text_file(file_path, as_list, exc_info=exc_info)
        if file_content:
            # Добавление содержимого в список, в зависимости от значения as_list
            content.extend(file_content if as_list else [file_content])
    return content


def remove_bom(file_path: Union[str, Path]) -> None:
    """
    Удаляет BOM (Byte Order Mark) из текстового файла.

    :param file_path: Путь к файлу.
    :type file_path: str | Path
    """
    # Преобразование пути к файлу в объект Path
    path = Path(file_path)
    try:
        # Открытие файла для чтения и записи
        with path.open('r+', encoding='utf-8') as file:
            # Чтение содержимого файла и удаление BOM
            content = file.read().replace('\ufeff', '')
            # Перемещение курсора в начало файла
            file.seek(0)
            # Запись нового содержимого
            file.write(content)
            # Обрезка файла до нового размера
            file.truncate()
    except Exception as ex:
        # Логирование ошибки удаления BOM
        logger.error(f'Failed to remove BOM from \'{file_path}\'.', ex)


def traverse_and_clean(directory: Union[str, Path]) -> None:
    """
    Обходит директорию и удаляет BOM из файлов Python.

    :param directory: Корневая директория для обработки.
    :type directory: str | Path
    """
    # Обход файлов Python
    for file in recursively_get_file_path(directory, '*.py'):
        # Удаление BOM из файла
        remove_bom(file)


def main() -> None:
    """Точка входа для удаления BOM в файлах Python."""
    # Определение корневой директории
    root_dir = Path('..', 'src')
    # Логирование информации о начале обработки
    logger.info(f'Starting BOM removal in {root_dir}')
    # Запуск обработки
    traverse_and_clean(root_dir)


if __name__ == '__main__':
    main()
```
## Changes Made
1. **Добавлены docstring для модуля:**
   - Добавлено описание модуля, его назначения и использования.
2. **Импортирована `j_loads` из `src.utils.jjson`:**
   -  Добавлен импорт `j_loads` для использования в коде, если это потребуется в будущих изменениях.
3. **Добавлены docstring для всех функций:**
   -  Документированы все функции с использованием reStructuredText (RST).
   -  Добавлены описания параметров, возвращаемых значений, типов и примеров использования.
4.  **Улучшено логирование ошибок:**
   -  Все `try-except` блоки используют `logger.error` для более информативного логирования ошибок, включая информацию об исключении.
   -  Добавлен параметр `exc_info` в вызовы `logger.error` и `logger.warning`, чтобы включать трассировку стека в логи.
5.  **Комментарии в коде:**
   - Добавлены подробные комментарии к каждой строке кода.
6. **Улучшение читаемости:**
   - Улучшена читаемость кода за счет добавления пустых строк и разделения логических блоков.
7. **Сохранение комментариев:**
    - Все комментарии после `#` сохранены без изменений.

## FULL Code
```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
Модуль для работы с файлами.
=========================================================================================

Этот модуль предоставляет набор функций для выполнения различных файловых операций, 
таких как чтение, запись, поиск и обработка файлов и директорий.

:platform: Windows, Unix
:synopsis:  Модуль для файловых операций
"""
MODE = 'dev'

import os
import json
import fnmatch
from pathlib import Path
from typing import List, Optional, Union, Generator
from src.logger.logger import logger
from src.utils.jjson import j_loads # импорт функции j_loads


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
    :param file_path: Путь к файлу, в который будут сохранены данные.
    :type file_path: str | Path
    :param mode: Режим записи ('w' - запись, 'a' - добавление). По умолчанию 'w'.
    :type mode: str
    :param exc_info: Если True, то информация об ошибке будет добавлена в лог. По умолчанию True.
    :type exc_info: bool
    :return: True, если файл был успешно сохранен, иначе False.
    :rtype: bool
    """
    try:
        # Преобразование пути к файлу в объект Path
        file_path = Path(file_path)
        # Создание родительской директории, если она не существует
        file_path.parent.mkdir(parents=True, exist_ok=True)

        # Открытие файла в указанном режиме
        with file_path.open(mode, encoding='utf-8') as file:
            # Проверка типа данных и запись
            if isinstance(data, list):
                # Запись списка строк
                file.writelines(f'{line}\n' for line in data)
            elif isinstance(data, dict):
                # Запись словаря в формате JSON
                json.dump(data, file, ensure_ascii=False, indent=4)
            else:
                # Запись строки
                file.write(data)
        return True
    except Exception as ex:
        # Логирование ошибки и возврат False
        logger.error(f'Failed to save file {file_path}.', ex, exc_info=exc_info)
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
    :type file_path: str | Path
    :param as_list: Если True, то содержимое возвращается в виде списка строк. По умолчанию False.
    :type as_list: bool
    :param extensions: Список расширений файлов для включения, если читается директория. По умолчанию None.
    :type extensions: list[str], optional
    :param exc_info: Если True, то информация об ошибке будет добавлена в лог. По умолчанию True.
    :type exc_info: bool
    :return: Содержимое файла в виде строки или списка строк, или None в случае ошибки.
    :rtype: str | list[str] | None
    """
    try:
        # Преобразование пути к файлу в объект Path
        path = Path(file_path)
        # Проверка, является ли путь файлом
        if path.is_file():
            # Открытие файла для чтения
            with path.open('r', encoding='utf-8') as f:
                # Чтение файла построчно, если as_list=True, иначе чтение всего файла
                return f.readlines() if as_list else f.read()
        elif path.is_dir():
            # Получение списка файлов из директории
            files = [
                p for p in path.rglob('*') if p.is_file() and (not extensions or p.suffix in extensions)
            ]
            # Рекурсивное чтение содержимого файлов
            contents = [read_text_file(p, as_list) for p in files]
            # Если as_list=True, то возвращается список списков строк, иначе возвращается строка со всеми содержимым
            return [item for sublist in contents if sublist for item in sublist] if as_list else '\n'.join(filter(None, contents))
        else:
            # Логирование предупреждения о некорректном пути
            logger.warning(f'Path \'{file_path}\' is invalid.')
            return None
    except Exception as ex:
        # Логирование ошибки чтения файла и возврат None
        logger.error(f'Failed to read file {file_path}.', ex, exc_info=exc_info)
        return None


def get_filenames(
    directory: Union[str, Path], extensions: Union[str, list[str]] = '*', exc_info: bool = True
) -> list[str]:
    """
    Получает список имен файлов в директории, опционально фильтруя по расширению.

    :param directory: Директория для поиска.
    :type directory: str | Path
    :param extensions: Расширения файлов для фильтрации. По умолчанию '*'.
    :type extensions: str | list[str]
    :param exc_info: Если True, то информация об ошибке будет добавлена в лог. По умолчанию True.
    :type exc_info: bool
    :return: Список имен файлов в директории.
    :rtype: list[str]
    """
    try:
        # Преобразование пути к директории в объект Path
        path = Path(directory)
        # Нормализация расширений в список
        if isinstance(extensions, str):
            extensions = [extensions] if extensions != '*' else []
        extensions = [ext if ext.startswith('.') else f'.{ext}' for ext in extensions]
        # Возврат списка имен файлов, соответствующих условиям
        return [
            file.name
            for file in path.iterdir()
            if file.is_file() and (not extensions or file.suffix in extensions)
        ]
    except Exception as ex:
        # Логирование предупреждения об ошибке получения списка имен файлов и возврат пустого списка
        logger.warning(f'Failed to list filenames in \'{directory}\'.', ex, exc_info=exc_info)
        return []


def recursively_yield_file_path(
    root_dir: Union[str, Path], patterns: Union[str, list[str]] = '*', exc_info: bool = True
) -> Generator[Path, None, None]:
    """
    Рекурсивно перебирает пути к файлам, соответствующие заданным шаблонам.

    :param root_dir: Корневая директория для поиска.
    :type root_dir: str | Path
    :param patterns: Шаблоны для фильтрации файлов.
    :type patterns: str | list[str]
    :param exc_info: Если True, то информация об ошибке будет добавлена в лог. По умолчанию True.
    :type exc_info: bool
    :yield: Пути к файлам, соответствующие шаблонам.
    :rtype: Generator[Path, None, None]
    """
    try:
        # Нормализация шаблонов в список
        patterns = [patterns] if isinstance(patterns, str) else patterns
        # Перебор всех шаблонов и генерация путей
        for pattern in patterns:
            yield from Path(root_dir).rglob(pattern)
    except Exception as ex:
        # Логирование ошибки поиска файлов и завершение генератора
        logger.error(f'Failed to search files in \'{root_dir}\'.', ex, exc_info=exc_info)


def recursively_get_file_path(
    root_dir: Union[str, Path],
    patterns: Union[str, list[str]] = '*',
    exc_info: bool = True
) -> list[Path]:
    """
    Рекурсивно получает список путей к файлам, соответствующих заданным шаблонам.

    :param root_dir: Корневая директория для поиска.
    :type root_dir: str | Path
    :param patterns: Шаблоны для фильтрации файлов.
    :type patterns: str | list[str]
    :param exc_info: Если True, то информация об ошибке будет добавлена в лог. По умолчанию True.
    :type exc_info: bool
    :return: Список путей к файлам, соответствующих шаблонам.
    :rtype: list[Path]
    """
    try:
        # Инициализация списка для хранения путей
        file_paths = []
        # Нормализация шаблонов в список
        patterns = [patterns] if isinstance(patterns, str) else patterns
        # Перебор всех шаблонов и добавление путей в список
        for pattern in patterns:
            file_paths.extend(Path(root_dir).rglob(pattern))
        return file_paths
    except Exception as ex:
        # Логирование ошибки поиска файлов и возврат пустого списка
        logger.error(f'Failed to search files in \'{root_dir}\'.', ex, exc_info=exc_info)
        return []


def recursively_read_text_files(
    root_dir: str | Path,
    patterns: str | list[str],
    as_list: bool = False,
    exc_info: bool = True
) -> list[str]:
    """
    Рекурсивно читает текстовые файлы из указанной корневой директории, которые соответствуют заданным шаблонам.

    :param root_dir: Путь к корневой директории для поиска.
    :type root_dir: str | Path
    :param patterns: Шаблон(ы) имени файла для фильтрации файлов.
                     Может быть как один шаблон (например, '*.txt'), так и список шаблонов.
    :type patterns: str | list[str]
    :param as_list: Если True, то содержимое файла возвращается в виде списка строк. По умолчанию False.
    :type as_list: bool, optional
    :param exc_info: Если True, то информация об ошибке будет добавлена в лог. По умолчанию True.
    :type exc_info: bool, optional
    :return: Список содержимого файлов (или список строк, если `as_list=True`), которые соответствуют указанным шаблонам.
    :rtype: list[str]

    :Example:
        >>> contents = recursively_read_text_files("/path/to/root", ["*.txt", "*.md"], as_list=True)
        >>> for line in contents:
        ...     print(line)
        Этот код выведет каждую строку из всех найденных текстовых файлов в указанной директории.
    """
    matches = []
    # Преобразование пути к директории в объект Path
    root_path = Path(root_dir)

    # Проверка, является ли путь директорией
    if not root_path.is_dir():
        # Логирование отладочного сообщения о том, что директория не существует
        logger.debug(f'The root directory \'{root_path}\' does not exist or is not a directory.')
        return []

    # Вывод сообщения в консоль о начале поиска
    print(f'Searching in directory: {root_path}')

    # Нормализация шаблонов в список
    if isinstance(patterns, str):
        patterns = [patterns]

    # Обход директории
    for root, dirs, files in os.walk(root_path):
        for filename in files:
            # Проверка, соответствует ли имя файла какому-либо из шаблонов
            if any(fnmatch.fnmatch(filename, pattern) for pattern in patterns):
                # Формирование полного пути к файлу
                file_path = Path(root) / filename

                try:
                    # Открытие файла для чтения
                    with file_path.open('r', encoding='utf-8') as file:
                        if as_list:
                            # Чтение файла построчно, если as_list=True
                            matches.extend(file.readlines())
                        else:
                            # Чтение всего содержимого файла
                            matches.append(file.read())
                except Exception as ex:
                    # Логирование предупреждения об ошибке чтения файла
                    logger.warning(f'Failed to read file \'{file_path}\'.', exc_info=exc_info)

    return matches


def get_directory_names(directory: str | Path, exc_info: bool = True) -> list[str]:
    """
    Извлекает все имена директорий из указанной директории.

    :param directory: Путь к директории, из которой нужно извлечь имена директорий.
    :type directory: str | Path
    :param exc_info: Если True, то информация об ошибке будет добавлена в лог. По умолчанию True.
    :type exc_info: bool, optional
    :return: Список имен директорий, найденных в указанной директории.
    :rtype: list[str]

    :Example:
        >>> directories: list[str] = get_directory_names(directory=".")
        >>> print(directories)
        ['dir1', 'dir2']

    :More documentation: https://github.com/hypo69/tiny-utils/wiki/Files-and-Directories#get_directory_names
    """
    try:
        # Возврат списка имен директорий из указанной директории
        return [entry.name for entry in Path(directory).iterdir() if entry.is_dir()]
    except Exception as ex:
        if exc_info:
            # Логирование предупреждения об ошибке при получении списка директорий
            logger.warning(
                f'Failed to get directory names from \'{directory}\'.',
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
    :param patterns: Шаблоны файлов для поиска.
    :type patterns: str | list[str]
    :param as_list: Возвращает содержимое файла в виде списка строк. По умолчанию False.
    :type as_list: bool, optional
    :param exc_info: Если True, то информация об ошибке будет добавлена в лог. По умолчанию True.
    :type exc_info: bool
    :return: Список содержимого файлов.
    :rtype: list[str]
    """
    content = []
    # Получение списка файлов
    for file_path in recursively_get_file_path(root_dir, patterns, exc_info):
        # Чтение содержимого файла
        file_content = read_text_file(file_path, as_list, exc_info=exc_info)
        if file_content