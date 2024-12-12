# Улучшенный код
```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12
"""
Модуль для определения настроек проекта и метаданных.
======================================================

Этот модуль находит корневую директорию проекта, загружает настройки из `settings.json`
и `README.MD`, а также устанавливает глобальные переменные проекта.

:var MODE: Режим работы (по умолчанию 'dev').
:vartype MODE: str
:var __root__: Путь к корневой директории проекта.
:vartype __root__: Path
:var settings: Словарь с настройками проекта, загруженными из `settings.json`.
:vartype settings: dict
:var doc_str: Строка с содержимым файла `README.MD`.
:vartype doc_str: str
:var __project_name__: Название проекта.
:vartype __project_name__: str
:var __version__: Версия проекта.
:vartype __version__: str
:var __doc__: Содержимое файла `README.MD`.
:vartype __doc__: str
:var __details__: Детали проекта (по умолчанию пустая строка).
:vartype __details__: str
:var __author__: Автор проекта.
:vartype __author__: str
:var __copyright__: Авторское право проекта.
:vartype __copyright__: str
:var __cofee__: Строка с предложением поддержать разработчика.
:vartype __cofee__: str

Примеры:
    
    Использование переменных:

    .. code-block:: python

        print(f"Project Name: {__project_name__}")
        print(f"Version: {__version__}")
"""
MODE = 'dev'

import sys
# Импортируем json из src.utils.jjson
from src.utils.jjson import j_loads
from packaging.version import Version
from pathlib import Path
from src.logger.logger import logger # Импортируем logger

def set_project_root(marker_files=('pyproject.toml', 'requirements.txt', '.git')) -> Path:
    """
    Определяет корневую директорию проекта.

    Функция выполняет поиск корневой директории проекта, начиная с директории текущего файла
    и двигаясь вверх по структуре каталогов. Поиск останавливается при обнаружении одного из
    файлов-маркеров (например, pyproject.toml, requirements.txt, .git).

    :param marker_files: Кортеж с именами файлов или директорий, которые обозначают корень проекта.
    :type marker_files: tuple
    :return: Путь к корневой директории проекта, или директория, где расположен скрипт, если корень не найден.
    :rtype: Path
    """
    __root__:Path
    # Получаем абсолютный путь к директории текущего файла
    current_path:Path = Path(__file__).resolve().parent
    __root__ = current_path
    # Перебираем директории от текущей до родительских
    for parent in [current_path] + list(current_path.parents):
        # Проверяем наличие файлов-маркеров в текущей директории
        if any((parent / marker).exists() for marker in marker_files):
            __root__ = parent
            break
    # Если корневая директория не в списке путей, то добавляем ее
    if __root__ not in sys.path:
        sys.path.insert(0, str(__root__))
    return __root__


# Получаем корневую директорию проекта
__root__ = set_project_root()
"""__root__ (Path): Путь к корневой директории проекта"""

from src import gs

settings:dict = None
try:
    # Чтение настроек из settings.json
    with open(gs.path.root / 'src' /  'settings.json', 'r') as settings_file:
        # Используем j_loads для загрузки JSON
        settings = j_loads(settings_file)
except (FileNotFoundError, json.JSONDecodeError) as e:
    # Логируем ошибку, если файл не найден или JSON невалидный
    logger.error(f'Ошибка чтения файла настроек: {e}')
    ...

doc_str:str = None
try:
    # Чтение содержимого README.MD
    with open(gs.path.root / 'src' /  'README.MD', 'r') as settings_file:
        doc_str = settings_file.read()
except (FileNotFoundError, json.JSONDecodeError) as e:
    # Логируем ошибку, если файл не найден
    logger.error(f'Ошибка чтения файла документации: {e}')
    ...


__project_name__ = settings.get("project_name", 'hypotez') if settings  else 'hypotez'
__version__: str = settings.get("version", '')  if settings  else ''
__doc__: str = doc_str if doc_str else ''
__details__: str = ''
__author__: str = settings.get("author", '')  if settings  else ''
__copyright__: str = settings.get("copyrihgnt", '')  if settings  else ''
__cofee__: str = settings.get("cofee", "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69")  if settings  else "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69"
```
# Внесённые изменения
*   Добавлены reStructuredText комментарии к модулю, переменным и функциям.
*   Добавлен импорт `from src.utils.jjson import j_loads` для чтения json файлов.
*   Добавлен импорт `from src.logger.logger import logger` для логирования ошибок.
*   Изменено использование `json.load` на `j_loads` из `src.utils.jjson`.
*   Добавлена обработка исключений `FileNotFoundError` и `json.JSONDecodeError` с помощью `logger.error`.
*   Сохранены все комментарии `#` в коде.

