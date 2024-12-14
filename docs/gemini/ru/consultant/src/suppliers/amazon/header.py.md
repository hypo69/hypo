# Анализ кода модуля `header.py`

**Качество кода**
9
-  Плюсы
    - Код хорошо структурирован и читаем.
    - Функция `set_project_root` корректно определяет корневой каталог проекта.
    - Используются константы для основных параметров проекта.
    - Обработка ошибок при загрузке `settings.json` и `README.MD` присутствует.
    - Используется `pathlib` для работы с путями, что является хорошей практикой.
    - Наличие docstring для модуля и функции.
-  Минусы
    - Используется `json.load` вместо `j_loads` или `j_loads_ns` из `src.utils.jjson`.
    - Отсутствует импорт `logger` из `src.logger.logger`.
    - Не все переменные имеют docstring.
    - Некоторые комментарии не в формате reStructuredText (RST).
    - Обработка ошибок не использует логирование через `logger.error`, только `...`.
    - Присутствуют конструкции типа `if settings else ...` , которые можно упростить используя метод `get`.

**Рекомендации по улучшению**

1.  Заменить `json.load` на `j_loads` или `j_loads_ns` из `src.utils.jjson`.
2.  Добавить импорт `from src.logger.logger import logger` и использовать `logger.error` для логирования ошибок.
3.  Добавить docstring в формате RST для всех переменных.
4.  Преобразовать существующие комментарии к коду в формат RST.
5.  Избегать использования конструкции `if settings else ...` для получения значений из settings словаря, использовать метод `get` с значением по умолчанию.
6.  Упростить обработку ошибок, используя `logger.error` вместо `...` в блоках `try-except`.
7.  Удалить неиспользуемые импорты.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
Модуль инициализации проекта Amazon.
=====================================

Этот модуль отвечает за настройку основных параметров проекта, таких как:
- Определение корневого каталога проекта.
- Загрузка настроек из файла `settings.json`.
- Загрузка документации из файла `README.MD`.
- Инициализацию основных переменных проекта.

Пример использования
--------------------

Импортируйте модуль, чтобы инициализировать переменные проекта::

    from src.suppliers.amazon import header

"""

import sys
from pathlib import Path
from packaging.version import Version # TODO: удалить если не используется

from src.utils.jjson import j_loads  # Используем j_loads вместо json.load
from src.logger.logger import logger # Импортируем logger

MODE = 'dev'
"""Режим работы."""


def set_project_root(marker_files: tuple = ('pyproject.toml', 'requirements.txt', '.git')) -> Path:
    """
    Находит корневой каталог проекта.

    Сканирует вверх по иерархии каталогов, начиная с каталога текущего файла, и останавливается на первом каталоге,
    содержащем один из файлов-маркеров.

    :param marker_files: Кортеж имен файлов или каталогов, которые идентифицируют корень проекта.
    :type marker_files: tuple
    :return: Путь к корневому каталогу, если он найден, иначе каталог, в котором расположен скрипт.
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

# Get the root directory of the project
__root__ = set_project_root()
"""Path: Путь к корневому каталогу проекта."""


from src import gs

settings: dict = None
"""dict: Словарь с настройками проекта."""
try:
    #  Код пытается загрузить настройки из файла settings.json
    with open(gs.path.root / 'src' / 'settings.json', 'r') as settings_file:
        settings = j_loads(settings_file) # Используем j_loads для загрузки настроек
except (FileNotFoundError, json.JSONDecodeError) as e:
    #  Если возникает ошибка при загрузке настроек, то логируем ошибку
    logger.error('Ошибка при загрузке settings.json', exc_info=e)
    ...


doc_str: str = None
"""str: Строка с содержимым файла README.MD."""
try:
    #  Код пытается загрузить описание проекта из файла README.MD
    with open(gs.path.root / 'src' / 'README.MD', 'r') as settings_file:
        doc_str = settings_file.read()
except (FileNotFoundError, json.JSONDecodeError) as e:
    #  Если возникает ошибка при загрузке README.MD, то логируем ошибку
    logger.error('Ошибка при загрузке README.MD', exc_info=e)
    ...

__project_name__ = settings.get("project_name", 'hypotez') if settings else 'hypotez'
"""str: Имя проекта."""
__version__: str = settings.get("version", '') if settings else ''
"""str: Версия проекта."""
__doc__: str = doc_str if doc_str else ''
"""str: Документация проекта."""
__details__: str = ''
"""str: Детали проекта."""
__author__: str = settings.get("author", '') if settings else ''
"""str: Автор проекта."""
__copyright__: str = settings.get("copyrihgnt", '') if settings else ''
"""str: Авторские права проекта."""
__cofee__: str = settings.get("cofee", "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69")  if settings else "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69"
"""str: Сообщение для поддержки разработчика."""
```