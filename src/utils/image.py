## \file hypotez/src/utils/image.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
.. module::  src.utils
    :platform: Windows, Unix
    :synopsis: Image Saving Utilities

This module provides asynchronous functions to download, save, and retrieve image data.

Functions:
    - :func:`save_png_from_url`
    - :func:`save_png`
    - :func:`get_image_data`

.. function:: save_png_from_url(image_url: str, filename: str | Path) -> str | None

    Download an image from a URL and save it locally asynchronously.

    :param image_url: The URL to download the image from.
    :param filename: The name of the file to save the image to.
    :return: The path to the saved file or ``None`` if the operation failed.

    Example:
    >>> asyncio.run(save_png_from_url("https://example.com/image.png", "local_image.png"))
    'local_image.png'

.. function:: save_png(image_data: bytes, file_name: str | Path) -> str | None

    Save an image in PNG format asynchronously.

    :param image_data: The binary image data.
    :param file_name: The name of the file to save the image to.
    :return: The path to the saved file or ``None`` if the operation failed.

    Example:
    >>> with open("example_image.png", "rb") as f:
    ...     image_data = f.read()
    >>> asyncio.run(save_png(image_data, "saved_image.png"))
    'saved_image.png'

.. function:: get_image_data(file_name: str | Path) -> bytes | None

    Retrieve binary data of a file if it exists.

    :param file_name: The name of the file to read.
    :return: The binary data of the file if it exists, or ``None`` if the file is not found or an error occurred.

    Example:
    >>> get_image_data("saved_image.png")
    b'\x89PNG\r\n...'
"""
MODE = 'dev'
import aiohttp
import aiofiles
from PIL import Image
from pathlib import Path
import asyncio
from src.logger.logger import logger
from src.utils.printer import pprint


async def save_png_from_url(
    image_url: str, filename: str | Path
) -> str | None:
    """Download an image from a URL and save it locally asynchronously.

    :param image_url: The URL to download the image from.
    :param filename: The name of the file to save the image to.
    :return: The path to the saved file or ``None`` if the operation failed.

    :example:
        >>> asyncio.run(save_png_from_url("https://example.com/image.png", "local_image.png"))
        'local_image.png'
    """
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(image_url) as response:
                response.raise_for_status()
                image_data = await response.read()
    except Exception as ex:
        logger.error("Error downloading image", ex, exc_info=True)
        return 

    return await save_png(image_data, filename)


async def save_png(image_data: bytes, file_name: str | Path) -> str | None:
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
    file_path = Path(file_name)

    try:
        # Create necessary directories
        file_path.parent.mkdir(parents=True, exist_ok=True)

        # Write file
        async with aiofiles.open(file_path, "wb") as file:
            await file.write(image_data)

        # Verify file creation
        if not file_path.exists():
            logger.error(f"File {file_path} was not created.")
            return

        # Open and save the image
        image = Image.open(file_path)
        image.save(file_path, "PNG")

        # Verify file size
        if file_path.stat().st_size == 0:
            logger.error(f"File {file_path} saved, but its size is 0 bytes.")
            return

    except Exception as ex:
        logger.critical(f"Failed to save file {file_path}", ex, exc_info=True)
        return

    return str(file_path)


def get_image_data(file_name: str | Path) -> bytes | None:
    """Retrieve binary data of a file if it exists.

    :param file_name: The name of the file to read.
    :return: The binary data of the file if it exists, or ``None`` if the file is not found or an error occurred.

    :example:
        >>> get_image_data("saved_image.png")
        b'\x89PNG\r\n...'
    """
    file_path = Path(file_name)

    if not file_path.exists():
        logger.error(f"File {file_path} does not exist.")
        return

    try:
        with open(file_path, "rb") as file:
            return file.read()
    except Exception as ex:
        logger.error(f"Error reading file {file_path}", ex, exc_info=True)
        return
