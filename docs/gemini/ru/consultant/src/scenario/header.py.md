# Анализ кода модуля `header.py`

**Качество кода**
9
-  Плюсы
    - Код хорошо структурирован и логически понятен.
    - Используется `pathlib` для работы с путями, что является хорошей практикой.
    - Функция `set_project_root` четко выполняет свою задачу, находя корень проекта.
    - Есть обработка исключений при чтении файлов настроек.
-  Минусы
    - Отсутствует документация в формате reStructuredText (RST) для модуля, функций и переменных.
    - Используется стандартный `json.load` вместо `j_loads` или `j_loads_ns` из `src.utils.jjson`.
    - Исключения обрабатываются с использованием `...`, что затрудняет отладку.
    - Нет логирования ошибок.
    - Не используются константы для строк, что затрудняет поддержку кода.

**Рекомендации по улучшению**

1.  **Документация**:
    -   Добавить документацию в формате RST для модуля, функции `set_project_root` и всех глобальных переменных.
2.  **Использование `j_loads`**:
    -   Заменить `json.load` на `j_loads` из `src.utils.jjson`.
3.  **Обработка исключений**:
    -   Заменить `...` на логирование ошибок с использованием `logger.error` и возвращать `None` при ошибке.
4.  **Логирование**:
    -   Использовать `from src.logger.logger import logger` для логирования ошибок и отладочной информации.
5.  **Константы**:
    -   Определить константы для повторяющихся строк, таких как пути к файлам, ключи JSON и значения по умолчанию.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-

#! venv/bin/python/python3.12

"""
Модуль для определения основных настроек проекта.
=========================================================================================

Этот модуль определяет корень проекта, загружает настройки из файла ``settings.json``,
а также загружает документацию из файла ``README.MD``.

Затем он определяет основные переменные проекта, такие как имя, версия, автор и т.д.
"""


import sys
from pathlib import Path
from typing import Tuple
# TODO:  импорт из src.utils.jjson
from src.utils.jjson import j_loads
from src.logger.logger import logger # импортируем logger
from packaging.version import Version

# Константы для путей и ключей
SETTINGS_FILE = 'settings.json'
README_FILE = 'README.MD'
PROJECT_NAME_KEY = "project_name"
VERSION_KEY = "version"
AUTHOR_KEY = "author"
COPYRIGHT_KEY = "copyrihgnt"
COFEE_KEY = "cofee"
DEFAULT_COFEE_MESSAGE = "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69"
DEFAULT_PROJECT_NAME = 'hypotez'
DEFAULT_VERSION = ''
DEFAULT_AUTHOR = ''
DEFAULT_COPYRIGHT = ''

def set_project_root(marker_files: Tuple[str, ...] = ('pyproject.toml', 'requirements.txt', '.git')) -> Path:
    """
    Определяет корневой каталог проекта.

    Поиск производится вверх по дереву каталогов, начиная с каталога текущего файла.
    Поиск останавливается при нахождении каталога, содержащего хотя бы один из файлов-маркеров.

    :param marker_files: Кортеж имен файлов или каталогов, которые идентифицируют корень проекта.
    :type marker_files: tuple
    :return: Путь к корневому каталогу, если он найден, иначе путь к каталогу, где расположен скрипт.
    :rtype: Path
    """
    __root__: Path
    current_path: Path = Path(__file__).resolve().parent
    __root__ = current_path
    for parent in [current_path] + list(current_path.parents):
        if any((parent / marker).exists() for marker in marker_files):
            __root__ = parent
            break
    if __root__ not in sys.path:
        sys.path.insert(0, str(__root__))
    return __root__


# Get the root directory of the project
__root__ = set_project_root()
"""__root__ (Path): Путь к корневому каталогу проекта."""

from src import gs

settings: dict = None
try:
    # код исполняет загрузку настроек из файла settings.json
    with open(gs.path.root / 'src' / SETTINGS_FILE, 'r') as settings_file:
        settings = j_loads(settings_file) # используем j_loads
except (FileNotFoundError, json.JSONDecodeError) as e: # добавили исключение
    logger.error(f'Не удалось загрузить настройки из файла {SETTINGS_FILE}: {e}') # логируем ошибку
    settings = None #  присваиваем None

doc_str: str = None
try:
    # код исполняет чтение документации из файла README.MD
    with open(gs.path.root / 'src' / README_FILE, 'r') as settings_file:
        doc_str = settings_file.read()
except (FileNotFoundError, json.JSONDecodeError) as e: # добавили исключение
    logger.error(f'Не удалось прочитать файл {README_FILE}: {e}') # логируем ошибку
    doc_str = None #  присваиваем None


__project_name__ = settings.get(PROJECT_NAME_KEY, DEFAULT_PROJECT_NAME) if settings else DEFAULT_PROJECT_NAME
"""__project_name__ (str): Имя проекта, полученное из настроек или значение по умолчанию 'hypotez'."""

__version__: str = settings.get(VERSION_KEY, DEFAULT_VERSION) if settings else DEFAULT_VERSION
"""__version__ (str): Версия проекта, полученная из настроек или пустая строка."""

__doc__: str = doc_str if doc_str else ''
"""__doc__ (str): Документация проекта, полученная из файла README.MD или пустая строка."""

__details__: str = ''
"""__details__ (str): Детали проекта."""

__author__: str = settings.get(AUTHOR_KEY, DEFAULT_AUTHOR) if settings else DEFAULT_AUTHOR
"""__author__ (str): Автор проекта, полученный из настроек или пустая строка."""

__copyright__: str = settings.get(COPYRIGHT_KEY, DEFAULT_COPYRIGHT) if settings else DEFAULT_COPYRIGHT
"""__copyright__ (str): Информация об авторских правах, полученная из настроек или пустая строка."""

__cofee__: str = settings.get(COFEE_KEY, DEFAULT_COFEE_MESSAGE) if settings else DEFAULT_COFEE_MESSAGE
"""__cofee__ (str): Сообщение о кофе, полученное из настроек или значение по умолчанию."""
```