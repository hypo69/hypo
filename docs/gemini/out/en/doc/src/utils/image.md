# hypotez/src/utils/image.py

## Overview

This module provides asynchronous functions for downloading, saving, and retrieving image data.  It utilizes `aiohttp` for asynchronous HTTP requests, `aiofiles` for asynchronous file operations, and `PIL` for image manipulation.  Crucially, it includes error handling and logging to ensure robustness.

## Table of Contents

* [Functions](#functions)

## Functions

### `save_png_from_url`

**Description**: Downloads an image from a given URL and saves it as a PNG file asynchronously.

**Parameters**:
- `image_url` (str): The URL of the image to download.
- `filename` (str | Path): The name of the file to save the image to.

**Returns**:
- `str | None`: The path to the saved file if successful, or `None` if an error occurred during the download or saving process.

**Raises**:
- `Exception`: Any exception encountered during the HTTP request or file saving process.  Detailed error logging is included.

### `save_png`

**Description**: Saves image data in PNG format asynchronously.

**Parameters**:
- `image_data` (bytes): The binary data representing the image.
- `file_name` (str | Path): The name of the file to save the image to.

**Returns**:
- `str | None`: The path to the saved file if successful, or `None` if an error occurred during the file saving process.

**Raises**:
- `Exception`: Any exception encountered during the file saving process, including issues creating directories, writing the file, or verifying the saved file's integrity (e.g., empty file). Detailed error logging is included.

### `get_image_data`

**Description**: Retrieves the binary data of a file.

**Parameters**:
- `file_name` (str | Path): The name of the file to read.

**Returns**:
- `bytes | None`: The binary data of the file if it exists, or `None` if the file is not found or an error occurred during the read operation.

**Raises**:
- `Exception`: Any exception encountered during the file reading process. Detailed error logging is included.