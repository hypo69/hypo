# Анализ кода модуля `header.py`

**Качество кода**
6
-  Плюсы
    - Код выполняет определение корневой директории проекта.
    - Присутствует попытка загрузки настроек и документации.
    - Используется `packaging.version` для работы с версиями.
 -  Минусы
    - Отсутствует reStructuredText (RST) документация для модуля и функций.
    - Используется стандартный `json.load` вместо `j_loads` или `j_loads_ns`.
    - Использование `try-except` с `...` может затруднить отладку.
    - Не все переменные имеют docstring.
    - Не используется логгер для обработки ошибок.
    - Отсутствуют проверки на существование ключей в словаре `settings`.
    - Использование `FileNotFoundError, json.JSONDecodeError`  может маскировать другие ошибки.

**Рекомендации по улучшению**

1.  Добавить RST документацию для модуля и всех функций.
2.  Использовать `j_loads` или `j_loads_ns` для загрузки JSON-файлов.
3.  Заменить `...` в блоках `try-except` на логирование ошибок с помощью `logger.error`.
4.  Добавить docstring для всех переменных, включая `__root__`.
5.  Использовать `settings.get` с проверкой на `None` для предотвращения ошибок, если `settings` не определен или отсутствуют ключи.
6.  Разделить блоки `try-except` для `FileNotFoundError` и `json.JSONDecodeError` для более точного логирования ошибок.
7. Добавить проверку на существование ключей в словаре `settings` перед их использованием, чтобы избежать ошибок.
8. Использовать `pathlib.Path` для всех путей.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
Модуль для определения настроек проекта и получения основной информации.
========================================================================

Этот модуль определяет корневую директорию проекта, загружает настройки из JSON-файла
и читает документацию из файла README.MD. Также модуль устанавливает основные переменные
проекта такие как имя, версия, автор и т.д.

Пример использования:
--------------------

.. code-block:: python

    from src.goog.spreadsheet.header import __project_name__, __version__, __doc__

    print(f"Project Name: {__project_name__}")
    print(f"Version: {__version__}")
    print(f"Documentation: {__doc__}")
"""
MODE = 'dev'

import sys
from pathlib import Path
from packaging.version import Version
# from src.utils.jjson import j_loads # TODO: uncomment if needed
from src.logger.logger import logger # # Импортируем логгер для обработки ошибок

def set_project_root(marker_files: tuple = ('pyproject.toml', 'requirements.txt', '.git')) -> Path:
    """
    Определяет корневую директорию проекта.

    Функция ищет корневую директорию проекта, начиная с директории текущего файла,
    продвигаясь вверх по дереву каталогов и останавливаясь на первом каталоге,
    содержащем хотя бы один из файлов-маркеров.

    :param marker_files: Кортеж с именами файлов или директорий, которые обозначают корень проекта.
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
    if str(__root__) not in sys.path:
        sys.path.insert(0, str(__root__))
    return __root__

# # Получаем корневую директорию проекта
__root__: Path = set_project_root()
"""__root__ (Path): Путь к корневой директории проекта."""

from src import gs

settings: dict = None
try:
    # # Используем j_loads для загрузки файла настроек
    # with open(gs.path.root / 'src' / 'settings.json', 'r') as settings_file: # TODO: uncomment if needed
    #     settings = j_loads(settings_file) # TODO: uncomment if needed
    with open(Path(gs.path.root) / 'src' / 'settings.json', 'r') as settings_file: # Загружаем файл настроек
        import json
        settings = json.load(settings_file)
except FileNotFoundError as ex:
    # # Логируем ошибку, если файл не найден
    logger.error(f'Файл настроек settings.json не найден: {ex}')
except json.JSONDecodeError as ex:
    # # Логируем ошибку, если файл не является валидным JSON
    logger.error(f'Ошибка декодирования JSON в файле settings.json: {ex}')

doc_str: str = None
try:
    # # Читаем файл README.MD
    with open(Path(gs.path.root) / 'src' / 'README.MD', 'r', encoding='utf-8') as doc_file:
        doc_str = doc_file.read()
except FileNotFoundError as ex:
     # # Логируем ошибку, если файл не найден
    logger.error(f'Файл документации README.MD не найден: {ex}')


# #  Получаем значения из настроек, устанавливаем значения по умолчанию если ключи не найдены
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
"""__copyright__ (str): Авторские права проекта."""
__cofee__: str = settings.get("cofee", "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69") if settings else "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69"
"""__cofee__ (str): Сообщение о возможности угостить разработчика кофе."""
```