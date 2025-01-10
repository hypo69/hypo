# Анализ кода модуля header.py

**Качество кода**
8
- Плюсы
    - Код выполняет задачу определения корневой директории проекта и загрузки настроек.
    - Присутствуют базовые проверки на наличие файлов и корректность JSON.
    - Используется `pathlib` для работы с путями, что является хорошей практикой.
- Минусы
    -  Не используется `j_loads` для чтения `json`
    -  Используются  `try-except` без логирования ошибок.
    -  Отсутствует документация в формате RST.
    -  Не используется logger.
    -  Не все переменные имею type hints

**Рекомендации по улучшению**
1.  Использовать `j_loads_ns` из `src.utils.jjson` для загрузки `settings.json`.
2.  Использовать `logger.error` для логирования ошибок.
3.  Добавить `docstring` для модуля, функций и переменных в формате RST.
4.  Добавить type hints для переменных.
5.  Убрать лишние комментарии.
6.  Добавить импорт logger из `src.logger`.
7.  Использовать константы для строк, такие как  `'src'`, `'settings.json'`, `'README.MD'`

**Оптимизированный код**
```python
# -*- coding: utf-8 -*-
"""
Модуль для настройки окружения и получения метаданных проекта.
=================================================================

Этот модуль выполняет поиск корневой директории проекта, загрузку
настроек из файла settings.json и документации из README.MD.

Пример использования
--------------------

.. code-block:: python

    from src.ai.dialogflow.header import __project_name__, __version__, __doc__, __author__, __copyright__

    print(f"Имя проекта: {__project_name__}")
    print(f"Версия: {__version__}")
    print(f"Автор: {__author__}")

"""
import sys
from pathlib import Path
from packaging.version import Version
from typing import Tuple, Dict, Optional

from src.utils.jjson import j_loads_ns #  Импортируем j_loads_ns из src.utils.jjson
from src.logger import logger #  Импортируем logger из src.logger
from src import gs

# Константы для строк
SRC_DIR = 'src'
SETTINGS_FILE = 'settings.json'
README_FILE = 'README.MD'


def set_project_root(marker_files: Tuple[str, ...] = ('__root__', '.git')) -> Path:
    """
    Определение корневой директории проекта.

    Функция ищет корневую директорию проекта, начиная с директории текущего файла.
    Поиск идет вверх по дереву директорий до первой директории, содержащей один из маркеров.

    Args:
        marker_files (tuple): Кортеж имен файлов или директорий, по которым определяется корень проекта.

    Returns:
        Path: Путь к корневой директории проекта.
    """
    current_path: Path = Path(__file__).resolve().parent
    root: Path = current_path
    for parent in [current_path] + list(current_path.parents):
        if any((parent / marker).exists() for marker in marker_files):
            root = parent
            break
    if root not in sys.path:
        sys.path.insert(0, str(root))
    return root


# Вызов функции для определения корневой директории проекта
__root__: Path = set_project_root()
"""Path: Путь к корневой директории проекта"""

settings: Optional[Dict] = None
try:
    # Чтение файла настроек с использованием j_loads_ns
    settings = j_loads_ns(gs.path.root / SRC_DIR / SETTINGS_FILE)
except (FileNotFoundError, json.JSONDecodeError) as e:
    # Логирование ошибки при чтении файла настроек
    logger.error(f'Ошибка при загрузке файла настроек {gs.path.root / SRC_DIR / SETTINGS_FILE}', exc_info=e)
    ...

doc_str: Optional[str] = None
try:
    # Чтение файла README.MD
    with open(gs.path.root / SRC_DIR / README_FILE, 'r', encoding='utf-8') as doc_file:
        doc_str = doc_file.read()
except (FileNotFoundError,  UnicodeDecodeError) as e:
     # Логирование ошибки при чтении файла документации
    logger.error(f'Ошибка при загрузке файла документации {gs.path.root / SRC_DIR / README_FILE}', exc_info=e)
    ...

__project_name__: str = settings.get("project_name", 'hypotez') if settings else 'hypotez'
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
"""str: Авторские права."""
__cofee__: str = settings.get("cofee", "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69") if settings else "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69"
"""str: Призыв к поддержке разработчика."""
```