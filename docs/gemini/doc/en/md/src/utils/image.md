# hypotez/src/utils/image.py

## Overview

This module provides asynchronous functions for downloading, saving, and retrieving image data.  It utilizes asynchronous operations for improved efficiency, particularly when dealing with network requests.

## Table of Contents

* [save_png_from_url](#save-png-from-url)
* [save_png](#save-png)
* [get_image_data](#get-image-data)


## Functions

### `save_png_from_url`

**Description**: Downloads an image from a given URL and saves it as a PNG file locally.

**Parameters**:
- `image_url` (str): The URL of the image to download.
- `filename` (str | Path): The name of the file to save the image to.

**Returns**:
- `str | None`: The path to the saved file if successful, or `None` if an error occurs during the download or saving process.

**Raises**:
- `Exception`: Any exception encountered during the HTTP request or file saving process.

### `save_png`

**Description**: Saves image data in PNG format to a specified file.

**Parameters**:
- `image_data` (bytes): The binary image data to save.
- `file_name` (str | Path): The name of the file to save the image to.

**Returns**:
- `str | None`: The path to the saved file if successful, or `None` if an error occurs during saving.

**Raises**:
- `Exception`: Any exception encountered during file saving or image processing.


### `get_image_data`

**Description**: Retrieves the binary data of a file if it exists.

**Parameters**:
- `file_name` (str | Path): The name of the file to read.

**Returns**:
- `bytes | None`: The binary data of the file if successful, or `None` if the file is not found or an error occurs.

**Raises**:
- `Exception`: Any exception encountered during file reading.