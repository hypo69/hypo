# Улучшенный код
```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12
"""
Модуль для определения основных настроек и констант проекта.
===========================================================

Этот модуль определяет корневую директорию проекта, загружает настройки из файла `settings.json`,
инициализирует основные переменные, такие как имя проекта, версию, автор и т.д.

.. note::
   Модуль использует функции из `src.utils.jjson` для загрузки JSON файлов, что обеспечивает
   корректную обработку ошибок и не требует явного указания кодировки.
   Это позволяет корректно работать с файлами, в том числе и с русскими символами.

Пример использования
--------------------

.. code-block:: python

   from src.suppliers.visualdg.header import __project_name__, __version__

   print(f"Имя проекта: {__project_name__}")
   print(f"Версия: {__version__}")

"""
MODE = 'dev'

import sys
from pathlib import Path
from packaging.version import Version

from src.utils.jjson import j_loads # Импортируем j_loads из src.utils.jjson
from src.logger.logger import logger # Импортируем logger из src.logger.logger

def set_project_root(marker_files: tuple = ('pyproject.toml', 'requirements.txt', '.git')) -> Path:
    """
    Определяет корневую директорию проекта.

    Функция выполняет поиск вверх по дереву каталогов от текущего файла,
    останавливаясь на первом каталоге, содержащем любой из файлов-маркеров.

    :param marker_files: Кортеж с именами файлов или каталогов, которые идентифицируют корень проекта.
    :type marker_files: tuple
    :return: Путь к корневой директории проекта. Если корень не найден, возвращает директорию, где находится текущий файл.
    :rtype: Path
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
"""
:type: Path
:description: Путь к корневой директории проекта
"""

from src import gs

settings: dict = None
try:
    # Чтение файла settings.json
    with open(gs.path.root / 'src' / 'settings.json', 'r', encoding='utf-8') as settings_file:
        settings = j_loads(settings_file) # Используем j_loads вместо json.load
except FileNotFoundError:
     # Логирование ошибки при отсутствии файла
    logger.error(f'Файл settings.json не найден по пути {gs.path.root / "src" / "settings.json"}')
except Exception as ex:
     # Логирование ошибки при чтении файла
    logger.error(f'Ошибка при чтении файла settings.json: {ex}')
    ...


doc_str: str = None
try:
    # Чтение файла README.MD
    with open(gs.path.root / 'src' / 'README.MD', 'r', encoding='utf-8') as readme_file:
        doc_str = readme_file.read()
except FileNotFoundError:
     # Логирование ошибки при отсутствии файла
    logger.error(f'Файл README.MD не найден по пути {gs.path.root / "src" / "README.MD"}')
except Exception as ex:
     # Логирование ошибки при чтении файла
    logger.error(f'Ошибка при чтении файла README.MD: {ex}')
    ...

# Инициализация основных переменных проекта
__project_name__ = settings.get('project_name', 'hypotez') if settings else 'hypotez'
"""
:type: str
:description: Имя проекта.
"""
__version__: str = settings.get('version', '') if settings else ''
"""
:type: str
:description: Версия проекта.
"""
__doc__: str = doc_str if doc_str else ''
"""
:type: str
:description: Содержимое файла README.MD.
"""
__details__: str = ''
"""
:type: str
:description: Детальная информация о проекте.
"""
__author__: str = settings.get('author', '') if settings else ''
"""
:type: str
:description: Автор проекта.
"""
__copyright__: str = settings.get('copyrihgnt', '') if settings else ''
"""
:type: str
:description: Информация об авторских правах.
"""
__cofee__: str = settings.get('cofee', 'Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69') if settings else 'Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69'
"""
:type: str
:description: Призыв к поддержке разработчика.
"""
```
# Внесённые изменения
1.  **Добавлены импорты**:
    -   Импортирован `j_loads` из `src.utils.jjson` для загрузки JSON.
    -   Импортирован `logger` из `src.logger.logger` для логирования ошибок.
2.  **Изменено использование `json.load`**:
    -   Заменено `json.load` на `j_loads` для чтения файла `settings.json`.
