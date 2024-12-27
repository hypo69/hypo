# Анализ кода модуля `header.py`

**Качество кода**
8
- Плюсы
    - Код достаточно структурирован, используются функции для определения корневой директории проекта.
    - Присутствует обработка исключений при чтении файлов настроек и документации.
    - Используются константы для хранения информации о проекте.
- Минусы
    - Не используется `j_loads` или `j_loads_ns` для чтения файлов.
    - Отсутствует подробная документация в формате reStructuredText.
    - Избыточное использование `try-except` с `...` для обработки ошибок.
    - Код не соответствует code style (одинарные кавычки)

**Рекомендации по улучшению**

1.  **Использовать `j_loads`**: Заменить `json.load` на `j_loads` из `src.utils.jjson` для чтения `settings.json`.
2.  **Добавить документацию**: Написать подробные docstring в формате reStructuredText для модуля, функций и переменных.
3.  **Логирование ошибок**: Заменить `...` в блоках `try-except` на логирование ошибок с использованием `logger.error`.
4.  **Унифицировать кавычки**: Заменить двойные кавычки на одинарные в строках.
5.  **Добавить импорты**: Добавить отсутствующие импорты `from src.utils.jjson import j_loads`.
6. **Убрать избыточность** убрать лишние переменные.
7. **Использовать f-строки**: использовать f-строки для форматирования строк.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12
"""
Модуль для настройки окружения и получения базовых параметров проекта.
====================================================================

Этот модуль устанавливает корневую директорию проекта, загружает настройки из файла `settings.json`
и считывает документацию из файла `README.MD`.

Пример использования
--------------------

Пример использования для определения корневой директории и загрузки параметров:

.. code-block:: python

    from pathlib import Path

    # Получение корневой директории проекта
    project_root: Path = set_project_root()

    # Загрузка настроек проекта
    settings: dict = load_settings()

    # Доступ к имени проекта
    project_name: str = get_project_name()

    # Получение версии проекта
    version: str = get_project_version()

    # Получение документации проекта
    doc: str = get_project_doc()

"""
MODE = 'dev'

import sys
from pathlib import Path
from packaging.version import Version
from src.utils.jjson import j_loads
from src.logger.logger import logger

def set_project_root(marker_files: tuple = ('pyproject.toml', 'requirements.txt', '.git')) -> Path:
    """
    Определяет корневую директорию проекта.

    Функция ищет корневую директорию проекта, начиная с директории текущего файла,
    перемещаясь вверх по дереву каталогов, пока не найдет один из маркерных файлов.

    :param marker_files: Кортеж имен файлов или директорий, которые идентифицируют корень проекта.
    :type marker_files: tuple
    :return: Путь к корневой директории. Если маркерные файлы не найдены, возвращается директория,
             где расположен скрипт.
    :rtype: Path
    """
    current_path: Path = Path(__file__).resolve().parent
    root: Path = current_path

    for parent in [current_path] + list(current_path.parents):
        if any((parent / marker).exists() for marker in marker_files):
            root = parent
            break
    if root not in sys.path:
        sys.path.insert(0, str(root))
    return root

# Установка корневой директории проекта
__root__: Path = set_project_root()
"""
Путь к корневой директории проекта.
:type: Path
"""

from src import gs

settings: dict = {}
"""
Словарь настроек проекта, загруженный из файла settings.json.
:type: dict
"""
try:
    # Чтение настроек из файла settings.json
    with open(gs.path.root / 'src' / 'settings.json', 'r', encoding='utf-8') as settings_file:
        settings = j_loads(settings_file)
except (FileNotFoundError, json.JSONDecodeError) as e:
    # Логирование ошибки, если файл не найден или не является валидным JSON
    logger.error(f'Ошибка при загрузке файла settings.json: {e}')


doc_str: str = ''
"""
Строка, содержащая документацию проекта, загруженную из файла README.MD.
:type: str
"""
try:
    # Чтение документации из файла README.MD
    with open(gs.path.root / 'src' / 'README.MD', 'r', encoding='utf-8') as doc_file:
        doc_str = doc_file.read()
except (FileNotFoundError) as e:
        # Логирование ошибки, если файл не найден
        logger.error(f'Ошибка при загрузке файла README.MD: {e}')


__project_name__: str = settings.get('project_name', 'hypotez')
"""
Имя проекта, полученное из настроек или значение по умолчанию.
:type: str
"""
__version__: str = settings.get('version', '')
"""
Версия проекта, полученная из настроек или пустая строка.
:type: str
"""
__doc__: str = doc_str
"""
Документация проекта, загруженная из файла README.MD.
:type: str
"""
__details__: str = ''
"""
Детальная информация о проекте (в настоящее время пустая строка).
:type: str
"""
__author__: str = settings.get('author', '')
"""
Автор проекта, полученный из настроек или пустая строка.
:type: str
"""
__copyright__: str = settings.get('copyrihgnt', '')
"""
Информация об авторских правах проекта, полученная из настроек или пустая строка.
:type: str
"""
__cofee__: str = settings.get('cofee', "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69")
"""
Сообщение с предложением угостить разработчика кофе, полученное из настроек или значение по умолчанию.
:type: str
"""
```