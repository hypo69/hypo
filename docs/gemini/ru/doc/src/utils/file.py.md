# Модуль `src.utils.file`

## Обзор

Модуль `src.utils.file` предназначен для выполнения различных операций с файлами, таких как сохранение, чтение, поиск и обработка содержимого файлов. Он предоставляет набор функций для работы с текстовыми файлами и каталогами, а также для удаления BOM.

## Содержание
- [Функции](#Функции)
    - [`save_text_file`](#save_text_file)
    - [`read_text_file`](#read_text_file)
    - [`get_filenames`](#get_filenames)
    - [`recursively_yield_file_path`](#recursively_yield_file_path)
    - [`recursively_get_file_path`](#recursively_get_file_path)
    - [`recursively_read_text_files`](#recursively_read_text_files)
    - [`get_directory_names`](#get_directory_names)
    - [`read_files_content`](#read_files_content)
    - [`remove_bom`](#remove_bom)
    - [`traverse_and_clean`](#traverse_and_clean)
    - [`main`](#main)

## Функции

### `save_text_file`

**Описание**: Сохраняет данные в текстовый файл.

**Параметры**:
- `data` (str | list[str] | dict): Данные для записи (строка, список строк или словарь).
- `file_path` (str | Path): Путь, где будет сохранен файл.
- `mode` (str, optional): Режим записи (`w` для записи, `a` для добавления). По умолчанию `'w'`.
- `exc_info` (bool, optional): Если `True`, логирует трассировку ошибки. По умолчанию `True`.

**Возвращает**:
- `bool`: `True`, если файл был успешно сохранен, `False` в противном случае.

### `read_text_file`

**Описание**: Читает содержимое файла.

**Параметры**:
- `file_path` (str | Path): Путь к файлу или каталогу.
- `as_list` (bool, optional): Если `True`, возвращает содержимое в виде списка строк. По умолчанию `False`.
- `extensions` (list[str], optional): Список расширений файлов для включения при чтении каталога. По умолчанию `None`.
- `exc_info` (bool, optional): Если `True`, логирует трассировку ошибки. По умолчанию `True`.

**Возвращает**:
- `str | list[str] | None`: Содержимое файла в виде строки или списка строк, или `None`, если произошла ошибка.

### `get_filenames`

**Описание**: Получает имена файлов в каталоге, опционально фильтруя их по расширению.

**Параметры**:
- `directory` (str | Path): Каталог для поиска.
- `extensions` (str | list[str], optional): Расширения для фильтрации. По умолчанию `'*'`.
- `exc_info` (bool, optional): Если `True`, логирует трассировку ошибки. По умолчанию `True`.

**Возвращает**:
- `list[str]`: Список имен файлов, найденных в каталоге.

### `recursively_yield_file_path`

**Описание**: Рекурсивно возвращает пути к файлам, соответствующие заданным шаблонам.

**Параметры**:
- `root_dir` (str | Path): Корневой каталог для поиска.
- `patterns` (str | list[str]): Шаблоны для фильтрации файлов.
- `exc_info` (bool, optional): Если `True`, логирует трассировку ошибки. По умолчанию `True`.

**Возвращает**:
- `Generator[Path, None, None]`: Генератор путей к файлам, соответствующим шаблонам.

### `recursively_get_file_path`

**Описание**: Рекурсивно получает пути к файлам, соответствующие заданным шаблонам.

**Параметры**:
- `root_dir` (str | Path): Корневой каталог для поиска.
- `patterns` (str | list[str]): Шаблоны для фильтрации файлов.
- `exc_info` (bool, optional): Если `True`, логирует трассировку ошибки. По умолчанию `True`.

**Возвращает**:
- `list[Path]`: Список путей к файлам, соответствующим шаблонам.

### `recursively_read_text_files`

**Описание**: Рекурсивно читает текстовые файлы из указанного корневого каталога, которые соответствуют заданным шаблонам.

**Параметры**:
- `root_dir` (str | Path): Путь к корневому каталогу для поиска.
- `patterns` (str | list[str]): Шаблон(ы) имени файла для фильтрации файлов. Может быть как одним шаблоном (например, `'*.txt'`), так и списком шаблонов.
- `as_list` (bool, optional): Если `True`, возвращает содержимое файла в виде списка строк. По умолчанию `False`.
- `exc_info` (bool, optional): Если `True`, включает информацию об исключении в предупреждения. По умолчанию `True`.

**Возвращает**:
- `list[str]`: Список содержимого файлов (или строк, если `as_list=True`), которые соответствуют указанным шаблонам.

**Пример**:
```python
contents = recursively_read_text_files("/path/to/root", ["*.txt", "*.md"], as_list=True)
for line in contents:
    print(line)
```
Этот код распечатает каждую строку из всех совпадающих текстовых файлов в указанном каталоге.

### `get_directory_names`

**Описание**: Извлекает все имена каталогов из указанного каталога.

**Параметры**:
- `directory` (str | Path): Путь к каталогу, из которого нужно извлечь имена каталогов.
- `exc_info` (bool, optional): Если `True`, логирует трассировку в случае ошибки. По умолчанию `True`.

**Возвращает**:
- `list[str]`: Список имен каталогов, найденных в указанном каталоге.

**Пример**:
```python
directories: list[str] = get_directory_names(directory=".")
print(directories) # ['dir1', 'dir2']
```

**Дополнительная документация**: [https://github.com/hypo69/tiny-utils/wiki/Files-and-Directories#get_directory_names](https://github.com/hypo69/tiny-utils/wiki/Files-and-Directories#get_directory_names)

### `read_files_content`

**Описание**: Читает содержимое файлов, соответствующих шаблонам.

**Параметры**:
- `root_dir` (str | Path): Корневой каталог для поиска.
- `patterns` (str | list[str]): Шаблоны файлов для сопоставления.
- `as_list` (bool, optional): Возвращает содержимое в виде списка строк. По умолчанию `False`.
- `exc_info` (bool, optional): Если `True`, логирует трассировку ошибки. По умолчанию `True`.

**Возвращает**:
- `list[str]`: Список содержимого файлов.

### `remove_bom`

**Описание**: Удаляет BOM из текстового файла.

**Параметры**:
- `file_path` (str | Path): Файл для обработки.

**Возвращает**:
- `None`

### `traverse_and_clean`

**Описание**: Обходит каталог и удаляет BOM из Python-файлов.

**Параметры**:
- `directory` (str | Path): Корневой каталог для обработки.

**Возвращает**:
- `None`

### `main`

**Описание**: Точка входа для удаления BOM в Python-файлах.

**Возвращает**:
- `None`