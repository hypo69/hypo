### Анализ кода модуля `image`

**Качество кода**:

- **Соответствие стандартам**: 8/10
- **Плюсы**:
    - Код хорошо структурирован, использует асинхронность для операций ввода-вывода.
    - Присутствует обработка ошибок с использованием кастомного исключения `ImageError`.
    - Используется `Path` для работы с путями, что является хорошей практикой.
    - Документация в виде docstring присутствует у всех функций.
- **Минусы**:
    - Некоторые функции используют `try-except` без конкретизации типа исключений, что затрудняет отладку.
    - В функции `add_image_watermark` есть некоторая избыточность в коде, связанная с проверкой режима изображения.
    - Отсутствует проверка на корректность формата изображения при открытии.
    - В блоке `if __name__ == '__main__':` отсутствует обработка возможных исключений при вводе пути.

**Рекомендации по улучшению**:

1. **Уточнить обработку исключений**:
   - Вместо общего `except Exception as ex:` перехватывать конкретные исключения (например, `FileNotFoundError`, `IOError`, `aiohttp.ClientError`).
   - Логировать ошибки с более подробными сообщениями, включая тип исключения.
2. **Улучшить функцию `add_image_watermark`**:
   - Упростить логику конвертации режимов изображения, возможно, с использованием `match-case` (Python 3.10+).
   - Добавить проверку, что изображения имеют корректный формат.
3. **Упростить функцию `add_text_watermark`**:
   - Использовать более гибкую логику для определения размера шрифта.
4.  **Улучшить  `process_images_with_watermark`**:
     - Обработать исключения  `add_image_watermark`.
     - Сделать асинхронный вызов `add_image_watermark`.
5. **Добавить проверки**:
   - Проверять, что формат изображения поддерживается PIL при загрузке и сохранении.
6. **Улучшить форматирование**:
    -  Использовать  `from src.logger.logger import logger`
    - Привести все импорты к одному формату, согласно PEP8.

**Оптимизированный код**:

