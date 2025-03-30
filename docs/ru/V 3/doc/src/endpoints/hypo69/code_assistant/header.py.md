# Модуль `header`

## Обзор

Модуль `header` определяет корневой путь к проекту `hypotez`. Все импорты строятся относительно этого пути.

## Подробней

Этот модуль важен для правильной организации импортов в проекте и определения его версии и других метаданных. Функция `set_project_root` автоматически определяет корень проекта, что упрощает переносимость и настройку проекта в различных средах. Метаданные, такие как имя проекта, версия, автор и т. д., считываются из файла `settings.json` и `README.MD`, расположенного в корне проекта.

## Функции

### `set_project_root`

```python
def set_project_root(marker_files: tuple[str, ...]=('__root__', '.git')) -> Path:
    """
    Args:
        marker_files (tuple): Filenames or directory names to identify the project root.
    
    Returns:
        Path: Path to the root directory if found, otherwise the directory where the script is located.
    """
```

**Описание**: Находит корневой каталог проекта, начиная с каталога текущего файла, выполняя поиск вверх и останавливаясь на первом каталоге, содержащем любой из маркерных файлов.

**Параметры**:
- `marker_files` (tuple[str, ...], optional): Кортеж имен файлов или каталогов для идентификации корня проекта. По умолчанию `('__root__', '.git')`.

**Возвращает**:
- `Path`: Путь к корневому каталогу, если он найден, в противном случае — каталог, в котором расположен скрипт.

**Примеры**:
```python
from pathlib import Path
import sys
# Создадим временные файлы и структуру каталогов для тестирования
import os
import tempfile

def create_temp_project(marker_file:str) -> Path:
    temp_dir = Path(tempfile.mkdtemp())
    (temp_dir / "src").mkdir(exist_ok=True)
    (temp_dir / marker_file).touch()  # Создаем маркерный файл
    return temp_dir

# Пример 1: С маркером '__root__'
temp_project_dir = create_temp_project('__root__')
# Добавляем временный каталог в sys.path, чтобы header.py мог быть импортирован
sys.path.insert(0, str(temp_project_dir))
# Устанавливаем корень проекта
import header
root_path = header.set_project_root(marker_files=('__root__',))
print(f"Root path with '__root__' marker: {root_path}")

# Пример 2: С маркером '.git'
temp_project_dir = create_temp_project('.git')
# Добавляем временный каталог в sys.path, чтобы header.py мог быть импортирован
sys.path.insert(0, str(temp_project_dir))
# Устанавливаем корень проекта
import header
root_path = header.set_project_root(marker_files=('.git',))
print(f"Root path with '.git' marker: {root_path}")

#  Удаляем временные файлы и директории
import shutil
shutil.rmtree(temp_project_dir)
```

## Переменные

### `__root__`

**Описание**: Путь к корневому каталогу проекта.

### `settings`

**Описание**: Словарь с настройками проекта, загруженными из файла `settings.json`. Если файл не найден или содержит ошибки JSON, переменная остаётся `None`.

### `doc_str`

**Описание**: Строка с содержимым файла `README.MD`. Если файл не найден или содержит ошибки, переменная остаётся `None`.

### `__project_name__`

**Описание**: Имя проекта, полученное из `settings.json` или `'hypotez'`, если настройка отсутствует.

### `__version__`

**Описание**: Версия проекта, полученная из `settings.json` или `''`, если настройка отсутствует.

### `__doc__`

**Описание**: Содержимое файла `README.MD`, если он существует, иначе пустая строка.

### `__details__`

**Описание**: Пустая строка.

### `__author__`

**Описание**: Автор проекта, полученный из `settings.json` или `''`, если настройка отсутствует.

### `__copyright__`

**Описание**: Информация об авторских правах, полученная из `settings.json` или `''`, если настройка отсутствует.

### `__cofee__`

**Описание**: Текст с предложением угостить разработчика чашкой кофе, полученный из `settings.json` или стандартное сообщение, если настройка отсутствует.