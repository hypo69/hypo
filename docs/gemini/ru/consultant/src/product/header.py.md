# Анализ кода модуля `header.py`

**Качество кода**
- **Соответствие требованиям по оформлению кода: 6/10**
    - **Плюсы:**
        - Код в целом структурирован и выполняет свою задачу - определение корневой директории проекта и загрузку базовых настроек.
        - Присутствуют docstring для функций.
        - Используется `Path` для работы с путями.
        - Есть обработка исключений при чтении файлов настроек.
    - **Минусы:**
        - Не все комментарии оформлены в стиле RST.
        - Использование `json.load` вместо `j_loads` или `j_loads_ns`.
        - Отсутствует импорт `logger` и обработка ошибок через логирование.
        - Не все переменные имеют docstring.
        - Не используется `from src.utils.jjson import j_loads` или `j_loads_ns`.
        - Отсутствует обработка ошибки `FileNotFoundError` в блоке чтения `README.MD`, используется многоточие `...`.
        - Присутствуют лишние комментарии.
        - Смешение стилей написания комментариев.
        - Использование глобальных переменных.

**Рекомендации по улучшению**

1.  **Импорты**: Добавить импорт `from src.utils.jjson import j_loads` и `from src.logger.logger import logger`.
2.  **Использование `j_loads`**: Заменить `json.load` на `j_loads` для чтения JSON файлов.
3.  **Логирование ошибок**: Использовать `logger.error` вместо `...` в блоках `except`.
4.  **Документация**: Переписать все комментарии и docstring в формате RST. Добавить docstring для всех переменных.
5.  **Обработка ошибок**: Добавить обработку `FileNotFoundError` в блоке чтения `README.MD` с использованием `logger.error`.
6.  **Избавиться от лишних комментариев**: Удалить лишние комментарии.
7.  **Переменные**: Использовать `snake_case` для имен переменных.
8. **Перенести константы:** Перенести константы `MODE` в файл настроек `settings.json`.
9. **Удаление лишних комментариев**: Удалить дублирующие и ненужные комментарии.

**Оптимизированный код**

```python
# -*- coding: utf-8 -*-
"""
Модуль для определения корневого пути проекта и загрузки настроек.
====================================================================

Модуль выполняет поиск корневой директории проекта на основе наличия
маркерных файлов, таких как `pyproject.toml`, `requirements.txt` или `.git`.
Также загружает настройки проекта из файла `settings.json` и устанавливает глобальные
переменные, такие как имя проекта, версия, автор и т.д.

.. note::
    В дальнейшем, корневой путь проекта и настройки могут быть перенесены в системные переменные.

"""
import sys
from pathlib import Path
from packaging.version import Version
from src.utils.jjson import j_loads
from src.logger.logger import logger


MODE = 'dev' # TODO : move to settings.json
"""str: Режим работы (dev, prod)"""


def set_project_root(marker_files: tuple = ('pyproject.toml', 'requirements.txt', '.git')) -> Path:
    """
    Определяет корневую директорию проекта.

    Функция выполняет поиск корневой директории проекта, начиная с директории текущего файла
    и поднимаясь вверх по дереву каталогов. Поиск останавливается при обнаружении первого
    каталога, содержащего хотя бы один из маркерных файлов.

    :param marker_files: Кортеж с именами маркерных файлов или каталогов, которые идентифицируют корень проекта.
    :type marker_files: tuple
    :return: Путь к корневой директории проекта.
    :rtype: Path
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


# Получение корневой директории проекта
__root__ = set_project_root()
"""Path: Путь к корневой директории проекта."""


from src import gs

settings: dict = None
"""dict: Словарь с настройками проекта."""
try:
    # Код выполняет чтение файла настроек 'settings.json'
    with open(gs.path.root / 'src' / 'settings.json', 'r') as settings_file:
        settings = j_loads(settings_file) # Загрузка настроек с использованием j_loads
except FileNotFoundError:
    logger.error(f'Файл настроек "settings.json" не найден в {gs.path.root / "src"}')
    settings = {}
except Exception as ex:
    logger.error(f'Ошибка декодирования файла настроек "settings.json"', ex)
    settings = {}



doc_str: str = None
"""str: Содержимое файла README.MD."""
try:
    # Код выполняет чтение файла README.MD
    with open(gs.path.root / 'src' / 'README.MD', 'r') as readme_file:
        doc_str = readme_file.read()
except FileNotFoundError:
    logger.error(f'Файл "README.MD" не найден в {gs.path.root / "src"}')
except Exception as ex:
        logger.error(f'Ошибка чтения файла "README.MD"', ex)
        doc_str = ''

__project_name__ = settings.get("project_name", 'hypotez') if settings else 'hypotez'
"""str: Название проекта."""
__version__: str = settings.get("version", '') if settings else ''
"""str: Версия проекта."""
__doc__: str = doc_str if doc_str else ''
"""str: Документация проекта."""
__details__: str = ''
"""str: Детали проекта."""
__author__: str = settings.get("author", '') if settings else ''
"""str: Автор проекта."""
__copyright__: str = settings.get("copyrihgnt", '') if settings else ''
"""str: Авторские права проекта."""
__cofee__: str = settings.get("cofee", "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69") if settings else "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69"
"""str: Сообщение для поддержки автора."""
```