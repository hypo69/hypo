# Анализ кода модуля header.py

**Качество кода**
8
 -  Плюсы
    - Код выполняет поставленную задачу по определению корневой директории проекта.
    - Используются комментарии для пояснения кода.
    - Присутствует обработка исключений при чтении файлов конфигурации.
    - Применяется `pathlib` для работы с путями, что является хорошей практикой.
    - Добавлены docstring для функций.
 -  Минусы
    - Используется стандартный `json.load` вместо `j_loads` из `src.utils.jjson`.
    - Не все переменные имеют аннотации типов.
    - Отсутствуют импорты `logger` из `src.logger`.
    - Избыточное использование `try-except` вместо `logger.error`.
    - Есть `...` в блоках `except`, которые лучше заменить на логирование ошибки.
    - В docstring для модуля и функций недостаточно подробное описание.
    - Не используется `f-строки`.
    - Отсутствует описание модуля в начале файла.
    - Некоторые имена переменных не соответствуют стандарту (например, `doc_str` вместо `doc_string`).

**Рекомендации по улучшению**

1.  Заменить `json.load` на `j_loads_ns` из `src.utils.jjson`.
2.  Добавить аннотации типов для переменных.
3.  Импортировать `logger` из `src.logger.logger`.
4.  Заменить `try-except` на обработку ошибок с помощью `logger.error`.
5.  Заменить `...` на логирование ошибок.
6.  Дополнить docstring для модуля и функций, следуя стандарту RST.
7.  Использовать `f-строки` для форматирования строк.
8.  Переименовать переменные для соответствия стандартам, например, `doc_str` в `doc_string`.
9.  Добавить описание модуля в начале файла.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
#! venv/bin/python/python3.12
"""
Модуль для определения корневого пути проекта и загрузки основных настроек.
=========================================================================

Этот модуль определяет корневой путь проекта на основе наличия файлов-маркеров
(__root__, .git) в директориях. Также выполняет загрузку настроек из `settings.json`
и `README.MD`, устанавливает основные переменные проекта, такие как имя, версия,
документация, авторские права и сообщение для поддержки.

Пример использования
--------------------

Пример использования:

.. code-block:: python

    from src.logger.header import __root__, __project_name__, __version__

    print(f"Корневая директория: {__root__}")
    print(f"Имя проекта: {__project_name__}")
    print(f"Версия проекта: {__version__}")

"""
import sys
from pathlib import Path
from packaging.version import Version
from src.utils.jjson import j_loads_ns
from src.logger.logger import logger # Импортирован logger

def set_project_root(marker_files: tuple = ('__root__', '.git')) -> Path:
    """
    Определяет корневую директорию проекта.

    Функция осуществляет поиск корневой директории проекта, начиная с директории
    текущего файла, поднимаясь вверх по дереву каталогов. Поиск завершается при
    обнаружении директории, содержащей один из файлов-маркеров.

    Args:
        marker_files (tuple): Кортеж имен файлов или директорий, указывающих на корневую директорию.

    Returns:
        Path: Путь к корневой директории проекта, если она найдена, иначе - директория, где находится скрипт.
    """
    root: Path  # аннотация типа
    current_path: Path = Path(__file__).resolve().parent
    root = current_path
    for parent in [current_path] + list(current_path.parents):
        if any((parent / marker).exists() for marker in marker_files):
            root = parent
            break
    if root not in sys.path:
        sys.path.insert(0, str(root))
    return root


#  Код исполняет получение корневой директории проекта
__root__: Path = set_project_root()
"""__root__ (Path): Путь к корневой директории проекта"""

from src import gs
settings: dict | None = None  # аннотация типа
try:
    # Код исполняет чтение файла настроек
    with open(gs.path.root / 'src' / 'settings.json', 'r') as settings_file:
        settings = j_loads_ns(settings_file) # Используется j_loads_ns
except (FileNotFoundError, Exception) as ex: # Обработка ошибок чтения файла настроек
    logger.error(f'Ошибка чтения файла настроек: {ex}', exc_info=True)  #  Логирование ошибки и ее типа


doc_string: str | None = None # аннотация типа
try:
    # Код исполняет чтение файла документации
    with open(gs.path.root / 'src' / 'README.MD', 'r') as doc_file:
        doc_string = doc_file.read()
except (FileNotFoundError, Exception) as ex: # Обработка ошибок чтения файла документации
    logger.error(f'Ошибка чтения файла документации: {ex}', exc_info=True) # Логирование ошибки и ее типа

__project_name__: str = settings.get("project_name", 'hypotez') if settings else 'hypotez' #  установка имени проекта
__version__: str = settings.get("version", '') if settings else '' # установка версии проекта
__doc__: str = doc_string if doc_string else ''  # установка документации проекта
__details__: str = ''  # установка подробностей проекта
__author__: str = settings.get("author", '') if settings else ''  #  установка автора проекта
__copyright__: str = settings.get("copyrihgnt", '') if settings else ''  # установка авторских прав проекта
__cofee__: str = settings.get("cofee", "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69") if settings else "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69"  #  установка сообщения для поддержки
```