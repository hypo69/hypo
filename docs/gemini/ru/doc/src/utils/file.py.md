# Модуль `src.utils.file`

## Обзор

Модуль предоставляет набор утилит для работы с файлами, включая сохранение, чтение и поиск файлов, а также другие операции, такие как удаление BOM. Поддерживает чтение и запись больших файлов с использованием генераторов для экономии памяти.

## Подробней

Этот модуль содержит функции для выполнения различных операций с файлами и директориями, такие как чтение, запись, рекурсивный поиск и удаление BOM (Byte Order Mark). Он используется в проекте для обеспечения надежной работы с файловой системой, обработки текстовых данных и фильтрации файлов по различным критериям.

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

**Назначение**: Сохраняет строковые данные, список строк или словарь в текстовый файл.

**Параметры**:
- `file_path` (str | Path): Путь к файлу, в который нужно сохранить данные.
- `data` (str | list[str] | dict): Данные для записи в файл. Поддерживаются строки, списки строк и словари.
- `mode` (str, optional): Режим открытия файла. `'w'` для перезаписи (по умолчанию), `'a'` для добавления в конец файла.

**Возвращает**:
- `bool`: `True`, если запись в файл прошла успешно, и `False` в случае ошибки.

**Вызывает исключения**:
- `Exception`: Возникает при ошибках записи в файл, например, при отсутствии доступа к файлу или директории.

**Как работает функция**:
1. Преобразует `file_path` в объект `Path` для удобства работы.
2. Создает родительские директории, если они не существуют.
3. Открывает файл в указанном режиме и кодировке (`utf-8`).
4. Записывает данные в файл в зависимости от их типа:
   - Если `data` - список, записывает каждый элемент списка как отдельную строку.
   - Если `data` - словарь, записывает его в формате JSON с отступами.
   - Если `data` - строка, записывает ее в файл.
5. Возвращает `True` при успешной записи и `False` в случае ошибки.
6. Логирует информацию об ошибке при возникновении исключения.

**ASCII flowchart**:

```
    File Path -> Path Object
    |
    Create Parent Directories
    |
    Open File (w/a mode)
    |
    Check Data Type
    |
    String -> Write String
    List -> Write Lines
    Dict -> Write JSON
    |
    Return True/False
```

**Примеры**:

```python
from pathlib import Path
# Пример записи строки в файл
file_path = Path('example.txt')
data = 'Пример текста'
result = save_text_file(file_path, data)
print(result)  # Вывод: True

# Пример записи списка строк в файл
file_path = Path('example.txt')
data = ['Строка 1', 'Строка 2', 'Строка 3']
result = save_text_file(file_path, data)
print(result)  # Вывод: True

# Пример записи словаря в файл
file_path = Path('example.json')
data = {'ключ1': 'значение1', 'ключ2': 'значение2'}
result = save_text_file(file_path, data)
print(result)  # Вывод: True
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
            >>> content = read_text_file(file_path)
            >>> if content:
            ...    print(f'File content: {content[:100]}...')
            File content: Пример текста...
    Функция read_text_file может возвращать несколько разных типов данных в зависимости от входных параметров:

    Возвращаемые значения:
    ----------------------

    - Generator[str, None, None] (Генератор строк):
        Генератор при итерации выдаёт строки из файла(ов) по одной. Эффективно для работы с большими файлами, так как они не загружаются полностью в память.
        - Когда:
            file_path – это файл и as_list равен True.
            file_path – это директория, recursive равен True и as_list равен True. При этом в генератор попадают строки из всех найденных файлов.
            file_path – это директория, recursive равен False и as_list равен True. При этом в генератор попадают строки из всех найденных файлов в текущей директории.
        
    - str (Строка):
        Содержимое файла или объединенное содержимое всех файлов в виде одной строки.
        - Когда:
            file_path – это файл и as_list равен False.
            file_path – это директория, recursive равен False и as_list равен False. При этом возвращается объединенная строка, состоящая из содержимого всех файлов в директории, разделенных символами новой строки (\\n).
            file_path – это директория, recursive равен True и as_list равен False. При этом возвращается объединенная строка, состоящая из содержимого всех файлов в директории и её поддиректориях, разделенных символами новой строки (\\n).\n \n    - list[str] (Список строк):\n        Этот тип явно не возвращается функцией, однако когда file_path – это директория, recursive равен True и as_list равен True - функция возвращает генератор, который можно преобразовать в список при помощи list()\n        - Когда:\n            file_path – не является ни файлом, ни директорией.\n            Произошла ошибка при чтении файла или директории (например, файл не найден, ошибка доступа и т.п.).\n\n\n    Note:\n        Если вы хотите прочитать содержимое файла построчно (особенно для больших файлов) используйте as_list = True. В этом случае вы получите генератор строк.\n        Если вы хотите получить всё содержимое файла в виде одной строки используйте as_list = False.\n        Если вы работаете с директорией, recursive = True будет обходить все поддиректории.\n        extensions и patterns позволят вам фильтровать файлы при работе с директорией.\n        chunk_size позволяет оптимизировать работу с большими файлами при чтении их по частям.\n        None будет возвращён в случае ошибок.\n\n    Важно помнить:\n        В случае чтения директории, если as_list=False, функция объединяет все содержимое найденных файлов в одну строку. Это может потребовать много памяти, если файлов много или они большие.\n        Функция полагается на другие функции-помощники (_read_file_lines_generator, _read_file_content, recursively_get_file_path, yield_text_from_files), которые здесь не определены и их поведение влияет на результат read_text_file.\n\n\n    """
```

