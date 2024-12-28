## Анализ кода модуля `header.py`

**Качество кода**
9
-  Плюсы
    - Код хорошо структурирован, использует `pathlib` для работы с путями.
    - Присутствует обработка ошибок при загрузке `settings.json` и `README.MD`.
    - Используются константы для хранения имени проекта, версии и прочей информации.
    -  Имеется функция для определения корневой директории проекта.
    - Код соответствует PEP 8.
-  Минусы
    - Не используется `j_loads` или `j_loads_ns` из `src.utils.jjson` для чтения файлов.
    - Отсутствуют docstring для модуля, переменных, констант и т.д.
    - Не используется `logger` для логирования ошибок.
    - Присутствуют многословные и не информативные комментарии.
    - Использование `...` вместо более информативной обработки ошибок.
    - Не соответствует стандарту reStructuredText (RST).

**Рекомендации по улучшению**

1.  Использовать `j_loads` из `src.utils.jjson` вместо `json.load` для чтения файлов.
2.  Добавить docstring в формате RST для модуля, функций и переменных.
3.  Использовать `logger` для логирования ошибок вместо `...`.
4.  Убрать излишние комментарии и переформулировать их в соответствии с RST.
5.  Использовать `sys.exit(1)` при критических ошибках, когда не удаётся загрузить важные файлы.
6.  Устранить `__root__:Path` в `set_project_root`.
7.  Проверить и добавить отсутствующие импорты.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
Модуль для определения корневой директории проекта и загрузки основных настроек.
==============================================================================

Этот модуль предназначен для автоматического определения корневой директории проекта,
загрузки конфигурационных файлов (`settings.json`) и `README.MD`.

Модуль обеспечивает доступ к основным параметрам проекта, таким как имя, версия, авторские права.

Пример использования
--------------------

Пример использования переменных модуля:

.. code-block:: python

    print(f'Имя проекта: {__project_name__}')
    print(f'Версия проекта: {__version__}')
"""

import sys
from pathlib import Path
from packaging.version import Version

#  Импортируем необходимые функции из src.utils.jjson
from src.utils.jjson import j_loads
# Импортируем logger для логирования ошибок
from src.logger.logger import logger

#: Режим работы приложения (dev или prod).


def set_project_root(marker_files: tuple = ('pyproject.toml', 'requirements.txt', '.git')) -> Path:
    """
    Определяет корневую директорию проекта, начиная с директории текущего файла.
     
    Поиск идет вверх по дереву каталогов до первого каталога, содержащего любой из файлов-маркеров.

    :param marker_files: Кортеж имен файлов или директорий для идентификации корневой директории проекта.
    :type marker_files: tuple
    :return: Путь к корневой директории, если найдена. В противном случае возвращается путь к директории, где находится скрипт.
    :rtype: Path
    """
    current_path: Path = Path(__file__).resolve().parent
    root: Path = current_path
    for parent in [current_path] + list(current_path.parents):
        if any((parent / marker).exists() for marker in marker_files):
            root = parent
            break
    if root not in sys.path:
        sys.path.insert(0, str(root))
    return root


# Вызываем функцию для определения корневой директории проекта
__root__: Path = set_project_root()
"""Path: Путь к корневой директории проекта"""

from src import gs

settings: dict = None
try:
    #  Используем j_loads для загрузки данных из settings.json
    with open(gs.path.root / 'src' / 'settings.json', 'r', encoding='utf-8') as settings_file:
        settings = j_loads(settings_file)
except FileNotFoundError:
    #  Логируем ошибку, если файл settings.json не найден
    logger.error(f'Файл settings.json не найден по пути: {gs.path.root / "src" / "settings.json"}')
    sys.exit(1)
except Exception as ex:
    # Логируем любую другую ошибку, возникшую при чтении файла
    logger.error(f'Ошибка при чтении файла settings.json: {ex}')
    sys.exit(1)

doc_str: str = None
try:
    #  Пытаемся открыть и прочитать файл README.MD
    with open(gs.path.root / 'src' / 'README.MD', 'r', encoding='utf-8') as readme_file:
         doc_str = readme_file.read()
except FileNotFoundError:
     #  Логируем ошибку, если файл README.MD не найден
    logger.error(f'Файл README.MD не найден по пути: {gs.path.root / "src" / "README.MD"}')
    doc_str = ''
except Exception as ex:
    # Логируем любую другую ошибку, возникшую при чтении файла
    logger.error(f'Ошибка при чтении файла README.MD: {ex}')
    doc_str = ''


#  Получаем имя проекта из настроек или устанавливаем значение по умолчанию
__project_name__: str = settings.get("project_name", 'hypotez') if settings else 'hypotez'
"""str: Имя проекта."""
#  Получаем версию проекта из настроек или устанавливаем значение по умолчанию
__version__: str = settings.get("version", '') if settings else ''
"""str: Версия проекта."""
#  Получаем содержимое файла README.MD или устанавливаем значение по умолчанию
__doc__: str = doc_str if doc_str else ''
"""str: Содержимое README.MD"""
#  Инициализируем переменную для подробностей проекта (пока пустая строка)
__details__: str = ''
"""str: Детали проекта (пока не используется)."""
#  Получаем имя автора проекта из настроек или устанавливаем значение по умолчанию
__author__: str = settings.get("author", '') if settings else ''
"""str: Автор проекта."""
#  Получаем информацию об авторских правах из настроек или устанавливаем значение по умолчанию
__copyright__: str = settings.get("copyrihgnt", '') if settings else ''
"""str: Информация об авторских правах."""
#  Получаем текст о поддержке проекта из настроек или устанавливаем значение по умолчанию
__cofee__: str = settings.get("cofee", "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69") if settings else "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69"
"""str: Текст о поддержке проекта."""
```