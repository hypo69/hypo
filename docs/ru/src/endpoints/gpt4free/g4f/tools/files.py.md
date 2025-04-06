# Модуль для работы с файлами
## Обзор

Модуль предоставляет набор функций для обработки различных типов файлов, включая текстовые файлы, PDF, DOCX, ODT, EPUB, XLSX, HTML и ZIP архивы. Он также включает функции для скачивания файлов из интернета, кэширования содержимого и извлечения информации. Модуль предназначен для использования в проектах, требующих обработки и анализа больших объемов текстовых данных, извлеченных из различных источников.
Расположение файла в проекте `hypotez` указывает на то, что он является частью подсистемы, отвечающей за взаимодействие с внешними файлами и данными, возможно, для последующего анализа или обработки другими компонентами системы.

## Подробнее

Этот модуль играет важную роль в обработке и анализе файлов различных форматов, предоставляя функциональность для чтения, извлечения текста, кэширования и скачивания. Он позволяет системе `hypotez` эффективно работать с данными, поступающими из разнообразных источников.
Он включает в себя следующие возможности:

- Чтение и извлечение текста из различных форматов файлов (txt, xml, json, pdf, docx, odt, epub, xlsx, html, zip).
- Скачивание файлов по URL-адресам.
- Кэширование содержимого файлов для повышения производительности.
- Разбиение файлов на части для обработки большими объемами данных.
- Использование библиотеки `spacy` для улучшения качества извлеченного текста.

## Функции

### `secure_filename`

```python
def secure_filename(filename: str) -> str:
    """
    Очищает имя файла, удаляя небезопасные символы.

    Args:
        filename (str): Имя файла для очистки.

    Returns:
        str: Очищенное имя файла.

    Как работает функция:
    1. Если `filename` равно `None`, функция возвращает `None`.
    2. Использует регулярное выражение для замены всех символов, кроме букв, цифр, точек, запятых, подчеркиваний, плюсов и минусов, на символ подчеркивания `_`.
    3. Удаляет все URL-кодированные символы с помощью `urllib.parse.unquote`.
    4. Ограничивает длину имени файла до 100 символов и удаляет символы ".,_+" с начала и конца строки.

    Flowchart:
    Имя файла --> Проверка на None --> Замена небезопасных символов --> URL-декодирование --> Обрезка длины --> Удаление лишних символов --> Возврат очищенного имени файла

    Примеры:
        >>> secure_filename("безпечне_ім'я_файлу.txt")
        'безпечне_ім_я_файлу.txt'
        >>> secure_filename("config.json")
        'config.json'
        >>> secure_filename("file_with_spaces.txt")
        'file_with_spaces.txt'
    """
    ...
```

### `supports_filename`

```python
def supports_filename(filename: str):
    """
    Проверяет, поддерживается ли указанный тип файла для обработки.

    Args:
        filename (str): Имя файла для проверки.

    Returns:
        bool: `True`, если файл поддерживается, `False` в противном случае.

    Raises:
        MissingRequirementsError: Если отсутствуют необходимые зависимости для обработки определенного типа файла.

    Как работает функция:
    1. Проверяет расширение файла и наличие необходимых библиотек для обработки.
    2. Если файл PDF, проверяет наличие `pypdf2`, `pdfplumber` или `pdfminer`.
    3. Если файл DOCX, проверяет наличие `docx` или `docx2txt`.
    4. Если файл ODT, проверяет наличие `odfpy`.
    5. Если файл EPUB, проверяет наличие `ebooklib`.
    6. Если файл XLSX, проверяет наличие `openpyxl`.
    7. Если файл HTML, проверяет наличие `beautifulsoup4`.
    8. Если файл ZIP, возвращает `True`.
    9. Для остальных файлов проверяет, входит ли расширение в список `PLAIN_FILE_EXTENSIONS`.

    Flowchart:
    Имя файла --> Проверка расширения --> Проверка зависимостей --> Возврат True/False или вызов исключения

    Примеры:
        >>> supports_filename("example.pdf")
        True  # если установлены pypdf2, pdfplumber или pdfminer
        >>> supports_filename("example.docx")
        True  # если установлены docx или docx2txt
        >>> supports_filename("example.txt")
        True
    """
    ...
```

