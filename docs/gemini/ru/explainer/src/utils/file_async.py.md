## ИНСТРУКЦИЯ:

Анализируй предоставленный код подробно и объясни его функциональность. Ответ должен включать три раздела:

1.  **<алгоритм>**: Опиши рабочий процесс в виде пошаговой блок-схемы, включая примеры для каждого логического блока, и проиллюстрируй поток данных между функциями, классами или методами.
2.  **<mermaid>**: Напиши код для диаграммы в формате `mermaid`, проанализируй и объясни все зависимости,
    которые импортируются при создании диаграммы.
    **ВАЖНО!** Убедитесь, что все имена переменных, используемые в диаграмме `mermaid`,
    имеют осмысленные и описательные имена. Имена переменных вроде `A`, `B`, `C`, и т.д., не допускаются!

    **Дополнительно**: Если в коде есть импорт `import header`, добавьте блок `mermaid` flowchart, объясняющий `header.py`:
    ```mermaid
    flowchart TD
        Start --> Header[<code>header.py</code><br> Determine Project Root]

        Header --> import[Import Global Settings: <br><code>from src import gs</code>]
    ```

3.  **<объяснение>**: Предоставьте подробные объяснения:
    *   **Импорты**: Их назначение и взаимосвязь с другими пакетами `src.`.
    *   **Классы**: Их роль, атрибуты, методы и взаимодействие с другими компонентами проекта.
    *   **Функции**: Их аргументы, возвращаемые значения, назначение и примеры.
    *   **Переменные**: Их типы и использование.
    *   Выделите потенциальные ошибки или области для улучшения.

Дополнительно, постройте цепочку взаимосвязей с другими частями проекта (если применимо).

Это обеспечивает всесторонний и структурированный анализ кода.
## Формат ответа: `.md` (markdown)
**КОНЕЦ ИНСТРУКЦИИ**

## <алгоритм>

**1. `save_text_file(file_path, data, mode='w')`**

   - **Начало:** Функция принимает `file_path` (путь к файлу), `data` (содержимое для записи) и `mode` (режим записи, по умолчанию 'w').
   - **Создание директории:** Преобразует `file_path` в объект `Path` и асинхронно создаёт родительскую директорию, если её нет.
     ```python
     file_path = Path('path/to/file.txt')
     await aiofiles.os.makedirs(file_path.parent, exist_ok=True)
     ```
   - **Открытие файла:** Асинхронно открывает файл в заданном режиме ('w' или 'a') с кодировкой UTF-8.
     ```python
     async with aiofiles.open(file_path, mode, encoding='utf-8') as file:
     ```
   - **Запись данных:**
       - Если `data` — это список, записывает каждую строку с новой строки.
         ```python
         if isinstance(data, list):
             for line in data:
                 await file.write(f'{line}\n')
         ```
       - Если `data` — это словарь, записывает его как JSON с отступами.
          ```python
          elif isinstance(data, dict):
              await file.write(json.dumps(data, ensure_ascii=False, indent=4))
          ```
       - В противном случае, записывает `data` как строку.
         ```python
         else:
             await file.write(data)
         ```
   - **Успешное завершение:** Возвращает `True`.
   - **Ошибка:** При возникновении ошибки, логирует ее и возвращает `False`.

