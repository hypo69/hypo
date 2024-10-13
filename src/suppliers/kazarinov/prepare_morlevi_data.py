## \file src/suppliers/aliexpress/gui/category.py
# -*- coding: utf-8 -*-
#! /usr/share/projects/hypotez/venv/scripts python
"""! Module for handling Morlevi product data extraction and saving. 

This module interacts with a web driver to scrape product details from given URLs, processes the data, and saves relevant product information, including images, locally.
"""

import asyncio
import requests
from bs4 import BeautifulSoup
from types import SimpleNamespace
from lxml import etree
from pathlib import Path

import header
from src import gs
from src.product.product_fields import ProductFields
from src.webdriver import Driver, Chrome
from src.suppliers.morlevi.graber import async_grab_page
from src.utils.jjson import j_loads, j_loads_ns, j_dumps
from src.utils.image import save_png_from_url, save_png
from src.utils import pprint
from src.logger import logger

locators = j_loads_ns(gs.path.src / 'suppliers' / 'morlevi' / 'locators' / 'product.json')


class ExecuteProducts:
    """! Handles Morlevi product extraction, parsing, and saving processes."""
    d:Driver
    base_path:Path
    def __init__(self, d:Driver):
        """"""
        self.d = d
        self.base_path =  gs.path.data / 'kazarinov' / 'mexironim' / gs.now
    
    async def prepare_morlevi_data(self, price: str, urls: list | str) -> list[dict] | None:
        """Prepares product data by parsing and saving product pages.

        Args:
            driver (Driver): Web driver instance to interact with the browser.
            price (str): Price to assign or process.
            urls (list | str): URL(s) to be processed.

        Returns:
            bool: `True` if all operations succeed, otherwise `False`.
        """
        ...
        product_fields = await self.parse_morlevi_pages(urls)
        if not product_fields:
            return 

        # Если product_fields — не список, преобразуем его в список для единообразной обработки
        product_fields = product_fields if isinstance(product_fields, list) else [product_fields]

        # Сохраняем все продукты в одном цикле
        for product in product_fields:
            if not self.save_product(product):
                logger.error(f"Ошибка сохаранения товара в файл\n{pprint(product)}")

        return product_fields


    
    async def parse_morlevi_pages(self, urls: list | str) -> list | None:
        """Parses the contents of the given URLs.

        Args:
            urls (list | str): A single URL or a list of URLs to parse.

        Returns:
            list | None: Parsed product data or `None` if parsing fails.
        """

        async def parse_url(self, url: str):
            """Parses a single URL if it belongs to Morlevi's domain.

            Args:
                url (str): URL to be parsed.

            Returns:
                dict | None: Parsed product data or `None` if the URL is invalid.
            """
            if not (url.startswith('https://morlevi.co.il') or url.startswith('https://www.morlevi.co.il')):
                return 

            self.d.get_url(url)
            self.d.wait(1)
            return await async_grab_page(self.d)
            

        tasks = [asyncio.create_task(parse_url(url)) for url in urls]
        product_fields = await asyncio.gather(*tasks)
        return product_fields if any(product_fields) else None

    
    async def prepare_product_fields(self, f: ProductFields) -> dict:
        """Prepares a product dictionary from product field data.

        Args:
            f (ProductFields): Object containing product field data.

        Returns:
            dict: Product information including title, description, ID, and image path.
        """
        default_image_url = f.default_image_url  # Byte stream of PNG screenshot.
        image_local_saved_path = await save_png(
            default_image_url, 
            self.base_path / 'images' / f'{gs.now}.png'
        )

        product = {
            'product_title': f.name['language'][0]['value'].strip(),
            'product_id': f.id_supplier,
            'product_description': f.description['language'][0]['value'].strip(),
            'image_local_saved_path': image_local_saved_path
        }
        return product

    
    async def save_product(self, product: dict) -> bool:
        """Saves the product data to storage.

        Args:
            product (dict): Dictionary containing product data.

        Returns:
            bool: `True` if the product was saved successfully, otherwise `False`.
        """
        if j_dumps(product,  self.base_path / 'products' / f"{product['product_id']}.json"):
            return True
        return False