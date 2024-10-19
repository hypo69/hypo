## \file ../src/utils/video.py
# -*- coding: utf-8 -*-
#! /path/to/interpreter/python
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

    Example:
        >>> asyncio.run(save_video_from_url("https://example.com/video.mp4", "local_video.mp4"))
        PosixPath('local_video.mp4')
    """
    save_path = Path(save_path)

    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                response.raise_for_status()  # Check if the request was successful

                save_path.parent.mkdir(parents=True, exist_ok=True)

                async with aiofiles.open(save_path, "wb") as file:
                    while True:
                        chunk = await response.content.read(8192)
                        if not chunk:
                            break
                        await file.write(chunk)

        # Check if the file was saved
        if not save_path.exists():
            logger.error(f"File {save_path=} was not saved.")
            return None

        if save_path.stat().st_size == 0:
            logger.error(f"File {save_path=} was saved, but its size is 0 bytes.")
            return None

    except Exception as ex:
        logger.error(f"Error saving video {save_path=}: {ex}", exc_info=True)
        return None

    return save_path

def get_video_data(file_name: str) -> Optional[bytes]:
    """Retrieve binary data of a video file if it exists.

    Args:
        file_name (str): The path to the video file to read.

    Returns:
        Optional[bytes]: The binary data of the file if it exists, or `None` if the file is not found or an error occurred.

    Example:
        >>> get_video_data("local_video.mp4")
        b'\x00\x00\x00...'
    """
    file_path = Path(file_name)

    if not file_path.exists():
        logger.error(f"File {file_path=} does not exist.")
        return None

    try:
        with open(file_path, "rb") as file:
            return file.read()
    except Exception as ex:
        logger.error(f"Error reading file {file_path=}: {ex}", exc_info=True)
        return None

def main():
    url = "https://example.com/video.mp4"
    save_path = "local_video.mp4"
    asyncio.run(save_video_from_url(url, save_path))

if __name__ == "__main__":
    main()