**2. `read_text_file(file_path, as_list=False, extensions=None, chunk_size=8192, recursive=False, patterns=None)`**

   - **Начало:** Функция принимает `file_path` (путь к файлу или директории), `as_list` (флаг возврата списка строк или генератора), `extensions` (список расширений), `chunk_size` (размер чанка для чтения), `recursive` (рекурсивный поиск), `patterns` (шаблоны поиска).
   - **Проверка типа `file_path`:**
     - **Файл:** Если `file_path` является файлом:
       - Если `as_list` равно `True`: возвращает асинхронный генератор строк, вызывая `_read_file_lines_generator(path, chunk_size)`.
         ```python
         if as_list:
           return _read_file_lines_generator(path, chunk_size=chunk_size)
         ```
       - Если `as_list` равно `False`: возвращает содержимое файла как строку, вызывая `_read_file_content(path, chunk_size)`.
          ```python
         else:
           return await _read_file_content(path, chunk_size=chunk_size)
          ```
     - **Директория:** Если `file_path` является директорией:
       - **Рекурсивный поиск:** Если `recursive` равно `True`:
         - Получает список файлов, используя `recursively_get_file_path()` (если `patterns` есть) или `path.rglob('*')` с фильтрацией по `extensions`.
         - Если `as_list` равно `True`: возвращает асинхронный генератор строк из всех найденных файлов, используя `yield_text_from_files()`.
         ```python
             if as_list:
                 return (
                         line
                         async for file in files
                         async for line in yield_text_from_files(file, as_list = True, chunk_size = chunk_size)
                     )
         ```
         - Если `as_list` равно `False`:  асинхронно читает содержимое всех файлов и возвращает объединенную строку (результат `read_text_file` для каждого файла), разделенную `\n`.
         ```python
          else:
             contents = await asyncio.gather(*[read_text_file(p, chunk_size=chunk_size) for p in files])
             return '\n'.join(filter(None, contents))
         ```
       - **Нерекурсивный поиск:** Если `recursive` равно `False`:
         - Получает список файлов, используя `path.iterdir()` с фильтрацией по `extensions`.
         - Если `as_list` равно `True`: возвращает асинхронный генератор строк из всех файлов, используя `read_text_file()` с `as_list=True`
           ```python
            if as_list:
                 return (line async for file in files async for line in read_text_file(file, as_list=True, chunk_size=chunk_size))
           ```
        - Если `as_list` равно `False`: асинхронно читает содержимое всех файлов и возвращает объединенную строку, разделенную `\n`.
           ```python
           else:
                contents = await asyncio.gather(*[read_text_file(p, chunk_size=chunk_size) for p in files])
                return '\n'.join(filter(None, contents))
           ```
     - **Не файл и не директория:** Логирует ошибку и возвращает `None`.
   - **Ошибка:** При возникновении ошибки, логирует ее и возвращает `None`.

**3. `yield_text_from_files(file_path, as_list=False, chunk_size=8192)`**

   - **Начало:** Функция принимает `file_path` (путь к файлу), `as_list` (флаг возврата генератора или строки) и `chunk_size` (размер чанка).
   - **Проверка типа `file_path`:**
     - **Файл:** Если `file_path` является файлом:
       - Если `as_list` равно `True`: возвращает асинхронный генератор строк, вызывая `_read_file_lines_generator(path, chunk_size)`.
         ```python
         if as_list:
           async for line in _read_file_lines_generator(path, chunk_size=chunk_size):
              yield line
         ```
       - Если `as_list` равно `False`: возвращает содержимое файла как строку, вызывая `_read_file_content(path, chunk_size)`.
         ```python
         else:
             yield await _read_file_content(path, chunk_size=chunk_size)
         ```
     - **Не файл:** Логирует ошибку.
   - **Ошибка:** При возникновении ошибки, логирует ее.

**4. `_read_file_content(file_path, chunk_size)`**

   - **Начало:** Функция принимает `file_path` (путь к файлу) и `chunk_size` (размер чанка).
   - **Чтение файла по чанкам:** Асинхронно открывает файл и читает его по частям размера `chunk_size`, накапливая содержимое в строке.
     ```python
     async with aiofiles.open(file_path, 'r', encoding='utf-8') as f:
         while True:
             chunk = await f.read(chunk_size)
             if not chunk:
                 break
             content += chunk
     ```
   - **Успешное завершение:** Возвращает строку с содержимым файла.
   - **Ошибка:** При возникновении ошибки, логирует ее и возвращает пустую строку.

**5. `_read_file_lines_generator(file_path, chunk_size)`**

   - **Начало:** Функция принимает `file_path` (путь к файлу) и `chunk_size` (размер чанка).
   - **Чтение файла по чанкам и строкам:** Асинхронно открывает файл и читает его по частям размера `chunk_size`.
   - **Разделение на строки:** Разделяет каждый чанк на строки, используя `splitlines()`.
   - **Обработка переноса строк:** Проверяет конец чанка на наличие символа переноса строки. Если нет, пытается дочитать 1 байт, если он есть, то объединяет его с последней строкой.
   - **Генерация строк:** Возвращает строки файла по одной.
   - **Ошибка:** При возникновении ошибки, логирует ее.