### `get_bucket_dir`

```python
def get_bucket_dir(*parts):
    """
    Формирует путь к каталогу bucket на основе переданных частей.

    Args:
        *parts: Переменное количество частей пути к каталогу.

    Returns:
        str: Полный путь к каталогу bucket.

    Как работает функция:
    1. Получает базовый путь к каталогу cookies.
    2. Добавляет к нему подкаталог "buckets".
    3. Добавляет остальные части пути, очищая их с помощью `secure_filename`.
    4. Объединяет все части пути с помощью `os.path.join`.

    Flowchart:
    Части пути --> Очистка частей пути --> Объединение частей пути --> Возврат полного пути

    Примеры:
        >>> get_bucket_dir("my_bucket", "file1.txt")
        '/path/to/cookies/buckets/my_bucket/file1.txt'
    """
    ...
```

### `get_buckets`

```python
def get_buckets():
    """
    Возвращает список всех существующих каталогов bucket.

    Args:
        None

    Returns:
        list: Список имен каталогов bucket или `None`, если каталог не существует.

    Как работает функция:
    1. Формирует путь к каталогу buckets.
    2. Пытается получить список подкаталогов в каталоге buckets.
    3. Возвращает список каталогов, если они существуют, или `None`, если каталог buckets не существует.

    Flowchart:
    Получение пути к каталогу buckets --> Получение списка подкаталогов --> Возврат списка или None

    Примеры:
        >>> get_buckets()
        ['bucket1', 'bucket2']
    """
    ...
```

### `spacy_refine_chunks`

```python
def spacy_refine_chunks(source_iterator):
    """
    Использует `spacy` для улучшения качества текста, разделенного на части.

    Args:
        source_iterator (Iterator[str]): Итератор, возвращающий части текста.

    Yields:
        str: Улучшенные части текста.

    Raises:
        MissingRequirementsError: Если библиотека `spacy` не установлена.

    Как работает функция:
    1. Проверяет, установлена ли библиотека `spacy`. Если нет, вызывает исключение `MissingRequirementsError`.
    2. Загружает модель `spacy` "en_core_web_sm".
    3. Для каждой части текста создает объект `doc` с помощью `nlp`.
    4. Извлекает предложения из `doc` и сортирует их по длине текста в обратном порядке.
    5. Возвращает два самых длинных предложения из каждой части текста.

    Flowchart:
    Итератор частей текста --> Проверка наличия spacy --> Загрузка модели spacy --> Обработка каждой части текста --> Извлечение предложений --> Сортировка предложений --> Возврат двух самых длинных предложений

    Примеры:
        >>> iterator = iter(["This is the first sentence. This is the second sentence.", "Another sentence here."])
        >>> list(spacy_refine_chunks(iterator))
        ['This is the first sentence. This is the second sentence.', 'Another sentence here.']
    """
    ...
```

### `get_filenames`

```python
def get_filenames(bucket_dir: Path):
    """
    Возвращает список имен файлов, хранящихся в файле `FILE_LIST` в указанном каталоге.

    Args:
        bucket_dir (Path): Путь к каталогу bucket.

    Returns:
        list: Список имен файлов.

    Как работает функция:
    1. Формирует путь к файлу `FILE_LIST` в указанном каталоге.
    2. Если файл существует, открывает его и считывает имена файлов построчно.
    3. Удаляет пробельные символы в начале и конце каждой строки.
    4. Возвращает список имен файлов.

    Flowchart:
    Путь к каталогу --> Формирование пути к файлу FILE_LIST --> Проверка существования файла --> Чтение имен файлов --> Возврат списка имен файлов

    Примеры:
        >>> bucket_dir = Path("/path/to/bucket")
        >>> # Создаем файл FILE_LIST с содержимым "file1.txt\\nfile2.txt"
        >>> get_filenames(bucket_dir)
        ['file1.txt', 'file2.txt']
    """
    ...
```

