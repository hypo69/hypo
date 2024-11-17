```python
## \file hypotez/src/endpoints/kazarinov/header.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
""" module: src.endpoints.kazarinov """
MODE = 'debug'
import sys
import json
from packaging.version import Version

from pathlib import Path
def get_project_root(marker_files=('pyproject.toml', 'requirements.txt', '.git')) -> Path:
    """!
    Находит корневую директорию проекта, начиная от директории текущего файла,
    ищет вверх по дереву директорий и останавливается на первой директории,
    содержащей любой из указанных файлов-маркеров.

    @param marker_files: Кортеж имен файлов или директорий,
        используемых для определения корневой директории проекта.

    @return: Путь к корневой директории, если найдена, иначе - директория,
        в которой расположен текущий скрипт.
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


# Получение корневой директории проекта
__root__: Path = get_project_root()
"""__root__ (Path): Путь к корневой директории проекта"""

from src import gs

settings:dict = None
try:
    with open(gs.path.root / 'src' /  'settings.json', 'r', encoding='utf-8') as settings_file:  # Добавление encoding='utf-8'
        settings = json.load(settings_file)
except (FileNotFoundError, json.JSONDecodeError) as e:
    print(f"Ошибка загрузки settings.json: {e}")  # Обработка ошибок


doc_str:str = None
try:
    with open(gs.path.root / 'src' /  'README.MD', 'r', encoding='utf-8') as settings_file:  # Добавление encoding='utf-8'
        doc_str = settings_file.read()
except (FileNotFoundError, json.JSONDecodeError) as e:
    print(f"Ошибка загрузки README.MD: {e}")  # Обработка ошибок


__project_name__ = settings.get("project_name", 'hypotez') if settings  else 'hypotez'
__version__: str = settings.get("version", '')  if settings  else ''
__doc__: str = doc_str if doc_str else ''
__details__: str = ''
__author__: str = settings.get("author", '')  if settings  else ''
__copyright__: str = settings.get("copyright", '')  if settings  else '' # Исправление опечатки
__cofee__: str = settings.get("cofee", "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69")  if settings  else "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69"


```

**Изменения и объяснения:**

* **Обработка ошибок:** добавлен `try...except` блок для обработки `FileNotFoundError` и `json.JSONDecodeError` при чтении `settings.json` и `README.MD`.  Выводится сообщение об ошибке, что критично для отладки.
* **Кодировка:** Добавлено `encoding='utf-8'` в операциях `open()`, чтобы корректно обрабатывать файлы с русскими символами (и другими).  Это чрезвычайно важно, если в файлах есть кириллица или другие не-ASCII символы.
* **Дополнения к документации:**  Изменён комментарий в функции `get_project_root` для большей ясности и лучшей локализации.
* **Исправление опечатки:** Исправлена опечатка в переменной `__copyright__`.
* **Стиль кода:** Улучшена читаемость кода и структура.
* **Подробности об ошибках:**  В сообщениях об ошибках теперь содержится информация о типе ошибки и, что важно, о том, какой файл вызывал ошибку. Это значительно облегчит отладку в будущем.


**Как использовать:**

Этот улучшенный код надежно находит корневую директорию проекта, обрабатывает ошибки чтения конфигурационного файла и файла документации, а также корректно работает с кириллицей (и другими не-ASCII символами).  Вы можете импортировать этот файл в другие скрипты вашего проекта и использовать переменные `__root__`, `__project_name__`, `__version__` и другие.


**Дополнительные советы:**

* **Логирование:** Для более продвинутых сценариев, рекомендуется использовать библиотеку `logging` для записи сообщений об ошибках в файл журнала. Это позволит отслеживать все ошибки во время работы приложения.
* **`pathlib`:**  Используйте методы `pathlib` для работы с путями.  Этот подход делает код более переносимым и проще для понимания.
* **Исключения:** Если в вашем коде есть другие потенциальные ошибки, добавьте соответствующие `try...except` блоки, чтобы обработать их.