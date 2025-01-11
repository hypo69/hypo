# Анализ кода модуля `header.py`

**Качество кода**
9
-  Плюсы
    - Код хорошо структурирован и легко читается.
    - Присутствует документация для модуля и функции `set_project_root`.
    - Используется `pathlib` для работы с путями.
    - Логика определения корневой директории проекта корректна.
    - Добавлены переменные для настроек проекта, версии, автора и т.д.

- Минусы
    - Не используются константы для ключей json, что может привести к опечаткам и ошибкам.
    - Отсутствуют докстринги для переменных модуля.
    - Стандартный `json.load`  используется для загрузки json файлов.
    - `logger` не импортируется из `src.logger`, а ошибки обрабатываются через `try-except` + `...`.

**Рекомендации по улучшению**

1.  **Добавить докстринги для переменных модуля**:  
    - Добавить описания для переменных `__project_name__`, `__version__`, `__doc__`, `__details__`, `__author__`, `__copyright__`, `__cofee__`.
2.  **Использовать `j_loads_ns` для загрузки JSON**:  
    - Заменить `json.load` на `j_loads_ns` из `src.utils.jjson`.
3.  **Импортировать `logger` из `src.logger`**:  
    - Добавить `from src.logger import logger` и использовать его для логирования ошибок.
4.  **Убрать `try-except` с `...` и использовать `logger.error`**:  
    - Заменить `try-except` блоки на более явную обработку ошибок с помощью `logger.error`.
5.  **Использовать константы для ключей `json`**:
    - Вынести ключи `project_name`, `version`, `author`, `copyrihgnt` и `cofee` в константы.
6.  **Добавить описание модуля**:
    - В начало файла добавить описание модуля, согласно инструкциям.
7.  **Привести в порядок импорты**
    - Добавить отсутствующие импорты.
8.  **Упростить чтение README.MD**
    - Убрать ненужную обработку `json.JSONDecodeError` при чтении `README.MD`.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-

#! venv/bin/python/python3.12
"""
Модуль инициализации и настроек проекта.
========================================

Этот модуль отвечает за определение корневой директории проекта, загрузку настроек из JSON-файла,
а также инициализацию основных переменных, таких как имя проекта, версия и автор.
Модуль также обеспечивает доступ к документации проекта из файла README.MD

Основные функции:
    - `set_project_root`: Определяет корневую директорию проекта.
    - Инициализация переменных: Загружает настройки и устанавливает глобальные переменные проекта.

Пример использования:
--------------------

.. code-block:: python

    from src.suppliers.amazon.header import __project_name__, __version__, __author__

    print(f"Project Name: {__project_name__}")
    print(f"Version: {__version__}")
    print(f"Author: {__author__}")
"""
import sys
from pathlib import Path
from packaging.version import Version

from src.logger import logger
from src.utils.jjson import j_loads_ns
from src import gs

__PROJECT_NAME_KEY__ = "project_name"
__VERSION_KEY__ = "version"
__AUTHOR_KEY__ = "author"
__COPYRIGHT_KEY__ = "copyrihgnt"
__COFEE_KEY__ = "cofee"


def set_project_root(marker_files: tuple = ('__root__', '.git')) -> Path:
    """
    Определяет корневую директорию проекта.

    Функция ищет корневую директорию проекта, начиная с директории текущего файла,
    двигаясь вверх по дереву каталогов, пока не найдет директорию, содержащую
    один из файлов-маркеров.

    Args:
        marker_files (tuple): Кортеж имен файлов или директорий, которые идентифицируют корень проекта.

    Returns:
        Path: Путь к корневой директории, если она найдена, иначе путь к директории, где находится скрипт.

    Example:
        >>> set_project_root()
        .../hypotez
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

settings: dict = None
try:
    #  чтение файла настроек из `settings.json`
    with open(gs.path.root / 'src' / 'settings.json', 'r') as settings_file:
         settings = j_loads_ns(settings_file)
except FileNotFoundError:
    logger.error(f'Файл настроек не найден {gs.path.root / "src" / "settings.json"}')
    settings = {}
except Exception as e:
    logger.error(f'Ошибка при чтении файла настроек {e}')
    settings = {}


doc_str: str = None
try:
    # чтение файла документации из `README.MD`
    with open(gs.path.root / 'src' / 'README.MD', 'r') as doc_file:
        doc_str = doc_file.read()
except FileNotFoundError:
    logger.error(f'Файл документации не найден {gs.path.root / "src" / "README.MD"}')
    doc_str = ''

#  Получение настроек из settings.json или установка значений по умолчанию
__project_name__: str = settings.get(__PROJECT_NAME_KEY__, 'hypotez') if settings else 'hypotez'
"""__project_name__ (str): Имя проекта."""
__version__: str = settings.get(__VERSION_KEY__, '') if settings else ''
"""__version__ (str): Версия проекта."""
__doc__: str = doc_str if doc_str else ''
"""__doc__ (str): Строка документации проекта."""
__details__: str = ''
"""__details__ (str): Детали проекта."""
__author__: str = settings.get(__AUTHOR_KEY__, '') if settings else ''
"""__author__ (str): Автор проекта."""
__copyright__: str = settings.get(__COPYRIGHT_KEY__, '') if settings else ''
"""__copyright__ (str): Информация об авторских правах."""
__cofee__: str = settings.get(__COFEE_KEY__, "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69") if settings else "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69"
"""__cofee__ (str): Сообщение для поддержки разработчика."""
```