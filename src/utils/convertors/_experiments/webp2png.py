## \file /src/utils/convertors/_experiments/webp2png.py
# -*- coding: utf-8 -*-

#! venv/bin/python/python3.12

"""
.. module:: src.utils.convertors._experiments 
	:platform: Windows, Unix
	:synopsis:

"""


"""
	:platform: Windows, Unix
	:synopsis:

"""

"""
	:platform: Windows, Unix
	:synopsis:

"""

"""
  :platform: Windows, Unix

"""
"""
  :platform: Windows, Unix
  :platform: Windows, Unix
  :synopsis:
"""
  
""" module: src.utils.convertors._experiments """


""" This module converts WebP images to PNG format.

It retrieves WebP files from a specified directory and converts them to PNG format, 
saving the output to another directory. The conversion is handled by the `webp2png` function.
"""

import header
from pathlib import Path
from src import gs
from src.utils.convertors.webp2png import webp2png
from src.utils.file import get_filenames

def convert_images(webp_dir: Path, png_dir: Path) -> None:
    """ Convert all WebP images in the specified directory to PNG format.

    Args:
        webp_dir (Path): Directory containing the source WebP images.
        png_dir (Path): Directory to save the converted PNG images.

    Example:
        convert_images(
            gs.path.google_drive / 'emil' / 'raw_images_from_openai',
            gs.path.google_drive / 'emil' / 'converted_images'
        )
    """
    webp_files: list = get_filenames(webp_dir)

    for webp in webp_files:
        png = png_dir / f"{Path(webp).stem}.png"  # Use `stem` to get the file name without extension
        webp_path = webp_dir / webp  
        result = webp2png(webp_path, png)
        print(result)

if __name__ == '__main__':
    # Define the directories for WebP and PNG images
    webp_dir = gs.path.google_drive / 'kazarinov' / 'raw_images_from_openai'
    png_dir = gs.path.google_drive / 'kazarinov' / 'converted_images'
    print(f"from: {webp_dir=}\nto:{png_dir=}")
    # Run the conversion
    convert_images(webp_dir, png_dir)
