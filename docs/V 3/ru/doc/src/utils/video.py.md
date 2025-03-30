# Модуль `src.utils.video`

## Обзор

Модуль `src.utils.video` предоставляет асинхронные функции для скачивания и сохранения видеофайлов, а также для извлечения видеоданных. Он включает обработку ошибок и ведение журнала для обеспечения надежной работы.

## Подробней

Этот модуль предоставляет асинхронные функции для загрузки и сохранения видеофайлов, а также для получения видеоданных. Он включает в себя обработку ошибок и ведение журнала для обеспечения надежной работы. Модуль содержит функции для асинхронной загрузки и сохранения видео с использованием URL-адреса, а также для получения двоичных данных из локального видеофайла. Он использует `aiohttp` для асинхронных HTTP-запросов и `aiofiles` для асинхронных файловых операций, что позволяет эффективно выполнять операции ввода-вывода, не блокируя основной поток. Логирование реализовано через модуль `src.logger.logger`.

## Функции

### `save_video_from_url`

```python
async def save_video_from_url(
    url: str,
    save_path: str
) -> Optional[Path]:
    """Download a video from a URL and save it locally asynchronously.

    Args:
        url (str): The URL from which to download the video.
        save_path (str): The path to save the downloaded video.

    Returns:
        Optional[Path]: The path to the saved file, or `None` if the operation failed.  Returns None on errors and if file is 0 bytes.

    Raises:
        aiohttp.ClientError: on network issues during the download.
    """
```

**Описание**: Асинхронно загружает видео по URL-адресу и сохраняет его локально.

**Параметры**:
- `url` (str): URL-адрес, с которого скачивается видео.
- `save_path` (str): Путь для сохранения скачанного видео.

**Возвращает**:
- `Optional[Path]`: Путь к сохраненному файлу или `None`, если операция не удалась. Возвращает `None` в случае ошибок и если размер файла равен 0 байт.

**Вызывает исключения**:
- `aiohttp.ClientError`: При сетевых проблемах во время загрузки.

**Примеры**:

```python
    >>> import asyncio
    >>> asyncio.run(save_video_from_url("https://example.com/video.mp4", "local_video.mp4"))
    PosixPath('local_video.mp4')  # или None, если не удалось
```

### `get_video_data`

```python
def get_video_data(file_name: str) -> Optional[bytes]:
    """Retrieve binary data of a video file if it exists.

    Args:
        file_name (str): The path to the video file to read.

    Returns:
        Optional[bytes]: The binary data of the file if it exists, or `None` if the file is not found or an error occurred.
    """
```

**Описание**: Извлекает двоичные данные видеофайла, если он существует.

**Параметры**:
- `file_name` (str): Путь к видеофайлу для чтения.

**Возвращает**:
- `Optional[bytes]`: Двоичные данные файла, если он существует, или `None`, если файл не найден или произошла ошибка.

**Примеры**:

```python
    >>> data = get_video_data("local_video.mp4")
    >>> if data:
    ...     print(data[:10])  # Print first 10 bytes to check
    b'\x00\x00\x00...'
```