**6. `get_filenames_from_directory(directory, extensions='*')`**

   - **Начало:** Функция принимает `directory` (путь к директории) и `extensions` (список расширений, по умолчанию '*').
   - **Преобразование `extensions`:** Преобразует `extensions` в список расширений.
   - **Получение списка файлов:** Возвращает список имен файлов в директории, отфильтрованных по `extensions`.
   - **Ошибка:** При возникновении ошибки, логирует ее и возвращает пустой список.

**7. `recursively_yield_file_path(root_dir, patterns='*')`**

   - **Начало:** Функция принимает `root_dir` (корневая директория) и `patterns` (шаблоны фильтрации).
   - **Преобразование `patterns`:** Преобразует `patterns` в список шаблонов.
   - **Рекурсивный поиск файлов:** Возвращает асинхронный генератор путей к файлам, найденных по шаблонам.
   - **Ошибка:** При возникновении ошибки, логирует ее.

**8. `recursively_get_file_path(root_dir, patterns='*')`**

   - **Начало:** Функция принимает `root_dir` (корневая директория) и `patterns` (шаблоны фильтрации).
   - **Преобразование `patterns`:** Преобразует `patterns` в список шаблонов.
   - **Рекурсивный поиск файлов:** Возвращает список путей к файлам, найденных по шаблонам.
   - **Ошибка:** При возникновении ошибки, логирует ее и возвращает пустой список.

**9. `recursively_read_text_files(root_dir, patterns, as_list=False)`**

   - **Начало:** Функция принимает `root_dir` (корневая директория), `patterns` (шаблоны поиска) и `as_list` (флаг возврата списка строк).
   - **Проверка директории:** Проверяет, является ли `root_dir` директорией.
   - **Преобразование `patterns`:** Преобразует `patterns` в список шаблонов.
   - **Поиск и чтение файлов:**  Рекурсивно проходит по директории, ищет файлы по шаблонам.
   - **Чтение содержимого файлов:** Читает файлы, добавляя содержимое в список.
       - Если `as_list` равно `True`: возвращает список строк.
       - Если `as_list` равно `False`: возвращает список содержимого файлов.
   - **Ошибка:** При возникновении ошибки, логирует ее.

**10. `get_directory_names(directory)`**
    - **Начало:** Принимает путь к директории (`directory`).
    - **Получение списка имен директорий:** Возвращает список имен поддиректорий внутри `directory`.
    - **Обработка ошибок:** Логирует ошибку и возвращает пустой список в случае исключения.

**11. `remove_bom(path)`**

    -   **Начало:** Принимает путь к файлу или директории (`path`).
    -   **Проверка типа пути:** Проверяет, является ли `path` файлом или директорией.
    -   **Обработка файла:** Если `path` является файлом:
        -   Асинхронно открывает файл на чтение/запись.
        -   Читает содержимое, удаляет BOM (если есть), переписывает файл.
    -   **Обработка директории:** Если `path` является директорией:
        -   Рекурсивно проходит по всем поддиректориям.
        -   Для каждого файла Python, открывает файл на чтение/запись.
        -   Удаляет BOM (если есть), переписывает файл.
    -   **Обработка ошибок:** Логирует ошибки для каждого файла или директории.
    -   **Обработка неверного пути:** Логирует ошибку, если путь не является файлом или директорией.

**12. `main()`**

    - **Начало:** Точка входа для удаления BOM.
    - **Определение корневой директории:** Устанавливает корневую директорию для поиска `src`.
    - **Удаление BOM:** Вызывает функцию `remove_bom()` для удаления BOM из файлов.
    - **Логирование начала процесса:** Записывает сообщение о начале процесса в лог.

**Пример потока данных при чтении директории с `recursive=True` и `as_list=True`:**

