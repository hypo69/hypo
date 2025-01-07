# Анализ кода модуля header.py

**Качество кода**
8
-  Плюсы
    - Код структурирован и выполняет свою задачу по определению корневой директории проекта.
    - Используются `pathlib.Path` для работы с путями, что является хорошей практикой.
    - Есть обработка исключений при загрузке файла настроек.
    - Код предоставляет метаданные проекта.
-  Минусы
    - Используется `json.load` вместо `j_loads` или `j_loads_ns`.
    - Не хватает документации в формате RST.
    - Присутствуют многоточия `...`, которые следует обрабатывать.
    - Нет логирования ошибок.
    - Код излишне полагается на `try-except` вместо более конкретной обработки ошибок.

**Рекомендации по улучшению**
1. Заменить `json.load` на `j_loads` из `src.utils.jjson`.
2. Добавить комментарии в формате RST для модуля, функций и переменных.
3. Использовать `logger.error` для логирования ошибок при чтении файлов.
4. Избегать использования многоточий `...`
5. Добавить импорт `from src.utils.jjson import j_loads`
6. Добавить импорт `from src.logger.logger import logger`

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-

#! venv/bin/python/python3.12

"""
Модуль для определения корневого пути проекта и загрузки настроек.
=================================================================

Модуль определяет корневой путь проекта на основе наличия файлов-маркеров, 
а также загружает настройки из файла settings.json и README.MD.

Этот модуль предоставляет метаданные проекта.

Пример использования
--------------------

.. code-block:: python

    from src.logger.header import __root__, __project_name__, __version__
    print(f"Root directory: {__root__}")
    print(f"Project name: {__project_name__}")
    print(f"Project version: {__version__}")
"""


import sys
from pathlib import Path
from packaging.version import Version
from src.utils.jjson import j_loads # Импорт j_loads из src.utils.jjson
from src.logger.logger import logger # Импорт logger для логирования


def set_project_root(marker_files: tuple = ('pyproject.toml', 'requirements.txt', '.git')) -> Path:
    """
    Определяет корневой каталог проекта.

    Ищет корневой каталог проекта, начиная с каталога текущего файла,
    поднимаясь вверх и останавливаясь в первом каталоге, содержащем
    любой из файлов-маркеров.

    :param marker_files: Кортеж имен файлов или каталогов для определения корня проекта.
    :type marker_files: tuple
    :return: Путь к корневому каталогу, если он найден, иначе каталог, где расположен скрипт.
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


# Определяем корневую директорию проекта
__root__ = set_project_root()
"""__root__ (Path): Путь к корневой директории проекта."""

from src import gs

settings: dict = None
try:
    #  код исполняет открытие файла settings.json для чтения
    with open(gs.path.root / 'src' / 'settings.json', 'r') as settings_file:
        # код исполняет загрузку данных из JSON файла с использованием j_loads
        settings = j_loads(settings_file)
except (FileNotFoundError, Exception) as ex:
    #  Логирование ошибки если файл не найден или JSON имеет неверный формат
    logger.error(f'Ошибка загрузки файла настроек: {ex}')
    settings = {}


doc_str: str = None
try:
    #  код исполняет открытие файла README.MD для чтения
    with open(gs.path.root / 'src' / 'README.MD', 'r') as settings_file:
         # код исполняет чтение содержимого файла
        doc_str = settings_file.read()
except (FileNotFoundError, Exception) as ex:
     #  Логирование ошибки если файл не найден или ошибка чтения файла
    logger.error(f'Ошибка загрузки файла README.MD: {ex}')
    doc_str = ''



__project_name__ = settings.get("project_name", 'hypotez') if settings else 'hypotez'
"""__project_name__ (str): Имя проекта."""
__version__: str = settings.get("version", '') if settings else ''
"""__version__ (str): Версия проекта."""
__doc__: str = doc_str if doc_str else ''
"""__doc__ (str): Содержимое файла README.MD."""
__details__: str = ''
"""__details__ (str): Детали проекта."""
__author__: str = settings.get("author", '') if settings else ''
"""__author__ (str): Автор проекта."""
__copyright__: str = settings.get("copyrihgnt", '') if settings else ''
"""__copyright__ (str): Авторские права проекта."""
__cofee__: str = settings.get("cofee", "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69") if settings else "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69"
"""__cofee__ (str): Сообщение о поддержке разработчика."""
```