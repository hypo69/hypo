# Анализ кода модуля `header.py`

**Качество кода**
7
 -  Плюсы
    - Код имеет docstring для модуля.
    - Функция `set_project_root` имеет docstring, описывающий ее назначение, аргументы и возвращаемое значение.
    - Используется `pathlib` для работы с путями, что является хорошей практикой.
    - Присутствует базовая обработка ошибок для чтения `settings.json` и `README.MD`.
    - Переменные настроек вынесены в глобальную область видимости.
 -  Минусы
    - Не используется `j_loads` или `j_loads_ns` из `src.utils.jjson` для чтения `settings.json`.
    - Не все переменные имеют docstring.
    - Использование `try-except` с многоточием `...` вместо логирования ошибок.
    - Наличие `__cofee__` как параметра в коде.
    - Нет импорта `from src.logger.logger import logger`.
    - Не стандартизированы кавычки в коде.
    - Не хватает документации для переменных.

**Рекомендации по улучшению**

1.  Использовать `j_loads` из `src.utils.jjson` для загрузки JSON файлов.
2.  Добавить логирование ошибок с помощью `logger.error` вместо `...` в блоках `try-except`.
3.  Добавить docstring для всех глобальных переменных, включая `__root__`, `settings`, `doc_str` и др.
4.  Использовать одинарные кавычки в коде (кроме операций вывода).
5.  Импортировать `logger` из `src.logger.logger`.
6.  Убрать `__cofee__` как параметр и вынести его в конфиг или переменную среды.
7.  Сделать консистентными наименования переменных.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
"""
Модуль определяет корневой путь к проекту и загружает основные настройки.
=========================================================================================

Этот модуль выполняет поиск корневой директории проекта, устанавливает ее в `sys.path`
и загружает основные параметры из `settings.json` и `README.MD`.

Пример использования
--------------------

Пример использования:

.. code-block:: python

    from src.logger.header import __root__, __project_name__, __version__

    print(f"Project root: {__root__}")
    print(f"Project name: {__project_name__}")
    print(f"Project version: {__version__}")

"""
import sys
from pathlib import Path
from packaging.version import Version
# импортируем j_loads из src.utils.jjson
from src.utils.jjson import j_loads
# импортируем logger из src.logger.logger
from src.logger.logger import logger

def set_project_root(marker_files: tuple = ('__root__', '.git')) -> Path:
    """
    Определяет корневую директорию проекта.

    Обходит директории вверх от текущего файла, пока не найдет директорию, содержащую
    один из файлов-маркеров.

    Args:
        marker_files (tuple): Кортеж с именами файлов или директорий, которые идентифицируют корень проекта.

    Returns:
        Path: Путь к корневой директории проекта.
        Если корень не найден, возвращает директорию, где находится скрипт.
    """
    __root__:Path
    current_path:Path = Path(__file__).resolve().parent
    __root__ = current_path
    for parent in [current_path] + list(current_path.parents):
        if any((parent / marker).exists() for marker in marker_files):
            __root__ = parent
            break
    if __root__ not in sys.path:
        sys.path.insert(0, str(__root__))
    return __root__


# Получение корневой директории проекта
__root__:Path = set_project_root()
"""Path: Путь к корневой директории проекта."""


from src import gs

settings: dict = None
"""dict: Словарь с настройками проекта, загруженный из 'settings.json'."""
try:
    # используем j_loads для загрузки json
    with open(gs.path.root / 'src' /  'settings.json', 'r') as settings_file:
        settings = j_loads(settings_file)
except (FileNotFoundError,  Exception) as ex:
    # логируем ошибку
    logger.error('Ошибка загрузки settings.json', exc_info=ex)

doc_str: str = None
"""str: Строка с содержимым файла 'README.MD'."""
try:
    with open(gs.path.root / 'src' /  'README.MD', 'r') as readme_file:
        doc_str = readme_file.read()
except (FileNotFoundError,  Exception) as ex:
    # логируем ошибку
    logger.error('Ошибка загрузки README.MD', exc_info=ex)

# Проектные параметры
__project_name__: str = settings.get('project_name', 'hypotez') if settings  else 'hypotez'
"""str: Имя проекта, извлекается из settings.json или значение по умолчанию 'hypotez'."""
__version__: str = settings.get('version', '') if settings else ''
"""str: Версия проекта, извлекается из settings.json или пустая строка."""
__doc__: str = doc_str if doc_str else ''
"""str: Содержание файла README.MD или пустая строка."""
__details__: str = ''
"""str: Дополнительная информация о проекте."""
__author__: str = settings.get('author', '') if settings else ''
"""str: Автор проекта, извлекается из settings.json или пустая строка."""
__copyright__: str = settings.get('copyrihgnt', '') if settings else ''
"""str: Информация об авторских правах, извлекается из settings.json или пустая строка."""
__cofee__: str = "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69"
"""str: Сообщение о поддержке разработчика."""
```