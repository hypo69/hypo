# Модуль `src.utils.file`

## Обзор

Модуль `src.utils.file` предоставляет набор утилит для работы с файлами, включая чтение, запись, поиск и другие операции. Он предназначен для упрощения взаимодействия с файловой системой и обеспечивает удобные функции для обработки текстовых данных.

## Подробней

Этот модуль содержит функции для сохранения данных в текстовые файлы, чтения содержимого файлов (как целиком, так и построчно с использованием генераторов для экономии памяти), получения списков файлов в директориях (с возможностью фильтрации по расширениям и шаблонам), рекурсивного поиска файлов, а также для удаления BOM (Byte Order Mark) из файлов. Модуль предназначен для использования в проектах, где требуется интенсивная работа с файлами, и предоставляет инструменты для эффективной обработки больших объемов текстовых данных. Расположен в корневой директории `src/utils/file.py`.

## Функции

### `save_text_file`

```python
def save_text_file(
    file_path: str | Path,
    data: str | list[str] | dict,
    mode: str = 'w'
) -> bool:
    """
    Сохраняет данные в текстовый файл.

    Args:
        file_path (str | Path): Путь к файлу для сохранения.
        data (str | list[str] | dict): Данные для записи. Могут быть строкой, списком строк или словарем.
        mode (str, optional): Режим записи файла ('w' для записи, 'a' для добавления).
    Returns:
        bool: `True`, если файл успешно сохранен, `False` в противном случае.
    Raises:
        Exception: При возникновении ошибки при записи в файл.

    Example:
        >>> from pathlib import Path
        >>> file_path = Path('example.txt')
        >>> data = 'Пример текста'
        >>> result = save_text_file(file_path, data)
        >>> print(result)
        True
    """
```

**Описание**: Сохраняет переданные данные в текстовый файл. Поддерживает запись строк, списков строк и словарей.

**Параметры**:
- `file_path` (str | Path): Путь к файлу, в который будут записаны данные.
- `data` (str | list[str] | dict): Данные для записи. Может быть строкой, списком строк или словарем.
- `mode` (str, optional): Режим открытия файла. `'w'` - для записи (перезаписи), `'a'` - для добавления. По умолчанию `'w'`.

**Возвращает**:
- `bool`: `True`, если данные успешно записаны в файл, и `False` в случае ошибки.

**Вызывает исключения**:
- `Exception`: Возникает при ошибке записи в файл.

**Примеры**:

```python
from pathlib import Path
file_path = Path('example.txt')
data = 'Пример текста'
result = save_text_file(file_path, data)
print(result)
```

### `read_text_file_generator`

