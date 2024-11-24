## \file hypotez/src/endpoints/kazarinov/scenarios/scenario_pricelist.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
.. module: src.endpoints.kazarinov.scenarios 
	:platform: Windows, Unix
	:synopsis: Provides functionality for extracting, parsing, and processing product data from 
various suppliers. The module handles data preparation, AI processing, 
and integration with Facebook for product posting.

"""
MODE = 'dev'

import asyncio
import random
from pathlib import Path
from typing import Optional, List
from types import SimpleNamespace
from dataclasses import field

from src import gs
from src.product.product_fields import ProductFields
from src.webdriver import Driver
from src.ai.gemini import GoogleGenerativeAI
from src.endpoints.advertisement.facebook.scenarios import (
    post_message_title, upload_post_media, message_publish
)
from src.suppliers.morlevi.graber import Graber as MorleviGraber
from src.suppliers.ksp.graber import Graber as KspGraber
from src.suppliers.ivory.graber import Graber as IvoryGraber
from src.suppliers.grandadvance.graber import Graber as GrandadvanceGraber
from src.endpoints.kazarinov.react import ReportGenerator
from src.utils.jjson import j_loads_ns, j_dumps
from src.utils.file import read_text_file, save_text_file, recursively_get_file_path
from src.utils.image import save_png_from_url, save_png
from src.logger import logger

class Mexiron:
    """
    Handles suppliers' product extraction, parsing, and saving processes.
    
    Supported suppliers:
    - https://morlevi.co.il
    - https://ivory.co.il
    - https://ksp.co.il
    - https://grandadvance.co.il
    """

    # Class attributes
    driver: Driver
    export_path: Path
    mexiron_name: str
    price: float
    timestamp: str
    products_list: List = field(default_factory=list)
    model: GoogleGenerativeAI
    model_command:str
    def __init__(self, driver: Driver, mexiron_name: Optional[str] = None):
        """
        Initializes Mexiron class with required components.

        Args:
            d (Driver): Selenium WebDriver instance.
            mexiron_name (Optional[str]): Custom name for the Mexiron process.
        """
        self.timestamp = gs.now
        self.driver = driver
        self.mexiron_name = mexiron_name or self.timestamp
        self.export_path = gs.path.external_storage / 'kazarinov' / 'mexironim' / self.mexiron_name

        # Read system instructions for the AI model
       
        system_instruction:str = Path( gs.path.endpoints / 'kazarinov' / 'instructions' / 'system_instruction_mexiron.md').read_text(encoding='UTF-8')
        self.model_command:str = Path( gs.path.endpoints / 'kazarinov' / 'instructions' / 'command_instruction_mexiron.md').read_text(encoding='UTF-8')
        api_key:str = gs.credentials.gemini.kazarinov
        self.model = GoogleGenerativeAI(
            api_key=api_key,
            system_instruction=system_instruction,
            generation_config={'response_mime_type': 'application/json'}
        )

    async def run_scenario(
        self, 
        system_instruction: Optional[str] = None, 
        price: Optional[str] = None, 
        mexiron_name: Optional[str] = None, 
        urls: Optional[str | List[str]] = None
    ) -> bool:
        """
        Executes the scenario: parses products, processes them via AI, and stores data.

        Args:
            system_instruction (Optional[str]): System instructions for the AI model.
            price (Optional[str]): Price to process.
            mexiron_name (Optional[str]): Custom Mexiron name.
            urls (Optional[str | List[str]]): Product page URLs.

        Returns:
            bool: True if the scenario executes successfully, False otherwise.
        """
        urls_list = [urls] if isinstance(urls, str) else urls
        if not urls_list:
            logger.debug('No URLs provided for parsing.')
            ...
            return False

        product_fields_list = []
        products_list = []

        for url in urls_list:

            graber = self.get_graber_by_supplier_url(url)
            if not graber:
                ...
                continue

            try:
                self.driver.get_url(url)
                f = await graber.grab_page(self.driver)
            except Exception as ex:
                logger.debug(f'Failed to open page {url}.', ex)
                ...
                continue

            if not f:
                logger.debug(f'Failed to parse product fields for URL: {url}')
                ...
                continue

            product_data = await self.convert_product_fields(f)
            if not product_data:
                logger.debug(f'Failed to convert product fields: {product_data}')
                ...
                continue

            products_list.append(product_data)
            self.save_product_data(product_data)

        # AI processing
        ru, he = self.process_ai(products_list, price)
        if ru and he:
            self.create_report()
            self.post_facebook(ru)
            self.post_facebook(he)

        return True

    def get_graber_by_supplier_url(self, url: str):
        """
        Returns the appropriate graber for a given supplier URL.

        Args:
            url (str): Supplier page URL.

        Returns:
            Optional[object]: Graber instance if a match is found, None otherwise.
        """
        if url.startswith(('https://morlevi.co.il', 'https://www.morlevi.co.il')):
            return MorleviGraber(self.driver)
        if url.startswith(('https://ksp.co.il', 'https://www.ksp.co.il')):
            return KspGraber(self.driver)
        if url.startswith(('https://grandadvance.co.il', 'https://www.grandadvance.co.il')):
            return GrandadvanceGraber(self.driver)
        if url.startswith(('https://ivory.co.il', 'https://www.ivory.co.il')):
            return IvoryGraber(self.driver)
        logger.debug(f'No graber found for URL: {url}')
        return None

    async def convert_product_fields(self, f: ProductFields) -> dict:
        """
        Converts product fields into a dictionary.

        Args:
            f (ProductFields): Object containing parsed product data.

        Returns:
            dict: Formatted product data dictionary.
        """
        # image_path = self.export_path / 'images' / f'{f.id_product}.png'
        # await save_png(f.default_image_url, image_path)

        return {
            'product_title': f.name['language'][0]['value'].strip(),
            'product_id': f.id_product,
            'description_short': f.description_short['language'][0]['value'].strip(),
            'description': f.description['language'][0]['value'].strip(),
            'specification': f.specification['language'][0]['value'].strip(),
            #'local_saved_image': str(image_path),
        }

    def save_product_data(self, product_data: dict):
        """
        Saves individual product data to a file.

        Args:
            product_data (dict): Formatted product data.
        """
        file_path = self.export_path / 'products' / f"{product_data['product_id']}.json"
        j_dumps(product_data, file_path, ensure_ascii=False)



    def process_ai(self, products_list:str, attemts:int = 3) -> tuple | bool:
        """
        Processes the product list through the AI model.

        Args:
            products_list (list): List of product data dictionaries.
            price (Optional[str]): Price to include in the response.

        Returns:
            tuple: Processed response in `ru` and `he` formats.
        Notes:
            Модель может возвращать невелидный результат. В таком случае я переспрашиваю модель
        """
        ...
        if attemts < 1:
            return
        response = self.model.ask(self.model_command + products_list)
        if not response:
            logger.error("no response from gemini")
            ...
            return


        data: SimpleNamespace = j_loads_ns(response) # <- вернет False в случае ошибки

        if not data:
            logger.error(f"Error in data from gemini:{data}")
            ...
            self.process_ai(products_list,attemts - 1)

            if not j_dumps(data, base_path / 'ai' / f'{gs.now}.json', ensure_ascii=False): # <- певая проверка валидности полученных данных
                ...
                self.process_ai(products_list, attemts - 1)

        try:
            if hasattr(data,'ru'):
                ru:SimpleNamespace = data.ru
                if not ru:
                    ...
                    self.process_ai(products_list, attemts-1)
            else:
                ...
                self.process_ai(products_list, attemts-1)

            if hasattr(data,'he'):
                he:SimpleNamespace = data.he
                if not he:
                    ...
                    self.process_ai(products_list, attemts-1)
            else:
                ...
                self.process_ai(products_list, attemts-1)
            return ru, he
        except Exception as ex:
            logger.debug(f"ошибка словаря")
            ...
            return
