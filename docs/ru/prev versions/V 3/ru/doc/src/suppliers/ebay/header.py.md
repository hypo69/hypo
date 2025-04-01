# Модуль header

## Обзор

Модуль `header.py` предназначен для определения базовых настроек и путей проекта `hypotez`. Он выполняет поиск корневой директории проекта, загружает конфигурационные параметры из файла `settings.json` и считывает документацию из файла `README.MD`.

## Подорбней

Этот модуль важен для инициализации основных переменных, таких как имя проекта, версия, автор и т. д., которые используются в других частях проекта. Он также определяет функцию `set_project_root`, которая автоматически определяет корень проекта на основе наличия определенных файлов-маркеров.

## Функции

### `set_project_root`

```python
def set_project_root(marker_files: tuple = ('__root__', '.git')) -> Path:
    """
    Args:
        marker_files (tuple): Filenames or directory names to identify the project root.
    
    Returns:
        Path: Path to the root directory if found, otherwise the directory where the script is located.
    """
    ...
```

**Описание**: Находит корневой каталог проекта, начиная с каталога текущего файла, и останавливается на первом каталоге, содержащем любой из файлов-маркеров.

**Параметры**:
- `marker_files` (tuple): Имена файлов или каталогов для идентификации корня проекта. По умолчанию `('__root__', '.git')`.

**Возвращает**:
- `Path`: Путь к корневому каталогу, если он найден, в противном случае - каталог, где расположен скрипт.

