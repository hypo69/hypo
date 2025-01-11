# Анализ кода модуля `header.py`

**Качество кода**
8
-  Плюсы
    - Код выполняет свою основную задачу - определение корневого каталога проекта и загрузку настроек.
    - Присутствует базовая документация для функций.
    - Используются константы `marker_files` для определения корня проекта.
    - Проектные настройки и документация загружаются из файлов.
-  Минусы
    - Использование `json.load` вместо `j_loads` или `j_loads_ns`.
    - Отсутствует обработка ошибок с помощью `logger.error`.
    - Не используются f-строки для форматирования.
    - Отсутствуют комментарии перед блоками кода.
    - Неполная документация для переменных модуля.
    - `...` как точки остановки не информативны.
    - Не приведены примеры использования.
    - Использование `header` в импорте не имеет смысла, так как это текущий файл.
    - Нет описания модуля в начале файла.

**Рекомендации по улучшению**

1.  Добавить описание модуля в начале файла.
2.  Использовать `j_loads` из `src.utils.jjson` вместо стандартного `json.load` для чтения файлов.
3.  Заменить блоки `try-except` на использование `logger.error` для обработки ошибок.
4.  Добавить комментарии перед каждым блоком кода.
5.  Добавить документацию для каждой переменной модуля.
6.  Использовать `f-strings` для форматирования строк.
7.  Удалить неиспользуемый импорт `header`.
8.  Добавить примеры использования в документацию.
9.  Заменить точки остановки на более информативные.
10. Привести в соответствие имена переменных и импортов с ранее обработанными файлами.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
"""
Модуль для определения корневого каталога проекта и загрузки основных настроек.
=========================================================================================

Этот модуль определяет корневой каталог проекта, выполняя поиск вверх по иерархии директорий
до тех пор, пока не будет найден один из маркерных файлов. Также загружает настройки проекта
из `settings.json` и документацию из `README.MD`.

Пример использования
--------------------

Пример определения корневого каталога и загрузки настроек:

.. code-block:: python

    from src.logger.header import __root__, __project_name__, __version__

    print(f"Корневой каталог проекта: {__root__}")
    print(f"Имя проекта: {__project_name__}")
    print(f"Версия проекта: {__version__}")
"""

import sys
from pathlib import Path
from packaging.version import Version
from src.utils.jjson import j_loads
from src.logger.logger import logger # исправлен импорт logger
from src import gs

# Функция для поиска корневой директории проекта
def set_project_root(marker_files: tuple = ('__root__', '.git')) -> Path:
    """
    Ищет корневой каталог проекта, начиная с директории текущего файла,
    двигаясь вверх и останавливаясь на первой директории, содержащей любой из маркерных файлов.

    Args:
        marker_files (tuple): Имена файлов или директорий для идентификации корня проекта.

    Returns:
        Path: Путь к корневому каталогу, если найден, иначе - директория, где расположен скрипт.
    
    Example:
    
        >>> set_project_root()
        PosixPath('/home/user/project')
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

# Получение корневого каталога проекта
__root__: Path = set_project_root()
"""__root__ (Path): Путь к корневому каталогу проекта."""


settings: dict | None = None
#  Загрузка настроек из файла settings.json
try:
    with open(gs.path.root / 'src' / 'settings.json', 'r') as settings_file:
        settings = j_loads(settings_file)
except (FileNotFoundError, Exception) as ex:
    logger.error(f'Ошибка при загрузке файла настроек: {ex}')
    settings = {}  # Инициализация settings пустым словарем в случае ошибки

doc_str: str | None = None
# Загрузка документации из файла README.MD
try:
    with open(gs.path.root / 'src' / 'README.MD', 'r') as doc_file:
        doc_str = doc_file.read()
except (FileNotFoundError, Exception) as ex:
    logger.error(f'Ошибка при загрузке файла документации: {ex}')
    doc_str = '' # Инициализация doc_str пустой строкой в случае ошибки
# Определение имени проекта, версии, документации и прочих параметров
__project_name__: str = settings.get('project_name', 'hypotez') if settings else 'hypotez'
"""__project_name__ (str): Имя проекта."""

__version__: str = settings.get('version', '') if settings else ''
"""__version__ (str): Версия проекта."""

__doc__: str = doc_str if doc_str else ''
"""__doc__ (str): Строка документации проекта."""

__details__: str = ''
"""__details__ (str): Детали проекта (не используется)."""

__author__: str = settings.get('author', '') if settings else ''
"""__author__ (str): Автор проекта."""

__copyright__: str = settings.get('copyrihgnt', '') if settings else ''
"""__copyright__ (str): Авторские права проекта."""

__cofee__: str = settings.get('cofee', 'Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69') if settings else 'Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69'
"""__cofee__ (str): Сообщение с предложением поддержать разработчика."""
```