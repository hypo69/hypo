# Анализ кода модуля header.py

**Качество кода**
6
- Плюсы
    - Код выполняет поставленную задачу по определению корневого каталога проекта и загрузке настроек из `settings.json`.
    - Используется `pathlib.Path` для работы с путями, что является хорошей практикой.
    - Присутствует обработка исключений при открытии и чтении файлов настроек.
    - Код структурирован и легко читается.
- Минусы
    - Не используются `j_loads` или `j_loads_ns` для загрузки `json` файлов.
    - Присутствуют `try-except` блоки с `...`, что не является лучшей практикой для обработки ошибок.
    - Отсутствует RST-документация для модуля, функций и переменных.
    - Некоторые переменные и константы, такие как `MODE`, не документированы.
    - Использование магических строк в `marker_files` и при открытии `settings.json` и `README.MD` .

**Рекомендации по улучшению**

1.  **Использовать `j_loads`**: Замените `json.load` на `j_loads` для чтения JSON-файлов.
2.  **Логирование ошибок**: Замените `...` в `try-except` блоках на логирование ошибок с помощью `logger.error`.
3.  **RST-документация**: Добавьте подробную документацию в формате RST для модуля, функций и переменных.
4.  **Улучшить обработку настроек**: Обеспечьте более надежную загрузку настроек и обработку их отсутствия.
5.  **Переменные окружения**:  Рассмотреть возможность загрузки некоторых настроек из переменных окружения, что повысит гибкость конфигурации.
6.  **Константы**: Определить константы для строк  `settings.json` и `README.MD`
7. **Форматирование**: Использовать f-строки для форматирования строк.

**Оптимизированный код**
```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
Модуль для определения корневого пути проекта и загрузки настроек.
=========================================================================================

Этот модуль определяет корневой путь проекта на основе наличия маркерных файлов, таких как
'pyproject.toml', 'requirements.txt' и '.git'. Он также загружает настройки из файла 'settings.json'
и устанавливает основные переменные проекта.

Пример использования:
--------------------

.. code-block:: python

    from src.logger import header

    print(header.__root__)
    print(header.__project_name__)
"""

MODE = 'dev'
"""str: Режим работы приложения. Возможные значения: 'dev', 'prod'. """

import sys
from pathlib import Path
#  Импортирует j_loads из модуля src.utils.jjson для загрузки json файлов
from src.utils.jjson import j_loads
#  Импортирует логер для обработки ошибок
from src.logger.logger import logger
from packaging.version import Version

SETTINGS_FILE = 'settings.json'
"""str: Имя файла с настройками."""
README_FILE = 'README.MD'
"""str: Имя файла с документацией."""


def set_project_root(marker_files: tuple = ('pyproject.toml', 'requirements.txt', '.git')) -> Path:
    """
    Определяет корневой каталог проекта.

    Поиск начинается с каталога, где расположен этот файл, и продвигается вверх
    по дереву каталогов до тех пор, пока не будет найден каталог, содержащий хотя бы один из
    маркерных файлов.

    :param marker_files: Список файлов или каталогов, наличие которых означает корень проекта.
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

# Получает корневой каталог проекта
__root__ = set_project_root()
"""Path: Путь к корневому каталогу проекта."""

from src import gs

settings: dict = None
"""dict: Словарь с настройками проекта."""
try:
    #  Код открывает файл настроек 'settings.json', читает и загружает его содержимое, используя j_loads
    with open(gs.path.root / 'src' / SETTINGS_FILE, 'r') as settings_file:
        settings = j_loads(settings_file)
except (FileNotFoundError, ValueError) as ex:
    #  Если возникает ошибка при открытии или чтении файла настроек, то она логируется и переменная `settings` остается `None`
    logger.error(f'Ошибка при загрузке файла настроек {SETTINGS_FILE}: {ex}')
    

doc_str: str = None
"""str: Строка с документацией проекта."""
try:
    #  Код открывает файл 'README.MD', читает и сохраняет его содержимое
    with open(gs.path.root / 'src' / README_FILE, 'r') as readme_file:
        doc_str = readme_file.read()
except (FileNotFoundError, ValueError) as ex:
    #  Если возникает ошибка при открытии или чтении файла 'README.MD', то она логируется и переменная `doc_str` остается `None`
    logger.error(f'Ошибка при загрузке файла документации {README_FILE}: {ex}')


__project_name__ = settings.get("project_name", 'hypotez') if settings else 'hypotez'
"""str: Название проекта."""
__version__: str = settings.get("version", '') if settings else ''
"""str: Версия проекта."""
__doc__: str = doc_str if doc_str else ''
"""str: Строка с документацией проекта."""
__details__: str = ''
"""str: Дополнительная информация о проекте."""
__author__: str = settings.get("author", '') if settings else ''
"""str: Автор проекта."""
__copyright__: str = settings.get("copyrihgnt", '') if settings else ''
"""str: Информация об авторских правах."""
__cofee__: str = settings.get("cofee", "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69") if settings else "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69"
"""str: Сообщение с призывом поддержать разработчика."""
```