# `image` Module

## `save_png_from_url()`

The `save_png_from_url` function downloads an image from a URL and saves it locally asynchronously.

### How the function works:

1. **Image Download**: Uses `aiohttp` to fetch the image data from the URL.
2. **Error Handling**: Logs errors if the download fails.
3. **File Saving**: Calls `save_png` to save the image data to a file.

### Args:
- **image_url (str)**: The URL to download the image from.
- **filename (str | Path)**: The name of the file to save the image to.

### Returns:
- **str | None**: The path to the saved file or `None` if the operation failed.

### Raises:
- **Exception**: Logs errors if the image download fails.

### Examples:

```python
>>> asyncio.run(save_png_from_url("https://example.com/image.png", "local_image.png"))
'local_image.png'

>>> asyncio.run(save_png_from_url("https://example.com/image.png", Path("local_image.png")))
'local_image.png'
```

## `save_png()`

The `save_png` function saves image data in PNG format asynchronously.

### How the function works:

1. **Directory Creation**: Ensures that any necessary directories exist.
2. **File Writing**: Writes the binary image data to a file.
3. **Image Saving**: Opens the image with PIL and saves it in PNG format.
4. **Error Handling**: Logs errors if file operations or image saving fails.

### Args:
- **image_data (bytes)**: The binary image data.
- **file_name (str | Path)**: The name of the file to save the image to.

### Returns:
- **str | None**: The path to the saved file or `None` if the operation failed.

### Raises:
- **Exception**: Logs errors if file operations or image saving fails.

### Examples:

```python
>>> with open("example_image.png", "rb") as f:
...     image_data = f.read()
>>> asyncio.run(save_png(image_data, "saved_image.png"))
'saved_image.png'

>>> with open("example_image.png", "rb") as f:
...     image_data = f.read()
>>> asyncio.run(save_png(image_data, Path("saved_image.png")))
'saved_image.png'
```

## `get_image_data()`

The `get_image_data` function retrieves the binary data of a file if it exists.

### How the function works:

1. **File Existence Check**: Verifies if the file exists.
2. **File Reading**: Opens the file and reads its binary data.
3. **Error Handling**: Logs errors if file reading fails.

### Args:
- **file_name (str | Path)**: The name of the file to read.

### Returns:
- **bytes | None**: The binary data of the file if it exists, or `None` if the file is not found or an error occurred.

### Raises:
- **FileNotFoundError**: Logs an error if the file does not exist.
- **Exception**: Logs errors if file reading fails.

### Examples:

```python
>>> get_image_data("saved_image.png")
b'\x89PNG\r\n...'

>>> get_image_data("nonexistent_image.png")
None
```
