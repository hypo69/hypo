# Анализ кода модуля `header.py`

**Качество кода**
6
- Плюсы
    - Код содержит базовую структуру модуля, включая определение переменных проекта и путей.
    - Используется функция `set_project_root` для определения корневой директории проекта.
    - Есть обработка исключений для чтения файлов `settings.json` и `README.MD`.
- Минусы
    - Использование стандартного `json.load` вместо `j_loads` или `j_loads_ns`.
    - Отсутствуют импорты из `src.utils.jjson`.
    - Отсутствуют docstring для модуля и функции.
    - Избыточное использование `try-except` блоков без логирования ошибок.
    - Не стандартизированы имена переменных и констант.
    - Не используется логирование ошибок.
    - Отсутствует описание модуля в формате RST.

**Рекомендации по улучшению**

1.  Использовать `j_loads` из `src.utils.jjson` вместо `json.load`.
2.  Добавить docstring в формате RST для модуля и функции `set_project_root`.
3.  Использовать `logger.error` для обработки исключений вместо многократных `try-except` с `...`.
4.  Привести в соответствие имена переменных.
5.  Удалить неиспользуемые переменные `MODE`.
6.  Обеспечить логирование ошибок при чтении файлов.
7.  Добавить проверку, что `settings` это словарь перед обращением к его методу `get()`.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
Модуль header.py
=========================================================================================

Этот модуль определяет основные настройки проекта, загружая их из файлов `settings.json` и `README.MD`,
а также определяет корневую директорию проекта.

Пример использования
--------------------

Для использования необходимо импортировать модуль и получить доступ к переменным,
таким как ``__project_name__``, ``__version__`` и другие.

.. code-block:: python

    import src.goog.spreadsheet.header as header

    print(header.__project_name__)
    print(header.__version__)

"""
import sys
# Добавляем импорт j_loads из src.utils.jjson
from src.utils.jjson import j_loads
from packaging.version import Version
from pathlib import Path
# Добавляем импорт logger для логирования
from src.logger.logger import logger
# Импортируем модуль gs
from src import gs


def set_project_root(marker_files: tuple = ('pyproject.toml', 'requirements.txt', '.git')) -> Path:
    """
    Определяет корневую директорию проекта, начиная с директории текущего файла.

    Функция ищет вверх по дереву директорий, пока не найдет директорию, содержащую один из файлов-маркеров.

    :param marker_files: Кортеж имен файлов или директорий, используемых для идентификации корня проекта.
    :type marker_files: tuple
    :return: Путь к корневой директории проекта.
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
"""__root__ (Path): Путь к корневой директории проекта."""

settings: dict = None
try:
    # Используем j_loads для загрузки настроек из файла settings.json
    with open(gs.path.root / 'src' / 'settings.json', 'r') as settings_file:
        settings = j_loads(settings_file)
except (FileNotFoundError, json.JSONDecodeError) as e:
    # Логируем ошибку, если файл не найден или не является JSON
    logger.error(f'Ошибка при чтении файла настроек: {e}')
    ...

doc_str: str = None
try:
    # Считываем содержимое файла README.MD
    with open(gs.path.root / 'src' / 'README.MD', 'r') as readme_file:
        doc_str = readme_file.read()
except (FileNotFoundError, json.JSONDecodeError) as e:
    # Логируем ошибку, если файл не найден
    logger.error(f'Ошибка при чтении файла README.MD: {e}')
    ...

# Извлекаем данные из settings или задаем значения по умолчанию
__project_name__: str = settings.get("project_name", 'hypotez') if isinstance(settings, dict) else 'hypotez'
"""__project_name__ (str): Имя проекта, извлекается из файла настроек."""
__version__: str = settings.get("version", '') if isinstance(settings, dict) else ''
"""__version__ (str): Версия проекта, извлекается из файла настроек."""
__doc__: str = doc_str if doc_str else ''
"""__doc__ (str): Содержимое файла README.MD, используемое как описание проекта."""
__details__: str = ''
"""__details__ (str): Детальное описание проекта."""
__author__: str = settings.get("author", '') if isinstance(settings, dict) else ''
"""__author__ (str): Автор проекта, извлекается из файла настроек."""
__copyright__: str = settings.get("copyrihgnt", '') if isinstance(settings, dict) else ''
"""__copyright__ (str): Информация об авторских правах, извлекается из файла настроек."""
__cofee__: str = settings.get("cofee", "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69") if isinstance(settings, dict) else "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69"
"""__cofee__ (str): Сообщение с предложением поддержать разработчика, извлекается из файла настроек."""
```