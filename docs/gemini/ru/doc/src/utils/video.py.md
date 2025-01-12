# Модуль `video.py`

## Обзор

Модуль `video.py` предоставляет асинхронные функции для загрузки и сохранения видеофайлов, а также получения данных видео. Он включает в себя обработку ошибок и журналирование для надежной работы.

## Содержание

- [Функции](#функции)
    - [`save_video_from_url`](#save_video_from_url)
    - [`get_video_data`](#get_video_data)
- [Пример использования](#пример-использования)

## Функции

### `save_video_from_url`

**Описание**: Загружает видео из URL-адреса и асинхронно сохраняет его локально.

**Параметры**:
- `url` (str): URL-адрес, с которого нужно загрузить видео.
- `save_path` (str): Путь для сохранения загруженного видео.

**Возвращает**:
- `Optional[Path]`: Путь к сохраненному файлу или `None`, если операция не удалась. Возвращает `None` при ошибках и если размер файла равен 0 байт.

**Вызывает исключения**:
- `aiohttp.ClientError`: при сетевых проблемах во время загрузки.

### `get_video_data`

**Описание**: Получает бинарные данные видеофайла, если он существует.

**Параметры**:
- `file_name` (str): Путь к видеофайлу для чтения.

**Возвращает**:
- `Optional[bytes]`: Бинарные данные файла, если он существует, или `None`, если файл не найден или произошла ошибка.

## Пример использования

```python
import asyncio
from pathlib import Path
from src.utils.video import save_video_from_url, get_video_data

async def main():
    # Пример использования save_video_from_url
    url = "https://example.com/video.mp4" # Замените на валидный URL
    save_path = "local_video.mp4"
    saved_path = await save_video_from_url(url, save_path)
    if saved_path:
        print(f"Видео сохранено по пути: {saved_path}")
    else:
        print("Не удалось сохранить видео.")
    
    # Пример использования get_video_data
    if saved_path:
        video_data = get_video_data(str(saved_path))
        if video_data:
            print(f"Первые 10 байт видео: {video_data[:10]}")
        else:
            print("Не удалось получить данные видео.")

if __name__ == "__main__":
    asyncio.run(main())
```