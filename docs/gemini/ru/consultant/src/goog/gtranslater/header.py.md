# Анализ кода модуля `header.py`

**Качество кода**
8
- Плюсы
    - Код хорошо структурирован и читаем.
    - Используется `pathlib` для работы с путями, что является хорошей практикой.
    - Наличие документации к функции `set_project_root`.
    - Установлен корневой каталог проекта.
    - Выделены основные метаданные проекта (название, версия, автор и т.д.).
- Минусы
    - Не используется `j_loads` или `j_loads_ns` для чтения JSON файлов.
    - Отсутствуют импорты для `src.logger.logger`.
    - Использование `try-except` с `...` вместо явного логирования ошибок.
    - Много пустых строк в начале файла и лишние блоки комментариев.
    - Отсутствует документация для всех переменных.
    - Не все строки в файле соответствуют стандарту PEP 8 по длине.
    - Нет описания модуля.
    - Не используются rst docstring для переменных.
    - Неполная документация для переменных.

**Рекомендации по улучшению**

1.  **Улучшение обработки JSON:**
    -   Заменить `json.load` на `j_loads` или `j_loads_ns` из `src.utils.jjson`.
2.  **Логирование ошибок:**
    -   Использовать `logger.error` из `src.logger.logger` для обработки исключений.
    -   Удалить `...` и добавить логирование.
3.  **Документирование кода:**
    -   Добавить описание модуля в начале файла.
    -   Добавить документацию в формате RST для всех переменных модуля.
    -   Использовать rst docstring.
4.  **Удаление лишнего:**
    -   Удалить лишние пустые строки и повторяющиеся комментарии.
    -   Удалить неиспользуемый импорт `sys`.
5.  **Соблюдение PEP 8:**
    -   Обеспечить длину строк не более 79 символов.
6.  **Улучшение структуры:**
    -  Импортировать logger из `src.logger.logger`.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
"""
Модуль для определения корневой директории проекта и загрузки настроек.
========================================================================

Этот модуль определяет корневую директорию проекта на основе наличия
маркерных файлов и загружает настройки из файла `settings.json`,
а также считывает документацию из `README.md`

Пример использования
--------------------

.. code-block:: python

    from src.goog.gtranslater.header import __project_name__, __version__, __doc__, __author__
    print(f"Project name: {__project_name__}")
    print(f"Version: {__version__}")
    print(f"Author: {__author__}")
    print(f"Documentation: {__doc__}")
"""
from pathlib import Path
from src.utils.jjson import j_loads
from src.logger.logger import logger
from packaging.version import Version
# from typing import Any

def set_project_root(marker_files: tuple = ('__root__', '.git')) -> Path:
    """
    Находит корневой каталог проекта, начиная с директории текущего файла,
    и двигаясь вверх, пока не будет найдена директория с одним из маркерных файлов.

    Args:
        marker_files (tuple): Кортеж имен файлов или директорий,
        которые обозначают корень проекта.

    Returns:
        Path: Путь к корневому каталогу, если он найден,
        или к директории, где расположен скрипт.
    
    Example:
        >>> from pathlib import Path
        >>> root_path = set_project_root()
        >>> print(isinstance(root_path,Path))
        True
    """
    current_path: Path = Path(__file__).resolve().parent
    root_path: Path = current_path
    for parent in [current_path] + list(current_path.parents):
        if any((parent / marker).exists() for marker in marker_files):
            root_path = parent
            break
    if str(root_path) not in sys.path:
        sys.path.insert(0, str(root_path))
    return root_path


# Получение корневой директории проекта.
__root__: Path = set_project_root()
"""Path: Путь к корневой директории проекта."""

from src import gs

settings: dict = None
"""dict: Словарь с настройками проекта."""
try:
    #  Чтение настроек из файла `settings.json`.
    with open(gs.path.root / 'src' / 'settings.json', 'r') as settings_file:
        settings = j_loads(settings_file)
except (FileNotFoundError, json.JSONDecodeError) as e:
    logger.error('Ошибка при чтении файла settings.json', exc_info=e)

doc_str: str = None
"""str: Строка с документацией из файла `README.md`."""
try:
    #  Чтение документации из файла `README.MD`.
    with open(gs.path.root / 'src' / 'README.MD', 'r') as settings_file:
        doc_str = settings_file.read()
except (FileNotFoundError, Exception) as e:
    logger.error('Ошибка при чтении файла README.MD', exc_info=e)

# Получение метаданных проекта из настроек или значения по умолчанию.
__project_name__: str = settings.get('project_name', 'hypotez') if settings else 'hypotez'
"""str: Название проекта."""
__version__: str = settings.get('version', '') if settings else ''
"""str: Версия проекта."""
__doc__: str = doc_str if doc_str else ''
"""str: Документация проекта."""
__details__: str = ''
"""str: Детали проекта."""
__author__: str = settings.get('author', '') if settings else ''
"""str: Автор проекта."""
__copyright__: str = settings.get('copyrihgnt', '') if settings else ''
"""str: Копирайт проекта."""
__cofee__: str = settings.get(
    'cofee',
    'Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69'
) if settings else 'Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69'
"""str: Сообщение для доната разработчику."""
```