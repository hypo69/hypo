# Анализ кода модуля `header.py`

**Качество кода: 6/10**

*   **Плюсы:**
    *   Используется `pathlib` для работы с путями, что является хорошей практикой.
    *   Функция `set_project_root` корректно определяет корневую директорию проекта.
    *   Код читает данные из `settings.json` и `README.MD` с обработкой ошибок.
    *   Установлены переменные проекта из `settings.json`.
*   **Минусы:**
    *   Отсутствуют необходимые импорты, такие как `from src.utils.jjson import j_loads, j_loads_ns`.
    *   Используется стандартный `json.load` вместо `j_loads`.
    *   Не используется `logger` для логирования ошибок.
    *   В коде присутствуют `...` как заглушки, которые должны быть заменены на логику.
    *   Отсутствует документация в формате RST для функций и переменных.
    *   Используются двойные кавычки для строк в коде, необходимо использовать одинарные.
    *   Отсутствует описание модуля в начале файла в формате RST.
    *   Отсутствует явное определение типа для переменных.

**Рекомендации по улучшению**

1.  Добавить описание модуля в формате RST в начале файла.
2.  Использовать `j_loads` для чтения `settings.json`.
3.  Добавить необходимые импорты.
4.  Использовать `logger` для логирования ошибок вместо `...` и стандартного `try-except`.
5.  Применить docstring в формате RST к функции `set_project_root`.
6.  Изменить двойные кавычки на одинарные в Python коде.
7.  Добавить документацию для переменных модуля.
8.  Явное указание типов переменных.
9.  Убрать неиспользуемые импорты.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-

#! venv/bin/python/python3.12

"""
Модуль `header`
=====================

Модуль предназначен для определения корневой директории проекта,
загрузки настроек из файла `settings.json` и получения информации из `README.MD`,
а также для установки переменных проекта.

Пример использования
--------------------

.. code-block:: python

    from pathlib import Path
    from src.suppliers.etzmaleh.header import __project_name__, __version__, __doc__, __author__

    print(f"Project name: {__project_name__}")
    print(f"Version: {__version__}")
    print(f"Author: {__author__}")

"""
import sys
from pathlib import Path
from packaging.version import Version
from src.utils.jjson import j_loads #  Используем j_loads вместо json.load
from src.logger.logger import logger #  Импорт logger
from typing import Optional

def set_project_root(marker_files: tuple[str, ...] = ('__root__', '.git')) -> Path:
    """
    Определяет корневой каталог проекта, начиная с каталога текущего файла,
    поиска вверх и останавливаясь в первом каталоге, содержащем любой из файлов-маркеров.

    Args:
        marker_files (tuple[str, ...]): Имена файлов или каталогов для определения корня проекта.

    Returns:
        Path: Путь к корневому каталогу, если найден, иначе каталог, где находится скрипт.

    Example:
        >>> set_project_root()
        PosixPath('/path/to/your/project')

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

# Получение корневой директории проекта
__root__: Path = set_project_root()
"""Path: Путь к корневой директории проекта."""

from src import gs

settings: Optional[dict] = None
try:
    #  Читаем данные из settings.json
    with open(gs.path.root / 'src' / 'settings.json', 'r') as settings_file:
        settings = j_loads(settings_file) # Используем j_loads
except (FileNotFoundError, json.JSONDecodeError) as ex:
    #  Логируем ошибку, если файл не найден или невалидный json
    logger.error(f'Ошибка чтения файла settings.json: {ex}')

doc_str: Optional[str] = None
try:
    #  Читаем содержимое README.MD
    with open(gs.path.root / 'src' / 'README.MD', 'r') as settings_file:
        doc_str = settings_file.read()
except (FileNotFoundError, json.JSONDecodeError) as ex:
    #  Логируем ошибку, если файл не найден или ошибка чтения
    logger.error(f'Ошибка чтения файла README.MD: {ex}')
     

__project_name__: str = settings.get('project_name', 'hypotez') if settings else 'hypotez'
"""str: Имя проекта."""
__version__: str = settings.get('version', '') if settings else ''
"""str: Версия проекта."""
__doc__: str = doc_str if doc_str else ''
"""str: Документация проекта из README.MD."""
__details__: str = ''
"""str: Детали проекта."""
__author__: str = settings.get('author', '') if settings else ''
"""str: Автор проекта."""
__copyright__: str = settings.get('copyrihgnt', '') if settings else ''
"""str: Информация об авторских правах."""
__cofee__: str = settings.get('cofee', "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69") if settings else "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69"
"""str: Сообщение для поддержки разработчика."""
```