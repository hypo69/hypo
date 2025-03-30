# Анализ кода модуля `header.py`

## Качество кода:
- **Соответствие стандартам**: 7
- **Плюсы**:
    - Имеется функция для определения корневой директории проекта.
    - Используются `pathlib.Path` для работы с путями.
    - Присутствует базовая обработка ошибок при чтении файлов.
    - Объявлены основные переменные проекта, такие как `__project_name__`, `__version__`, `__doc__` и т.д.
- **Минусы**:
    - Используется стандартный `json.load` вместо `j_loads` или `j_loads_ns`.
    - Не все переменные с настройками обрабатываются через `settings.get()`, что может привести к ошибкам, если настроек нет.
    - Отсутствует логирование ошибок при загрузке настроек и документации.
    - Не хватает документации в формате RST.
    - Присутствует неявное использование `gs.path.root`, которое не определено в данном коде.

## Рекомендации по улучшению:
- Заменить `json.load` на `j_loads` или `j_loads_ns` из `src.utils.jjson`.
- Добавить обработку ошибок с помощью `logger.error` при чтении `settings.json` и `README.MD`.
- Добавить проверку на наличие `settings` перед обращением к `settings.get()`, чтобы избежать ошибок при отсутствии файла настроек.
- Добавить RST-документацию для модуля и функции `set_project_root`.
- Обеспечить использование `from src.logger.logger import logger`.
- Использовать более точные описания в комментариях.
- Убрать `#! .pyenv/bin/python3`, так как это избыточно и может быть неверным для различных окружений.
- Заменить конструкцию `if settings else 'value'` на `settings.get('key', 'value')`.
- Обеспечить, что `gs.path.root` импортируется корректно.
- При чтении файлов добавить кодировку `encoding='utf-8'`.

## Оптимизированный код:
```python
# -*- coding: utf-8 -*-
"""
Модуль для определения корневого пути проекта и загрузки основных настроек.
===========================================================================

Модуль определяет корневой путь проекта и загружает основные настройки, 
такие как имя проекта, версия, автор и т.д., из файла `settings.json` и документацию из `README.MD`.
Использует `pathlib.Path` для работы с путями и `src.utils.jjson` для загрузки json.

Пример использования
----------------------
.. code-block:: python

    from src.logger import logger
    from src.header import __project_name__, __version__, __doc__

    logger.info(f'Project name: {__project_name__}')
    logger.info(f'Project version: {__version__}')
    logger.info(f'Project doc: {__doc__}')

"""
import sys
from pathlib import Path
from src.utils.jjson import j_loads  # Используем j_loads для загрузки json
from src.logger import logger # Импортируем logger
from packaging.version import Version

def set_project_root(marker_files: tuple = ('__root__', '.git')) -> Path:
    """
    Находит корневую директорию проекта, начиная с директории текущего файла.

    Поиск ведется вверх по директориям до тех пор, пока не будет найдена директория, 
    содержащая один из файлов-маркеров.

    :param marker_files: Названия файлов или директорий для идентификации корня проекта.
    :type marker_files: tuple, optional
    :return: Путь к корневой директории, если она найдена, иначе путь к директории, где расположен скрипт.
    :rtype: Path
    
    Пример:
        >>> from pathlib import Path
        >>> current_file = Path(__file__)
        >>> root_dir = set_project_root()
        >>> print(root_dir)
        ...
    """
    current_path: Path = Path(__file__).resolve().parent
    root_path: Path = current_path # Инициализируем root_path текущей директорией
    for parent in [current_path] + list(current_path.parents):
        if any((parent / marker).exists() for marker in marker_files):
            root_path = parent # Найдена корневая директория
            break
    if root_path not in sys.path:
        sys.path.insert(0, str(root_path))
    return root_path


# Получаем корневую директорию проекта
__root__: Path = set_project_root()
"""__root__ (Path): Путь к корневой директории проекта."""

from src import gs  # Импортируем gs для доступа к путям

settings: dict = None
try:
    with open(gs.path.root / 'src' / 'settings.json', 'r', encoding='utf-8') as settings_file: # Открываем файл с кодировкой utf-8
        settings = j_loads(settings_file) # Загружаем настройки с помощью j_loads
except (FileNotFoundError, Exception) as e: # Ловим ошибки FileNotFoundError и все остальные исключения
    logger.error(f"Не удалось загрузить файл настроек: {e}") # Логируем ошибку загрузки настроек
    settings = {} # Если ошибка, то настройки будут пустыми


doc_str: str = None
try:
    with open(gs.path.root / 'src' / 'README.MD', 'r', encoding='utf-8') as settings_file: # Открываем файл с кодировкой utf-8
        doc_str = settings_file.read() # Читаем содержимое файла
except (FileNotFoundError, Exception) as e: # Ловим ошибки FileNotFoundError и все остальные исключения
    logger.error(f"Не удалось загрузить файл документации: {e}") # Логируем ошибку загрузки документации
    doc_str = '' # Если ошибка, то doc_str будет пустым

# Получаем основные настройки проекта
__project_name__: str = settings.get("project_name", 'hypotez') if settings else 'hypotez' # Получаем имя проекта, если есть, иначе 'hypotez'
__version__: str = settings.get("version", '') if settings else '' # Получаем версию проекта, если есть, иначе ''
__doc__: str = doc_str if doc_str else '' # Получаем документацию, если есть, иначе ''
__details__: str = '' #  Инициализируем __details__
__author__: str = settings.get("author", '') if settings else '' # Получаем автора, если есть, иначе ''
__copyright__: str = settings.get("copyrihgnt", '') if settings else '' # Получаем копирайт, если есть, иначе ''
__cofee__: str = settings.get("cofee", "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69")  if settings else "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69" # Получаем сообщение про кофе, если есть, иначе сообщение по умолчанию
```