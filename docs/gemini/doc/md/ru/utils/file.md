```markdown
# Модуль `hypotez/src/utils/file.py`

## Обзор

Этот модуль предоставляет функции для работы с файлами, включая чтение, запись и поиск файлов в директориях. Он поддерживает разные форматы данных для записи (строка, список строк, словарь) и чтение файлов как в формате строки, так и списка строк. Модуль также включает обработку исключений и логирование ошибок.

## Функции

### `save_text_file`

**Описание**: Сохраняет данные в текстовый файл. Поддерживает запись строк, списков строк и словарей.

**Параметры**:
- `data` (str | list[str] | dict): Данные для записи (строка, список строк или словарь).
- `file_path` (str | Path): Путь к файлу для сохранения.
- `mode` (str, optional): Режим записи (`w` для записи, `a` для добавления). По умолчанию 'w'.
- `exc_info` (bool, optional): Если True, логирует информацию об ошибке (стек-трейс). По умолчанию True.

**Возвращает**:
- `bool`: True, если файл был успешно сохранён, False в противном случае.

**Вызывает исключения**:
- Различные исключения при операциях с файлами.


### `read_text_file`

**Описание**: Читает содержимое файла. Поддерживает чтение файлов и каталогов.

**Параметры**:
- `file_path` (str | Path): Путь к файлу или каталогу.
- `as_list` (bool, optional): Если True, возвращает содержимое как список строк. По умолчанию False.
- `extensions` (list[str], optional): Список расширений файлов для включения при чтении каталога. По умолчанию None.
- `exc_info` (bool, optional): Если True, логирует информацию об ошибке (стек-трейс). По умолчанию True.

**Возвращает**:
- `str | list[str] | None`: Содержимое файла в виде строки или списка строк, или None, если произошла ошибка.

**Вызывает исключения**:
- Различные исключения при операциях с файлами.


### `get_filenames`

**Описание**: Получает имена файлов в каталоге, опционально отфильтрованные по расширению.

**Параметры**:
- `directory` (str | Path): Каталог для поиска.
- `extensions` (str | list[str], optional): Расширения для фильтрации. По умолчанию '*'.

**Возвращает**:
- `list[str]`: Имена файлов, найденные в каталоге.

**Вызывает исключения**:
- `Exception`: При ошибках при чтении каталога.


### `recursively_yield_file_path`

**Описание**: Рекурсивно возвращает пути к файлам, соответствующим заданным шаблонам.

**Параметры**:
- `root_dir` (str | Path): Корневой каталог для поиска.
- `patterns` (str | list[str], optional): Шаблоны для фильтрации файлов. По умолчанию '*'.

**Возвращает**:
- `Generator[Path, None, None]`: Генерирует пути к файлам, соответствующим шаблонам.

**Вызывает исключения**:
- `Exception`: При ошибках при рекурсивном поиске файлов.


### `recursively_get_file_path`

**Описание**: Рекурсивно возвращает пути к файлам, соответствующим заданным шаблонам.

**Параметры**:
- `root_dir` (str | Path): Корневой каталог для поиска.
- `patterns` (str | list[str], optional): Шаблоны для фильтрации файлов. По умолчанию '*'.

**Возвращает**:
- `list[Path]`: Список путей к файлам, соответствующим шаблонам.

**Вызывает исключения**:
- `Exception`: При ошибках при рекурсивном поиске файлов.


### `recursively_read_text_files`

**Описание**: Рекурсивно читает содержимое текстовых файлов, соответствующих заданным шаблонам.

**Параметры**:
- `root_dir` (str | Path): Корневой каталог.
- `patterns` (str | list[str]): Шаблоны для поиска файлов.
- `as_list` (bool, optional): Если True, возвращает содержимое как список строк. По умолчанию False.
- `exc_info` (bool, optional): Если True, логгирует информацию об ошибке (стек-трейс). По умолчанию True.


**Возвращает**:
- `list[str]`: Список содержимого файлов, соответствующих шаблонам.


### `get_directory_names`

**Описание**: Возвращает список имён подкаталогов в заданном каталоге.

**Параметры**:
- `directory` (str | Path): Путь к каталогу.
- `exc_info` (bool, optional): Если True, логгирует информацию об ошибке (стек-трейс) при возникновении.

**Возвращает**:
- `list[str]`: Список имён подкаталогов.


### `read_files_content`

**Описание**: Читает содержимое файлов, соответствующих шаблонам, в указанной директории.


**Параметры**:
- `root_dir` (str | Path): Корневая директория.
- `patterns` (str | list[str]): Шаблоны файлов.
- `as_list` (bool, optional): Возвращает содержимое в виде списка строк.
- `exc_info` (bool, optional): Логировать стек-трейс.


**Возвращает**:
- `list[str]`: Список содержимого файлов.


### `remove_bom`

**Описание**: Удаляет BOM (Byte Order Mark) из текстового файла.

**Параметры**:
- `file_path` (str | Path): Путь к файлу.


**Вызывает исключения**:
- `Exception`: При ошибках при обработке файла.


### `traverse_and_clean`

**Описание**: Обходит каталог и удаляет BOM из файлов `.py`.


**Параметры**:
- `directory` (str | Path): Корневой каталог.


**Вызывает исключения**:
- `Exception`: При ошибках при обработке файлов.


### `main`

**Описание**: Точка входа для удаления BOM из файлов `.py` в указанном каталоге.


**Возвращает**:
- `None`

**Вызывает исключения**:
- `Exception`: При ошибках.

```