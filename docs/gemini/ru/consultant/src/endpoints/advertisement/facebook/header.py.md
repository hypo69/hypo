# Анализ кода модуля `header.py`

**Качество кода**
8
-  Плюсы
    - Код структурирован и выполняет свою задачу: определение корневой директории проекта, загрузка настроек и базовой информации.
    - Используются относительные импорты для доступа к другим модулям проекта.
    - Присутствует базовая обработка ошибок при загрузке файлов настроек.
    - Есть документация в виде docstring.
    
-  Минусы
    -  Не используются `j_loads` или `j_loads_ns` для чтения JSON, что противоречит требованиям.
    - Отсутствуют необходимые импорты для `logger`.
    - Обработка ошибок с помощью `try-except` без использования `logger.error` для логирования.
    - Некоторые docstring не соответствуют стандарту reStructuredText (RST).
    - Не хватает комментариев для некоторых блоков кода
    - Используются магические строки, которые можно вынести в константы
    - Переменные `MODE` не используются
    - Не все docstrings соответствуют reStructuredText,

**Рекомендации по улучшению**

1.  **Использовать `j_loads`**: Заменить стандартный `json.load` на `j_loads` из `src.utils.jjson` для чтения JSON-файлов.
2.  **Добавить импорт `logger`**: Добавить `from src.logger.logger import logger` для логирования ошибок.
3.  **Логирование ошибок**: Заменить `try-except` на `logger.error` для записи ошибок, вместо `...`.
4.  **Форматирование docstring**: Привести все docstring в соответствие со стандартом reStructuredText (RST).
5.  **Добавить комментарии**: Добавить комментарии к блокам кода, для понимания выполняемых действий.
6.  **Константы**: Вынести магические строки в константы, чтобы сделать код более читаемым.
7.  **Удалить неиспользуемые переменные**: Удалить переменную `MODE`
8.  **Проверка settings**: Добавить проверку на наличие ключа в `settings` перед его использованием
    
**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
Модуль для определения корневой директории проекта и загрузки базовых настроек.
===========================================================================

Этот модуль определяет корневую директорию проекта, загружает настройки из файла `settings.json` 
и информацию из `README.MD`, а также устанавливает основные переменные проекта, такие как имя, версия и автор.

.. code-block:: python

    from src.endpoints.advertisement.facebook.header import __project_name__, __version__, __doc__, __author__, __copyright__

    print(__project_name__)
    print(__version__)
    print(__doc__)
    print(__author__)
    print(__copyright__)
"""
import sys
from pathlib import Path

from packaging.version import Version

#  Добавляем импорт j_loads
from src.utils.jjson import j_loads
#  Добавляем импорт logger
from src.logger.logger import logger


#  Константы для имен файлов
SETTINGS_FILE = 'settings.json'
README_FILE = 'README.MD'
DEFAULT_COFEE_MESSAGE = "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69"
DEFAULT_PROJECT_NAME = 'hypotez'
# Список файлов маркеров для поиска корня проекта
MARKER_FILES = ('pyproject.toml', 'requirements.txt', '.git')

def set_project_root(marker_files: tuple = MARKER_FILES) -> Path:
    """
    Определение корневой директории проекта.

    Функция ищет корневую директорию проекта, начиная с директории текущего файла,
    продвигаясь вверх до первой директории, содержащей один из файлов-маркеров.

    :param marker_files: Кортеж имен файлов или директорий, определяющих корень проекта.
    :type marker_files: tuple
    :return: Путь к корневой директории, если найдена, иначе директория, где расположен скрипт.
    :rtype: Path
    """
    __root__:Path
    current_path:Path = Path(__file__).resolve().parent
    __root__ = current_path
    for parent in [current_path] + list(current_path.parents):
        if any((parent / marker).exists() for marker in marker_files):
            __root__ = parent
            break
    if __root__ not in sys.path:
        sys.path.insert(0, str(__root__))
    return __root__


#  Код исполняет поиск и установку корневой директории проекта
__root__ = set_project_root()
"""__root__ (Path): Путь к корневой директории проекта"""

from src import gs

settings:dict = None
try:
    # Код исполняет чтение файла настроек
    with open(gs.path.root / 'src' /  SETTINGS_FILE, 'r') as settings_file:
        # Код использует j_loads для загрузки JSON
        settings = j_loads(settings_file)
except (FileNotFoundError, json.JSONDecodeError) as e:
    #  Код логирует ошибку если не удалось загрузить файл настроек
    logger.error(f'Не удалось загрузить файл настроек {SETTINGS_FILE}', exc_info=e)

doc_str:str = None
try:
    # Код исполняет чтение файла README.MD
    with open(gs.path.root / 'src' /  README_FILE, 'r') as settings_file:
        #  Код считывает содержимое файла в строку
        doc_str = settings_file.read()
except (FileNotFoundError, json.JSONDecodeError) as e:
    #  Код логирует ошибку если не удалось загрузить файл README.MD
    logger.error(f'Не удалось загрузить файл документации {README_FILE}', exc_info=e)


#  Код определяет имя проекта из настроек или использует значение по умолчанию
__project_name__ = settings.get("project_name", DEFAULT_PROJECT_NAME) if settings else DEFAULT_PROJECT_NAME
#  Код определяет версию проекта из настроек или использует пустую строку
__version__: str = settings.get("version", '') if settings else ''
#  Код определяет документацию проекта из строки doc_str или использует пустую строку
__doc__: str = doc_str if doc_str else ''
__details__: str = ''
#  Код определяет автора проекта из настроек или использует пустую строку
__author__: str = settings.get("author", '') if settings else ''
#  Код определяет копирайт проекта из настроек или использует пустую строку
__copyright__: str = settings.get("copyrihgnt", '') if settings else ''
#  Код определяет сообщение для пожертвований из настроек или использует сообщение по умолчанию
__cofee__: str = settings.get("cofee", DEFAULT_COFEE_MESSAGE) if settings else DEFAULT_COFEE_MESSAGE
```