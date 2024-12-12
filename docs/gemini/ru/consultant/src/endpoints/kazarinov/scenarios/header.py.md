# Анализ кода модуля `header.py`

**Качество кода**
8
-   Плюсы
    -   Код достаточно хорошо структурирован, используется `Pathlib` для работы с путями, что является хорошей практикой.
    -   Присутствует функция `set_project_root` для определения корневой директории проекта, что полезно для работы с относительными путями.
    -   Код использует `try-except` блоки для обработки ошибок при чтении файлов конфигурации, что обеспечивает устойчивость программы.
-   Минусы
    -   Используется стандартный `json.load` вместо `j_loads` или `j_loads_ns` из `src.utils.jjson`.
    -   Отсутствуют некоторые импорты, необходимые для корректной работы с кодом.
    -   Не все переменные и функции имеют docstring в формате reStructuredText (RST).
    -   Обработка ошибок `FileNotFoundError` и `json.JSONDecodeError`  в блоках `try-except`  не записывается в лог.
    -   Код содержит избыточное использование `try-except` с `...`.

**Рекомендации по улучшению**

1.  Использовать `j_loads` из `src.utils.jjson` для чтения `settings.json` файла.
2.  Добавить необходимые импорты, включая `from src.utils.jjson import j_loads`.
3.  Добавить docstring в формате RST для функций и переменных, включая описание модуля.
4.  Использовать `logger.error` для логирования ошибок вместо `...` в `try-except` блоках.
5.  Удалить избыточные блоки `try-except` и `...`
6.  Обеспечить соответствие наименований переменных и функций с ранее обработанными файлами.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
Модуль для установки настроек проекта.
=====================================

Этот модуль определяет корневую директорию проекта, загружает настройки из файла `settings.json` и устанавливает
глобальные переменные, такие как имя проекта, версия и автор.

Пример использования
--------------------

.. code-block:: python

    from src.endpoints.kazarinov.scenarios.header import __project_name__, __version__, __author__

    print(f"Имя проекта: {__project_name__}")
    print(f"Версия проекта: {__version__}")
    print(f"Автор проекта: {__author__}")
"""

MODE = 'dev'

import sys
from pathlib import Path
from packaging.version import Version

from src.utils.jjson import j_loads
from src.logger.logger import logger


def set_project_root(marker_files: tuple = ('pyproject.toml', 'requirements.txt', '.git')) -> Path:
    """
    Определяет корневую директорию проекта.

    Ищет корневую директорию проекта, начиная с директории текущего файла,
    поднимаясь вверх по дереву директорий, пока не найдет директорию, содержащую
    один из указанных файлов-маркеров.

    :param marker_files: Кортеж имен файлов или директорий, которые идентифицируют корневую директорию проекта.
    :type marker_files: tuple
    :return: Путь к корневой директории проекта.
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


# Получение корневой директории проекта
__root__ = set_project_root()
"""__root__ (Path): Путь к корневой директории проекта."""

from src import gs

settings: dict = None
try:
    # Код выполняет загрузку настроек из файла settings.json
    with open(gs.path.root / 'src' / 'settings.json', 'r') as settings_file:
        settings = j_loads(settings_file)
except (FileNotFoundError, json.JSONDecodeError) as ex:
    # В случае ошибки чтения файла или декодирования JSON,  выполняется логирование ошибки
    logger.error(f'Ошибка при чтении файла settings.json: {ex}')


doc_str: str = None
try:
    # Код исполняет чтение содержимого файла README.MD
    with open(gs.path.root / 'src' / 'README.MD', 'r') as settings_file:
        doc_str = settings_file.read()
except (FileNotFoundError, json.JSONDecodeError) as ex:
    # В случае ошибки чтения файла или декодирования JSON, выполняется логирование ошибки
    logger.error(f'Ошибка при чтении файла README.MD: {ex}')

__project_name__: str = settings.get("project_name", 'hypotez') if settings else 'hypotez'
"""__project_name__ (str): Имя проекта."""
__version__: str = settings.get("version", '') if settings else ''
"""__version__ (str): Версия проекта."""
__doc__: str = doc_str if doc_str else ''
"""__doc__ (str): Строка документации проекта."""
__details__: str = ''
"""__details__ (str): Детали проекта."""
__author__: str = settings.get("author", '') if settings else ''
"""__author__ (str): Автор проекта."""
__copyright__: str = settings.get("copyrihgnt", '') if settings else ''
"""__copyright__ (str): Информация об авторских правах."""
__cofee__: str = settings.get("cofee", "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69") if settings else "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69"
"""__cofee__ (str): Сообщение о пожертвовании на кофе."""
```