# Анализ кода модуля `header.py`

**Качество кода**
7
- Плюсы
    - Код выполняет функцию определения корневой директории проекта и загрузки настроек.
    - Используется `pathlib.Path` для работы с путями, что улучшает читаемость.
    - Присутствует обработка исключений при открытии файлов настроек.
    - Есть документация для функции `set_project_root`.
    - Наличие docstring в начале файла
- Минусы
    -  Используется стандартный `json.load` вместо `j_loads` или `j_loads_ns` из `src.utils.jjson`.
    -  Не все переменные имеют docstring.
    -  Отсутствует импорт `from src.logger import logger`.
    -  Не используется `logger.error` для обработки ошибок.
    -  Дублирование `if settings  else` при объявлении переменных.
    -  Отсутствие обработки ошибок при чтении файла README.md
    - `__project_name__` написан не в стиле `PEP-8`

**Рекомендации по улучшению**

1.  **Импорты:** Добавить `from src.logger.logger import logger` для логирования ошибок и `from src.utils.jjson import j_loads` для загрузки json файлов.
2.  **Загрузка JSON:** Использовать `j_loads` вместо `json.load` для загрузки файла настроек.
3.  **Обработка ошибок:** Заменить `try-except` блоки на использование `logger.error` для логирования ошибок.
4.  **Документация:** Добавить docstring для переменных `__root__`, `settings`, `doc_str`, `__project_name__`, `__version__`, `__doc__`, `__details__`, `__author__`, `__copyright__`, `__cofee__`.
5.  **Упрощение кода:** Убрать избыточное повторение `if settings else` при присвоении переменных и использвать `settings.get` с дефолтом значением.
6.  **Стиль кода:** Переменную `__project_name__` переименовать в `__project_name`, согласно `PEP-8`.
7.  **Добавить docstring** для всего модуля.
8.  **Обработка ошибок**  при чтении файла README.md, с использованием `logger.error`.
9.  **Убрать магические значения** из `marker_files` в отдельную переменную.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
#! venv/bin/python/python3.12
"""
Модуль для определения корневой директории проекта и загрузки основных настроек.
=========================================================================================

Этот модуль автоматически определяет корневую директорию проекта на основе наличия файлов-маркеров,
загружает настройки из файла `settings.json` и информацию из `README.md`.
Также здесь определяются глобальные переменные проекта, такие как имя, версия, автор, и т.д.

Пример использования
--------------------

.. code-block:: python

    from pathlib import Path
    from src.suppliers.hb.header import __root__
    print(__root__) # Выведет корневую директорию проекта

"""

import sys
from pathlib import Path
from packaging.version import Version

from src.logger.logger import logger
from src.utils.jjson import j_loads

MARKER_FILES = ('__root__', '.git')

def set_project_root(marker_files: tuple = MARKER_FILES) -> Path:
    """
    Определяет корневую директорию проекта.

    Сканирует родительские директории, начиная с директории текущего файла,
    пока не найдет директорию, содержащую один из файлов-маркеров.

    Args:
        marker_files (tuple): Кортеж имен файлов или директорий, которые идентифицируют корневую директорию проекта.

    Returns:
        Path: Путь к корневой директории проекта или директория, где расположен скрипт, если не найдена корневая директория.
    """
    current_path: Path = Path(__file__).resolve().parent
    root_path: Path = current_path
    for parent in [current_path] + list(current_path.parents):
        if any((parent / marker).exists() for marker in marker_files):
            root_path = parent
            break
    if root_path not in sys.path:
        sys.path.insert(0, str(root_path))
    return root_path


# Определение корневой директории проекта
__root__: Path = set_project_root()
"""Path: Путь к корневой директории проекта."""

from src import gs

settings: dict | None = None
"""dict | None: Словарь с настройками проекта, загруженными из файла 'settings.json'."""
try:
    with open(gs.path.root / 'src' / 'settings.json', 'r') as settings_file:
        settings = j_loads(settings_file)
except (FileNotFoundError, json.JSONDecodeError) as e:
    logger.error(f"Ошибка при загрузке файла настроек: {e}")
    ...


doc_str: str | None = None
"""str | None: Строка с содержимым файла 'README.MD'."""
try:
    with open(gs.path.root / 'src' / 'README.MD', 'r') as readme_file:
        doc_str = readme_file.read()
except (FileNotFoundError,  Exception) as e:
    logger.error(f"Ошибка при чтении файла README.MD: {e}")
    ...


__project_name__: str = settings.get("project_name", 'hypotez') if settings else 'hypotez'
"""str: Имя проекта."""
__version__: str = settings.get("version", '') if settings else ''
"""str: Версия проекта."""
__doc__: str = doc_str if doc_str else ''
"""str: Описание проекта, загруженное из файла 'README.MD'."""
__details__: str = ''
"""str: Дополнительная информация о проекте."""
__author__: str = settings.get("author", '') if settings else ''
"""str: Автор проекта."""
__copyright__: str = settings.get("copyrihgnt", '') if settings else ''
"""str: Информация об авторских правах проекта."""
__cofee__: str = settings.get("cofee", "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69") if settings else "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69"
"""str: Сообщение для поддержки разработчика."""
```