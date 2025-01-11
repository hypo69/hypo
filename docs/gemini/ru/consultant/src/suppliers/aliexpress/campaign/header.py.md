# Анализ кода модуля `header.py`

## Качество кода:

- **Соответствие стандартам**: 7
- **Плюсы**:
    - Код имеет базовую структуру, понятную логику определения корневой директории проекта.
    - Присутствуют комментарии и docstring для функции `set_project_root`.
    - Используется `pathlib` для работы с путями.
- **Минусы**:
    - Не все строки docstring соответствуют стандарту RST.
    - Используется `json.load` вместо `j_loads` или `j_loads_ns`.
    - Не используются логирование ошибок.
    - Смешанные стили кавычек (одинарные и двойные) для строк.
    - Избыточное использование `try-except`.
    - Не хватает описания модуля в docstring.

## Рекомендации по улучшению:

- Необходимо добавить описание модуля в docstring в формате RST.
- Заменить все двойные кавычки на одинарные для строк в коде, кроме тех, которые используются для вывода (`print`, `logger.error`, `input`).
- Использовать `j_loads` или `j_loads_ns` из `src.utils.jjson` вместо `json.load`.
- Добавить логирование ошибок с помощью `logger.error` вместо простого пропуска исключений.
- Использовать аннотацию типов для переменных, где это уместно.
- Форматировать все строки в docstring в соответствии с RST.
- Уточнить описания в комментариях, избегая таких формулировок, как "получаем".

## Оптимизированный код:

```python
"""
Модуль для инициализации проекта и загрузки настроек.
======================================================

Этот модуль определяет корневую директорию проекта, загружает настройки из файла `settings.json`
и устанавливает переменные проекта.

Пример использования:
--------------------
.. code-block:: python

    from src.suppliers.aliexpress.campaign import header

    print(header.__project_name__)
"""
# -*- coding: utf-8 -*-

#! venv/bin/python/python3.12
import sys
from pathlib import Path
from src.utils.jjson import j_loads # Используем j_loads для загрузки json
from src.logger import logger # Импортируем logger из src.logger

def set_project_root(marker_files: tuple = ('__root__', '.git')) -> Path:
    """
    Находит корневую директорию проекта, начиная с директории текущего файла,
    идя вверх по дереву каталогов и останавливаясь на первой директории,
    содержащей один из маркерных файлов.

    :param marker_files: Названия файлов или каталогов для определения корневой директории.
    :type marker_files: tuple, optional
    :return: Путь к корневой директории, если она найдена, иначе путь к директории, где находится скрипт.
    :rtype: Path
    
    Пример:
        >>> set_project_root()
        PosixPath('/path/to/your/project')
    """
    current_path: Path = Path(__file__).resolve().parent
    root_path: Path = current_path # Переименовано __root__ в root_path для лучшей читаемости
    for parent in [current_path] + list(current_path.parents):
        if any((parent / marker).exists() for marker in marker_files):
            root_path = parent
            break
    if root_path not in sys.path:
        sys.path.insert(0, str(root_path))
    return root_path

# Get the root directory of the project
__root__: Path = set_project_root() # Аннотация типа для __root__
"""__root__ (Path): Путь к корневой директории проекта"""

from src import gs

settings: dict | None = None # Добавлена аннотация типа и None
try:
    with open(gs.path.root / 'src' / 'settings.json', 'r') as settings_file:
        settings = j_loads(settings_file) # Используем j_loads
except FileNotFoundError:
    logger.error(f"Файл settings.json не найден в {gs.path.root / 'src'}") # Используем logger.error
except Exception as e: # Обработка всех исключений json
    logger.error(f"Ошибка при чтении файла settings.json: {e}")

doc_str: str | None = None # Добавлена аннотация типа и None
try:
    with open(gs.path.root / 'src' / 'README.MD', 'r') as doc_file:
        doc_str = doc_file.read()
except FileNotFoundError:
    logger.error(f"Файл README.MD не найден в {gs.path.root / 'src'}") # Используем logger.error
except Exception as e:
    logger.error(f"Ошибка при чтении файла README.MD: {e}") # Добавлена обработка всех ошибок чтения файла


__project_name__: str = settings.get('project_name', 'hypotez') if settings else 'hypotez' # Добавлена аннотация типов
__version__: str = settings.get('version', '') if settings else ''
__doc__: str = doc_str if doc_str else ''
__details__: str = '' # Добавлена аннотация типов
__author__: str = settings.get('author', '') if settings else '' # Добавлена аннотация типов
__copyright__: str = settings.get('copyrihgnt', '') if settings else '' # Добавлена аннотация типов
__cofee__: str = settings.get('cofee', 'Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69') if settings else 'Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69' # Добавлена аннотация типов
```