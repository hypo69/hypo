# Модуль `src.utils.file_async`

## Обзор

Модуль `src.utils.file_async` предоставляет набор асинхронных утилит для работы с файлами, включая чтение, запись, поиск файлов и удаление BOM. Модуль поддерживает обработку больших файлов с использованием асинхронных генераторов для экономии памяти.

## Оглавление

- [Функции](#функции)
  - [`save_text_file`](#save_text_file)
  - [`read_text_file`](#read_text_file)
  - [`yield_text_from_files`](#yield_text_from_files)
  - [`_read_file_content`](#_read_file_content)
  - [`_read_file_lines_generator`](#_read_file_lines_generator)
  - [`get_filenames_from_directory`](#get_filenames_from_directory)
  - [`recursively_yield_file_path`](#recursively_yield_file_path)
  - [`recursively_get_file_path`](#recursively_get_file_path)
  - [`recursively_read_text_files`](#recursively_read_text_files)
  - [`get_directory_names`](#get_directory_names)
  - [`remove_bom`](#remove_bom)
- [Вспомогательные функции](#вспомогательные-функции)
  - [`main`](#main)

## Функции

### `save_text_file`

**Описание**: Асинхронно сохраняет данные в текстовый файл.

**Параметры**:
- `file_path` (str | Path): Путь к файлу для сохранения.
- `data` (str | list[str] | dict): Данные для записи.
- `mode` (str, optional): Режим записи файла ('w' для записи, 'a' для добавления). По умолчанию `'w'`.

**Возвращает**:
- `bool`: `True`, если файл успешно сохранен, `False` в противном случае.

**Вызывает исключения**:
- `Exception`: При возникновении ошибки при записи в файл.

**Пример**:
```python
from pathlib import Path
file_path = Path('example.txt')
data = 'Пример текста'
result = await save_text_file(file_path, data)
print(result)
```

### `read_text_file`

**Описание**: Асинхронно читает содержимое файла(ов) или директории.

**Параметры**:
- `file_path` (str | Path): Путь к файлу или директории.
- `as_list` (bool, optional): Если `True`, то возвращает генератор строк или список строк, в зависимости от типа вывода. По умолчанию `False`.
- `extensions` (list[str], optional): Список расширений файлов для включения при чтении директории. По умолчанию `None`.
- `chunk_size` (int, optional): Размер чанка для чтения файла в байтах. По умолчанию `8192`.
- `recursive` (bool, optional): Если `True`, то поиск файлов выполняется рекурсивно. По умолчанию `False`.
- `patterns` (str | list[str], optional): Шаблоны для фильтрации файлов при рекурсивном поиске. По умолчанию `None`.

**Возвращает**:
- `AsyncGenerator[str, None] | str | list[str] | None`:
  - Если `as_list` is `True` и `file_path` является файлом, возвращает асинхронный генератор строк.
  - Если `as_list` is `True` и `file_path` является директорией и `recursive` is `True`, возвращает асинхронный генератор строк.
  - Если `as_list` is `False` и `file_path` является файлом, возвращает строку.
  - Если `as_list` is `False` и `file_path` является директорией, возвращает объединенную строку.
  - Возвращает `None` в случае ошибки.

**Вызывает исключения**:
- `Exception`: При возникновении ошибки при чтении файла.

**Пример**:
```python
from pathlib import Path
file_path = Path('example.txt')
content = await read_text_file(file_path)
if content:
    print(f'File content: {content[:100]}...')
```

**Примечания**:
- Если вы хотите прочитать содержимое файла построчно (особенно для больших файлов) используйте `as_list = True`. В этом случае вы получите генератор строк.
- Если вы хотите получить всё содержимое файла в виде одной строки используйте `as_list = False`.
- Если вы работаете с директорией, `recursive = True` будет обходить все поддиректории.
- `extensions` и `patterns` позволят вам фильтровать файлы при работе с директорией.
- `chunk_size` позволяет оптимизировать работу с большими файлами при чтении их по частям.
- `None` будет возвращён в случае ошибок.

### `yield_text_from_files`

**Описание**: Асинхронно читает содержимое файла и возвращает его в виде генератора строк или одной строки.

**Параметры**:
- `file_path` (str | Path): Путь к файлу.
- `as_list` (bool, optional): Если `True`, возвращает генератор строк. По умолчанию `False`.
- `chunk_size` (int, optional): Размер чанка для чтения файла в байтах. По умолчанию `8192`.

**Возвращает**:
- `AsyncGenerator[str, None] | str | None`: Генератор строк, объединенная строка или `None` в случае ошибки.

**Вызывает исключения**:
 - `Exception`: При возникновении ошибки при чтении файла.

**Пример**:
```python
from pathlib import Path
file_path = Path('example.txt')
async for line in yield_text_from_files(file_path, as_list=True):
    print(line)
```

### `_read_file_content`

**Описание**: Асинхронно читает содержимое файла по чанкам и возвращает как строку.

**Параметры**:
- `file_path` (Path): Путь к файлу для чтения.
- `chunk_size` (int): Размер чанка для чтения файла в байтах.

**Возвращает**:
- `str`: Содержимое файла в виде строки.

**Вызывает исключения**:
- `Exception`: При возникновении ошибки при чтении файла.

### `_read_file_lines_generator`

**Описание**: Асинхронно читает файл по строкам с помощью генератора.

**Параметры**:
- `file_path` (Path): Путь к файлу для чтения.
- `chunk_size` (int): Размер чанка для чтения файла в байтах.

**Возвращает**:
- `AsyncGenerator[str, None]`: Генератор строк из файла.

**Вызывает исключения**:
- `Exception`: При возникновении ошибки при чтении файла.

### `get_filenames_from_directory`

**Описание**: Асинхронно возвращает список имен файлов в директории, опционально отфильтрованных по расширению.

**Параметры**:
- `directory` (str | Path): Путь к директории для поиска.
- `extensions` (str | list[str], optional): Расширения для фильтрации. По умолчанию `'*'`.

**Возвращает**:
- `list[str]`: Список имен файлов, найденных в директории.

**Вызывает исключения**:
 - `Exception`: При возникновении ошибки при получении списка имен файлов.

**Пример**:
```python
from pathlib import Path
directory = Path('.')
await get_filenames_from_directory(directory, ['.txt', '.md'])
```

### `recursively_yield_file_path`

**Описание**: Асинхронно рекурсивно возвращает пути ко всем файлам, соответствующим заданным шаблонам, в указанной директории.

**Параметры**:
- `root_dir` (str | Path): Корневая директория для поиска.
- `patterns` (str | list[str]): Шаблоны для фильтрации файлов.

**Возвращает**:
- `AsyncGenerator[Path, None]`: Генератор путей к файлам, соответствующим шаблону.

**Вызывает исключения**:
 - `Exception`: При возникновении ошибки при рекурсивном поиске файлов.

**Пример**:
```python
from pathlib import Path
root_dir = Path('.')
async for path in recursively_yield_file_path(root_dir, ['*.txt', '*.md']):
    print(path)
```

### `recursively_get_file_path`

**Описание**: Асинхронно рекурсивно возвращает список путей ко всем файлам, соответствующим заданным шаблонам, в указанной директории.

**Параметры**:
- `root_dir` (str | Path): Корневая директория для поиска.
- `patterns` (str | list[str]): Шаблоны для фильтрации файлов.

**Возвращает**:
- `list[Path]`: Список путей к файлам, соответствующим шаблонам.

**Вызывает исключения**:
 - `Exception`: При возникновении ошибки при рекурсивном поиске файлов.

**Пример**:
```python
from pathlib import Path
root_dir = Path('.')
paths = await recursively_get_file_path(root_dir, ['*.txt', '*.md'])
print(paths)
```

### `recursively_read_text_files`

**Описание**: Асинхронно рекурсивно читает текстовые файлы из указанной корневой директории, соответствующие заданным шаблонам.

**Параметры**:
- `root_dir` (str | Path): Путь к корневой директории для поиска.
- `patterns` (str | list[str]): Шаблон(ы) имени файла для фильтрации.
- `as_list` (bool, optional): Если `True`, то возвращает содержимое файла как список строк. По умолчанию `False`.

**Возвращает**:
- `list[str]`: Список содержимого файлов (или список строк, если `as_list=True`), соответствующих заданным шаблонам.

**Вызывает исключения**:
 - `Exception`: При возникновении ошибки при чтении файла.

**Пример**:
```python
from pathlib import Path
root_dir = Path('.')
contents = await recursively_read_text_files(root_dir, ['*.txt', '*.md'], as_list=True)
for line in contents:
    print(line)
```

### `get_directory_names`

**Описание**: Асинхронно возвращает список имен директорий из указанной директории.

**Параметры**:
- `directory` (str | Path): Путь к директории, из которой нужно получить имена.

**Возвращает**:
- `list[str]`: Список имен директорий, найденных в указанной директории.

**Вызывает исключения**:
 - `Exception`: При возникновении ошибки при получении списка имен директорий.

**Пример**:
```python
from pathlib import Path
directory = Path('.')
await get_directory_names(directory)
```

### `remove_bom`

**Описание**: Асинхронно удаляет BOM из текстового файла или из всех файлов Python в директории.

**Параметры**:
- `path` (str | Path): Путь к файлу или директории.

**Вызывает исключения**:
 - `Exception`: При возникновении ошибки при удалении BOM из файла.

**Пример**:
```python
from pathlib import Path
file_path = Path('example.txt')
with open(file_path, 'w', encoding='utf-8') as f:
    f.write('\ufeffПример текста с BOM')
await remove_bom(file_path)
with open(file_path, 'r', encoding='utf-8') as f:
    print(f.read())
```

## Вспомогательные функции

### `main`

**Описание**: Точка входа для удаления BOM из файлов Python.