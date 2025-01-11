# Анализ кода модуля `header.py`

**Качество кода**
7
-  Плюсы
    - Код выполняет свою основную задачу: находит корневую директорию проекта и загружает настройки из файла.
    - Использует `pathlib` для работы с путями, что является хорошей практикой.
    - Присутствуют базовые docstring для модуля и функции.
-  Минусы
    -  Отсутствует обработка ошибок через `logger.error` при загрузке `settings.json` и `README.MD`.
    -  Множественные пустые docstring, которые не несут никакой смысловой нагрузки.
    -  Не используются `j_loads` или `j_loads_ns`.
    -  Не все импорты указаны в начале файла.
    -  Использование `...` в блоках `except` неинформативно.
    -  Не хватает комментариев, которые бы объясняли назначение переменных и блоков кода.

**Рекомендации по улучшению**

1.  **Импорт `logger`**: Добавить импорт `logger` из `src.logger.logger`.
2.  **Использование `j_loads`**: Использовать `j_loads` из `src.utils.jjson` для загрузки JSON-файлов.
3.  **Обработка ошибок**: Заменить `try-except` на конструкцию с `logger.error` для обработки ошибок при загрузке файлов.
4.  **Документация**: Добавить подробные docstring для всех функций и переменных, а также для модуля.
5.  **Комментарии**: Добавить комментарии для объяснения назначения блоков кода.
6.  **Удалить неиспользуемые docstring**: Удалить пустые docstring.
7.  **Форматирование**: Привести код в соответствие с PEP8.
8. **Переменные**: Объявить переменные с указанием типа.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
"""
Модуль для определения корневой директории проекта и загрузки настроек.
=========================================================================================

Этот модуль содержит функции для определения корневой директории проекта,
загрузки настроек из `settings.json` и чтения документации из `README.MD`.

Пример использования
--------------------

Пример использования функции `set_project_root`:

.. code-block:: python

    root_path = set_project_root()
    print(f"Root directory: {root_path}")

"""
import sys
from pathlib import Path
from typing import Tuple, Dict, Optional
from packaging.version import Version

from src.utils.jjson import j_loads  #  Импортируем j_loads из src.utils.jjson
from src.logger.logger import logger #  Импортируем logger из src.logger.logger

def set_project_root(marker_files: Tuple[str, ...] = ('__root__', '.git')) -> Path:
    """
    Определяет корневую директорию проекта, начиная с директории текущего файла.

    Функция ищет родительские директории до тех пор, пока не найдет директорию,
    содержащую один из файлов-маркеров.

    Args:
        marker_files (tuple): Кортеж имен файлов или директорий для идентификации корневой директории проекта.

    Returns:
        Path: Путь к корневой директории, если она найдена. В противном случае, возвращает директорию, в которой находится скрипт.
    """
    current_path: Path = Path(__file__).resolve().parent #  Получаем абсолютный путь к директории текущего файла
    root_path: Path = current_path #  Инициализируем корневой путь текущей директорией

    #  Итерируемся по родительским директориям текущего файла
    for parent in [current_path] + list(current_path.parents):
        #  Проверяем, существует ли в родительской директории какой-либо из файлов-маркеров
        if any((parent / marker).exists() for marker in marker_files):
            root_path = parent #  Если файл-маркер найден, устанавливаем корневой путь
            break #  Прерываем цикл

    #  Добавляем корневой путь в sys.path, если его там нет
    if root_path not in sys.path:
        sys.path.insert(0, str(root_path))
    return root_path


#  Определяем корневую директорию проекта
__root__: Path = set_project_root()
"""Path: Путь к корневой директории проекта."""


from src import gs

settings: Optional[Dict] = None
"""dict: Словарь с настройками проекта, загруженными из settings.json."""
try:
    #  Пытаемся открыть и прочитать файл настроек
    with open(gs.path.root / 'src' / 'settings.json', 'r') as settings_file:
        settings = j_loads(settings_file.read())#  Используем j_loads для загрузки JSON
except (FileNotFoundError, json.JSONDecodeError) as e:
     #  Логируем ошибку, если файл не найден или невалиден
    logger.error(f'Не удалось загрузить настройки из файла settings.json: {e}')


doc_str: Optional[str] = None
"""str: Строка с содержимым файла README.MD."""
try:
    #  Пытаемся открыть и прочитать файл README.MD
    with open(gs.path.root / 'src' / 'README.MD', 'r') as readme_file:
        doc_str = readme_file.read()
except (FileNotFoundError,  UnicodeDecodeError) as e:
      # Логируем ошибку, если файл не найден или невалиден
    logger.error(f'Не удалось загрузить документацию из файла README.MD: {e}')


__project_name__: str = settings.get("project_name", 'hypotez') if settings else 'hypotez'
"""str: Название проекта."""
__version__: str = settings.get("version", '') if settings else ''
"""str: Версия проекта."""
__doc__: str = doc_str if doc_str else ''
"""str: Документация проекта."""
__details__: str = ''
"""str: Дополнительные детали проекта."""
__author__: str = settings.get("author", '') if settings else ''
"""str: Автор проекта."""
__copyright__: str = settings.get("copyrihgnt", '') if settings else ''
"""str: Информация об авторских правах."""
__cofee__: str = settings.get("cofee", "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69") if settings else "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69"
"""str: Призыв поддержать разработчика."""
```