```python
## \file /src/utils/image.py
# -*- coding: utf-8 -*-

#! venv/bin/python/python3.12

"""
.. module:: src.utils.image
    :platform: Windows, Unix
    :synopsis: Image Processing Utilities

This module provides asynchronous functions for downloading, saving, and manipulating images.
It includes functionalities such as saving images from URLs, saving image data to files,
retrieving image data, finding random images within directories, adding watermarks, resizing,
and converting image formats.
"""

import aiohttp
import aiofiles
import asyncio
import random
from pathlib import Path
from typing import Optional, Union, Tuple

from io import BytesIO
from PIL import Image, ImageDraw, ImageFont

from src.logger.logger import logger # Изменен импорт logger


class ImageError(Exception):
    """Custom exception for image-related errors."""

    pass


async def save_image_from_url(image_url: str, filename: Union[str, Path]) -> Optional[str]:
    """
    Downloads an image from a URL and saves it locally asynchronously.

    :param image_url: The URL to download the image from.
    :type image_url: str
    :param filename: The name of the file to save the image to.
    :type filename: Union[str, Path]
    :return: The path to the saved file, or None if the operation failed.
    :rtype: Optional[str]
    :raises ImageError: If the image download or save operation fails.

    Example:
        >>> url = 'https://www.easygifanimator.net/images/samples/video-to-gif-sample.gif'
        >>> file = Path('test_image_url.gif')
        >>> result = await save_image_from_url(url, file)
        >>> print(result)
        test_image_url.gif
    """
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(image_url) as response:
                response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
                image_data = await response.read()
    except aiohttp.ClientError as ex: # Изменена обработка исключения
        logger.error(f"Error downloading image from {image_url}: {ex}", exc_info=True) # Добавлено сообщение об ошибке
        raise ImageError(f"Failed to download image from {image_url}") from ex

    return await save_image(image_data, filename)


async def save_image(image_data: bytes, file_name: Union[str, Path], format: str = 'PNG') -> Optional[str]:
    """
    Saves image data to a file in the specified format asynchronously.

    :param image_data: The binary image data.
    :type image_data: bytes
    :param file_name: The name of the file to save the image to.
    :type file_name: Union[str, Path]
    :param format: The format to save the image in, default is PNG.
    :type format: str, optional
    :return: The path to the saved file, or None if the operation failed.
    :rtype: Optional[str]
    :raises ImageError: If the file cannot be created, saved, or if the saved file is empty.

    Example:
        >>> import os
        >>> image_data = b'...' # some bytes of image data
        >>> file_path = Path('test_image.png')
        >>> result = await save_image(image_data, file_path)
        >>> print(result)
        test_image.png
        >>> os.remove(file_path)
    """
    file_path = Path(file_name)

    try:
        file_path.parent.mkdir(parents=True, exist_ok=True)  # Create parent directories if they don't exist
        async with aiofiles.open(file_path, "wb") as file:
            await file.write(image_data)

        if not file_path.exists():
            logger.error(f"File {file_path} was not created.")
            raise ImageError(f"File {file_path} was not created.")

        img = Image.open(file_path) # Открываем для проверки формата
        img.save(file_path, format=format) # Сохраняем в нужном формате

        if file_path.stat().st_size == 0:
            logger.error(f"File {file_path} saved, but its size is 0 bytes.")
            raise ImageError(f"File {file_path} saved, but its size is 0 bytes.")

        return str(file_path)

    except (IOError, OSError) as ex: # Изменена обработка исключения
        logger.critical(f"Failed to save file {file_path}: {ex}", exc_info=True) # Добавлено сообщение об ошибке
        raise ImageError(f"Failed to save file {file_path}") from ex


def get_image_bytes(image_path: Path, raw: bool = True) -> Optional[Union[BytesIO, bytes]]:
    """
    Reads an image using Pillow and returns its bytes in JPEG format.

    :param image_path: The path to the image file.
    :type image_path: Path
    :param raw: If True, returns a BytesIO object; otherwise, returns bytes. Defaults to True.
    :type raw: bool, optional
    :return: The bytes of the image in JPEG format, or None if an error occurs.
    :rtype: Optional[Union[BytesIO, bytes]]

    Example:
        >>> from pathlib import Path
        >>> file_path = Path('test_image.jpg')
        >>> with open(file_path, 'wb') as f:
        ...     f.write(b'some image data')
        >>> result = get_image_bytes(file_path)
        >>> print(type(result))
        <class 'io.BytesIO'>
        >>> os.remove(file_path)
    """
    try:
        img = Image.open(image_path)
        img_byte_arr = BytesIO()
        img.save(img_byte_arr, format="JPEG")
        return img_byte_arr if raw else img_byte_arr.getvalue()
    except (IOError, OSError) as ex: # Изменена обработка исключения
        logger.error(f"Error reading image with Pillow: {ex}", exc_info=True) # Добавлено сообщение об ошибке
        return None


def get_raw_image_data(file_name: Union[str, Path]) -> Optional[bytes]:
    """
    Retrieves the raw binary data of a file if it exists.

    :param file_name: The name or path of the file to read.
    :type file_name: Union[str, Path]
    :return: The binary data of the file, or None if the file does not exist or an error occurs.
    :rtype: Optional[bytes]

    Example:
        >>> file_path = Path('test.txt')
        >>> with open(file_path, 'w') as f:
        ...    f.write('test text')
        >>> data = get_raw_image_data(file_path)
        >>> print(data)
        b'test text'
        >>> os.remove(file_path)
    """
    file_path = Path(file_name)

    if not file_path.exists():
        logger.error(f"File {file_path} does not exist.")
        return None

    try:
        return file_path.read_bytes()
    except (IOError, OSError) as ex: # Изменена обработка исключения
        logger.error(f"Error reading file {file_path}: {ex}", exc_info=True)  # Добавлено сообщение об ошибке
        return None


def random_image(root_path: Union[str, Path]) -> Optional[str]:
    """
    Recursively searches for a random image in the specified directory.

    :param root_path: The directory to search for images.
    :type root_path: Union[str, Path]
    :return: The path to a random image, or None if no images are found.
    :rtype: Optional[str]

     Example:
        >>> import os
        >>> os.makedirs('test_dir', exist_ok=True)
        >>> with open('test_dir/test.png', 'wb') as f:
        ...    f.write(b'some image data')
        >>> result = random_image('test_dir')
        >>> print(result)
        test_dir/test.png
        >>> os.remove('test_dir/test.png')
        >>> os.rmdir('test_dir')
    """
    root_path = Path(root_path)
    image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp']
    image_files = [
        file_path
        for file_path in root_path.rglob("*")
        if file_path.is_file() and file_path.suffix.lower() in image_extensions
    ]

    if not image_files:
        logger.warning(f"No images found in {root_path}.")
        return None

    return str(random.choice(image_files))


def add_text_watermark(image_path: Union[str, Path], watermark_text: str, output_path: Optional[Union[str, Path]] = None) -> Optional[str]:
    """
    Adds a text watermark to an image.

    :param image_path: Path to the image file.
    :type image_path: Union[str, Path]
    :param watermark_text: Text to use as the watermark.
    :type watermark_text: str
    :param output_path: Path to save the watermarked image. Defaults to overwriting the original image.
    :type output_path: Optional[Union[str, Path]], optional
    :return: Path to the watermarked image, or None on failure.
    :rtype: Optional[str]

    Example:
        >>> from pathlib import Path
        >>> file_path = Path('test_image.png')
        >>> with open(file_path, 'wb') as f:
        ...    f.write(b'some image data')
        >>> text = 'test_watermark'
        >>> result = add_text_watermark(file_path, text)
        >>> print(result)
        test_image.png
        >>> os.remove(file_path)
    """
    image_path = Path(image_path)
    output_path = image_path if output_path is None else Path(output_path)

    try:
        image = Image.open(image_path).convert("RGBA")

        # Create a transparent layer for the watermark
        watermark_layer = Image.new('RGBA', image.size, (255, 255, 255, 0))
        draw = ImageDraw.Draw(watermark_layer)

        font_size = min(image.size) // 10  # Adjust the font size based on the image
        try:
            font = ImageFont.truetype("arial.ttf", size=font_size)
        except IOError:
            font = ImageFont.load_default(size=font_size)
            logger.warning("Font arial.ttf not found; using default font.")

        text_width, text_height = draw.textsize(watermark_text, font=font)
        x = (image.width - text_width) // 2
        y = (image.height - text_height) // 2

        # Draw text on the transparent layer
        draw.text((x, y), watermark_text, font=font, fill=(255, 255, 255, 128))

        # Combine the image and watermark
        watermarked_image = Image.alpha_composite(image, watermark_layer)
        watermarked_image.save(output_path)

        return str(output_path)

    except (IOError, OSError) as ex: # Изменена обработка исключения
        logger.error(f"Failed to add watermark to {image_path}: {ex}", exc_info=True) # Добавлено сообщение об ошибке
        return None


def add_image_watermark(input_image_path: Path, watermark_image_path: Path, output_image_path: Optional[Path] = None) -> Optional[Path]:
    """
    Adds a watermark to an image and saves the result to the specified output path.

    :param input_image_path: Path to the input image.
    :type input_image_path: Path
    :param watermark_image_path: Path to the watermark image.
    :type watermark_image_path: Path
    :param output_image_path: Path to save the watermarked image. If not provided, the image will be saved in an "output" directory.
    :type output_image_path: Optional[Path], optional
    :return: Path to the saved watermarked image, or None if the operation failed.
    :rtype: Optional[Path]

    Example:
        >>> from pathlib import Path
        >>> base_image = Path('base_image.png')
        >>> watermark_image = Path('watermark_image.png')
        >>> with open(base_image, 'wb') as f:
        ...    f.write(b'some image data')
        >>> with open(watermark_image, 'wb') as f:
        ...    f.write(b'some image data')
        >>> result = add_image_watermark(base_image, watermark_image)
        >>> print(result)
        output/base_image.png
        >>> os.remove(base_image)
        >>> os.remove(watermark_image)
        >>> os.remove(result)
        >>> os.rmdir('output')
    """
    try:
        # Open the base image
        base_image = Image.open(input_image_path)

        # Open the watermark image and convert it to RGBA
        watermark = Image.open(watermark_image_path).convert("RGBA")

        # Set the size of the watermark (8% of the width of the base image)
        position = base_image.size  # Size of the base image (width, height)
        newsize = (int(position[0] * 8 / 100), int(position[0] * 8 / 100))  # New size of the watermark
        watermark = watermark.resize(newsize)  # Resize the watermark

        # Determine the position to place the watermark (bottom-right corner with 20px padding)
        new_position = position[0] - newsize[0] - 20, position[1] - newsize[1] - 20

        # Create a new transparent layer for combining the images
        transparent = Image.new(mode='RGBA', size=position, color=(0, 0, 0, 0))

        # Paste the base image onto the new layer
        transparent.paste(base_image, (0, 0))

        # Paste the watermark on top of the base image
        transparent.paste(watermark, new_position, watermark)

        # Check the image mode and convert the transparent layer to the original mode
        match base_image.mode: # Упрощаем проверку режима
            case 'RGB':
                transparent = transparent.convert('RGB')  # Convert to RGB
            case _:
                transparent = transparent.convert('P')  # Convert to palette

        # Save the final image to the specified output path with optimized quality
        if output_image_path is None:
            output_image_path = input_image_path.parent / "output" / input_image_path.name
        output_image_path.parent.mkdir(parents=True, exist_ok=True)  # Create output directory if it doesn't exist
        transparent.save(output_image_path, optimize=True, quality=100)
        logger.info(f"Saving {output_image_path}...")

        return output_image_path

    except (IOError, OSError) as ex: # Изменена обработка исключения
        logger.error(f"Failed to add watermark to {input_image_path}: {ex}", exc_info=True) # Добавлено сообщение об ошибке
        return None


def resize_image(image_path: Union[str, Path], size: Tuple[int, int], output_path: Optional[Union[str, Path]] = None) -> Optional[str]:
    """
    Resizes an image to the specified dimensions.

    :param image_path: Path to the image file.
    :type image_path: Union[str, Path]
    :param size: A tuple containing the desired width and height of the image.
    :type size: Tuple[int, int]
    :param output_path: Path to save the resized image. Defaults to overwriting the original image.
    :type output_path: Optional[Union[str, Path]], optional
    :return: Path to the resized image, or None on failure.
    :rtype: Optional[str]

    Example:
        >>> from pathlib import Path
        >>> file_path = Path('test_image.png')
        >>> with open(file_path, 'wb') as f:
        ...    f.write(b'some image data')
        >>> new_size = (100, 100)
        >>> result = resize_image(file_path, new_size)
        >>> print(result)
        test_image.png
        >>> os.remove(file_path)
    """
    image_path = Path(image_path)
    output_path = image_path if output_path is None else Path(output_path)

    try:
        img = Image.open(image_path)
        resized_img = img.resize(size)
        resized_img.save(output_path)
        return str(output_path)

    except (IOError, OSError) as ex: # Изменена обработка исключения
        logger.error(f"Failed to resize image {image_path}: {ex}", exc_info=True)  # Добавлено сообщение об ошибке
        return None


def convert_image(image_path: Union[str, Path], format: str, output_path: Optional[Union[str, Path]] = None) -> Optional[str]:
    """
    Converts an image to the specified format.

    :param image_path: Path to the image file.
    :type image_path: Union[str, Path]
    :param format: Format to convert image to (e.g., "JPEG", "PNG").
    :type format: str
    :param output_path: Path to save the converted image. Defaults to overwriting the original image.
    :type output_path: Optional[Union[str, Path]], optional
    :return: Path to the converted image or None on failure.
    :rtype: Optional[str]

     Example:
        >>> from pathlib import Path
        >>> file_path = Path('test_image.png')
        >>> with open(file_path, 'wb') as f:
        ...    f.write(b'some image data')
        >>> new_format = 'JPEG'
        >>> result = convert_image(file_path, new_format)
        >>> print(result)
        test_image.png
        >>> os.remove(file_path)
    """
    image_path = Path(image_path)
    output_path = image_path if output_path is None else Path(output_path)

    try:
        img = Image.open(image_path)
        img.save(output_path, format=format)
        return str(output_path)
    except (IOError, OSError) as ex: # Изменена обработка исключения
        logger.error(f"Failed to convert image {image_path}: {ex}", exc_info=True) # Добавлено сообщение об ошибке
        return None

async def process_images_with_watermark(folder_path: Path, watermark_path: Path) -> None:
    """
    Processes all images in the specified folder by adding a watermark and saving them in an "output" directory.

    :param folder_path: Path to the folder containing images.
    :type folder_path: Path
    :param watermark_path: Path to the watermark image.
    :type watermark_path: Path

    Example:
        >>> import os
        >>> os.makedirs('test_dir', exist_ok=True)
        >>> os.makedirs('watermark_dir', exist_ok=True)
        >>> with open('test_dir/test.png', 'wb') as f:
        ...    f.write(b'some image data')
        >>> with open('watermark_dir/watermark.png', 'wb') as f:
        ...    f.write(b'some image data')
        >>> folder = Path('test_dir')
        >>> watermark = Path('watermark_dir/watermark.png')
        >>> asyncio.run(process_images_with_watermark(folder, watermark))
        >>> os.remove('test_dir/test.png')
        >>> os.remove('watermark_dir/watermark.png')
        >>> os.remove('test_dir/output/test.png')
        >>> os.rmdir('test_dir/output')
        >>> os.rmdir('test_dir')
        >>> os.rmdir('watermark_dir')
    """
    if not folder_path.is_dir():
        logger.error(f"Folder {folder_path} does not exist.")
        return

    # Create an "output" directory if it doesn't exist
    output_dir = folder_path / "output"
    output_dir.mkdir(parents=True, exist_ok=True)

    # Process each file in the folder
    for file_path in folder_path.iterdir():
        if file_path.is_file() and file_path.suffix.lower() in ['.png', '.jpg', '.jpeg']:
            output_image_path = output_dir / file_path.name
            try: # Обрабатываем возможные ошибки добавления ватермарки
                await asyncio.to_thread(add_image_watermark, file_path, watermark_path, output_image_path) # Делаем асинхронный вызов
            except Exception as ex:
                 logger.error(f'Error processing image {file_path}: {ex}', exc_info=True)


# Example usage
if __name__ == "__main__":
    try: # Добавляем обработку ошибок ввода
        folder = Path(input("Enter Folder Path: "))  # Path to the folder containing images
        watermark = Path(input("Enter Watermark Path: "))  # Path to the watermark image
        asyncio.run(process_images_with_watermark(folder, watermark))
    except Exception as ex:
        logger.error(f"Error during script execution: {ex}", exc_info=True)