# Анализ кода модуля `header.py`

**Качество кода**
9
-   Плюсы
    - Код хорошо структурирован и читаем.
    - Используется функция `set_project_root` для определения корневой директории проекта, что является хорошей практикой для управления путями.
    - Присутствует обработка исключений для чтения файлов настроек (`settings.json`) и документации (`README.MD`).
    - Используются константы для хранения информации о проекте.
-   Минусы
    -  Не все переменные и функции имеют docstring.
    -  Используется стандартный `json.load` вместо `j_loads` или `j_loads_ns`.
    - Отсутствуют импорты `logger` и `j_loads`

**Рекомендации по улучшению**

1.  Добавить docstring к переменным `MODE`, `settings`, `doc_str`, `__project_name__`, `__version__`, `__doc__`, `__details__`, `__author__`, `__copyright__`, `__cofee__`.
2.  Заменить `json.load` на `j_loads` или `j_loads_ns` для чтения `settings.json`.
3.  Добавить импорт `from src.utils.jjson import j_loads`
4.  Использовать `logger.error` вместо `...` в блоках `except`.
5.  Добавить импорт `from src.logger.logger import logger`.
6.  Удалить ненужные shebang строки
7.  Устранить дублирование в блоках `try-except`.
8.  Привести в соответствие имена переменных с ранее обработанными файлами
9.  Привести в соответствие форматирование кода

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
"""
Модуль для определения основных настроек и переменных проекта.
=========================================================================================
    
Этот модуль определяет корневую директорию проекта, загружает настройки из `settings.json`
и устанавливает основные переменные, такие как имя проекта, версия, автор, и т.д.

Пример использования
--------------------

    Импортируйте модуль `header` для доступа к основным переменным проекта.

    .. code-block:: python
    
        from src.endpoints import header

        print(header.__project_name__)
        print(header.__version__)
"""
# Имортируем необходимые модули
import sys
from pathlib import Path
from packaging.version import Version

# импортируем кастомные модули
from src.utils.jjson import j_loads
from src.logger.logger import logger
from src import gs

# Режим работы приложения
MODE = 'dev'
"""str: Режим работы приложения (dev, prod)."""


def set_project_root(marker_files: tuple = ('pyproject.toml', 'requirements.txt', '.git')) -> Path:
    """
    Определяет корневую директорию проекта.
    
    Функция ищет корневую директорию проекта, начиная с директории текущего файла, 
    проверяя наличие маркерных файлов.
    
    :param marker_files: Кортеж имен файлов или директорий, которые являются маркерами корневой директории.
    :type marker_files: tuple
    :return: Путь к корневой директории проекта.
    :rtype: Path
    
    :raises FileNotFoundError: Если корневая директория не найдена.
    """
    __root__:Path
    current_path:Path = Path(__file__).resolve().parent
    __root__ = current_path
    for parent in [current_path] + list(current_path.parents):
        if any((parent / marker).exists() for marker in marker_files):
            __root__ = parent
            break
    if __root__ not in sys.path:
        sys.path.insert(0, str(__root__))
    return __root__

# устанавливаем корневую директорию проекта
__root__ = set_project_root()
"""Path: Путь к корневой директории проекта."""

settings: dict = None
"""dict: Словарь настроек проекта, загруженный из `settings.json`."""
try:
    # код исполняет чтение файла настроек и декодирование JSON
    with open(gs.path.root / 'src' /  'settings.json', 'r') as settings_file:
        settings = j_loads(settings_file)
except (FileNotFoundError,  json.JSONDecodeError) as ex:
    logger.error('Ошибка чтения файла настроек settings.json', ex)

doc_str: str = None
"""str: Строка документации проекта, загруженная из `README.MD`."""
try:
    # код исполняет чтение файла документации
    with open(gs.path.root / 'src' /  'README.MD', 'r') as settings_file:
        doc_str = settings_file.read()
except (FileNotFoundError,  json.JSONDecodeError) as ex:
    logger.error('Ошибка чтения файла документации README.MD', ex)
 
# основные переменные проекта
__project_name__ = settings.get("project_name", 'hypotez') if settings  else 'hypotez'
"""str: Название проекта."""
__version__: str = settings.get("version", '')  if settings  else ''
"""str: Версия проекта."""
__doc__: str = doc_str if doc_str else ''
"""str: Документация проекта."""
__details__: str = ''
"""str: Детали проекта."""
__author__: str = settings.get("author", '')  if settings  else ''
"""str: Автор проекта."""
__copyright__: str = settings.get("copyrihgnt", '')  if settings  else ''
"""str: Авторские права проекта."""
__cofee__: str = settings.get("cofee", "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69")  if settings  else "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69"
"""str: Сообщение о поддержке разработчика."""
```