**Назначение**: Читает содержимое файла(ов) или директории с возможностью фильтрации, рекурсивного поиска и возврата данных в различных форматах.

**Параметры**:

- `file_path` (str | Path): Путь к файлу или директории для чтения.
- `as_list` (bool, optional): Если `True`, возвращает содержимое в виде генератора строк. По умолчанию `False`.
- `extensions` (list[str], optional): Список расширений файлов для включения при чтении директории. По умолчанию `None`.
- `chunk_size` (int, optional): Размер чанка для чтения файла в байтах. Используется для чтения больших файлов. По умолчанию `8192`.
- `recursive` (bool, optional): Если `True`, выполняет рекурсивный поиск файлов в директории. По умолчанию `False`.
- `patterns` (str | list[str], optional): Шаблоны для фильтрации файлов при рекурсивном поиске. По умолчанию `None`.

**Возвращает**:

- `Generator[str, None, None] | str | list[str] | None`:
  - Если `as_list` равен `True` и `file_path` является файлом, возвращает генератор строк.
  - Если `as_list` равен `True` и `file_path` является директорией, возвращает генератор строк из всех файлов в директории (и поддиректориях, если `recursive` равен `True`).
  - Если `as_list` равен `False` и `file_path` является файлом, возвращает строку, содержащую содержимое файла.
  - Если `as_list` равен `False` и `file_path` является директорией, возвращает объединенную строку, содержащую содержимое всех файлов в директории (и поддиректориях, если `recursive` равен `True`), разделенных символами новой строки (`\n`).
  - Возвращает `None` в случае ошибки или если `file_path` не является ни файлом, ни директорией.

**Вызывает исключения**:

- `Exception`: Возникает при ошибке при чтении файла или директории.

**Как работает функция**:

1. Преобразует `file_path` в объект `Path`.
2. Проверяет, является ли `file_path` файлом или директорией.
3. Если `file_path` - файл:
   - Если `as_list` равен `True`, вызывает внутреннюю функцию `_read_file_lines_generator` для чтения файла построчно с использованием генератора.
   - Если `as_list` равен `False`, вызывает внутреннюю функцию `_read_file_content` для чтения всего файла в одну строку.
4. Если `file_path` - директория:
   - Если `recursive` равен `True`, выполняет рекурсивный поиск файлов с использованием функции `recursively_get_file_path` (если указаны `patterns`) или `rglob` (если `patterns` не указаны).
     - Если `as_list` равен `True`, возвращает генератор строк, полученный из всех найденных файлов.
     - Если `as_list` равен `False`, объединяет содержимое всех найденных файлов в одну строку, разделенную символами новой строки.
   - Если `recursive` равен `False`, выполняет поиск файлов только в текущей директории.
     - Если `as_list` равен `True`, возвращает генератор строк, полученный из всех найденных файлов.
     - Если `as_list` равен `False`, объединяет содержимое всех найденных файлов в одну строку, разделенную символами новой строки.