### `stream_read_files`

```python
def stream_read_files(bucket_dir: Path, filenames: list, delete_files: bool = False) -> Iterator[str]:
    """
    Читает содержимое файлов из указанного каталога bucket и возвращает его в виде потока строк.

    Args:
        bucket_dir (Path): Путь к каталогу bucket.
        filenames (list): Список имен файлов для чтения.
        delete_files (bool): Удалять ли файлы после прочтения.

    Yields:
        str: Содержимое файлов.

    Как работает функция:
    1. Для каждого имени файла в списке `filenames` проверяет его существование и размер.
    2. Если файл является ZIP-архивом, извлекает все файлы из него и рекурсивно вызывает `stream_read_files` для извлеченных файлов.
    3. Если файл PDF, DOCX, ODT, EPUB, XLSX или HTML, использует соответствующие библиотеки для извлечения текста.
    4. Если файл имеет одно из расширений, перечисленных в `PLAIN_FILE_EXTENSIONS`, читает его содержимое как обычный текст.
    5. Если `delete_files` равно `True`, удаляет файл после прочтения.

    Flowchart:
    Путь к каталогу, список имен файлов --> Для каждого файла: проверка существования и размера --> Обработка в зависимости от типа файла --> Извлечение содержимого --> Если delete_files: удаление файла --> Возврат содержимого

    Примеры:
        >>> bucket_dir = Path("/path/to/bucket")
        >>> filenames = ["file1.txt", "file2.pdf"]
        >>> # Создаем файлы file1.txt и file2.pdf
        >>> for chunk in stream_read_files(bucket_dir, filenames):
        ...     print(chunk)
    """
    ...
```

### `cache_stream`

```python
def cache_stream(stream: Iterator[str], bucket_dir: Path) -> Iterator[str]:
    """
    Кэширует поток данных в файл и возвращает поток данных.

    Args:
        stream (Iterator[str]): Поток данных для кэширования.
        bucket_dir (Path): Путь к каталогу bucket.

    Yields:
        str: Часть данных из потока.

    Как работает функция:
    1. Формирует пути к файлу кэша и временному файлу.
    2. Если файл кэша существует, возвращает его содержимое.
    3. Если файл кэша не существует, открывает временный файл для записи.
    4. Для каждой части данных в потоке записывает ее во временный файл и возвращает.
    5. После записи всех данных переименовывает временный файл в файл кэша.

    Flowchart:
    Поток данных, путь к каталогу --> Проверка существования файла кэша --> Если существует: возврат содержимого файла кэша --> Если не существует: открытие временного файла --> Запись данных во временный файл --> Переименование временного файла в файл кэша --> Возврат данных

    Примеры:
        >>> stream = iter(["chunk1", "chunk2"])
        >>> bucket_dir = Path("/path/to/bucket")
        >>> for chunk in cache_stream(stream, bucket_dir):
        ...     print(chunk)
    """
    ...
```

### `is_complete`

