# Модуль `src.utils.file`

## Обзор

Модуль `src.utils.file` предоставляет набор утилит для работы с файлами, включая функции для чтения, записи и поиска текстовых файлов. Он также включает в себя поддержку обработки больших файлов с использованием генераторов для экономии памяти.

## Подробней

Этот модуль предназначен для упрощения операций с файлами в проекте `hypotez`. Он содержит функции для сохранения данных в текстовые файлы, чтения содержимого файлов (как целиком, так и построчно с использованием генераторов), получения списков файлов в директориях и рекурсивного поиска файлов по шаблонам. Модуль также включает функциональность для удаления BOM (Byte Order Mark) из файлов, что может быть полезно при работе с текстовыми файлами, созданными в различных операционных системах.

## Содержание

- [save_text_file](#save_text_file)
- [read_text_file_generator](#read_text_file_generator)
- [read_text_file](#read_text_file)
- [yield_text_from_files](#yield_text_from_files)
- [_read_file_content](#_read_file_content)
- [_read_file_lines_generator](#_read_file_lines_generator)
- [get_filenames_from_directory](#get_filenames_from_directory)
- [recursively_yield_file_path](#recursively_yield_file_path)
- [recursively_get_file_path](#recursively_get_file_path)
- [recursively_read_text_files](#recursively_read_text_files)
- [get_directory_names](#get_directory_names)
- [remove_bom](#remove_bom)
- [main](#main)

## Функции

### `save_text_file`

```python
def save_text_file(
    file_path: str | Path,
    data: str | list[str] | dict,
    mode: str = 'w'
) -> bool:
```

**Назначение**: Сохраняет данные в текстовый файл.

**Как работает функция**:

Функция `save_text_file` принимает путь к файлу, данные для записи и режим записи. Сначала она создает родительские директории, если они не существуют. Затем, в зависимости от типа данных (строка, список строк или словарь), она записывает данные в файл. Если данные представлены в виде списка, каждая строка записывается с новой строки. Если данные - словарь, они записываются в формате JSON. Функция возвращает `True`, если файл успешно сохранен, и `False` в противном случае. В случае возникновения ошибки при записи в файл, она логируется с использованием `logger.error`.

**Параметры**:

- `file_path` (str | Path): Путь к файлу для сохранения.
- `data` (str | list[str] | dict): Данные для записи. Могут быть строкой, списком строк или словарем.
- `mode` (str, optional): Режим записи файла ('w' для записи, 'a' для добавления). По умолчанию 'w'.

**Возвращает**:

- `bool`: `True`, если файл успешно сохранен, `False` в противном случае.

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
```

**Назначение**: Читает содержимое файла(ов) или директории с использованием генератора.

**Как работает функция**:

Функция `read_text_file_generator` предназначена для чтения содержимого файла или файлов в директории. Она может возвращать данные как генератор строк (если `as_list` равен `True`), как одну строку (если `as_list` равен `False`) или как список строк (если `file_path` является директорией, `recursive` равен `True` и `as_list` равен `True`). Функция обрабатывает различные сценарии, включая чтение одного файла, чтение файлов из директории (рекурсивно или нет) и фильтрацию файлов по расширениям и шаблонам. В случае ошибки возвращает `None` и логирует ошибку с использованием `logger.error`.

**Параметры**:

- `file_path` (str | Path): Путь к файлу или директории.
- `as_list` (bool, optional): Если `True`, то возвращает генератор строк или список строк, в зависимости от типа вывода. По умолчанию `False`.
- `extensions` (list[str], optional): Список расширений файлов для включения при чтении директории. По умолчанию `None`.
- `chunk_size` (int, optional): Размер чанка для чтения файла в байтах. По умолчанию 8192.
- `recursive` (bool, optional): Если `True`, то поиск файлов выполняется рекурсивно. По умолчанию `False`.
- `patterns` (str | list[str], optional): Шаблоны для фильтрации файлов при рекурсивном поиске. По умолчанию `None`.

**Возвращает**:

- `Generator[str, None, None] | str | list[str] | None`: Генератор строк, строка или список строк в зависимости от параметров, или `None` в случае ошибки.

**Вызывает исключения**:

- `Exception`: Возникает при ошибке при чтении файла.

**Примеры**:

```python
from pathlib import Path
file_path = Path('example.txt')
content = read_text_file_generator(file_path)
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
```

**Назначение**: Читает содержимое файла.

**Как работает функция**:

Функция `read_text_file` считывает содержимое файла по указанному пути. Она может возвращать содержимое как строку или как список строк, в зависимости от значения параметра `as_list`. Если указан путь к директории, функция рекурсивно считывает все файлы в этой директории и возвращает их содержимое. В случае ошибки возвращает `None` и логирует ошибку с использованием `logger.error`.

**Параметры**:

- `file_path` (str | Path): Путь к файлу или директории.
- `as_list` (bool, optional): Если `True`, возвращает содержимое как список строк. По умолчанию `False`.
- `extensions` (list[str], optional): Список расширений файлов для включения при чтении директории. По умолчанию `None`.
- `exc_info` (bool, optional): Если `True`, логирует traceback при ошибке. По умолчанию `True`.

**Возвращает**:

- `str | list[str] | None`: Содержимое файла как строка или список строк, или `None`, если произошла ошибка.

**Вызывает исключения**:

- `Exception`: Возникает при ошибке при чтении файла.

**Примеры**:

```python
from pathlib import Path
file_path = Path('example.txt')
content = read_text_file(file_path)
if content:
    print(f'File content: {content[:100]}...')
```

### `yield_text_from_files`

```python
def yield_text_from_files(
    file_path: str | Path,
    as_list: bool = False,
    chunk_size: int = 8192
) -> Generator[str, None, None] | str | None:
```

**Назначение**: Читает содержимое файла и возвращает его в виде генератора строк или одной строки.

**Как работает функция**:

Функция `yield_text_from_files` читает файл по указанному пути и возвращает его содержимое либо в виде генератора строк (если `as_list` равен `True`), либо в виде одной строки (если `as_list` равен `False`). Функция использует другие функции (`_read_file_lines_generator` и `_read_file_content`) для фактического чтения содержимого файла. В случае ошибки возвращает `None` и логирует ошибку с использованием `logger.error`.

**Параметры**:

- `file_path` (str | Path): Путь к файлу.
- `as_list` (bool, optional): Если `True`, возвращает генератор строк. По умолчанию `False`.
- `chunk_size` (int, optional): Размер чанка для чтения файла в байтах. По умолчанию 8192.

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
```

**Назначение**: Читает содержимое файла по чанкам и возвращает как строку.

**Как работает функция**:

Функция `_read_file_content` читает файл по частям (чанкам) заданного размера и объединяет их в одну строку. Она открывает файл, читает его содержимое по частям, добавляет каждую часть к результирующей строке и возвращает полную строку после завершения чтения.

**Параметры**:

- `file_path` (Path): Путь к файлу для чтения.
- `chunk_size` (int): Размер чанка для чтения файла в байтах.

**Возвращает**:

- `str`: Содержимое файла в виде строки.

**Вызывает исключения**:

- `Exception`: Возникает при ошибке при чтении файла.

### `_read_file_lines_generator`

```python
def _read_file_lines_generator(file_path: Path, chunk_size: int) -> Generator[str, None, None]:
```

**Назначение**: Читает файл по строкам с помощью генератора.

**Как работает функция**:

Функция `_read_file_lines_generator` читает файл по частям (чанкам) заданного размера и разделяет каждую часть на строки. Она использует генератор для построчного возврата содержимого файла, что позволяет экономить память при работе с большими файлами. Если чанк не заканчивается полной строкой, функция добавляет последнюю строку к следующему чанку.

**Параметры**:

- `file_path` (Path): Путь к файлу для чтения.
- `chunk_size` (int): Размер чанка для чтения файла в байтах.

**Yields**:

- `str`: Строки из файла.

**Вызывает исключения**:

- `Exception`: Возникает при ошибке при чтении файла.

### `get_filenames_from_directory`

```python
def get_filenames_from_directory(
    directory: str | Path, ext: str | list[str] = '*'
) -> list[str]:
```

**Назначение**: Возвращает список имен файлов в директории, опционально отфильтрованных по расширению.

**Как работает функция**:

Функция `get_filenames_from_directory` принимает путь к директории и опциональный список расширений файлов. Она возвращает список имен файлов в указанной директории, которые соответствуют заданным расширениям. Если расширения не указаны, функция возвращает имена всех файлов в директории. Функция проверяет, является ли указанный путь директорией, и логирует ошибку, если это не так.

**Параметры**:

- `directory` (str | Path): Путь к директории для поиска.
- `ext` (str | list[str], optional): Расширения для фильтрации. По умолчанию '*'.

**Возвращает**:

- `list[str]`: Список имен файлов, найденных в директории.

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
```

**Назначение**: Рекурсивно возвращает пути ко всем файлам, соответствующим заданным шаблонам, в указанной директории.

**Как работает функция**:

Функция `recursively_yield_file_path` рекурсивно обходит указанную директорию и возвращает пути ко всем файлам, которые соответствуют заданным шаблонам. Она использует генератор для построчного возврата путей к файлам.

**Параметры**:

- `root_dir` (str | Path): Корневая директория для поиска.
- `patterns` (str | list[str]): Шаблоны для фильтрации файлов.

**Yields**:

- `Path`: Путь к файлу, соответствующему шаблону.

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
```

**Назначение**: Рекурсивно возвращает список путей ко всем файлам, соответствующим заданным шаблонам, в указанной директории.

**Как работает функция**:

Функция `recursively_get_file_path` рекурсивно обходит указанную директорию и возвращает список путей ко всем файлам, которые соответствуют заданным шаблонам.

**Параметры**:

- `root_dir` (str | Path): Корневая директория для поиска.
- `patterns` (str | list[str]): Шаблоны для фильтрации файлов.

**Возвращает**:

- `list[Path]`: Список путей к файлам, соответствующим шаблонам.

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
```

**Назначение**: Рекурсивно читает текстовые файлы из указанной корневой директории, соответствующие заданным шаблонам.

**Как работает функция**:

Функция `recursively_read_text_files` рекурсивно обходит указанную директорию и читает содержимое всех файлов, которые соответствуют заданным шаблонам. Она может возвращать содержимое файлов как список строк (если `as_list` равен `True`) или как список полных текстов файлов (если `as_list` равен `False`). В случае ошибки при чтении файла, она логируется с использованием `logger.error`.

**Параметры**:

- `root_dir` (str | Path): Путь к корневой директории для поиска.
- `patterns` (str | list[str]): Шаблон(ы) имени файла для фильтрации.
- `as_list` (bool, optional): Если `True`, то возвращает содержимое файла как список строк. По умолчанию `False`.

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
```

**Назначение**: Возвращает список имен директорий из указанной директории.

**Как работает функция**:

Функция `get_directory_names` принимает путь к директории и возвращает список имен всех поддиректорий в этой директории. В случае ошибки возвращает пустой список и логирует ошибку с использованием `logger.error`.

**Параметры**:

- `directory` (str | Path): Путь к директории, из которой нужно получить имена.

**Возвращает**:

- `list[str]`: Список имен директорий, найденных в указанной директории.

**Примеры**:

```python
from pathlib import Path
directory = Path('.')
get_directory_names(directory)
```

### `remove_bom`

```python
def remove_bom(path: str | Path) -> None:
```

**Назначение**: Удаляет BOM из текстового файла или из всех файлов Python в директории.

**Как работает функция**:

Функция `remove_bom` удаляет BOM (Byte Order Mark) из указанного файла или из всех файлов Python в указанной директории. Если указан путь к файлу, функция открывает файл, удаляет BOM и перезаписывает содержимое файла. Если указан путь к директории, функция рекурсивно обходит все файлы Python в этой директории и удаляет BOM из каждого файла. В случае ошибки логирует её с использованием `logger.error`.

**Параметры**:

- `path` (str | Path): Путь к файлу или директории.

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
```

**Назначение**: Entry point для удаления BOM в Python файлах.

**Как работает функция**:

Функция `main` является точкой входа для удаления BOM из всех Python файлов в директории `../src`. Она вызывает функцию `remove_bom` с указанием этой директории. Информация о начале процесса логируется с использованием `logger.info`.

### `__name__ == '__main__'`

```python
if __name__ == '__main__':
    main()
```

**Назначение**: Entry point для запуска скрипта.

**Как работает**:
Этот блок кода проверяет, запущен ли скрипт как основная программа. Если это так, он вызывает функцию `main()`, которая запускает процесс удаления BOM из Python файлов в указанной директории.