# Анализ кода модуля `header.py`

**Качество кода**
9
- Плюсы
    - Код хорошо структурирован, используются понятные имена переменных и функций.
    - Присутствует функция для определения корневой директории проекта.
    - Используется try-except для обработки ошибок при чтении файлов.
    - Наличие `docstring` для модуля.
- Минусы
    - Отсутствует импорт `logger` из `src.logger.logger` для логирования ошибок.
    - Не используется `j_loads` из `src.utils.jjson` для загрузки json.
    - Отсутствует `docstring` для функций, переменных.
    - Использование `...` для обозначения пропуска обработки.
    - Отсутствие обработки ошибок при чтении файла `README.MD`.

**Рекомендации по улучшению**
- Добавить импорт `logger` из `src.logger.logger`.
- Заменить `json.load` на `j_loads` из `src.utils.jjson`.
- Добавить `docstring` для функций и переменных.
- Заменить `...` на логирование ошибок с помощью `logger.error`.
- Добавить проверку на наличие файла `README.MD`.
- Добавить обработки исключений при доступе к ключам словаря `settings`.

**Оптимизированный код**
```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
Модуль для определения настроек и метаданных проекта.
=========================================================================================

Модуль выполняет следующие функции:

- Поиск корневой директории проекта.
- Загрузка настроек из файла `settings.json`.
- Чтение документации из файла `README.MD`.
- Определение метаданных проекта (имя, версия, автор и т.д.).
"""

import sys
from pathlib import Path
from packaging.version import Version

# from src.utils.jjson import j_loads #TODO import
from src.logger.logger import logger
from src.utils.jjson import j_loads_ns #TODO import

MODE = 'dev'
"""Режим работы приложения."""


def set_project_root(marker_files: tuple = ('pyproject.toml', 'requirements.txt', '.git')) -> Path:
    """
    Определяет корневую директорию проекта.

    Функция ищет корневую директорию проекта, начиная с директории текущего файла,
    поднимаясь вверх по структуре каталогов и останавливаясь на первой директории,
    содержащей любой из файлов-маркеров.

    :param marker_files: Кортеж имен файлов или директорий, определяющих корень проекта.
    :type marker_files: tuple
    :return: Путь к корневой директории проекта.
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


#  Код получает корневую директорию проекта
__root__ = set_project_root()
"""Путь к корневой директории проекта."""

from src import gs

settings: dict = None
"""Словарь настроек проекта."""
try:
    # Код загружает настройки из файла settings.json
    settings = j_loads_ns(gs.path.root / 'src' / 'settings.json')
except FileNotFoundError:
    logger.error('Файл settings.json не найден.')
    settings = {}
except json.JSONDecodeError:
     logger.error('Ошибка декодирования JSON в файле settings.json.')
     settings = {}


doc_str: str = None
"""Строка документации проекта."""
try:
    # Код читает содержимое файла README.MD
    with open(gs.path.root / 'src' / 'README.MD', 'r', encoding='utf-8') as settings_file:
        doc_str = settings_file.read()
except FileNotFoundError:
    logger.error('Файл README.MD не найден.')
    doc_str = ''
except Exception as ex:
    logger.error(f'Ошибка чтения файла README.MD: {ex}')
    doc_str = ''

__project_name__: str = settings.get("project_name", 'hypotez') if settings else 'hypotez'
"""Имя проекта."""
__version__: str = settings.get("version", '') if settings else ''
"""Версия проекта."""
__doc__: str = doc_str if doc_str else ''
"""Документация проекта."""
__details__: str = ''
"""Дополнительная информация о проекте."""
__author__: str = settings.get("author", '') if settings else ''
"""Автор проекта."""
__copyright__: str = settings.get("copyrihgnt", '') if settings else ''
"""Информация об авторских правах."""
__cofee__: str = settings.get("cofee", "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69") if settings else "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69"
"""Призыв к поддержке разработчика."""
```