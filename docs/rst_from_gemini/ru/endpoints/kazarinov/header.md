```markdown
# hypotez/src/endpoints/kazarinov/header.py

Этот файл определяет функцию `get_project_root` для нахождения корневой директории проекта.  Он также загружает настройки из файла `settings.json` и читает содержимое файла `README.MD` для документации проекта.  Полученные данные используются для формирования метаданных проекта.

```python
## \file hypotez/src/endpoints/kazarinov/header.py
# -*- coding: utf-8 -*-
import sys
import json
from packaging.version import Version

from pathlib import Path
def get_project_root(marker_files=('pyproject.toml', 'requirements.txt', '.git')) -> Path:
    """!
    Находит корневую директорию проекта, начиная с директории текущего файла,
    переходя наверх по директориям и останавливаясь на первой, содержащей один из указанных файлов или директорий.

    Args:
        marker_files (tuple): Имена файлов или директорий, указывающие на корень проекта.

    Returns:
        Path: Путь к корневой директории, если найдена, иначе — директория, где расположен данный скрипт.
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
    print(f"Ошибка при загрузке настроек: {e}")
    settings = {}


doc_str:str = None
try:
    with open(gs.path.root / 'src' /  'README.MD', 'r', encoding='utf-8') as settings_file:  # Добавление encoding='utf-8'
        doc_str = settings_file.read()
except (FileNotFoundError, json.JSONDecodeError) as e:
    print(f"Ошибка при чтении README.MD: {e}")
    doc_str = ''


__project_name__ = settings.get("project_name", 'hypotez') if settings  else 'hypotez'
__version__: str = settings.get("version", '')  if settings  else ''
__doc__: str = doc_str if doc_str else ''
__details__: str = ''
__author__: str = settings.get("author", '')  if settings  else ''
__copyright__: str = settings.get("copyright", '')  if settings  else ''  # Исправление имени ключа
__cofee__: str = settings.get("coffee", "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69") if settings else "Treat the developer to a cup of coffee for boosting enthusiasm in development: https://boosty.to/hypo69"


```

**Изменения и улучшения:**

* **Обработка ошибок:** Добавлена обработка `FileNotFoundError` и `json.JSONDecodeError` с выводом сообщений об ошибках. Это предотвращает аварийный выход программы и позволяет определить причину сбоя.  Также инициализируются переменные `settings` и `doc_str` по умолчанию.
* **Кодировка:** Добавлено `encoding='utf-8'` в функции `open`.  Это критически важно для корректной обработки файлов, содержащих символы с кодировкой UTF-8.  Без этого могут возникнуть ошибки при работе с русским языком.
* **Уточнение документации:** Добавлен более подробный комментарий к функции `get_project_root`.  В документирование отражено, как именно функция определяет корень проекта.
* **Исправление имени переменной:** Изменено `copyrihgnt` на `copyright` в `settings.get`.


**Рекомендации:**

* **Более подробная обработка ошибок:**  Добавьте логирование ошибок для лучшей отладки.
* **Документация для `gs`:**  Если `gs` — это собственная библиотека, необходимо добавить документацию для нее.
* **Обработка пустого файла `settings.json`:** Проверьте, чтобы переменная `settings` была не пустым словарем, если файл `settings.json` существует, но пустой.
* **Возвращаемое значение `get_project_root`:**  Рекомендуется, чтобы функция `get_project_root` возвращала `None` или `Path(None)`, если корень проекта не найден, чтобы можно было обрабатывать этот случай.

Эти изменения делают код более надежным, удобочитаемым и удобным в использовании.  Они также повышают устойчивость к различным ситуациям, которые могут возникнуть при работе с файлами и данными.