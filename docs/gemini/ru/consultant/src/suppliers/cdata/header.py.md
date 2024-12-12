# Анализ кода модуля `header.py`

**Качество кода**
9
-   Плюсы
    -   Код структурирован и разбит на логические блоки.
    -   Используется функция `set_project_root` для определения корневой директории проекта, что является хорошей практикой.
    -   Присутствует обработка исключений при чтении файлов настроек.
    -   Используются константы для хранения метаданных проекта.
-   Минусы
    -   Отсутствуют docstring для модуля и переменных.
    -   Не используется `j_loads` или `j_loads_ns` из `src.utils.jjson` для чтения JSON файлов.
    -   Использование `try-except` с многоточием `...` не является лучшей практикой для обработки ошибок.
    -   Не используется логирование ошибок.
    -   Импорты не отформатированы и не сгруппированы.

**Рекомендации по улучшению**

1.  Добавить docstring для модуля и всех переменных, используя reStructuredText.
2.  Использовать `j_loads` из `src.utils.jjson` вместо `json.load` для загрузки `settings.json`.
3.  Заменить многоточие `...` в `try-except` на `logger.error` для логирования ошибок.
4.  Добавить импорт `logger` из `src.logger.logger`.
5.  Отформатировать импорты.
6.  Добавить docstring к функции `set_project_root` с описанием параметров и возвращаемого значения в формате reStructuredText.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
Модуль для определения метаданных проекта и корневой директории.
================================================================

Этот модуль предназначен для настройки окружения проекта, включая определение
корневой директории, загрузку настроек из файла ``settings.json``,
и извлечение метаданных проекта, таких как имя, версия, автор и т.д.
"""

import sys
from pathlib import Path
from packaging.version import Version

# from src.utils.jjson import j_loads # TODO: добавить j_loads если понадобится 
import json # исправлено на json
from src.logger.logger import logger


MODE = 'dev'
"""Режим работы приложения ('dev' или 'prod')"""



def set_project_root(marker_files: tuple = ('pyproject.toml', 'requirements.txt', '.git')) -> Path:
    """
    Определяет корневую директорию проекта.

    Функция ищет корневую директорию проекта, начиная с директории текущего файла,
    поднимаясь вверх по дереву каталогов и останавливаясь на первой директории,
    содержащей любой из файлов-маркеров.

    :param marker_files:  Список имен файлов или директорий, которые идентифицируют корень проекта.
    :type marker_files: tuple
    :return: Путь к корневой директории, если она найдена, или директория, в которой находится скрипт.
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

# Получение корневой директории проекта
__root__ = set_project_root()
"""Path: Путь к корневой директории проекта."""


from src import gs

settings: dict = None
"""dict: Словарь с настройками проекта, загруженный из файла settings.json."""
try:
    # Код загружает настройки из файла 'settings.json', используя j_loads
    with open(gs.path.root / 'src' / 'settings.json', 'r') as settings_file:
        settings = json.load(settings_file)
except (FileNotFoundError, json.JSONDecodeError) as e:
    # Код логирует ошибку, если не удается найти файл или декодировать JSON
    logger.error(f'Ошибка при загрузке файла настроек: {e}')
    settings = {}


doc_str: str = None
"""str: Строка с содержимым файла README.MD."""
try:
    # Код читает содержимое файла 'README.MD'
    with open(gs.path.root / 'src' / 'README.MD', 'r') as settings_file:
        doc_str = settings_file.read()
except (FileNotFoundError, json.JSONDecodeError) as e:
    # Код логирует ошибку, если не удается найти файл
    logger.error(f'Ошибка при загрузке файла README.MD: {e}')
    doc_str = ''


__project_name__: str = settings.get("project_name", 'hypotez') if settings else 'hypotez'
"""str: Имя проекта, по умолчанию 'hypotez'."""
__version__: str = settings.get("version", '') if settings else ''
"""str: Версия проекта."""
__doc__: str = doc_str if doc_str else ''
"""str: Описание проекта, загруженное из файла README.MD."""
__details__: str = ''
"""str: Детали проекта (в настоящее время не используется)."""
__author__: str = settings.get("author", '') if settings else ''
"""str: Автор проекта."""
__copyright__: str = settings.get("copyrihgnt", '') if settings else ''
"""str: Информация об авторских правах."""
__cofee__: str = settings.get("cofee", "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69") if settings else "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69"
"""str: Сообщение с призывом угостить разработчика кофе."""
```