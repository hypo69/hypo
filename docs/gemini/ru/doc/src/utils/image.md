# Модуль `hypotez/src/utils/image.py`

## Обзор

Модуль `hypotez/src/utils/image.py` предоставляет асинхронные функции для загрузки, сохранения и извлечения данных изображений.  Он поддерживает работу с PNG-изображениями, используя библиотеки `aiohttp`, `aiofiles` и `PIL`.

## Функции

### `save_png_from_url`

**Описание**: Загружает изображение из URL и сохраняет его локально в формате PNG асинхронно.

**Параметры**:
- `image_url` (str): URL изображения для загрузки.
- `filename` (str | Path): Имя файла для сохранения изображения.

**Возвращает**:
- str | None: Путь к сохранённому файлу или `None`, если операция завершилась неудачно.

**Обрабатывает исключения**:
- `Exception`: Возможные исключения при работе с HTTP запросом (например, проблемы с соединением или 404 ошибка).  Подробности логгируются в `logger`.


### `save_png`

**Описание**: Сохраняет изображение в формате PNG асинхронно.

**Параметры**:
- `image_data` (bytes): Бинарные данные изображения.
- `file_name` (str | Path): Имя файла для сохранения.

**Возвращает**:
- str | None: Путь к сохранённому файлу или `None`, если операция завершилась неудачно.

**Обрабатывает исключения**:
- `Exception`: Возможные исключения при работе с файловой системой (например, проблемы с доступом к файлу, проблемы с созданием папок). Подробности логгируются в `logger`.


### `get_image_data`

**Описание**: Извлекает бинарные данные файла, если он существует.

**Параметры**:
- `file_name` (str | Path): Имя файла для чтения.

**Возвращает**:
- bytes | None: Бинарные данные файла, если он существует, или `None`, если файл не найден или произошла ошибка.

**Обрабатывает исключения**:
- `Exception`: Возможные исключения при работе с файловой системой (например, проблемы с доступом к файлу). Подробности логгируются в `logger`.


## Константы

### `MODE`

**Описание**: Текущий режим работы (в примере "dev").


##  Использование

Этот модуль предназначен для использования в асинхронных задачах.  При работе с функциями `save_png_from_url` и `save_png` необходимо использовать `asyncio.run()`.

```python
import asyncio
from hypotez.src.utils.image import save_png_from_url

async def main():
    await save_png_from_url("https://example.com/image.png", "downloaded_image.png")

asyncio.run(main())
```
```python
import asyncio
from hypotez.src.utils.image import save_png

async def main():
  with open("example_image.png", "rb") as f:
    image_data = f.read()
  await save_png(image_data, "saved_image.png")

asyncio.run(main())
```

```python
from hypotez.src.utils.image import get_image_data

image_bytes = get_image_data("path/to/image.png")
if image_bytes:
  print(f"Image data: {image_bytes}")
```
```python
import asyncio
from hypotez.src.utils.image import save_png_from_url

async def main():
    try:
        result = await save_png_from_url("https://invalid-url.com/image.png", "invalid_image.png")
        if result:
            print(f"Image saved to: {result}")
    except Exception as ex:
        print(f"Error: {ex}")


asyncio.run(main())

```
Обратите внимание на использование обработки исключений для надежности кода.  В примере демонстрируется как это сделать.

```python
import asyncio
import logging

async def main():
    # ... (your code)
    try:
        # ... (your code that might raise an exception)
        await save_png_from_url(...)
    except Exception as e:
        logging.exception("An error occurred")  # Use logging!


asyncio.run(main())

```