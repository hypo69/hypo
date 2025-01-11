# Анализ кода модуля `header.py`

**Качество кода**
8
- Плюсы
    - Код имеет хорошую структуру и читаемость.
    - Используется функция `set_project_root` для определения корневой директории проекта.
    - Код использует try-except блоки для обработки ошибок при чтении файлов.
    - Наличие констант для базовой информации о проекте (`__project_name__`, `__version__`, `__doc__`, и т.д.).
- Минусы
    -  Не используется `j_loads` или `j_loads_ns` из `src.utils.jjson` для чтения `settings.json`.
    -  Используются двойные кавычки для строк, хотя согласно инструкции следует использовать одинарные.
    -  Недостаточно комментариев и документации, особенно для переменных и констант.
    -  Импорт `gs` не используется в коде, следует проверить его необходимость.
    -  Не производится логирование ошибок.

**Рекомендации по улучшению**

1.  Использовать `j_loads_ns` для загрузки JSON-файлов.
2.  Использовать одинарные кавычки для строковых литералов.
3.  Добавить комментарии и документацию в формате RST для модуля, функций и переменных.
4.  Использовать `logger` для логирования ошибок.
5.  Удалить неиспользуемый импорт `gs` или использовать его.
6.  Обработать ошибку импорта `settings` с помощью `logger.error`.
7.  Добавить документацию к переменным с информацией о типе данных.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
"""
Модуль для определения корневой директории проекта и загрузки настроек.
=========================================================================================

Этот модуль определяет корневую директорию проекта, загружает настройки из файла 'settings.json'
и устанавливает глобальные переменные, содержащие информацию о проекте.

.. code-block:: python

    from src.endpoints.advertisement.facebook.header import __project_name__, __version__

    print(f"Project name: {__project_name__}")
"""
import sys
from pathlib import Path
from src.utils.jjson import j_loads_ns
from src.logger.logger import logger # Импортируем logger
from packaging.version import Version


def set_project_root(marker_files: tuple = ('__root__', '.git')) -> Path:
    """
    Определяет корневую директорию проекта, начиная с директории текущего файла,
    поиска вверх и останавливаясь в первой директории, содержащей любой из маркерных файлов.

    :param marker_files: Кортеж имен файлов или каталогов, определяющих корень проекта.
    :type marker_files: tuple
    :return: Путь к корневой директории, если она найдена, иначе - директория, где расположен скрипт.
    :rtype: Path

    :Example:
        >>> root_path = set_project_root()
        >>> print(root_path)
        /path/to/your/project
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
__root__: Path = set_project_root()
"""Path: Путь к корневой директории проекта."""

settings: dict = None
# блок кода исполняет загрузку настроек из файла settings.json
try:
    with open(__root__ / 'src' / 'settings.json', 'r') as settings_file: # используем __root__
        settings = j_loads_ns(settings_file)
except (FileNotFoundError, json.JSONDecodeError) as e:
    logger.error('Ошибка при загрузке файла settings.json', exc_info=True)
    ...

doc_str: str = None
# блок кода исполняет загрузку содержимого файла README.MD
try:
    with open(__root__ / 'src' / 'README.MD', 'r') as doc_file: # используем __root__
        doc_str = doc_file.read()
except (FileNotFoundError, json.JSONDecodeError) as e:
    logger.error('Ошибка при чтении файла README.MD', exc_info=True)
    ...
# блок кода определяет основные параметры проекта
__project_name__: str = settings.get('project_name', 'hypotez') if settings else 'hypotez'
"""str: Название проекта."""
__version__: str = settings.get('version', '') if settings else ''
"""str: Версия проекта."""
__doc__: str = doc_str if doc_str else ''
"""str: Содержимое документации проекта."""
__details__: str = ''
"""str: Детали проекта (пока не используется)."""
__author__: str = settings.get('author', '') if settings else ''
"""str: Автор проекта."""
__copyright__: str = settings.get('copyrihgnt', '') if settings else ''
"""str: Информация об авторских правах проекта."""
__cofee__: str = settings.get('cofee', 'Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69') if settings else 'Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69'
"""str: Сообщение с предложением угостить разработчика кофе."""
```