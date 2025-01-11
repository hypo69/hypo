# Анализ кода модуля `header.py`

**Качество кода**
7
- Плюсы
    - Код содержит функцию `set_project_root`, которая корректно определяет корневую директорию проекта.
    - Используется `pathlib` для работы с путями, что является хорошей практикой.
    - Код пытается загрузить настройки из `settings.json` и `README.MD`, что полезно для конфигурации и документации.
    - Инициализация основных переменных проекта с использованием настроек.
- Минусы
    - Отсутствует импорт `logger` из `src.logger`.
    - Используется стандартный `json.load` вместо `j_loads` или `j_loads_ns`.
    - Отсутствует docstring для модуля.
    - Использование `try-except` с `...` может скрывать ошибки.
    - Не используется `gs.path` для работы с путями, `gs.path.root`  устарел.
    - Не стандартизированный комментарий для блока `__root__ = set_project_root()`.
    - Присвоение типа `__root__:Path` не является обязательным.
    - Комментарии в начале файла не несут смысловой нагрузки.

**Рекомендации по улучшению**

1.  Добавить docstring для модуля.
2.  Использовать `from src.logger.logger import logger` для логирования.
3.  Заменить `json.load` на `j_loads` или `j_loads_ns` из `src.utils.jjson`.
4.  Убрать неинформативные комментарии в начале файла.
5.  Обработку ошибок `FileNotFoundError` и `json.JSONDecodeError` перенести в логер.
6.  Использовать `gs.path.root` для получения корневого пути.
7.  Добавить документацию в формате RST для `set_project_root`.
8.  Удалить ненужное объявление типа `__root__:Path`.
9.  Стандартизировать комментарий для блока `__root__ = set_project_root()`.

**Оптимизированный код**

```python
"""
Модуль для определения основных настроек проекта и путей.
=========================================================================================

Этот модуль предназначен для:
- Поиска корневой директории проекта.
- Загрузки основных настроек проекта из файла settings.json.
- Получения документации из README.MD.
- Инициализации глобальных переменных проекта.

Пример использования
--------------------

Пример использования функции `set_project_root`::

    from pathlib import Path
    root_path = set_project_root()
    print(f"Корневая директория проекта: {root_path}")
"""
# -*- coding: utf-8 -*-

#! venv/bin/python/python3.12

import sys
from pathlib import Path
from packaging.version import Version
#  Импорт j_loads из src.utils.jjson
from src.utils.jjson import j_loads
#  Импорт logger из src.logger.logger
from src.logger.logger import logger
from src import gs


def set_project_root(marker_files: tuple = ('__root__', '.git')) -> Path:
    """
    Определяет корневую директорию проекта, начиная с директории текущего файла,
    и продвигаясь вверх до первого каталога, содержащего любой из маркеров.

    :param marker_files: Кортеж имен файлов или каталогов, определяющих корень проекта.
    :type marker_files: tuple
    :return: Путь к корневой директории.
    :rtype: Path

    :raises FileNotFoundError: Если маркерные файлы не найдены.

    :Example:
        >>> from pathlib import Path
        >>> root_path = set_project_root()
        >>> print(f"Корневая директория проекта: {root_path}")
        ...
    """
    current_path: Path = Path(__file__).resolve().parent
    __root__: Path = current_path
    for parent in [current_path] + list(current_path.parents):
        if any((parent / marker).exists() for marker in marker_files):
            __root__ = parent
            break
    if __root__ not in sys.path:
        sys.path.insert(0, str(__root__))
    return __root__


#  Получение корневой директории проекта
__root__ = set_project_root()
"""Path: Путь к корневой директории проекта."""

settings: dict = None
#  Загрузка настроек из файла settings.json
try:
    with open(gs.path.root / 'src' / 'settings.json', 'r') as settings_file:
        settings = j_loads(settings_file)
except (FileNotFoundError, json.JSONDecodeError) as ex:
    logger.error(f'Ошибка загрузки файла settings.json: {ex}')
    ...

doc_str: str = None
#  Чтение документации из файла README.MD
try:
    with open(gs.path.root / 'src' / 'README.MD', 'r') as settings_file:
        doc_str = settings_file.read()
except (FileNotFoundError, json.JSONDecodeError) as ex:
    logger.error(f'Ошибка загрузки файла README.MD: {ex}')
    ...

# Инициализация глобальных переменных
__project_name__ = settings.get("project_name", 'hypotez') if settings else 'hypotez'
__version__: str = settings.get("version", '') if settings else ''
__doc__: str = doc_str if doc_str else ''
__details__: str = ''
__author__: str = settings.get("author", '') if settings else ''
__copyright__: str = settings.get("copyrihgnt", '') if settings else ''
__cofee__: str = settings.get("cofee", "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69") if settings else "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69"
```