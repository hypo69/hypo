# Анализ кода модуля `header.py`

**Качество кода**
    
    -   **Соответствие требованиям по оформлению кода: 7/10**
    -   **Плюсы**
        *   Код структурирован и выполняет основную задачу: определение корневой директории проекта и загрузку настроек.
        *   Используется `pathlib` для работы с путями.
        *   Есть обработка исключений `FileNotFoundError` и `json.JSONDecodeError` при загрузке настроек.
    -   **Минусы**
        *   Отсутствуют docstring для модуля.
        *   Не используется `j_loads` или `j_loads_ns` для загрузки JSON, как указано в требованиях.
        *   Используются стандартные `try-except` блоки.
        *   Переменные не документированы в формате reStructuredText.
        *   Не все импорты используются.
        *   Наличие magic comments (`# -*- coding: utf-8 -*-`, `#! venv/Scripts/python.exe`, `#! venv/bin/python/python3.12`) в начале файла.

**Рекомендации по улучшению**

1.  **Документация:** Добавить docstring для модуля в формате reStructuredText (RST).
2.  **Загрузка JSON:** Использовать `j_loads` или `j_loads_ns` для загрузки JSON из файла настроек.
3.  **Логирование ошибок:** Заменить стандартные `try-except` на использование `logger.error` для обработки ошибок.
4.  **Docstring:** Добавить docstring в формате RST для всех функций и переменных.
5.  **Импорты:** Удалить неиспользуемые импорты, добавить недостающие, привести в соответствие с другими файлами.
6.  **Magic comments:** Удалить magic comments.
7.  **Переменные:** Добавить документацию для всех переменных, включая глобальные, в формате RST.
8.  **Форматирование:** Привести код в соответствие со стандартом PEP8.

**Оптимизированный код**

```python
"""
Модуль для настройки окружения и загрузки конфигурации проекта.
==============================================================

Этот модуль определяет корневую директорию проекта, загружает настройки из `settings.json`
и `README.MD`, а также предоставляет основные переменные проекта, такие как имя, версия,
описание и автор.

Пример использования
--------------------

Чтобы получить корневую директорию проекта, вызовите функцию `set_project_root`.
После этого вы можете использовать переменные, такие как `__project_name__`,
`__version__`, `__doc__`, и другие для доступа к информации о проекте.

.. code-block:: python

    from src.endpoints.header import __project_name__, __version__, __doc__

    print(f"Project name: {__project_name__}")
    print(f"Version: {__version__}")
    print(f"Documentation: {__doc__}")
"""
import sys
from pathlib import Path

from src.utils.jjson import j_loads
from src.logger.logger import logger
from src import gs

MODE = 'dev'
"""
    Режим работы приложения (dev или prod).
    
    :type: str
"""


def set_project_root(marker_files: tuple = ('pyproject.toml', 'requirements.txt', '.git')) -> Path:
    """
    Определяет корневой каталог проекта.

    Код осуществляет поиск корневого каталога проекта, начиная с каталога текущего файла,
    двигаясь вверх по иерархии каталогов и останавливаясь на первом каталоге, содержащем
    один из файлов-маркеров.

    :param marker_files: Список файлов-маркеров, указывающих на корневой каталог.
    :type marker_files: tuple
    :return: Путь к корневому каталогу, если найден, или к каталогу скрипта.
    :rtype: Path
    """
    current_path: Path = Path(__file__).resolve().parent
    __root__: Path = current_path

    for parent in [current_path] + list(current_path.parents):
        if any((parent / marker).exists() for marker in marker_files):
            __root__ = parent
            break
    if __root__ not in sys.path:
        sys.path.insert(0, str(__root__))
    return __root__


# Код инициализирует корневую директорию проекта
__root__: Path = set_project_root()
"""
    Корневой каталог проекта.

    :type: Path
"""

settings: dict = None
"""
    Словарь с настройками проекта, загруженный из `settings.json`.

    :type: dict or None
"""
try:
    # Код загружает настройки из файла 'settings.json'
    with open(gs.path.root / 'src' / 'settings.json', 'r') as settings_file:
        settings = j_loads(settings_file)
except FileNotFoundError as ex:
    # Код регистрирует ошибку, если файл настроек не найден
    logger.error(f'Файл настроек не найден {ex=}', exc_info=True)
    ...
except Exception as ex:
    # Код регистрирует ошибку при разборе JSON
    logger.error(f'Ошибка при чтении файла настроек {ex=}', exc_info=True)
    ...

doc_str: str = None
"""
    Строка с содержимым документации проекта, загруженная из `README.MD`.

    :type: str or None
"""
try:
    # Код загружает документацию из файла 'README.MD'
    with open(gs.path.root / 'src' / 'README.MD', 'r') as settings_file:
        doc_str = settings_file.read()
except FileNotFoundError as ex:
     # Код регистрирует ошибку, если файл документации не найден
    logger.error(f'Файл документации не найден {ex=}', exc_info=True)
    ...
except Exception as ex:
    # Код регистрирует ошибку при чтении файла документации
    logger.error(f'Ошибка при чтении файла документации {ex=}', exc_info=True)
    ...

# Код устанавливает значения по умолчанию, если настройки не загружены
__project_name__: str = settings.get("project_name", 'hypotez') if settings else 'hypotez'
"""
    Имя проекта.

    :type: str
"""
__version__: str = settings.get("version", '') if settings else ''
"""
    Версия проекта.

    :type: str
"""
__doc__: str = doc_str if doc_str else ''
"""
    Описание проекта, загруженное из файла `README.MD`.

    :type: str
"""
__details__: str = ''
"""
    Детальное описание проекта.

    :type: str
"""
__author__: str = settings.get("author", '') if settings else ''
"""
    Автор проекта.

    :type: str
"""
__copyright__: str = settings.get("copyrihgnt", '') if settings else ''
"""
    Информация об авторских правах.

    :type: str
"""
__cofee__: str = settings.get("cofee", "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69") if settings else "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69"
"""
    Сообщение с призывом поддержать разработчика.

    :type: str
"""
```