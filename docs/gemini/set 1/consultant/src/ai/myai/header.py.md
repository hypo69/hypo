# Анализ кода модуля header.py

**Качество кода**
7
-  Плюсы
    - Код структурирован и имеет базовую функциональность.
    - Используются константы для определения имени проекта, версии и т.д.
    - Есть функция для определения корневой директории проекта.
-  Минусы
    - Присутствуют множественные, идентичные закомментированные строки ``""" ..."""``.
    - Не используется `j_loads` для загрузки JSON.
    - Отсутствует логирование ошибок при загрузке `settings.json` и `README.MD`.
    - Не все переменные и константы имеют docstring.
    - Нарушение стандарта PEP8 в объявлении переменных в одну строку, таких как `__project_name__`, `__version__`.
    - Повторение кода обработки ошибок.
    - Отсутствуют импорты из `src.utils.jjson` и `src.logger.logger`.
    - Файловые пути не унифицированы (используются и `'/'` и `Path` ).

**Рекомендации по улучшению**

1. **Удалить дублирующие комментарии**: Убрать лишние пустые docstring `""" ..."""`.
2. **Использовать `j_loads`**: Заменить `json.load` на `j_loads` для загрузки JSON файлов.
3. **Добавить логирование**: Использовать `logger.error` для логирования ошибок при загрузке файлов `settings.json` и `README.MD`.
4. **Добавить docstring**: Добавить docstring для всех переменных и констант.
5. **Соблюдать PEP8**: Разделить объявление переменных `__project_name__`, `__version__` и т.д.
6. **Унифицировать пути**: Использовать `Path` для всех путей.
7. **Использовать `from src.logger.logger import logger`**:  Для логирования ошибок.
8. **Убрать `try-except`**: Перенести обработку ошибок в функцию `j_loads`.
9. **Импортировать из `src.utils.jjson`**: Добавить `from src.utils.jjson import j_loads, j_loads_ns`.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-

#! venv/bin/python/python3.12

"""
Модуль для определения основных настроек и констант проекта.
=========================================================================================

Этот модуль содержит функции и переменные для определения корневой директории проекта,
загрузки настроек из JSON-файла и чтения документации из README.MD.

Пример использования
--------------------

Пример использования констант:

.. code-block:: python

    from src.ai.myai.header import __project_name__, __version__

    print(f"Project name: {__project_name__}")
    print(f"Version: {__version__}")
"""

import sys
from pathlib import Path
from packaging.version import Version

from src.logger.logger import logger # Импортируем logger
from src.utils.jjson import j_loads, j_loads_ns # Импортируем j_loads

#: str: Режим работы приложения.

def set_project_root(marker_files: tuple = ('pyproject.toml', 'requirements.txt', '.git')) -> Path:
    """
    Находит корневую директорию проекта, начиная с директории текущего файла.

    Поиск ведется вверх по дереву каталогов и останавливается на первом каталоге,
    содержащем один из файлов-маркеров.

    :param marker_files: Кортеж имен файлов или каталогов для идентификации корня проекта.
    :type marker_files: tuple
    :return: Путь к корневой директории, если она найдена, иначе - директория, где находится скрипт.
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
__root__:Path = set_project_root()
#: Path: Путь к корневой директории проекта.

from src import gs

settings: dict = None
#: dict: Словарь с настройками, загруженными из settings.json.
try:
    # Код загружает настройки из файла settings.json, используя j_loads
    settings = j_loads(__root__ / 'src' / 'settings.json')
except (FileNotFoundError, json.JSONDecodeError) as e:
    # Логируем ошибку, если файл не найден или не удается декодировать JSON
    logger.error(f'Не удалось загрузить settings.json: {e}')
    ...

doc_str: str = None
#: str: Строка с содержимым файла README.MD.
try:
    # Код читает содержимое файла README.MD
    with open(__root__ / 'src' /  'README.MD', 'r') as settings_file:
        doc_str = settings_file.read()
except (FileNotFoundError, json.JSONDecodeError) as e:
    # Логируем ошибку, если файл не найден или не удается его прочитать
    logger.error(f'Не удалось загрузить README.MD: {e}')
    ...


__project_name__: str = settings.get("project_name", 'hypotez') if settings else 'hypotez'
#: str: Имя проекта.

__version__: str = settings.get("version", '') if settings else ''
#: str: Версия проекта.

__doc__: str = doc_str if doc_str else ''
#: str: Содержимое файла README.MD.

__details__: str = ''
#: str: Дополнительные детали проекта.

__author__: str = settings.get("author", '') if settings else ''
#: str: Автор проекта.

__copyright__: str = settings.get("copyrihgnt", '') if settings else ''
#: str: Информация об авторских правах.

__cofee__: str = settings.get("cofee", "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69") if settings else "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69"
#: str: Сообщение для поддержки разработчика.
```