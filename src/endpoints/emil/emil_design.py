## \file ../src/suppliers/emil/emil_design.py
# -*- coding: utf-8 -*-
#! /usr/share/projects/hypotez/venv/scripts python
"""! Module for managing and processing images and promoting to Facebook and Prestashop. """

import header
from pathlib import Path
from types import SimpleNamespace
import time

from src import gs, logger
from src.endpoints.prestashop.api.api import Prestashop
from src.webdriver import Driver, Chrome
from src.ai.gemini import GoogleGenerativeAI
from src.ai.openai.model import OpenAIModel
from src.product import Product
from src.advertisement.facebook.scenarios.post_message import post_message, post_title, upload_media
from src.utils.file import read_text_file, save_text_file, get_filenames
from src.utils.jjson import j_loads_ns, j_dumps
from src.logger import logger

class EmilDesign:
    """! Class for designing and promoting images through various platforms. """

    # Base path for the module data
    base_path: Path = (
        gs.path.google_drive
        / "emil"
    )

    def __init__(self):
        """! Initialize the EmilDesign class. """
        ...

    def describe_images(self, from_url: str = False):
        """! Describe images based on the provided instruction and examples.

        Args:
            from_url (str, optional): If True, uses URL to describe images. Defaults to False.
        """
        ...

        # Define paths for system instructions, examples, images directory, and output file
        system_instruction_path: Path = (
            self.base_path 
            / 'instructions'
            / 'hand_made_furniture_he.txt'
        )

        examples_path: Path = ( 
            self.base_path 
            / 'instructions'
            / "examples_he.txt"
        )

        images_dir: Path = (
            self.base_path
            / "images"
        )

        output_file: Path = (
            self.base_path
            /  "images_descritions_he.json"
        )
        
        base_url: str = r'https://emil-design.com/img/images_emil/'
        trainig_data = read_text_file(system_instruction_path)

        updated_images_path: Path = self.base_path / 'updated_images.txt'
        
        system_instruction = read_text_file(system_instruction_path)
        examples = read_text_file(examples_path)
        
        # Prompt for the AI model
        prompt: str = "איזה רהיטים מוצגים כאן?"
        
        # Initialize the AI model with the system instructions
        model = OpenAIModel(system_instruction=system_instruction, assistant_id='asst_uDr5aVY3qRByRwt5qFiMDk43')
        
        # Ask the model to categorize examples
        response = model.ask(examples, "this is example for build categories")
        logger.info(response)

        updated_images_list: list = read_text_file(updated_images_path, as_list=True) or []

        images_path_list: list = get_filenames(images_dir)
        data: list = []
        
        for image_path in images_path_list:
            if image_path in updated_images_list:
                continue

            # Describe the image either from URL or local file
            if from_url:
                response = model.describe_image(str(base_url + image_path), prompt, system_instruction)  # <- url
            else:
                response = model.describe_image(images_dir / image_path, prompt, system_instruction)  # <- local file

            if not response:
                continue

            # Process the response into a structured format
            res_ns: SimpleNamespace = j_loads_ns(response)
            setattr(res_ns, 'local_saved_image', str(Path(images_dir / image_path)))
            data.append(res_ns)
            j_dumps(data, output_file)
            updated_images_list.append(image_path)
            save_text_file(updated_images_list, updated_images_path)
            logger.info(response)
            # logger.debug("going sleep", None, False)
            # time.sleep(20)
            ...

    def promote_to_facebook(self):
        """! Promote images and their descriptions to Facebook.

        This function logs into Facebook and posts messages derived from the image descriptions.
        """
        d = Driver(Chrome)
        d.get_url(r'https://www.facebook.com/groups/1080630957030546')
        messages: SimpleNamespace | list = j_loads_ns(self.base_path / "images_descritions_he.json")
        
        for m in messages:
            message: SimpleNamespace = SimpleNamespace() 
            setattr(message, 'title', f"{m.parent}\n{m.category}")
            setattr(message, 'description', m.description)
            message.products = SimpleNamespace()
            setattr(message.products, 'local_saved_image', [m.local_saved_image])
           
            post_message(d, message, without_captions=True)
            ...

    def upload_to_prestashop(self):
        """! Upload product information to Prestashop.

        This function initializes a product and Prestashop instance for uploading data.
        """
        p = Product()
        presta = Prestashop()
        

if __name__ == "__main__":
    e = EmilDesign()
    # e.describe_images()
    # e.promote_to_facebook()
