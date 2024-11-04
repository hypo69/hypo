## \file src/utils/image.py
# -*- coding: utf-8 -*-
#! /path/to/interpreter/python
"""
Image Saving Utilities.

This module provides asynchronous functions to download, save, and retrieve image data.

Functions:
    save_png_from_url(image_url: str, filename: str | Path) -> str | None:
        Download an image from a URL and save it locally asynchronously.

    save_png(image_data: bytes, file_name: str | Path) -> str | None:
        Save an image in PNG format asynchronously.

    get_image_data(file_name: str | Path) -> bytes | None:
        Retrieve binary data of a file if it exists.

Examples:
    >>> asyncio.run(save_png_from_url("https://example.com/image.png", "local_image.png"))
    'local_image.png'

    >>> with open("example_image.png", "rb") as f:
    ...     image_data = f.read()
    >>> asyncio.run(save_png(image_data, "saved_image.png"))
    'saved_image.png'

    >>> get_image_data("saved_image.png")
    b'\x89PNG\r\n...'
"""

import aiohttp
import aiofiles
from PIL import Image
from pathlib import Path
import asyncio
from src.logger import logger
from src.utils.printer import pprint


async def save_png_from_url(
    image_url: str, filename: str | Path
) -> str | None:
    """Download an image from a URL and save it locally asynchronously.

    Args:
        image_url (str): The URL to download the image from.
        filename (str | Path): The name of the file to save the image to.

    Returns:
        str | None: The path to the saved file or `None` if the operation failed.

    Example:
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

    Args:
        image_data (bytes): The binary image data.
        file_name (str | Path): The name of the file to save the image to.

    Returns:
        str | None: The path to the saved file or `None` if the operation failed.

    Example:
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

    Args:
        file_name (str | Path): The name of the file to read.

    Returns:
        bytes | None: The binary data of the file if it exists, or `None` if the file is not found or an error occurred.

    Example:
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
