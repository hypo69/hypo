# Анализ кода модуля `header.py`

**Качество кода**
8
-   Плюсы
    -   Код выполняет поиск корневой директории проекта и устанавливает её в `sys.path`.
    -   Загружает настройки из `settings.json` и данные из `README.MD`, если они существуют.
    -   Определяет основные метаданные проекта, такие как имя, версия, автор и т.д.
-   Минусы
    -   Используется стандартный `json.load` вместо `j_loads` или `j_loads_ns` из `src.utils.jjson`.
    -   Не хватает обработки ошибок с использованием `logger.error`.
    -   Не используется `from src.logger.logger import logger` для логирования.
    -   В `try-except` блоках используется `...` вместо обработки ошибок.
    -   Не все переменные и константы имеют документацию.

**Рекомендации по улучшению**

1.  Заменить `json.load` на `j_loads` или `j_loads_ns` из `src.utils.jjson`.
2.  Использовать `logger.error` для обработки ошибок при загрузке файлов настроек и документации.
3.  Использовать `from src.logger.logger import logger` для импорта логгера.
4.  Добавить `docstring` к каждой переменной и константе.
5.  Убрать `...` из `try-except` блоков и добавить логирование ошибок.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-

#! venv/bin/python/python3.12

"""
Модуль для определения корневого каталога проекта и загрузки основных настроек.
=========================================================================================

Этот модуль определяет корневой каталог проекта, загружает настройки из файла `settings.json`
и данные из `README.MD`, а также устанавливает основные метаданные проекта.

Пример использования
--------------------

.. code-block:: python

    from src.logger.header import __root__, __project_name__, __version__, __doc__

    print(__root__)
    print(__project_name__)
    print(__version__)
    print(__doc__)
"""


import sys
from pathlib import Path
from packaging.version import Version
from src.utils.jjson import j_loads
from src.logger.logger import logger
from src import gs


def set_project_root(marker_files: tuple = ('__root__', '.git')) -> Path:
    """
    Определение корневого каталога проекта.

    Функция ищет корневой каталог проекта, начиная с директории текущего файла,
    поднимаясь вверх по дереву директорий и останавливаясь на первой директории,
    содержащей один из файлов-маркеров.

    Args:
        marker_files (tuple): Кортеж с именами файлов или директорий, которые идентифицируют корень проекта.

    Returns:
        Path: Путь к корневому каталогу, если он найден, иначе - путь к директории, где находится скрипт.
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


# Вызов функции set_project_root для определения корневой директории проекта
__root__: Path = set_project_root()
"""Path: Путь к корневой директории проекта."""


settings: dict = None
try:
    # Код загружает настройки из файла settings.json
    with open(gs.path.root / 'src' / 'settings.json', 'r') as settings_file:
        settings = j_loads(settings_file)
except (FileNotFoundError, ValueError) as e:
    logger.error('Ошибка при загрузке файла settings.json', exc_info=e)


doc_str: str = None
try:
    # Код загружает содержимое файла README.MD
    with open(gs.path.root / 'src' / 'README.MD', 'r') as settings_file:
        doc_str = settings_file.read()
except (FileNotFoundError,  UnicodeDecodeError) as e:
    logger.error('Ошибка при загрузке файла README.MD', exc_info=e)


__project_name__: str = settings.get('project_name', 'hypotez') if settings else 'hypotez'
"""str: Имя проекта."""
__version__: str = settings.get('version', '') if settings else ''
"""str: Версия проекта."""
__doc__: str = doc_str if doc_str else ''
"""str: Содержание файла README.MD."""
__details__: str = ''
"""str: Детали проекта."""
__author__: str = settings.get('author', '') if settings else ''
"""str: Автор проекта."""
__copyright__: str = settings.get('copyrihgnt', '') if settings else ''
"""str: Авторские права."""
__cofee__: str = settings.get('cofee', "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69") if settings else "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69"
"""str: Сообщение с предложением угостить разработчика кофе."""
```