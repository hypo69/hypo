# hypotez/src/utils/video.py

## Overview

This module provides asynchronous functions for downloading and saving video files, as well as retrieving video data. It includes error handling and logging for robust operation.

## Table of Contents

* [save_video_from_url](#save_video_from_url)
* [get_video_data](#get_video_data)


## Functions

### `save_video_from_url`

**Description**: Download a video from a URL and save it locally asynchronously. Handles potential network issues and file saving errors.

**Parameters**:

- `url` (str): The URL from which to download the video.
- `save_path` (str): The path to save the downloaded video.

**Returns**:

- `Optional[Path]`: The path to the saved file, or `None` if the operation failed. Returns `None` on errors and if the file is 0 bytes.

**Raises**:

- `aiohttp.ClientError`: On network issues during the download.


### `get_video_data`

**Description**: Retrieve binary data of a video file if it exists. Handles file not found and read errors.

**Parameters**:

- `file_name` (str): The path to the video file to read.


**Returns**:

- `Optional[bytes]`: The binary data of the file if it exists, or `None` if the file is not found or an error occurred.

**Raises**:
- No exceptions are explicitly documented, but `Exception` is caught, indicating potential other errors.