```python
def read_text_file_generator(
    file_path: str | Path,
    as_list: bool = False,
    extensions: Optional[list[str]] = None,
    chunk_size: int = 8192,
    recursive: bool = False,
    patterns: Optional[str | list[str]] = None,
) -> Generator[str, None, None] | str | list[str] | None:
    """
    Читает содержимое файла(ов) или директории.

        Args:
            file_path (str | Path): Путь к файлу или директории.
            as_list (bool, optional): Если `True`, то возвращает генератор строк или список строк, в зависимости от типа вывода.
            extensions (list[str], optional): Список расширений файлов для включения при чтении директории.
            chunk_size (int, optional): Размер чанка для чтения файла в байтах.
            recursive (bool, optional): Если `True`, то поиск файлов выполняется рекурсивно.
            patterns (str | list[str], optional): Шаблоны для фильтрации файлов при рекурсивном поиске.

        Returns:
            Generator[str, None, None] | str | list[str] | None:
            - Если `as_list` is True и `file_path` является файлом, возвращает генератор строк.
            - Если `as_list` is True и `file_path` является директорией и `recursive` is True, возвращает список строк.
            - Если `as_list` is False и `file_path` является файлом, возвращает строку.
            - Если `as_list` is False и `file_path` является директорией, возвращает объединенную строку.
            - Возвращает `None` в случае ошибки.
        Raises:
            Exception: При возникновении ошибки при чтении файла.

        Example:
            >>> from pathlib import Path
            >>> file_path = Path('example.txt')
            >>> content = read_text_file(file_path)\n    >>> if content:\n    ...    print(f'File content: {content[:100]}...')\n    File content: Пример текста...\n    Функция read_text_file может возвращать несколько разных типов данных в зависимости от входных параметров:\n\n    Возвращаемые значения:\n    ----------------------\n\n    - Generator[str, None, None] (Генератор строк):\n        Генератор при итерации выдаёт строки из файла(ов) по одной. Эффективно для работы с большими файлами, так как они не загружаются полностью в память.\n        - Когда:\n            file_path – это файл и as_list равен True.\n            file_path – это директория, recursive равен True и as_list равен True. При этом в генератор попадают строки из всех найденных файлов.\n            file_path – это директория, recursive равен False и as_list равен True. При этом в генератор попадают строки из всех найденных файлов в текущей директории.\n        \n    - str (Строка):\n        Содержимое файла или объединенное содержимое всех файлов в виде одной строки.\n        - Когда:\n            file_path – это файл и as_list равен False.\n            file_path – это директория, recursive равен False и as_list равен False. При этом возвращается объединенная строка, состоящая из содержимого всех файлов в директории, разделенных символами новой строки (\\n).\n            file_path – это директория, recursive равен True и as_list равен False. При этом возвращается объединенная строка, состоящая из содержимого всех файлов в директории и её поддиректориях, разделенных символами новой строки (\\n).\n \n    - list[str] (Список строк):\n        Этот тип явно не возвращается функцией, однако когда file_path – это директория, recursive равен True и as_list равен True - функция возвращает генератор, который можно преобразовать в список при помощи list()\n        - Когда:\n            file_path – не является ни файлом, ни директорией.\n            Произошла ошибка при чтении файла или директории (например, файл не найден, ошибка доступа и т.п.).\n\n\n    Note:\n        Если вы хотите прочитать содержимое файла построчно (особенно для больших файлов) используйте as_list = True. В этом случае вы получите генератор строк.\n        Если вы хотите получить всё содержимое файла в виде одной строки используйте as_list = False.\n        Если вы работаете с директорией, recursive = True будет обходить все поддиректории.\n        extensions и patterns позволят вам фильтровать файлы при работе с директорией.\n        chunk_size позволяет оптимизировать работу с большими файлами при чтении их по частям.\n        None будет возвращён в случае ошибок.\n\n    Важно помнить:\n        В случае чтения директории, если as_list=False, функция объединяет все содержимое найденных файлов в одну строку. Это может потребовать много памяти, если файлов много или они большие.\n        Функция полагается на другие функции-помощники (_read_file_lines_generator, _read_file_content, recursively_get_file_path, yield_text_from_files), которые здесь не определены и их поведение влияет на результат read_text_file.\n\n
    """
```

**Описание**: Читает содержимое файла или файлов в директории и возвращает его в различных форматах в зависимости от параметров.

**Параметры**:
- `file_path` (str | Path): Путь к файлу или директории.
- `as_list` (bool, optional): Если `True`, возвращает содержимое в виде генератора строк. По умолчанию `False`.
- `extensions` (list[str], optional): Список расширений файлов для чтения из директории. По умолчанию `None`.
- `chunk_size` (int, optional): Размер чанка для чтения файла. По умолчанию `8192`.
- `recursive` (bool, optional): Если `True`, выполняет рекурсивный поиск файлов в директории. По умолчанию `False`.
- `patterns` (str | list[str], optional): Шаблоны для фильтрации файлов. По умолчанию `None`.

**Возвращает**:
- `Generator[str, None, None] | str | list[str] | None`: Возвращает генератор строк, одну строку, список строк, или `None` в случае ошибки.

**Вызывает исключения**:
- `Exception`: Возникает при ошибке чтения файла или директории.

**Примеры**:

```python
from pathlib import Path
file_path = Path('example.txt')
content = read_text_file(file_path)
if content:
    print(f'File content: {content[:100]}...')
```

### `read_text_file`

```python
def read_text_file(
    file_path: Union[str, Path],
    as_list: bool = False,
    extensions: Optional[list[str]] = None,
    exc_info: bool = True,
) -> str | list[str] | None:
    """
    Read the contents of a file.

    Args:
        file_path (str | Path): Path to the file or directory.
        as_list (bool, optional): If True, returns content as list of lines. Defaults to False.
        extensions (list[str], optional): List of file extensions to include if reading a directory. Defaults to None.
        exc_info (bool, optional): If True, logs traceback on error. Defaults to True.

    Returns:
        str | list[str] | None: File content as a string or list of lines, or None if an error occurs.
    """
```

