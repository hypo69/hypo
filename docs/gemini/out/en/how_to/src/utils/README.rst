rst
How to Use Tiny Utils
========================================================================================

Description
-------------------------
Tiny Utils is a utility library containing various helper functions for common tasks, such as data format conversion, text and file manipulation, string operations, date-time formatting, image processing, and more.  It's organized into modules for easy access to specific functionalities.  This document provides an overview and usage examples for the library.

Execution steps
-------------------------
1. **Clone the repository:** Use `git clone https://github.com/hypo69/tiny-utils.git` to download the project to your local machine.

2. **Navigate to the project directory:** Use `cd tiny_utils`.

3. **Install the necessary dependencies:** Run `pip install -r requirements.txt` to install all required packages.

4. **Import the desired module:**  Import the module that contains the function you want to use.  For example, to use the `text2png` function, import it from the `convertors` module: `from tiny_utils.convertors import text2png`.

5. **Call the function:** Follow the function's parameters and arguments, as documented in the module's description or the Tiny Utils Wiki.

6. **Process the result:** Handle the output of the function as appropriate for your application. For example, if `text2png.convert()` returns a path to an image file, you might want to display the image or further process it.

Usage example
-------------------------
.. code-block:: python

    from tiny_utils.convertors import text2png

    text_to_convert = "Hello, World!"
    output_filepath = "output_image.png"

    try:
        text2png.convert(text_to_convert, output_filepath)
        print(f"Image '{output_filepath}' created successfully.")
    except Exception as e:
        print(f"Error creating image: {e}")