# Анализ кода модуля `header.py`

**Качество кода**
**Соответствие требованиям по оформлению кода: 7/10**

-   **Плюсы:**
    *   Код структурирован и разделен на логические блоки.
    *   Используется `pathlib` для работы с путями.
    *   Есть функция `set_project_root` для определения корня проекта.
    *   Присутствует обработка исключений при чтении файлов.
    *   Используется переменная `__root__` для хранения пути к корневому каталогу проекта.
-   **Минусы:**
    *   Отсутствует docstring для модуля.
    *   Используется стандартный `json.load` вместо `j_loads` или `j_loads_ns`.
    *   Не все переменные имеют аннотации типов.
    *   Не все функции и переменные имеют документацию в стиле RST.
    *   Много пустых docstring комментариев.
    *   Стандартные `try-except` блоки используются вместо логирования ошибок через `logger`.
    *   Не используется `from src.logger.logger import logger` для логирования.
    *   Присутствуют неиспользуемые импорты.
    *   Имена переменных не всегда соответствуют PEP8 (например `doc_str`).

**Рекомендации по улучшению**

1.  **Документация модуля:** Добавить docstring в начало файла с описанием модуля, его назначения и примером использования.
2.  **Импорт `j_loads`:** Заменить `json.load` на `j_loads` или `j_loads_ns` из `src.utils.jjson`.
3.  **Документация функций:** Добавить docstring в стиле RST для функции `set_project_root`.
4.  **Использование `logger`:**  Заменить `try-except` блоки на логирование ошибок с помощью `logger.error` из `src.logger.logger`.
5.  **Переменные окружения:** Рассмотреть использование переменных окружения для конфигурации вместо `settings.json`.
6. **Удалить неиспользуемые импорты:** Удалить импорт `sys`.
7.  **Имена переменных:** Привести имена переменных в соответствие со стандартами PEP8 (например, `doc_str` -> `doc_string`).
8.  **Аннотации типов:** Добавить аннотации типов для переменных, где это возможно.
9. **Улучшить docstring:** Добавить документацию для всех переменных модуля.
10. **Удалить пустые docstring:** Удалить пустые docstring, не несущие смысловой нагрузки.

**Оптимизированный код**

```python
"""
Модуль для настройки окружения и загрузки конфигурации проекта.
================================================================

Этот модуль содержит функции для определения корневой директории проекта, загрузки настроек из файла `settings.json`
и инициализации глобальных переменных проекта, таких как имя, версия, автор и т.д.

Пример использования
--------------------

.. code-block:: python

   from src.suppliers.chat_gpt.scenarios.header import __project_name__, __version__, __doc__, __author__

   print(f"Project name: {__project_name__}")
   print(f"Version: {__version__}")
   print(f"Author: {__author__}")
   print(f"Documentation: {__doc__}")
"""
import json
from pathlib import Path
from packaging.version import Version

from src.utils.jjson import j_loads
from src.logger.logger import logger
from src import gs


def set_project_root(marker_files: tuple = ('__root__', '.git')) -> Path:
    """
    Определяет корневой каталог проекта, начиная с директории текущего файла,
    двигаясь вверх и останавливаясь на первой директории, содержащей любой из маркеров.

    Args:
        marker_files (tuple): Имена файлов или директорий для идентификации корня проекта.

    Returns:
        Path: Путь к корневой директории, если найден, иначе - директория, где расположен скрипт.

    Example:
        >>> from pathlib import Path
        >>> root = set_project_root(marker_files=('__root__', '.git'))
        >>> print(isinstance(root, Path))
        True
    """
    current_path: Path = Path(__file__).resolve().parent
    root: Path = current_path

    for parent in [current_path] + list(current_path.parents):
        if any((parent / marker).exists() for marker in marker_files):
            root = parent
            break
    if str(root) not in gs.sys_path:
        gs.sys_path.insert(0, str(root))
    return root


# Получение корневой директории проекта
__root__: Path = set_project_root()
"""__root__ (Path): Путь к корневой директории проекта."""


settings: dict | None = None
try:
    # код исполняет загрузку настроек из файла settings.json
    with open(gs.path.root / 'src' / 'settings.json', 'r') as settings_file:
        settings = j_loads(settings_file)
except (FileNotFoundError, json.JSONDecodeError) as ex:
    # Логирование ошибки, если файл не найден или не является валидным JSON
    logger.error('Ошибка при загрузке settings.json', exc_info=ex)
    ...

doc_string: str | None = None
try:
    # код исполняет загрузку документации из файла README.MD
    with open(gs.path.root / 'src' / 'README.MD', 'r') as doc_file:
        doc_string = doc_file.read()
except (FileNotFoundError, json.JSONDecodeError) as ex:
    # Логирование ошибки, если файл не найден или не может быть прочитан
    logger.error('Ошибка при загрузке README.MD', exc_info=ex)
    ...

__project_name__: str = settings.get('project_name', 'hypotez') if settings else 'hypotez'
"""__project_name__ (str): Название проекта."""
__version__: str = settings.get('version', '') if settings else ''
"""__version__ (str): Версия проекта."""
__doc__: str = doc_string if doc_string else ''
"""__doc__ (str): Документация проекта."""
__details__: str = ''
"""__details__ (str): Детали проекта."""
__author__: str = settings.get('author', '') if settings else ''
"""__author__ (str): Автор проекта."""
__copyright__: str = settings.get('copyrihgnt', '') if settings else ''
"""__copyright__ (str): Авторское право проекта."""
__cofee__: str = settings.get(
    'cofee', 'Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69'
) if settings else 'Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69'
"""__cofee__ (str): Сообщение о возможности угостить разработчика кофе."""
```