**Описание**: Читает содержимое файла и возвращает его в виде строки или списка строк.

**Параметры**:
- `file_path` (str | Path): Путь к файлу или директории.
- `as_list` (bool, optional): Если `True`, возвращает содержимое в виде списка строк. По умолчанию `False`.
- `extensions` (list[str], optional): Список расширений файлов для чтения из директории. По умолчанию `None`.
- `exc_info` (bool, optional): Если `True`, логирует traceback при ошибке. По умолчанию `True`.

**Возвращает**:
- `str | list[str] | None`: Содержимое файла в виде строки или списка строк, или `None` в случае ошибки.

**Примеры**:

```python
from pathlib import Path
file_path = Path('example.txt')
content = read_text_file(file_path)
print(content)
```

### `yield_text_from_files`

```python
def yield_text_from_files(
    file_path: str | Path,
    as_list: bool = False,
    chunk_size: int = 8192
) -> Generator[str, None, None] | str | None:
    """
    Читает содержимое файла и возвращает его в виде генератора строк или одной строки.

    Args:
        file_path (str | Path): Путь к файлу.
        as_list (bool, optional): Если True, возвращает генератор строк. По умолчанию False.
        chunk_size (int, optional): Размер чанка для чтения файла в байтах.

    Returns:
        Generator[str, None, None] | str | None: Генератор строк, объединенная строка или None в случае ошибки.

    Yields:
       str: Строки из файла, если as_list is True.

    Example:
        >>> from pathlib import Path
        >>> file_path = Path('example.txt')
        >>> for line in yield_text_from_files(file_path, as_list=True):
        ...     print(line)
        Первая строка файла
        Вторая строка файла
    """
```

**Описание**: Читает содержимое файла и возвращает его в виде генератора строк или одной строки.

**Параметры**:
- `file_path` (str | Path): Путь к файлу.
- `as_list` (bool, optional): Если `True`, возвращает генератор строк. По умолчанию `False`.
- `chunk_size` (int, optional): Размер чанка для чтения файла в байтах.

**Возвращает**:
- `Generator[str, None, None] | str | None`: Генератор строк, объединенная строка или `None` в случае ошибки.

**Примеры**:

```python
from pathlib import Path
file_path = Path('example.txt')
for line in yield_text_from_files(file_path, as_list=True):
    print(line)
```

### `_read_file_content`

```python
def _read_file_content(file_path: Path, chunk_size: int) -> str:
    """
    Читает содержимое файла по чанкам и возвращает как строку.

    Args:
        file_path (Path): Путь к файлу для чтения.
        chunk_size (int): Размер чанка для чтения файла в байтах.
    Returns:
        str: Содержимое файла в виде строки.
    Raises:
        Exception: При возникновении ошибки при чтении файла.
    """
```

**Описание**: Читает содержимое файла по частям (чанкам) и возвращает его в виде одной строки.

**Параметры**:
- `file_path` (Path): Путь к файлу, который нужно прочитать.
- `chunk_size` (int): Размер чанка (в байтах) для чтения файла.

**Возвращает**:
- `str`: Строка, содержащая все содержимое файла.

**Вызывает исключения**:
- `Exception`: Если возникает ошибка при чтении файла.

### `_read_file_lines_generator`

```python
def _read_file_lines_generator(file_path: Path, chunk_size: int) -> Generator[str, None, None]:
    """
    Читает файл по строкам с помощью генератора.

    Args:
        file_path (Path): Путь к файлу для чтения.
        chunk_size (int): Размер чанка для чтения файла в байтах.
    Yields:
        str: Строки из файла.
    Raises:
        Exception: При возникновении ошибки при чтении файла.
    """
```

**Описание**: Читает содержимое файла построчно, используя генератор для экономии памяти.

**Параметры**:
- `file_path` (Path): Путь к файлу.
- `chunk_size` (int): Размер чанка для чтения файла в байтах.

**Возвращает**:
- `str`: Каждую строку из файла.

**Вызывает исключения**:
- `Exception`: Если возникает ошибка при чтении файла.

### `get_filenames_from_directory`

