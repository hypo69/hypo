# Модуль `get_images`

## Обзор

Модуль предназначен для получения списка изображений, сгенерированных ИИ, из определенной директории. Он использует функции для рекурсивного поиска файлов изображений с заданными расширениями.

## Подробней

Данный модуль предназначен для экспериментов, связанных с изображениями, сгенерированными ИИ. Он сканирует указанную директорию в поисках файлов с расширениями `.jpeg`, `.jpg` и `.png`, и возвращает список путей к этим файлам. Модуль использует функции из других модулей проекта, таких как `recursively_get_filepath` для поиска файлов и `pprint` для вывода результатов.

## Функции

### `read_text_file`

```python
def read_text_file(
    file_path: str | Path,
    as_list: bool = False,
    extensions: Optional[list[str]] = None,
    chunk_size: int = 8192
) -> Generator[str, None, None] | str | None:
    """
    Считывает содержимое файла (или файлов из каталога) с использованием генератора для экономии памяти.

    :param file_path: Путь к файлу или каталогу.
    :param as_list: Если `True`, возвращает генератор строк.
    :param extensions: Список расширений файлов для чтения из каталога.
    :param chunk_size: Размер чанков для чтения файла в байтах.

    :returns: Генератор строк, объединенная строка или `None` в случае ошибки.

    :raises Exception: Если возникает ошибка при чтении файла.

    Пример:
        >>> from pathlib import Path
        >>> file_path = Path('example.txt')
        >>> content = read_text_file(file_path)
        >>> if content:
        ...    print(f'File content: {content[:100]}...')
        File content: Example text...
    """
```

**Описание**: Функция для чтения текстовых файлов или файлов из каталога.

**Параметры**:
- `file_path` (str | Path): Путь к файлу или каталогу.
- `as_list` (bool, optional): Если `True`, возвращает генератор строк. По умолчанию `False`.
- `extensions` (Optional[list[str]], optional): Список расширений файлов для чтения из каталога. По умолчанию `None`.
- `chunk_size` (int, optional): Размер чанков для чтения файла в байтах. По умолчанию `8192`.

**Возвращает**:
- `Generator[str, None, None] | str | None`: Генератор строк, объединенная строка или `None` в случае ошибки.

**Вызывает исключения**:
- `Exception`: Если возникает ошибка при чтении файла.

**Примеры**:

```python
from pathlib import Path
file_path = Path('example.txt')
content = read_text_file(file_path)
if content:
    print(f'File content: {content[:100]}...')
```

### `save_text_file`

```python
def save_text_file(file_path: str | Path, content: str, encoding: str = 'utf-8') -> None:
    """
    Сохраняет текстовое содержимое в файл.

    :param file_path: Путь к файлу.
    :param content: Текстовое содержимое для сохранения.
    :param encoding: Кодировка файла.

    :raises Exception: Если возникает ошибка при записи в файл.

    Пример:
        >>> from pathlib import Path
        >>> file_path = Path('example.txt')
        >>> content = 'Example text'
        >>> save_text_file(file_path, content)
    """
```

**Описание**: Функция для сохранения текстового содержимого в файл.

**Параметры**:
- `file_path` (str | Path): Путь к файлу.
- `content` (str): Текстовое содержимое для сохранения.
- `encoding` (str, optional): Кодировка файла. По умолчанию `'utf-8'`.

**Возвращает**:
- `None`: Функция ничего не возвращает.

**Вызывает исключения**:
- `Exception`: Если возникает ошибка при записи в файл.

**Примеры**:

```python
from pathlib import Path
file_path = Path('example.txt')
content = 'Example text'
save_text_file(file_path, content)
```

### `recursively_get_filepath`

```python
def recursively_get_filepath(dir_path: str | Path, file_masks: list[str] = ['*']) -> list[Path]:
    """
    Рекурсивно получает список путей файлов, соответствующих заданным маскам, в указанной директории.

    :param dir_path: Путь к директории.
    :param file_masks: Список масок файлов для поиска.

    :returns: Список путей к найденным файлам.

    Пример:
        >>> from pathlib import Path
        >>> dir_path = Path('.')
        >>> file_masks = ['*.txt', '*.log']
        >>> files = recursively_get_filepath(dir_path, file_masks)
        >>> print(files)
        [Path('file1.txt'), Path('file2.log')]
    """
```

**Описание**: Функция для рекурсивного получения списка путей файлов, соответствующих заданным маскам, в указанной директории.

**Параметры**:
- `dir_path` (str | Path): Путь к директории.
- `file_masks` (list[str], optional): Список масок файлов для поиска. По умолчанию `['*']`.

**Возвращает**:
- `list[Path]`: Список путей к найденным файлам.

**Примеры**:

```python
from pathlib import Path
dir_path = Path('.')
file_masks = ['*.txt', '*.log']
files = recursively_get_filepath(dir_path, file_masks)
print(files)
```

### `pprint`

```python
def pprint(*args, **kwargs) -> None:
    """
    Wrapper around `pprint.pprint` to handle encoding errors.
    """
```

**Описание**: Функция-обертка для `pprint.pprint` для обработки ошибок кодировки.

**Параметры**:
- `*args`: Аргументы, передаваемые в `pprint.pprint`.
- `**kwargs`: Ключевые аргументы, передаваемые в `pprint.pprint`.

**Возвращает**:
- `None`: Функция ничего не возвращает.

**Примеры**:
```python
data = {'key1': 'value1', 'key2': 'value2'}
pprint(data)
```