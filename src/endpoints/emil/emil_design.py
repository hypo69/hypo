## \file /src/endpoints/emil/emil_design.py
# -*- coding: utf-8 -*-
#! .pyenv/bin/python3

"""
.. module:: src.endpoints.emil 
	:platform: Windows, Unix
	:synopsis: Module for managing and processing images and promoting to Facebook and PrestaShop.

"""
from __future__ import annotations
import os
import asyncio
import time
from pathlib import Path
from types import SimpleNamespace
from typing import Optional, List
from dotenv import load_dotenv
from dataclasses import dataclass, field

load_dotenv()
import header
from header import __root__

# External modules
from src import gs
from src.webdriver.driver import Driver
from src.webdriver.chrome import Chrome
from src.ai.gemini import GoogleGenerativeAI
from src.ai.openai.model import OpenAIModel
from src.endpoints.prestashop.product import PrestaProduct
from src.endpoints.prestashop.language import PrestaLanguage
from src.endpoints.prestashop.product_fields import ProductFields
from src.endpoints.advertisement.facebook.scenarios.post_message import (
    post_message,
)
from src.utils.file import read_text_file, save_text_file, get_filenames_from_directory
from src.utils.jjson import j_loads, j_loads_ns, j_dumps
from src.utils.image import get_image_bytes, get_raw_image_data
from src.logger.logger import logger

# ---------------------------------
ENDPOINT: str = 'emil'
USE_ENV: bool = True

class EmilDesign:
    """Dataclass for designing and promoting images through various platforms."""

    gemini: Optional[GoogleGenerativeAI] = None
    openai: Optional[OpenAIModel] = None
    base_path: Path = gs.path.endpoints / ENDPOINT
    config: SimpleNamespace = j_loads_ns(base_path / f'{ENDPOINT}.json')
    data_path: Path = getattr(gs.path, config.storage, 'external_storage') / ENDPOINT
    gemini_api: str = os.getenv('GEMINI_API') if USE_ENV else gs.credentials.gemini.emil
    presta_api: str = os.getenv('PRESTA_API') if USE_ENV else gs.credentials.prestashop.emil_design.api_key
    presta_url: str = os.getenv('PRESTA_URL') if USE_ENV else gs.credentials.prestashop.emil_design.url

    def describe_images(self, 
                              lang: str,
                              models:dict = {'gemini': {'model_name':'gemini-1.5-flash'}, 
                                             'openai': {'model_name':'gpt-4o-mini',
                                                        'assistant_id':'asst_uDr5aVY3qRByRwt5qFiMDk43'}}):
        """Describe images based on the provided instruction and examples."""
        system_instruction = Path(self.base_path / 'instructions' / f'system_instruction.{lang}.md').read_text(encoding='UTF-8')
        prompt = Path(self.base_path / 'instructions' / f'hand_made_furniture.{lang}.md').read_text(encoding='UTF-8')
        furniture_categories = Path(self.base_path / 'categories' / 'main_categories_furniture.json').read_text(encoding='UTF-8').replace(r'\n', '').replace(r'\t', '')
        system_instruction += furniture_categories + prompt

        output_json = self.data_path / f'out_{gs.now}_{lang}.json'
        described_images_path = self.data_path / 'described_images.txt'
        described_images: list = read_text_file(described_images_path, as_list=True) or []
        images_dir = self.data_path / 'images' / 'furniture_images'
        images_files_list: list = get_filenames_from_directory(images_dir)
        images_to_process = [img for img in images_files_list if str(images_dir / img) not in described_images]

        use_openai: bool = False
        if use_openai:
            self.openai = OpenAIModel(system_instruction=system_instruction, 
                                      model_name= models['openai']['model_name'],
                                      assistant_id=models['openai']['assistant_id'])

        use_gemini: bool = True
        if use_gemini:
            self.gemini = GoogleGenerativeAI(
                api_key=self.gemini_api,
                model_name= models['gemini']['model_name'],
                system_instruction=system_instruction,
                generation_config={'response_mime_type': 'application/json'}
            )

        for img in images_to_process:
            print(f"Starting process file {img}\n")
            
            raw_img_data = get_raw_image_data(images_dir / img)
            response = self.gemini.describe_image(image=raw_img_data, mime_type='image/jpeg', prompt = prompt)

            if not response:
                logger.debug(f"Failed to get description for {img}")
            else:
                res_ns: SimpleNamespace = j_loads_ns(response)[0] if isinstance(j_loads_ns(response), list) else j_loads_ns(response)
                setattr(res_ns, 'local_image_path', str(images_dir / img))
                described_images.append(str(images_dir / img))
                j_dumps(described_images, described_images_path)
                j_dumps([res_ns], output_json)
                
            time.sleep(15)

    async def promote_to_facebook(self):
        """Promote images and their descriptions to Facebook."""
        d = Driver(Chrome)
        d.get_url(r'https://www.facebook.com/groups/1080630957030546')
        messages = j_loads_ns(self.base_path / "images_descritions_he.json")
        
        for m in messages:
            message = SimpleNamespace(title=f"{m.parent}\n{m.category}", description=m.description, products=SimpleNamespace(local_image_path=[m.local_image_path]))
            post_message(d, message, without_captions=True)

    async def upload_described_products_to_prestashop(self, products_list: Optional[List[SimpleNamespace]] = None, lang: Optional[str] = None) -> bool:
        """Upload product information to PrestaShop."""
        products_list_file = self.data_path / "out_250108230345305_he.json"
        products_list = products_list if products_list else j_loads_ns(products_list_file)

        host = gs.credentials.presta.client.emil_design.api_domain if USE_ENV else os.getenv('HOST')
        api_key = gs.credentials.presta.client.emil_design.api_key if USE_ENV else os.getenv('API_KEY')
        MODE: str = 'dev8'

        if MODE == 'dev8':
            host = gs.credentials.presta.client.dev8_emil_design.api_domain
            api_key = gs.credentials.presta.client.dev8_emil_design.api_key

        p = PrestaProduct(api_domain=host, api_key=api_key)
        lang_ns = j_loads_ns(__root__ / 'src' / 'endpoints' / ENDPOINT / 'shop_locales' / 'locales.json')
        lang_index = getattr(lang_ns, lang)

        for product_ns in products_list:
            f = ProductFields(lang_index=lang_index or lang_ns.he)
            f.name=product_ns.name,
            f.description=product_ns.description
            f.price=100,
            f.id_category_default=product_ns.id_category_default,
            f.additional_category_append(product_ns.id_category_parent)
            f.id_supplier = 11366
            f.local_image_path=product_ns.local_image_path
            p.add_new_product(f)

if __name__ == "__main__":
    emil = EmilDesign()
    #asyncio.run(emil.upload_described_products_to_prestashop(lang='he'))
    emil.describe_images('he')

