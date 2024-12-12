# Анализ кода модуля `header.py`

**Качество кода**
7
-  Плюсы
    -  Код структурирован и в целом понятен.
    -  Используется `pathlib` для работы с путями, что является хорошей практикой.
    -  Функция `set_project_root` корректно определяет корневую директорию проекта.
    -  Используется `try-except` для обработки ошибок при чтении файлов.
    -  Используются константы для хранения метаданных проекта.
-  Минусы
    -  Используется `json.load` вместо `j_loads` или `j_loads_ns`.
    -  Отсутствует необходимая документация в формате reStructuredText (RST) для модуля, функций и переменных.
    -  Используются пустые `try-except` блоки с `...`, что затрудняет отладку.
    -  Много лишних комментариев вида `# -*- coding: utf-8 -*-`, `# !venv/Scripts/python.exe` и т.д.
    -  В коде много лишних пустых docstring.
    -  Не используются логирование ошибок.
    -  Используются `if settings else` конструкции, которые можно упростить, используя метод `get`.

**Рекомендации по улучшению**

1. Заменить `json.load` на `j_loads` из `src.utils.jjson`.
2. Добавить reStructuredText (RST) документацию для модуля, функций и переменных.
3.  Использовать `logger.error` для логирования ошибок вместо пустых `try-except` блоков.
4. Удалить лишние комментарии и docstring.
5. Упростить конструкции `if settings else` с использованием `get`.
6. Добавить импорты недостающих модулей.

**Оптимизированный код**

```python
"""
Модуль для определения метаданных проекта и его корневой директории.
==================================================================

Этот модуль содержит функции и переменные, необходимые для определения
корневой директории проекта, а также для загрузки метаданных проекта
из файлов настроек и документации.

Пример использования
--------------------

.. code-block:: python

    from src.product.product_fields import header

    print(header.__project_name__)
    print(header.__version__)
"""
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

import sys
from pathlib import Path
from packaging.version import Version

from src.utils.jjson import j_loads  #  Импорт j_loads для загрузки JSON
from src.logger.logger import logger #  Импорт logger для логирования

MODE = 'dev'

def set_project_root(marker_files: tuple = ('pyproject.toml', 'requirements.txt', '.git')) -> Path:
    """
    Определяет корневую директорию проекта.

    Начиная с директории текущего файла, функция ищет вверх по дереву каталогов,
    пока не найдет директорию, содержащую один из файлов-маркеров.

    :param marker_files: Кортеж имен файлов или директорий, которые идентифицируют корень проекта.
    :type marker_files: tuple
    :return: Путь к корневой директории проекта.
    :rtype: Path
    """
    current_path: Path = Path(__file__).resolve().parent
    root_path: Path = current_path
    for parent in [current_path] + list(current_path.parents):
        if any((parent / marker).exists() for marker in marker_files):
            root_path = parent
            break
    if root_path not in sys.path:
        sys.path.insert(0, str(root_path))
    return root_path

#  Получение корневой директории проекта
__root__: Path = set_project_root()
"""Path: Путь к корневой директории проекта."""

from src import gs

settings: dict = {}
"""dict: Словарь с настройками проекта."""
try:
    #  Чтение настроек из файла settings.json с использованием j_loads
    with open(gs.path.root / 'src' / 'settings.json', 'r') as settings_file:
        settings = j_loads(settings_file)
except FileNotFoundError:
    logger.error(f'Файл настроек не найден: {gs.path.root / "src" / "settings.json"}')
except Exception as ex:
    logger.error(f'Ошибка при чтении файла настроек: {ex}')

doc_str: str = ''
"""str: Строка с документацией проекта из файла README.MD."""
try:
    #  Чтение документации из файла README.MD
    with open(gs.path.root / 'src' / 'README.MD', 'r') as doc_file:
        doc_str = doc_file.read()
except FileNotFoundError:
    logger.error(f'Файл документации не найден: {gs.path.root / "src" / "README.MD"}')
except Exception as ex:
    logger.error(f'Ошибка при чтении файла документации: {ex}')

#  Получение метаданных проекта из настроек
__project_name__: str = settings.get("project_name", 'hypotez')
"""str: Имя проекта."""
__version__: str = settings.get("version", '')
"""str: Версия проекта."""
__doc__: str = doc_str
"""str: Документация проекта."""
__details__: str = ''
"""str: Детали проекта."""
__author__: str = settings.get("author", '')
"""str: Автор проекта."""
__copyright__: str = settings.get("copyrihgnt", '')
"""str: Авторские права проекта."""
__cofee__: str = settings.get("cofee", "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69")
"""str: Сообщение о поддержке проекта."""
```