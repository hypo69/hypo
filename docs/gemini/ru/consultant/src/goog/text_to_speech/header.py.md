# Анализ кода модуля `header.py`

**Качество кода**
7
- Плюсы
    - Код выполняет задачу поиска корневой директории проекта.
    - Используется `pathlib` для работы с путями.
    - Чтение `settings.json` и `README.MD`  с обработкой исключений.
    - Объявление основных переменных проекта таких как `__project_name__`, `__version__`, `__doc__`.
- Минусы
    - Не используется `j_loads` для чтения `settings.json`.
    - Отсутствуют docstring для переменных модуля.
    - Использование стандартного `try-except` с `...` вместо `logger.error`.
    - Не все импорты находятся в начале файла.
    - Ошибки в именах переменных `copyrihgnt` -> `copyright`, `cofee` -> `coffee`.

**Рекомендации по улучшению**

1.  Заменить `json.load` на `j_loads` из `src.utils.jjson`.
2.  Добавить подробные docstring для всех функций, переменных модуля и переменных.
3.  Использовать `logger.error` для логирования ошибок вместо `try-except` с `...`.
4.  Перенести импорт `from src import gs` в начало файла.
5.  Исправить опечатки в именах переменных.
6.  Добавить описание модуля в начале файла.
7.  Использовать `from src.logger.logger import logger`.

**Оптимизированный код**

```python
"""
Модуль для инициализации проекта и загрузки основных настроек.
==================================================================

Этот модуль выполняет следующие задачи:

- Находит корневую директорию проекта.
- Загружает настройки из файла `settings.json`.
- Загружает описание из файла `README.MD`.
- Определяет основные переменные проекта, такие как имя проекта, версия, автор и т.д.

Пример использования
--------------------

.. code-block:: python

    from src.goog.text_to_speech.header import __project_name__, __version__, __doc__
    print(f"Имя проекта: {__project_name__}")
    print(f"Версия: {__version__}")
    print(f"Описание: {__doc__}")
"""

# -*- coding: utf-8 -*-

#! venv/bin/python/python3.12

import sys
from pathlib import Path
from packaging.version import Version
from src.utils.jjson import j_loads  # Используем j_loads для загрузки json
from src.logger.logger import logger # импортируем logger
from src import gs


def set_project_root(marker_files: tuple = ('__root__', '.git')) -> Path:
    """
    Определяет корневую директорию проекта.

    Функция ищет родительские директории, пока не найдет одну из директорий или файлов,
    указанных в `marker_files`.

    Args:
        marker_files (tuple): Кортеж имен файлов или директорий для идентификации корневой директории.
        По умолчанию: ('__root__', '.git').

    Returns:
        Path: Путь к корневой директории проекта или директории, где расположен текущий скрипт, если не найдено.

    Example:
        >>> set_project_root()
        WindowsPath('C:/Users/user/project')
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
__root__: Path = set_project_root()
"""Path: Путь к корневой директории проекта."""


settings: dict = None
"""dict: Словарь с настройками проекта, загруженными из `settings.json`."""
try:
    #  Читаем файл settings.json, используя j_loads
    with open(gs.path.root / 'src' / 'settings.json', 'r') as settings_file:
        settings = j_loads(settings_file)
except (FileNotFoundError, Exception) as ex: # обрабатываем ошибку
    logger.error(f"Ошибка при загрузке settings.json: {ex}")


doc_str: str = None
"""str: Содержимое файла `README.MD`."""
try:
    #  Читаем файл README.MD
    with open(gs.path.root / 'src' / 'README.MD', 'r') as settings_file:
        doc_str = settings_file.read()
except (FileNotFoundError, Exception) as ex: # обрабатываем ошибку
    logger.error(f"Ошибка при чтении README.MD: {ex}")


__project_name__: str = settings.get("project_name", 'hypotez') if settings else 'hypotez'
"""str: Имя проекта."""
__version__: str = settings.get("version", '') if settings else ''
"""str: Версия проекта."""
__doc__: str = doc_str if doc_str else ''
"""str: Описание проекта, полученное из `README.MD`."""
__details__: str = ''
"""str: Детали проекта."""
__author__: str = settings.get("author", '') if settings else ''
"""str: Автор проекта."""
__copyright__: str = settings.get("copyright", '') if settings else ''
"""str: Авторские права проекта."""
__coffee__: str = settings.get("coffee", "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69") if settings else "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69"
"""str: Сообщение о поддержке разработчика."""
```