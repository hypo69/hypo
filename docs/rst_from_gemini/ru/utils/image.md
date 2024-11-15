```
```python
# -*- coding: utf-8 -*-
 # <- venv win
""" module: src.utils """
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
        str | None: The path to the saved file or `None` if the operation failed.  Raises exceptions instead of returning None in cases where the URL is invalid or the request fails

    Example:
        >>> asyncio.run(save_png_from_url("https://example.com/image.png", "local_image.png"))
        'local_image.png'
    """
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(image_url) as response:
                response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
                image_data = await response.read()
        return await save_png(image_data, filename)
    except aiohttp.ClientError as e:
        logger.error(f"Error downloading image from {image_url}: {e}")
        return None
    except Exception as e:
        logger.error(f"An unexpected error occurred while downloading {image_url}: {e}")
        return None


async def save_png(image_data: bytes, file_name: str | Path) -> str | None:
    """Save an image in PNG format asynchronously.

    Args:
        image_data (bytes): The binary image data.
        file_name (str | Path): The name of the file to save the image to.

    Returns:
        str | None: The path to the saved file or `None` if the operation failed.  Returns None if the image data is empty or if the file size is 0.
    """
    file_path = Path(file_name)

    try:
        # Create necessary directories
        file_path.parent.mkdir(parents=True, exist_ok=True)

        # Check if image_data is empty
        if not image_data:
            logger.error("Image data is empty.")
            return None

        # Write file
        async with aiofiles.open(file_path, "wb") as file:
            await file.write(image_data)

        # Verify file creation and size.  This needs to be done after writing!
        if not file_path.exists() or file_path.stat().st_size == 0:
            logger.error(f"Failed to save or file is empty: {file_path}")
            return None

        # Open and save the image with PIL (ensuring proper format)
        img = Image.open(file_path)
        img.save(file_path, "PNG")

    except Exception as ex:
        logger.critical(f"Failed to save or process image {file_name}", exc_info=True)
        return None

    return str(file_path)


def get_image_data(file_name: str | Path) -> bytes | None:
    """Retrieve binary data of a file if it exists.

    Args:
        file_name (str | Path): The name of the file to read.

    Returns:
        bytes | None: The binary data of the file if it exists, or `None` if the file is not found or an error occurred.
    """
    file_path = Path(file_name)

    if not file_path.exists():
        logger.error(f"File {file_path} not found.")
        return None

    try:
        with open(file_path, "rb") as file:
            return file.read()
    except Exception as ex:
        logger.error(f"Error reading file {file_path}: {ex}")
        return None
```

**Key Improvements and Explanations:**

* **Error Handling:** The code now includes robust error handling using `try...except` blocks.  This is crucial for production-quality code.  The `save_png_from_url` function specifically catches `aiohttp.ClientError` for more specific error handling.  Critically, it now logs *all* exceptions and returns `None` to indicate failure, providing valuable information to the calling code.

* **Empty Image Data Check:** Added a check in `save_png` to handle cases where `image_data` is empty. This prevents potential errors.

* **File Existence and Size Check:** The file creation and size checks are *moved* to after the write operation.  This ensures the file exists before checking size.

* **PIL Image Handling:** The image is now opened and saved using PIL's `Image.open()` and `save()`. This is significantly more robust and handles potential image formats more gracefully.


* **Clearer Error Messages:** Error messages are more informative, including the filename or URL involved.

* **Return `None` for Failure:**  Explicitly returns `None` from functions to indicate failure cases.  This is much better than returning an empty string.

* **`raise_for_status()`:** The `save_png_from_url` function now uses `response.raise_for_status()`, which correctly raises an `aiohttp.ClientError` for bad HTTP responses (4xx or 5xx).  This is critical for proper error handling.


These changes make the code more reliable, easier to debug, and less prone to unexpected crashes.  The logging is crucial for seeing what went wrong in a production environment.  Always handle potential errors in your asynchronous code.