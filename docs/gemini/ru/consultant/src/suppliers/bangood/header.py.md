# Анализ кода модуля `header`

**Качество кода**
9
- Плюсы
    - Код хорошо структурирован и читаем.
    - Используется `pathlib` для работы с путями.
    - Присутствует обработка исключений при чтении файлов.
    -  Использование `set_project_root` для определения корневой директории.
- Минусы
    - Не все импорты в начале файла.
    - Использование стандартного `json.load`, а не `j_loads`.
    - Отсутствует логирование ошибок при обработке исключений.
    - Отсутствует документация в формате RST.
    - Не используется `logger`.

**Рекомендации по улучшению**

1.  **Импорты**: Добавить недостающие импорты в начало файла, а именно `from src.utils.jjson import j_loads`.
2.  **Чтение JSON**: Использовать `j_loads` для чтения `settings.json` вместо `json.load`.
3.  **Логирование**: Добавить логирование ошибок с использованием `logger.error` при возникновении исключений.
4.  **Документация**: Добавить docstring в формате RST для функций и модуля.
5.  **Форматирование**: Привести код в соответствие с PEP 8, включая пробелы вокруг операторов и т. д.
6.  **Убрать неиспользуемый import**: Убрать импорт `Version`.
7. **Избегать `...`**: Заменить `...` на `pass` и сделать log ошибки.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
"""
Модуль для установки корневого каталога проекта, загрузки настроек и определения метаданных проекта.
=========================================================================================

Этот модуль предоставляет функции для определения корневого каталога проекта,
загрузки настроек из файла `settings.json`, и чтения документации из `README.MD`.
Также он устанавливает метаданные проекта, такие как имя, версию, автор и т.д.

Пример использования
--------------------

.. code-block:: python

    from pathlib import Path

    # Получение корневого каталога проекта
    root_path = set_project_root()
    print(f"Корневой каталог проекта: {root_path}")

    # Доступ к метаданным проекта
    print(f"Имя проекта: {__project_name__}")
    print(f"Версия проекта: {__version__}")

"""
import sys
from pathlib import Path
from src.utils.jjson import j_loads
from src.logger.logger import logger


def set_project_root(marker_files: tuple = ('__root__', '.git')) -> Path:
    """
    Определяет корневую директорию проекта.

    Ищет корневую директорию проекта, начиная с директории текущего файла и двигаясь вверх
    по дереву каталогов, останавливаясь на первой директории, содержащей один из маркеров.

    Args:
        marker_files (tuple, optional): Список файлов или директорий, которые отмечают корень проекта.
             Defaults to ('__root__', '.git').

    Returns:
        Path: Путь к корневой директории проекта. Если не найдена, возвращается директория,
        где находится скрипт.

    Example:
        >>> set_project_root()
        PosixPath('/path/to/your/project')
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


# Получение корневой директории проекта
__root__ = set_project_root()
"""__root__ (Path): Путь к корневой директории проекта."""

from src import gs

settings: dict = None
try:
    # Чтение настроек из settings.json с использованием j_loads
    with open(gs.path.root / 'src' / 'settings.json', 'r') as settings_file:
        settings = j_loads(settings_file)
except (FileNotFoundError, json.JSONDecodeError) as e:
    logger.error(f'Ошибка при чтении файла настроек: {e}')
    settings = {}  # Инициализируем settings как пустой словарь

doc_str: str = None
try:
    # Чтение документации из README.MD
    with open(gs.path.root / 'src' / 'README.MD', 'r') as doc_file:
        doc_str = doc_file.read()
except (FileNotFoundError, json.JSONDecodeError) as e:
    logger.error(f'Ошибка при чтении файла документации: {e}')
    doc_str = ''  # Инициализируем doc_str как пустую строку

# Определение метаданных проекта
__project_name__ = settings.get('project_name', 'hypotez') if settings else 'hypotez'
"""str: Название проекта, по умолчанию 'hypotez'."""
__version__: str = settings.get('version', '') if settings else ''
"""str: Версия проекта."""
__doc__: str = doc_str if doc_str else ''
"""str: Документация проекта, загруженная из README.MD."""
__details__: str = ''
"""str: Дополнительная информация о проекте."""
__author__: str = settings.get('author', '') if settings else ''
"""str: Автор проекта."""
__copyright__: str = settings.get('copyrihgnt', '') if settings else ''
"""str: Информация об авторских правах."""
__cofee__: str = settings.get('cofee', "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69") if settings else "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69"
"""str: Сообщение о возможности угостить разработчика кофе."""
```