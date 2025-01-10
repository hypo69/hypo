# Анализ кода модуля `header.py`

**Качество кода**
9
- Плюсы
    - Код хорошо структурирован и выполняет свою задачу по определению корневой директории проекта и загрузке настроек.
    - Используется `pathlib.Path` для работы с путями, что делает код более читаемым и кросс-платформенным.
    - Присутствует обработка исключений `FileNotFoundError` и `json.JSONDecodeError` при загрузке файлов настроек.
    - Есть описание модуля и переменных.
- Минусы
    - Используется `json.load` вместо `j_loads` или `j_loads_ns` из `src.utils.jjson`.
    - Отсутствуют импорты `logger` из `src.logger.logger`.
    - Присутствуют `...` в обработке исключений, которые должны быть заменены на логирование ошибок.
    - Документация не соответствует RST стандарту (отсутсвует документация для функций и переменных, кроме `set_project_root`).
    - Нет docstring для модуля

**Рекомендации по улучшению**

1.  Заменить `json.load` на `j_loads` или `j_loads_ns` из `src.utils.jjson`.
2.  Добавить импорт `logger` из `src.logger.logger`.
3.  Заменить `...` в блоках `except` на логирование ошибок с помощью `logger.error`.
4.  Добавить docstring в формате RST для модуля и переменных.
5.  Добавить docstring в формате RST для функции `set_project_root`.
6.  Привести в соответствие названия переменных (например `__root__` сделать `root_path`) и убрать лишние переменные.

**Оптимизированный код**

```python
"""
Модуль для определения корневой директории проекта, загрузки настроек и определения глобальных переменных.
=========================================================================================

Этот модуль предоставляет функциональность для автоматического определения корневой директории проекта,
загрузки настроек из файла `settings.json` и документации из `README.MD`, а также определения глобальных переменных
проекта, таких как имя, версия и автор.

Пример использования
--------------------

Пример использования:

.. code-block:: python

    from src.fast_api.header import root_path, __project_name__, __version__, __doc__, __author__, __copyright__

    print(f"Project Root: {root_path}")
    print(f"Project Name: {__project_name__}")
    print(f"Project Version: {__version__}")
    print(f"Project Author: {__author__}")
"""
# -*- coding: utf-8 -*-

#! venv/bin/python/python3.12

import sys
from pathlib import Path
from packaging.version import Version

from src.utils.jjson import j_loads
from src.logger.logger import logger
from src import gs


def set_project_root(marker_files: tuple[str, ...] = ('__root__', '.git')) -> Path:
    """
    Определяет корневую директорию проекта, начиная с директории текущего файла,
    поиска вверх и остановки в первой директории, содержащей любой из маркерных файлов.

    Args:
        marker_files (tuple): Кортеж с именами файлов или директорий для идентификации корневой директории проекта.

    Returns:
        Path: Путь к корневой директории, если она найдена, иначе директория, где расположен скрипт.

    Example:
        >>> set_project_root()
        WindowsPath('...')
    """
    root_path: Path
    current_path: Path = Path(__file__).resolve().parent
    root_path = current_path
    for parent in [current_path] + list(current_path.parents):
        if any((parent / marker).exists() for marker in marker_files):
            root_path = parent
            break
    if root_path not in sys.path:
        sys.path.insert(0, str(root_path))
    return root_path

# Код исполняет поиск и установку корневой директории проекта
root_path: Path = set_project_root()
"""Path: Путь к корневой директории проекта"""

settings: dict | None = None
try:
    # Код исполняет загрузку настроек из файла settings.json
    with open(gs.path.root / 'src' /  'settings.json', 'r') as settings_file:
        settings = j_loads(settings_file) # Заменено на j_loads
except (FileNotFoundError, json.JSONDecodeError) as e:
    # Логирование ошибки, если файл не найден или не может быть прочитан
    logger.error('Ошибка при загрузке настроек из файла settings.json', exc_info=e)

doc_str: str | None = None
try:
    # Код исполняет чтение содержимого файла README.MD
    with open(gs.path.root / 'src' /  'README.MD', 'r') as readme_file:
        doc_str = readme_file.read()
except (FileNotFoundError, json.JSONDecodeError) as e:
    # Логирование ошибки, если файл не найден или не может быть прочитан
    logger.error('Ошибка при чтении файла README.MD', exc_info=e)

# Код устанавливает значения глобальных переменных из настроек или по умолчанию
__project_name__: str = settings.get("project_name", 'hypotez') if settings  else 'hypotez'
"""str: Имя проекта"""
__version__: str = settings.get("version", '')  if settings  else ''
"""str: Версия проекта"""
__doc__: str = doc_str if doc_str else ''
"""str: Документация проекта"""
__details__: str = ''
"""str: Детали проекта"""
__author__: str = settings.get("author", '')  if settings  else ''
"""str: Автор проекта"""
__copyright__: str = settings.get("copyrihgnt", '')  if settings  else ''
"""str: Авторские права проекта"""
__cofee__: str = settings.get("cofee", "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69")  if settings  else "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69"
"""str: Сообщение для поддержки разработчика"""
```