```python
def get_filenames_from_directory(
    directory: str | Path, ext: str | list[str] = '*'
) -> list[str]:
    """
    Возвращает список имен файлов в директории, опционально отфильтрованных по расширению.

    Args:
        directory (str | Path): Путь к директории для поиска.
        ext (str | list[str], optional): Расширения для фильтрации.
            По умолчанию '*'.

    Returns:
        list[str]: Список имен файлов, найденных в директории.

    Example:
        >>> from pathlib import Path
        >>> directory = Path('.')
        >>> get_filenames_from_directory(directory, ['.txt', '.md'])
        ['example.txt', 'readme.md']
    """
```

**Описание**: Возвращает список имен файлов в указанной директории, с возможностью фильтрации по расширению.

**Параметры**:
- `directory` (str | Path): Путь к директории.
- `ext` (str | list[str], optional): Расширения файлов для фильтрации. Если `ext` равно `'*'`, то фильтрация не производится. По умолчанию `'*'`.

**Возвращает**:
- `list[str]`: Список имен файлов, найденных в директории.

**Вызывает исключения**:
- `Exception`: Если возникает ошибка при получении списка файлов.

**Примеры**:

```python
from pathlib import Path
directory = Path('.')
get_filenames_from_directory(directory, ['.txt', '.md'])
```

### `recursively_yield_file_path`

```python
def recursively_yield_file_path(
    root_dir: str | Path, patterns: str | list[str] = '*'
) -> Generator[Path, None, None]:
    """
    Рекурсивно возвращает пути ко всем файлам, соответствующим заданным шаблонам, в указанной директории.

    Args:
        root_dir (str | Path): Корневая директория для поиска.
        patterns (str | list[str]): Шаблоны для фильтрации файлов.

    Yields:
        Path: Путь к файлу, соответствующему шаблону.

    Example:
        >>> from pathlib import Path
        >>> root_dir = Path('.')
        >>> for path in recursively_yield_file_path(root_dir, ['*.txt', '*.md']):
        ...    print(path)
        ./example.txt
        ./readme.md
    """
```

**Описание**: Рекурсивно проходит по указанной директории и возвращает пути ко всем файлам, соответствующим заданным шаблонам, в виде генератора.

**Параметры**:
- `root_dir` (str | Path): Корневая директория для поиска.
- `patterns` (str | list[str]): Шаблоны для фильтрации файлов.

**Возвращает**:
- `Path`: Путь к файлу, соответствующему шаблону.

**Вызывает исключения**:
- `Exception`: Если возникает ошибка при рекурсивном поиске файлов.

**Примеры**:

```python
from pathlib import Path
root_dir = Path('.')
for path in recursively_yield_file_path(root_dir, ['*.txt', '*.md']):
    print(path)
```

### `recursively_get_file_path`

```python
def recursively_get_file_path(
    root_dir: str | Path,
    patterns: str | list[str] = '*'
) -> list[Path]:
    """
    Рекурсивно возвращает список путей ко всем файлам, соответствующим заданным шаблонам, в указанной директории.

    Args:
        root_dir (str | Path): Корневая директория для поиска.
        patterns (str | list[str]): Шаблоны для фильтрации файлов.

    Returns:
        list[Path]: Список путей к файлам, соответствующим шаблонам.

    Example:
        >>> from pathlib import Path
        >>> root_dir = Path('.')
        >>> paths = recursively_get_file_path(root_dir, ['*.txt', '*.md'])
        >>> print(paths)
        [Path('./example.txt'), Path('./readme.md')]
    """
```

**Описание**: Рекурсивно возвращает список путей ко всем файлам, соответствующим заданным шаблонам, в указанной директории.

**Параметры**:
- `root_dir` (str | Path): Корневая директория для поиска.
- `patterns` (str | list[str]): Шаблоны для фильтрации файлов.

**Возвращает**:
- `list[Path]`: Список путей к файлам, соответствующим шаблонам.

**Вызывает исключения**:
- `Exception`: Если возникает ошибка при рекурсивном поиске файлов.

**Примеры**:

```python
from pathlib import Path
root_dir = Path('.')
paths = recursively_get_file_path(root_dir, ['*.txt', '*.md'])
print(paths)
```

### `recursively_read_text_files`

