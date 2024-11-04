## \file src/utils/convertors/webp2png.py
# -*- coding: utf-8 -*-
#! /path/to/python/interpreter
"""
This module reads text from a file, generates PNG images for each line of text using Pillow,
and saves them to an output directory with customizable options for image appearance.
"""


from PIL import Image

def webp2png(webp_path: str, png_path: str) -> bool:
    """
    Converts a WEBP image to PNG format.

    Args:
        webp_path (str): Path to the input WEBP file.
        png_path (str): Path to save the converted PNG file.

    Example:
        webp2png('image.webp', 'image.png')
    """
    try:
        # Open the webp image
        with Image.open(webp_path) as img:
            # Convert to PNG and save
            img.save(png_path, 'PNG')
        return True
    except Exception as e:
        print(f"Error during conversion: {e}")
        return

if __name__ == "main":
    # Example usage
    #webp2png('input_image.webp', 'output_image.png')
    ...
