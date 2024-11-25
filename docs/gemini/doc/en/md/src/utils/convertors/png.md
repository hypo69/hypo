# hypotez/src/utils/convertors/png.py

## Overview

This module provides functionality for generating PNG images from text using the Pillow library. It allows customization of various aspects such as output directory, font, canvas size, padding, background and text colors, and logging levels.  The module also includes a function for converting WEBP images to PNG.


## Classes

### `TextToImageGenerator`

**Description**: This class encapsulates the logic for generating PNG images from text. It handles file path assignment, text centering, image creation, and logging.

**Methods**

#### `__init__`

**Description**: Initializes the `TextToImageGenerator` class with default settings.

#### `generate_images`

**Description**: Generates PNG images from a list of text lines.

**Parameters**

- `lines` (List[str]): A list of strings containing the text to generate images from.
- `output_dir` (str | Path, optional): Directory to save the output images. Defaults to "./output".
- `font` (str | ImageFont.ImageFont, optional): Font to use for the text. Defaults to "sans-serif".
- `canvas_size` (Tuple[int, int], optional): Size of the canvas in pixels. Defaults to (1024, 1024).
- `padding` (float, optional): Percentage of canvas size to use as a blank border. Defaults to 0.10.
- `background_color` (str, optional): Background color for the images. Defaults to "white".
- `text_color` (str, optional): Color of the text. Defaults to "black".
- `log_level` (int | str | bool, optional): Logging verbosity level. Defaults to "WARNING".
- `clobber` (bool, optional): If True, overwrites existing files. Defaults to False.


**Returns**

- List[Path]: A list of paths to the generated PNG images.

**Example**:
```python
generator = TextToImageGenerator()
lines = ["Text 1", "Text 2", "Text 3"]
output_dir = "./output"
images = await generator.generate_images(lines, output_dir=output_dir)
print(images)
```

#### `generate_png`

**Description**: Creates a PNG image with the specified text, font, colors, etc.


**Parameters**

- `text` (str): Text to render on the image.
- `canvas_size` (Tuple[int, int]): Size of the canvas in pixels.
- `padding` (float): Padding percentage to use as a border.
- `background_color` (str): Background color of the image.
- `text_color` (str): Color of the text.
- `font` (str | ImageFont.ImageFont): Font to use for the text.


**Returns**

- Image: The generated PNG image.


#### `center_text_position`

**Description**: Calculates the position to center the text on the canvas.

**Parameters**

- `draw` (ImageDraw.Draw): The ImageDraw instance.
- `text` (str): Text to be rendered.
- `font` (ImageFont.ImageFont): Font used for the text.
- `canvas_size` (Tuple[int, int]): Size of the canvas in pixels.

**Returns**

- Tuple[int, int]: Coordinates for centering the text.


#### `overlay_images`

**Description**: Overlays one PNG image on top of another at a specified position.

**Parameters**

- `background_path` (str | Path): Path to the background PNG image.
- `overlay_path` (str | Path): Path to the overlay PNG image.
- `position` (tuple[int, int], optional): (x, y) coordinates where the overlay will be placed. Defaults to (0, 0).
- `alpha` (float, optional): Transparency level of the overlay image (0.0 - 1.0). Defaults to 1.0.

**Returns**

- Image: The resulting image with the overlay.


## Functions

### `webp2png`

**Description**: Converts a WEBP image to PNG format.

**Parameters**

- `webp_path` (str): Path to the input WEBP file.
- `png_path` (str): Path to save the converted PNG file.

**Returns**

- bool: True if the conversion was successful, otherwise None.
  Raises an exception if the conversion fails.


**Example**:
```python
webp2png('image.webp', 'image.png')
```