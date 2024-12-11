# `image.py` Module

## Description

The `image.py` module provides utilities for working with images, including asynchronous downloading, saving, reading, and finding random images. It is designed for use in projects that require image processing, such as downloading images from URLs, saving them to local storage, and recursively searching for random images in a specified directory.

## Key Functions

### 1. `save_png_from_url(image_url: str, filename: str | Path) -> str | None`

Asynchronously downloads an image from the specified URL and saves it locally in PNG format.

- **Parameters:**
  - `image_url` (str): The URL of the image to download.
  - `filename` (str | Path): The file name or path where the image will be saved.
- **Returns:**
  - The path to the saved file or `None` if the operation failed.

**Example:**
```python
import asyncio

asyncio.run(save_png_from_url("https://example.com/image.png", "local_image.png"))
```

---

### 2. `save_png(image_data: bytes, file_name: str | Path) -> str | None`

Asynchronously saves the provided image data in PNG format.

- **Parameters:**
  - `image_data` (bytes): The binary image data.
  - `file_name` (str | Path): The file name or path where the image will be saved.
- **Returns:**
  - The path to the saved file or `None` if the operation failed.

**Example:**
```python
import asyncio

with open("example_image.png", "rb") as f:
    image_data = f.read()

asyncio.run(save_png(image_data, "saved_image.png"))
```

---

### 3. `get_image_data(file_name: str | Path) -> bytes | None`

Synchronously reads the binary data of an image from the specified file.

- **Parameters:**
  - `file_name` (str | Path): The file name or path of the image.
- **Returns:**
  - The binary data of the image or `None` if the file is not found or an error occurred.

**Example:**
```python
data = get_image_data("saved_image.png")
print(data)  # Output: b'\x89PNG\r\n...'
```

---

### 4. `random_image(root_path: str | Path) -> str | None`

Recursively searches for a random image in the specified directory and returns its path.

- **Parameters:**
  - `root_path` (str | Path): The directory to search for images.
- **Returns:**
  - The path to a random image or `None` if no images are found.

**Example:**
```python
random_image_path = random_image("path/to/images")
if random_image_path:
    print(f"Random image: {random_image_path}")
else:
    print("No images found.")
```

---

## Installation and Usage

1. Ensure you have Python 3.8 or higher installed.
2. Install the required dependencies:
   ```bash
   pip install aiohttp aiofiles pillow
   ```
3. Import the functions from the `image.py` module into your project:
   ```python
   from src.utils.image import save_png_from_url, save_png, get_image_data, random_image
   ```

---

## Usage Examples

### Downloading an Image from a URL and Saving It
```python
import asyncio

asyncio.run(save_png_from_url("https://example.com/image.png", "local_image.png"))
```

### Saving an Image from Data
```python
import asyncio

with open("example_image.png", "rb") as f:
    image_data = f.read()

asyncio.run(save_png(image_data, "saved_image.png"))
```

### Reading Image Data
```python
data = get_image_data("saved_image.png")
print(data)
```

### Finding a Random Image
```python
random_image_path = random_image("path/to/images")
if random_image_path:
    print(f"Random image: {random_image_path}")
else:
    print("No images found.")
```

---

## Logging

The module uses a built-in logger to track errors and warnings. Ensure that the logger is configured in your project to receive messages.

---

## License

This project is licensed under the [MIT License](../LICENSE).

---

## Author

hypo69