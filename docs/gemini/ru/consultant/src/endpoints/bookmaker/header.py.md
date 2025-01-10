# Анализ кода модуля header.py

**Качество кода**
8
- Плюсы
    - Код выполняет свою задачу: определяет корневую директорию проекта, загружает настройки и документацию.
    - Используется `pathlib` для работы с путями, что делает код более читаемым и кроссплатформенным.
    - Есть обработка ошибок при загрузке файлов настроек и документации.
    - Присутствует базовая документация модуля.
- Минусы
    -  Используется `json.load` вместо `j_loads` или `j_loads_ns`.
    -  Отсутствуют импорты `j_loads` и `logger`.
    -  Вместо `try-except` c `...` предпочтительнее использовать `logger.error`.
    -  Отсутствует подробная документация функций и переменных в формате RST.
    -  Не все переменные имеют аннотации типов.
    - `__doc__` в переменной  записан результат чтения `README.MD`.
    - Отсутствует описание модуля и переменных в формате RST.

**Рекомендации по улучшению**

1.  Использовать `j_loads` из `src.utils.jjson` для загрузки JSON файлов.
2.  Импортировать `logger` из `src.logger.logger`.
3.  Заменить `try-except` с `...` на `try-except` с `logger.error` для более информативного логирования ошибок.
4.  Добавить docstring к функции `set_project_root` в формате RST.
5.  Добавить описание модуля в формате RST.
6.  Добавить аннотации типов для переменных.
7.  Переменной `__doc__` присвоить `__doc__` из модуля
8.  Добавить описание для каждой переменной в формате RST.
9.  Переименовать переменную `__cofee__` на `__coffee__`
10.  Вместо константы `'hypotez'` использовать `gs.DEFAULT_PROJECT_NAME`

**Оптимизированный код**

```python
"""
Модуль для определения корневой директории проекта и загрузки основных настроек.
==================================================================================

Этот модуль предназначен для автоматического определения корневой директории проекта
и загрузки основных настроек, таких как имя проекта, версия, автор и т.д.,
из файла `settings.json`, а так же загрузки документации из файла `README.MD`.

Пример использования
--------------------

.. code-block:: python

    from src.endpoints.bookmaker import header

    print(header.__project_name__)
    print(header.__version__)
    print(header.__author__)
"""
# -*- coding: utf-8 -*-

#! venv/bin/python/python3.12

import sys
from pathlib import Path
from packaging.version import Version

from src.utils.jjson import j_loads  # Импорт j_loads
from src.logger.logger import logger # Импорт logger
from src import gs


def set_project_root(marker_files: tuple[str, ...] = ('__root__', '.git')) -> Path:
    """
    Определяет корневой каталог проекта.
    ===================================

    Начиная с текущего каталога файла, поиск вверх по структуре каталогов
    до первого каталога, содержащего любой из файлов-маркеров.

    :param marker_files: tuple[str, ...]:  Список имен файлов-маркеров.
    :return: Path: Путь к корневому каталогу, если найден, иначе каталог, где расположен скрипт.
    
    :Example:
    
        >>> set_project_root()
        PosixPath('/home/user/project')
    
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


settings: dict | None = None
try:
    # код загружает настройки из файла settings.json используя j_loads
    with open(gs.path.root / 'src' / 'settings.json', 'r') as settings_file:
        settings = j_loads(settings_file)
except (FileNotFoundError, Exception) as e:
    logger.error(f'Ошибка загрузки файла settings.json: {e}')
    ...

doc_str: str | None = None
try:
    # код загружает документацию из файла README.MD
    with open(gs.path.root / 'src' / 'README.MD', 'r') as settings_file:
        doc_str = settings_file.read()
except (FileNotFoundError, Exception) as e:
        logger.error(f'Ошибка загрузки файла README.MD: {e}')
        ...


__project_name__: str = settings.get("project_name", gs.DEFAULT_PROJECT_NAME) if settings else gs.DEFAULT_PROJECT_NAME
"""str: Имя проекта."""
__version__: str = settings.get("version", '') if settings else ''
"""str: Версия проекта."""
__doc__: str = __doc__ if __doc__ else ''
"""str: Документация проекта."""
__details__: str = ''
"""str: Детали проекта."""
__author__: str = settings.get("author", '') if settings else ''
"""str: Автор проекта."""
__copyright__: str = settings.get("copyrihgnt", '') if settings else ''
"""str: Авторские права проекта."""
__coffee__: str = settings.get("cofee", "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69") if settings else "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69"
"""str: Призыв к чаепитию."""
```