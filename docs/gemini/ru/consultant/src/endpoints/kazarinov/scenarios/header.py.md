# Анализ кода модуля `header.py`

**Качество кода**
8
-   Плюсы
    - Код хорошо структурирован и читаем.
    - Используется `pathlib` для работы с путями, что является хорошей практикой.
    - Есть базовая обработка ошибок при чтении файлов.
    - Определены основные переменные проекта, такие как имя, версия, автор и т.д.
-   Минусы
    - Используется стандартный `json.load` вместо `j_loads` или `j_loads_ns`.
    - Отсутствуют docstring для модуля и функций, отсутствуют комментарии в формате reStructuredText (RST).
    - Обработка ошибок недостаточно детализирована, нет логирования ошибок.
    - Не все переменные имеют аннотации типов.
    - Использование `...` в блоках `try-except` не является информативным.
    - Не все переменные и константы следуют соглашениям об именовании (например, `doc_str`).
    - Не хватает обработки потенциальных ошибок при чтении `settings.json`.

**Рекомендации по улучшению**

1.  **Импорт**: Добавить недостающие импорты, например `from src.utils.jjson import j_loads`, `from src.logger.logger import logger`.
2.  **Документация**: Написать docstring для модуля и функции в формате reStructuredText (RST).
3.  **Обработка ошибок**: Заменить `try-except` на использование `logger.error` для логирования ошибок и избегать использования `...`.
4.  **Использование `j_loads`**: Использовать `j_loads` вместо `json.load` для чтения `settings.json`.
5.  **Аннотации типов**: Добавить аннотации типов для переменных, где это уместно.
6.  **Комментарии**: Добавить подробные комментарии в формате RST для функций, методов и переменных.
7.  **Переменные**: Привести имена переменных в соответствие со стилем snake_case.
8.  **Константы**: Объявить константы MODE как `UPPER_CASE`.
9.  **Соглашения об именовании**: Привести в соответствие имена переменных, такие как `doc_str`  в `doc_string`.
10. **Логирование**: Добавить логирование для отладки и ошибок в `try-except` блоках.
11. **Обработка исключений**: Заменить `...` в блоках `try-except` на логирование с помощью `logger.error`, для более информативной обработки ошибок.
12. **Обработка `settings`**: Добавить проверку на существование ключей в `settings`.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
Модуль для инициализации окружения и получения настроек проекта.
=============================================================

Этот модуль устанавливает корневую директорию проекта, загружает настройки из файла `settings.json`,
а также читает описание проекта из `README.MD`.

Основные задачи:
    - Определение корневой директории проекта.
    - Загрузка настроек проекта.
    - Получение документации проекта.

Пример использования:
--------------------

.. code-block:: python

    from src.endpoints.kazarinov.scenarios.header import __project_name__, __version__, __doc__, __author__

    print(f"Project Name: {__project_name__}")
    print(f"Version: {__version__}")
    print(f"Author: {__author__}")
    print(f"Documentation: {__doc__}")
"""
import sys
from pathlib import Path
from typing import Tuple
from packaging.version import Version
from src.utils.jjson import j_loads
from src.logger.logger import logger

MODE: str = 'dev'

def set_project_root(marker_files: Tuple[str, ...] = ('pyproject.toml', 'requirements.txt', '.git')) -> Path:
    """
    Определяет корневую директорию проекта.

    Функция ищет корневую директорию проекта, начиная с директории текущего файла.
    Поиск осуществляется вверх по дереву директорий до тех пор, пока не будет найдена директория,
    содержащая хотя бы один из указанных файлов-маркеров.

    :param marker_files: Кортеж имен файлов или директорий, которые используются для идентификации корневой директории проекта.
    :type marker_files: Tuple[str, ...]
    :return: Путь к корневой директории проекта.
    :rtype: Path
    :raises FileNotFoundError: Если ни один из файлов-маркеров не найден.

    :Example:
    
    .. code-block:: python
    
        root_path = set_project_root()
        print(root_path)

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


# Получаем корневую директорию проекта
__root__: Path = set_project_root()
"""__root__ (Path): Путь к корневой директории проекта."""

from src import gs

settings: dict | None = None
try:
    # код выполняет загрузку настроек из файла settings.json
    with open(gs.path.root / 'src' / 'settings.json', 'r') as settings_file:
        settings = j_loads(settings_file)
except (FileNotFoundError, json.JSONDecodeError) as e:
    # Логируем ошибку, если файл не найден или не удалось декодировать JSON
    logger.error(f'Ошибка при загрузке настроек из файла: {e}')
    settings = {}

doc_string: str | None = None
try:
    # код выполняет чтение описания проекта из файла README.MD
    with open(gs.path.root / 'src' / 'README.MD', 'r') as doc_file:
        doc_string = doc_file.read()
except (FileNotFoundError, json.JSONDecodeError) as e:
    # Логируем ошибку, если файл не найден
    logger.error(f'Ошибка при чтении файла README.MD: {e}')
    doc_string = ''


__project_name__: str = settings.get("project_name", 'hypotez') if settings else 'hypotez'
"""__project_name__ (str): Имя проекта."""
__version__: str = settings.get("version", '') if settings else ''
"""__version__ (str): Версия проекта."""
__doc__: str = doc_string if doc_string else ''
"""__doc__ (str): Описание проекта."""
__details__: str = ''
"""__details__ (str): Детали проекта."""
__author__: str = settings.get("author", '') if settings else ''
"""__author__ (str): Автор проекта."""
__copyright__: str = settings.get("copyrihgnt", '') if settings else ''
"""__copyright__ (str): Авторские права проекта."""
__cofee__: str = settings.get("cofee", "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69") if settings else "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69"
"""__cofee__ (str): Сообщение о поддержке разработчика."""
```