rst
How to use Tiny Utils
========================================================================================

Description
-------------------------
Tiny Utils is a utility library providing a set of lightweight helper functions for various common tasks.  It includes utilities for data format conversion, text and file processing, string operations, date and time formatting, image processing, and more. The library is organized into modules for easy access to specific functionalities. This document provides instructions on how to use specific modules within the library, taking `text2png.py` as an example.

Execution steps
-------------------------
1. **Install Tiny Utils:** Clone the repository and install the required dependencies.  This example requires `requirements.txt` as specified in the README.

2. **Import the necessary module:** Import the desired module into your Python script. For example, to use the `text2png` module:

   ```python
   from tiny_utils.convertors import text2png
   ```
3. **Prepare input data:** Define the text string you want to convert.

   ```python
   text_to_convert = "Hello, world!"
   ```
4. **Define output parameters:** Specify the output file name, path, and potentially other parameters like image dimensions or quality.

   ```python
   output_filename = "output.png"
   output_path = "output_image/" # Ensure the path exists
   ```

5. **Call the conversion function:** Call the `text2png` function, providing the input text, output file name, and other parameters.
   ```python
   text2png.convert_to_png(text_to_convert, output_filename, output_path)
   ```
6. **Verify the output:** Check the generated PNG file at the specified output path to ensure the conversion was successful.

   ```python
   import os
   if os.path.exists(os.path.join(output_path, output_filename)):
       print(f"Image '{output_filename}' created successfully.")
   else:
       print(f"Error: Image '{output_filename}' not found.")
   ```

Usage example
-------------------------
.. code-block:: python

    from tiny_utils.convertors import text2png

    text_to_convert = "This is a sample text."
    output_filename = "sample_image.png"
    output_path = "output_images/"

    # Create output directory if it doesn't exist
    import os
    os.makedirs(output_path, exist_ok=True)

    text2png.convert_to_png(text_to_convert, output_filename, output_path)


    import os
    if os.path.exists(os.path.join(output_path, output_filename)):
        print(f"Image '{output_filename}' created successfully.")
    else:
        print(f"Error: Image '{output_filename}' not found.")