# Анализ кода модуля `header.py`

**Качество кода**
8
-  Плюсы
    - Код выполняет свою основную задачу - определение корневой директории проекта.
    - Использует `pathlib` для работы с путями, что является хорошей практикой.
    - Документация в формате reStructuredText (RST) присутствует в начале модуля.
    - Присутствует обработка ошибок при загрузке `settings.json` и `README.md`.
-  Минусы
    - Не хватает импорта `logger` из `src.logger.logger`.
    - Используется стандартный `json.load` вместо `j_loads` или `j_loads_ns` из `src.utils.jjson`.
    -  Обработка ошибок `FileNotFoundError` и `json.JSONDecodeError` в блоках `try-except` нелогична с точки зрения логгирования, нужно использовать `logger.error`.
    - Отсутствуют docstring для переменных и констант, определенных в модуле (например `MODE`, `settings`, `__root__`).
    - Отсутствует docstring для `__project_name__`, `__version__`, `__doc__` и т.д.
    - Не все комментарии к коду в стиле RST.
    - `__cofee__` опечатка в переменной `__copyright__`

**Рекомендации по улучшению**

1. Добавить импорт `from src.logger.logger import logger`.
2. Использовать `j_loads` или `j_loads_ns` из `src.utils.jjson` для загрузки `settings.json`.
3. Заменить стандартные блоки `try-except` на `logger.error` для обработки ошибок.
4. Добавить docstring для всех переменных и констант.
5. Переписать комментарии в стиле RST.
6. Исправить опечатку `copyrihgnt` на `copyright`
7. Добавить RST описание для константы `MODE`

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
Модуль для определения корневого пути проекта.
=========================================================================================

Этот модуль определяет корневой путь проекта и загружает основные настройки.
Все импорты строятся относительно этого пути.

:platform: Windows, Unix
:synopsis: Модуль определяющий корневой путь к проекту. Все импорты строятся относительно этого пути.
:TODO: В дальнейшем перенести в системную переменную
"""
import sys
# добавляем импорт j_loads из src.utils.jjson
from src.utils.jjson import j_loads
# добавляем импорт logger из src.logger.logger
from src.logger.logger import logger
from pathlib import Path
from packaging.version import Version

#: Режим работы приложения.
MODE = 'dev'


def set_project_root(marker_files: tuple = ('pyproject.toml', 'requirements.txt', '.git')) -> Path:
    """
    Определяет корневой каталог проекта.

    Функция ищет корневой каталог проекта, начиная с каталога текущего файла,
    просматривая родительские каталоги и останавливаясь на первом каталоге,
    содержащем любой из файлов-маркеров.

    :param marker_files: Кортеж имен файлов или каталогов, идентифицирующих корень проекта.
    :type marker_files: tuple
    :return: Путь к корневому каталогу, если он найден, иначе путь к каталогу, где расположен скрипт.
    :rtype: Path
    """
    __root__: Path
    current_path: Path = Path(__file__).resolve().parent
    __root__ = current_path
    # Цикл перебирает текущий каталог и его родительские каталоги
    for parent in [current_path] + list(current_path.parents):
        # проверяет наличие одного из файлов маркеров в текущем родительском каталоге
        if any((parent / marker).exists() for marker in marker_files):
            __root__ = parent
            break
    #  Если корневой каталог еще не добавлен в sys.path, то добавляет его
    if __root__ not in sys.path:
        sys.path.insert(0, str(__root__))
    return __root__


# Получение корневой директории проекта
__root__ = set_project_root()
#: Путь к корневой директории проекта.
#: :type: Path
#:
from src import gs

settings: dict = None
# обработка загрузки файла settings.json
try:
    # используем j_loads для загрузки json
    with open(gs.path.root / 'src' / 'settings.json', 'r') as settings_file:
        settings = j_loads(settings_file)
except FileNotFoundError as ex:
    # Логируем ошибку если файл не найден
    logger.error(f'Файл настроек не найден {ex}', exc_info=True)
    ...
except Exception as ex:
    # Логируем ошибку декодирования json
    logger.error(f'Ошибка декодирования JSON в settings.json {ex}', exc_info=True)
    ...

doc_str: str = None
# обработка загрузки файла README.md
try:
    with open(gs.path.root / 'src' / 'README.MD', 'r') as settings_file:
        doc_str = settings_file.read()
except FileNotFoundError as ex:
    # Логируем ошибку если файл не найден
    logger.error(f'Файл README.MD не найден {ex}', exc_info=True)
    ...
except Exception as ex:
    # Логируем ошибку чтения файла
    logger.error(f'Ошибка чтения файла README.MD {ex}', exc_info=True)
    ...


#: Название проекта.
__project_name__ = settings.get("project_name", 'hypotez') if settings else 'hypotez'
#: Версия проекта.
__version__: str = settings.get("version", '') if settings else ''
#: Документация проекта.
__doc__: str = doc_str if doc_str else ''
#: Дополнительная информация о проекте.
__details__: str = ''
#: Автор проекта.
__author__: str = settings.get("author", '') if settings else ''
#: Авторские права проекта.
__copyright__: str = settings.get("copyright", '') if settings else ''
#: Сообщение для поддержки разработчика.
__cofee__: str = settings.get("cofee", "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69") if settings else "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69"
```