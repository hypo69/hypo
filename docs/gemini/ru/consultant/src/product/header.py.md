# Анализ кода модуля `header.py`

**Качество кода**
8
- Плюсы
    - Код выполняет задачу определения корневого каталога проекта и загрузки настроек.
    - Используется `pathlib` для работы с путями, что делает код более читаемым и кроссплатформенным.
    - Присутствуют docstring для функций.
    - Используется `try-except` для обработки ошибок при чтении файлов.
- Минусы
    - Не используются `j_loads` или `j_loads_ns` из `src.utils.jjson` для чтения файлов.
    - Отсутствует явная обработка исключений с помощью `logger.error`.
    -  Имена переменных `__root__` не соответствуют конвенции именования Python (имена с двумя подчеркиваниями в начале и конце обычно зарезервированы для специальных методов).
    - В `try-except` блоках используется `...` вместо явной обработки ошибок.
    - Присутствуют не все необходимые импорты.
    - Отсутствует RST документация для модуля.
    - Используется `json.load` вместо `j_loads` или `j_loads_ns`
    - Не все docstring написаны в RST

**Рекомендации по улучшению**

1.  Использовать `j_loads` или `j_loads_ns` вместо `json.load` для загрузки JSON файлов.
2.  Заменить обработку исключений `...` на логирование ошибок с помощью `logger.error`.
3.  Устранить использование переменной `__root__` как глобальной.
4.  Добавить проверку на наличие ключей в словаре `settings` перед их использованием.
5.  Добавить документацию в формате RST для модуля.
6.  Привести в соответствие имена переменных и констант.
7.  Добавить недостающие импорты.
8.  Заменить `FileNotFoundError, json.JSONDecodeError` на `Exception` для более общей обработки ошибок.
9.  Избавиться от дублирования кода в `try` блоках.
10. Все docstring переписать в формате `RST`

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
Модуль для определения корневого каталога проекта и загрузки настроек.
=======================================================================

Модуль определяет корневой путь к проекту и загружает настройки из файла `settings.json`.
Все импорты строятся относительно этого пути.

:TODO: В дальнейшем перенести в системную переменную

Пример использования:
---------------------

.. code-block:: python

    from src.product import header

    print(header.__project_name__)
    print(header.__version__)
"""
import sys
from pathlib import Path
from packaging.version import Version
from typing import Tuple, Optional, Dict, Any

from src.utils.jjson import j_loads  # Используем j_loads для загрузки JSON
from src.logger.logger import logger # Используем logger для обработки ошибок


MODE = 'dev'
"""
Режим работы приложения. Может принимать значения 'dev', 'test', 'prod'
"""

def set_project_root(marker_files: Tuple[str, ...] = ('pyproject.toml', 'requirements.txt', '.git')) -> Path:
    """
    Определяет корневой каталог проекта.

    Функция ищет родительский каталог, содержащий один из указанных файлов-маркеров.
    Поиск начинается с каталога, в котором находится данный файл и идет вверх по дереву каталогов.

    :param marker_files: Кортеж имен файлов или директорий, которые служат маркерами корневого каталога.
    :type marker_files: tuple[str, ...]
    :return: Абсолютный путь к корневому каталогу проекта.
    :rtype: pathlib.Path
    """
    current_path: Path = Path(__file__).resolve().parent
    root_path: Path = current_path # Инициализация root_path

    for parent in [current_path] + list(current_path.parents):
        if any((parent / marker).exists() for marker in marker_files):
            root_path = parent
            break
    if root_path not in sys.path:
        sys.path.insert(0, str(root_path))
    return root_path


# Получение корневого каталога проекта
root_path: Path = set_project_root()
"""
:type: pathlib.Path
:var root_path: Абсолютный путь к корневому каталогу проекта.
"""

from src import gs

settings: Optional[Dict[str, Any]] = None
"""
:type: dict | None
:var settings: Словарь с настройками проекта, загруженными из файла `settings.json`.
"""

try:
    # Код исполняет загрузку настроек из файла settings.json
    with open(root_path / 'src' / 'settings.json', 'r', encoding='utf-8') as settings_file:
        settings = j_loads(settings_file.read())
except Exception as ex:
    logger.error('Ошибка при загрузке настроек из файла settings.json', exc_info=ex)


doc_str: str = None
"""
:type: str | None
:var doc_str: Строка с содержимым файла `README.MD`, используемая для документации проекта.
"""
try:
    # Код исполняет загрузку документации из файла README.MD
    with open(root_path / 'src' / 'README.MD', 'r', encoding='utf-8') as readme_file:
        doc_str = readme_file.read()
except Exception as ex:
    logger.error('Ошибка при загрузке документации из файла README.MD', exc_info=ex)

__project_name__: str = settings.get("project_name", 'hypotez') if settings else 'hypotez'
"""
:type: str
:var __project_name__: Название проекта.
"""
__version__: str = settings.get("version", '') if settings else ''
"""
:type: str
:var __version__: Версия проекта.
"""
__doc__: str = doc_str if doc_str else ''
"""
:type: str
:var __doc__: Строка с документацией проекта.
"""
__details__: str = ''
"""
:type: str
:var __details__: Дополнительная информация о проекте.
"""
__author__: str = settings.get("author", '') if settings else ''
"""
:type: str
:var __author__: Автор проекта.
"""
__copyright__: str = settings.get("copyrihgnt", '') if settings else ''
"""
:type: str
:var __copyright__: Информация об авторских правах.
"""
__cofee__: str = settings.get("cofee", "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69") if settings else "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69"
"""
:type: str
:var __cofee__: Сообщение с призывом угостить разработчика кофе.
"""
```