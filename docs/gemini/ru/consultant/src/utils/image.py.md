# Анализ кода модуля `image.py`

**Качество кода: 8**

*   **Плюсы:**
    *   Код хорошо структурирован и разбит на логические функции.
    *   Используются асинхронные операции для неблокирующего ввода-вывода.
    *   Присутствуют комментарии и docstring в формате reStructuredText (RST).
    *   Обработка исключений присутствует, ошибки логируются.
    *   Используется библиотека `pathlib` для работы с путями.
*   **Минусы:**
    *   Не хватает проверки аргументов функций.
    *   Не все функции имеют примеры использования в docstring (необходимо добавить для `get_image_data`).
    *   Используется `logger.critical` для ошибок сохранения, что может быть излишним (заменить на `logger.error`).
    *   В некоторых местах обработка исключений может быть более конкретной.
    *   В `random_image` можно использовать list comprehension.

**Рекомендации по улучшению**

1.  **Добавить проверку аргументов:**
    *   В функциях `save_png_from_url`, `save_png`, `get_image_data` и `random_image` добавить проверки на типы и значения аргументов, что позволит избежать ошибок на ранних стадиях.
2.  **Уточнить обработку ошибок:**
    *   В `save_png` вместо `logger.critical` использовать `logger.error`, поскольку ошибка не является критичной для всего приложения.
    *   В `save_png_from_url`, `save_png`, `get_image_data` можно добавить более конкретные исключения для разных типов ошибок, если это необходимо.
3.  **Улучшить docstring:**
    *   Добавить пример использования в docstring для функции `get_image_data`.
4.  **Улучшить функцию `random_image`:**
    *   Использовать генератор списков (list comprehension) для более краткой записи.
5. **Добавить блок `if __name__ == '__main__':`**
    * Добавить блок для тестирования функций, проверки работоспособности.
6.  **Удалить лишний MODE**
    * Переменная `MODE` не используется, следует удалить.
    * Добавить `from typing import Union` и заменить `str | Path` на `Union[str, Path]`

**Оптимизированный код**