```mermaid
flowchart TD
    Start[Start: read_text_file(path, as_list=True, recursive=True)]
    CheckPathType[Check if path is directory]
    RecursiveSearch[recursively_get_file_path() or path.rglob('*')]
    YieldFiles[yield_text_from_files() for each file in list]
    ReadFileLines[_read_file_lines_generator() for each file]
    ReturnGenerator[Return AsyncGenerator of lines]
    Start --> CheckPathType
    CheckPathType -- Is Directory --> RecursiveSearch
    RecursiveSearch --> YieldFiles
    YieldFiles --> ReadFileLines
    ReadFileLines --> ReturnGenerator
    CheckPathType -- Is File --> ReadFileLines
    CheckPathType -- None --> ReturnNone[Return None]
```

## <mermaid>

```mermaid
flowchart TD
    subgraph FileOperations [File Operations]
        save_text_file(file_path, data, mode) -->|Success| SaveSuccess[Return True]
        save_text_file(file_path, data, mode) -->|Exception| SaveError[Return False, Log Error]
        
        read_text_file(file_path, as_list, extensions, chunk_size, recursive, patterns) -->|Is File| CheckAsListFile
        read_text_file(file_path, as_list, extensions, chunk_size, recursive, patterns) -->|Is Directory| CheckRecursive
        read_text_file(file_path, as_list, extensions, chunk_size, recursive, patterns) -->|Not File or Directory| ReadErrorReturnNone[Return None, Log Error]

        subgraph File[File Operations]
            CheckAsListFile -- as_list=True --> ReadFileLinesGeneratorCall[_read_file_lines_generator()]
            CheckAsListFile -- as_list=False --> ReadFileContentCall[_read_file_content()]
            ReadFileContentCall --> ReturnContentStr[Return File Content Str]
            ReadFileLinesGeneratorCall --> ReturnGeneratorLines[Return AsyncGenerator of Lines]
        end

        subgraph Dir[Directory Operations]
            CheckRecursive -- recursive=True --> CheckPatterns
            CheckRecursive -- recursive=False --> GetFilesNoRecursive
            CheckPatterns -- Has Patterns --> GetFilesRecursivePatterns[recursively_get_file_path()]
            CheckPatterns -- No Patterns --> GetFilesRecursiveNoPatterns[path.rglob('*')]
            GetFilesRecursivePatterns --> CheckAsListDirRecursive
            GetFilesRecursiveNoPatterns --> CheckAsListDirRecursive
            GetFilesNoRecursive --> CheckAsListDirNoRecursive

            CheckAsListDirRecursive -- as_list=True --> YieldTextFromFilesCall[Yield Lines from Files]
            CheckAsListDirRecursive -- as_list=False --> ReadTextFilesRecursive[read_text_file() for each file]

            CheckAsListDirNoRecursive -- as_list=True --> ReadTextFileCallGenerator[read_text_file() for each file]
            CheckAsListDirNoRecursive -- as_list=False --> ReadTextFileCallStr[read_text_file() for each file]
            
            YieldTextFromFilesCall --> ReturnGeneratorLinesDir[Return AsyncGenerator of Lines from Directory]
            ReadTextFilesRecursive --> ReturnContentStrDir[Return Str from Directory]
            ReadTextFileCallGenerator --> ReturnGeneratorLinesDir
            ReadTextFileCallStr --> ReturnContentStrDir

         end

        yield_text_from_files(file_path, as_list, chunk_size) -->|Is File, as_list=True| YieldTextFromFilesLines[ _read_file_lines_generator()]
        yield_text_from_files(file_path, as_list, chunk_size) -->|Is File, as_list=False| YieldTextFromFilesContent[_read_file_content()]
        yield_text_from_files(file_path, as_list, chunk_size) -->|Not File| YieldTextFromFilesLogError[Log Error]
    
       
        _read_file_content(file_path, chunk_size) --> ReadFileChunkByChunk[Read File Chunk by Chunk]
        ReadFileChunkByChunk --> ReturnFileContent[Return File Content as Str]
        _read_file_lines_generator(file_path, chunk_size)--> ReadFileChunkByChunkLines[Read File Chunk By Chunk and Split Lines]
        ReadFileChunkByChunkLines--> ReturnFileLinesGenerator[Return Generator of File Lines]


        get_filenames_from_directory(directory, extensions) -->|Success|ReturnFileNameList[Return List of Filenames]
        get_filenames_from_directory(directory, extensions) -->|Exception|ReturnEmptyFileNameList[Return Empty List, Log Error]
        recursively_yield_file_path(root_dir, patterns) --> |Success| ReturnFilePathGenerator[Return AsyncGenerator of File Paths]
        recursively_yield_file_path(root_dir, patterns) --> |Exception| LogError[Log Error]
        recursively_get_file_path(root_dir, patterns) -->|Success|ReturnFilePathList[Return List of File Paths]
         recursively_get_file_path(root_dir, patterns) -->|Exception|ReturnEmptyFilePathList[Return Empty List, Log Error]
    
        recursively_read_text_files(root_dir, patterns, as_list) -->|Is Directory| ReadTextFromFilesRecursive
        recursively_read_text_files(root_dir, patterns, as_list) -->|Not Directory| ReturnEmptyListFiles[Return Empty List]
        ReadTextFromFilesRecursive -->ReturnListContentFiles[Return List of File Content]
       
        get_directory_names(directory) --> |Success| ReturnDirectoryNameList[Return List of Directory Names]
        get_directory_names(directory) --> |Exception| ReturnEmptyDirectoryNameList[Return Empty List, Log Error]
        
       
        remove_bom(path) --> |Is File| RemoveBomFromFile[Remove BOM From File]
         remove_bom(path) --> |Is Directory| RemoveBomFromDirectory[Remove BOM From Directory]
         remove_bom(path) --> |Not File or Directory| RemoveBomLogPathError[Log Path Error]
         RemoveBomFromDirectory -->RemoveBomFromFiles[Remove BOM from Files]
    end
    main() --> RemoveBomCall[remove_bom(src_directory)]
```
**Анализ зависимостей:**

