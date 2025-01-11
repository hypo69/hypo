# Анализ кода модуля `header`

**Качество кода**
8
- Плюсы
    - Код выполняет поиск корневого каталога проекта.
    - Имеется загрузка настроек и документации из файлов.
    - Используются константы для хранения данных о проекте.
    - Код разбит на логические блоки, что улучшает читаемость.
- Минусы
    - Не хватает импортов модулей `json`, `sys`.
    - Использование `try-except` для `FileNotFoundError` и `json.JSONDecodeError` может быть упрощено с использованием `logger.error`.
    - Отсутствует документация в формате RST для модуля и переменных.
    - Желательно использовать `j_loads` или `j_loads_ns` из `src.utils.jjson` вместо стандартного `json.load`.
    - Не все переменные аннотированы типами.
    - Отсутствует `from src.logger.logger import logger`

**Рекомендации по улучшению**
1.  Добавить недостающие импорты `json`, `sys`, `from src.utils.jjson import j_loads` и `from src.logger.logger import logger`.
2.  Использовать `j_loads` для загрузки `settings.json`.
3.  Добавить документацию к модулю, переменным и функциям в формате RST.
4.  Заменить стандартный `try-except` на `logger.error` для обработки ошибок загрузки файла и JSON.
5.  Добавить аннотации типов для переменных.
6.  Обеспечить единообразие использования одинарных кавычек в коде.
7.  Переформулировать некоторые комментарии.

**Оптимизированный код**
```python
# -*- coding: utf-8 -*-
"""
Модуль для определения корневого каталога проекта, загрузки настроек и документации.
=========================================================================================

Этот модуль предназначен для автоматического определения корневого каталога проекта, загрузки
конфигурационных настроек из файла `settings.json` и чтения документации из файла `README.md`.
Модуль также устанавливает основные атрибуты проекта, такие как имя, версия, автор, и т.д.

Пример использования
--------------------

Для использования модуля достаточно импортировать его.  Модуль автоматически определит
корневой каталог проекта и загрузит необходимые данные.

.. code-block:: python

    from src.suppliers.aliexpress.campaign import header

    print(header.__project_name__)
    print(header.__version__)
"""

#! venv/bin/python/python3.12

import sys
from pathlib import Path
from src.utils.jjson import j_loads
from src.logger.logger import logger #  Импорт logger
import json # Импорт модуля json


def set_project_root(marker_files: tuple = ('__root__', '.git')) -> Path:
    """
    Определяет корневой каталог проекта, начиная с каталога текущего файла.

    Сканирует каталоги вверх по дереву, останавливаясь на первом каталоге,
    содержащем любой из файлов-маркеров.

    :param marker_files: Кортеж имен файлов или каталогов, идентифицирующих корень проекта.
    :type marker_files: tuple
    :return: Путь к корневому каталогу, если найден, иначе каталог, где расположен скрипт.
    :rtype: Path
    """
    __root__:Path
    current_path: Path = Path(__file__).resolve().parent
    __root__ = current_path
    for parent in [current_path] + list(current_path.parents):
        if any((parent / marker).exists() for marker in marker_files):
            __root__ = parent
            break
    if __root__ not in sys.path:
        sys.path.insert(0, str(__root__))
    return __root__


# Определение корневого каталога проекта
__root__: Path = set_project_root()
"""Path: Путь к корневому каталогу проекта."""

from src import gs

settings: dict | None = None
try:
    #  Загрузка настроек из файла settings.json
    with open(gs.path.root / 'src' / 'settings.json', 'r') as settings_file:
        settings = j_loads(settings_file)
except (FileNotFoundError, json.JSONDecodeError) as ex:
    #  Обработка ошибок при загрузке файла или декодировании JSON
    logger.error(f'Ошибка загрузки файла настроек: {ex}')
    ... # Остановка в случае ошибки

doc_str: str | None = None
try:
    #  Чтение документации из файла README.MD
    with open(gs.path.root / 'src' / 'README.MD', 'r') as settings_file:
        doc_str = settings_file.read()
except (FileNotFoundError, json.JSONDecodeError) as ex:
    #  Обработка ошибок при загрузке файла или декодировании JSON
    logger.error(f'Ошибка загрузки файла документации: {ex}')
    ... # Остановка в случае ошибки

__project_name__: str = settings.get('project_name', 'hypotez') if settings else 'hypotez'
"""str: Имя проекта."""
__version__: str = settings.get('version', '') if settings else ''
"""str: Версия проекта."""
__doc__: str = doc_str if doc_str else ''
"""str: Документация проекта."""
__details__: str = ''
"""str: Дополнительные сведения о проекте."""
__author__: str = settings.get('author', '') if settings else ''
"""str: Автор проекта."""
__copyright__: str = settings.get('copyrihgnt', '') if settings else ''
"""str: Авторские права проекта."""
__cofee__: str = settings.get('cofee', "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69") if settings else "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69"
"""str: Призыв поддержать разработчика чашкой кофе."""
```