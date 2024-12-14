# Анализ кода модуля `header.py`

**Качество кода**
8
- Плюсы
    - Код выполняет поставленную задачу по определению корневой директории проекта и загрузке настроек.
    - Используются константы для параметров.
    - Код достаточно читабельный и понятный.
    - Присутствует базовая обработка исключений.
    - Присутствует документация к функции.
- Минусы
    - Не все импорты отсортированы и находятся в начале файла.
    - Отсутствует docstring для модуля.
    - Используется стандартный `json.load` вместо `j_loads` или `j_loads_ns` из `src.utils.jjson`.
    - Не используется `logger` для обработки исключений.
    - Отсутствует docstring для переменных модуля.
    - Код содержит магические строки, которые могут быть вынесены в константы.
    - Переменные `settings_file` следует переименовать в более описательные, такие как `settings_file_handler`.

**Рекомендации по улучшению**

1.  Добавить docstring к модулю, описывающий его назначение.
2.  Использовать `j_loads` или `j_loads_ns` из `src.utils.jjson` для чтения JSON файла.
3.  Использовать `logger.error` для обработки исключений и логирования ошибок.
4.  Добавить docstring для всех переменных модуля.
5.  Импортировать `logger` из `src.logger.logger`.
6.  Перенести магические строки в константы.
7.  Добавить проверки на наличие ключей в `settings` перед обращением к ним, чтобы избежать `KeyError`.
8.  Переименовать переменные `settings_file` в `settings_file_handler`.

**Оптимизированный код**

```python
"""
Модуль для определения корневой директории проекта и загрузки настроек.
=========================================================================================

Этот модуль содержит функции и переменные, необходимые для определения
корневой директории проекта, а также загрузки настроек из файла settings.json
и README.MD.

Пример использования
--------------------

Пример использования функции `set_project_root`:

.. code-block:: python

    from src.endpoints.hypo69.header import set_project_root
    root_path = set_project_root()
    print(f"Корневая директория проекта: {root_path}")
"""
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

import sys
from pathlib import Path
from packaging.version import Version

# import json  #  Импорт json удален, так как используется j_loads
from src.utils.jjson import j_loads  #  Используем j_loads
from src.logger.logger import logger #  Импортируем logger

MODE = 'dev'
MARKER_FILES = ('pyproject.toml', 'requirements.txt', '.git') #  Константа для marker_files
SETTINGS_FILE_NAME = 'settings.json' #  Константа для имени файла настроек
README_FILE_NAME = 'README.MD' #  Константа для имени файла README
DEFAULT_COFEE_MESSAGE = "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69" #  Константа для сообщения о кофе

def set_project_root(marker_files: tuple = MARKER_FILES) -> Path:
    """
    Определяет корневую директорию проекта, начиная с директории текущего файла.

    Поиск ведется вверх по структуре директорий до тех пор, пока не будет найдена
    директория, содержащая один из файлов-маркеров.

    :param marker_files: Кортеж с именами файлов или директорий, идентифицирующих корень проекта.
    :type marker_files: tuple
    :return: Путь к корневой директории проекта или директория, в которой находится скрипт, если корень не найден.
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


#  Получаем корневую директорию проекта
__root__ = set_project_root()
"""Path: Путь к корневой директории проекта."""

from src import gs


settings: dict = None
"""dict: Словарь настроек, загруженный из файла `settings.json`."""
try:
    #  Открываем файл settings.json, используя j_loads
    with open(gs.path.root / 'src' /  SETTINGS_FILE_NAME, 'r', encoding='utf-8') as settings_file_handler: #  Изменено имя переменной на settings_file_handler
        settings = j_loads(settings_file_handler) #  Используем j_loads вместо json.load
except FileNotFoundError as e:
    logger.error(f'Файл {SETTINGS_FILE_NAME} не найден', exc_info=True) #  Логируем ошибку
    ...
except Exception as e: #  Ловим все исключения
    logger.error(f'Ошибка при чтении или декодировании файла {SETTINGS_FILE_NAME}', exc_info=True) #  Логируем ошибку
    ...


doc_str: str = None
"""str: Строка документации, загруженная из файла `README.MD`."""
try:
    #  Открываем файл README.MD
    with open(gs.path.root / 'src' /  README_FILE_NAME, 'r', encoding='utf-8') as doc_file_handler: #  Изменено имя переменной на doc_file_handler
        doc_str = doc_file_handler.read()
except FileNotFoundError as e:
     logger.error(f'Файл {README_FILE_NAME} не найден', exc_info=True) #  Логируем ошибку
     ...
except Exception as e:
    logger.error(f'Ошибка при чтении файла {README_FILE_NAME}', exc_info=True) #  Логируем ошибку
    ...
    
#  Получаем значения из settings, если settings не пустой
__project_name__ = settings.get("project_name", 'hypotez') if settings  else 'hypotez'
"""str: Название проекта."""
__version__: str = settings.get("version", '')  if settings  else ''
"""str: Версия проекта."""
__doc__: str = doc_str if doc_str else ''
"""str: Строка документации проекта."""
__details__: str = ''
"""str: Детали проекта."""
__author__: str = settings.get("author", '')  if settings  else ''
"""str: Автор проекта."""
__copyright__: str = settings.get("copyrihgnt", '')  if settings  else ''
"""str: Авторские права проекта."""
__cofee__: str = settings.get("cofee", DEFAULT_COFEE_MESSAGE)  if settings  else DEFAULT_COFEE_MESSAGE
"""str: Сообщение о кофе."""
```