rst
How to use the image saving utilities
=========================================================================================

Description
-------------------------
This Python module (`hypotez/src/utils/image.py`) provides functions for asynchronously downloading, saving, and retrieving image data. It utilizes libraries like `aiohttp` for asynchronous HTTP requests, `aiofiles` for asynchronous file I/O, and `PIL` for image manipulation.  Crucially, the functions incorporate error handling and logging to manage potential issues during file operations.


Execution steps
-------------------------
1. **Download an image from a URL (save_png_from_url):**
   - Takes the image URL and the desired filename as input.
   - Establishes an asynchronous HTTP session using `aiohttp`.
   - Retrieves the image data from the specified URL.
   - Handles potential errors during the download process (e.g., invalid URL, network issues) using `try...except` blocks and logging.
   - Calls the `save_png` function to save the received image data to the specified file.


2. **Save image data to a file (save_png):**
   - Takes the image data (as bytes) and the filename as input.
   - Creates the necessary directories if they don't exist using `Path.mkdir`.
   - Writes the image data to the specified file using `aiofiles`.
   - Verifies that the file was successfully created and has non-zero size.
   - Opens the saved image using Pillow, ensuring that it's a valid image before saving. Saves the image in PNG format.
   - Handles potential file-related errors (e.g., file not created, issues with image format) during the save process using `try...except` and logging.


3. **Retrieve image data from a file (get_image_data):**
   - Takes the filename as input.
   - Checks if the file exists. If not, logs an error and returns `None`.
   - Opens the file in binary read mode (`"rb"`).
   - Reads the entire content of the file into a byte string.
   - Handles potential errors during file reading using `try...except` and logging.
   - Returns the image data if successful, otherwise returns `None`.

Usage example
-------------------------
.. code-block:: python

    import asyncio
    from hypotez.src.utils.image import save_png_from_url, save_png, get_image_data

    async def main():
        # Example 1: Downloading and saving an image from a URL
        await save_png_from_url("https://upload.wikimedia.org/wikipedia/commons/thumb/6/6d/Example.jpg/1200px-Example.jpg", "downloaded_image.png")
        #await save_png_from_url("invalid_url", "failed_download.png") #Example with bad URL


        # Example 2: Saving image data from a file-like object
        with open("example_image.png", "rb") as f:
            image_data = f.read()
        await save_png(image_data, "saved_image_from_data.png")

        # Example 3: Retrieving image data from a file
        image_data = get_image_data("saved_image_from_data.png")

        if image_data:
          print("Image data:", image_data[:10])  # Print first 10 bytes

    asyncio.run(main())