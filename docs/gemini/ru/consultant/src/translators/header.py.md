# Анализ кода модуля `header.py`

**Качество кода**
8
 -  Плюсы
    - Код выполняет поиск корневой директории проекта.
    - Используется `pathlib` для работы с путями.
    - Есть обработка исключений при чтении файлов настроек.
    - Присутствует установка корневого каталога проекта в `sys.path`.

 -  Минусы
    - Отсутствует подробная документация в формате reStructuredText (RST).
    - Использован стандартный `json.load` вместо `j_loads` или `j_loads_ns`.
    -  Блоки `try-except` используют `...` вместо логирования ошибок.
    -  Имена переменных и импортов не согласованы с предыдущими файлами.
    -  Много неиспользуемых комментариев

**Рекомендации по улучшению**

1.  **Документация**: Переписать docstring в формате reStructuredText (RST) для всех функций, классов и модулей.
2.  **Импорты**: Добавить недостающие импорты, такие как `logger` из `src.logger.logger`.
3.  **Чтение JSON**: Заменить `json.load` на `j_loads` или `j_loads_ns` из `src.utils.jjson`.
4.  **Обработка ошибок**:  Использовать `logger.error` для записи ошибок и избегать использования `...` в блоках `except`.
5.  **Переменные**: Привести имена переменных в соответствие с принятыми стандартами, например, `project_name` вместо `__project_name__`.
6.  **Комментарии**: Удалить все неиспользуемые комментарии и добавить подробные комментарии к коду.
7. **Модульные константы** : Заменить на `__MODE__` вместо `MODE`, чтобы соответствовать конвенции о модульных константах.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
"""
Модуль для определения и загрузки настроек проекта.
=========================================================================================

Этот модуль содержит функции для определения корневой директории проекта,
а также для загрузки настроек из файла `settings.json` и README.MD.

Пример использования
--------------------

Пример использования модуля:

.. code-block:: python

    from src.translators import header

    print(header.__project_name__)
"""
import sys
from pathlib import Path
from packaging.version import Version
from src.utils.jjson import j_loads  #  импортируем j_loads из src.utils.jjson
from src.logger.logger import logger # импортируем logger
__MODE__ = 'dev'


def set_project_root(marker_files: tuple = ('pyproject.toml', 'requirements.txt', '.git')) -> Path:
    """
    Определяет корневую директорию проекта.

    Функция ищет корневую директорию проекта, начиная с директории текущего файла,
    продвигаясь вверх по дереву директорий. Поиск останавливается на первой директории,
    содержащей один из файлов-маркеров.

    :param marker_files: Кортеж имен файлов или директорий, используемых для определения корня проекта.
    :type marker_files: tuple
    :return: Путь к корневой директории проекта.
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


#  Код определяет корневую директорию проекта
root = set_project_root()
"""root (Path): Путь к корневой директории проекта."""

from src import gs
settings: dict = None
try:
    # код загружает настройки из файла settings.json
    with open(gs.path.root / 'src' / 'settings.json', 'r', encoding='utf-8') as settings_file:
        settings = j_loads(settings_file) # используем j_loads для загрузки настроек
except FileNotFoundError as ex:
    #  Код обрабатывает ошибку, если файл настроек не найден
    logger.error(f'Файл settings.json не найден: {ex}')
except Exception as ex:
    #  Код обрабатывает ошибку, если файл настроек не удалось декодировать
    logger.error(f'Ошибка декодирования settings.json: {ex}')

doc_str: str = None
try:
    #  Код загружает содержимое файла README.MD
    with open(gs.path.root / 'src' / 'README.MD', 'r', encoding='utf-8') as readme_file:
        doc_str = readme_file.read()
except FileNotFoundError as ex:
     #  Код обрабатывает ошибку, если файл README.MD не найден
    logger.error(f'Файл README.MD не найден: {ex}')
except Exception as ex:
    #  Код обрабатывает ошибку, если файл README.MD не удалось прочитать
    logger.error(f'Ошибка чтения README.MD: {ex}')

project_name = settings.get("project_name", 'hypotez') if settings else 'hypotez'
"""project_name (str): Название проекта."""
version: str = settings.get("version", '') if settings else ''
"""version (str): Версия проекта."""
doc: str = doc_str if doc_str else ''
"""doc (str): Документация проекта из README.MD."""
details: str = ''
"""details (str): Дополнительные сведения о проекте."""
author: str = settings.get("author", '') if settings else ''
"""author (str): Автор проекта."""
copyright_str: str = settings.get("copyrihgnt", '') if settings else ''
"""copyright_str (str): Информация об авторских правах."""
coffee: str = settings.get("cofee", "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69") if settings else "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69"
"""coffee (str): Сообщение с предложением поддержать разработчика."""
```