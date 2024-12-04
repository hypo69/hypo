# Image Handling Utilities in `hypotez`

## <input code>

```python
## \file hypotez/src/utils/image.py
# -*- coding: utf-8 -*-\n#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
.. module:: src.utils
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
from src.logger import logger
from src.utils.printer import pprint

# ... (rest of the code)
```

## <algorithm>

**Workflow Diagram:**

**1. `save_png_from_url(image_url, filename)`:**

*   **Input:** Image URL, filename.
*   **Process:**
    *   Establish an `aiohttp.ClientSession`.
    *   Make an asynchronous GET request to the `image_url`.
    *   Error Handling: Checks for HTTP errors (status codes).
    *   Reads the image data from the response.
    *   Calls `save_png` function with the retrieved image data and filename.
*   **Output:** Path to the saved file or `None` if failure.

**2. `save_png(image_data, file_name)`:**

*   **Input:** Image data (bytes), filename.
*   **Process:**
    *   Constructs a `Path` object from the `file_name`.
    *   Creates parent directories if they don't exist (`file_path.parent.mkdir(parents=True, exist_ok=True)`).
    *   Opens the file in write binary mode (`aiofiles.open`) for asynchronous writing.
    *   Writes the `image_data` to the file.
    *   Validation: Checks if the file was successfully created and has non-zero size.
    *   Opens the file using `PIL` to verify and save it as PNG.
    *   Error Handling: Catches exceptions during file operations.
*   **Output:** Path to the saved file or `None` if failure.


**3. `get_image_data(file_name)`:**

*   **Input:** Filename.
*   **Process:**
    *   Constructs a `Path` object from the `file_name`.
    *   Checks if the file exists using `file_path.exists()`.
    *   Reads the file in read binary mode (`open`).
    *   Error Handling: Catches exceptions during file reading.
*   **Output:** Binary data of the file or `None` if not found or error.


## <mermaid>

```mermaid
graph LR
    A[save_png_from_url(image_url, filename)] --> B{aiohttp.ClientSession};
    B --> C[GET Request];
    C --> D{Response Check};
    D --Success--> E[Read Data];
    D --Failure--> F[Error Logging];
    E --> G[save_png(image_data, filename)];
    G --> H[Check & Save];
    H --Success--> I[Return Path];
    H --Failure--> J[Error Logging];
    F --> J;
    G --> K[get_image_data(file_name)];
    K --> L[Check Existence];
    L --Exist--> M[Read Data (open)];
    L --Not Exist--> N[Error Logging];
    M --> O[Return Data];
    N --> O;
    style I fill:#ccf,stroke:#333,stroke-width:2px;
    style J fill:#fdd,stroke:#333,stroke-width:2px;
    style O fill:#ccf,stroke:#333,stroke-width:2px;
```

**Dependencies:**
*   `aiohttp`: Asynchronous HTTP client for downloading images.
*   `aiofiles`: Asynchronous file I/O operations.
*   `PIL (Pillow)`:  Image processing library (for saving in PNG format).
*   `pathlib`: For path manipulation.
*   `asyncio`: Asynchronous programming framework.
*   `src.logger`: Custom logging module (likely part of the project).
*   `src.utils.printer`: Custom utility module for printing (likely part of the project).

## <explanation>

**Imports:**

*   `aiohttp`: Used for making asynchronous HTTP requests to download images from URLs.  Relationship with `src` packages is not direct but implicitly relies on network interactions.
*   `aiofiles`: Provides asynchronous file I/O operations, crucial for saving downloaded images efficiently.  Dependent on `asyncio`.
*   `PIL`: Enables image manipulation, particularly saving images in PNG format.
*   `pathlib`:  Provides an object-oriented way to work with file paths, making code more readable and robust.
*   `asyncio`: Required for asynchronous operations in the functions (`save_png_from_url`, `save_png`).
*   `src.logger` and `src.utils.printer`: Custom modules, suggesting a structured logging and output system within the project (`hypotez`).

**Classes:**

*   There are no classes defined in this module.

**Functions:**

*   `save_png_from_url(image_url, filename)`: Downloads an image from a given URL and saves it locally as a PNG file.  Robust error handling using `try...except` blocks for network issues, ensuring that partial downloads aren't left behind and that issues are logged.
*   `save_png(image_data, file_name)`: Saves image data (in bytes) to a specified file. It handles file creation, ensuring parent directories exist. Key improvement is the file verification: checking if it was created and whether it's empty or not before proceeding. This avoids silent errors and improves reliability.
*   `get_image_data(file_name)`: Reads and returns the binary data of an existing image file.  Handles potential exceptions during file reading.

**Variables:**

*   `MODE`: A string variable likely used for different modes of operation (e.g., development, production).


**Potential Errors/Improvements:**

*   **Error Handling:** While error handling is present, consider more specific exception handling (e.g., `aiohttp.ClientError` for network issues) within `save_png_from_url`.
*   **File Locking:** If multiple processes might access or modify the files concurrently, using file locks (e.g., `threading.Lock`) would prevent race conditions and data corruption.
*   **Input Validation:**  Validating `image_url` and `filename` (e.g., checking for valid URLs and file extensions) could further improve robustness.


**Relationships:**

This module interacts with `src.logger` and potentially `src.utils.printer` for logging and output purposes, showing its dependency on other parts of the `hypotez` project. It's also coupled with external libraries for downloading images and saving files.