5. Если `file_path` не является ни файлом, ни директорией, логирует ошибку и возвращает `None`.
6. Обрабатывает исключения и логирует ошибки при чтении файла или директории.

**ASCII flowchart**:

```
    File Path -> Path Object
    |
    Is File?
    |
    Yes -> as_list? -> True: _read_file_lines_generator
    |       |          -> False: _read_file_content
    |
    No  -> Is Directory?
    |
    Yes -> Recursive? -> Yes: recursively_get_file_path
    |       |            |
    |       |            -> as_list? -> True: yield from files
    |       |            |            -> False: join contents
    |       |
    |       |          -> No: iterate directory
    |       |            |
    |       |            -> as_list? -> True: yield from files
    |       |            -> False: join contents
    |
    No  -> Log Error, Return None
```

**Примеры**:

```python
from pathlib import Path

# Пример чтения файла построчно с использованием генератора
file_path = Path('example.txt')
for line in read_text_file_generator(file_path, as_list = True):
    print(line)

# Пример чтения файла целиком в виде строки
file_path = Path('example.txt')
content = read_text_file_generator(file_path, as_list = False)
print(content)

# Пример чтения всех файлов в директории рекурсивно и объединения в одну строку
dir_path = Path('.')
content = read_text_file_generator(dir_path, recursive = True, as_list = False, patterns = ['*.txt', '*.md'])
print(content)
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

**Назначение**: Читает содержимое файла или файлов в директории.

**Параметры**:
- `file_path` (str | Path): Путь к файлу или директории.
- `as_list` (bool, optional): Если `True`, возвращает содержимое в виде списка строк. По умолчанию `False`.
- `extensions` (list[str], optional): Список расширений файлов для включения при чтении директории. По умолчанию `None`.
- `exc_info` (bool, optional): Если `True`, логирует traceback при ошибке. По умолчанию `True`.

**Возвращает**:
- `str | list[str] | None`: Содержимое файла в виде строки или списка строк. Возвращает `None` в случае ошибки.

**Как работает функция**:

1. Преобразует `file_path` в объект `Path`.
2. Проверяет, является ли `file_path` файлом или директорией.
3. Если `file_path` - файл:
   - Открывает файл и читает его содержимое.
   - Если `as_list` равен `True`, возвращает список строк.
   - Если `as_list` равен `False`, возвращает строку.
4. Если `file_path` - директория:
   - Рекурсивно получает список всех файлов в директории и её поддиректориях.
   - Для каждого файла вызывает `read_text_file` и собирает результаты.
   - Если `as_list` равен `True`, возвращает список строк.
   - Если `as_list` равен `False`, возвращает строку.
5. Если `file_path` не является ни файлом, ни директорией, логирует предупреждение и возвращает `None`.
6. Обрабатывает исключения и логирует ошибки при чтении файла или директории.

**ASCII flowchart**:
```
    File Path -> Path Object
    |
    Is File?
    |
    Yes -> as_list? -> True: readlines()
    |       |          -> False: read()
    |
    No  -> Is Directory?
    |
    Yes -> Recursively get files
    |    -> Read each file
    |    -> as_list? -> True: return list of lines
    |               -> False: return joined string
    |
    No  -> Log Warning, Return None
```

**Примеры**:

```python
from pathlib import Path

# Пример чтения файла построчно
file_path = Path('example.txt')
content = read_text_file(file_path, as_list = True)
print(content)

# Пример чтения файла целиком
file_path = Path('example.txt')
content = read_text_file(file_path, as_list = False)
print(content)