```python
"""
.. module:: src.utils.image
    :platform: Windows, Unix
    :synopsis: Image Saving Utilities

This module provides asynchronous functions to download, save, and retrieve image data.

Functions:
    - :func:`save_png_from_url`
    - :func:`save_png`
    - :func:`get_image_data`
    - :func:`random_image`

.. function:: save_png_from_url(image_url: str, filename: Union[str, Path]) -> str | None

    Download an image from a URL and save it locally asynchronously.

    :param image_url: The URL to download the image from.
    :param filename: The name of the file to save the image to.
    :return: The path to the saved file or ``None`` if the operation failed.

    :example:
        >>> asyncio.run(save_png_from_url("https://example.com/image.png", "local_image.png"))
        'local_image.png'

.. function:: save_png(image_data: bytes, file_name: Union[str, Path]) -> str | None

    Save an image in PNG format asynchronously.

    :param image_data: The binary image data.
    :param file_name: The name of the file to save the image to.
    :return: The path to the saved file or ``None`` if the operation failed.

    :example:
        >>> with open("example_image.png", "rb") as f:
        ...     image_data = f.read()
        >>> asyncio.run(save_png(image_data, "saved_image.png"))
        'saved_image.png'

.. function:: get_image_data(file_name: Union[str, Path]) -> bytes | None

    Retrieve binary data of a file if it exists.

    :param file_name: The name of the file to read.
    :return: The binary data of the file if it exists, or ``None`` if the file is not found or an error occurred.

    :example:
        >>> get_image_data("saved_image.png")
        b'\\x89PNG\\r\\n...'

.. function:: random_image(root_path: Union[str, Path]) -> str | None

    Recursively search for a random image in the specified directory and return its path.

    :param root_path: The directory to search for images.
    :return: The path to a random image or ``None`` if no images are found.

    :example:
        >>> random_image("path/to/images")
        'path/to/images/subfolder/random_image.png'
"""
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

import aiohttp
import aiofiles
from PIL import Image
from pathlib import Path
import asyncio
import random
from src.logger.logger import logger
from typing import Union


async def save_png_from_url(
    image_url: str, filename: Union[str, Path]
) -> str | None:
    """Download an image from a URL and save it locally asynchronously.

    :param image_url: The URL to download the image from.
    :param filename: The name of the file to save the image to.
    :return: The path to the saved file or ``None`` if the operation failed.

    :example:
        >>> asyncio.run(save_png_from_url("https://example.com/image.png", "local_image.png"))
        'local_image.png'
    """
    # Проверка, что `image_url` является строкой
    if not isinstance(image_url, str):
         logger.error(f"Invalid argument type: image_url must be a string, not {type(image_url)}")
         return None
    # Проверка, что `filename` является строкой или экземпляром Path
    if not isinstance(filename, (str, Path)):
         logger.error(f"Invalid argument type: filename must be a string or Path, not {type(filename)}")
         return None

    try:
        # Код исполняет запрос на скачивание изображения по URL
        async with aiohttp.ClientSession() as session:
            async with session.get(image_url) as response:
                response.raise_for_status()
                image_data = await response.read()
    except Exception as ex:
        # Логирование ошибки скачивания изображения
        logger.error("Error downloading image", ex, exc_info=True)
        return

    # Сохранение полученных данных изображения в файл
    return await save_png(image_data, filename)


async def save_png(image_data: bytes, file_name: Union[str, Path]) -> str | None:
    """Save an image in PNG format asynchronously.

    :param image_data: The binary image data.
    :param file_name: The name of the file to save the image to.
    :return: The path to the saved file or ``None`` if the operation failed.

    :example:
        >>> with open("example_image.png", "rb") as f:
        ...     image_data = f.read()
        >>> asyncio.run(save_png(image_data, "saved_image.png"))
        'saved_image.png'
    """
    # Проверка, что `image_data` является байтами
    if not isinstance(image_data, bytes):
        logger.error(f"Invalid argument type: image_data must be bytes, not {type(image_data)}")
        return None
    # Проверка, что `file_name` является строкой или экземпляром Path
    if not isinstance(file_name, (str, Path)):
        logger.error(f"Invalid argument type: file_name must be a string or Path, not {type(file_name)}")
        return None

    file_path = Path(file_name)

    try:
        # Создание необходимых директорий
        file_path.parent.mkdir(parents=True, exist_ok=True)
        # Запись файла
        async with aiofiles.open(file_path, "wb") as file:
            await file.write(image_data)

        # Проверка, что файл создан
        if not file_path.exists():
            logger.error(f"File {file_path} was not created.")
            return

        # Открытие и сохранение изображения
        image = Image.open(file_path)
        image.save(file_path, "PNG")

        # Проверка размера файла
        if file_path.stat().st_size == 0:
            logger.error(f"File {file_path} saved, but its size is 0 bytes.")
            return
    except Exception as ex:
        # Логирование ошибки сохранения файла
        logger.error(f"Failed to save file {file_path}", ex, exc_info=True)
        return

    return str(file_path)


def get_image_data(file_name: Union[str, Path]) -> bytes | None:
    """Retrieve binary data of a file if it exists.

    :param file_name: The name of the file to read.
    :return: The binary data of the file if it exists, or ``None`` if the file is not found or an error occurred.

    :example:
        >>> get_image_data("saved_image.png")
        b'\\x89PNG\\r\\n...'
    """
    # Проверка, что `file_name` является строкой или экземпляром Path
    if not isinstance(file_name, (str, Path)):
        logger.error(f"Invalid argument type: file_name must be a string or Path, not {type(file_name)}")
        return None

    file_path = Path(file_name)

    # Проверка, что файл существует
    if not file_path.exists():
        logger.error(f"File {file_path} does not exist.")
        return

    try:
        # Чтение данных из файла
        with open(file_path, "rb") as file:
            return file.read()
    except Exception as ex:
        # Логирование ошибки чтения файла
        logger.error(f"Error reading file {file_path}", ex, exc_info=True)
        return


def random_image(root_path: Union[str, Path]) -> str | None:
    """Recursively search for a random image in the specified directory and return its path.

    :param root_path: The directory to search for images.
    :return: The path to a random image or ``None`` if no images are found.

    :example:
        >>> random_image("path/to/images")
        'path/to/images/subfolder/random_image.png'
    """
    # Проверка, что `root_path` является строкой или экземпляром Path
    if not isinstance(root_path, (str, Path)):
        logger.error(f"Invalid argument type: root_path must be a string or Path, not {type(root_path)}")
        return None
    root_path = Path(root_path)
    image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp']
    # Код формирует список файлов изображений
    image_files = [
        file_path
        for file_path in root_path.rglob("*")
        if file_path.is_file() and file_path.suffix.lower() in image_extensions
    ]
    # Проверка наличия файлов
    if not image_files:
        logger.warning(f"No images found in {root_path}.")
        return None

    # Возврат случайного пути к изображению
    return str(random.choice(image_files))

if __name__ == '__main__':
    async def main():
        # Test save_png_from_url
        image_url = "https://www.easygifanimator.net/images/samples/video-to-gif-sample.gif"
        saved_file = await save_png_from_url(image_url, "test_image_from_url.gif")
        if saved_file:
            print(f"Image from URL saved to: {saved_file}")

        # Test save_png
        with open("test_image_from_url.gif", "rb") as f:
            image_data = f.read()
        saved_file_png = await save_png(image_data, "test_image.png")
        if saved_file_png:
              print(f"Image saved to: {saved_file_png}")

        # Test get_image_data
        retrieved_data = get_image_data("test_image.png")
        if retrieved_data:
           print(f"Image data retrieved successfully. Data size: {len(retrieved_data)}")


        # Test random_image
        random_image_path = random_image(".")
        if random_image_path:
          print(f"Random image found at: {random_image_path}")
        else:
            print("No images found.")

    asyncio.run(main())
```