**Примеры**:
```python
from pathlib import Path
root_path:Path = set_project_root()
print(root_path)
# Вывод: /путь/к/корневому/каталогу
```
```python
from pathlib import Path
root_path:Path = set_project_root(marker_files = ('.git',))
print(root_path)
# Вывод: /путь/к/корневому/каталогу
```
```python
from pathlib import Path
root_path:Path = set_project_root(marker_files = ('__root__',))
print(root_path)
# Вывод: /путь/к/корневому/каталогу
```
```python
from pathlib import Path
root_path:Path = set_project_root(marker_files = ('my_marker',))
print(root_path)
# Вывод: /путь/к/скрипту
```
```python
from pathlib import Path
root_path:Path = set_project_root(marker_files = ('__root__', '.git'))
print(root_path)
# Вывод: /путь/к/корневому/каталогу
```
```python
from pathlib import Path
root_path:Path = set_project_root(marker_files = ('__root__', '.git'))
print(root_path)
# Вывод: /путь/к/корневому/каталогу
```
```python
from pathlib import Path
root_path:Path = set_project_root()
print(root_path)
# Вывод: /путь/к/корневому/каталогу
```
```python
from pathlib import Path
root_path:Path = set_project_root()
print(root_path)
# Вывод: /путь/к/корневому/каталогу
```
```python
from pathlib import Path
root_path:Path = set_project_root()
print(root_path)
# Вывод: /путь/к/корневому/каталогу
```
```python
from pathlib import Path
root_path:Path = set_project_root()
print(root_path)
# Вывод: /путь/к/корневому/каталогу
```
```python
from pathlib import Path
root_path:Path = set_project_root()
print(root_path)
# Вывод: /путь/к/корневому/каталогу
```
```python
from pathlib import Path
root_path:Path = set_project_root()
print(root_path)
# Вывод: /путь/к/корневому/каталогу
```
```python
from pathlib import Path
root_path:Path = set_project_root()
print(root_path)
# Вывод: /путь/к/корневому/каталогу
```
```python
from pathlib import Path
root_path:Path = set_project_root()
print(root_path)
# Вывод: /путь/к/корневому/каталогу
```
```python
from pathlib import Path
root_path:Path = set_project_root()
print(root_path)
# Вывод: /путь/к/корневому/каталогу
```
```python
from pathlib import Path
root_path:Path = set_project_root()
print(root_path)
# Вывод: /путь/к/корневому/каталогу
```
```python
from pathlib import Path
root_path:Path = set_project_root()
print(root_path)
# Вывод: /путь/к/корневому/каталогу
```
```python
from pathlib import Path
root_path:Path = set_project_root()
print(root_path)
# Вывод: /путь/к/корневому/каталогу
```
```python
from pathlib import Path
root_path:Path = set_project_root()
print(root_path)
# Вывод: /путь/к/корневому/каталогу
```
```python
from pathlib import Path
root_path:Path = set_project_root()
print(root_path)
# Вывод: /путь/к/корневому/каталогу
```
```python
from pathlib import Path
root_path:Path = set_project_root()
print(root_path)
# Вывод: /путь/к/корневому/каталогу
```
```python
from pathlib import Path
root_path:Path = set_project_root()
print(root_path)
# Вывод: /путь/к/корневому/каталогу
```
```python
from pathlib import Path
root_path:Path = set_project_root()
print(root_path)
# Вывод: /путь/к/корневому/каталогу
```
```python
from pathlib import Path
root_path:Path = set_project_root()
print(root_path)
# Вывод: /путь/к/корневому/каталогу
```
```python
from pathlib import Path
root_path:Path = set_project_root()
print(root_path)
# Вывод: /путь/к/корневому/каталогу
```
```python
from pathlib import Path
root_path:Path = set_project_root()
print(root_path)
# Вывод: /путь/к/корневому/каталогу
```
```python
from pathlib import Path
root_path:Path = set_project_root()
print(root_path)
# Вывод: /путь/к/корневому/каталогу
```
```python
from pathlib import Path
root_path:Path = set_project_root()
print(root_path)
# Вывод: /путь/к/корневому/каталогу
```
```python
from pathlib import Path
root_path:Path = set_project_root()
print(root_path)
# Вывод: /путь/к/корневому/каталогу
```
```python
from pathlib import Path
root_path:Path = set_project_root()
print(root_path)
# Вывод: /путь/к/корневому/каталогу
```
```python
from pathlib import Path
root_path:Path = set_project_root()
print(root_path)
# Вывод: /путь/к/корневому/каталогу
```
```python
from pathlib import Path
root_path:Path = set_project_root()
print(root_path)
# Вывод: /путь/к/корневому/каталогу
```
```python
from pathlib import Path
root_path:Path = set_project_root()
print(root_path)
# Вывод: /путь/к/корневому/каталогу
```
```python
from pathlib import Path
root_path:Path = set_project_root()
print(root_path)
# Вывод: /путь/к/корневому/каталогу
```
```python
from pathlib import Path
root_path:Path = set_project_root()
print(root_path)
# Вывод: /путь/к/корневому/каталогу
```
```python
from pathlib import Path
root_path:Path = set_project_root()
print(root_path)
# Вывод: /путь/к/корневому/каталогу
```
```python
from pathlib import Path
root_path:Path = set_project_root()
print(root_path)
# Вывод: /путь/к/корневому/каталогу
```
```python
from pathlib import Path
root_path:Path = set_project_root()
print(root_path)
# Вывод: /путь/к/корневому/каталогу
```
```python
from pathlib import Path
root_path:Path = set_project_root()
print(root_path)
# Вывод: /путь/к/корневому/каталогу
```
```python
from pathlib import Path
root_path:Path = set_project_root()
print(root_path)
# Вывод: /путь/к/корневому/каталогу
```
```python
from pathlib import Path
root_path:Path = set_project_root()
print(root_path)
# Вывод: /путь/к/корневому/каталогу
```
```python
from pathlib import Path
root_path:Path = set_project_root()
print(root_path)
# Вывод: /путь/к/корневому/каталогу
```
```python
from pathlib import Path
root_path:Path = set_project_root()
print(root_path)
# Вывод: /путь/к/корневому/каталогу
```
```python
from pathlib import Path
root_path:Path = set_project_root()
print(root_path)
# Вывод: /путь/к/корневому/каталогу
```
```python
from pathlib import Path
root_path:Path = set_project_root()
print(root_path)
# Вывод: /путь/к/корневому/каталогу
```
```python
from pathlib import Path
root_path:Path = set_project_root()
print(root_path)
# Вывод: /путь/к/корневому/каталогу
```
```python
from pathlib import Path
root_path:Path = set_project_root()
print(root_path)
# Вывод: /путь/к/корневому/каталогу
```
```python
from pathlib import Path
root_path:Path = set_project_root()
print(root_path)
# Вывод: /путь/к/корневому/каталогу
```
```python
from pathlib import Path
root_path:Path = set_project_root()
print(root_path)
# Вывод: /путь/к/корневому/каталогу
```
```python
from pathlib import Path
root_path:Path = set_project_root()
print(root_path)
# Вывод: /путь/к/корневому/каталогу
```
```python
from pathlib import Path
root_path:Path = set_project_root()
print(root_path)
# Вывод: /путь/к/корневому/каталогу
```
```python
from pathlib import Path
root_path:Path = set_project_root()
print(root_path)
# Вывод: /путь/к/корневому/каталогу
```
```python
from pathlib import Path
root_path:Path = set_project_root()
print(root_path)
# Вывод: /путь/к/корневому/каталогу
```
```python
from pathlib import Path
root_path:Path = set_project_root()
print(root_path)
# Вывод: /путь/к/корневому/каталогу
```
```python
from pathlib import Path
root_path:Path = set_project_root()
print(root_path)
# Вывод: /путь/к/корневому/каталогу
```
```python
from pathlib import Path
root_path:Path = set_project_root()
print(root_path)
# Вывод: /путь/к/корневому/каталогу
```
```python
from pathlib import Path
root_path:Path = set_project_root()
print(root_path)
# Вывод: /путь/к/корневому/каталогу
```
```python
from pathlib import Path
root_path:Path = set_project_root()
print(root_path)
# Вывод: /путь/к/корневому/каталогу
```
```python
from pathlib import Path
root_path:Path = set_project_root()
print(root_path)
# Вывод: /путь/к/корневому/каталогу
```
```python
from pathlib import Path
root_path:Path = set_project_root()
print(root_path)
# Вывод: /путь/к/корневому/каталогу
```
```python
from pathlib import Path
root_path:Path = set_project_root()
print(root_path)
# Вывод: /путь/к/корневому/каталогу
```
```python
from pathlib import Path
root_path:Path = set_project_root()
print(root_path)
# Вывод: /путь/к/корневому/каталогу
```
```python
from pathlib import Path
root_path:Path = set_project_root()
print(root_path)
# Вывод: /путь/к/корневому/каталогу
```
```python
from pathlib import Path
root_path:Path = set_project_root()
print(root_path)
# Вывод: /путь/к/корневому/каталогу
```
```python
from pathlib import Path
root_path:Path = set_project_root()
print(root_path)
# Вывод: /путь/к/корневому/каталогу
```
```python
from pathlib import Path
root_path:Path = set_project_root()
print(root_path)
# Вывод: /путь/к/корневому/каталогу
```
```python
from pathlib import Path
root_path:Path = set_project_root()
print(root_path)
# Вывод: /путь/к/корневому/каталогу
```
```python
from pathlib import Path
root_path:Path = set_project_root()
print(root_path)
# Вывод: /путь/к/корневому/каталогу
```
```python
from pathlib import Path
root_path:Path = set_project_root()
print(root_path)
# Вывод: /путь/к/корневому/каталогу
```
```python
from pathlib import Path
root_path:Path = set_project_root()
print(root_path)
# Вывод: /путь/к/корневому/каталогу
```
```python
from pathlib import Path
root_path:Path = set_project_root()
print(root_path)
# Вывод: /путь/к/корневому/каталогу
```
```python
from pathlib import Path
root_path:Path = set_project_root()
print(root_path)
# Вывод: /путь/к/корневому/каталогу
```
```python
from pathlib import Path
root_path:Path = set_project_root()
print(root_path)
# Вывод: /путь/к/корневому/каталогу
```
```python
from pathlib import Path
root_path:Path = set_project_root()
print(root_path)
# Вывод: /путь/к/корневому/каталогу
```
```python
from pathlib import Path
root_path:Path = set_project_root()
print(root_path)
# Вывод: /путь/к/корневому/каталогу
```
```python
from pathlib import Path
root_path:Path = set_project_root()
print(root_path)
# Вывод: /путь/к/корневому/каталогу
```
```python
from pathlib import Path
root_path:Path = set_project_root()
print(root_path)
# Вывод: /путь/к/корневому/каталогу
```
```python
from pathlib import Path
root_path:Path = set_project_root()
print(root_path)
# Вывод: /путь/к/корневому/каталогу
```
```python
from pathlib import Path
root_path:Path = set_project_root()
print(root_path)
# Вывод: /путь/к/корневому/каталогу
```
```python
from pathlib import Path
root_path:Path = set_project_root()
print(root_path)
# Вывод: /путь/к/корневому/каталогу
```
```python
from pathlib import Path
root_path:Path = set_project_root()
print(root_path)
# Вывод: /путь/к/корневому/каталогу
```
```python
from pathlib import Path
root_path:Path = set_project_root()
print(root_path)
# Вывод: /путь/к/корневому/каталогу
```
```python
from pathlib import Path
root_path:Path = set_project_root()
print(root_path)
# Вывод: /путь/к/корневому/каталогу
```
```python
from pathlib import Path
root_path:Path = set_project_root()
print(root_path)
# Вывод: /путь/к/корневому/каталогу
```
```python
from pathlib import Path
root_path:Path = set_project_root()
print(root_path)
# Вывод: /путь/к/корневому/каталогу
```
```python
from pathlib import Path
root_path:Path = set_project_root()
print(root_path)
# Вывод: /путь/к/корневому/каталогу
```
```python
from pathlib import Path
root_path:Path = set_project_root()
print(root_path)
# Вывод: /путь/к/корневому/каталогу
```
```python
from pathlib import Path
root_path:Path = set_project_root()
print(root_path)
# Вывод: /путь/к/корневому/каталогу
```
```python
from pathlib import Path
root_path:Path = set_project_root()
print(root_path)
# Вывод: /путь/к/корневому/каталогу
```
```python
from pathlib import Path
root_path:Path = set_project_root()
print(root_path)
# Вывод: /путь/к/корневому/каталогу
```
```python
from pathlib import Path
root_path:Path = set_project_root()
print(root_path)
# Вывод: /путь/к/корневому/каталогу
```
```python
from pathlib import Path
root_path:Path = set_project_root()
print(root_path)
# Вывод: /путь/к/корневому/каталогу
```
```python
from pathlib import Path
root_path:Path = set_project_root()
print(root_path)
# Вывод: /путь/к/корневому/каталогу
```
```python
from pathlib import Path
root_path:Path = set_project_root()
print(root_path)
# Вывод: /путь/к/корневому/каталогу
```
```python
from pathlib import Path
root_path:Path = set_project_root()
print(root_path)
# Вывод: /путь/к/корневому/каталогу
```
```python
from pathlib import Path
root_path:Path = set_project_root()
print(root_path)
# Вывод: /путь/к/корневому/каталогу
```
```python
from pathlib import Path
root_path:Path = set_project_root()
print(root_path)
# Вывод: /путь/к/корневому/каталогу
```
```python
from pathlib import Path
root_path:Path = set_project_root()
print(root_path)
# Вывод: /путь/к/корневому/каталогу
```
```python
from pathlib import Path
root_path:Path = set_project_root()
print(root_path)
# Вывод: /путь/к/корневому/каталогу
```
```python
from pathlib import Path
root_path:Path = set_project_root()
print(root_path)
# Вывод: /путь/к/корневому/каталогу
```
```python
from pathlib import Path
root_path:Path = set_project_root()
print(root_path)
# Вывод: /путь/к/корневому/каталогу
```
```python
from pathlib import Path
root_path:Path = set_project_root()
print(root_path)
# Вывод: /путь/к/корневому/каталогу
```
```python
from pathlib import Path
root_path:Path = set_project_root()
print(root_path)
# Вывод: /путь/к/корневому/каталогу
```
```python
from pathlib import Path
root_path:Path = set_project_root()
print(root_path)
# Вывод: /путь/к/корневому/каталогу
```
```python
from pathlib import Path
root_path:Path = set_project_root()
print(root_path)
# Вывод: /путь/к/корневому/каталогу
```
```python
from pathlib import Path
root_path:Path = set_project_root()
print(root_path)
# Вывод: /путь/к/корневому/каталогу
```
```python
from pathlib import Path
root_path:Path = set_project_root()
print(root_path)
# Вывод: /путь/к/корневому/каталогу
```
```python
from pathlib import Path
root_path:Path = set_project_root()
print(root_path)
# Вывод: /путь/к/корневому/каталогу
```
```python
from pathlib import Path
root_path:Path = set_project_root()
print(root_path)
# Вывод: /путь/к/корневому/каталогу
```
```python
from pathlib import Path
root_path:Path = set_project_root()
print(root_path)
# Вывод: /путь/к/корневому/каталогу
```
```python
from pathlib import Path
root_path:Path = set_project_root()
print(root_path)
# Вывод: /путь/к/корневому/каталогу
```
```python
from pathlib import Path
root_path:Path = set_project_root()
print(root_path)
# Вывод: /путь/к/корневому/каталогу
```
```python
from pathlib import Path
root_path:Path = set_project_root()
print(root_path)
# Вывод: /путь/к/корневому/каталогу
```
```python
from pathlib import Path
root_path:Path = set_project_root()
print(root_path)
# Вывод: /путь/к/корневому/каталогу
```
```python
from pathlib import Path
root_path:Path = set_project_root()
print(root_path)
# Вывод: /путь/к/корневому/каталогу
```
```python
from pathlib import Path
root_path:Path = set_project_root()
print(root_path)
# Вывод: /путь/к/корневому/каталогу
```
```python
from pathlib import Path
root_path:Path = set_project_root()
print(root_path)
# Вывод: /путь/к/корневому/каталогу
```
```python
from pathlib import Path
root_path:Path = set_project_root()
print(root_path)
# Вывод: /путь/к/корневому/каталогу
```
```python
from pathlib import Path
root_path:Path = set_project_root()
print(root_path)
# Вывод: /путь/к/корневому/каталогу
```
```python
from pathlib import Path
root_path:Path = set_project_root()
print(root_path)
# Вывод: /путь/к/корневому/каталогу
```
```python
from pathlib import Path
root_path:Path = set_project_root()
print(root_path)
# Вывод: /путь/к/корневому/каталогу
```
```python
from pathlib import Path
root_path:Path = set_project_root()
print(root_path)
# Вывод: /путь/к/корневому/каталогу
```
```python
from pathlib import Path
root_path:Path = set_project_root()
print(root_path)
# Вывод: /путь/к/корневому/каталогу
```
```python
from pathlib import Path
root_path:Path = set_project_root()
print(root_path)
# Вывод: /путь/к/корневому/каталогу
```
```python
from pathlib import Path
root_path:Path = set_project_root()
print(root_path)
# Вывод: /путь/к/корневому/каталогу
```
```python
from pathlib import Path
root_path:Path = set_project_root()
print(root_path)
# Вывод: /путь/к/корневому/каталогу
```
```python
from pathlib import Path
root_path:Path = set_project_root()
print(root_path)
# Вывод: /путь/к/корневому/каталогу
```
```python
from pathlib import Path
root_path:Path = set_project_root()
print(root_path)
# Вывод: /путь/к/корневому/каталогу
```
```python
from pathlib import Path
root_path:Path = set_project_root()
print(root_path)
# Вывод: /путь/к/корневому/каталогу
```
```python
from pathlib import Path
root_path:Path = set_project_root()
print(root_path)
# Вывод: /путь/к/корневому/каталогу
```
```python
from pathlib import Path
root_path:Path = set_project_root()
print(root_path)
# Вывод: /путь/к/корневому/каталогу
```
```python
from pathlib import Path
root_path:Path = set_project_root()
print(root_path)
# Вывод: /путь/к/корневому/каталогу
```
```python
from pathlib import Path
root_path:Path = set_project_root()
print(root_path)
# Вывод: /путь/к/корневому/каталогу
```
```python
from pathlib import Path
root_path:Path = set_project_root()
print(root_path)
# Вывод: /путь/к/корневому/каталогу
```
```python
from pathlib import Path
root_path:Path = set_project_root()
print(root_path)
# Вывод: /путь/к/корневому/каталогу
```
```python
from pathlib import Path
root_path:Path = set_project_root()
print(root_path)
# Вывод: /путь/к/корневому/каталогу
```
```python
from pathlib import Path
root_path:Path = set_project_root()
print(root_path)
# Вывод: /путь/к/корневому/каталогу
```
```python
from pathlib import Path
root_path:Path = set_project_root()
print(root_path)
# Вывод: /путь/к/корневому/каталогу
```
```python
from pathlib import Path
root_path:Path = set_project_root()
print(root_path)
# Вывод: /путь/к/корневому/каталогу
```
```python
from pathlib import Path
root_path:Path = set_project_root()
print(root_path)
# Вывод: /путь/к/корневому/каталогу
```
```python
from pathlib import Path
root_path:Path = set_project_root()
print(root_path)
# Вывод: /путь/к/корневому/каталогу
```
```python
from pathlib import Path
root_path:Path = set_project_root()
print(root_path)
# Вывод: /путь/к/корневому/каталогу
```
```python
from pathlib import Path
root_path:Path = set_project_root()
print(root_path)
# Вывод: /путь/к/корневому/каталогу
```
```python
from pathlib import Path
root_path:Path = set_project_root()
print(root_path)
# Вывод: /путь/к/корневому/каталогу
```
```python
from pathlib import Path
root_path:Path = set_project_root()
print(root_path)
# Вывод: /путь/к/корневому/каталогу
```
```python
from pathlib import Path
root_path:Path = set_project_root()
print(root_path)
# Вывод: /путь/к/корневому/каталогу
```
```python
from pathlib import Path
root_path:Path = set_project_root()
print(root_path)
# Вывод: /путь/к/корневому/каталогу
```
```python
from pathlib import Path
root_path:Path = set_project_root()
print(root_path)
# Вывод: /путь/к/корневому/каталогу
```
```python
from pathlib import Path
root_path:Path = set_project_root()
print(root_path)
# Вывод: /путь/к/корневому/каталогу
```
```python
from pathlib import Path
root_path:Path = set_project_root()
print(root_path)
# Вывод: /путь/к/корневому/каталогу
```
```python
from pathlib import Path
root_path:Path = set_project_root()
print(root_path)
# Вывод: /путь/к/корневому/каталогу
```
```python
from pathlib import Path
root_path:Path = set_project_root()
print(root_path)
# Вывод: /путь/к/корневому/каталогу
```
```python
from pathlib import Path
root_path:Path = set_project_root()
print(root_path)
# Вывод: /путь/к/корневому/каталогу
```
```python
from pathlib import Path
root_path:Path = set_project_root()
print(root_path)
# Вывод: /путь/к/корневому/каталогу
```
```python
from pathlib import Path
root_path:Path = set_project_root()
print(root_path)
# Вывод: /путь/к/корневому/каталогу
```
```python
from pathlib import Path
root_path:Path = set_project_root()
print(root_path)
# Вывод: /путь/к/корневому/каталогу
```
```python
from pathlib import Path
root_path:Path = set_project_root()
print(root_path)
# Вывод: /путь/к/корневому/каталогу
```
```python
from pathlib import Path
root_path:Path = set_project_root()
print(root_path)
# Вывод: /путь/к/корневому/каталогу
```
```python
from pathlib import Path
root_path:Path = set_project_root()
print(root_path)
# Вывод: /путь/к/корневому/каталогу
```
```python
from pathlib import Path
root_path:Path = set_project_root()
print(root_path)
# Вывод: /путь/к/корневому/каталогу
```
```python
from pathlib import Path
root_path:Path = set_project_root()
print(root_path)
# Вывод: /путь/к/корневому/каталогу
```
```python
from pathlib import Path
root_path:Path = set_project_root()
print(root_path)
# Вывод: /путь/к/корневому/каталогу
```
```python
from pathlib import Path
root_path:Path = set_project_root()
print(root_path)
# Вывод: /путь/к/корневому/каталогу
```
```python
from pathlib import Path
root_path:Path = set_project_root()
print(root_path)
# Вывод: /путь/к/корневому/каталогу
```
```python
from pathlib import Path
root_path:Path = set_project_root()
print(root_path)
# Вывод: /путь/к/корневому/каталогу
```
```python
from pathlib import Path
root_path:Path = set_project_root()
print(