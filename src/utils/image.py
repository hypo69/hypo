## \file /src/utils/image.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
.. module::  src.utils
    :platform: Windows, Unix
    :synopsis: Image Saving Utilities

This module provides asynchronous functions to download, save, and retrieve image data.

Functions:
    - :func:`save_image_from_url`
    - :func:`save_image`
    - :func:`get_image_data`
    - :func:`random_image`
    - :func:`add_watermark`
    - :func:`resize_image`
    - :func:`convert_image`

.. function:: save_image_from_url(image_url: str, filename: str | Path) -> str | None

    Download an image from a URL and save it locally asynchronously.

    :param image_url: The URL to download the image from.
    :param filename: The name of the file to save the image to.
    :return: The path to the saved file or ``None`` if the operation failed.

    Example:
    >>> asyncio.run(save_image_from_url("https://example.com/image.png", "local_image.png"))
    'local_image.png'

.. function:: save_image(image_data: bytes, file_name: str | Path, format: str='PNG') -> str | None

    Save an image in the specified format asynchronously.

    :param image_data: The binary image data.
    :param file_name: The name of the file to save the image to.
    :param format: The format to save the image in, default is PNG
    :return: The path to the saved file or ``None`` if the operation failed.

    Example:
    >>> with open("example_image.png", "rb") as f:
    ...     image_data = f.read()
    >>> asyncio.run(save_image(image_data, "saved_image.png"))
    'saved_image.png'

.. function:: get_image_data(file_name: str | Path) -> bytes | None

    Retrieve binary data of a file if it exists.

    :param file_name: The name of the file to read.
    :return: The binary data of the file if it exists, or ``None`` if the file is not found or an error occurred.

    Example:
    >>> get_image_data("saved_image.png")
    b'\x89PNG\r\n...'

.. function:: random_image(root_path: str | Path) -> str | None

    Recursively search for a random image in the specified directory and return its path.

    :param root_path: The directory to search for images.
    :return: The path to a random image or ``None`` if no images are found.

    Example:
    >>> random_image("path/to/images")
    'path/to/images/subfolder/random_image.png'
    
.. function:: add_watermark(image_path: str | Path, watermark_text: str, output_path: str | Path=None) -> str | None

    Adds a text watermark to an image.
    
    :param image_path: Path to the image file.
    :param watermark_text: Text to use as the watermark.
    :param output_path: Path to save the watermarked image, defaults to original image.
    :return: Path to the watermarked image or None on failure
    
.. function:: resize_image(image_path: str | Path, size: tuple[int, int], output_path: str | Path=None) -> str | None
    
    Resizes an image to specified dimensions.
    
    :param image_path: Path to the image file.
    :param size: A tuple containing the desired width and height of the image.
    :param output_path: Path to save the resized image, defaults to original image.
    :return: Path to the resized image or None on failure

.. function:: convert_image(image_path: str | Path, format: str, output_path: str | Path=None) -> str | None
    
    Converts an image to the specified format.
    
    :param image_path: Path to the image file.
    :param format: Format to convert image to (e.g., "JPEG", "PNG").
    :param output_path: Path to save the converted image, defaults to original image.
    :return: Path to the converted image or None on failure