```python
def recursively_read_text_files(
    root_dir: str | Path,
    patterns: str | list[str],
    as_list: bool = False
) -> list[str]:
    """
    Рекурсивно читает текстовые файлы из указанной корневой директории, соответствующие заданным шаблонам.

    Args:
        root_dir (str | Path): Путь к корневой директории для поиска.
        patterns (str | list[str]): Шаблон(ы) имени файла для фильтрации.
             Может быть как одиночным шаблоном (например, '*.txt'), так и списком.
        as_list (bool, optional): Если True, то возвращает содержимое файла как список строк.
             По умолчанию `False`.

    Returns:
        list[str]: Список содержимого файлов (или список строк, если `as_list=True`),
         соответствующих заданным шаблонам.

    Example:
        >>> from pathlib import Path
        >>> root_dir = Path('.')
        >>> contents = recursively_read_text_files(root_dir, ['*.txt', '*.md'], as_list=True)
        >>> for line in contents:
        ...     print(line)
        Содержимое example.txt
        Первая строка readme.md
        Вторая строка readme.md
    """
```

**Описание**: Рекурсивно читает текстовые файлы, соответствующие заданным шаблонам, из указанной корневой директории.

**Параметры**:
- `root_dir` (str | Path): Путь к корневой директории для поиска.
- `patterns` (str | list[str]): Шаблоны для фильтрации файлов.
- `as_list` (bool, optional): Если `True`, возвращает содержимое файла как список строк. По умолчанию `False`.

**Возвращает**:
- `list[str]`: Список содержимого файлов (или список строк, если `as_list=True`), соответствующих заданным шаблонам.

**Примеры**:

```python
from pathlib import Path
root_dir = Path('.')
contents = recursively_read_text_files(root_dir, ['*.txt', '*.md'], as_list=True)
for line in contents:
    print(line)
```

### `get_directory_names`

```python
def get_directory_names(directory: str | Path) -> list[str]:
    """
    Возвращает список имен директорий из указанной директории.

    Args:
        directory (str | Path): Путь к директории, из которой нужно получить имена.

    Returns:
        list[str]: Список имен директорий, найденных в указанной директории.

    Example:
        >>> from pathlib import Path
        >>> directory = Path('.')
        >>> get_directory_names(directory)
        ['dir1', 'dir2']
    """
```

**Описание**: Возвращает список имен поддиректорий, находящихся в указанной директории.

**Параметры**:
- `directory` (str | Path): Путь к директории, в которой производится поиск поддиректорий.

**Возвращает**:
- `list[str]`: Список имен поддиректорий.

**Вызывает исключения**:
- `Exception`: Если возникает ошибка при получении списка поддиректорий.

**Примеры**:

```python
from pathlib import Path
directory = Path('.')
get_directory_names(directory)
```

### `remove_bom`

```python
def remove_bom(path: str | Path) -> None:
    """
    Удаляет BOM из текстового файла или из всех файлов Python в директории.

    Args:
        path (str | Path): Путь к файлу или директории.

    Example:
        >>> from pathlib import Path
        >>> file_path = Path('example.txt')
        >>> with open(file_path, 'w', encoding='utf-8') as f:
        ...     f.write('\ufeffПример текста с BOM')
        >>> remove_bom(file_path)
        >>> with open(file_path, 'r', encoding='utf-8') as f:
        ...     print(f.read())
        Пример текста с BOM
    """
```

**Описание**: Удаляет BOM (Byte Order Mark) из текстового файла или из всех файлов Python в указанной директории.

**Параметры**:
- `path` (str | Path): Путь к файлу или директории.

**Возвращает**:
- `None`: Функция ничего не возвращает.

**Вызывает исключения**:
- `Exception`: Если возникает ошибка при удалении BOM из файла.

**Примеры**:

```python
from pathlib import Path
file_path = Path('example.txt')
with open(file_path, 'w', encoding='utf-8') as f:
    f.write('\ufeffПример текста с BOM')
remove_bom(file_path)
with open(file_path, 'r', encoding='utf-8') as f:
    print(f.read())
```

### `main`

```python
def main() -> None:
    """Entry point for BOM removal in Python files."""
```

**Описание**: Главная функция для удаления BOM из файлов Python в директории `../src`.

**Параметры**:
- Отсутствуют

**Возвращает**:
- `None`

**Примеры**:
- Запуск функции `main` для удаления BOM

```python
if __name__ == '__main__':
    main()