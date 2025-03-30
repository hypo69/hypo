# Модуль `make_summary`

## Обзор

Модуль `make_summary` предназначен для автоматического создания файла `SUMMARY.md`, используемого для формирования структуры книги в формате `mdbook`. Он рекурсивно обходит указанную директорию с исходными файлами (`.md`) и генерирует содержание книги, фильтруя файлы по языку (русский или английский).

## Подробней

Этот модуль является частью процесса подготовки документации для проекта `hypotez`. Он облегчает создание и обновление структуры документации, автоматически добавляя ссылки на все файлы `.md`, найденные в директории `src`. Функция фильтрации по языку позволяет создавать отдельные версии документации для разных языковых аудиторий.

## Функции

### `make_summary`

```python
def make_summary(docs_dir: Path, lang: str = 'en') -> None:
    """
    Создает файл SUMMARY.md, рекурсивно обходя папку.

    Args:
        docs_dir (Path): Путь к исходной директории 'src'.
        lang (str): Язык фильтрации файлов. Возможные значения: 'ru' или 'en'.
    """
```

**Описание**: Создает файл `SUMMARY.md`, который служит оглавлением для `mdbook`. Рекурсивно обходит указанную директорию `docs_dir` и добавляет в `SUMMARY.md` ссылки на все `.md` файлы, отфильтрованные по языку `lang`.

**Параметры**:
- `docs_dir` (Path): Путь к исходной директории, содержащей `.md` файлы. Обычно это директория `src`.
- `lang` (str, optional): Язык, по которому фильтруются файлы. Может принимать значения `'ru'` (русский) или `'en'` (английский). По умолчанию `'en'`.

**Возвращает**:
- `None`: Функция ничего не возвращает.

**Примеры**:
```python
from pathlib import Path
import header
PROJECT_ROOT = header.__root__
docs_dir = PROJECT_ROOT / 'src'
make_summary(docs_dir, lang='ru')
```

### `_make_summary`

```python
def _make_summary(src_dir: Path, summary_file: Path, lang: str = 'en') -> bool:
    """
    Рекурсивно обходит папку и создает файл SUMMARY.md с главами на основе .md файлов.

    Args:
        src_dir (Path): Путь к папке с исходниками .md.
        summary_file (Path): Путь для сохранения файла SUMMARY.md.
        lang (str): Язык фильтрации файлов. Возможные значения: 'ru' или 'en'.
    """
```

**Описание**: Внутренняя функция, которая рекурсивно обходит директорию `src_dir` и создает файл `SUMMARY.md` с главами, основанными на `.md` файлах. Фильтрует файлы по языку `lang`.

**Параметры**:
- `src_dir` (Path): Путь к директории с исходными `.md` файлами.
- `summary_file` (Path): Путь, по которому будет сохранен файл `SUMMARY.md`.
- `lang` (str, optional): Язык, по которому фильтруются файлы. Может принимать значения `'ru'` или `'en'`. По умолчанию `'en'`.

**Возвращает**:
- `bool`: Возвращает `True` в случае успешного создания файла `SUMMARY.md`, `False` в случае ошибки.

**Примеры**:
```python
from pathlib import Path
import header
PROJECT_ROOT = header.__root__
src_dir = PROJECT_ROOT / 'src'
summary_file = PROJECT_ROOT / 'docs' / 'SUMMARY.md'
_make_summary(src_dir, summary_file, lang='en')
```

### `prepare_summary_path`

```python
def prepare_summary_path(src_dir: Path, file_name: str = 'SUMMARY.md') -> Path:
    """
    Формирует путь к файлу, заменяя часть пути 'src' на 'docs' и добавляя имя файла.

    Args:
        src_dir (Path): Исходный путь с 'src'.
        file_name (str): Имя файла, который нужно создать. По умолчанию 'SUMMARY.md'.

    Returns:
        Path: Новый путь к файлу.
    """
```

**Описание**: Формирует путь к файлу `SUMMARY.md` в директории `docs`, заменяя часть пути `src` на `docs`.

**Параметры**:
- `src_dir` (Path): Исходный путь к директории `src`.
- `file_name` (str, optional): Имя файла, который нужно создать. По умолчанию `'SUMMARY.md'`.

**Возвращает**:
- `Path`: Новый путь к файлу `SUMMARY.md` в директории `docs`.

**Примеры**:
```python
from pathlib import Path
import header
PROJECT_ROOT = header.__root__
src_dir = PROJECT_ROOT / 'src'
summary_path = prepare_summary_path(src_dir)
print(summary_path)
```