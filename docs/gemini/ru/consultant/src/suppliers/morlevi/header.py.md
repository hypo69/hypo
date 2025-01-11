# Анализ кода модуля `header.py`

**Качество кода**

- **Соответствие требованиям по оформлению кода: 7/10**
    - **Плюсы:**
        - Присутствует определение `__root__` для корневой директории проекта.
        - Используется `pathlib` для работы с путями.
        - Есть обработка ошибок при чтении файлов настроек.
    - **Минусы:**
        - Не все строки кода соответствуют стилю PEP8 (например, лишние пробелы).
        - Используется стандартный `json.load` вместо `j_loads` или `j_loads_ns`.
        - Отсутствует импорт `logger` из `src.logger`.
        - Не все функции и переменные имеют docstring.
        - Обработка исключений использует `...` вместо логирования ошибок.
        - Смешивание стилей кавычек в строках.
        - Использование `sys.path.insert(0, str(__root__))` может привести к проблемам с импортами.

**Рекомендации по улучшению**

1.  **Импорты:**
    - Добавить `from src.utils.jjson import j_loads` для чтения JSON.
    - Добавить `from src.logger import logger` для логирования.
2.  **Использование `j_loads`:**
    - Заменить `json.load` на `j_loads` для чтения JSON файлов.
3.  **Логирование ошибок:**
    - Заменить `...` в блоках `except` на `logger.error(f'Сообщение об ошибке: {ex}')`.
4.  **Документация:**
    - Добавить docstring для переменных `__project_name__`, `__version__`, `__doc__`, `__details__`, `__author__`, `__copyright__`, `__cofee__`.
5.  **Форматирование кода:**
    - Привести код в соответствие с PEP8, убрать лишние пробелы и выравнивания.
6.  **Стиль кавычек:**
    - Использовать одинарные кавычки в коде Python, двойные только в операциях вывода.
7.  **Удаление лишних комментариев:**
    - Удалить неинформативные комментарии.
8.  **`sys.path.insert`:**
    - Рассмотреть альтернативные способы настройки путей, чтобы избежать проблем с импортами.

**Оптимизированный код**

```python
"""
Модуль для определения корневой директории проекта и загрузки настроек.
=========================================================================================

Этот модуль содержит функции и переменные, используемые для определения
корневой директории проекта, загрузки настроек из файла `settings.json`
и получения описания из файла `README.MD`.

Пример использования
--------------------

.. code-block:: python

    from src.suppliers.morlevi.header import __project_name__, __version__, __doc__, __author__

    print(f"Project Name: {__project_name__}")
    print(f"Version: {__version__}")
    print(f"Author: {__author__}")
"""

import sys
from pathlib import Path
from packaging.version import Version

from src.utils.jjson import j_loads
from src.logger import logger
from src import gs


def set_project_root(marker_files: tuple[str, ...] = ('__root__', '.git')) -> Path:
    """
    Определяет корневую директорию проекта, начиная с директории текущего файла.

    Поиск идет вверх по иерархии директорий и останавливается на первой директории,
    содержащей любой из файлов-маркеров.

    Args:
        marker_files (tuple): Кортеж с именами файлов или директорий, которые идентифицируют корень проекта.

    Returns:
        Path: Путь к корневой директории, если она найдена, иначе директория, где расположен скрипт.
    """
    __root__: Path
    current_path: Path = Path(__file__).resolve().parent
    __root__ = current_path
    for parent in [current_path] + list(current_path.parents):
        if any((parent / marker).exists() for marker in marker_files):
            __root__ = parent
            break
    if str(__root__) not in sys.path:
        sys.path.insert(0, str(__root__))
    return __root__


# Код исполняет определение корневой директории проекта
__root__: Path = set_project_root()
"""__root__ (Path): Путь к корневой директории проекта."""

settings: dict | None = None
try:
    # Код исполняет чтение настроек из файла settings.json
    with open(gs.path.root / 'src' / 'settings.json', 'r') as settings_file:
        settings = j_loads(settings_file)
except (FileNotFoundError, json.JSONDecodeError) as ex:
    # Код логирует ошибку, если файл не найден или не может быть декодирован
    logger.error(f'Ошибка чтения файла настроек: {ex}')

doc_str: str | None = None
try:
    # Код исполняет чтение содержимого файла README.MD
    with open(gs.path.root / 'src' / 'README.MD', 'r') as settings_file:
        doc_str = settings_file.read()
except (FileNotFoundError, json.JSONDecodeError) as ex:
    # Код логирует ошибку, если файл не найден или не может быть прочитан
    logger.error(f'Ошибка чтения файла README.MD: {ex}')

# Код исполняет получение значений настроек проекта, если они существуют
__project_name__: str = settings.get('project_name', 'hypotez') if settings else 'hypotez'
"""__project_name__ (str): Наименование проекта."""
__version__: str = settings.get('version', '') if settings else ''
"""__version__ (str): Версия проекта."""
__doc__: str = doc_str if doc_str else ''
"""__doc__ (str): Описание проекта."""
__details__: str = ''
"""__details__ (str): Дополнительные детали проекта."""
__author__: str = settings.get('author', '') if settings else ''
"""__author__ (str): Автор проекта."""
__copyright__: str = settings.get('copyrihgnt', '') if settings else ''
"""__copyright__ (str): Информация об авторских правах."""
__cofee__: str = settings.get('cofee', 'Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69') if settings else 'Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69'
"""__cofee__ (str): Сообщение с призывом поддержать разработчика."""
```