# Пример чтения всех файлов в директории рекурсивно
dir_path = Path('.')
content = read_text_file(dir_path, as_list = False, extensions=['.txt', '.md'])
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
        >>> for line in yield_text_from_files(file_path, as_list=True):\n        ...     print(line)
        Первая строка файла
        Вторая строка файла
    """
```

**Назначение**: Читает содержимое файла и возвращает его в виде генератора строк или одной строки.

**Параметры**:
- `file_path` (str | Path): Путь к файлу.
- `as_list` (bool, optional): Если `True`, возвращает генератор строк. По умолчанию `False`.
- `chunk_size` (int, optional): Размер чанка для чтения файла в байтах. По умолчанию `8192`.

**Возвращает**:
- `Generator[str, None, None] | str | None`: Генератор строк, объединенная строка или `None` в случае ошибки.

**Yields**:
- `str`: Строки из файла, если `as_list` is `True`.

**Как работает функция**:

1. Преобразует `file_path` в объект `Path`.
2. Проверяет, является ли `file_path` файлом.
3. Если `file_path` - файл:
   - Если `as_list` равен `True`, вызывает внутреннюю функцию `_read_file_lines_generator` для чтения файла построчно с использованием генератора и возвращает результат через `yield from`.
   - Если `as_list` равен `False`, вызывает внутреннюю функцию `_read_file_content` для чтения всего файла в одну строку и возвращает результат через `yield`.
4. Если `file_path` не является файлом, логирует ошибку и возвращает `None`.
5. Обрабатывает исключения и логирует ошибки при чтении файла.

**ASCII flowchart**:
```
    File Path -> Path Object
    |
    Is File?
    |
    Yes -> as_list? -> True: yield from _read_file_lines_generator
    |       |          -> False: yield _read_file_content
    |
    No  -> Log Error, Return None
```

**Примеры**:
```python
from pathlib import Path

# Пример чтения файла построчно с использованием генератора
file_path = Path('example.txt')
for line in yield_text_from_files(file_path, as_list = True):
    print(line)

# Пример чтения файла целиком в виде строки
file_path = Path('example.txt')
for content in yield_text_from_files(file_path, as_list = False):
    print(content)
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

**Назначение**: Читает содержимое файла по частям (чанкам) и возвращает его в виде одной строки.

**Параметры**:
- `file_path` (Path): Путь к файлу, который нужно прочитать.
- `chunk_size` (int): Размер каждого чанка (в байтах), который считывается из файла за одну операцию.

**Возвращает**:
- `str`: Полное содержимое файла в виде одной строки.

**Вызывает исключения**:
- `Exception`: Возникает при ошибках чтения из файла.

**Как работает функция**:

1. Открывает файл для чтения в текстовом режиме с кодировкой UTF-8.
2. Инициализирует пустую строку `content`, в которую будет накапливаться содержимое файла.
3. В цикле читает файл по частям размером `chunk_size`.
4. Добавляет каждый прочитанный чанк в строку `content`.
5. Завершает цикл, когда достигнут конец файла (когда `f.read(chunk_size)` возвращает пустую строку).
6. Возвращает строку `content`, содержащую полное содержимое файла.

**ASCII flowchart**:

```
    File Path -> Open File (UTF-8)
    |
    Init: content = ""
    |
    Loop: Read Chunk (chunk_size)
    |
    No Chunk? -> Break
    |
    Append Chunk to content
    |
    End Loop
    |
    Return content
```

**Примеры**:

```python
from pathlib import Path

# Пример использования функции для чтения содержимого файла
file_path = Path('example.txt')
chunk_size = 1024
content = _read_file_content(file_path, chunk_size)
print(content)
```

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

**Назначение**: Читает файл построчно, используя генератор для экономии памяти.

**Параметры**:
- `file_path` (Path): Путь к файлу, который нужно прочитать.
- `chunk_size` (int): Размер чанка (в байтах), который считывается из файла за одну операцию.

**Yields**:
- `str`: Каждая строка из файла.

**Вызывает исключения**:
- `Exception`: Возникает при ошибках чтения из файла.

**Как работает функция**:
1. Открывает файл для чтения в текстовом режиме с кодировкой UTF-8.
2. В цикле читает файл по частям размером `chunk_size`.
3. Разделяет каждый прочитанный чанк на строки с помощью `splitlines()`.
4. Если чанк не заканчивается полной строкой (т.е. не заканчивается символом новой строки `\n`), то последняя строка добавляется к следующему чанку.
5. Использует `yield from` для выдачи каждой строки из списка строк.
6. Завершает чтение при достижении конца файла.

**ASCII flowchart**:

```
    File Path -> Open File (UTF-8)
    |
    Loop: Read Chunk (chunk_size)
    |
    No Chunk? -> Break
    |
    Split Chunk into Lines
    |
    Chunk Ends with Newline?
    |
    No -> Append Next Chunk to Last Line
    |
    Yield from Lines
    |
    End Loop
```

**Примеры**:

```python
from pathlib import Path

# Пример использования функции для чтения файла построчно
file_path = Path('example.txt')
chunk_size = 1024

for line in _read_file_lines_generator(file_path, chunk_size):
    print(line)
```

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

**Назначение**: Получает список имен файлов в указанной директории, с возможностью фильтрации по расширению.

**Параметры**:
- `directory` (str | Path): Путь к директории, в которой нужно искать файлы.
- `ext` (str | list[str], optional): Расширение или список расширений для фильтрации файлов. Если указано `'*'`, то возвращаются все файлы. По умолчанию `'*'`.

**Возвращает**:
- `list[str]`: Список имен файлов, найденных в директории и соответствующих заданным расширениям.

**Как работает функция**:
1. Проверяет, является ли указанный путь директорией. Если нет, логирует ошибку и возвращает пустой список.
2. Преобразует параметр `ext` в список расширений, если он представлен строкой. Если `ext` равен `'*'`, список расширений остается пустым, что означает отсутствие фильтрации по расширению.
3. Если расширения указаны, к каждому расширению добавляется точка, если она отсутствует.
4. Итерируется по содержимому директории и выбирает только файлы, расширения которых соответствуют заданным (если список расширений не пуст).
5. Возвращает список имен найденных файлов.
6. Если возникает ошибка, логирует ее и возвращает пустой список.

**ASCII flowchart**:
```
    Directory Path -> Is Directory?
    |
    No -> Log Error, Return []
    |
    Yes -> Ext to List[Ext]
    |
    Iterate Directory
    |
    File? and Ext matches?
    |
    Yes -> Add Filename to List
    |
    Return List of Filenames
```

**Примеры**:
```python
from pathlib import Path

# Пример получения списка всех файлов в текущей директории
directory = Path('.')
filenames = get_filenames_from_directory(directory)
print(filenames)

# Пример получения списка файлов с расширениями .txt и .md
directory = Path('.')
filenames = get_filenames_from_directory(directory, ['.txt', '.md'])
print(filenames)
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

**Назначение**: Рекурсивно обходит указанную директорию и возвращает пути ко всем файлам, соответствующим заданным шаблонам, в виде генератора.

**Параметры**:
- `root_dir` (str | Path): Корневая директория для поиска файлов.
- `patterns` (str | list[str], optional): Шаблон или список шаблонов для фильтрации файлов. По умолчанию `'*'`, что соответствует всем файлам.

**Yields**:
- `Path`: Путь к файлу, который соответствует заданному шаблону.

**Как работает функция**:
1. Преобразует `patterns` в список, если передан строковый шаблон.
2. Итерируется по списку шаблонов.
3. Для каждого шаблона использует `rglob` для рекурсивного поиска файлов, соответствующих шаблону, начиная с `root_dir`.
4. Выдает каждый найденный путь к файлу с помощью `yield from`.
5. Если возникает ошибка, логирует ее.

**ASCII flowchart**:
```
    Root Directory, Patterns -> Patterns to List
    |
    Loop: For each Pattern
    |
    Recursively Glob Files (rglob)
    |
    Yield from Files
    |
    End Loop
```

**Примеры**:
```python
from pathlib import Path

# Пример рекурсивного поиска файлов с расширениями .txt и .md в текущей директории
root_dir = Path('.')
for path in recursively_yield_file_path(root_dir, ['*.txt', '*.md']):
    print(path)

# Пример рекурсивного поиска всех файлов в директории
root_dir = Path('.')
for path in recursively_yield_file_path(root_dir):
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

**Назначение**: Рекурсивно получает список путей ко всем файлам, соответствующим заданным шаблонам, в указанной директории.

**Параметры**:
- `root_dir` (str | Path): Корневая директория для поиска.
- `patterns` (str | list[str], optional): Шаблоны для фильтрации файлов. По умолчанию `'*'`.

**Возвращает**:
- `list[Path]`: Список путей к файлам, соответствующим шаблонам.

**Как работает функция**:
1. Преобразует `patterns` в список, если это строка.
2. Создает пустой список `file_paths` для хранения результатов.
3. Для каждого шаблона в списке `patterns` выполняет рекурсивный поиск файлов, соответствующих шаблону, используя `Path(root_dir).rglob(pattern)`.
4. Добавляет найденные пути к файлам в список `file_paths`.
5. Возвращает список `file_paths`.
6. Если возникает ошибка, логирует ее и возвращает пустой список.

**ASCII flowchart**:
```
    Root Directory,