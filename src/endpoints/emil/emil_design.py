from __future__ import annotations
## \file hypotez/src/endpoints/emil/emil_design.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
.. module:: src.endpoints.emil 
	:platform: Windows, Unix
	:synopsis: Module for managing and processing images and promoting to Facebook and PrestaShop.

"""

import asyncio
from pathlib import Path
from types import SimpleNamespace
import time

import header
from src import gs, logger
from src.endpoints.prestashop.api.api import PrestaShop

from src.webdriver.driver import Driver
from src.webdriver.chrome import Chrome
from src.webdriver.firefox import Firefox
## Add  drivers e.g. Fdge, crawlee_python, playwright

from src.ai.gemini import GoogleGenerativeAI
from src.ai.openai.model import OpenAIModel
from src.product.product_fields import ProductFields

from src.endpoints.advertisement.facebook.scenarios.post_message import post_message, post_title, upload_media
from src.utils.file import read_text_file, save_text_file, get_filenames
from src.utils.jjson import j_loads_ns, j_dumps
from src.logger.logger import logger
from src.utils.image import get_image_bytes

class EmilDesign:
    """ Class for designing and promoting images through various platforms. """

    # ---------------------------------
    ENDPOINT:str = 'emil'
    # ---------------------------------

    gemini:'GoogleGenerativeAI'
    openai:'OpenAIModel'

    base_path:Path = gs.path.endpoints / ENDPOINT
    config:SimpleNamespace = j_loads_ns( base_path / f'{ENDPOINT}.json')
    data_path:Path = getattr( gs.path , config.storage , 'external_storage')  / ENDPOINT
    


    def __init__(self):
        """ Initialize the EmilDesign class. """
        ...

    async def describe_images(self, lang:str):
        """ Describe images based on the provided instruction and examples.

        Args:
            from_url (str, optional): If True, uses URL to describe images. Defaults to False.
        """
        ...

        # 1. Define paths for system instructions, examples, images directory, and output file
        system_instruction: str = Path( self.base_path  / 'instructions' / f'hand_made_furniture_{lang}.md' ).read_text(encoding='UTF-8')
        furniture_categories: str = Path( self.base_path  / 'categories' / 'main_categories_furniture.json' ).read_text(encoding='UTF-8').replace(r'\n','').replace(r'\t','')
        system_instruction += furniture_categories
        examples:str =  Path( self.base_path / 'instructions' / f'examples_{lang}.md' ).read_text(encoding='UTF-8')
        output_file: Path = ( self.data_path /  f"images_descritions_{lang}.json" )

        # 2. Initialize the AI model with the system instructions
        use_openai:bool = False
        if use_openai:
            self.openai = OpenAIModel(system_instruction = system_instruction, assistant_id='asst_uDr5aVY3qRByRwt5qFiMDk43')

        use_gemini:bool = True
        if use_gemini:
            self.gemini = GoogleGenerativeAI(
                    api_key= gs.credentials.gemini.emil ,
                    system_instruction=system_instruction,
                    generation_config={'response_mime_type': 'application/json'}
                )
        


        # 3. Define images paths
        images_dir = self.data_path  / 'images' / 'furniture_images'
        images_files_list: list = get_filenames( images_dir )

        # 4. Define output file
        output_json: Path = Path(self.data_path  / f'out_{gs.now}_{lang}.json')


        data: list = [] # <- список всех обработанных данных
        for img in images_files_list:
            prompt = Path(self.base_path / 'instructions' / f'describe_image_command_{lang}.md').read_text(encoding='UTF-8')
            img_data = get_image_bytes(images_dir / img)
            response = await self.gemini.chat(img_data, prompt = prompt)  

            if not response:
                ...
                continue
            logger.info(response)
            ...
            # Process the response into a structured format
            res_ns: SimpleNamespace = j_loads_ns(response)
            
            setattr(res_ns, 'local_saved_image', str( Path(images_dir / img) ) )
            data.append(res_ns)
            j_dumps(data, output_json)
            #updated_images_list.append(image_path)
            #save_text_file(updated_images_list, updated_images_path)
            
            # logger.debug("going sleep", None, False)
            # time.sleep(20)
            ...

    async def promote_to_facebook(self):
        """ Promote images and their descriptions to Facebook.

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

    async def upload_to_prestashop(self):
        """
        Поднимаю на сервер изображения из сохраненного файла описаний.
        Файл описаний мне делает телеграм
        
        Upload product information to PrestaShop.

        This function initializes a product and PrestaShop instance for uploading data.
        """
        products_list: SimpleNamespace | list[SimpleNamespace] = j_loads_ns(self.data_path / "images_descritions_he.json")
        ...
        # convert to ProductFields
        f:ProductFields = ProductFields()
        for product_ns in products_list:
            f.name 
        
        

if __name__ == "__main__":
    emil = EmilDesign()
    #emil.upload_to_prestashop()
    asyncio.run( emil.describe_images(lang='he')  )
    # emil.promote_to_facebook()
