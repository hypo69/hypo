# Модуль `header.py`

## Обзор

Модуль `header.py` предназначен для определения корневой директории проекта, загрузки настроек из файла `settings.json` и чтения содержимого файла `README.MD`. Он также устанавливает глобальные переменные, такие как имя проекта, версия, авторские права и т.д.

## Подробней

Этот модуль выполняет несколько ключевых задач:

1.  **Определение корневой директории проекта**: Функция `set_project_root` используется для поиска корневой директории проекта на основе наличия определенных файлов-маркеров (например, `__root__` или `.git`). Это позволяет скрипту определять свое местоположение относительно корня проекта, независимо от того, где он запущен.
2.  **Загрузка настроек**: Модуль пытается загрузить настройки из файла `settings.json`, расположенного в корне проекта. Если файл не найден или содержит ошибки JSON, выполнение продолжается с использованием значений по умолчанию.
3.  **Чтение документации**: Модуль пытается прочитать содержимое файла `README.MD`, расположенного в корне проекта, для использования в качестве документации проекта.
4.  **Установка глобальных переменных**: На основе загруженных настроек или значений по умолчанию модуль устанавливает глобальные переменные, такие как имя проекта, версия, автор, авторские права и сообщение о поддержке разработчиков.

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

**Описание**: Находит корневую директорию проекта, начиная с директории текущего файла, и останавливается на первой директории, содержащей любой из файлов-маркеров.

**Параметры**:

*   `marker_files` (tuple): Кортеж имен файлов или директорий для идентификации корня проекта. По умолчанию `('__root__', '.git')`.

**Возвращает**:

*   `Path`: Путь к корневой директории, если она найдена, иначе - директория, где расположен скрипт.

**Примеры**:

```python
from pathlib import Path
# Создадим временные файлы и директории для демонстрации
temp_dir = Path('./temp_test_root')
temp_dir.mkdir(exist_ok=True)
(temp_dir / '__root__').touch()

root_path = set_project_root()
print(f"Root path: {root_path}")

# Очистка
import shutil
shutil.rmtree(temp_dir)