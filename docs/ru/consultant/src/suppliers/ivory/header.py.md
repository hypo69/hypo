# Анализ кода модуля `header`

## Качество кода:

- **Соответствие стандартам**: 7
- **Плюсы**:
    - Код в целом структурирован и выполняет свою функцию по установке корневой директории проекта.
    - Используется `pathlib` для работы с путями, что является хорошей практикой.
    - Присутствует базовая обработка исключений для чтения файлов настроек и документации.
- **Минусы**:
    - Не используется `j_loads` или `j_loads_ns` для загрузки JSON, что противоречит инструкции.
    - Отсутствует явная обработка ошибок через `logger.error`, вместо этого используется `...`.
    - Некоторые переменные, такие как `__root__`, объявлены без аннотации типа.
    - Не хватает RST-документации для модуля, переменных и функций.
    - Не всегда используются одинарные кавычки для строк.

## Рекомендации по улучшению:

1.  **Использовать `j_loads`**: Замените `json.load` на `j_loads` или `j_loads_ns` из `src.utils.jjson`.
2.  **Обработка ошибок через `logger.error`**:  Замените `...` на логирование ошибок с использованием `logger.error`.
3.  **Добавить RST-документацию**: Добавьте docstring в формате RST для модуля, функции `set_project_root`, а также для всех глобальных переменных.
4.  **Аннотация типов**: Добавьте аннотации типов для переменных, где это возможно.
5.  **Использовать одинарные кавычки**: Перейдите на одинарные кавычки в коде и двойные кавычки только в операциях вывода и логирования.
6.  **Импортировать `logger`**: Импортируйте `logger` из `src.logger`.
7. **Упростить извлечение настроек**: Упростите код, использующий `settings.get`, чтобы избежать повторения `if settings else`
8. **Добавить `__all__`**: Добавьте `__all__` для определения публичного интерфейса модуля.

## Оптимизированный код:

```python
"""
Модуль для определения настроек проекта и корневой директории.
=============================================================

Модуль обеспечивает функциональность для автоматического определения корневой директории проекта,
а также загружает настройки проекта из файла `settings.json` и документацию из `README.MD`.

Пример использования
----------------------
.. code-block:: python

    from src.suppliers.ivory.header import __project_name__, __version__, __doc__

    print(f'Имя проекта: {__project_name__}')
    print(f'Версия проекта: {__version__}')
    print(f'Документация проекта: {__doc__}')
"""
__all__ = [
    '__project_name__',
    '__version__',
    '__doc__',
    '__details__',
    '__author__',
    '__copyright__',
    '__cofee__'
]

import sys
from pathlib import Path
from packaging.version import Version

from src.utils.jjson import j_loads
from src.logger import logger # Импорт logger из src.logger


def set_project_root(marker_files: tuple = ('__root__', '.git')) -> Path:
    """
    Находит корневой каталог проекта, начиная с каталога текущего файла,
    поиском вверх и останавливаясь на первом каталоге, содержащем любой из файлов-маркеров.

    :param marker_files: Имена файлов или каталогов для идентификации корня проекта.
    :type marker_files: tuple, optional
    :return: Путь к корневому каталогу, если он найден, иначе каталог, где находится скрипт.
    :rtype: Path

    Пример:
       >>> set_project_root()
       PosixPath('/path/to/your/project')
    """
    current_path: Path = Path(__file__).resolve().parent
    __root__: Path = current_path # Аннотация типа
    for parent in [current_path] + list(current_path.parents):
        if any((parent / marker).exists() for marker in marker_files):
            __root__ = parent
            break
    if __root__ not in sys.path:
        sys.path.insert(0, str(__root__))
    return __root__


# Get the root directory of the project
__root__: Path = set_project_root()
"""Path: Путь к корневому каталогу проекта."""

from src import gs


settings: dict | None = None
try:
    with open(gs.path.root / 'src' / 'settings.json', 'r') as settings_file:
        settings = j_loads(settings_file)  # Используем j_loads
except (FileNotFoundError, json.JSONDecodeError) as e: # Добавляем имя исключения для более точного логирования
    logger.error(f'Ошибка при загрузке файла настроек: {e}') # Логируем ошибку

doc_str: str | None = None
try:
    with open(gs.path.root / 'src' / 'README.MD', 'r') as settings_file:
        doc_str = settings_file.read()
except (FileNotFoundError) as e: # Добавляем имя исключения для более точного логирования
    logger.error(f'Ошибка при загрузке файла документации: {e}') # Логируем ошибку


__project_name__: str = settings.get('project_name', 'hypotez') if settings else 'hypotez'
"""str: Имя проекта."""
__version__: str = settings.get('version', '') if settings else ''
"""str: Версия проекта."""
__doc__: str = doc_str if doc_str else ''
"""str: Документация проекта."""
__details__: str = ''
"""str: Детали проекта."""
__author__: str = settings.get('author', '') if settings else ''
"""str: Автор проекта."""
__copyright__: str = settings.get('copyrihgnt', '') if settings else ''
"""str: Авторские права."""
__cofee__: str = settings.get('cofee', 'Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69') if settings else 'Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69'
"""str: Сообщение о кофе."""