# Анализ кода модуля `header.py`

**Качество кода**
    - **Соответствие требованиям по оформлению кода: 6/10**
    - **Плюсы:**
        - Код содержит docstring для модуля, а также для функции `set_project_root`.
        - Используется `pathlib` для работы с путями, что является хорошей практикой.
        - Код читаем и логически структурирован.
        - Имеется обработка исключений при чтении файлов.
    - **Минусы:**
        - Не используются `j_loads` или `j_loads_ns` для чтения файлов.
        - Отсутствует логирование ошибок с использованием `logger.error`.
        - Есть избыточные комментарии, которые не несут смысловой нагрузки.
        - Много дублирующихся комментариев.
        - Присутсвуют лишние пустые комментарии `"""`
        - Не все переменные и константы имеют docstring.
        - Необходимо преобразовать docstring в reStructuredText формат.
        - Не импортирован `logger`.

**Рекомендации по улучшению**

1.  **Использование `j_loads`**: Заменить `json.load` на `j_loads` из `src.utils.jjson` для чтения файла `settings.json`.
2.  **Логирование ошибок**: Использовать `logger.error` для логирования ошибок при чтении файлов `settings.json` и `README.MD`, а также для других возможных исключений.
3.  **Удаление избыточных комментариев**: Удалить все пустые и дублирующиеся комментарии.
4.  **Документирование переменных**: Добавить docstring для всех переменных и констант, чтобы они были описаны в формате reStructuredText.
5.  **Преобразование docstring в reStructuredText**: Переписать docstring в соответствии с форматом reStructuredText.
6.  **Добавить импорт logger**: Добавить импорт `from src.logger.logger import logger`.
7.  **Исключить `...`**:  Удалить  `...` заменив на `logger.error(...)`.
8.  **Переименовать переменные**: Переименовать `settings_file` на более корректное имя (например, `f`).

**Оптимизированный код**
```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
Модуль для определения основных настроек проекта.
==================================================

Этот модуль предназначен для определения корневой директории проекта,
загрузки настроек из `settings.json` и получения информации из `README.MD`.
Также модуль содержит основные переменные проекта, такие как имя, версия,
автор и копирайт.

Пример использования:
--------------------

.. code-block:: python

    from src.ai.myai.header import __project_name__, __version__, __doc__, __author__

    print(f"Project name: {__project_name__}")
    print(f"Version: {__version__}")
    print(f"Author: {__author__}")
    print(f"Documentation: {__doc__}")
"""

import sys
from pathlib import Path
from packaging.version import Version
from src.utils.jjson import j_loads
from src.logger.logger import logger # Импортируем logger

MODE = 'dev'
"""Режим работы ('dev', 'prod', и т.д.)"""


def set_project_root(marker_files: tuple = ('pyproject.toml', 'requirements.txt', '.git')) -> Path:
    """
    Находит корневую директорию проекта, начиная с директории текущего файла.

    Поиск ведется вверх по дереву каталогов до первого каталога, содержащего
    один из файлов-маркеров.

    :param marker_files: Кортеж имен файлов или каталогов для определения корня проекта.
    :type marker_files: tuple
    :return: Путь к корневой директории, если найдена, или к директории текущего файла.
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


# Получаем корневую директорию проекта
__root__ = set_project_root()
"""Путь к корневой директории проекта"""

from src import gs

settings: dict = None
"""Словарь с настройками проекта, загруженный из 'settings.json'"""
try:
    # Код загружает настройки из файла settings.json
    with open(gs.path.root / 'src' / 'settings.json', 'r') as f:
        settings = j_loads(f)
except (FileNotFoundError, json.JSONDecodeError) as e:
    # Код логгирует ошибку, если файл не найден или не удается его декодировать
    logger.error(f'Ошибка загрузки settings.json: {e}')


doc_str: str = None
"""Строка с содержимым файла 'README.MD'"""
try:
    # Код загружает содержимое из файла README.MD
    with open(gs.path.root / 'src' / 'README.MD', 'r') as f:
        doc_str = f.read()
except (FileNotFoundError, json.JSONDecodeError) as e:
     # Код логгирует ошибку, если файл не найден или не удается его декодировать
    logger.error(f'Ошибка загрузки README.MD: {e}')


__project_name__ = settings.get("project_name", 'hypotez') if settings else 'hypotez'
"""Имя проекта, по умолчанию 'hypotez'"""
__version__: str = settings.get("version", '') if settings else ''
"""Версия проекта"""
__doc__: str = doc_str if doc_str else ''
"""Документация проекта, загруженная из README.MD"""
__details__: str = ''
"""Детали проекта, пока не определены"""
__author__: str = settings.get("author", '') if settings else ''
"""Автор проекта"""
__copyright__: str = settings.get("copyrihgnt", '') if settings else ''
"""Копирайт проекта"""
__cofee__: str = settings.get("cofee", "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69") if settings else "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69"
"""Сообщение о поддержке разработчика"""
```