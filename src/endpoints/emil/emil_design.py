from __future__ import annotations
from typing import Optional
## \file /src/endpoints/emil/emil_design.py
# -*- coding: utf-8 -*-

#! venv/bin/python/python3.12

"""
.. module:: src.endpoints.emil 
	:platform: Windows, Unix
	:synopsis: Module for managing and processing images and promoting to Facebook and PrestaShop.

"""

import asyncio
import time
from pathlib import Path
from types import SimpleNamespace

import header

# Сторонние библиотеки
from src import gs, logger
from src.endpoints.prestashop import PrestaShopAsync

# Веб-драйверы
from src.webdriver.driver import Driver
from src.webdriver.chrome import Chrome
from src.webdriver.firefox import Firefox
# TODO: Add drivers e.g. Edge, crawlee_python, playwright

# AI модели
from src.ai.gemini import GoogleGenerativeAI
from src.ai.openai.model import OpenAIModel

# Обработка товаров
from src.product.product_fields import ProductFields

# Работа с соцсетями
from src.endpoints.advertisement.facebook.scenarios.post_message import (
    post_message,
    post_title,
    upload_media,
)

# Утилиты
from src.utils.file import read_text_file, save_text_file, get_filenames
from src.utils.jjson import j_loads, j_loads_ns, j_dumps
from src.utils.image import get_image_bytes, get_raw_image_data
from src.utils.convertors.ns import ns2dict

# Логирование
from src.logger.logger import logger


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
        

        # 1. Initialize the AI model with the system instructions

        system_instruction: str = Path( self.base_path  / 'instructions' / f'hand_made_furniture_{lang}.md' ).read_text(encoding='UTF-8')

        use_openai:bool = False
        if use_openai:
            self.openai = OpenAIModel(system_instruction = system_instruction, assistant_id = 'asst_uDr5aVY3qRByRwt5qFiMDk43')

        use_gemini:bool = True
        if use_gemini:
            self.gemini = GoogleGenerativeAI(
                    api_key= gs.credentials.gemini.emil ,                        
                    model_name = 'gemini-1.5-flash',
                    system_instruction = system_instruction,
                    generation_config = {'response_mime_type': 'application/json'}
                )


        # 2. Define paths for examples, images directory, and output file
        
        furniture_categories: str = Path( self.base_path  / 'categories' / 'main_categories_furniture.json' ).read_text(encoding='UTF-8').replace(r'\n','').replace(r'\t','')
        system_instruction += furniture_categories
        
        output_file: Path = ( self.data_path /  f"described_images_{lang}.json" )

        described_images_path:Path = self.data_path / 'described_images.txt'
        described_images:list = read_text_file(described_images_path, as_list=True) or []


        # 3. Define images paths
        images_dir = self.data_path  / 'images' / 'furniture_images'
        images_files_list: list = get_filenames( images_dir ) 

        # 4. Subtract described images from the list of all images
        images_to_process = [img for img in images_files_list if str(images_dir / img) not in described_images]


        # 5. Define output file
        output_json: Path = Path(self.data_path  / f'out_{gs.now}_{lang}.json')


        data: list = [] # <- список всех обработанных данных
        for img in images_to_process:
            
            print(f"starting process file {img}\nsleep for 20 sec")
            time.sleep(20)
            img_path = str(images_dir / img)  # Store the full path for saving


            # здесь два разных типа байтового собедржимого картинки. Если модель ругается на один, то можно вырать другой 
            
            # - using Pillow and returns its bytes in JPEG format
            img_bytes = get_image_bytes (images_dir / img)

            # - raw binary data of a file
            raw_img_data = get_raw_image_data (images_dir / img)
            
            response = await self.gemini.describe_image(image = raw_img_data, mime_type = 'image/jpeg', prompt = system_instruction)  

            if not response:
                ...
                continue

            # Process the response into a structured format
            res_ns: SimpleNamespace | list[SimpleNamespace] = j_loads_ns(response)
            res_ns: SimpleNamespace = res_ns[0] if isinstance(res_ns, list) else res_ns 

            setattr(res_ns, 'local_saved_image', str( Path(images_dir / img) ) )

            # append structured data to list of products
            data.append(res_ns)
            j_dumps(data, output_json)

            # Add the processed image path to the list and save to file
            described_images.append(img_path)
            save_text_file(described_images_path, described_images)

        


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

    async def upload_to_prestashop(self, products_list: Optional[ SimpleNamespace | list[SimpleNamespace] ]= None, lang: Optional [str] = None) -> bool:
        """
        Поднимаю на сервер изображения из сохраненного файла описаний.
        Файл описаний мне делает телеграм
        
        Upload product information to PrestaShop.

        This function initializes a product and PrestaShop instance for uploading data.
        """
        products_list: SimpleNamespace | list[SimpleNamespace] = products_list if products_list else  j_loads_ns(self.data_path / "out_250108230345305_he.json")

        ...
        
        lang_ns = j_loads_ns (self.base_path / 'shop_locales' / 'locales.json' )

        default_lang = lang or lang_ns.he


        # convert to ProductFields
        f:ProductFields = ProductFields()
        host = gs.credentials.presta.client.emil_design.api_domain
        api_key = gs.credentials.presta.client.emil_design.api_key
        presta = PrestaShopAsync(api_domain = host, api_key = api_key, default_lang = default_lang )

        for product_ns in products_list:
                                                                           
            # convert to prestashop fields
            f.name = product_ns.name
            f.id_category_default = product_ns.category
            f.id_supplier = 11366 #  https://docs.google.com/spreadsheets/d/14f0PyQa32pur-sW2MBvA5faIVghnsA0hWClYoKpkFBQ
            f.description = product_ns.description
            f.images_urls = product_ns.local_saved_image
            
            fields_dict:dict = j_dumps (f)            
            product_id = await presta.create('products', fields_dict)
            ...

        
        

if __name__ == "__main__":
    emil = EmilDesign()
    asyncio.run( emil.upload_to_prestashop() )

    #asyncio.run( emil.describe_images(lang='he')  )
    # emil.promote_to_facebook()