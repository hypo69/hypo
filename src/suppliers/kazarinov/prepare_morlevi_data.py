## \file ../src/suppliers/kazarinov/prepare_morlevi_data.py
# -*- coding: utf-8 -*-
#! /usr/share/projects/hypotez/venv/scripts python
"""! Module for handling Morlevi product data extraction and saving.

This module interacts with a web driver to scrape product details from given URLs, 
processes the data, and saves relevant product information, including images, locally.
"""

import asyncio
from pathlib import Path
from types import SimpleNamespace

import requests
from bs4 import BeautifulSoup
from lxml import etree

import header
from src import gs
from src.product.product_fields import ProductFields
from src.webdriver import Driver
from src.suppliers.morlevi.graber import async_grab_page
from src.utils.jjson import j_loads_ns, j_dumps
from src.utils.image import save_png
from src.utils import pprint
from src.logger import logger

locators = j_loads_ns(gs.path.src / 'suppliers' / 'morlevi' / 'locators' / 'product.json')


class ExecuteProducts:
    """! Handles Morlevi product extraction, parsing, and saving processes."""
    
    d:Driver
    base_path:Path
    def __init__(self, d: Driver):
        """Initializes the driver and base path."""
        self.d = d
        self.base_path = gs.path.data / 'kazarinov' / 'mexironim' / gs.now

    async def prepare_morlevi_data(self, price: str, urls: list | str) -> list[dict] | None:
        """Prepares product data by parsing and saving product pages.

        Args:
            price (str): Price to assign or process.
            urls (list | str): URL(s) to be processed.

        Returns:
            list[dict] | None: List of product data if successful, otherwise None.
        """
        product_fields = await self.grab_morlevi_pages(urls)
        if not product_fields:
            return

        product_fields = product_fields if isinstance(product_fields, list) else [product_fields]

        # Save products and log errors, if any
        tasks = [self.save_product(product) for product in product_fields]
        results = await asyncio.gather(*tasks, return_exceptions=True)

        for product, result in zip(product_fields, results):
            if isinstance(result, Exception) or not result:
                logger.error(f"Error in creatong product:\n{pprint(product)}")
                ...
        return product

    async def grab_morlevi_pages(self, urls: list | str) -> list | None:
        """Parses the contents of the given URLs.

        Args:
            urls (list | str): A single URL or a list of URLs to parse.

        Returns:
            list | None: Parsed product data or `None` if parsing fails.
        """
        if isinstance(urls, str):
            urls = [urls]

        async def _grab_page(url: str):
            if url.startswith(('https://morlevi.co.il', 'https://www.morlevi.co.il')):
                self.d.get_url(url)
                self.d.wait(1)
                return await async_grab_page(self.d)

        tasks = [asyncio.create_task(_grab_page(url)) for url in urls]
        product_fields = await asyncio.gather(*tasks, return_exceptions=True)

        # Filter out any exceptions and return valid results
        return [p for p in product_fields if not isinstance(p, Exception) and p]

    async def convert_product_fields(self, f: ProductFields) -> dict:
        """Prepares a product dictionary from product field data.

        Args:
            f (ProductFields): Object containing product field data.

        Returns:
            dict: Product information including title, description, ID, and image path.
        """
        image_path = self.base_path / 'images' / f'{f.id_product}.png'
        await save_png(f.default_image_url, image_path)

        return {
            'product_title': f.name['language'][0]['value'].strip(),
            'product_id': f.id_product,
            'product_description': f.description['language'][0]['value'].strip(),
            'image_local_saved_path': str(image_path),
        }

    async def save_product(self, product_fields: ProductFields) -> SimpleNamespace | None:
        """Saves the product data to storage.

        Args:
            product (ProductFields): Object containing product data.

        Returns:
            bool: `True` if the product was saved successfully, otherwise `False`.
        """
        product_data = await self.convert_product_fields(product_fields)
        product_ns: SimpleNamespace = SimpleNamespace(**product_data)
        product_path = self.base_path / 'products' / f"{product_fields.id_product}.json"

        j_dumps(product_ns, product_path)
        return product_ns 
