# Анализ кода модуля `header.py`

**Качество кода**
7
-   Плюсы
    -   Код структурирован и читаем.
    -   Используется `pathlib` для работы с путями.
    -   Функция `set_project_root` корректно определяет корневую директорию проекта.
-   Минусы
    -   Не используются `j_loads` и `j_loads_ns` для чтения `json`.
    -   Не все переменные и функции имеют docstring.
    -   Избыточное использование `try-except`.
    -   Не используется `logger` для логирования ошибок.
    -   Некоторые переменные не имеют аннотации типов.
    -   Не хватает комментариев в стиле RST.

**Рекомендации по улучшению**

1.  Заменить `json.load` на `j_loads` из `src.utils.jjson`.
2.  Добавить docstring для всех функций, переменных и модуля в формате RST.
3.  Использовать `logger` для логирования ошибок, вместо `try-except`.
4.  Добавить аннотацию типов для переменных.
5.  Удалить неиспользуемые импорты.
6.  Переписать комментарии в формате RST.
7.  Использовать константы для дефолтных значений.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
Модуль `header.py`
==================

Модуль содержит общие настройки и метаданные проекта.
Используется для определения корневой директории проекта,
загрузки настроек из `settings.json` и получения документации из `README.md`.
"""
import sys
from pathlib import Path
from typing import Tuple

# from packaging.version import Version # Удален неиспользуемый импорт
from src.utils.jjson import j_loads # Заменен импорт json
from src.logger.logger import logger # Добавлен импорт logger
from src import gs


MODE: str = 'dev' # Добавлена аннотация типов

_DEFAULT_COFEE_MESSAGE = "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69" # Добавлена константа
_DEFAULT_PROJECT_NAME = 'hypotez' # Добавлена константа
_DEFAULT_VERSION = '' # Добавлена константа
_DEFAULT_AUTHOR = '' # Добавлена константа
_DEFAULT_COPYRIGHT = '' # Добавлена константа



def set_project_root(marker_files: Tuple[str, ...] = ('pyproject.toml', 'requirements.txt', '.git')) -> Path:
    """
    Определяет корневую директорию проекта.

    Функция ищет корневую директорию проекта, начиная с директории текущего файла,
    двигаясь вверх по дереву директорий и останавливаясь на первой директории,
    содержащей любой из файлов-маркеров.

    :param marker_files: Кортеж имен файлов или директорий, которые используются для определения корня проекта.
    :type marker_files: tuple
    :return: Путь к корневой директории, если она найдена, иначе - директория, где расположен скрипт.
    :rtype: Path
    """
    __root__: Path # аннотация типа
    current_path: Path = Path(__file__).resolve().parent # аннотация типа
    __root__ = current_path
    for parent in [current_path] + list(current_path.parents):
        if any((parent / marker).exists() for marker in marker_files):
            __root__ = parent
            break
    if __root__ not in sys.path:
        sys.path.insert(0, str(__root__))
    return __root__


# Получение корневой директории проекта
__root__: Path = set_project_root()
""" Path:  путь к корневой директории проекта.""" # Добавлена аннотация типа и docstring


settings: dict = None # Добавлена аннотация типов
try:
    # код исполняет открытие файла settings.json и его чтение
    with open(gs.path.root / 'src' /  'settings.json', 'r') as settings_file:
        settings = j_loads(settings_file) # Заменил json.load на j_loads
except (FileNotFoundError, Exception) as ex: #  обработка ошибок через logger
    logger.error(f"Ошибка при чтении файла settings.json: {ex}")
    ... # Оставляем `...` без изменений

doc_str: str = None # Добавлена аннотация типов
try:
    # код исполняет открытие файла README.MD и его чтение
    with open(gs.path.root / 'src' /  'README.MD', 'r') as settings_file:
        doc_str = settings_file.read()
except (FileNotFoundError, Exception) as ex: #  обработка ошибок через logger
    logger.error(f"Ошибка при чтении файла README.MD: {ex}")
    ... # Оставляем `...` без изменений


__project_name__: str = settings.get("project_name", _DEFAULT_PROJECT_NAME) if settings  else _DEFAULT_PROJECT_NAME
"""str: Имя проекта.""" # Добавлен docstring
__version__: str = settings.get("version", _DEFAULT_VERSION)  if settings  else _DEFAULT_VERSION
"""str: Версия проекта.""" # Добавлен docstring
__doc__: str = doc_str if doc_str else ''
"""str: Строка документации.""" # Добавлен docstring
__details__: str = ''
"""str: Детали проекта.""" # Добавлен docstring
__author__: str = settings.get("author", _DEFAULT_AUTHOR)  if settings  else _DEFAULT_AUTHOR
"""str: Автор проекта.""" # Добавлен docstring
__copyright__: str = settings.get("copyrihgnt", _DEFAULT_COPYRIGHT)  if settings  else _DEFAULT_COPYRIGHT
"""str: Авторские права.""" # Добавлен docstring
__cofee__: str = settings.get("cofee", _DEFAULT_COFEE_MESSAGE)  if settings  else _DEFAULT_COFEE_MESSAGE
"""str: Сообщение для поддержки разработчика.""" # Добавлен docstring
```