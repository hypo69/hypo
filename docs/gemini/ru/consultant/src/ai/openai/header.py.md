# Анализ кода модуля `header.py`

**Качество кода**
8
- Плюсы
    - Код хорошо структурирован и имеет четкую логику.
    - Используется `pathlib` для работы с путями, что является хорошей практикой.
    - Присутствует обработка ошибок при чтении файлов.
    - Добавлены docstring для функций и модуля.
    - Определены основные метаданные проекта (имя, версия, автор и т.д.) из `settings.json`.
- Минусы
    - Используется `json.load` вместо `j_loads` или `j_loads_ns` из `src.utils.jjson`.
    - Отсутствует импорт `logger` из `src.logger`.
    - Избыточное использование `try-except` с многоточием `...` вместо `logger.error`.
    - Дублирование `if settings else 'default'` можно упростить.
    - Нет проверки на наличие ключей в словаре settings перед тем как к ним обращаться

**Рекомендации по улучшению**

1.  Использовать `j_loads_ns` из `src.utils.jjson` вместо `json.load`.
2.  Импортировать `logger` из `src.logger.logger`.
3.  Заменить `try-except` на проверку существования файла и `logger.error`.
4.  Добавить проверку на существование ключей в словаре `settings` для предотвращения ошибок.
5.  Упростить получение метаданных проекта, используя `settings.get` с дефолтными значениями.
6.  Документировать переменные на уровне модуля в формате reStructuredText (RST).
7.  Добавить обработку ошибок при чтении файлов README.MD

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
#! venv/bin/python/python3.12
"""
Модуль для определения корневого пути проекта и загрузки настроек.
=================================================================

Этот модуль определяет корневой каталог проекта и загружает настройки из файла `settings.json`.
Все импорты должны строиться относительно этого корневого пути.

:TODO: В дальнейшем перенести в системную переменную

Пример использования
--------------------

Пример получения корневой директории:

.. code-block:: python

    from src.logger.header import __root__
    print(__root__)

"""

import sys
from pathlib import Path
from packaging.version import Version

from src.utils.jjson import j_loads_ns
from src.logger.logger import logger


def set_project_root(marker_files: tuple = ('__root__', '.git')) -> Path:
    """
    Определяет корневую директорию проекта.

    Сканирует вверх по дереву каталогов от текущего файла, пока не найдет каталог, содержащий один из файлов-маркеров.

    Args:
        marker_files (tuple): Кортеж имен файлов или каталогов, обозначающих корень проекта.

    Returns:
        Path: Путь к корневой директории проекта.

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
"""Path: Путь к корневой директории проекта."""

from src import gs

settings: dict = {}
"""dict: Словарь с настройками проекта."""
# Загружает настройки из файла settings.json
try:
    # код исполняет загрузку настроек из файла `settings.json`
    with open(gs.path.root / 'src' / 'settings.json', 'r') as settings_file:
        settings = j_loads_ns(settings_file)
except FileNotFoundError:
    logger.error(f"Файл настроек не найден: {gs.path.root / 'src' / 'settings.json'}")
except Exception as e:
    logger.error(f"Ошибка при загрузке настроек из файла: {e}")


doc_str: str = ''
"""str: Строка с документацией из файла README.MD."""
# Загружает документацию из файла README.MD
try:
    # Код загружает документацию из файла README.MD
    with open(gs.path.root / 'src' / 'README.MD', 'r') as settings_file:
        doc_str = settings_file.read()
except FileNotFoundError:
    logger.error(f"Файл README.MD не найден: {gs.path.root / 'src' / 'README.MD'}")
except Exception as e:
     logger.error(f"Ошибка при загрузке документации из файла: {e}")



# Получаем метаданные проекта из настроек или устанавливаем значения по умолчанию
__project_name__: str = settings.get('project_name', 'hypotez')
"""str: Имя проекта."""
__version__: str = settings.get('version', '')
"""str: Версия проекта."""
__doc__: str = doc_str if doc_str else ''
"""str: Документация проекта."""
__details__: str = ''
"""str: Детали проекта."""
__author__: str = settings.get('author', '')
"""str: Автор проекта."""
__copyright__: str = settings.get('copyrihgnt', '')
"""str: Информация об авторских правах."""
__cofee__: str = settings.get('cofee', "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69")
"""str: Призыв поддержать разработчика."""
```