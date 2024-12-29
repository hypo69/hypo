# Модуль `src.utils.video`

## Обзор

Модуль `src.utils.video` предоставляет асинхронные функции для загрузки и сохранения видеофайлов, а также для извлечения видеоданных. Он включает обработку ошибок и логирование для обеспечения надежной работы.

## Оглавление

- [Обзор](#обзор)
- [Функции](#функции)
    - [`save_video_from_url`](#save_video_from_url)
    - [`get_video_data`](#get_video_data)
- [Пример использования](#пример-использования)

## Функции

### `save_video_from_url`

**Описание**:
Асинхронно загружает видео с URL-адреса и сохраняет его локально.

**Параметры**:
- `url` (str): URL-адрес для загрузки видео.
- `save_path` (str): Путь для сохранения загруженного видео.

**Возвращает**:
- `Optional[Path]`: Путь к сохраненному файлу или `None`, если операция не удалась. Возвращает `None` при ошибках и если файл имеет размер 0 байт.

**Вызывает исключения**:
- `aiohttp.ClientError`: При сетевых проблемах во время загрузки.

### `get_video_data`

**Описание**:
Извлекает бинарные данные видеофайла, если он существует.

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
    url = "https://example.com/video.mp4"  # Замените на действительный URL
    save_path = "local_video.mp4"

    saved_path = await save_video_from_url(url, save_path)
    if saved_path:
        print(f"Видео сохранено по пути: {saved_path}")

        # Пример использования get_video_data
        video_data = get_video_data(str(saved_path))
        if video_data:
            print(f"Первые 10 байт видео: {video_data[:10]}")
        else:
            print("Не удалось получить данные видео")
    else:
        print("Не удалось сохранить видео")


if __name__ == "__main__":
    asyncio.run(main())

```