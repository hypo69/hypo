
## \file ../src/utils/convertors/text2png.py
# -*- coding: utf-8 -*-
#! /path/to/python/interpreter
"""
This module reads text from a file, generates PNG images for each line of text using Pillow,
and saves them to an output directory with customizable options for image appearance.
"""

import logging
import math
from pathlib import Path
from typing import List, Tuple, Optional
from PIL import Image, ImageDraw, ImageFont


class TextToImageGenerator:
    """
    A class for generating PNG images from text lines.

    **Functions**:
    
    - `assign_path`: Determines the correct path for output PNG files, creating the directory if necessary.
    - `center_text_position`: Calculates the position to center text on the canvas.
    - `generate_png`: Creates a PNG image with the specified text, font, colors, etc.
    - `not_comment_or_blank`: Checks if a line is neither a comment nor blank.
    - `which_exist`: Checks which file names already exist in the directory.
    - `get_characters`: Extracts text lines from the input file or list, filtering out comments and blank lines.
    - `parse_size`: Parses a string into a `Size` object.
    - `get_max_text_size`: Computes the maximum text size based on the font and text lines.
    - `get_font`: Determines the font size based on canvas size and padding.
    - `setup_logging`: Configures logging based on the specified logging level.
    - `error`: Logs an error message and raises an exception.

    **Parameters**:
    
    - `default_output_dir`: Default directory for saving images.
    - `default_canvas_size`: Default canvas size for images.
    - `default_padding`: Default padding around text in the image.
    - `default_background`: Default background color for images.
    - `default_text_color`: Default text color for images.
    - `default_log_level`: Default logging level.
    """

    def __init__(self):
        """
        Initializes the TextToImageGenerator class with default settings.
        """
        self.default_output_dir = Path("./output")
        self.default_canvas_size = (1024, 1024)
        self.default_padding = 0.10
        self.default_background = "white"
        self.default_text_color = "black"
        self.default_log_level = logging.WARNING

    async def generate_images(
        self,
        lines: List[str],
        output_dir: Optional[str | Path] = None,
        font: Optional[str | ImageFont.ImageFont] = "sans-serif",
        canvas_size: Optional[Tuple[int, int]] = None,
        padding: Optional[float] = None,
        background_color: Optional[str] = None,
        text_color: Optional[str] = None,
        log_level: Optional[int | str | bool] = None,
        clobber: bool = False,
    ) -> List[Path]:
        """
        Generates PNG images from the provided text lines.

        Args:
            lines (List[str]): A list of strings containing the text to generate images from.
            output_dir (Optional[str | Path], optional): Directory to save the output images. Defaults to "./output".
            font (Optional[str | ImageFont.ImageFont], optional): Font to use for the text. Defaults to "sans-serif".
            canvas_size (Optional[Tuple[int, int]], optional): Size of the canvas in pixels. Defaults to (1024, 1024).
            padding (Optional[float], optional): Percentage of canvas size to use as a blank border. Defaults to 0.10.
            background_color (Optional[str], optional): Background color for the images. Defaults to "white".
            text_color (Optional[str], optional): Color of the text. Defaults to "black".
            log_level (Optional[int | str | bool], optional): Logging verbosity level. Defaults to logging.WARNING.
            clobber (bool, optional): If True, overwrites existing files. Defaults to False.

        Returns:
            List[Path]: A list of paths to the generated PNG images.

        Example:
            .. code-block:: python

                generator = TextToImageGenerator()
                lines = ["Text 1", "Text 2", "Text 3"]
                output_dir = "./output"
                images = await generator.generate_images(lines, output_dir=output_dir)
                print(images)
                [PosixPath('./output/Text 1.png'), PosixPath('./output/Text 2.png'), PosixPath('./output/Text 3.png')]
        """
        output_directory = Path(output_dir) if output_dir else self.default_output_dir
        self.setup_logging(level=log_level)

        if not canvas_size:
            canvas_size = self.default_canvas_size

        if not padding:
            padding = self.default_padding

        if not background_color:
            background_color = self.default_background

        if not text_color:
            text_color = self.default_text_color

        images = []
        for text in lines:
            image = self.generate_png(
                text=text,
                font=font,
                canvas_size=canvas_size,
                padding=padding,
                background_color=background_color,
                text_color=text_color,
            )
            image_path = self.assign_path(text=text, output_dir=output_directory)
            image.save(fp=image_path, format="PNG")
            images.append(image_path)

        return images

    def setup_logging(self, level: Optional[int | str | bool] = None) -> None:
        """
        Sets up logging configurations based on the specified level.

        Args:
            level (Optional[int | str | bool], optional): Logging level to set. Defaults to logging.WARNING.
        """
        if level is False:
            return None
        elif not level:
            logging.basicConfig(format="%(message)s", level=self.default_log_level)
        else:
            logging.basicConfig(format="%(message)s", level=level)

    def assign_path(self, text: str, output_dir: str | Path) -> Path:
        """
        Determines the path for saving the output image.

        Args:
            text (str): The text for which the path is assigned.
            output_dir (str | Path): Directory to save the images.

        Returns:
            Path: The path to the output image.

        Raises:
            FileExistsError: If the specified path is not a directory.
            Exception: If there is a filesystem error preventing the use of the filename.
        """
        proper_dir = Path(output_dir)
        if proper_dir.exists() and not proper_dir.is_dir():
            raise FileExistsError(f"'{proper_dir}' is not a directory")
        elif proper_dir.exists():
            proper_path = proper_dir / (text + ".png")
        else:
            proper_dir.mkdir()
            proper_path = proper_dir / (text + ".png")

        try:
            proper_path.touch()
        except OSError as err:
            raise Exception(
                "Filesystem error likely prevented using a particular filename"
            ) from err

        return proper_path.expanduser().resolve()

    def center_text_position(
        self, text_size: Tuple[int, int], canvas_size: Tuple[int, int], padding: float
    ) -> Tuple[int, int]:
        """
        Calculates the position to center the text on the canvas.

        Args:
            text_size (Tuple[int, int]): The size of the text.
            canvas_size (Tuple[int, int]): The size of the canvas.
            padding (float): The percentage of the canvas dimensions to use as a blank border.

        Returns:
            Tuple[int, int]: Coordinates (x, y) of the text position.

        Raises:
            ValueError: If the text is too large for the canvas.
        """
        padding_width = padding * canvas_size[0] / 2
        padding_height = padding * canvas_size[1] / 2
        leftover_width = canvas_size[0] - text_size[0] - (padding_width * 2)
        leftover_height = canvas_size[1] - text_size[1] - (padding_height * 2)
        if leftover_height < 0 or leftover_width < 0:
            raise ValueError("Calculation error: text too big for canvas")

        x = math.floor((leftover_width / 2) + padding_width)
        y = math.floor((leftover_height / 2) + padding_height)
        return x, y

    def generate_png(
        self,
        text: str,
        font: str | ImageFont.ImageFont,
        canvas_size: Tuple[int, int],
        padding: float,
        background_color: str,
        text_color: str,
    ) -> Image:
        """
        Creates a PNG image with the specified text.

        Args:
            text (str): The text to display in the image.
            font (str | ImageFont.ImageFont): Font to use for the text.
            canvas_size (Tuple[int, int]): Size of the canvas.
            padding (float): Percentage of canvas dimensions to use as a blank border.
            background_color (str): Color of the background.
            text_color (str): Color of the text.

        Returns:
            Image: The generated PIL Image object.
        """
        canvas = Image.new("RGBA", canvas_size, background_color)
        draw = ImageDraw.Draw(canvas)
        if isinstance(font, str):
            font = ImageFont.load_default()
        text_size = draw.textsize(text=text, font=font)
        text_position = self.center_text_position(
            text_size=text_size, canvas_size=canvas_size, padding=padding
        )
        draw.text(
            xy=text_position, text=text, fill=text_color, font=font,
        )
        return canvas
