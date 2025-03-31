# Модуль `src.utils.video`

## Обзор

Модуль `src.utils.video` предоставляет асинхронные функции для загрузки и сохранения видеофайлов, а также для получения видеоданных. Включает обработку ошибок и логирование для обеспечения надежной работы.

## Подробней

Этот модуль предназначен для асинхронной загрузки видеофайлов из сети и сохранения их локально. Он также предоставляет возможность чтения данных видеофайлов. Модуль использует библиотеки `aiohttp` для асинхронных HTTP-запросов и `aiofiles` для асинхронной работы с файлами. Логирование осуществляется с помощью модуля `logger` из `src.logger.logger`.

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
    ...
```

**Описание**: Асинхронно загружает видео по URL и сохраняет его локально.

**Как работает функция**:

1.  Принимает URL видео и путь для сохранения.
2.  Использует `aiohttp.ClientSession` для выполнения асинхронного HTTP-запроса к указанному URL.
3.  Проверяет статус ответа на наличие HTTP-ошибок.
4.  Создает родительские директории для файла, если они не существуют.
5.  Асинхронно открывает файл для записи (`aiofiles.open`).
6.  Читает содержимое ответа чанками (по 8192 байт) и записывает их в файл.
7.  После завершения загрузки проверяет, был ли файл успешно сохранен и не является ли он пустым.
8.  В случае ошибок логирует их и возвращает `None`.

**Параметры**:

*   `url` (str): URL-адрес видео для загрузки.
*   `save_path` (str): Путь для сохранения загруженного видео.

**Возвращает**:

*   `Optional[Path]`: Путь к сохраненному файлу, если операция выполнена успешно, иначе `None`.

**Вызывает исключения**:

*   `aiohttp.ClientError`: При сетевых проблемах во время загрузки.

**Примеры**:

```python
import asyncio
from pathlib import Path

# Пример асинхронного вызова функции
async def main():
    url = "https://example.com/video.mp4"  # Замените на реальный URL
    save_path = "local_video.mp4"
    result = await save_video_from_url(url, save_path)
    if result:
        print(f"Видео сохранено в {result}")
    else:
        print("Не удалось сохранить видео.")

if __name__ == "__main__":
    asyncio.run(main())

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
    ...
```

**Описание**: Извлекает двоичные данные видеофайла, если он существует.

**Как работает функция**:

1.  Принимает имя файла видео.
2.  Проверяет, существует ли файл по указанному пути.
3.  Если файл не найден, логирует ошибку и возвращает `None`.
4.  Если файл существует, открывает его в режиме чтения двоичных данных (`"rb"`).
5.  Читает все содержимое файла и возвращает его в виде байтовой строки.
6.  В случае ошибки при чтении файла логирует ее и возвращает `None`.

**Параметры**:

*   `file_name` (str): Путь к видеофайлу для чтения.

**Возвращает**:

*   `Optional[bytes]`: Двоичные данные файла, если он существует, иначе `None`.

**Вызывает исключения**:

*   Не вызывает исключений, но логирует ошибки при отсутствии файла или ошибках чтения.

**Примеры**:

```python
# Пример использования функции для чтения данных видеофайла
video_data = get_video_data("local_video.mp4")
if video_data:
    print(f"Размер видео: {len(video_data)} байт")
else:
    print("Не удалось получить данные видео.")
```

### `main`

```python
def main():
    url = "https://example.com/video.mp4"  # Replace with a valid URL!
    save_path = "local_video.mp4"
    result = asyncio.run(save_video_from_url(url, save_path))
    if result:
        print(f"Video saved to {result}")
```

**Описание**: Главная функция для демонстрации работы модуля.

**Как работает функция**:

1.  Определяет URL видео и путь для сохранения.
2.  Вызывает `save_video_from_url` для загрузки и сохранения видео.
3.  Выводит сообщение об успехе или неудаче операции.

**Параметры**:

*   Нет

**Возвращает**:

*   Нет

**Вызывает исключения**:

*   Нет

**Примеры**:

```python
# Пример вызова главной функции
if __name__ == "__main__":
    main()