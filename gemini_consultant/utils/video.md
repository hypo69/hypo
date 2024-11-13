```python
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe # <- venv win
"""
Video Saving Utilities.

This module provides asynchronous functions for downloading and saving video files, as well as retrieving video data.

Functions:
    save_video_from_url(url: str, save_path: str) -> Optional[Path]:
        Download a video from a URL and save it locally asynchronously.

    get_video_data(file_name: str) -> Optional[bytes]:
        Retrieve binary data of a video file if it exists.


Examples:
    >>> asyncio.run(save_video_from_url("https://example.com/video.mp4", "local_video.mp4"))
    PosixPath('local_video.mp4')

    >>> get_video_data("local_video.mp4")
    b'\x00\x00\x00...'
"""

import aiohttp
import aiofiles
from pathlib import Path
from typing import Optional
import asyncio
from src.logger import logger
import os


async def save_video_from_url(
    url: str,
    save_path: str
) -> Optional[Path]:
    """Download a video from a URL and save it locally asynchronously.

    Args:
        url (str): The URL from which to download the video.
        save_path (str): The path to save the downloaded video.

    Returns:
        Optional[Path]: The path to the saved file, or `None` if the operation failed.
    """

    save_path = Path(save_path)

    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                response.raise_for_status()  # Check if the request was successful
                
                # Crucial: Check content-length before creating the file
                content_length = int(response.headers.get('content-length', 0))
                if content_length == 0:
                    logger.error(f"Content-length for {url} is 0")
                    return None

                save_path.parent.mkdir(parents=True, exist_ok=True)

                async with aiofiles.open(save_path, "wb") as file:
                    total_received = 0
                    while True:
                        chunk = await response.content.read(8192)
                        if not chunk:
                            break
                        await file.write(chunk)
                        total_received += len(chunk)
                        # Optionally, log progress (important for large files)
                        # logger.info(f"Downloaded {total_received}/{content_length} bytes")
                    
                    if total_received != content_length:
                        logger.error(f"Downloaded {total_received} bytes, expected {content_length}.  File might be corrupted.")
                        return None

    except aiohttp.ClientError as e:
        logger.error(f"Client error while downloading {url}: {e}")
        return None
    except Exception as ex:
        logger.error(f"Error saving video {save_path=}: {ex}", exc_info=True)
        return None

    return save_path


def get_video_data(file_name: str) -> Optional[bytes]:
    file_path = Path(file_name)
    if not file_path.exists():
        logger.error(f"File {file_path} does not exist.")
        return None
    try:
      return open(file_path, "rb").read()
    except Exception as ex:
        logger.error(f"Error reading file {file_path=}: {ex}", exc_info=True)
        return None



# Example usage (remove if not needed in your final script)
def main():
    url = "https://www.w3schools.com/images/w3schoolslogo.svg"  # Example image
    save_path = "local_image.svg"
    asyncio.run(save_video_from_url(url, save_path))


if __name__ == "__main__":
    main()
```

**Key Improvements and Explanations:**

* **Error Handling (Crucial):**  The `save_video_from_url` function now has robust error handling. It catches `aiohttp.ClientError` specifically for HTTP errors (e.g., 404 Not Found) and general exceptions. This is *much* more reliable.  It also checks for 0 content length and if the downloaded size matches the expected size.
* **Content-Length Check:** Added a crucial check for the `content-length` header.  If the header is missing or zero, it logs an error and returns `None`—preventing potential issues.
* **Progress Logging (Optional):**  Included a commented-out section to show how you could log download progress, which is beneficial for large files.
* **File Existence Check:** The `get_video_data` function now checks if the file exists before trying to open it.
* **Simplified `get_video_data`:** Improved the `get_video_data` function for clarity and efficiency.
* **Example Usage (Modified):**  The example now uses a valid image URL (important for testing).  It's much safer to test with a real (small!) file for debugging purposes.
* **Import `os` (helpful):** I added the `import os` line for potential use of the operating system (e.g., for creating directories).
* **Clearer Error Messages:** Improved error messages to provide more context.


**How to Run (Crucial):**

1.  **Install aiohttp and aiofiles:**
    ```bash
    pip install aiohttp aiofiles
    ```

2.  **Create a `src/logger.py`:**  If you don't have one already.  This handles logging.  A simple example:

```python
# src/logger.py
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
```

3.  **Run:**
    ```bash
    python your_script_name.py 
    ```

This revised code is significantly more robust and handles potential problems that could lead to errors or silent failures.  Always test with actual URLs and files to validate the functionality. Remember to adjust the example usage to your specific needs.