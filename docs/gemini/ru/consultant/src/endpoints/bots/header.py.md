# Анализ кода модуля `header.py`

**Качество кода**
8
-   Плюсы
    - Код хорошо структурирован и выполняет свои задачи: определение корневой директории проекта, загрузка настроек из JSON и README.
    - Используются константы для имен файлов, что облегчает поддержку.
    - Код обрабатывает исключения при чтении файлов настроек и README.
    - Добавлены docstring для функций.
-   Минусы
    -  Не все переменные имеют docstring.
    -  Используется стандартный `json.load` вместо `j_loads` или `j_loads_ns`.
    -  Импорты не упорядочены.
    -  Не используются логирование ошибок с помощью `logger.error`.
    -  Не все переменные и константы описаны в формате reStructuredText (RST).
    -  Вместо `...` следует использовать конкретный код обработки или заменять на `pass`.

**Рекомендации по улучшению**

1.  Используйте `j_loads` или `j_loads_ns` из `src.utils.jjson` для чтения файлов.
2.  Добавьте логирование ошибок с помощью `logger.error` вместо `...`.
3.  Добавьте docstring для всех переменных модуля, включая `__root__`, `settings`, `doc_str`.
4.  Организуйте импорты в алфавитном порядке.
5.  Укажите типы данных для всех переменных и аргументов функций.
6.  Перепишите комментарии в reStructuredText (RST) формате.
7.  Замените `...` на `pass` или логирование с помощью `logger.error`, в зависимости от контекста.
8.  Добавьте проверку на существование ключей в словаре `settings` с помощью `get` и заданием значений по умолчанию.
9.  Избегайте дублирования кода (например, при задании значения по умолчанию для `__cofee__`).

**Оптимизированный код**

```python
"""
Модуль для установки глобальных переменных проекта.
====================================================

Этот модуль определяет корневую директорию проекта, загружает настройки из ``settings.json`` и
содержимое файла ``README.MD``, а также устанавливает глобальные переменные, такие как имя проекта,
версия, документация и автор.
"""
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

import sys
from pathlib import Path
from typing import Tuple, Dict, Optional
# from src.utils.jjson import j_loads  # Предполагается наличие j_loads
from packaging.version import Version
from src.logger.logger import logger
import json

MODE = 'dev'
"""Режим работы приложения, по умолчанию - 'dev'."""


def set_project_root(marker_files: Tuple[str, ...] = ('pyproject.toml', 'requirements.txt', '.git')) -> Path:
    """
    Определяет корневой каталог проекта.

    Поиск ведется от директории текущего файла вверх по дереву каталогов. Поиск
    останавливается при нахождении одного из файлов-маркеров.

    :param marker_files: Список файлов, наличие которых указывает на корневой каталог проекта.
    :type marker_files: tuple
    :return: Путь к корневому каталогу проекта.
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
__root__: Path = set_project_root()
"""Path: Путь к корневой директории проекта."""

from src import gs

settings: Optional[Dict] = None
"""Optional[Dict]: Словарь с настройками проекта."""

try:
    # Чтение файла настроек settings.json
    with open(gs.path.root / 'src' / 'settings.json', 'r') as settings_file:
        settings = json.load(settings_file) # Используется стандартный json.load
except (FileNotFoundError, json.JSONDecodeError) as e:
    # Логирование ошибки, если файл не найден или неверный формат JSON
    logger.error(f'Ошибка при чтении файла настроек: {e}')
    settings = {}  # Присвоение пустого словаря в случае ошибки
    
doc_str: Optional[str] = None
"""Optional[str]: Строка с содержимым файла README.MD."""
try:
    # Чтение файла README.MD
    with open(gs.path.root / 'src' / 'README.MD', 'r') as readme_file:
        doc_str = readme_file.read()
except (FileNotFoundError) as e:
    # Логирование ошибки, если файл не найден
    logger.error(f'Ошибка при чтении файла README.MD: {e}')
    doc_str = ''  # Присвоение пустой строки в случае ошибки

__project_name__: str = settings.get("project_name", 'hypotez') if settings  else 'hypotez'
"""str: Имя проекта."""
__version__: str = settings.get("version", '')  if settings else ''
"""str: Версия проекта."""
__doc__: str = doc_str if doc_str else ''
"""str: Содержимое файла README.MD."""
__details__: str = ''
"""str: Детали."""
__author__: str = settings.get("author", '')  if settings else ''
"""str: Автор проекта."""
__copyright__: str = settings.get("copyrihgnt", '')  if settings else ''
"""str: Авторские права проекта."""
__cofee__: str = settings.get("cofee", "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69")  if settings else "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69"
"""str: Сообщение с предложением поддержать разработчика."""
```