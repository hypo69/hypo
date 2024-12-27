# Анализ кода модуля `header.py`

**Качество кода**
8
-  Плюсы
    -  Код выполняет свою основную задачу - устанавливает корневую директорию проекта и загружает настройки.
    -  Используется `pathlib` для работы с путями, что является хорошей практикой.
    -  Есть обработка ошибок при загрузке файлов настроек, хотя и не полная.
    -  Используются `__` для приватных переменных.
 -  Минусы
    -  Не используется `j_loads` или `j_loads_ns` из `src.utils.jjson` для чтения `json` файлов.
    -  Отсутствует логирование ошибок.
    -  Использование `...` как заглушки не является оптимальным.
    -  Неполная документация функций, переменных и модуля в стиле reStructuredText (RST).
    -  Смешанный стиль наименования переменных (например `__root__` и `settings`).
    -  Не все переменные аннотированы типами.
    -  Не все импорты необходимы.
    -  Избыточный `try-except` для чтения файла README.

**Рекомендации по улучшению**

1.  Использовать `j_loads` из `src.utils.jjson` для загрузки `json` файлов.
2.  Добавить логирование ошибок с помощью `from src.logger.logger import logger`.
3.  Заменить `...` на логирование и обработку ошибок.
4.  Добавить полную документацию в стиле reStructuredText (RST) для модуля, функций и переменных.
5.  Привести к единообразному стилю наименование переменных (например `project_root_path`).
6.  Добавить аннотацию типов для переменных, где это возможно.
7.  Удалить ненужные импорты.
8.  Избавиться от избыточных `try-except` блоков, используя логирование.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
"""
Модуль для определения и настройки окружения проекта.
===================================================

Этот модуль устанавливает корневую директорию проекта, загружает настройки из файла
`settings.json`, и извлекает информацию из `README.MD`, определяет основные параметры проекта,
такие как название, версия, автор и т.д.

Использование
-------------
Для использования, просто импортируйте этот модуль.

Пример:
    
    import src.fast_api.header as header

    print(header.__project_name__)
"""

import sys
from pathlib import Path
from packaging.version import Version
from src.utils.jjson import j_loads
from src.logger.logger import logger

MODE = 'dev'


def set_project_root(marker_files: tuple[str, ...] = ('pyproject.toml', 'requirements.txt', '.git')) -> Path:
    """
    Определяет корневой каталог проекта.

    Функция ищет корневой каталог проекта, начиная с директории текущего файла и
    продвигаясь вверх по дереву каталогов, пока не найдет каталог, содержащий
    один из указанных файлов-маркеров.

    :param marker_files: Кортеж с именами файлов или директорий, которые
                         идентифицируют корневой каталог проекта.
    :return: Объект Path, представляющий корневой каталог проекта.
             Возвращает каталог, где расположен скрипт, если корневой каталог не найден.
    """
    project_root_path: Path
    current_path: Path = Path(__file__).resolve().parent
    project_root_path = current_path
    for parent in [current_path] + list(current_path.parents):
        if any((parent / marker).exists() for marker in marker_files):
            project_root_path = parent
            break
    if project_root_path not in sys.path:
        sys.path.insert(0, str(project_root_path))
    return project_root_path


# Устанавливаем корневую директорию проекта
project_root_path: Path = set_project_root()
"""project_root_path (Path): Путь к корневой директории проекта."""

from src import gs

settings: dict | None = None
try:
    # Читаем настройки из файла settings.json с использованием j_loads
    with open(gs.path.root / 'src' / 'settings.json', 'r', encoding='utf-8') as settings_file:
        settings = j_loads(settings_file)
except FileNotFoundError:
    # Логируем ошибку если файл не найден
    logger.error(f'Файл settings.json не найден по пути: {gs.path.root / "src" / "settings.json"}')
except Exception as ex:
    # Логируем любую другую ошибку
    logger.error(f'Ошибка при чтении файла settings.json: {ex}')


doc_str: str | None = None
try:
    # Читаем файл README.MD
    with open(gs.path.root / 'src' / 'README.MD', 'r', encoding='utf-8') as readme_file:
        doc_str = readme_file.read()
except FileNotFoundError:
    # Логируем ошибку если файл не найден
    logger.error(f'Файл README.MD не найден по пути: {gs.path.root / "src" / "README.MD"}')
except Exception as ex:
    # Логируем любую другую ошибку
    logger.error(f'Ошибка при чтении файла README.MD: {ex}')

__project_name__: str = settings.get("project_name", 'hypotez') if settings else 'hypotez'
"""__project_name__ (str): Название проекта, по умолчанию 'hypotez'."""
__version__: str = settings.get("version", '') if settings else ''
"""__version__ (str): Версия проекта, по умолчанию ''. """
__doc__: str = doc_str if doc_str else ''
"""__doc__ (str): Содержимое README.MD, по умолчанию ''. """
__details__: str = ''
"""__details__ (str): Дополнительная информация о проекте, по умолчанию ''. """
__author__: str = settings.get("author", '') if settings else ''
"""__author__ (str): Автор проекта, по умолчанию ''. """
__copyright__: str = settings.get("copyrihgnt", '') if settings else ''
"""__copyright__ (str): Информация об авторских правах, по умолчанию ''. """
__cofee__: str = settings.get("cofee", "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69")  if settings  else "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69"
"""__cofee__ (str): Сообщение о поддержке разработчика, по умолчанию ссылка на Boosty."""
```