1.  **`save_text_file`**:
    *   Импортирует `Path` из `pathlib` для работы с путями.
    *   Использует `aiofiles` для асинхронной работы с файлами.
    *   Использует `json` для работы с JSON.
    *   Использует `logger` из `src.logger.logger` для логирования ошибок.
2.  **`read_text_file`**:
    *   Импортирует `Path` из `pathlib` для работы с путями.
    *   Использует `asyncio.gather` для параллельного чтения нескольких файлов.
    *   Зависит от внутренних функций `_read_file_lines_generator`, `_read_file_content`, `recursively_get_file_path` и  `yield_text_from_files`.
    *   Использует `logger` из `src.logger.logger` для логирования ошибок.
3.  **`yield_text_from_files`**:
    *   Использует `Path` из `pathlib`.
    *   Зависит от внутренних функций `_read_file_lines_generator` и `_read_file_content`.
    *  Использует `logger` из `src.logger.logger` для логирования ошибок.
4.  **`_read_file_content`**:
    *   Использует `aiofiles` для асинхронного чтения файлов.
    *   Использует `logger` из `src.logger.logger` для логирования ошибок.
5.  **`_read_file_lines_generator`**:
    *   Использует `aiofiles` для асинхронного чтения файлов.
    *  Использует `logger` из `src.logger.logger` для логирования ошибок.
6.  **`get_filenames_from_directory`**:
    *   Использует `Path` из `pathlib` для работы с путями.
    *    Использует `logger` из `src.logger.logger` для логирования ошибок.
7.  **`recursively_yield_file_path`**:
    *   Использует `Path` из `pathlib` для работы с путями.
     *    Использует `logger` из `src.logger.logger` для логирования ошибок.
8.  **`recursively_get_file_path`**:
    *   Использует `Path` из `pathlib` для работы с путями.
    *   Использует `logger` из `src.logger.logger` для логирования ошибок.
9.  **`recursively_read_text_files`**:
    *   Использует `Path` из `pathlib` для работы с путями.
    *   Использует `os.walk` для рекурсивного обхода директории.
    *   Использует `fnmatch` для фильтрации файлов по шаблону.
    *   Использует `aiofiles` для асинхронного чтения файлов.
    *    Использует `logger` из `src.logger.logger` для логирования ошибок.
