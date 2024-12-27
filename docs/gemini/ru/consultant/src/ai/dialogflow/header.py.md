# Анализ кода модуля `header.py`

**Качество кода**
8
-  Плюсы
    - Код содержит docstring для модуля.
    - Используется `pathlib` для работы с путями.
    - Код старается обрабатывать исключения при чтении файлов.
    - Определены основные метаданные проекта, такие как имя, версия, автор и т.д.
-  Минусы
    - Не используется `j_loads` или `j_loads_ns` для загрузки JSON.
    - Обработка исключений использует многоточие `...`, что не является информативным.
    - Отсутствует логирование ошибок.
    - Комментарии не соответствуют формату RST.
    - Отсутствуют докстринги для некоторых переменных.
    - Некоторые имена переменных не соответствуют стандарту.

**Рекомендации по улучшению**
1.  Замените `json.load` на `j_loads` или `j_loads_ns` из `src.utils.jjson`.
2.  Добавьте логирование ошибок с помощью `logger.error` вместо `...` в блоках `try-except`.
3.  Преобразуйте все комментарии в формат RST.
4.  Добавьте docstring для переменных `settings`, `doc_str`, `__project_name__`, `__version__`, `__doc__`, `__details__`, `__author__`, `__copyright__`, `__cofee__`.
5.  Переименуйте `settings_file` на более конкретное название, например `file_descriptor`.
6.  Добавьте комментарии в формате RST к каждой функции, переменной и классу.
7.  Удалите неиспользуемые импорты.
8.  Добавьте type hints.

**Оптимизированный код**

```python
"""
Модуль для определения общих параметров и настроек проекта.
================================================================

Этот модуль определяет корень проекта, загружает настройки из файла `settings.json`
и извлекает метаданные проекта, такие как имя, версия, автор и т.д.

Пример использования
--------------------

Пример использования::

    import src.ai.dialogflow.header as header

    print(header.__project_name__)
    print(header.__version__)
    print(header.__author__)
"""

import sys
from pathlib import Path
from typing import Tuple, Optional
# from packaging.version import Version # не используется
from src.utils.jjson import j_loads
from src.logger.logger import logger
from src import gs


MODE: str = 'dev'
"""Режим работы приложения."""



def set_project_root(marker_files: Tuple[str, ...] = ('pyproject.toml', 'requirements.txt', '.git')) -> Path:
    """
    Определяет корневой каталог проекта.

    Функция ищет корневой каталог проекта, начиная с каталога текущего файла,
    проверяя наличие файлов-маркеров в родительских каталогах.

    :param marker_files: Кортеж с именами файлов или каталогов, которые идентифицируют корень проекта.
    :type marker_files: tuple
    :return: Путь к корневому каталогу проекта.
    :rtype: pathlib.Path
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
"""`Path`: Путь к корневому каталогу проекта."""

settings: Optional[dict] = None
"""Словарь с настройками проекта, загруженный из `settings.json`."""
try:
    # код загружает настройки из файла settings.json
    with open(gs.path.root / 'src' /  'settings.json', 'r') as file_descriptor:
        settings = j_loads(file_descriptor)
except FileNotFoundError as e:
    # Логирование ошибки, если файл не найден
    logger.error('Файл settings.json не найден', exc_info=e)
except Exception as e:
    # Логирование ошибки при декодировании JSON
    logger.error('Ошибка декодирования JSON в файле settings.json', exc_info=e)

doc_str: Optional[str] = None
"""Строка с документацией проекта, загруженная из `README.MD`."""
try:
    # код загружает документацию из файла README.MD
    with open(gs.path.root / 'src' /  'README.MD', 'r') as file_descriptor:
        doc_str = file_descriptor.read()
except FileNotFoundError as e:
    # Логирование ошибки, если файл не найден
    logger.error('Файл README.MD не найден', exc_info=e)
except Exception as e:
    # Логирование ошибки при чтении файла
    logger.error('Ошибка чтения файла README.MD', exc_info=e)
    

__project_name__: str = settings.get("project_name", 'hypotez') if settings else 'hypotez'
"""`str`: Имя проекта."""
__version__: str = settings.get("version", '') if settings else ''
"""`str`: Версия проекта."""
__doc__: str = doc_str if doc_str else ''
"""`str`: Документация проекта."""
__details__: str = ''
"""`str`: Детальная информация о проекте."""
__author__: str = settings.get("author", '') if settings else ''
"""`str`: Автор проекта."""
__copyright__: str = settings.get("copyrihgnt", '') if settings else ''
"""`str`: Информация об авторских правах."""
__cofee__: str = settings.get("cofee", "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69") if settings else "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69"
"""`str`: Призыв к поддержке разработчика."""
```