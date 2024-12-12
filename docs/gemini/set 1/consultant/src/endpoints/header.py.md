# Анализ кода модуля `header`

**Качество кода**
8
- Плюсы
    - Код имеет базовую структуру, необходимую для определения корневой директории проекта и загрузки настроек.
    - Используется `pathlib` для работы с путями, что является хорошей практикой.
    - Функция `set_project_root` корректно находит корень проекта.
    - Присутствует обработка исключений при загрузке настроек и документации.
    - Присутствует установка пути к проекту в `sys.path`.
- Минусы
    - Не используются `j_loads` или `j_loads_ns` для загрузки `json`.
    - Отсутствуют docstring для модуля.
    - Отсутствуют комментарии в формате RST.
    - Использование `try-except` с `...` вместо логирования ошибок.
    - Не стандартизированы имена переменных.
    - Не используется `from src.logger.logger import logger` для логирования.

**Рекомендации по улучшению**

1.  Добавить docstring для модуля в формате RST.
2.  Использовать `j_loads` или `j_loads_ns` из `src.utils.jjson` для чтения `settings.json`.
3.  Добавить комментарии в формате RST для всех функций, переменных и констант.
4.  Использовать `from src.logger.logger import logger` для логирования ошибок, а не `try-except` с многоточием.
5.  Стандартизировать имена переменных в соответствии с PEP8.
6.  Убрать лишний `#!` и ` -*- coding: utf-8 -*-` в начале файла.
7.  Привести в соответствие имена переменных и импортов с ранее обработанными файлами.

**Оптимизированный код**

```python
"""
Модуль для определения корневой директории проекта и загрузки основных настроек.
============================================================================

Этот модуль предоставляет функциональность для определения корневой директории проекта
и загрузки основных настроек из файла `settings.json`, а также чтения документации из `README.MD`.

Функции:
    - `set_project_root`: Находит корневую директорию проекта.

Переменные:
    - `__root__`: Путь к корневой директории проекта.
    - `__project_name__`: Название проекта.
    - `__version__`: Версия проекта.
    - `__doc__`: Содержание файла `README.MD`.
    - `__details__`: Дополнительная информация о проекте (сейчас пустая строка).
    - `__author__`: Автор проекта.
    - `__copyright__`: Информация об авторских правах.
    - `__cofee__`: Призыв поддержать разработчика.

Пример использования
--------------------

    >>> from src.endpoints.header import __root__, __project_name__, __version__
    >>> print(__root__)
    >>> print(__project_name__)
    >>> print(__version__)
"""
import sys
from pathlib import Path
from packaging.version import Version
from src.utils.jjson import j_loads
from src.logger.logger import logger
from src import gs

MODE = 'dev' # Режим работы приложения

def set_project_root(marker_files: tuple =('pyproject.toml', 'requirements.txt', '.git')) -> Path:
    """
    Находит корневую директорию проекта, начиная с директории текущего файла.

    Поиск осуществляется вверх по дереву директорий до тех пор, пока не будет найдена
    директория, содержащая один из файлов-маркеров.

    :param marker_files: Список файлов-маркеров для определения корневой директории.
    :type marker_files: tuple
    :return: Путь к корневой директории.
    :rtype: Path
    """
    __root__: Path
    current_path: Path = Path(__file__).resolve().parent
    __root__ = current_path
    # Итерация по родительским директориям, включая текущую
    for parent in [current_path] + list(current_path.parents):
        # Проверка наличия файла-маркера в текущей родительской директории
        if any((parent / marker).exists() for marker in marker_files):
            __root__ = parent
            break
    # Добавляем корень проекта в sys.path если его там нет
    if __root__ not in sys.path:
        sys.path.insert(0, str(__root__))
    return __root__


# Получение корневой директории проекта
__root__: Path = set_project_root()
"""__root__ (Path): Путь к корневой директории проекта"""


settings: dict = None
try:
    # Чтение настроек из файла settings.json
    with open(gs.path.root / 'src' / 'settings.json', 'r') as settings_file:
         settings = j_loads(settings_file)
except (FileNotFoundError, json.JSONDecodeError) as e:
    # Логирование ошибки, если файл не найден или неверный формат JSON
    logger.error(f'Ошибка при чтении файла настроек: {e}')

doc_str: str = None
try:
    # Чтение документации из файла README.MD
    with open(gs.path.root / 'src' / 'README.MD', 'r') as doc_file:
        doc_str = doc_file.read()
except (FileNotFoundError, json.JSONDecodeError) as e:
    # Логирование ошибки, если файл не найден или неверный формат JSON
    logger.error(f'Ошибка при чтении файла документации: {e}')


# Загрузка или установка значений по умолчанию
__project_name__: str = settings.get("project_name", 'hypotez') if settings else 'hypotez'
"""__project_name__ (str): Название проекта"""
__version__: str = settings.get("version", '') if settings else ''
"""__version__ (str): Версия проекта"""
__doc__: str = doc_str if doc_str else ''
"""__doc__ (str): Содержание файла README.MD"""
__details__: str = ''
"""__details__ (str): Дополнительная информация о проекте"""
__author__: str = settings.get("author", '') if settings else ''
"""__author__ (str): Автор проекта"""
__copyright__: str = settings.get("copyrihgnt", '') if settings else ''
"""__copyright__ (str): Информация об авторских правах"""
__cofee__: str = settings.get("cofee", "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69") if settings else "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69"
"""__cofee__ (str): Призыв поддержать разработчика"""
```