3.  **Добавлена обработка ошибок**:
    -   Используется `logger.error` для логирования ошибок при открытии и чтении файлов `settings.json` и `README.MD`.
    -   Удалены избыточные `try-except` блоки и оставлены `...` как точки остановки.
4.  **Документация**:
    -   Добавлена документация в формате reStructuredText (RST) для модуля, функции `set_project_root`, и переменных.
5.  **Комментарии**:
    -   Добавлены подробные комментарии к коду, объясняющие каждый блок.
6.  **Кодировка**:
    -   Указана кодировка 'utf-8' при открытии файлов для корректной обработки русских символов.
# Оптимизированный код
```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12
"""
Модуль для определения основных настроек и констант проекта.
===========================================================

Этот модуль определяет корневую директорию проекта, загружает настройки из файла `settings.json`,
инициализирует основные переменные, такие как имя проекта, версию, автор и т.д.

.. note::
   Модуль использует функции из `src.utils.jjson` для загрузки JSON файлов, что обеспечивает
   корректную обработку ошибок и не требует явного указания кодировки.
   Это позволяет корректно работать с файлами, в том числе и с русскими символами.

Пример использования
--------------------

.. code-block:: python

   from src.suppliers.visualdg.header import __project_name__, __version__

   print(f"Имя проекта: {__project_name__}")
   print(f"Версия: {__version__}")

"""
MODE = 'dev'

import sys
from pathlib import Path
from packaging.version import Version

from src.utils.jjson import j_loads # Импортируем j_loads из src.utils.jjson
from src.logger.logger import logger # Импортируем logger из src.logger.logger

def set_project_root(marker_files: tuple = ('pyproject.toml', 'requirements.txt', '.git')) -> Path:
    """
    Определяет корневую директорию проекта.

    Функция выполняет поиск вверх по дереву каталогов от текущего файла,
    останавливаясь на первом каталоге, содержащем любой из файлов-маркеров.

    :param marker_files: Кортеж с именами файлов или каталогов, которые идентифицируют корень проекта.
    :type marker_files: tuple
    :return: Путь к корневой директории проекта. Если корень не найден, возвращает директорию, где находится текущий файл.
    :rtype: Path
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
"""
:type: Path
:description: Путь к корневой директории проекта
"""

from src import gs

settings: dict = None
try:
    # Чтение файла settings.json
    with open(gs.path.root / 'src' / 'settings.json', 'r', encoding='utf-8') as settings_file:
        settings = j_loads(settings_file) # Используем j_loads вместо json.load
except FileNotFoundError:
     # Логирование ошибки при отсутствии файла
    logger.error(f'Файл settings.json не найден по пути {gs.path.root / "src" / "settings.json"}')
except Exception as ex:
     # Логирование ошибки при чтении файла
    logger.error(f'Ошибка при чтении файла settings.json: {ex}')
    ...


doc_str: str = None
try:
    # Чтение файла README.MD
    with open(gs.path.root / 'src' / 'README.MD', 'r', encoding='utf-8') as readme_file:
        doc_str = readme_file.read()
except FileNotFoundError:
     # Логирование ошибки при отсутствии файла
    logger.error(f'Файл README.MD не найден по пути {gs.path.root / "src" / "README.MD"}')
except Exception as ex:
     # Логирование ошибки при чтении файла
    logger.error(f'Ошибка при чтении файла README.MD: {ex}')
    ...

# Инициализация основных переменных проекта
__project_name__ = settings.get('project_name', 'hypotez') if settings else 'hypotez'
"""
:type: str
:description: Имя проекта.
"""
__version__: str = settings.get('version', '') if settings else ''
"""
:type: str
:description: Версия проекта.
"""
__doc__: str = doc_str if doc_str else ''
"""
:type: str
:description: Содержимое файла README.MD.
"""
__details__: str = ''
"""
:type: str
:description: Детальная информация о проекте.
"""
__author__: str = settings.get('author', '') if settings else ''
"""
:type: str
:description: Автор проекта.
"""
__copyright__: str = settings.get('copyrihgnt', '') if settings else ''
"""
:type: str
:description: Информация об авторских правах.
"""
__cofee__: str = settings.get('cofee', 'Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69') if settings else 'Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69'
"""
:type: str
:description: Призыв к поддержке разработчика.
"""
```
```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12
"""
Модуль для определения основных настроек и констант проекта.
===========================================================

Этот модуль определяет корневую директорию проекта, загружает настройки из файла `settings.json`,
инициализирует основные переменные, такие как имя проекта, версию, автор и т.д.

.. note::
   Модуль использует функции из `src.utils.jjson` для загрузки JSON файлов, что обеспечивает
   корректную обработку ошибок и не требует явного указания кодировки.
   Это позволяет корректно работать с файлами, в том числе и с русскими символами.

Пример использования
--------------------

.. code-block:: python

   from src.suppliers.visualdg.header import __project_name__, __version__

   print(f"Имя проекта: {__project_name__}")
   print(f"Версия: {__version__}")

"""
MODE = 'dev'

import sys
from pathlib import Path
from packaging.version import Version

from src.utils.jjson import j_loads # Импортируем j_loads из src.utils.jjson
from src.logger.logger import logger # Импортируем logger из src.logger.logger

def set_project_root(marker_files: tuple = ('pyproject.toml', 'requirements.txt', '.git')) -> Path:
    """
    Определяет корневую директорию проекта.

    Функция выполняет поиск вверх по дереву каталогов от текущего файла,
    останавливаясь на первом каталоге, содержащем любой из файлов-маркеров.

    :param marker_files: Кортеж с именами файлов или каталогов, которые идентифицируют корень проекта.
    :type marker_files: tuple
    :return: Путь к корневой директории проекта. Если корень не найден, возвращает директорию, где находится текущий файл.
    :rtype: Path
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
"""
:type: Path
:description: Путь к корневой директории проекта
"""

from src import gs

settings: dict = None
try:
    # Чтение файла settings.json
    with open(gs.path.root / 'src' / 'settings.json', 'r', encoding='utf-8') as settings_file:
        settings = j_loads(settings_file) # Используем j_loads вместо json.load
except FileNotFoundError:
     # Логирование ошибки при отсутствии файла
    logger.error(f'Файл settings.json не найден по пути {gs.path.root / "src" / "settings.json"}')
except Exception as ex:
     # Логирование ошибки при чтении файла
    logger.error(f'Ошибка при чтении файла settings.json: {ex}')
    ...


doc_str: str = None
try:
    # Чтение файла README.MD
    with open(gs.path.root / 'src' / 'README.MD', 'r', encoding='utf-8') as readme_file:
        doc_str = readme_file.read()
except FileNotFoundError:
     # Логирование ошибки при отсутствии файла
    logger.error(f'Файл README.MD не найден по пути {gs.path.root / "src" / "README.MD"}')
except Exception as ex:
     # Логирование ошибки при чтении файла
    logger.error(f'Ошибка при чтении файла README.MD: {ex}')
    ...

# Инициализация основных переменных проекта
__project_name__ = settings.get('project_name', 'hypotez') if settings else 'hypotez'
"""
:type: str
:description: Имя проекта.
"""
__version__: str = settings.get('version', '') if settings else ''
"""
:type: str
:description: Версия проекта.
"""
__doc__: str = doc_str if doc_str else ''
"""
:type: str
:description: Содержимое файла README.MD.
"""
__details__: str = ''
"""
:type: str
:description: Детальная информация о проекте.
"""
__author__: str = settings.get('author', '') if settings else ''
"""
:type: str
:description: Автор проекта.
"""
__copyright__: str = settings.get('copyrihgnt', '') if settings else ''
"""
:type: str
:description: Информация об авторских правах.
"""
__cofee__: str = settings.get('cofee', 'Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69') if settings else 'Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69'
"""
:type: str
:description: Призыв к поддержке разработчика.
"""