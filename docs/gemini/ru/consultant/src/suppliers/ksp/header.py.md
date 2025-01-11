# Анализ кода модуля `header.py`

**Качество кода: 7/10**
- Плюсы:
    -   Функция `set_project_root` хорошо документирована и выполняет свою задачу по определению корневой директории проекта.
    -   Использование `pathlib.Path` для работы с путями.
    -   Код читаемый и логически структурирован.
- Минусы:
    -   Используется стандартный `json.load` вместо `j_loads` или `j_loads_ns` из `src.utils.jjson`.
    -   Отсутствует импорт `logger` из `src.logger.logger`.
    -   Обработка исключений `FileNotFoundError` и `json.JSONDecodeError` не использует `logger.error`.
    -   В комментариях после `#` есть общие фразы, вместо конкретного описания кода.
    -   Неполная документация модуля.
    -   Необходимо унифицировать использование кавычек (только одинарные в коде, двойные в выводе).

**Рекомендации по улучшению**

1.  Использовать `j_loads` или `j_loads_ns` из `src.utils.jjson` для чтения файлов `settings.json`.
2.  Импортировать `logger` из `src.logger.logger` для логирования ошибок.
3.  Заменить стандартный `try-except` на обработку ошибок с использованием `logger.error`.
4.  Добавить документацию модуля, функций и переменных в формате RST.
5.  Унифицировать использование кавычек в соответствии с инструкциями.
6.  Уточнить комментарии после `#` для лучшего понимания кода.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
#! venv/bin/python/python3.12
"""
Модуль для определения корневой директории проекта и загрузки основных настроек.
=========================================================================================

Модуль содержит функцию :func:`set_project_root` для определения корневой директории проекта,
а также загружает основные настройки из файла `settings.json` и описание из `README.md`
для использования в проекте.

Пример использования
--------------------

.. code-block:: python

    from src.suppliers.ksp.header import __project_name__, __version__, __doc__

    print(f'Project Name: {__project_name__}')
    print(f'Version: {__version__}')
    print(f'Documentation: {__doc__}')
"""
import sys
from pathlib import Path
from packaging.version import Version
#  Импорт j_loads для загрузки json
from src.utils.jjson import j_loads
#  Импорт logger для логирования ошибок
from src.logger.logger import logger


def set_project_root(marker_files: tuple = ('__root__', '.git')) -> Path:
    """
    Находит корневую директорию проекта, начиная с директории текущего файла,
    поиском вверх и останавливаясь на первой директории, содержащей любой из файлов-маркеров.

    :param marker_files:  Кортеж с именами файлов или директорий для идентификации корня проекта.
    :type marker_files: tuple
    :return: Путь к корневой директории, если найден, иначе директория, где расположен скрипт.
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
"""__root__ (Path): Путь к корневой директории проекта"""

from src import gs

settings: dict = None
#  Попытка открыть и прочитать файл настроек settings.json
try:
    with open(gs.path.root / 'src' / 'settings.json', 'r') as settings_file:
        # Используем j_loads для чтения файла
        settings = j_loads(settings_file)
except (FileNotFoundError, json.JSONDecodeError) as ex:
    # Логируем ошибку при открытии или чтении файла
    logger.error('Ошибка при загрузке файла настроек', ex)
    ...

doc_str: str = None
#  Попытка открыть и прочитать файл README.MD
try:
    with open(gs.path.root / 'src' / 'README.MD', 'r') as settings_file:
        doc_str = settings_file.read()
except (FileNotFoundError, json.JSONDecodeError) as ex:
    #  Логируем ошибку при открытии или чтении файла
    logger.error('Ошибка при загрузке файла README.MD', ex)
    ...

# Имя проекта, версия и другие переменные, получаемые из настроек или значения по умолчанию
__project_name__ = settings.get('project_name', 'hypotez') if settings else 'hypotez'
"""__project_name__ (str): Имя проекта."""
__version__: str = settings.get('version', '') if settings else ''
"""__version__ (str): Версия проекта."""
__doc__: str = doc_str if doc_str else ''
"""__doc__ (str): Документация проекта."""
__details__: str = ''
"""__details__ (str): Детали проекта."""
__author__: str = settings.get('author', '') if settings else ''
"""__author__ (str): Автор проекта."""
__copyright__: str = settings.get('copyrihgnt', '') if settings else ''
"""__copyright__ (str): Информация об авторских правах."""
__cofee__: str = settings.get('cofee', 'Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69') if settings else 'Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69'
"""__cofee__ (str): Ссылка на поддержку разработчика."""
```