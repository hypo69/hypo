# Анализ кода модуля `header.py`

**Качество кода**
1/10
 - Плюсы
   -  Код содержит функцию `set_project_root` для определения корневой директории проекта.
   -  Используется `pathlib` для работы с путями.
 - Минусы
    -  Множество пустых docstring, не соответствующих reStructuredText.
    -  Используется стандартный `json.load` вместо `j_loads` из `src.utils.jjson`.
    -  Отсутствует импорт `logger` из `src.logger.logger`.
    -  Избыточные блоки `try-except` с `...` вместо обработки ошибок через `logger.error`.
    -  Непоследовательное использование docstring и комментариев.
    -  Переменные `doc_str` и `settings` не имеют аннотации типов.
    -  Код содержит много повторяющихся комментариев.

**Рекомендации по улучшению**

1.  **Улучшить docstring**:
    - Переписать docstring в формате reStructuredText (RST).
    - Добавить описание модуля, функций и переменных, а также примеры использования.
2.  **Использовать `j_loads`**:
    - Заменить `json.load` на `j_loads` из `src.utils.jjson` для чтения файлов.
3.  **Импортировать `logger`**:
    - Добавить импорт `from src.logger.logger import logger` для логирования ошибок.
4.  **Обрабатывать ошибки**:
    - Заменить `...` в блоках `try-except` на логирование ошибок с помощью `logger.error`.
    - Убрать лишние блоки `try-except` и `...`.
5.  **Аннотировать переменные**:
    - Добавить аннотацию типов к переменным `doc_str` и `settings`.
6.  **Улучшить консистентность**
    - Избавиться от дубликатов комментариев в начале файла.
    - Удалить неиспользуемые или неинформативные комментарии.
7.  **Упростить логику**:
    - Упростить логику `if settings else '...'` , добавив значения по умолчанию непосредственно при вызове `settings.get()`.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
Модуль для определения настроек проекта и получения метаданных.
================================================================

Этот модуль содержит функции и переменные, необходимые для настройки окружения,
определения корневой директории проекта, загрузки настроек из файла и получения
метаданных проекта.

Пример использования
--------------------

Пример использования функции `set_project_root`:

.. code-block:: python

    root_path = set_project_root()
    print(f"Root directory of project: {root_path}")

Пример использования переменных с метаданными:

.. code-block:: python

   print(f"Project name: {__project_name__}")
   print(f"Version: {__version__}")
"""
import sys
from pathlib import Path
from typing import Tuple, Dict, Optional

from src.utils.jjson import j_loads
from src.logger.logger import logger
from packaging.version import Version

MODE = 'dev'
"""str: Режим работы приложения (по умолчанию 'dev')."""

def set_project_root(marker_files: Tuple[str, ...] = ('pyproject.toml', 'requirements.txt', '.git')) -> Path:
    """
    Находит корневой каталог проекта, начиная с каталога текущего файла,
    двигаясь вверх по иерархии каталогов. Поиск прекращается при обнаружении
    каталога, содержащего один из файлов-маркеров.

    :param marker_files: Кортеж имен файлов или каталогов, используемых для идентификации корня проекта.
    :type marker_files: Tuple[str, ...]
    :return: Путь к корневому каталогу. Если корень не найден, возвращается каталог, где находится скрипт.
    :rtype: Path
    """
    current_path: Path = Path(__file__).resolve().parent
    root_path: Path = current_path
    for parent in [current_path] + list(current_path.parents):
        if any((parent / marker).exists() for marker in marker_files):
            root_path = parent
            break
    if root_path not in sys.path:
        sys.path.insert(0, str(root_path))
    return root_path


# Код устанавливает корневую директорию проекта
__root__: Path = set_project_root()
"""Path: Путь к корневой директории проекта."""

from src import gs

settings: Optional[Dict] = None
"""Optional[Dict]: Словарь настроек проекта, загруженных из `settings.json`."""
try:
    # Код исполняет чтение настроек из файла `settings.json`
    settings = j_loads(gs.path.root / 'src' /  'settings.json')
except (FileNotFoundError, Exception) as ex:
    logger.error(f'Ошибка при загрузке settings.json: {ex}')

doc_str: Optional[str] = None
"""Optional[str]: Строка документации проекта, загруженная из `README.MD`."""
try:
    # Код исполняет чтение документации из файла `README.MD`
    with open(gs.path.root / 'src' /  'README.MD', 'r', encoding='utf-8') as settings_file:
        doc_str = settings_file.read()
except (FileNotFoundError, Exception) as ex:
    logger.error(f'Ошибка при загрузке README.MD: {ex}')

__project_name__: str = settings.get("project_name", 'hypotez') if settings else 'hypotez'
"""str: Название проекта."""
__version__: str = settings.get("version", '') if settings else ''
"""str: Версия проекта."""
__doc__: str = doc_str if doc_str else ''
"""str: Документация проекта."""
__details__: str = ''
"""str: Детали проекта (в настоящее время пустая строка)."""
__author__: str = settings.get("author", '') if settings else ''
"""str: Автор проекта."""
__copyright__: str = settings.get("copyrihgnt", '') if settings else ''
"""str: Авторские права проекта."""
__cofee__: str = settings.get("cofee", "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69")  if settings else "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69"
"""str: Сообщение о поддержке разработчика."""
```