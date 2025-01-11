# Анализ кода модуля `header.py`

**Качество кода**
8
- Плюсы
    - Код достаточно хорошо структурирован.
    - Используется `pathlib` для работы с путями, что является хорошей практикой.
    - Присутствует обработка ошибок при чтении файлов настроек и документации.
    - Есть документация для функции `set_project_root`.
- Минусы
    -  Не используются `j_loads` или `j_loads_ns` из `src.utils.jjson` для чтения файлов.
    - Отсутствует импорт `logger` из `src.logger.logger`.
    - Использован `try-except` с `...` для обработки исключений, что затрудняет отладку.
    -  Не хватает документации в формате RST для переменных модуля.
    - Не используется проверка на наличие `settings` при доступе к ключам.
    - Отсутствует описание модуля в формате RST.

**Рекомендации по улучшению**
1.  Использовать `j_loads` или `j_loads_ns` для загрузки JSON файлов.
2.  Импортировать `logger` из `src.logger.logger` и использовать его для логирования ошибок.
3.  Заменить `...` в блоках `try-except` на логирование ошибок с помощью `logger.error`.
4.  Добавить документацию в формате RST для переменных модуля.
5.  Добавить проверку наличия `settings` перед доступом к ключам.
6.  Добавить описание модуля в формате RST.
7.  Изменить способ импорта `gs`, чтобы избежать неоднозначности.
8.  Привести имена переменных к единому стилю (например, `doc_str` -> `doc_string`).

**Оптимизированный код**
```python
# -*- coding: utf-8 -*-
"""
Модуль для определения корневого пути проекта и загрузки настроек.
=================================================================

Модуль `src.utils.string.header` определяет корневой путь проекта,
загружает настройки из файла `settings.json` и документацию из `README.md`,
а также предоставляет информацию о проекте, такую как имя, версия и автор.

Пример использования
--------------------

Для получения пути к корню проекта:

.. code-block:: python

    from src.utils.string.header import __root__
    print(__root__)

Для получения версии проекта:

.. code-block:: python

    from src.utils.string.header import __version__
    print(__version__)

"""
import sys
from pathlib import Path
from packaging.version import Version

from src.logger.logger import logger  # Импорт logger
from src.utils.jjson import j_loads   #  Импорт j_loads

def set_project_root(marker_files: tuple = ('__root__', '.git')) -> Path:
    """
    Определяет корневой каталог проекта, начиная с каталога текущего файла,
    поиск вверх и остановка на первом каталоге, содержащем любой из файлов-маркеров.

    Args:
        marker_files (tuple): Имена файлов или каталогов, определяющих корень проекта.

    Returns:
        Path: Путь к корневому каталогу, если найден, иначе путь к каталогу, где расположен скрипт.
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


# Получение корневого каталога проекта
__root__ = set_project_root()
"""
Path: Путь к корневому каталогу проекта.
"""

from src import gs  #  Импорт gs

settings: dict | None = None
try:
    #  Загрузка настроек из файла settings.json
    settings_file_path = gs.path.root / 'src' / 'settings.json'
    settings = j_loads(settings_file_path)
except (FileNotFoundError, Exception) as ex:
     # Логирование ошибки при загрузке настроек
    logger.error(f'Ошибка при загрузке файла настроек: {settings_file_path}', exc_info=ex)
    ...

doc_string: str | None = None
try:
    #  Загрузка документации из файла README.MD
    doc_file_path = gs.path.root / 'src' / 'README.MD'
    with open(doc_file_path, 'r', encoding='utf-8') as doc_file:
        doc_string = doc_file.read()
except (FileNotFoundError, Exception) as ex:
    # Логирование ошибки при загрузке документации
    logger.error(f'Ошибка при загрузке файла документации: {doc_file_path}', exc_info=ex)
    ...

__project_name__: str = settings.get('project_name', 'hypotez') if settings else 'hypotez'
"""str: Название проекта."""

__version__: str = settings.get('version', '') if settings else ''
"""str: Версия проекта."""

__doc__: str = doc_string if doc_string else ''
"""str: Строка документации проекта."""

__details__: str = ''
"""str: Дополнительная информация о проекте."""

__author__: str = settings.get('author', '') if settings else ''
"""str: Автор проекта."""

__copyright__: str = settings.get('copyrihgnt', '') if settings else ''
"""str: Информация об авторских правах проекта."""

__cofee__: str = settings.get('cofee', 'Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69') if settings else 'Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69'
"""str: Призыв к поддержке разработчика."""
```