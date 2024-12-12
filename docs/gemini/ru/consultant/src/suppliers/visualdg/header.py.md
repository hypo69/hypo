# Анализ кода модуля `header.py`

**Качество кода**
9
-  Плюсы
    - Код имеет хорошую структуру и читаемость.
    - Используется `Pathlib` для работы с путями, что является хорошей практикой.
    - Присутствует обработка исключений при чтении файлов.
    - Код достаточно хорошо документирован с использованием docstring.
    - Есть разделение на логические блоки.
    - Используются константы для имени проекта, версии и т.д.
-  Минусы
    - Отсутствуют необходимые импорты из `src.utils.jjson`, которые должны быть использованы вместо стандартного `json.load`.
    - Не используется `logger` для логирования ошибок.
    - В блоках `try-except` используется `...`, что не позволяет отслеживать ошибки.
    - Присутствует дублирование кода при чтении `settings.json` и `README.MD`.

**Рекомендации по улучшению**

1.  **Импорты:** Добавить необходимые импорты из `src.utils.jjson` и `src.logger.logger`.
2.  **Обработка JSON:** Заменить `json.load` на `j_loads_ns` из `src.utils.jjson`.
3.  **Логирование:** Использовать `logger.error` для логирования ошибок вместо `...`.
4.  **Устранение дублирования:** Вынести логику чтения файла в отдельную функцию.
5.  **Комментарии:** Переписать комментарии в формате RST, добавить комментарии к переменным.
6.  **Переменные**: Для констант использовать написание в верхнем регистре (UPPER_CASE).

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
Модуль для настройки окружения и определения общих переменных проекта.
======================================================================

Модуль :mod:`src.suppliers.visualdg.header` предназначен для настройки окружения,
определения корня проекта и загрузки основных параметров проекта из файлов конфигурации.
Он также обеспечивает доступ к общим переменным, таким как имя проекта, версия и описание.

Пример использования
--------------------

.. code-block:: python

    from src.suppliers.visualdg.header import __project_name__, __version__, __doc__
    print(f"Project Name: {__project_name__}")
    print(f"Version: {__version__}")
    print(f"Documentation: {__doc__}")
"""
MODE = 'dev'

import sys
from pathlib import Path
# добавляем импорт j_loads_ns из src.utils.jjson
from src.utils.jjson import j_loads_ns
# добавляем импорт logger из src.logger.logger
from src.logger.logger import logger
from packaging.version import Version


def set_project_root(marker_files: tuple = ('pyproject.toml', 'requirements.txt', '.git')) -> Path:
    """
    Определяет корневой каталог проекта.

    Функция ищет корневой каталог проекта, начиная с текущего файла,
    поднимаясь вверх по дереву каталогов до тех пор, пока не найдет
    один из файлов-маркеров.

    :param marker_files: Список файлов-маркеров для определения корня проекта.
    :type marker_files: tuple
    :return: Путь к корневому каталогу проекта.
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
"""Path: Путь к корневому каталогу проекта"""

from src import gs


def _read_file(file_path: Path) -> str | dict | None:
    """
    Читает содержимое файла.

    Функция пытается прочитать файл как JSON, если не удается, то читает как текст.
    В случае ошибки логирует её и возвращает None.

    :param file_path: Путь к файлу.
    :type file_path: Path
    :return: Содержимое файла в виде строки или словаря, или None в случае ошибки.
    :rtype: str | dict | None
    """
    try:
        # код исполняет попытку чтения файла как JSON
        with open(file_path, 'r', encoding='utf-8') as file:
            if file_path.suffix == '.json':
                return j_loads_ns(file)
            else:
                return file.read()
    except (FileNotFoundError, json.JSONDecodeError) as ex:
        # логирование ошибки чтения файла
        logger.error(f'Ошибка при чтении файла {file_path}', exc_info=ex)
        return None


settings: dict = _read_file(gs.path.root / 'src' / 'settings.json')
"""dict: Словарь с настройками проекта, загруженный из `settings.json`"""

doc_str: str = _read_file(gs.path.root / 'src' / 'README.MD')
"""str: Строка с содержимым файла `README.MD`"""

# Переменные проекта
PROJECT_NAME: str = settings.get("project_name", 'hypotez') if settings else 'hypotez'
"""str: Имя проекта."""
VERSION: str = settings.get("version", '') if settings else ''
"""str: Версия проекта."""
DOC: str = doc_str if doc_str else ''
"""str: Документация проекта, загруженная из `README.MD`"""
DETAILS: str = ''
"""str: Детали проекта (не используется в коде)"""
AUTHOR: str = settings.get("author", '') if settings else ''
"""str: Автор проекта."""
COPYRIGHT: str = settings.get("copyrihgnt", '') if settings else ''
"""str: Авторские права проекта."""
COFEE: str = settings.get("cofee", "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69") if settings else "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69"
"""str: Сообщение о кофе."""
```