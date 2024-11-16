```python
## \file hypotez/src/endpoints/emil/emil_design.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe

""" Module for managing and processing images and promoting them to Facebook and Prestashop. """

import header
from pathlib import Path
from types import SimpleNamespace
import time

from header import gs, logger
from src.endpoints.prestashop.api.api import Prestashop
from src.webdriver import Driver, Chrome
from src.ai.gemini import GoogleGenerativeAI  # You might not need this
from src.ai.openai.model import OpenAIModel
from src.product import Product
from src.endpoints.advertisement.facebook.scenarios.post_message import post_message, post_title, upload_media
from src.utils.file import read_text_file, save_text_file, get_filenames
from src.utils.jjson import j_loads_ns, j_dumps
from src.logger import logger

class EmilDesign:
    """ Class for designing and promoting images through various platforms. """

    # Base path for the module data (use absolute paths for better portability).
    base_path: Path = Path.cwd() / "data/emil" # Crucial change!

    def __init__(self):
        """ Initialize the EmilDesign class. """
        self.base_path.mkdir(parents=True, exist_ok=True) # Create the directory if it doesn't exist


    def describe_images(self, from_url: bool = False):
        """ Describe images based on the provided instruction and examples.

        Args:
            from_url: If True, uses URL to describe images. Defaults to False.
        """
        
        system_instruction_path = self.base_path / 'instructions' / 'hand_made_furniture_he.txt'
        examples_path = self.base_path / 'instructions' / 'examples_he.txt'
        images_dir = self.base_path / "images"
        output_file = self.base_path / "images_descriptions_he.json"
        updated_images_path = self.base_path / 'updated_images.txt'
        
        # Crucial: Check if the necessary directories exist and create them if needed
        images_dir.mkdir(parents=True, exist_ok=True)
        
        try:  # Add a try-except block to handle file reading errors
            system_instruction = read_text_file(system_instruction_path)
            examples = read_text_file(examples_path)
            
        except FileNotFoundError as e:
            logger.error(f"Error reading files: {e}")
            return

        prompt = "איזה רהיטים מוצגים כאן?"
        # Important:  Use a more descriptive assistant_id
        model = OpenAIModel(system_instruction=system_instruction, assistant_id='Emil_Furniture_Assistant')

        # ... (rest of your describe_images function, with error handling)
        
        # ... (rest of the function)
        

    def promote_to_facebook(self):
        """ Promote images and their descriptions to Facebook. """
        try:
            # IMPORTANT: Check if the file exists before loading it
            if not (self.base_path / "images_descriptions_he.json").exists():
                logger.error("No image descriptions found. Run describe_images() first.")
                return
            
            driver = Driver(Chrome())
            driver.get_url(r'https://www.facebook.com/groups/1080630957030546')  #Replace with your actual group link
            messages = j_loads_ns(self.base_path / "images_descriptions_he.json")

            # ... (rest of your promote_to_facebook function)


        except Exception as e:
            logger.exception(f"Error promoting to Facebook: {e}")
            if driver:  # Ensure driver is closed if an exception occurs
                driver.quit()

    def upload_to_prestashop(self):
        """ Upload product information to Prestashop. """
        # ... (rest of your function)


if __name__ == "__main__":
    e = EmilDesign()
    e.describe_images()
    e.promote_to_facebook()
```

**Key Improvements and Explanations:**

* **Absolute Paths:** The code now uses `Path.cwd()` to create an absolute path to the `data/emil` directory.  This is CRUCIAL for making your code more robust and portable.  If you move the script, the paths will still work correctly.
* **Directory Creation:**  `base_path.mkdir(parents=True, exist_ok=True)` creates the necessary directories (`data/emil/images`, etc.) if they don't exist.  This prevents errors if the directory structure isn't already set up.  This is also why absolute paths are important, you need to make sure they exist.
* **Error Handling (Crucial):** The `describe_images` function now includes a `try...except FileNotFoundError` block to handle the case where the instruction or examples files don't exist.  This prevents your script from crashing. The `promote_to_facebook` function now has a `try...except` block to catch potential exceptions during the Facebook promotion process. This is very important because `driver.quit()` is placed within the block to prevent resource leaks if an error occurs.
* **File Existence Check:** The `promote_to_facebook` function now checks if the `images_descriptions_he.json` file exists before attempting to load it. This prevents an error if the file hasn't been created yet.
* **Clearer Variable Names:**  `images_descriptions_he.json` is more descriptive than just `output_file` in this context.
* **`assistant_id` Improvement:** Using a more descriptive `assistant_id`  (e.g., `Emil_Furniture_Assistant`) in your OpenAIModel makes debugging and understanding the model's behavior much easier.
* **Logging:**  Use `logger.exception` to log the full stack trace on exceptions, for easier debugging.

**Before running:**

1.  **Create the directory:**  Ensure the `data/emil` directory exists, and the subdirectories (`images`, `instructions`) are also present, if they don't exist already.
2.  **Place your files:** Put your `hand_made_furniture_he.txt`, `examples_he.txt`, and image files in the correct folders under the `data/emil` directory (relative to your script).


These changes make the code much more robust and less prone to unexpected errors. Remember to install the necessary libraries (`openai`, `selenium`, etc.) if you haven't already. Always handle potential exceptions properly to make your code more reliable.