# Оптимизированный код
```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12
"""
Модуль для определения настроек проекта и метаданных.
======================================================

Этот модуль находит корневую директорию проекта, загружает настройки из `settings.json`
и `README.MD`, а также устанавливает глобальные переменные проекта.

:var MODE: Режим работы (по умолчанию 'dev').
:vartype MODE: str
:var __root__: Путь к корневой директории проекта.
:vartype __root__: Path
:var settings: Словарь с настройками проекта, загруженными из `settings.json`.
:vartype settings: dict
:var doc_str: Строка с содержимым файла `README.MD`.
:vartype doc_str: str
:var __project_name__: Название проекта.
:vartype __project_name__: str
:var __version__: Версия проекта.
:vartype __version__: str
:var __doc__: Содержимое файла `README.MD`.
:vartype __doc__: str
:var __details__: Детали проекта (по умолчанию пустая строка).
:vartype __details__: str
:var __author__: Автор проекта.
:vartype __author__: str
:var __copyright__: Авторское право проекта.
:vartype __copyright__: str
:var __cofee__: Строка с предложением поддержать разработчика.
:vartype __cofee__: str

Примеры:
    
    Использование переменных:

    .. code-block:: python

        print(f"Project Name: {__project_name__}")
        print(f"Version: {__version__}")
"""
MODE = 'dev'

import sys
# Импортируем json из src.utils.jjson
from src.utils.jjson import j_loads
from packaging.version import Version
from pathlib import Path
from src.logger.logger import logger # Импортируем logger

def set_project_root(marker_files=('pyproject.toml', 'requirements.txt', '.git')) -> Path:
    """
    Определяет корневую директорию проекта.

    Функция выполняет поиск корневой директории проекта, начиная с директории текущего файла
    и двигаясь вверх по структуре каталогов. Поиск останавливается при обнаружении одного из
    файлов-маркеров (например, pyproject.toml, requirements.txt, .git).

    :param marker_files: Кортеж с именами файлов или директорий, которые обозначают корень проекта.
    :type marker_files: tuple
    :return: Путь к корневой директории проекта, или директория, где расположен скрипт, если корень не найден.
    :rtype: Path
    """
    __root__:Path
    # Получаем абсолютный путь к директории текущего файла
    current_path:Path = Path(__file__).resolve().parent
    __root__ = current_path
    # Перебираем директории от текущей до родительских
    for parent in [current_path] + list(current_path.parents):
        # Проверяем наличие файлов-маркеров в текущей директории
        if any((parent / marker).exists() for marker in marker_files):
            __root__ = parent
            break
    # Если корневая директория не в списке путей, то добавляем ее
    if __root__ not in sys.path:
        sys.path.insert(0, str(__root__))
    return __root__


# Получаем корневую директорию проекта
__root__ = set_project_root()
"""__root__ (Path): Путь к корневой директории проекта"""

from src import gs

settings:dict = None
try:
    # Чтение настроек из settings.json
    with open(gs.path.root / 'src' /  'settings.json', 'r') as settings_file:
        # Используем j_loads для загрузки JSON
        settings = j_loads(settings_file)
except (FileNotFoundError, json.JSONDecodeError) as e:
    # Логируем ошибку, если файл не найден или JSON невалидный
    logger.error(f'Ошибка чтения файла настроек: {e}')
    ...

doc_str:str = None
try:
    # Чтение содержимого README.MD
    with open(gs.path.root / 'src' /  'README.MD', 'r') as settings_file:
        doc_str = settings_file.read()
except (FileNotFoundError, json.JSONDecodeError) as e:
    # Логируем ошибку, если файл не найден
    logger.error(f'Ошибка чтения файла документации: {e}')
    ...


__project_name__ = settings.get("project_name", 'hypotez') if settings  else 'hypotez'
__version__: str = settings.get("version", '')  if settings  else ''
__doc__: str = doc_str if doc_str else ''
__details__: str = ''
__author__: str = settings.get("author", '')  if settings  else ''
__copyright__: str = settings.get("copyrihgnt", '')  if settings  else ''
__cofee__: str = settings.get("cofee", "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69")  if settings  else "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69"