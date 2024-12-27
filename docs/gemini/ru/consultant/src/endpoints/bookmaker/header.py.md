# Анализ кода модуля `header.py`

**Качество кода**
7
-   Плюсы
    -   Код выполняет функцию определения корневой директории проекта и загрузки настроек.
    -   Используется `pathlib` для работы с путями, что является хорошей практикой.
    -   Присутствует обработка исключений при загрузке файлов настроек, хотя и с использованием `...`.
    -   Используются константы для хранения значений метаданных проекта.
-   Минусы
    -   Отсутствует документация в формате RST для модуля, функций и переменных.
    -   Используется стандартный `json.load` вместо `j_loads` или `j_loads_ns`.
    -   Исключения обрабатываются не с помощью `logger.error`.
    -   Использование `...` не информативно.
    -   Наличие  комментариев `#`, которые нужно переоформить в `rst`.
    -   Импорты не отсортированы и не приведены в соответствие с другими файлами.

**Рекомендации по улучшению**

1.  Добавить документацию в формате RST для модуля, функций и переменных.
2.  Использовать `j_loads` или `j_loads_ns` из `src.utils.jjson` вместо стандартного `json.load` для чтения файлов.
3.  Заменить обработку исключений с использованием `...` на `logger.error`.
4.  Привести в соответствие импорты с другими файлами проекта.
5.  Удалить лишние комментарии `#` и переписать в `rst`.
6.  Добавить комментарии с подробным объяснением каждого блока кода.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
Модуль для определения корневой директории проекта и загрузки настроек.
======================================================================

Этот модуль выполняет поиск корневой директории проекта, загружает настройки из файла `settings.json`
и документацию из файла `README.MD`, а также предоставляет метаданные проекта.

Функции
-------
    - `set_project_root`: Находит корневую директорию проекта.

Переменные
----------
    - `__root__`: Путь к корневой директории проекта.
    - `settings`: Словарь с настройками проекта.
    - `doc_str`: Строка с документацией проекта.
    - `__project_name__`: Имя проекта.
    - `__version__`: Версия проекта.
    - `__doc__`: Документация проекта.
    - `__details__`: Детали проекта.
    - `__author__`: Автор проекта.
    - `__copyright__`: Авторские права проекта.
    - `__cofee__`: Сообщение о возможности поддержки разработчика.
"""
import sys
from pathlib import Path
from typing import Tuple, Dict, Optional

from src.utils.jjson import j_loads
from src.logger.logger import logger
from packaging.version import Version
from src import gs

MODE = 'dev'


def set_project_root(marker_files: Tuple[str, ...] = ('pyproject.toml', 'requirements.txt', '.git')) -> Path:
    """
    Находит корневую директорию проекта, начиная с директории текущего файла.

    Поиск идет вверх по дереву директорий и останавливается на первой директории,
    содержащей один из файлов-маркеров.

    :param marker_files: Кортеж имен файлов или директорий, которые служат маркерами корневой директории проекта.
    :type marker_files: Tuple[str, ...]
    :return: Путь к корневой директории проекта.
    :rtype: Path
    """
    __root__: Path
    # Получение абсолютного пути к текущему файлу и его родительской директории
    current_path: Path = Path(__file__).resolve().parent
    __root__ = current_path
    # Итерация по текущей директории и ее родительским директориям
    for parent in [current_path] + list(current_path.parents):
        # Проверка наличия маркеров в текущей директории
        if any((parent / marker).exists() for marker in marker_files):
            __root__ = parent
            break
    # Добавление корневой директории в sys.path, если ее там нет
    if __root__ not in sys.path:
        sys.path.insert(0, str(__root__))
    return __root__


# Получение корневой директории проекта
__root__: Path = set_project_root()
"""__root__ (Path): Путь к корневой директории проекта"""

settings: Optional[Dict] = None
# Попытка загрузить настройки из файла settings.json
try:
    # Открытие файла настроек
    with open(gs.path.root / 'src' / 'settings.json', 'r') as settings_file:
        # Загрузка настроек с использованием j_loads
        settings = j_loads(settings_file)
except (FileNotFoundError, Exception) as ex:
    # Логирование ошибки, если файл не найден или не удалось декодировать JSON
    logger.error(f'Ошибка загрузки файла настроек settings.json {ex}')
    ...

doc_str: Optional[str] = None
# Попытка загрузить документацию из файла README.MD
try:
    # Открытие файла документации
    with open(gs.path.root / 'src' / 'README.MD', 'r') as settings_file:
        # Чтение содержимого файла
        doc_str = settings_file.read()
except (FileNotFoundError, Exception) as ex:
    # Логирование ошибки, если файл не найден или не удалось прочитать файл
    logger.error(f'Ошибка загрузки файла документации README.MD {ex}')
    ...

# Получение метаданных проекта
__project_name__: str = settings.get("project_name", 'hypotez') if settings else 'hypotez'
"""__project_name__ (str): Имя проекта"""
__version__: str = settings.get("version", '') if settings else ''
"""__version__ (str): Версия проекта"""
__doc__: str = doc_str if doc_str else ''
"""__doc__ (str): Документация проекта"""
__details__: str = ''
"""__details__ (str): Детали проекта"""
__author__: str = settings.get("author", '') if settings else ''
"""__author__ (str): Автор проекта"""
__copyright__: str = settings.get("copyrihgnt", '') if settings else ''
"""__copyright__ (str): Авторские права проекта"""
__cofee__: str = settings.get("cofee", "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69") if settings else "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69"
"""__cofee__ (str): Сообщение о возможности поддержки разработчика"""
```