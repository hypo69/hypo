# Анализ кода модуля `header.py`

**Качество кода**
8
-  Плюсы
    - Код имеет docstring для модуля и функции `set_project_root`.
    - Используется `pathlib` для работы с путями, что является хорошей практикой.
    - Код читаемый и понятный.
    - Код правильно определяет корневую директорию проекта и добавляет её в `sys.path`.
    - Присутствует обработка ошибок при чтении файлов конфигурации и документации.
-  Минусы
    - Не все переменные имеют аннотацию типов, например `__root__` в функции `set_project_root`
    - Используется стандартный `json.load` вместо `j_loads` или `j_loads_ns` из `src.utils.jjson`.
    - Логирование ошибок отсутствует.
    - В блоках `try-except` используется `...`, что не является информативным.
    -  Не хватает docstring для переменных модуля.
    - Использование `settings` без предварительного определения.
    - Переменная `__cofee__` опечатка в `copyrihgnt`

**Рекомендации по улучшению**
1.  Использовать `j_loads` или `j_loads_ns` из `src.utils.jjson` вместо `json.load`.
2.  Добавить логирование ошибок с помощью `logger.error` при чтении файлов.
3.  Убрать использование `...` в блоках `try-except` и добавить конкретную обработку ошибок.
4.  Добавить docstring для переменных модуля.
5.  Исправить опечатку `copyrihgnt` на `copyright`.
6.  Заменить `settings` на `config` в строке `__cofee__`.
7. Добавить импорт `from src.logger import logger`.
8. Добавить аннотацию типов `Path` в `set_project_root`
9. Добавить аннотацию типа для `config`.
10. Привести в соответствие имена переменных `doc_str` на `readme_str`
11. Удалить лишние импорты.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
"""
Модуль для установки корневого каталога проекта и загрузки основных параметров.
=========================================================================================

Этот модуль содержит функции и переменные для определения корневого каталога проекта,
загрузки конфигурации из JSON-файла и README.MD, а также определения основных параметров
проекта, таких как имя, версия, автор и т.д.

Пример использования
--------------------

.. code-block:: python

    from src.ai.helicone.header import __project_name__, __version__

    print(f"Имя проекта: {__project_name__}")
    print(f"Версия проекта: {__version__}")
"""

import sys
from pathlib import Path
from typing import  Dict, Optional
from packaging.version import Version # type: ignore

from src.utils.jjson import j_loads # type: ignore
from src.logger import logger # type: ignore

def set_project_root(marker_files: tuple = ('__root__', '.git')) -> Path:
    """
    Определяет корневой каталог проекта, начиная с каталога текущего файла.
    Поиск ведется вверх по дереву каталогов до первого каталога, содержащего любой из файлов-маркеров.

    Args:
        marker_files (tuple): Кортеж имен файлов или каталогов, идентифицирующих корень проекта.

    Returns:
        Path: Путь к корневому каталогу, если он найден, иначе каталог, где расположен скрипт.
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


# Get the root directory of the project
__root__: Path = set_project_root()
"""Path: Путь к корневому каталогу проекта."""

from src import gs

config: Optional[Dict] = None
try:
    # Чтение файла конфигурации config.json
    with open(gs.path.root / 'src' / 'config.json', 'r') as f:
        config = j_loads(f)
except (FileNotFoundError, Exception) as e:
    logger.error(f'Ошибка чтения файла конфигурации config.json: {e}')

readme_str: Optional[str] = None
try:
    # Чтение файла README.MD
    with open(gs.path.root / 'src' / 'README.MD', 'r') as settings_file:
        readme_str = settings_file.read()
except (FileNotFoundError, Exception) as e:
    logger.error(f'Ошибка чтения файла README.MD: {e}')


__project_name__: str = config.get("project_name", 'hypotez') if config else 'hypotez'
"""str: Имя проекта."""
__version__: str = config.get("version", '') if config else ''
"""str: Версия проекта."""
__doc__: str = readme_str if readme_str else ''
"""str: Документация проекта из README.MD."""
__details__: str = ''
"""str: Дополнительные детали проекта."""
__author__: str = config.get("author", '') if config else ''
"""str: Автор проекта."""
__copyright__: str = config.get("copyright", '') if config else ''
"""str: Авторское право."""
__cofee__: str = config.get("cofee", "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69") if config else "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69"
"""str: Сообщение для поддержки разработчика."""
```