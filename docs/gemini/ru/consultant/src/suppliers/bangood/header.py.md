# Анализ кода модуля `header.py`

## Качество кода:

- **Соответствие стандартам**: 7
- **Плюсы**:
    - Код хорошо структурирован и понятен.
    - Используется `Path` для работы с путями, что обеспечивает кроссплатформенность.
    - Присутствует базовая обработка ошибок при загрузке настроек.
- **Минусы**:
    - Не используется `j_loads` для загрузки JSON, что не соответствует требованиям.
    - Использование стандартного `json.load`.
    - Отсутствует логирование ошибок при загрузке файлов.
    - Не все переменные и импорты выравнены.
    - Код содержит неявные ошибки, такие как использование `json.JSONDecodeError` для чтения `README.MD`.
    - Отсутствует  RST-документация для функций и модуля.

## Рекомендации по улучшению:

- Заменить `json.load` на `j_loads` или `j_loads_ns` из `src.utils.jjson`.
- Добавить логирование ошибок при загрузке файлов с использованием `logger.error` из `src.logger`.
- Исправить блок try except для файла `README.MD`.
- Добавить RST-документацию для модуля и функции `set_project_root`.
- Выровнять переменные и импорты.
- Добавить проверку на существование ключей `settings` перед их использованием.
- Использовать `from src.logger import logger` для импорта логгера.
- Добавить подробное описание модуля в формате RST.

## Оптимизированный код:

```python
# -*- coding: utf-8 -*-

"""
Модуль для инициализации проекта и загрузки основных настроек.
=============================================================

Этот модуль определяет корень проекта, загружает настройки из файла 'settings.json'
и документацию из 'README.MD', а также устанавливает основные переменные проекта.

Функция set_project_root используется для определения корневой директории проекта на основе
наличия определенных файлов-маркеров.

Пример использования:
----------------------
.. code-block:: python

    from src.suppliers.bangood.header import __project_name__, __version__, __doc__
    print(f"Project name: {__project_name__}")
    print(f"Version: {__version__}")
    print(f"Documentation: {__doc__}")
"""

import sys # импортируем sys
from pathlib import Path # импортируем Path
from packaging.version import Version # импортируем Version

from src.utils.jjson import j_loads # импортируем j_loads
from src.logger import logger # импортируем logger
from src import gs # импортируем gs



def set_project_root(marker_files: tuple = ('__root__', '.git')) -> Path:
    """
    Определяет корневую директорию проекта, начиная с текущей директории файла,
    поиском вверх по дереву директорий и останавливаясь на первой директории,
    содержащей любой из файлов-маркеров.

    :param marker_files: Кортеж с именами файлов или директорий для идентификации корня проекта.
    :type marker_files: tuple
    :return: Путь к корневой директории, если она найдена, иначе директория, где расположен скрипт.
    :rtype: Path

    Пример:
        >>> from pathlib import Path
        >>> set_project_root()
        ...
    """
    __root__: Path # аннотация переменной
    current_path: Path = Path(__file__).resolve().parent # получаем текущий путь
    __root__ = current_path # устанавливаем начальное значение
    for parent in [current_path] + list(current_path.parents): # проходимся по родительским каталогам
        if any((parent / marker).exists() for marker in marker_files): # проверяем наличие файлов маркеров
            __root__ = parent # устанавливаем корневую директорию
            break # выходим из цикла
    if __root__ not in sys.path: # проверяем наличие корневой директории в sys.path
        sys.path.insert(0, str(__root__)) # добавляем корневую директорию
    return __root__ # возвращаем корневую директорию


# Get the root directory of the project
__root__: Path = set_project_root() # получаем корневую директорию
"""__root__ (Path): Path to the root directory of the project"""

settings: dict = None # аннотация переменной
try: # обрабатываем ошибки
    with open(gs.path.root / 'src' / 'settings.json', 'r') as settings_file: # открываем файл
        settings = j_loads(settings_file) # загружаем настройки из файла
except FileNotFoundError: # обрабатываем ошибку
    logger.error(f"File 'settings.json' not found in {gs.path.root / 'src'}") # логируем ошибку
except Exception as e: # обрабатываем ошибку
     logger.error(f"Error while loading 'settings.json': {e}") # логируем ошибку


doc_str: str = None # аннотация переменной
try: # обрабатываем ошибки
    with open(gs.path.root / 'src' / 'README.MD', 'r') as doc_file: # открываем файл
        doc_str = doc_file.read() # считываем содержимое файла
except FileNotFoundError: # обрабатываем ошибку
    logger.error(f"File 'README.MD' not found in {gs.path.root / 'src'}") # логируем ошибку
except Exception as e: # обрабатываем ошибку
    logger.error(f"Error while loading 'README.MD': {e}")  # логируем ошибку

__project_name__: str = settings.get("project_name", 'hypotez') if settings else 'hypotez' # получаем имя проекта
__version__: str = settings.get("version", '') if settings else '' # получаем версию проекта
__doc__: str = doc_str if doc_str else '' # получаем описание проекта
__details__: str = '' # аннотация переменной
__author__: str = settings.get("author", '') if settings else '' # получаем автора проекта
__copyright__: str = settings.get("copyrihgnt", '') if settings else '' # получаем копирайт
__cofee__: str = settings.get("cofee", "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69") if settings else "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69" # получаем ссылку на кофе
```