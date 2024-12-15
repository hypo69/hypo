# Анализ кода модуля header.py

**Качество кода**
8
- Плюсы
    - Код хорошо структурирован и читабелен.
    - Используется функция `set_project_root` для определения корневой директории проекта, что является хорошей практикой.
    - Наличие констант для имени проекта, версии, автора и т.д.
    - Используется `pathlib` для работы с путями, что делает код более кроссплатформенным.
    - Документирование переменных на уровне модуля.
- Минусы
    - Отсутствие `j_loads` или `j_loads_ns` для загрузки `settings.json`.
    - Отсутствует описание модуля в формате reStructuredText.
    - Обработка ошибок при чтении `settings.json` и `README.MD` не использует логирование.
    - Отсутствуют docstring для констант.
    - Не все импорты используются (например, `sys`).

**Рекомендации по улучшению**

1.  Добавить описание модуля в формате reStructuredText.
2.  Использовать `j_loads` или `j_loads_ns` из `src.utils.jjson` для загрузки `settings.json`.
3.  Добавить логирование ошибок при загрузке `settings.json` и `README.MD` с использованием `logger.error`.
4.  Добавить docstring для констант, описывающие их назначение.
5.  Удалить неиспользуемые импорты (если таковые есть).
6.  Переписать комментарии в формате reStructuredText для функций.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
Модуль для определения настроек проекта и метаданных.
========================================================

Этот модуль предназначен для:
  - Определения корневой директории проекта.
  - Загрузки настроек из `settings.json`.
  - Извлечения метаданных проекта, таких как имя, версия, автор и т.д.

Основные функции:
    - set_project_root: Находит корневую директорию проекта.

Переменные:
    - __project_name__: Имя проекта.
    - __version__: Версия проекта.
    - __doc__: Строка документации проекта из README.MD
    - __details__: Детали проекта.
    - __author__: Автор проекта.
    - __copyright__: Авторские права.
    - __cofee__: Сообщение с призывом угостить разработчика кофе.
"""
import sys
from pathlib import Path
from packaging.version import Version

from src.utils.jjson import j_loads
from src.logger.logger import logger


MODE = 'dev'
"""Режим работы приложения: dev, test, prod."""

def set_project_root(marker_files: tuple =('pyproject.toml', 'requirements.txt', '.git')) -> Path:
    """
    Находит корневую директорию проекта, начиная с директории текущего файла.

    Поиск идет вверх по дереву каталогов и останавливается в первой директории,
    содержащей любой из файлов-маркеров.

    :param marker_files: Кортеж имен файлов или каталогов, идентифицирующих корень проекта.
    :type marker_files: tuple
    :return: Путь к корневой директории, если найдена, иначе директория, где расположен скрипт.
    :rtype: Path
    """
    __root__:Path
    current_path:Path = Path(__file__).resolve().parent
    __root__ = current_path
    # код проверяет наличие одного из маркеров в текущей директории и ее родительских директориях
    for parent in [current_path] + list(current_path.parents):
        if any((parent / marker).exists() for marker in marker_files):
            __root__ = parent
            break
    # код добавляет корневую директорию в sys.path, если ее там нет
    if __root__ not in sys.path:
        sys.path.insert(0, str(__root__))
    return __root__


# Get the root directory of the project
__root__: Path = set_project_root()
"""Path: Путь к корневой директории проекта."""

from src import gs

settings: dict = None
# код загружает настройки из файла settings.json или выдает ошибку
try:
    with open(gs.path.root / 'src' /  'settings.json', 'r') as settings_file:
        settings = j_loads(settings_file)
except (FileNotFoundError, json.JSONDecodeError) as e:
    logger.error(f'Ошибка при загрузке файла настроек: {e}')
    ...

doc_str: str = None
# код загружает контент файла README.MD
try:
    with open(gs.path.root / 'src' /  'README.MD', 'r') as settings_file:
        doc_str = settings_file.read()
except (FileNotFoundError, json.JSONDecodeError) as e:
     logger.error(f'Ошибка при загрузке файла README.MD: {e}')
     ...

__project_name__: str = settings.get("project_name", 'hypotez') if settings  else 'hypotez'
"""str: Имя проекта."""
__version__: str = settings.get("version", '')  if settings  else ''
"""str: Версия проекта."""
__doc__: str = doc_str if doc_str else ''
"""str: Описание проекта."""
__details__: str = ''
"""str: Детали проекта."""
__author__: str = settings.get("author", '')  if settings  else ''
"""str: Автор проекта."""
__copyright__: str = settings.get("copyrihgnt", '')  if settings  else ''
"""str: Авторские права проекта."""
__cofee__: str = settings.get("cofee", "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69")  if settings  else "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69"
"""str: Сообщение с призывом угостить разработчика кофе."""
```