# Анализ кода модуля `header.py`

**Качество кода**
7
- Плюсы
    - Код выполняет основную функцию: определяет корневой каталог проекта и загружает настройки.
    - Используются `pathlib` для работы с путями, что делает код более читаемым и кроссплатформенным.
    - Присутствует базовая обработка исключений для случаев, когда файл настроек или README не найдены.
    - В начале файла есть описание модуля.
- Минусы
    - Не используются `j_loads` или `j_loads_ns` из `src.utils.jjson` для чтения файлов.
    - Не хватает документации в формате RST для функций и переменных.
    - Не используются логирование через `logger` из `src.logger.logger`.
    - Используется избыточное `try-except` для обработки ошибок чтения файлов, вместо логгирования через `logger.error`.
    - В некоторых местах пропущены комментарии.
    - Желательно вынести константы с дефолтными значениями в отдельные переменные
    - Некоторые переменные не аннотированы, например `settings`.
    - Не везде используется `str` для приведения типов, где это требуется.

**Рекомендации по улучшению**

1.  **Импорты:** Добавить необходимые импорты, такие как `from src.utils.jjson import j_loads` и `from src.logger import logger`.
2.  **Использование `j_loads`:** Заменить `json.load` на `j_loads` для загрузки JSON файлов.
3.  **Логирование ошибок:** Заменить `try-except` на логирование с помощью `logger.error` при возникновении ошибок чтения файлов.
4.  **Документация:** Добавить документацию в формате RST для функций, переменных, включая описание модуля.
5.  **Комментарии:** Добавить комментарии для всех блоков кода.
6. **Константы:** Вынести дефолтные значения в константы.
7. **Аннотации:** Добавить аннотации для переменных.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
#! venv/bin/python/python3.12
"""
Модуль для определения корневого каталога проекта и загрузки основных настроек.
=========================================================================================

Этот модуль содержит функции и переменные для определения корневого каталога проекта,
загрузки настроек из `settings.json` и `README.MD`, а также для установки глобальных переменных проекта.

Пример использования
--------------------

Пример инициализации переменных проекта:

.. code-block:: python

    from src.webdriver.chrome import header
    print(header.__project_name__)
    print(header.__version__)
"""
import sys
from pathlib import Path
from typing import Dict
from packaging.version import Version

from src.utils.jjson import j_loads # Импорт j_loads для загрузки JSON
from src.logger import logger  # Импорт logger для логирования ошибок


DEFAULT_PROJECT_NAME = 'hypotez'
DEFAULT_VERSION = ''
DEFAULT_COFEE = "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69"
DEFAULT_AUTHOR = ''
DEFAULT_COPYRIGHT = ''


def set_project_root(marker_files: tuple = ('__root__', '.git')) -> Path:
    """
    Находит корневой каталог проекта, начиная с каталога текущего файла,
    идя вверх по иерархии каталогов и останавливаясь на первом каталоге,
    содержащем любой из файлов-маркеров.

    Args:
        marker_files (tuple, optional): Имена файлов или каталогов для идентификации корня проекта.
            По умолчанию: ('__root__', '.git').

    Returns:
        Path: Путь к корневому каталогу, если он найден, иначе - путь к каталогу, где находится скрипт.

    Example:
        >>> set_project_root()
        ...
    """
    __root__: Path
    current_path: Path = Path(__file__).resolve().parent
    __root__ = current_path
    # Проверка наличия маркерных файлов в текущем и родительских каталогах
    for parent in [current_path] + list(current_path.parents):
        if any((parent / marker).exists() for marker in marker_files):
            __root__ = parent
            break
    # Добавляет корневой каталог в sys.path, если его там нет
    if __root__ not in sys.path:
        sys.path.insert(0, str(__root__))
    return __root__


# Получение корневого каталога проекта
__root__: Path = set_project_root()
"""Path: Путь к корневому каталогу проекта."""

from src import gs

settings: Dict | None = None
# Попытка загрузить настройки из файла settings.json
try:
    with open(gs.path.root / 'src' / 'settings.json', 'r') as settings_file:
       # Используем j_loads для загрузки JSON
        settings = j_loads(settings_file)
except (FileNotFoundError, json.JSONDecodeError) as e:
     # Логгируем ошибку, если файл не найден или JSON невалидный
    logger.error(f'Ошибка при загрузке settings.json: {e}')
    settings = None

doc_str: str | None = None
# Попытка загрузить содержимое README.MD
try:
    with open(gs.path.root / 'src' / 'README.MD', 'r') as readme_file:
        doc_str = readme_file.read()
except (FileNotFoundError, json.JSONDecodeError) as e:
    # Логгируем ошибку, если файл не найден или не читается
    logger.error(f'Ошибка при загрузке README.MD: {e}')
    doc_str = None

# Определение глобальных переменных проекта
__project_name__: str = settings.get('project_name', DEFAULT_PROJECT_NAME) if settings else DEFAULT_PROJECT_NAME
"""str: Имя проекта."""
__version__: str = settings.get('version', DEFAULT_VERSION) if settings else DEFAULT_VERSION
"""str: Версия проекта."""
__doc__: str = doc_str if doc_str else ''
"""str: Содержимое файла README.MD."""
__details__: str = ''
"""str: Дополнительная информация о проекте."""
__author__: str = settings.get('author', DEFAULT_AUTHOR) if settings else DEFAULT_AUTHOR
"""str: Автор проекта."""
__copyright__: str = settings.get('copyrihgnt', DEFAULT_COPYRIGHT) if settings else DEFAULT_COPYRIGHT
"""str: Авторское право проекта."""
__cofee__: str = settings.get("cofee", DEFAULT_COFEE) if settings else DEFAULT_COFEE
"""str: Сообщение о поддержке разработчика."""
```