10. **`get_directory_names`**:
    *   Использует `Path` из `pathlib`.
     *   Использует `logger` из `src.logger.logger` для логирования ошибок.
11. **`remove_bom`**:
    *   Использует `Path` из `pathlib` для работы с путями.
    *   Использует `aiofiles` для асинхронной работы с файлами.
     *   Использует `os.walk` для рекурсивного обхода директории.
    *   Использует `logger` из `src.logger.logger` для логирования ошибок.
12. **`main`**:
    *   Использует `Path` из `pathlib` для работы с путями.
    *   Использует `asyncio.run` для запуска асинхронной функции.
    *   Вызывает `remove_bom` для удаления BOM.
    *   Использует `logger` из `src.logger.logger` для логирования.

## <объяснение>

### Импорты

*   `os`: Используется для работы с операционной системой, включая обход директорий с помощью `os.walk`.
*   `json`: Используется для сериализации и десериализации данных в формате JSON (например, при записи словаря в файл).
*   `fnmatch`: Используется для сопоставления имен файлов с шаблонами, что полезно при фильтрации файлов по расширению или имени.
*   `asyncio`: Используется для работы с асинхронным кодом, позволяя не блокировать выполнение программы во время операций ввода-вывода, таких как чтение и запись файлов.
*   `aiofiles`: Предоставляет асинхронный интерфейс для работы с файлами, что необходимо для асинхронных операций с файлами.
*   `aiofiles.os`: Используется для асинхронных операций с файловой системой (например, создание директорий).
*   `pathlib.Path`: Используется для представления путей к файлам и директориям, предоставляя более объектно-ориентированный способ работы с путями.
*   `typing.List`, `typing.Optional`, `typing.Union`, `typing.AsyncGenerator`, `typing.Generator`: Используется для аннотации типов, что помогает в отладке и улучшает читаемость кода.
*   `src.logger.logger.logger`:  Используется для логирования сообщений об ошибках и отладочной информации, что позволяет отслеживать работу программы и выявлять проблемы.

### Классы

В этом коде нет пользовательских классов, используются только стандартные классы Python и классы из импортированных библиотек (`Path`, `AsyncGenerator`).

### Функции

*   **`save_text_file(file_path, data, mode='w')`**
    *   **Аргументы**:
        *   `file_path` (str | Path): Путь к файлу для сохранения.
        *   `data` (str | list[str] | dict): Данные для записи (строка, список строк или словарь).
        *   `mode` (str, optional): Режим записи файла ('w' - перезапись, 'a' - добавление). По умолчанию 'w'.
    *   **Возвращаемое значение**:
        *   `bool`: `True`, если файл сохранен успешно, `False` в случае ошибки.
    *   **Назначение**: Асинхронно сохраняет данные в текстовый файл, поддерживая запись как строк, списков строк, так и словарей в формате JSON.
    *   **Пример**:
        ```python
        await save_text_file(Path("output.txt"), "hello world")  # Запись строки
        await save_text_file("output.txt", ["line1", "line2"], mode='a')  # Добавление списка строк
        await save_text_file(Path("data.json"), {"key": "value"})  # Запись словаря в JSON
        ```

*   **`read_text_file(file_path, as_list=False, extensions=None, chunk_size=8192, recursive=False, patterns=None)`**
    *   **Аргументы**:
        *   `file_path` (str | Path): Путь к файлу или директории.
        *   `as_list` (bool, optional): Если `True`, возвращает генератор строк (или список, если `recursive=True`), иначе строку. По умолчанию `False`.
        *   `extensions` (list[str], optional): Список расширений файлов для фильтрации (только при работе с директориями). По умолчанию `None`.
        *   `chunk_size` (int, optional): Размер чанка для чтения файла в байтах. По умолчанию `8192`.
        *   `recursive` (bool, optional): Если `True`, выполняет рекурсивный поиск в поддиректориях. По умолчанию `False`.
        *   `patterns` (str | list[str], optional): Шаблоны для фильтрации файлов при рекурсивном поиске.
    *   **Возвращаемое значение**:
        *   `AsyncGenerator[str, None] | str | list[str] | None`: Асинхронный генератор строк (если `as_list=True` и `file_path` - файл), строка (если `as_list=False` и `file_path` - файл, или если `as_list=False` и `file_path` - директория), список строк (если `as_list=True` и `file_path` - директория, `recursive=True` или список путей, если `file_path` - директория, `recursive=True` и `as_list=True`), или `None` в случае ошибки.
    *   **Назначение**: Асинхронно читает содержимое текстовых файлов или директорий, поддерживает разные режимы чтения (как одна строка или как генератор строк), а также рекурсивный обход директорий и фильтрацию файлов.
    *   **Пример**:
        ```python
        content_str = await read_text_file("input.txt")  # Чтение файла как строку
        async for line in read_text_file("input.txt", as_list=True):
            print(line) # Чтение файла построчно
        contents = await read_text_file("dir", recursive=True, extensions=['.txt'], as_list=True) # Чтение всех txt файлов из дирректории
        ```

