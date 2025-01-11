# Анализ кода модуля `header`

**Качество кода**:
- **Соответствие стандартам**: 7
- **Плюсы**:
    - Код структурирован и относительно легко читается.
    - Используется `pathlib` для работы с путями.
    - Есть функция для определения корневой директории проекта.
    - Присутствует обработка исключений для загрузки настроек.
- **Минусы**:
    -  Используются двойные кавычки для строковых литералов, кроме вывода.
    -  Не используется `j_loads` или `j_loads_ns` для загрузки JSON.
    -  Исключения обрабатываются через `...`, что не информативно.
    -  Отсутствует RST-документация для модуля и функции.
    -  Не все переменные и импорты выровнены.

**Рекомендации по улучшению**:
- Замените двойные кавычки на одинарные в строковых литералах, за исключением `print`, `input` и `logger`.
- Используйте `j_loads_ns` для загрузки JSON файлов.
- Замените `...` в блоках `except` на логирование ошибок с помощью `logger.error`.
- Добавьте RST-документацию для модуля и функции `set_project_root`.
- Выровняйте импорты и переменные.
- Избегайте чрезмерного использования `try-except`, если можно использовать более точную обработку ошибок.
- Используйте `from src.logger.logger import logger` для логирования ошибок.

**Оптимизированный код**:
```python
# -*- coding: utf-8 -*-
# file: /src/suppliers/header.py
#! venv/bin/python/python3.12

"""
Модуль для определения корневой директории и загрузки настроек проекта.
======================================================================

Этот модуль предоставляет функции для определения корневой директории проекта и загрузки основных настроек из файлов `settings.json` и `README.MD`.

Функции
--------
    - :func:`set_project_root`: Находит корневую директорию проекта.

Пример использования
--------------------
.. code-block:: python

    from pathlib import Path
    from src.suppliers.header import set_project_root

    root_path = set_project_root()
    print(f"Project root: {root_path}")
"""
import sys
from pathlib import Path
from packaging.version import Version
from src.utils.jjson import j_loads_ns #  Импортируем j_loads_ns для загрузки json
from src.logger.logger import logger # Импортируем logger из src.logger


def set_project_root(marker_files: tuple = ('__root__', '.git')) -> Path:
    """
    Находит корневую директорию проекта, начиная с директории текущего файла.

    Директория определяется как родительская директория, содержащая любой из файлов-маркеров.
    Поиск идет вверх по дереву директорий, пока не будет найден маркер.

    :param marker_files: Кортеж имен файлов или директорий, которые идентифицируют корень проекта.
    :type marker_files: tuple, optional
    :return: Путь к корневой директории проекта.
    :rtype: Path
    
    :raises FileNotFoundError: Если маркеры не найдены.

    Пример:
        >>> from pathlib import Path
        >>> root_dir = set_project_root()
        >>> print(isinstance(root_dir, Path))
        True
    """
    __root__:Path
    current_path: Path = Path(__file__).resolve().parent # Получаем путь к директории текущего файла
    __root__ = current_path # Изначально корневой путь - это путь к директории текущего файла

    for parent in [current_path] + list(current_path.parents): # Проверяем текущую и родительские директории
        if any((parent / marker).exists() for marker in marker_files): # Если любой маркер существует
            __root__ = parent # Устанавливаем корневой путь
            break # Выходим из цикла
    if __root__ not in sys.path: #  Если путь к корню не в sys.path
        sys.path.insert(0, str(__root__)) # Добавляем путь к корню в sys.path
    return __root__ # Возвращаем путь к корню

# Get the root directory of the project
__root__ = set_project_root()
"""__root__ (Path): Path to the root directory of the project"""

from src import gs

settings: dict = None
try:
    with open(gs.path.root / 'src' / 'settings.json', 'r') as settings_file: # Открываем файл настроек
        settings = j_loads_ns(settings_file) # Загружаем json данные c помощью j_loads_ns
except FileNotFoundError: #  Ловим ошибку если файл не найден
    logger.error(f'File not found {gs.path.root / "src" / "settings.json"}') # Логируем ошибку с помощью logger
except json.JSONDecodeError: #  Ловим ошибку если файл не удалось декодировать
    logger.error(f'JSON decode error {gs.path.root / "src" / "settings.json"}') # Логируем ошибку с помощью logger


doc_str: str = None
try:
    with open(gs.path.root / 'src' / 'README.MD', 'r') as settings_file: # Открываем файл документации
        doc_str = settings_file.read() # читаем данные из файла
except FileNotFoundError: # Ловим ошибку если файл не найден
     logger.error(f'File not found {gs.path.root / "src" / "README.MD"}') # Логируем ошибку с помощью logger
except Exception as e: #  Ловим ошибку если файл не удалось прочитать
    logger.error(f'Error reading {gs.path.root / "src" / "README.MD"}: {e}') # Логируем ошибку с помощью logger

__project_name__ = settings.get('project_name', 'hypotez') if settings else 'hypotez' # получаем имя проекта из settings
__version__: str = settings.get('version', '') if settings else ''  # получаем версию из settings
__doc__: str = doc_str if doc_str else ''  # получаем документацию из doc_str
__details__: str = '' # переменная details
__author__: str = settings.get('author', '') if settings else ''  # получаем автора из settings
__copyright__: str = settings.get('copyrihgnt', '') if settings else '' # получаем copyright из settings
__cofee__: str = settings.get('cofee', 'Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69')  if settings  else 'Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69' # получаем cofee из settings
```