```python
def is_complete(data: str):
    """
    Проверяет, является ли строка данных завершенной.

    Args:
        data (str): Строка данных для проверки.

    Returns:
        bool: `True`, если строка завершена, `False` в противном случае.

    Как работает функция:
    1. Проверяет, заканчивается ли строка данных последовательностью "\\n```\\n\\n".
    2. Проверяет, является ли количество вхождений "```" в строке данных четным числом.
    3. Возвращает `True`, если оба условия выполняются, `False` в противном случае.

    Flowchart:
    Строка данных --> Проверка окончания строки --> Проверка четности количества "```" --> Возврат True/False

    Примеры:
        >>> is_complete("some data\\n```\\n\\n")
        True
        >>> is_complete("some data```")
        False
        >>> is_complete("some data\\n```\\n\\n```")
        False
    """
    ...
```

### `read_path_chunked`

```python
def read_path_chunked(path: Path):
    """
    Читает файл по частям (chunks) указанного размера.

    Args:
        path (Path): Путь к файлу.

    Yields:
        str: Часть содержимого файла.

    Как работает функция:

    1. Открывает файл для чтения в кодировке UTF-8.
    2. Инициализирует переменные `current_chunk_size` и `buffer` для отслеживания размера текущего чанка и его содержимого.
    3. Итерируется по каждой строке в файле.
        - Добавляет длину строки в байтах к `current_chunk_size`.
        - Добавляет строку в `buffer`.
        - Если `current_chunk_size` превышает 4096 байт:
            - Проверяет, является ли `buffer` завершенным (с помощью функции `is_complete`) или `current_chunk_size` превышает 8192 байта.
            - Если условие выполнено, возвращает `buffer` и сбрасывает `buffer` и `current_chunk_size`.
    4. Если после завершения цикла в `buffer` осталось содержимое, возвращает его.

    Flowchart:

    ```
    OpenFile  -->  InitVars --> LoopLines
    LoopLines -->  AddLineToBuffer --> CheckChunkSize
    CheckChunkSize --> (Size >= 4096) --> CheckIsComplete
    CheckIsComplete --> (Complete OR Size >= 8192) --> YieldBuffer --> ResetVars --> LoopLines
    CheckIsComplete --> (Not Complete) --> LoopLines
    CheckChunkSize --> (Size < 4096) --> LoopLines
    LoopLines --> (No More Lines) --> CheckBufferNotEmpty
    CheckBufferNotEmpty --> (Buffer Not Empty) --> YieldBuffer
    ```

    Примеры:
    ```python
    # Создание временного файла для примера
    with open("temp_file.txt", "w", encoding="utf-8") as f:
        f.write("This is a line.\n" * 200)  # Создание файла с 200 строками

    # Чтение файла по частям
    for chunk in read_path_chunked(Path("temp_file.txt")):
        print(f"Chunk size: {len(chunk)}, Content: {chunk[:50]}...")

    # Удаление временного файла
    os.remove("temp_file.txt")
    ```
    """
    ...
```

### `read_bucket`

```python
def read_bucket(bucket_dir: Path):
    """
    Читает содержимое bucket из кэшированных файлов.

    Args:
        bucket_dir (Path): Путь к каталогу bucket.

    Yields:
        str: Содержимое кэшированных файлов.

    Как работает функция:
    1. Формирует пути к файлам кэша: основному и файлам, обработанным с помощью `spacy`.
    2. Если существует основной файл кэша и не существует файл, обработанный с помощью `spacy`, возвращает содержимое основного файла кэша.
    3. Перебирает файлы, обработанные с помощью `spacy`, и обычные файлы, начиная с индекса 1, и возвращает их содержимое.
    4. Останавливается, когда файл с текущим индексом не существует.

    Flowchart:

    ```
    GetCachePaths --> CheckMainCache --> (MainCacheExists AND NoSpacyCache) --> YieldMainCache
    GetCachePaths --> LoopFiles --> CheckSpacyCache
    CheckSpacyCache --> (SpacyCacheExists) --> YieldSpacyCache --> LoopFiles
    CheckSpacyCache --> (NoSpacyCache) --> CheckPlainCache
    CheckPlainCache --> (PlainCacheExists) --> YieldPlainCache --> LoopFiles
    CheckPlainCache --> (NoPlainCache) --> BreakLoop
    ```

    Примеры:
    ```python
    # Создание временных файлов для примера
    os.makedirs("temp_bucket", exist_ok=True)
    with open("temp_bucket/plain_0001.cache", "w", encoding="utf-8") as f:
        f.write("This is plain cache 1.")
    with open("temp_bucket/spacy_0002.cache", "w", encoding="utf-8") as f:
        f.write("This is spacy cache 2.")

    # Чтение bucket
    for chunk in read_bucket(Path("temp_bucket")):
        print(f"Content: {chunk}")

    # Удаление временных файлов
    import shutil
    shutil.rmtree("temp_bucket")
    ```
    """
    ...
```

### `stream_read_parts_and_refine`

```python
def stream_read_parts_and_refine(bucket_dir: Path, delete_files: bool = False) -> Iterator[str]:
    """
    Читает части файла из указанного каталога bucket, улучшает их с помощью `spacy` и возвращает в виде потока строк.

    Args:
        bucket_dir (Path): Путь к каталогу bucket.
        delete_files (bool): Удалять ли исходные файлы после обработки.

    Yields:
        str: Улучшенные части файла.

    Как работает функция:
    1. Формирует пути к файлам кэша, обработанным с помощью `spacy`, и обычным файлам.
    2. Если не существует файл, обработанный с помощью `spacy`, и обычный файл, но существует основной файл кэша, разбивает основной файл кэша на части с помощью `split_file_by_size_and_newline`.
    3. Перебирает обычные файлы, начиная с индекса 1.
    4. Для каждого обычного файла формирует пути к временному файлу и файлу кэша, обработанному с помощью `spacy`.
    5. Если существует файл кэша, обработанный с помощью `spacy`, возвращает его содержимое.
    6. Если файл кэша, обработанный с помощью `spacy`, не существует, открывает временный файл для записи.
    7. Для каждой части текста, возвращенной функцией `spacy_refine_chunks`, записывает ее во временный файл и возвращает.
    8. Переименовывает временный файл в файл кэша, обработанный с помощью `spacy`.
    9. Если `delete_files` равно `True`, удаляет обычный файл.

    Flowchart:

    ```
    GetCachePaths --> CheckFilesExist --> (NoSpacyAndNoPlain AND MainCacheExists) --> SplitMainCache
    GetCachePaths --> LoopFiles --> CheckSpacyCache
    CheckSpacyCache --> (SpacyCacheExists) --> YieldSpacyCache --> LoopFiles
    CheckSpacyCache --> (NoSpacyCache) --> OpenTmpFile
    OpenTmpFile --> SpacyRefine --> WriteToTmpFile --> YieldChunk --> SpacyRefine
    SpacyRefine --> (NoMoreChunks) --> RenameTmpToCache --> DeletePlain --> LoopFiles
    LoopFiles --> (NoMoreFiles) --> End
    ```

    Примеры:
    ```python
    # Создание временных файлов для примера
    os.makedirs("temp_bucket", exist_ok=True)
    with open("temp_bucket/plain_0001.cache", "w", encoding="utf-8") as f:
        f.write("This is the first sentence. This is the second sentence.")

    # Чтение и улучшение частей файла
    for chunk in stream_read_parts_and_refine(Path("temp_bucket")):
        print(f"Refined chunk: {chunk}")

    # Удаление временных файлов
    import shutil
    shutil.rmtree("temp_bucket")
    ```
    """
    ...
```

### `split_file_by_size_and_newline`

```python
def split_file_by_size_and_newline(input_filename, output_dir, chunk_size_bytes=1024*1024):
    """
    Разделяет файл на части заданного размера, разделяя только по символу новой строки.

    Args:
        input_filename: Путь к входному файлу.
        output_dir: Каталог для выходных файлов.
        chunk_size_bytes: Желаемый размер каждой части в байтах (по умолчанию 1MB).

    Как работает функция:
    1. Определяет префикс для выходных файлов на основе имени входного файла и выходного каталога.
    2. Открывает входной файл для чтения в кодировке UTF-8.
    3. Инициализирует переменные для отслеживания номера части, текущей части и ее размера.
    4. Итерируется по каждой строке во входном файле:
        - Добавляет строку в текущую часть.
        - Добавляет размер строки в байтах к размеру текущей части.
        - Если размер текущей части превышает заданный размер (`chunk_size_bytes`):
            - Определяет имя выходного файла для текущей части.
            - Открывает выходной файл для записи в кодировке UTF-8.
            - Записывает текущую часть в выходной файл.
            - Сбрасывает текущую часть и ее размер.
            - Увеличивает номер части.
    5. После завершения цикла записывает последнюю часть (если она не пуста) в отдельный файл.

    Flowchart:

    ```
    OpenFile --> InitVars --> LoopLines
    LoopLines --> AddLineToChunk --> UpdateChunkSize --> CheckChunkSize
    CheckChunkSize --> (ChunkSize >= MaxSize) --> CreateOutputFile --> WriteChunkToFile
    WriteChunkToFile --> ResetChunkVars --> IncChunkNum --> LoopLines
    CheckChunkSize --> (ChunkSize < MaxSize) --> LoopLines
    LoopLines --> (NoMoreLines) --> CheckLastChunkNotEmpty
    CheckLastChunkNotEmpty --> (LastChunkNotEmpty) --> CreateOutputFile --> WriteChunkToFile
    ```

    Примеры:
    ```python
    # Создание временного файла для примера
    with open("temp_file.txt", "w", encoding="utf-8") as f:
        f.write("This is a line.\n" * 2000)  # Создание файла с 2000 строками

    # Разделение файла на части
    split_file_by_size_and_newline("temp_file.txt", "temp_output")

    # Проверка, что файлы созданы
    import os
    print(f"Files created: {os.listdir('temp_output')}")

    # Удаление временных файлов
    import shutil
    shutil.rmtree("temp_output")
    os.remove("temp_file.txt")
    ```
    """
    ...
```

### `get_filename`

```python
async def get_filename(response: ClientResponse) -> str:
    """
    Пытается извлечь имя файла из HTTP-ответа.

    Args:
        response (ClientResponse): Объект HTTP-ответа aiohttp.

    Returns:
        str: Имя файла или None, если не удалось определить.

    Как работает функция:
    1. Проверяет наличие заголовка Content-Disposition и пытается извлечь имя файла из него.
    2. Если заголовок Content-Disposition отсутствует или не содержит имени файла, извлекает тип контента и URL из ответа.
    3. Если тип контента и URL доступны, пытается определить расширение файла.
    4. Генерирует имя файла на основе URL, хеша URL и расширения.
    5. Возвращает очищенное имя файла или None, если не удалось определить имя файла.

    Flowchart:

    ```
    GetContentDisposition --> (ContentDispositionExists) --> ExtractFilename --> ReturnFilename
    GetContentDisposition --> (ContentDispositionMissing) --> GetContentTypeAndUrl --> CheckContentTypeAndUrl
    CheckContentTypeAndUrl --> (ContentTypeAndUrlAvailable) --> GetFileExtension --> GenerateFilename
    GenerateFilename --> ReturnFilename
    CheckContentTypeAndUrl --> (ContentTypeOrUrlMissing) --> ReturnNone
    ```

    Примеры:
    ```python
    # Пример использования требует реального ClientResponse, который можно получить только в асинхронном контексте.
    # Этот пример демонстрирует логику функции, а не ее выполнение.
    # import aiohttp

    # async def example():
    #     async with aiohttp.ClientSession() as session:
    #         async with session.get("https://example.com/file.pdf") as response:
    #             filename = await get_filename(response)
    #             print(filename)

    # asyncio.run(example())
    ```
    """
    ...
```

### `get_file_extension`

```python
async def get_file_extension(response: ClientResponse):
    """
    Определяет расширение файла на основе HTTP-ответа.

    Args:
        response (ClientResponse): Объект HTTP-ответа aiohttp.

    Returns:
        str: Расширение файла (например, ".html", ".json", ".pdf", ".zip", ".md", ".txt") или None, если не удалось определить.

    Как работает функция:
    1. Извлекает заголовок Content-Type из ответа.
    2. На основе типа контента определяет расширение файла.
    3. Если тип контента не позволяет определить расширение, пытается извлечь расширение из URL.
    4. Возвращает расширение файла или None, если не удалось определить.

    Flowchart:

    ```
    GetContentType --> CheckContentType --> (ContentTypeExists) --> DetermineExtensionFromContentType
    DetermineExtensionFromContentType --> ReturnExtension
    CheckContentType --> (ContentTypeMissing) --> GetUrl --> ExtractExtensionFromUrl
    ExtractExtensionFromUrl --> ReturnExtension
    GetUrl --> (NoUrl) --> ReturnNone
    ```

    Примеры:
    ```python
    # Пример использования требует реального ClientResponse, который можно получить только в асинхронном контексте.
    # Этот пример демонстрирует логику функции, а не ее выполнение.
    # import aiohttp

    # async def example():
    #     async with aiohttp.ClientSession() as session:
    #         async with session.get("https://example.com/file.pdf") as response:
    #             extension = await get_file_extension(response)
    #             print(extension)

    # asyncio.run(example())
    ```
    """
    ...
```

### `read_links`

```python
def read_links(html: str, base: str) -> set[str]:
    """
    Извлекает ссылки из HTML-кода.

    Args:
        html (str): HTML-код для анализа.
        base (str): Базовый URL для объединения относительных ссылок.

    Returns:
        set[str]: Множество URL-адресов, найденных в HTML-коде.

    Как работает функция:
    1. Использует BeautifulSoup для анализа HTML-кода.
    2. Пытается найти основной контент, используя различные селекторы CSS.
    3. Извлекает все ссылки из тегов `<a>`, исключая ссылки с атрибутом `rel="nofollow"`.
    4. Объединяет относительные ссылки с базовым URL.
    5. Возвращает множество уникальных URL-адресов.

    Flowchart:

    ```
    ParseHtml --> FindMainContent --> ExtractLinks --> FilterLinks --> JoinRelativeLinks --> ReturnUniqueUrls
    ```

    Примеры:
    ```python
    html = '<a href="https://example.com">Example</a> <a href="/relative">Relative</a>'
    base = "https://base.com"
    links = read_links(html, base)
    print(links)  # Вывод: {'https://example.com', 'https://base.com/relative'}
    ```
    """
    ...
```

### `download_urls`

```python
async def download_urls(
    bucket_dir: Path,
    urls: list[str],
    max_depth: int = 0,
    loading_urls: set[str] = set(),
    lock: asyncio.Lock = None,
    delay: int = 3,
    new_urls: list[str] = list(),
    group_size: int = 5,
    timeout: int = 10,
    proxy: Optional[str] = None
) -> AsyncIterator[str]:
    """
    Асинхронно скачивает файлы по URL-адресам.

    Args:
        bucket_dir (Path): Каталог для сохранения скачанных файлов.
        urls (list[str]): Список URL-адресов для скачивания.
        max_depth (int): Максимальная глубина рекурсивного скачивания HTML-страниц (по умолчанию 0).
        loading_urls (set[str]): Множество URL-адресов, которые уже находятся в процессе скачивания (используется для предотвращения повторного скачивания).
        lock (asyncio.Lock): Блокировка для синхронизации доступа к общим ресурсам (по умолчанию None).
        delay (int): Задержка в секундах между запросами (по умолчанию 3).
        new_urls (list[str]): Список новых URL-адресов, найденных на скачанных страницах (используется для рекурсивного скачивания) (по умолчанию пустой список).
        group_size (int): Количество URL-адресов, которые будут скачиваться одновременно (по умолчанию 5).
        timeout (int): Максимальное время ожидания ответа от сервера в секундах (по умолчанию 10).
        proxy (Optional[str]): URL прокси-сервера (по умолчанию None).

    Yields:
        str: Имя скачанного файла.

    Как работает функция:
    1.  Инициализирует `asyncio.Lock`, если он не был передан.

    2.  Создает асинхронную сессию `ClientSession` с заданными параметрами (прокси, таймаут).

    3.  Определяет внутреннюю асинхронную функцию `download_url`, которая выполняет скачивание одного URL:
        *   Выполняет GET-запрос к URL.
        *   Извлекает имя файла из ответа.
        *   Проверяет, разрешено ли расширение файла и поддерживается ли оно.
        *   Если это HTML-страница и `max_depth > 0`, извлекает ссылки со страницы и добавляет их в список `new_urls` для дальнейшего скачивания.
        *   Сохраняет содержимое ответа в файл.
        *   Возвращает имя файла.

    4.  Запускает группу асинхронных задач `download_url` для всех URL-адресов в списке `urls`.

    5.  Возвращает имена скачанных файлов.

    6.  Если были найдены новые URL-адреса (`new_urls` не пуст), рекурсивно вызывает `download_urls` для каждой группы URL-адресов из `new_urls` с уменьшенной глубиной `max_depth`.

    Flowchart:

    ```
    InitSession --> LoopUrls --> DownloadUrl --> (DownloadSuccess) --> YieldFilename
    DownloadUrl --> (HtmlAndMaxDepth > 0) --> ExtractLinks --> AddToNewUrls
    LoopUrls --> (DownloadFailed) --> Sleep --> LoopUrls
    LoopUrls --> (NewUrlsNotEmpty) --> RecursiveCall
    ```
    """
    ...
```

### `get_downloads_urls`

```python
def get_downloads_urls(bucket_dir: Path, delete_files: bool = False) -> Iterator[str]:
    """
    Получает список URL-адресов для скачивания из файла `DOWNLOADS_FILE`.

    Args:
        bucket_dir (Path): Путь к каталогу bucket.
        delete_files (bool): Удалять ли файл `DOWNLOADS_FILE` после прочтения.

    Yields:
        dict: Словарь с информацией о URL-адресах для скачивания.

    Как работает функция:
    1. Формирует путь к файлу `DOWNLOADS_FILE` в указанном каталоге.
    2. Если файл существует, открывает его и загружает данные из него.
    3. Если `delete_files` равно `True`, удаляет файл `DOWNLOADS_FILE`.
    4. Перебирает элементы в загруженных данных.
    5. Для каждого элемента проверяет наличие ключей "url" или "urls".
    6. Возвращает словарь с информацией о URL-адресах для скачивания.

    Flowchart:

    ```
    GetDownloadFile --> CheckDownloadFileExists --> (DownloadFileExists) --> LoadData
    LoadData --> (DeleteFiles) --> DeleteDownloadFile
    LoadData --> LoopItems --> CheckUrlKey --> (UrlKeyExists) --> YieldItem
    CheckUrlKey --> (UrlKeyMissing) --> CheckUrlsKey --> (UrlsKeyExists) --> YieldItem
    ```
    """
    ...
```

### `read_and_download_urls`

```python
def read_and_download_urls(bucket_dir: Path, delete_files: bool = False, event_stream: bool = False) -> Iterator[str]:
    """
    Читает URL-адреса из файла загрузок и скачивает их.

    Args:
        bucket_dir (Path): Путь к каталогу bucket.
        delete_files (bool): Удалять ли файл загрузок после прочтения.
        event_stream (bool): Генерировать ли события о процессе скачивания.

    Yields:
        str: События о процессе скачивания, если `event_stream` равно `True`.

    Как работает функция:
    1. Получает список URL-адресов из файла загрузок с помощью `get_downloads_urls`.