*   **`yield_text_from_files(file_path, as_list=False, chunk_size=8192)`**
    *   **Аргументы**:
        *   `file_path` (str | Path): Путь к файлу.
        *   `as_list` (bool, optional): Если `True`, возвращает генератор строк, иначе - строку. По умолчанию `False`.
        *   `chunk_size` (int, optional): Размер чанка для чтения файла в байтах. По умолчанию `8192`.
    *   **Возвращаемое значение**:
        *   `AsyncGenerator[str, None] | str | None`: Асинхронный генератор строк или строка с содержимым файла (в зависимости от параметра `as_list`) или `None` в случае ошибки.
    *   **Назначение**: Асинхронно читает содержимое файла и возвращает его в виде генератора строк или одной строки.
    *   **Пример**:
        ```python
        async for line in yield_text_from_files("input.txt", as_list=True):
            print(line) # Чтение файла построчно
        content = await yield_text_from_files("input.txt") # Чтение файла как строку
        ```
*   **`_read_file_content(file_path, chunk_size)`**
    *   **Аргументы**:
        *   `file_path` (`Path`): Путь к файлу.
        *   `chunk_size` (int): Размер чанка для чтения файла.
    *   **Возвращаемое значение**:
        *   `str`: Содержимое файла в виде строки.
    *   **Назначение**: Асинхронно читает содержимое файла по чанкам и возвращает его как одну строку.
    *   **Пример**:
        ```python
         content = await _read_file_content(Path("input.txt"), 4096) # Чтение файла с размером чанка 4096
        ```
*   **`_read_file_lines_generator(file_path, chunk_size)`**
    *   **Аргументы**:
        *   `file_path` (`Path`): Путь к файлу.
        *   `chunk_size` (int): Размер чанка для чтения файла.
    *   **Возвращаемое значение**:
        *  `AsyncGenerator[str, None]`: Асинхронный генератор, предоставляющий строки файла.
    *   **Назначение**: Асинхронно читает файл по строкам с использованием генератора, что позволяет обрабатывать большие файлы, не загружая их полностью в память.
    *   **Пример**:
        ```python
         async for line in  _read_file_lines_generator(Path("input.txt"), 4096):
             print(line)
        ```
*   **`get_filenames_from_directory(directory, extensions='*')`**
    *   **Аргументы**:
        *   `directory` (str | Path): Путь к директории.
        *   `extensions` (str | list[str], optional): Список расширений для фильтрации. По умолчанию '\*', что соответствует всем файлам.
    *   **Возвращаемое значение**:
        *   `list[str]`: Список имен файлов в директории.
    *   **Назначение**: Асинхронно возвращает список имен файлов в директории, опционально отфильтрованных по расширению.
    *    **Пример**:
        ```python
        filenames = await get_filenames_from_directory(Path("dir"), ['.txt', '.md'])
        ```
*   **`recursively_yield_file_path(root_dir, patterns='*')`**
    *   **Аргументы**:
        *   `root_dir` (str | Path): Корневая директория для поиска.
        *   `patterns` (str | list[str], optional): Шаблоны для фильтрации файлов. По умолчанию '\*', что соответствует всем файлам.
    *   **Возвраща