# `text2png` Module

## `TextToImageGenerator` Class

The `TextToImageGenerator` class generates PNG images of text lines using the Pillow library. It offers various configuration options for customizing the appearance of the generated images.

### `__init__()`

Initializes the `TextToImageGenerator` class with default settings.

#### Attributes:
- **default_output_dir**: Default directory for output images (`./output`).
- **default_canvas_size**: Default size of the canvas (1024x1024 pixels).
- **default_padding**: Default padding percentage (10%).
- **default_background**: Default background color (`white`).
- **default_text_color**: Default text color (`black`).
- **default_log_level**: Default logging level (`WARNING`).

### `generate_images()`

Generates PNG images for a list of text lines.

#### Args:
- **lines (List[str])**: A list of text lines to convert to images.
- **output_dir (str | Path, optional)**: Directory to save the images. Defaults to `./output`.
- **font (str | ImageFont.ImageFont, optional)**: Font for the text. Defaults to `"sans-serif"`.
- **canvas_size (Tuple[int, int], optional)**: Size of the canvas in pixels. Defaults to (1024, 1024).
- **padding (float, optional)**: Percentage of canvas size to use as padding. Defaults to 0.10.
- **background_color (str, optional)**: Background color of the images. Defaults to `"white"`.
- **text_color (str, optional)**: Color of the text. Defaults to `"black"`.
- **log_level (int | str | bool, optional)**: Logging level. Defaults to `logging.WARNING`.
- **clobber (bool, optional)**: If `True`, overwrites existing files. Defaults to `False`.

#### Returns:
- **List[Path]**: List of paths to the generated images.

#### Raises:
- **Exception**: If unable to parse parameters or generate images.

### `setup_logging()`

Configures the logging settings.

#### Args:
- **level (int | str | bool, optional)**: Logging level. Defaults to `logging.WARNING`.

### `assign_path()`

Determines the path for saving the output image.

#### Args:
- **text (str)**: Text for which the path is assigned.
- **output_dir (str | Path)**: Directory to save the images.

#### Returns:
- **Path**: Path to the output image file.

#### Raises:
- **FileExistsError**: If the path is not a directory.
- **Exception**: If a filesystem error occurs.

### `center_text_position()`

Calculates the position to center the text on the canvas.

#### Args:
- **text_size (Tuple[int, int])**: Size of the text.
- **canvas_size (Tuple[int, int])**: Size of the canvas.
- **padding (float)**: Padding around the text.

#### Returns:
- **Tuple[int, int]**: Coordinates (x, y) to position the text.

#### Raises:
- **ValueError**: If the text is too large for the canvas.

### `generate_png()`

Creates a PNG image with the given text.

#### Args:
- **text (str)**: The text to render in the image.
- **font (str | ImageFont.ImageFont)**: Font for the text.
- **canvas_size (Tuple[int, int])**: Size of the canvas.
- **padding (float)**: Padding around the text.
- **background_color (str)**: Background color of the image.
- **text_color (str)**: Color of the text.

#### Returns:
- **Image**: A PIL `Image` object representing the generated PNG image.

#### Raises:
- **Exception**: If unable to generate the image.

### Example Usage

```python
async def main():
    generator = TextToImageGenerator()
    lines = ["Text 1", "Text 2", "Text 3"]
    output_dir = "./output"
    images = await generator.generate_images(lines, output_dir=output_dir)
    print(images)

await main()
```

```python
if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
```
