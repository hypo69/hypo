## \file /src/endpoints/emil/emil_design.py
# -*- coding: utf-8 -*-
#! .pyenv/bin/python3

"""
.. module:: src.endpoints.emil 
	:platform: Windows, Unix
	:synopsis: Module for managing and processing images and promoting to Facebook and PrestaShop.

"""

import os
import asyncio
import time
from pathlib import Path
from types import SimpleNamespace
from typing import Optional, List
from dataclasses import dataclass, field

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

from src import USE_ENV # <- True - использую переменные окружения, False - использую параметры из keepass

class Config:

    ENDPOINT: str = 'emil'
    MODE:str = 'dev'
    POST_FORMAT = 'XML'
    API_DOMAIN:str = ''
    API_KEY:str = ''

    if USE_ENV:
        from dotenv import load_dotenv
        load_dotenv()
        API_DOMAIN = os.getenv('HOST')
        API_KEY = os.getenv('API_KEY')

    elif MODE == 'dev':
        API_DOMAIN = gs.credentials.presta.client.dev_emil_design.api_domain
        API_KEY = gs.credentials.presta.client.dev_emil_design.api_key

    elif MODE == 'dev8':
        API_DOMAIN = gs.credentials.presta.client.dev8_emil_design.api_domain
        API_KEY = gs.credentials.presta.client.dev8_emil_design.api_key

    else:
        API_DOMAIN = gs.credentials.presta.client.emil_design.api_domain
        API_KEY = gs.credentials.presta.client.emil_design.api_key

class EmilDesign:
    """Dataclass for designing and promoting images through various platforms."""

    gemini: Optional[GoogleGenerativeAI] = None
    openai: Optional[OpenAIModel] = None
    base_path: Path = gs.path.endpoints / Config.ENDPOINT
    config: SimpleNamespace = j_loads_ns(base_path / f'{Config.ENDPOINT}.json')
    data_path: Path = getattr(gs.path, config.storage, 'external_storage') / Config.ENDPOINT
    gemini_api: str = os.getenv('GEMINI_API') if USE_ENV else gs.credentials.gemini.emil
    presta_api: str = os.getenv('PRESTA_API') if USE_ENV else gs.credentials.presta.client.emil_design.api_key
    presta_domain: str = os.getenv('PRESTA_URL') if USE_ENV else gs.credentials.presta.client.emil_design.api_domain

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
            
            logger.info(f"Starting process file {img}\n")
            
            raw_img_data = get_raw_image_data(images_dir / img)
            response = self.gemini.describe_image(image=raw_img_data, mime_type='image/jpeg', prompt = prompt)
            ...
            if not response:
                logger.debug(f"Failed to get description for {img}")
                ...
            else:
                response_dict: dict = j_loads(response)[0] if isinstance(j_loads(response), list) else j_loads(response)
                response_dict['local_image_path'] = str(images_dir / img)
                j_dumps(response_dict, self.data_path / f'{img}.json')
                # Список уже обработанных изображений
                described_images.append(str(images_dir / img))
                save_text_file(described_images_path, described_images)
                
                
            time.sleep(15) # Задержка между запросами

    async def promote_to_facebook(self):
        """Promote images and their descriptions to Facebook."""
        d = Driver(Chrome)
        d.get_url(r'https://www.facebook.com/groups/1080630957030546')
        messages = j_loads_ns(self.base_path / "images_descritions_he.json")
        
        for m in messages:
            message = SimpleNamespace(title=f"{m.parent}\n{m.category}", description=m.description, products=SimpleNamespace(local_image_path=[m.local_image_path]))
            post_message(d, message, without_captions=True)

    def upload_described_products_to_prestashop(self, 
                                                      products_list: Optional[List[SimpleNamespace]] = None, 
                                                      lang: Optional[str] = None,
                                                      *args, **kwards) -> bool:
        """Upload product information to PrestaShop."""
        json_files_list:list[str] = get_filenames_from_directory(self.data_path, ext='json')
        products_list:list[SimpleNamespace] = [j_loads_ns(self.data_path / f) for f in json_files_list]
        lang:str = lang or 'he'
        host:str = gs.credentials.presta.client.emil_design.api_domain if USE_ENV else os.getenv('HOST')
        api_key:str = gs.credentials.presta.client.emil_design.api_key if USE_ENV else os.getenv('API_KEY')


        # DEVELOPMENT ENVIRONMENT !!!
        """Список доменов для разных окружений
        dev - prestashop 1.7 https://dev.emil-design.com/api
        dev8 - prestashop 8  https://dev8.emil-design.com/api
        """
        SUB_DOMAIN: str = 'prod' # prod | dev | dev8
        host:str=''
        api_key:str=''

        if SUB_DOMAIN == 'dev8':
            host = gs.credentials.presta.client.dev8_emil_design.api_domain
            api_key = gs.credentials.presta.client.dev8_emil_design.api_key

        elif SUB_DOMAIN == 'dev':
            host = gs.credentials.presta.client.dev_emil_design.api_domain
            api_key = gs.credentials.presta.client.dev_emil_design.api_key
        
            ... # другие окружения 

        elif SUB_DOMAIN == 'prod':
            host = gs.credentials.presta.client.emil_design.api_domain
            api_key = gs.credentials.presta.client.emil_design.api_key

        if not host or not api_key:
            logger.error("PrestaShop credentials not found.", None, False)
            ...
            return False

        p:PrestaProduct = PrestaProduct(api_domain=host, api_key=api_key)

        """Важно! При загрузке товаров в PrestaShop, необходимо указать язык, на котором будут отображаться названия и характеристики товара.
        в данном случае, язык по умолчанию - иврит (he), но также можно указать английский (en) или русский (ru)
        индексы могут меняться в зависимости от настроек магазина. Обычно я выставляю индекс `1` для английского, `2` для иврита и `3` для русского.
        таблица с индексами для` emil-design.com` находится в файле `locales.json` в папке `shop_locales`
        """
        lang_ns: SimpleNamespace = j_loads_ns(Path(__root__ , 'src' , 'endpoints' , ENDPOINT , 'shop_locales' , 'locales.json'))
        lang_index = getattr(lang_ns, lang) 

        for product_ns in products_list:
            f:ProductFields = ProductFields( lang_index )
            f.name=product_ns.name
            f.description = product_ns.description
            f.price = '100'
            f.id_category_default=product_ns.id_category_default
            f.additional_category_append(product_ns.id_category_parent)
            f.id_supplier = 11366
            f.local_image_path=product_ns.local_image_path
            p.add_new_product(f)
            

if __name__ == "__main__":
    emil = EmilDesign()
    emil.upload_described_products_to_prestashop(lang='he')
    #asyncio.run(emil.upload_described_products_to_prestashop_async(lang='he'))
    #emil.describe_images('he')

