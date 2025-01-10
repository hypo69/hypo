# Анализ кода модуля `header.py`

**Качество кода**
8
-  Плюсы
    -   Код содержит docstring для модуля и функции `set_project_root`.
    -   Используется `pathlib.Path` для работы с путями.
    -   Есть обработка исключений при чтении файлов конфигурации и документации.
    -   Используется `packaging.version.Version` для работы с версиями (хотя в данном коде не используется).
-  Минусы
    -   Не используется `j_loads` или `j_loads_ns` для чтения JSON.
    -   Отсутствуют импорты для `settings` и `logger`.
    -   В коде есть `...` как точки остановки.
    -   Комментарии после `#` не всегда объясняют следующий блок кода.
    -   Для констант,  не используется `UPPER_SNAKE_CASE`.
    -   Используются двойные кавычки в выводе, хотя нужно одинарные.
    -   Присутсвуют дублирования кода `Treat the developer to a cup of coffee ...`
    -   Отсутсвует документация для переменных и констант.
    -   Переменная `__details__` не инициализируется значением из файла или словаря `config`
    -  Обработка исключений не использует `logger.error`, а просто `...`.

**Рекомендации по улучшению**

1.  Использовать `j_loads` или `j_loads_ns` для загрузки JSON из файла.
2.  Добавить импорт для `logger` из `src.logger.logger`.
3.  Заменить `...` на явную обработку ошибок с логированием через `logger.error`.
4.  Добавить документацию ко всем переменным, константам и функциям.
5.  Применить `UPPER_SNAKE_CASE` для констант, если они не меняются в процессе работы.
6.  Использовать одинарные кавычки для строк в Python коде, двойные только в `print()` и `logger.error()`.
7.  Избавиться от дублирования строки с сообщением про кофе, вынести в константу.
8.  Инициализировать переменную `__details__`
9.  Убедиться что `settings`  используется как `dict`
10. Убедиться что константа `__version__` имеет тип `packaging.version.Version`

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
#! venv/bin/python/python3.12

"""
Модуль для инициализации основных параметров проекта.
=========================================================================================

Этот модуль отвечает за установку корневой директории проекта, загрузку конфигурации
и извлечение метаданных, таких как название проекта, версия, автор и т.д.
"""

import sys
from pathlib import Path
from packaging.version import Version
from src.utils.jjson import j_loads  # Используем j_loads для загрузки JSON
from src.logger.logger import logger
#from src import gs
from typing import Any, Dict

COFEE_MESSAGE = "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69"
"""Строка с сообщением о возможности поддержать разработчика."""

def set_project_root(marker_files: tuple = ('__root__', '.git')) -> Path:
    """
    Находит корневую директорию проекта, начиная с директории текущего файла.

    Функция ищет вверх по дереву директорий, останавливаясь на первой директории,
    содержащей любой из указанных файлов-маркеров.

    Args:
        marker_files (tuple): Имена файлов или директорий, которые идентифицируют корень проекта.

    Returns:
        Path: Путь к корневой директории, если она найдена, иначе - директория, где расположен скрипт.
    """
    __root__: Path  # Объявляем тип переменной __root__
    current_path: Path = Path(__file__).resolve().parent  # Получаем путь к директории текущего файла
    __root__ = current_path  # Инициализируем __root__ текущим путем
    for parent in [current_path] + list(current_path.parents):  # Перебираем текущую директорию и все ее родительские
        if any((parent / marker).exists() for marker in marker_files):  # Проверяем наличие маркера в текущей директории
            __root__ = parent  # Если маркер найден, обновляем __root__
            break  # Выходим из цикла
    if __root__ not in sys.path:  # Проверяем, есть ли корневая директория в sys.path
        sys.path.insert(0, str(__root__))  # Добавляем корневую директорию в начало sys.path
    return __root__ # Возвращаем корневую директорию


# Получаем корневую директорию проекта
ROOT_DIR: Path = set_project_root()
"""ROOT_DIR (Path): Путь к корневой директории проекта."""

CONFIG: Dict = {}
"""CONFIG (dict): Словарь с данными конфигурации проекта."""
try:
    #  код загружает конфигурацию из файла config.json
    with open(ROOT_DIR / 'src' / 'config.json', 'r') as f:
        CONFIG = j_loads(f) # Используем j_loads для загрузки JSON
except FileNotFoundError:
     logger.error(f'Файл конфигурации не найден {ROOT_DIR / "src" / "config.json"}')
except Exception as ex:
    logger.error('Ошибка загрузки конфигурации', exc_info=ex)


DOC_STRING: str = ''
"""DOC_STRING (str): Строка с содержимым файла документации README.MD."""
try:
    # код загружает  текст из файла README.MD
    with open(ROOT_DIR / 'src' / 'README.MD', 'r') as settings_file:
        DOC_STRING = settings_file.read()
except FileNotFoundError:
    logger.error(f'Файл документации не найден {ROOT_DIR / "src" / "README.MD"}')
except Exception as ex:
   logger.error(f'Ошибка загрузки документации', exc_info=ex)

PROJECT_NAME: str = CONFIG.get('project_name', 'hypotez') if CONFIG else 'hypotez'
"""PROJECT_NAME (str): Название проекта."""
__version__: Version = Version(CONFIG.get('version', '0.0.0')) if CONFIG else Version('0.0.0')
"""__version__ (packaging.version.Version): Версия проекта."""
__doc__: str = DOC_STRING if DOC_STRING else ''
"""__doc__ (str): Описание проекта."""
__details__: str = CONFIG.get('details', '') if CONFIG else ''
"""__details__ (str): Дополнительные сведения о проекте."""
__author__: str = CONFIG.get('author', '') if CONFIG else ''
"""__author__ (str): Автор проекта."""
__copyright__: str = CONFIG.get('copyrihgnt', '') if CONFIG else ''
"""__copyright__ (str): Информация об авторских правах."""
__cofee__: str = CONFIG.get("cofee", COFEE_MESSAGE)  if CONFIG else COFEE_MESSAGE
"""__cofee__ (str): Сообщение о возможности поддержать разработчика."""
```