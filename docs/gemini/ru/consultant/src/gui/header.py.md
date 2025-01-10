# Анализ кода модуля `header.py`

**Качество кода**
8
-  Плюсы
    - Код достаточно хорошо структурирован, имеет функции и переменные с понятными именами.
    - Присутствует базовая обработка ошибок при чтении файлов настроек и документации.
    - Использование `pathlib.Path` для работы с путями является хорошей практикой.
    - Есть описание модуля и назначения переменных.

-  Минусы
    - Отсутствует документация в формате RST для функций и переменных.
    - Не используется `j_loads` или `j_loads_ns` для загрузки `json`.
    - Не используется `logger` для логирования ошибок.
    - Не все переменные имеют описания.
    - Использование `...` в `except` блоках может усложнить отладку.
    - Не всегда соблюдается форматирование строк в соответствии с требованиями.

**Рекомендации по улучшению**

1.  Добавить документацию в формате RST для модуля, функций и переменных.
2.  Использовать `j_loads` из `src.utils.jjson` для чтения `settings.json`.
3.  Использовать `logger` из `src.logger.logger` для логирования ошибок и отладки.
4.  Убрать `...` из блоков `except` и добавить логирование ошибок.
5.  Добавить описания для всех переменных в формате RST.
6.  Привести все строки к виду с одинарными кавычками.
7.  Удалить лишние комментарии.

**Оптимизированный код**

```python
"""
Модуль для определения корневого пути проекта и загрузки настроек.
=================================================================

Этот модуль устанавливает корневой каталог проекта, добавляет его в `sys.path`,
а также загружает настройки из файла `settings.json` и документацию из `README.MD`.

Пример использования
--------------------

Пример инициализации:

.. code-block:: python

    from src.gui.header import __root__, __project_name__, __version__

    print(f"Project root: {__root__}")
    print(f"Project name: {__project_name__}")
    print(f"Project version: {__version__}")
"""
import sys
from pathlib import Path
from packaging.version import Version
from src.utils.jjson import j_loads  # Используем j_loads для чтения json
from src.logger.logger import logger # Импортируем logger
def set_project_root(marker_files: tuple = ('__root__', '.git')) -> Path:
    """
    Определяет корневой каталог проекта, начиная с каталога текущего файла.

    Поиск идет вверх по дереву каталогов, останавливаясь на первом каталоге,
    содержащем любой из файлов-маркеров.

    :param marker_files: Список имен файлов или каталогов для идентификации корня проекта.
    :type marker_files: tuple
    :return: Путь к корневому каталогу, если найден. Иначе - путь к каталогу скрипта.
    :rtype: Path
    """
    __root__:Path
    current_path:Path = Path(__file__).resolve().parent
    __root__ = current_path
    for parent in [current_path] + list(current_path.parents):
        if any((parent / marker).exists() for marker in marker_files):
            __root__ = parent
            break
    if __root__ not in sys.path:
        sys.path.insert(0, str(__root__))
    return __root__

# Получаем корневой каталог проекта
__root__: Path = set_project_root()
"""
:type: Path
:var __root__: Путь к корневому каталогу проекта.
"""

from src import gs

settings: dict = None
try:
    # Используем j_loads для загрузки настроек
    with open(gs.path.root / 'src' / 'settings.json', 'r') as settings_file:
         settings = j_loads(settings_file)
except (FileNotFoundError, Exception) as ex:
    # Логируем ошибку если файл не найден или json не валиден
    logger.error(f'Не удалось загрузить файл настроек {gs.path.root / "src" / "settings.json"}', exc_info=ex)

doc_str: str = None
try:
    with open(gs.path.root / 'src' / 'README.MD', 'r') as settings_file:
        doc_str = settings_file.read()
except (FileNotFoundError, Exception) as ex:
    # Логируем ошибку если файл не найден или проблемы при чтении
    logger.error(f'Не удалось загрузить файл документации {gs.path.root / "src" / "README.MD"}', exc_info=ex)


__project_name__: str = settings.get('project_name', 'hypotez') if settings else 'hypotez'
"""
:type: str
:var __project_name__: Название проекта.
"""
__version__: str = settings.get('version', '') if settings else ''
"""
:type: str
:var __version__: Версия проекта.
"""
__doc__: str = doc_str if doc_str else ''
"""
:type: str
:var __doc__: Документация проекта (содержимое файла README.MD).
"""
__details__: str = ''
"""
:type: str
:var __details__: Детали проекта (в настоящее время не используется).
"""
__author__: str = settings.get('author', '') if settings else ''
"""
:type: str
:var __author__: Автор проекта.
"""
__copyright__: str = settings.get('copyrihgnt', '') if settings else ''
"""
:type: str
:var __copyright__: Информация об авторских правах.
"""
__cofee__: str = settings.get('cofee', 'Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69') if settings else 'Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69'
"""
:type: str
:var __cofee__: Сообщение для поддержки разработчика.
"""
```