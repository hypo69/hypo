# Анализ кода модуля `header.py`

**Качество кода**
7
-  Плюсы
    - Код содержит docstring для модуля.
    - Используется `pathlib` для работы с путями.
    - Код обрабатывает исключения при загрузке файлов настроек.
    - Используется переменная `__root__` для хранения пути к корню проекта.
-  Минусы
    - Не используются `j_loads` или `j_loads_ns` из `src.utils.jjson`.
    - Присутствуют общие блоки `try-except` с `...`.
    - Нет подробных docstring для функций и переменных.
    - Некоторые переменные используются без явного указания типа.
    - Присутствует дублирование кода в блоках `try` при загрузке `settings.json` и `README.MD`.

**Рекомендации по улучшению**

1.  **Использование `j_loads`**: Замените `json.load` на `j_loads` из `src.utils.jjson` для загрузки `settings.json`.
2.  **Логирование ошибок**: Используйте `logger.error` для обработки ошибок вместо общих блоков `try-except` с `...`.
3.  **Документация**: Добавьте подробные docstring для всех функций, переменных и констант в формате reStructuredText (RST).
4.  **Уточнение типов**: Добавьте аннотации типов для переменных, где это необходимо.
5.  **Избегание дублирования кода**: Рефакторинг блоков чтения файлов в отдельную функцию для уменьшения дублирования кода.
6.  **Импорт**: Добавьте отсутствующие импорты, например `from src.utils.jjson import j_loads` и `from src.logger.logger import logger`.

**Оптимизированный код**
```python
"""
Модуль :mod:`src.suppliers.morlevi.header`
=========================================================================================

Модуль предоставляет основные настройки и метаданные для проекта.

Содержит функции и константы для определения корневой директории проекта,
загрузки настроек из JSON файла, чтения README файла и определения общих метаданных.

Пример использования
--------------------

Импортируйте константы и функции для получения информации о проекте:

.. code-block:: python

    from src.suppliers.morlevi.header import __version__, __project_name__, __doc__

"""
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

import sys
from pathlib import Path
from packaging.version import Version

from src.utils.jjson import j_loads #  Импортирован j_loads
from src.logger.logger import logger #  Импортирован logger


"""str: Режим работы приложения (например, 'dev' или 'prod')."""


def set_project_root(marker_files: tuple = ('__root__',)) -> Path:
    """
    Определяет корневую директорию проекта, начиная с текущей директории файла.

    Поиск идет вверх по дереву директорий и останавливается на первой директории, содержащей любой из указанных файлов-маркеров.

    :param marker_files: Кортеж имен файлов или директорий, которые идентифицируют корень проекта.
    :type marker_files: tuple, optional
    :return: Путь к корневой директории. Если корень не найден, возвращает директорию, где расположен скрипт.
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

# Вычисляется корневая директория проекта
__root__: Path = set_project_root()
"""Path: Путь к корневой директории проекта."""

from src import gs

settings: dict = None
"""dict: Словарь с настройками проекта, загруженными из 'settings.json'."""

doc_str: str = None
"""str: Строка с содержимым файла 'README.MD'."""

def _load_file(file_path: Path, loader_function):
    """
    Загружает данные из файла, используя переданную функцию загрузки.

    :param file_path: Путь к файлу для загрузки.
    :type file_path: Path
    :param loader_function: Функция для загрузки данных (например, j_loads или read).
    :type loader_function: Callable
    :return: Загруженные данные или None в случае ошибки.
    :rtype: Any
    """
    try:
         #  код исполняет открытие файла и загрузку данных с использованием loader_function
        with open(file_path, 'r', encoding='utf-8') as file:
           return loader_function(file)
    except FileNotFoundError:
        logger.error(f'Файл не найден: {file_path}') #  Логирование ошибки отсутствия файла
        return None
    except Exception as ex:
        logger.error(f'Ошибка при загрузке файла: {file_path}', exc_info=ex) # Логирование ошибки загрузки файла
        return None


# Загрузка настроек из файла settings.json
settings = _load_file(gs.path.root / 'src' / 'settings.json', j_loads)

# Чтение содержимого файла README.MD
doc_str = _load_file(gs.path.root / 'src' / 'README.MD', lambda file: file.read())

__project_name__: str = settings.get("project_name", 'hypotez') if settings else 'hypotez'
"""str: Название проекта, по умолчанию 'hypotez'."""

__version__: str = settings.get("version", '') if settings else ''
"""str: Версия проекта, по умолчанию пустая строка."""

__doc__: str = doc_str if doc_str else ''
"""str: Строка с содержимым файла 'README.MD' или пустая строка, если файл не найден."""

__details__: str = ''
"""str: Детали проекта (в данный момент не используются)."""

__author__: str = settings.get("author", '') if settings else ''
"""str: Автор проекта, по умолчанию пустая строка."""

__copyright__: str = settings.get("copyrihgnt", '') if settings else ''
"""str: Информация об авторских правах, по умолчанию пустая строка."""

__cofee__: str = settings.get("cofee", "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69") if settings else "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69"
"""str: Сообщение с предложением поддержать разработчика."""
```