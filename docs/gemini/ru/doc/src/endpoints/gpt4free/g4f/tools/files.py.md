# Модуль для работы с файлами
==============================

Модуль предоставляет набор функций для обработки различных типов файлов, включая текстовые файлы, PDF, DOCX, ODT, EPUB, XLSX, HTML и ZIP архивы. Он также включает функции для скачивания файлов из интернета и обработки URL-адресов.

## Обзор

Этот модуль предназначен для обработки и извлечения текста из различных типов файлов. Он включает в себя функции для чтения файлов, скачивания файлов по URL-адресам, кэширования данных и обработки текстовых данных с использованием библиотеки `spacy`. Модуль используется для подготовки данных для дальнейшей обработки, например, для использования в задачах машинного обучения или анализа текста.

## Подробнее

Модуль `files.py` играет важную роль в проекте `hypotez`, поскольку он обеспечивает функциональность для работы с файлами различных форматов. Он позволяет загружать, обрабатывать и извлекать информацию из файлов, что необходимо для анализа данных и выполнения других задач, связанных с обработкой текста. Модуль также включает функции для скачивания файлов из интернета, что расширяет возможности проекта по сбору и обработке данных.

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
    1. Функция принимает имя файла в качестве аргумента.
    2. Удаляет из имени файла все символы, кроме букв, цифр, символов подчеркивания, точек, запятых, плюсов и минусов.
    3. Ограничивает длину имени файла до 100 символов.
    4. Удаляет начальные и конечные символы из набора ".,_-+".

    Примеры:
    >>> secure_filename("test file.txt")
    'test_file.txt'
    >>> secure_filename("file%$#name.ext")
    'file_name.ext'
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
        MissingRequirementsError: Если отсутствуют необходимые библиотеки для обработки файла.

    Как работает функция:
    1. Функция принимает имя файла в качестве аргумента.
    2. Проверяет расширение файла и наличие необходимых библиотек для его обработки.
    3. Если файл поддерживается, возвращает `True`.
    4. Если файл не поддерживается и отсутствуют необходимые библиотеки, вызывает исключение `MissingRequirementsError`.

    Примеры:
    >>> supports_filename("test.pdf")
    True
    >>> supports_filename("test.docx")
    True
    """
    ...
```

### `get_bucket_dir`

```python
def get_bucket_dir(*parts):
    """
    Формирует путь к каталогу bucket на основе переданных частей пути.

    Args:
        *parts: Переменное количество частей пути для формирования каталога bucket.

    Returns:
        str: Полный путь к каталогу bucket.

    Как работает функция:
    1. Функция принимает переменное количество частей пути в качестве аргументов.
    2. Объединяет части пути с использованием `os.path.join`.
    3. Очищает каждую часть пути с помощью функции `secure_filename`.

    Примеры:
    >>> get_bucket_dir("test", "file.txt")
    '/path/to/buckets/test/file_txt'
    """
    ...
```

### `get_buckets`

```python
def get_buckets():
    """
    Возвращает список директорий bucket.

    Returns:
        list | None: Список директорий bucket или `None`, если директория не существует.

    Как работает функция:
    1. Функция пытается получить список директорий в каталоге `buckets`.
    2. Если каталог `buckets` существует, возвращает список его поддиректорий.
    3. Если каталог `buckets` не существует, возвращает `None`.

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
    Обрабатывает текстовые чанки с использованием библиотеки `spacy` для извлечения предложений.

    Args:
        source_iterator: Итератор, предоставляющий текстовые чанки.

    Yields:
        str: Извлеченные предложения.

    Raises:
        MissingRequirementsError: Если библиотека `spacy` не установлена.

    Как работает функция:
    1. Функция принимает итератор текстовых чанков в качестве аргумента.
    2. Загружает модель `spacy` "en_core_web_sm".
    3. Для каждого чанка текста извлекает предложения и возвращает их.

    Примеры:
    >>> chunks = ["This is a test sentence.", "Another sentence here."]
    >>> for chunk in spacy_refine_chunks(chunks):
    ...     print(chunk)
    This is a test sentence.
    Another sentence here.
    """
    ...
```

### `get_filenames`

```python
def get_filenames(bucket_dir: Path):
    """
    Возвращает список имен файлов, хранящихся в файле `FILE_LIST` в указанной директории bucket.

    Args:
        bucket_dir (Path): Путь к директории bucket.

    Returns:
        list: Список имен файлов.

    Как работает функция:
    1. Функция принимает путь к директории bucket в качестве аргумента.
    2. Проверяет, существует ли файл `FILE_LIST` в указанной директории.
    3. Если файл существует, читает его и возвращает список имен файлов, удаляя пробельные символы.
    4. Если файл не существует, возвращает пустой список.

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
    Читает содержимое файлов из указанной директории bucket и возвращает итератор строк.

    Args:
        bucket_dir (Path): Путь к директории bucket.
        filenames (list): Список имен файлов для чтения.
        delete_files (bool, optional): Если `True`, файлы будут удалены после прочтения. По умолчанию `False`.

    Yields:
        str: Содержимое файлов.

    Как работает функция:
    1. Функция принимает путь к директории bucket и список имен файлов в качестве аргументов.
    2. Итерируется по списку имен файлов.
    3. Для каждого файла проверяет его существование и размер.
    4. В зависимости от расширения файла использует соответствующие библиотеки для чтения содержимого.
    5. Если `delete_files` установлен в `True`, удаляет файлы после прочтения.

    Примеры:
    >>> bucket_dir = Path("/path/to/bucket")
    >>> filenames = ["file1.txt", "file2.pdf"]
    >>> # Создаем файлы file1.txt и file2.pdf
    >>> for chunk in stream_read_files(bucket_dir, filenames):
    ...     print(chunk)
    ```file1.txt
    Содержимое file1.txt
    
    ```
    ```file2.pdf
    Содержимое file2.pdf
    
    ```
    """
    ...
```

### `cache_stream`

```python
def cache_stream(stream: Iterator[str], bucket_dir: Path) -> Iterator[str]:
    """
    Кэширует поток данных в файл и возвращает итератор строк.

    Args:
        stream (Iterator[str]): Итератор, предоставляющий данные для кэширования.
        bucket_dir (Path): Путь к директории bucket.

    Yields:
        str: Данные из потока.

    Как работает функция:
    1. Функция принимает итератор данных и путь к директории bucket в качестве аргументов.
    2. Проверяет, существует ли кэш-файл.
    3. Если кэш-файл существует, читает его содержимое и возвращает его.
    4. Если кэш-файл не существует, создает временный файл, записывает в него данные из потока и переименовывает его в кэш-файл.

    Примеры:
    >>> bucket_dir = Path("/path/to/bucket")
    >>> data = ["chunk1", "chunk2"]
    >>> for chunk in cache_stream(iter(data), bucket_dir):
    ...     print(chunk)
    chunk1
    chunk2
    """
    ...
```

### `is_complete`

```python
def is_complete(data: str):
    """
    Проверяет, является ли переданная строка завершенным блоком данных.

    Args:
        data (str): Строка для проверки.

    Returns:
        bool: `True`, если строка является завершенным блоком данных, `False` в противном случае.

    Как работает функция:
    1. Функция принимает строку в качестве аргумента.
    2. Проверяет, заканчивается ли строка на "\\n```\\n\\n" и является ли количество "```" в строке четным числом.

    Примеры:
    >>> is_complete("test\\n```\\n\\n")
    True
    >>> is_complete("test\\n```")
    False
    """
    ...
```

### `read_path_chunked`

```python
def read_path_chunked(path: Path):
    """
    Читает файл по частям, разделяя его на чанки заданного размера.

    Args:
        path (Path): Путь к файлу.

    Yields:
        str: Чанк данных из файла.

    Как работает функция:
    1. Функция принимает путь к файлу в качестве аргумента.
    2. Открывает файл для чтения в кодировке UTF-8.
    3. Читает файл построчно, накапливая данные в буфере.
    4. Если размер буфера превышает заданный размер (4096 байт), возвращает содержимое буфера.
    5. Если буфер содержит завершенный блок данных (определяется функцией `is_complete`) или его размер превышает 8192 байта, возвращает содержимое буфера.

    Примеры:
    >>> file_path = Path("/path/to/file.txt")
    >>> # Создаем файл file.txt с содержимым "line1\\nline2\\n"
    >>> for chunk in read_path_chunked(file_path):
    ...     print(chunk)
    line1
    line2
    """
    ...
```

### `read_bucket`

```python
def read_bucket(bucket_dir: Path):
    """
    Читает содержимое bucket из кэшированных файлов.

    Args:
        bucket_dir (Path): Путь к директории bucket.

    Yields:
        str: Содержимое кэшированных файлов.

    Как работает функция:
    1. Функция принимает путь к директории bucket в качестве аргумента.
    2. Проверяет наличие файлов `PLAIN_CACHE` и `spacy_XXXX.cache` в указанной директории.
    3. Если файлы существуют, читает их содержимое и возвращает его.

    Примеры:
    >>> bucket_dir = Path("/path/to/bucket")
    >>> # Создаем файлы PLAIN_CACHE и spacy_0001.cache
    >>> for chunk in read_bucket(bucket_dir):
    ...     print(chunk)
    Содержимое PLAIN_CACHE
    Содержимое spacy_0001.cache
    """
    ...
```

### `stream_read_parts_and_refine`

```python
def stream_read_parts_and_refine(bucket_dir: Path, delete_files: bool = False) -> Iterator[str]:
    """
    Читает части файла, обрабатывает их с использованием `spacy` и возвращает итератор строк.

    Args:
        bucket_dir (Path): Путь к директории bucket.
        delete_files (bool, optional): Если `True`, части файла будут удалены после обработки. По умолчанию `False`.

    Yields:
        str: Обработанные части файла.

    Как работает функция:
    1. Функция принимает путь к директории bucket и флаг удаления файлов в качестве аргументов.
    2. Проверяет наличие файлов `PLAIN_CACHE`, `spacy_XXXX.cache` и `plain_XXXX.cache` в указанной директории.
    3. Если файлы существуют, читает их содержимое, обрабатывает с использованием `spacy` и возвращает обработанные данные.
    4. Если `delete_files` установлен в `True`, удаляет части файла после обработки.

    Примеры:
    >>> bucket_dir = Path("/path/to/bucket")
    >>> # Создаем файлы PLAIN_CACHE, spacy_0001.cache и plain_0001.cache
    >>> for chunk in stream_read_parts_and_refine(bucket_dir):
    ...     print(chunk)
    Обработанные данные
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
        output_dir: Префикс для выходных файлов (например, 'output_part_').
        chunk_size_bytes: Желаемый размер каждой части в байтах.

    Как работает функция:
    1. Функция принимает путь к входному файлу, префикс для выходных файлов и желаемый размер каждой части в байтах в качестве аргументов.
    2. Открывает входной файл для чтения в кодировке UTF-8.
    3. Читает файл построчно, накапливая данные в текущей части.
    4. Если размер текущей части превышает заданный размер, записывает ее в выходной файл и начинает новую часть.
    5. Записывает последнюю часть в выходной файл.

    Примеры:
    >>> input_filename = "/path/to/input.txt"
    >>> output_dir = "/path/to/output"
    >>> # Создаем файл input.txt с содержимым "line1\\nline2\\nline3\\n"
    >>> split_file_by_size_and_newline(input_filename, output_dir)
    # Создаются файлы output_0001.txt и output_0002.txt
    """
    ...
```

### `get_filename`

```python
async def get_filename(response: ClientResponse) -> str:
    """
    Пытается извлечь имя файла из ответа aiohttp.

    Args:
        response: Объект ClientResponse aiohttp.

    Returns:
        str: Имя файла в виде строки или None, если не удалось определить.

    Как работает функция:
    1. Функция принимает объект `ClientResponse` в качестве аргумента.
    2. Пытается извлечь имя файла из заголовка `Content-Disposition`.
    3. Если заголовок `Content-Disposition` отсутствует или не содержит имени файла, пытается определить имя файла на основе URL.
    4. Возвращает очищенное имя файла или `None`, если не удалось определить имя файла.

    Примеры:
    >>> response = ClientResponse(...)
    >>> response.headers['Content-Disposition'] = 'filename="test.txt"'
    >>> await get_filename(response)
    'test.txt'
    """
    ...
```

### `get_file_extension`

```python
async def get_file_extension(response: ClientResponse):
    """
    Пытается определить расширение файла из ответа aiohttp.

    Args:
        response: Объект ClientResponse aiohttp.

    Returns:
        str: Расширение файла (например, ".html", ".json", ".pdf") в виде строки или None, если не удалось определить.

    Как работает функция:
    1. Функция принимает объект `ClientResponse` в качестве аргумента.
    2. Пытается определить расширение файла на основе заголовка `Content-Type`.
    3. Если заголовок `Content-Type` отсутствует или не содержит информации о расширении файла, пытается определить расширение файла на основе URL.
    4. Возвращает расширение файла или `None`, если не удалось определить расширение файла.

    Примеры:
    >>> response = ClientResponse(...)
    >>> response.headers['Content-Type'] = 'text/html'
    >>> await get_file_extension(response)
    '.html'
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
        set[str]: Множество URL-адресов.

    Как работает функция:
    1. Функция принимает HTML-код и базовый URL в качестве аргументов.
    2. Использует `BeautifulSoup` для анализа HTML-кода.
    3. Извлекает все ссылки из HTML-кода.
    4. Объединяет относительные ссылки с базовым URL.
    5. Возвращает множество URL-адресов.

    Примеры:
    >>> html = '<a href="https://example.com">Link</a>'
    >>> base = 'https://example.com'
    >>> read_links(html, base)
    {'https://example.com'}
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
        bucket_dir (Path): Директория для сохранения скачанных файлов.
        urls (list[str]): Список URL-адресов для скачивания.
        max_depth (int, optional): Максимальная глубина рекурсивного скачивания HTML-страниц. По умолчанию 0.
        loading_urls (set[str], optional): Множество URL-адресов, которые уже находятся в процессе скачивания. По умолчанию `set()`.
        lock (asyncio.Lock, optional): Блокировка для синхронизации доступа к общим ресурсам. По умолчанию `None`.
        delay (int, optional): Задержка между запросами в секундах. По умолчанию 3.
        new_urls (list[str], optional): Список новых URL-адресов, обнаруженных в процессе скачивания. По умолчанию `list()`.
        group_size (int, optional): Размер группы URL-адресов для одновременной загрузки. По умолчанию 5.
        timeout (int, optional): Время ожидания ответа от сервера в секундах. По умолчанию 10.
        proxy (Optional[str], optional): URL прокси-сервера. По умолчанию `None`.

    Yields:
        str: Имена скачанных файлов.

    Как работает функция:
    1. Функция принимает список URL-адресов и параметры скачивания в качестве аргументов.
    2. Асинхронно скачивает файлы по URL-адресам.
    3. Если скачиваемый файл является HTML-страницей и `max_depth` > 0, извлекает ссылки из HTML-кода и добавляет их в список `new_urls` для дальнейшего скачивания.
    4. Возвращает имена скачанных файлов.

    Внутренние функции:
    ### `download_url`

    ```python
    async def download_url(url: str, max_depth: int) -> str:
        """
        Асинхронно скачивает один файл по URL-адресу.

        Args:
            url (str): URL-адрес для скачивания.
            max_depth (int): Максимальная глубина рекурсивного скачивания HTML-страниц.

        Returns:
            str: Имя скачанного файла или None в случае ошибки.

        Как работает функция:
        1. Функция принимает URL-адрес и максимальную глубину рекурсивного скачивания в качестве аргументов.
        2. Асинхронно скачивает файл по URL-адресу.
        3. Если скачиваемый файл является HTML-страницей и `max_depth` > 0, извлекает ссылки из HTML-кода и добавляет их в список `new_urls` для дальнейшего скачивания.
        4. Возвращает имя скачанного файла или `None` в случае ошибки.

        """
    ```

    Примеры:
    >>> bucket_dir = Path("/path/to/bucket")
    >>> urls = ["https://example.com/file1.txt", "https://example.com/file2.pdf"]
    >>> async for filename in download_urls(bucket_dir, urls):
    ...     print(filename)
    file1.txt
    file2.pdf
    """
    ...
```

### `get_downloads_urls`

```python
def get_downloads_urls(bucket_dir: Path, delete_files: bool = False) -> Iterator[str]:
    """
    Возвращает итератор URL-адресов для скачивания из файла `DOWNLOADS_FILE`.

    Args:
        bucket_dir (Path): Путь к директории bucket.
        delete_files (bool, optional): Если `True`, файл `DOWNLOADS_FILE` будет удален после прочтения. По умолчанию `False`.

    Yields:
        str: URL-адрес для скачивания.

    Как работает функция:
    1. Функция принимает путь к директории bucket и флаг удаления файла в качестве аргументов.
    2. Проверяет наличие файла `DOWNLOADS_FILE` в указанной директории.
    3. Если файл существует, читает его содержимое и возвращает итератор URL-адресов для скачивания.
    4. Если `delete_files` установлен в `True`, удаляет файл `DOWNLOADS_FILE` после прочтения.

    Примеры:
    >>> bucket_dir = Path("/path/to/bucket")
    >>> # Создаем файл DOWNLOADS_FILE с содержимым '[{"url": "https://example.com/file1.txt"}, {"urls": ["https://example.com/file2.pdf"]}]'
    >>> for url in get_downloads_urls(bucket_dir):
    ...     print(url)
    {'urls': ['https://example.com/file1.txt']}
    {'urls': ['https://example.com/file2.pdf']}
    """
    ...
```

### `read_and_download_urls`

```python
def read_and_download_urls(bucket_dir: Path, delete_files: bool = False, event_stream: bool = False) -> Iterator[str]:
    """
    Читает URL-адреса из файла `DOWNLOADS_FILE` и скачивает файлы по этим URL-адресам.

    Args:
        bucket_dir (Path): Путь к директории bucket.
        delete_files (bool, optional): Если `True`, файл `DOWNLOADS_FILE` будет удален после прочтения. По умолчанию `False`.
        event_stream (bool, optional): Если `True`, возвращает события о процессе скачивания. По умолчанию `False`.

    Yields:
        str: События о процессе скачивания, если `event_stream` установлен в `True`.

    Как работает функция:
    1. Функция принимает путь к директории bucket, флаг удаления файла и флаг потока событий в качестве аргументов.
    2. Читает URL-адреса из файла `DOWNLOADS_FILE`.
    3. Скачивает файлы по URL-адресам.
    4. Если `event_stream` установлен в `True`, возвращает события о процессе скачивания.

    Примеры:
    >>> bucket_dir = Path("/path/to/bucket")
    >>> # Создаем файл DOWNLOADS_FILE с содержимым '[{"url": "https://example.com/file1.txt"}, {"urls": ["https://example.com/file2.pdf"]}]'
    >>> for event in read_and_download_urls(bucket_dir, event_stream=True):
    ...     print(event)
    data: {"action": "download", "count": 1}

    data: {"action": "download", "count": 2}
    """
    ...
```

### `async_read_and_download_urls`

```python
async def async_read_and_download_urls(bucket_dir: Path, delete_files: bool = False, event_stream: bool = False) -> AsyncIterator[str]:
    """
    Асинхронно читает URL-адреса из файла `DOWNLOADS_FILE` и скачивает файлы по этим URL-адресам.

    Args:
        bucket_dir (Path): Путь к директории bucket.
        delete_files (bool, optional): Если `True`, файл `DOWNLOADS_FILE` будет удален после прочтения. По умолчанию `False`.
        event_stream (bool, optional): Если `True`, возвращает события о процессе скачивания. По умолчанию `False`.

    Yields:
        str: События о процессе скачивания, если `event_stream` установлен в `True`.

    Как работает функция:
    1. Функция принимает путь к директории bucket, флаг удаления файла и флаг потока событий в качестве аргументов.
    2. Асинхронно читает URL-адреса из файла `DOWNLOADS_FILE`.
    3. Асинхронно скачивает файлы по URL-адресам.
    4. Если `event_stream` установлен в `True`, возвращает события о процессе скачивания.

    Примеры:
    >>> bucket_dir = Path("/path/to/bucket")
    >>> # Создаем файл DOWNLOADS_FILE с содержимым '[{"url": "https://example.com/file1.txt"}, {"urls": ["https://example.com/file2.pdf"]}]'
    >>> async for event in async_read_and_download_urls(bucket_dir, event_stream=True):
    ...     print(event)
    data: {"action": "download", "count": 1}

    data: {"action": "download", "count": 2}
    """
    ...
```

### `stream_chunks`

```python
def stream_chunks(bucket_dir: Path, delete_files: bool = False, refine_chunks_with_spacy: bool = False, event_stream: bool = False) -> Iterator[str]:
    """
    Генерирует чанки данных из файлов в bucket, с возможностью обработки с помощью `spacy`.

    Args:
        bucket_dir (Path): Путь к директории bucket.
        delete_files (bool, optional): Если `True`, файлы будут удалены после обработки. По умолчанию `False`.
        refine_chunks_with_spacy (bool, optional): Если `True`, чанки будут обработаны с помощью `spacy`. По умолчанию `False`.
        event_stream (bool, optional): Если `True`, возвращает события о процессе обработки. По умолчанию `False`.

    Yields:
        str: Чанки данных или события о процессе обработки, если `event_stream` установлен в `True`.

    Как работает функция:
    1. Функция принимает путь к директории bucket, флаг удаления файлов, флаг обработки с помощью `spacy` и флаг потока событий в качестве аргументов.
    2. Если `refine_chunks_with_spacy` установлен в `True`, обрабатывает чанки с использованием функции `stream_read_parts_and_refine`.
    3. Если `refine_chunks_with_spacy` не установлен в `True`, читает файлы из bucket и кэширует их содержимое.
    4. Если `event_stream` установлен в `True`, возвращает события о процессе обработки.

    Примеры:
    >>> bucket_dir = Path("/path/to/bucket")
    >>> # Создаем файлы в директории bucket
    >>> for chunk in stream_chunks(bucket_dir, event_stream=True):
    ...     print(chunk)
    data: {"action": "load", "size": 1024}

    data: {"action": "done", "size": 1024}
    """
    ...
```

### `get_streaming`

```python
def get_streaming(bucket_dir: str, delete_files = False, refine_chunks_with_spacy = False, event_stream: bool = False) -> Iterator[str]:
    """
    Основная функция для получения потока данных из bucket.

    Args:
        bucket_dir (str): Путь к директории bucket.
        delete_files (bool, optional): Если `True`, файлы будут удалены после обработки. По умолчанию `False`.
        refine_chunks_with_spacy (bool, optional): Если `True`, чанки будут обработаны с помощью `spacy`. По умолчанию `False`.
        event_stream (bool, optional): Если `True`, возвращает события о процессе обработки. По умолчанию `False`.

    Yields:
        str: Чанки данных или события о процессе обработки, если `event_stream` установлен в `True`.

    Raises:
        Exception: Если произошла ошибка в процессе обработки.

    Как работает функция:
    1. Функция принимает путь к директории bucket, флаг удаления файлов, флаг обработки с помощью `spacy` и флаг потока событий в качестве аргументов.
    2. Создает директорию bucket, если она не существует.
    3. Читает и скачивает URL-адреса из файла `DOWNLOADS_FILE`.
    4. Генерирует чанки данных из файлов в bucket.
    5. Если произошла ошибка в процессе обработки и `event_stream` установлен в `True`, возвращает событие об ошибке.

    Примеры:
    >>> bucket_dir = "/path/to/bucket"
    >>> for chunk in get_streaming(bucket_dir, event_stream=True):
    ...     print(chunk)
    data: {"action": "download", "count": 1}

    data: {"action": "load", "size": 1024}

    data: {"action": "done", "size": 1024}
    """
    ...
```

### `get_async_streaming`

```python
async def get_async_streaming(bucket_dir: str, delete_files = False, refine_chunks_with_spacy = False, event_stream: bool = False) -> Iterator[str]:
    """
    Асинхронная версия основной функции для получения потока данных из bucket.

    Args:
        bucket_dir (str): Путь к директории bucket.
        delete_files (bool, optional): Если `True`, файлы будут удалены после обработки. По умолчанию `False`.
        refine_chunks_with_spacy (bool, optional): Если `True`, чанки будут обработаны с помощью `spacy`. По умолчанию `False`.
        event_stream (bool, optional): Если `True`, возвращает события о процессе обработки. По умолчанию `False`.

    Yields:
        str: Чанки данных или события о процессе обработки, если `event_stream` установлен в `True`.

    Raises:
        Exception: Если произошла ошибка в процессе обработки.

    Как работает функция:
    1. Функция принимает путь к директории bucket, флаг удаления файлов, флаг обработки с помощью `spacy` и флаг потока событий в качестве аргументов.
    2. Создает директорию bucket, если она не существует.
    3. Асинхронно читает и скачивает URL-адреса из файла `DOWNLOADS_FILE`.
    4. Генерирует чанки данных из файлов в bucket.
    5. Если произошла ошибка в процессе обработки и `event_stream` установлен в `True`, возвращает событие об ошибке.

    Примеры:
    >>> bucket_dir = "/path/to/bucket"
    >>> async for chunk in get_async_streaming(bucket_dir, event_stream=True):
    ...     print(chunk)
    data: {"action": "download", "count": 1}

    data: {"action": "load", "size": 1024}

    data: {"action": "done", "size": 1024}
    """
    ...