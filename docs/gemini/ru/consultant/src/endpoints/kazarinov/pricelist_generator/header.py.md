# Анализ кода модуля `header.py`

**Качество кода:**

- **Соответствие стандартам**: 7/10
- **Плюсы**:
    - Код структурирован, есть определение корневой директории проекта.
    - Используются `Path` для работы с путями, что является хорошей практикой.
    - Присутствует обработка ошибок при загрузке `settings.json` и `README.MD`, хотя и с использованием `...`.
- **Минусы**:
    -  Не используется `j_loads` или `j_loads_ns` для загрузки JSON.
    - Импорт `logger` отсутствует.
    - Отсутствует документация в формате RST для модуля и функции `set_project_root`.
    - В блоках `try-except` используется `...`, что не информативно и не способствует отслеживанию ошибок.
    - Смешивание импорта стандартных библиотек и локальных.
    - Некоторые переменные не имеют аннотацию типа.
    - Загрузка документации из `README.MD`  не является частью логики `header` файла.
    -  Константы (`__project_name__`, `__version__` и т.д.) не соответствуют PEP8 (должны быть UPPER_CASE).
    -  Необходимо заменить все двойные кавычки на одинарные.

**Рекомендации по улучшению:**

1. **Импорты**:
   - Добавить импорт `logger` из `src.logger`.
   - Разделить импорты на стандартные библиотеки, сторонние и локальные.
2. **Загрузка JSON**:
   - Использовать `j_loads` или `j_loads_ns` из `src.utils.jjson` вместо `json.load`.
3. **Обработка ошибок**:
    -  Заменить `...` в блоках `try-except` на логирование ошибок с использованием `logger.error`.
4. **Документация**:
   - Добавить документацию в формате RST для модуля и функции `set_project_root`.
5. **Форматирование**:
   - Использовать `UPPER_CASE` для констант (например, `__PROJECT_NAME__`).
   - Убрать лишние пробелы.
6. **Типизация**:
   - Добавить аннотации типов для переменных `settings`, `doc_str`.
7. **Загрузка документации**:
   - Вынести логику загрузки документации из `README.MD` в отдельный модуль или функцию.
8. **Кавычки**:
   - Заменить двойные кавычки на одинарные, кроме операций вывода.
9. **Логирование**:
    -  Добавить логирование при возникновении ошибок в  `try-except` блоках.

**Оптимизированный код:**

```python
"""
Модуль для определения корневой директории проекта и загрузки настроек.
======================================================================

Модуль определяет корневую директорию проекта на основе наличия файлов-маркеров и
загружает основные настройки из `settings.json`, а также предоставляет доступ к общей документации проекта.

Пример использования
----------------------
.. code-block:: python

    from src.endpoints.kazarinov.pricelist_generator.header import (
        __PROJECT_NAME__,
        __VERSION__,
        __DOC__,
        __DETAILS__,
        __AUTHOR__,
        __COPYRIGHT__,
        __COFEE__
    )

    print(__PROJECT_NAME__)
"""

import sys
from pathlib import Path
# Third party imports
from packaging.version import Version
# Local imports
from src.utils.jjson import j_loads
from src.logger import logger
from src import gs


def set_project_root(marker_files: tuple = ('__root__', '.git')) -> Path:
    """
    Находит корневой каталог проекта, начиная с каталога текущего файла.

    Поиск идет вверх по директориям до первого каталога, содержащего любой из файлов-маркеров.

    :param marker_files: Кортеж имен файлов или каталогов для определения корня проекта.
    :type marker_files: tuple, optional
    :return: Путь к корневому каталогу, если найден, иначе - каталог, где расположен скрипт.
    :rtype: Path
    
    :Example:
        >>> set_project_root()
        PosixPath('/path/to/your/project')
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


# Get the root directory of the project
__root__: Path = set_project_root()
"""__root__ (Path): Путь к корневому каталогу проекта."""

settings: dict | None = None
try:
    with open(gs.path.root / 'src' / 'settings.json', 'r') as settings_file:
        settings = j_loads(settings_file)  # Используем j_loads
except FileNotFoundError:
    logger.error(f'Файл settings.json не найден по пути: {gs.path.root / "src" / "settings.json"}')
    settings = {}
except Exception as e:
    logger.error(f'Ошибка при загрузке settings.json: {e}')
    settings = {}


doc_str: str | None = None
try:
    with open(gs.path.root / 'src' / 'README.MD', 'r') as settings_file:
        doc_str = settings_file.read()
except FileNotFoundError:
    logger.error(f'Файл README.MD не найден по пути: {gs.path.root / "src" / "README.MD"}')
    doc_str = ''
except Exception as e:
    logger.error(f'Ошибка при чтении README.MD: {e}')
    doc_str = ''


__PROJECT_NAME__: str = settings.get('project_name', 'hypotez') if settings else 'hypotez'
__VERSION__: str = settings.get('version', '') if settings else ''
__DOC__: str = doc_str if doc_str else ''
__DETAILS__: str = ''
__AUTHOR__: str = settings.get('author', '') if settings else ''
__COPYRIGHT__: str = settings.get('copyrihgnt', '') if settings else ''
__COFEE__: str = settings.get('cofee', 'Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69') if settings else 'Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69'
```