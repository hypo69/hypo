# Анализ кода модуля `header.py`

**Качество кода**
7
-  Плюсы
    -   Код выполняет свою основную задачу по определению корневой директории проекта и загрузке настроек.
    -   Используется `pathlib.Path` для работы с путями, что является хорошей практикой.
    -   Есть базовая обработка исключений при загрузке файлов настроек и документации.
    -   Код хорошо структурирован и читаем.
    -   Наличие docstring для функции `set_project_root`
-  Минусы
    -   Отсутствует reStructuredText (RST) документация для модуля, глобальных переменных.
    -   Используется стандартный `json.load` вместо `j_loads` или `j_loads_ns`.
    -   Не производится логирование ошибок в блоках `try-except`.
    -   Отсутствует импорт logger
    -   Присутствуют `...` как точки остановки.
    -   Некоторые переменные именованы с использованием "__", например,  `__root__`.
    -   Загрузка `README.MD` не обрабатывает `JSONDecodeError`, хотя файл не является json.

**Рекомендации по улучшению**

1.  Добавить RST документацию для модуля и глобальных переменных.
2.  Использовать `j_loads` из `src.utils.jjson` для загрузки `settings.json`.
3.  Использовать `logger.error` для логирования ошибок в блоках `try-except`.
4.  Избавиться от `...` и добавить логирование.
5.  Исключить использование  `__` в названии переменных `__root__`, `__project_name__`.
6.  Исправить импорты и привести к единому стандарту.
7.  Убрать лишние комментарии, если они дублируют функциональность кода.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
Модуль для определения корневого пути проекта.
=========================================================================================

Модуль определяет корневой путь к проекту и загружает основные настройки и документацию.
Все импорты в проекте строятся относительно этого пути.

:TODO: В дальнейшем перенести в системную переменную
"""

import sys
from pathlib import Path
#from json import load #  `json.load` использовать нельзя!
from packaging.version import Version

from src.utils.jjson import j_loads
from src.logger.logger import logger

MODE = 'dev'
"""Режим работы приложения (dev, prod)"""

def set_project_root(marker_files: tuple = ('pyproject.toml', 'requirements.txt', '.git')) -> Path:
    """
    Определение корневой директории проекта.

    Функция ищет корневую директорию проекта, начиная с директории текущего файла,
    двигаясь вверх по дереву каталогов до тех пор, пока не найдет каталог,
    содержащий один из файлов-маркеров.

    :param marker_files: Кортеж имен файлов или каталогов, которые идентифицируют корень проекта.
    :type marker_files: tuple
    :return: Путь к корневой директории проекта. Если корень не найден, возвращает директорию, где расположен скрипт.
    :rtype: Path
    """
    root_path: Path
    current_path: Path = Path(__file__).resolve().parent
    root_path = current_path
    for parent in [current_path] + list(current_path.parents):
        if any((parent / marker).exists() for marker in marker_files):
            root_path = parent
            break
    if root_path not in sys.path:
        sys.path.insert(0, str(root_path))
    return root_path

# Получение корневой директории проекта
root_path:Path = set_project_root()
"""Путь к корневой директории проекта."""

from src import gs

settings: dict = None
"""Словарь с настройками проекта."""

try:
    #  Чтение файла настроек settings.json с помощью j_loads
    with open(gs.path.root / 'src' /  'settings.json', 'r') as settings_file:
        settings = j_loads(settings_file)
except FileNotFoundError as e:
    #  Логирование ошибки, если файл не найден
    logger.error(f'Файл настроек не найден {e}')
except Exception as e:
    # Логирование ошибки, если не удалось прочитать файл настроек
    logger.error(f'Ошибка при чтении файла настроек {e}')

doc_str: str = None
"""Строка с содержимым файла README.MD."""

try:
    #  Чтение файла README.MD
    with open(gs.path.root / 'src' /  'README.MD', 'r') as settings_file:
        doc_str = settings_file.read()
except FileNotFoundError as e:
    #  Логирование ошибки, если файл не найден
    logger.error(f'Файл README.MD не найден {e}')
except Exception as e:
     # Логирование ошибки, если не удалось прочитать файл README.MD
    logger.error(f'Ошибка при чтении файла README.MD {e}')

project_name: str = settings.get("project_name", 'hypotez') if settings  else 'hypotez'
"""Имя проекта."""
version: str = settings.get("version", '')  if settings  else ''
"""Версия проекта."""
doc: str = doc_str if doc_str else ''
"""Строка документации проекта."""
details: str = ''
"""Детали проекта."""
author: str = settings.get("author", '')  if settings  else ''
"""Автор проекта."""
copyright: str = settings.get("copyrihgnt", '')  if settings  else ''
"""Авторские права проекта."""
cofee: str = settings.get("cofee", "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69")  if settings  else "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69"
"""Ссылка для поддержки проекта."""
```