# Анализ кода модуля header.py

**Качество кода**
8
-  Плюсы
    - Код хорошо структурирован и выполняет свою задачу - определение корневой директории проекта и загрузку настроек.
    - Используется `pathlib` для работы с путями, что делает код более читаемым и кроссплатформенным.
    - Присутствуют базовые проверки и обработки ошибок при чтении файлов настроек и документации.
    - Код явно задает переменные и их типы (хоть и не всегда с использованием аннотаций).
    - Используются `get` для получения значений из `settings` с значениями по умолчанию.
    - В целом, код достаточно понятен и логичен.
-  Минусы
    - Отсутствует обработка исключений для случая, когда `settings` является `None` (при `FileNotFoundError` или `JSONDecodeError`).
    - Желательно было бы использовать `j_loads` или `j_loads_ns` из `src.utils.jjson` для чтения json файлов.
    - Присутствует использование `...` для обработки исключений, что не рекомендуется.
    - Отсутствует reStructuredText (RST) документация для модуля, функций и переменных.
    - Использование `__` для определения private полей (не рекомендуется).
    - Нет логирования ошибок.

**Рекомендации по улучшению**

1.  **Документация:**
    - Добавить reStructuredText (RST) документацию для модуля, функции `set_project_root` и всех переменных, включая `__root__`, `settings`, `doc_str` и т.д.
2.  **Импорты:**
    - Добавить `from src.utils.jjson import j_loads_ns` и использовать `j_loads_ns` вместо `json.load`.
3.  **Обработка ошибок:**
    - Заменить использование `...` на логирование ошибок с использованием `from src.logger.logger import logger` и более информативные сообщения об ошибках.
    - Обработать случай, когда `settings` является `None`, при попытке получить из него значения.
4.  **Стиль кода:**
    - Убрать использование `__` для определения "приватных" полей.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-

#! venv/bin/python/python3.12

"""
Модуль для определения корневой директории проекта и загрузки настроек.
========================================================================

Этот модуль предоставляет функциональность для определения корневой директории проекта
на основе наличия файлов-маркеров, а также для загрузки настроек из файла `settings.json`
и чтения документации из файла `README.MD`.

Модуль также определяет глобальные переменные, такие как имя проекта, версию,
автора и информацию об авторских правах, которые используются в проекте.

Пример использования
--------------------

Пример использования::

    from src.utils.header import __project_name__, __version__, __doc__
    print(f"Имя проекта: {__project_name__}")
    print(f"Версия: {__version__}")
    print(f"Документация: {__doc__}")
"""


"""
    :platform: Windows, Unix
    :synopsis: Модуль определяющий корневой путь к проекту. Все импорты строятся относительно этого пути.
    :TODO: В дальнейшем перенести в системную переменную
"""

import sys
# добавлено j_loads_ns
from src.utils.jjson import j_loads_ns
from packaging.version import Version
from pathlib import Path
# добавил импорт logger
from src.logger.logger import logger

def set_project_root(marker_files: tuple =('pyproject.toml', 'requirements.txt', '.git')) -> Path:
    """
    Определяет корневую директорию проекта.

    Функция ищет корневую директорию проекта, начиная с директории текущего файла
    и поднимаясь вверх по иерархии каталогов. Поиск останавливается при обнаружении
    первой директории, содержащей любой из файлов-маркеров.

    :param marker_files: Кортеж имен файлов или директорий для идентификации корневой директории проекта.
    :type marker_files: tuple
    :return: Путь к корневой директории проекта.
    :rtype: Path
    :raises FileNotFoundError: Если корневая директория не найдена.
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


# Get the root directory of the project
root_path = set_project_root()
"""Path: Путь к корневой директории проекта."""

from src import gs

settings: dict = None
"""dict: Словарь с настройками проекта."""
try:
    # используем j_loads_ns
    with open(gs.path.root / 'src' / 'settings.json', 'r', encoding='utf-8') as settings_file:
        settings = j_loads_ns(settings_file)
except (FileNotFoundError, json.JSONDecodeError) as e:
    logger.error(f'Ошибка при загрузке файла настроек: {e}')
    settings = {}

doc_str: str = None
"""str: Строка с документацией проекта."""
try:
    with open(gs.path.root / 'src' / 'README.MD', 'r', encoding='utf-8') as doc_file:
        doc_str = doc_file.read()
except (FileNotFoundError,  UnicodeDecodeError) as e:
    logger.error(f'Ошибка при чтении файла документации: {e}')
    doc_str = ''


project_name: str = settings.get("project_name", 'hypotez') if settings  else 'hypotez'
"""str: Имя проекта."""
version: str = settings.get("version", '') if settings else ''
"""str: Версия проекта."""
doc: str = doc_str if doc_str else ''
"""str: Документация проекта."""
details: str = ''
"""str: Детали проекта."""
author: str = settings.get("author", '') if settings else ''
"""str: Автор проекта."""
copyright_info: str = settings.get("copyrihgnt", '') if settings else ''
"""str: Информация об авторских правах."""
cofee: str = settings.get("cofee", "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69") if settings else "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69"
"""str: Сообщение о кофе."""
```