"""


import aiohttp
import aiofiles
from PIL import Image, ImageDraw, ImageFont
from pathlib import Path
import asyncio
import random
from pathlib import Path
from PIL import Image
from io import BytesIO
from src.logger.logger import logger
from src.utils.printer import pprint


class ImageError(Exception):
    """Custom exception for image related errors."""
    pass


async def save_image_from_url(
    image_url: str, filename: str | Path
) -> str | None:
    """Download an image from a URL and save it locally asynchronously."""
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(image_url) as response:
                response.raise_for_status()
                image_data = await response.read()
    except Exception as ex:
        logger.error(f"Error downloading image from {image_url}", exc_info=True)
        raise ImageError(f"Failed to download image from {image_url}") from ex

    return await save_image(image_data, filename)


async def save_image(image_data: bytes, file_name: str | Path, format: str = 'PNG') -> str | None:
    """Save an image in the specified format asynchronously."""
    file_path = Path(file_name)

    try:
        file_path.parent.mkdir(parents=True, exist_ok=True)
        async with aiofiles.open(file_path, "wb") as file:
            await file.write(image_data)

        if not file_path.exists():
            logger.error(f"File {file_path} was not created.")
            raise ImageError(f"File {file_path} was not created.")
        
        img = Image.open(file_path)
        img.save(file_path, format=format)
        
        if file_path.stat().st_size == 0:
            logger.error(f"File {file_path} saved, but its size is 0 bytes.")
            raise ImageError(f"File {file_path} saved, but its size is 0 bytes.")
            
        return str(file_path)


    except Exception as ex:
        logger.critical(f"Failed to save file {file_path}", exc_info=True)
        raise ImageError(f"Failed to save file {file_path}") from ex


def get_image_bytes(image_path: Path, raw:bool = True) -> bytes | None:
    """
    Читает изображение с помощью Pillow и возвращает его как байты JPEG.

    Args:
        image_path: Путь к файлу изображения.

    Returns:
            bytes: Байты изображения в формате JPEG.
            None: Если произошла ошибка.
    """
    try:
        img = Image.open(image_path)
        img_byte_arr = BytesIO()
        img.save(img_byte_arr, format="JPEG")
        return img_byte_arr if raw else img_byte_arr.getvalue()
    except Exception as ex:
        logger.error(f"Ошибка чтения изображения с Pillow:", ex)
        return None

def get_image_data(file_name: str | Path) -> bytes | None:
    """Retrieve binary data of a file if it exists."""
    file_path = Path(file_name)

    if not file_path.exists():
        logger.error(f"File {file_path} does not exist.")
        return None

    try:
        return file_path.read_bytes()
    except Exception as ex:
        logger.error(f"Error reading file {file_path}", exc_info=True)
        return None


def random_image(root_path: str | Path) -> str | None:
    """Recursively search for a random image in the specified directory and return its path."""
    root_path = Path(root_path)
    image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp']
    image_files = []

    for file_path in root_path.rglob("*"):
        if file_path.is_file() and file_path.suffix.lower() in image_extensions:
            image_files.append(file_path)

    if not image_files:
        logger.warning(f"No images found in {root_path}.")
        return None

    return str(random.choice(image_files))


def add_watermark(image_path: str | Path, watermark_text: str, output_path: str | Path=None) -> str | None:
    """Adds a text watermark to an image."""
    image_path = Path(image_path)
    if output_path is None:
        output_path = image_path
    else:
        output_path = Path(output_path)

    try:
        image = Image.open(image_path).convert("RGBA")
        
        # Create a transparent layer for the watermark
        watermark_layer = Image.new('RGBA', image.size, (255, 255, 255, 0))
        draw = ImageDraw.Draw(watermark_layer)
        
        font_size = min(image.size) // 10  # Adjust the font size based on the image
        font = ImageFont.truetype("arial.ttf", size=font_size)
        
        text_width, text_height = draw.textsize(watermark_text, font=font)
        
        x = (image.width - text_width) // 2
        y = (image.height - text_height) // 2

        # Draw text on the transparent layer
        draw.text((x, y), watermark_text, font=font, fill=(255, 255, 255, 128))

        # Combine the image and watermark
        watermarked_image = Image.alpha_composite(image, watermark_layer)
        watermarked_image.save(output_path)

        return str(output_path)

    except Exception as ex:
         logger.error(f"Failed to add watermark to {image_path}", exc_info=True)
         return None

def resize_image(image_path: str | Path, size: tuple[int, int], output_path: str | Path=None) -> str | None:
    """Resizes an image to specified dimensions."""
    image_path = Path(image_path)

    if output_path is None:
        output_path = image_path
    else:
        output_path = Path(output_path)

    try:
        img = Image.open(image_path)
        resized_img = img.resize(size)
        resized_img.save(output_path)
        return str(output_path)

    except Exception as ex:
        logger.error(f"Failed to resize image {image_path}", exc_info=True)
        return None

def convert_image(image_path: str | Path, format: str, output_path: str | Path=None) -> str | None:
    """Converts an image to the specified format."""
    image_path = Path(image_path)

    if output_path is None:
        output_path = image_path
    else:
        output_path = Path(output_path)

    try:
        img = Image.open(image_path)
        img.save(output_path, format=format)
        return str(output_path)
    except Exception as ex:
        logger.error(f"Failed to convert image {image_path}", exc_info=True)
        return None