# Модуль `src.utils.video`

## Обзор

Модуль `src.utils.video` предоставляет асинхронные функции для загрузки и сохранения видеофайлов, а также для получения видеоданных. Он включает в себя обработку ошибок и ведение журнала для обеспечения надежной работы.

## Подробней

Этот модуль предназначен для работы с видеофайлами, позволяя загружать их по URL и сохранять локально, а также считывать данные из локальных видеофайлов. Он использует асинхронный подход для неблокирующих операций, что особенно важно для сетевых запросов и операций ввода-вывода.

## Функции

### `save_video_from_url`

```python
async def save_video_from_url(url: str, save_path: str) -> Optional[Path]:
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

**Назначение**: Загружает видео по URL и асинхронно сохраняет его локально.

**Как работает функция**:

1.  Принимает URL видео и путь для сохранения.
2.  Использует `aiohttp` для выполнения асинхронного HTTP-запроса к URL.
3.  Проверяет статус ответа HTTP на наличие ошибок.
4.  Создает родительские каталоги, если они не существуют.
5.  Асинхронно записывает содержимое видео в файл по частям (chunk).
6.  После сохранения проверяет, был ли файл успешно сохранен и не является ли он пустым.
7.  Возвращает путь к сохраненному файлу или `None` в случае ошибки.

**Параметры**:

*   `url` (str): URL-адрес, с которого скачивается видео.
*   `save_path` (str): Путь для сохранения скачанного видео.

**Возвращает**:

*   `Optional[Path]`: Путь к сохраненному файлу или `None`, если операция не удалась. Возвращает `None` при ошибках и если размер файла равен 0 байт.

**Вызывает исключения**:

*   `aiohttp.ClientError`: Возникает при сетевых проблемах во время загрузки.

**Примеры**:

```python
import asyncio
async def main():
    url = "https://example.com/video.mp4"  # Замените на действительный URL!
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

**Назначение**: Извлекает двоичные данные видеофайла, если он существует.

**Как работает функция**:

1.  Принимает имя файла видео для чтения.
2.  Проверяет, существует ли файл по указанному пути.
3.  Открывает файл в двоичном режиме для чтения.
4.  Считывает все содержимое файла в виде байтов.
5.  Возвращает двоичные данные файла или `None`, если файл не найден или произошла ошибка.

**Параметры**:

*   `file_name` (str): Путь к видеофайлу для чтения.

**Возвращает**:

*   `Optional[bytes]`: Двоичные данные файла, если он существует, или `None`, если файл не найден или произошла ошибка.

**Примеры**:

```python
data = get_video_data("local_video.mp4")
if data:
    print(data[:10])  # Вывод первых 10 байт для проверки
else:
    print("Не удалось получить данные видео.")
```