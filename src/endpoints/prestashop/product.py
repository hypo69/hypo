## \file /src/endpoints/prestashop/product.py
# -*- coding: utf-8 -*-
#! .pyenv/bin/python3

"""
.. module:: src.endopoints.prestashop.product 
    :platform: Windows, Unix
    :synopsis: Interaction between website, product, and PrestaShop.
Defines the behavior of a product in the project.

"""
import asyncio
from dataclasses import dataclass, field
from typing import List, Dict, Any, Optional

import header
from src import gs
from src.endpoints.prestashop.api import PrestaShop
from src.endpoints.prestashop.product_fields import ProductFields
from src.utils.convertors.any import any2dict
from src.utils.printer import pprint as print
from src.logger.logger import logger




class PrestaProduct(PrestaShop):
    """Manipulations with the product.
    Initially, I instruct the grabber to fetch data from the product page,
    and then work with the PrestaShop API.
    """

    def __init__(self, api_key:str, api_domain:str, *args, **kwargs):
        """
        Initializes a Product object.

        """
                                    
        super().__init__(self, api_key = api_key ,api_domain = api_domain, *args, **kwargs)


    def add_new_product(self, f: ProductFields) -> dict:
        """
        Add a new product to PrestaShop.

        Args:
            f (ProductFields): An instance of the ProductFields data class containing the product information.

        Returns:
            ProductFields | None: Returns the `ProductFields` object with `id_product` set, if the product was added successfully, `None` otherwise.
        """
        # Convert the ProductFields object to a dictionary
        presta_product_dict:dict = f.to_dict()

        response = self.create('products', presta_product_dict)
        if response:
            try:
                f.id_product = int(response['product']['id'])
                logger.info(f"Product added: {presta_product_dict.get('name')}")
                return f
            except (KeyError, TypeError) as ex:
                logger.error(f"Ошибка при разборе ответа от сервера: {ex}", exc_info=True)
                return {}
        else:
            logger.error(f"Ошибка при добавлении товара:\n{print(print_data=presta_product_dict, text_color='yellow')}", exc_info=True)
            return {}




async def main():
    # Example usage
    product = PrestaProduct()
    product_fields = ProductFields(
        lang_index = 1,
        name='Test Product Async',
        price=19.99,
        description='This is an asynchronous test product.',
    )
    


    new_product = product.add_new_product(product_fields)
    if new_product:
        print(f'New product id = {new_product.id_product}')
    else:
        print(f'Error add new product')

    product.fetch_data_async()

if __name__ == '__main__':
    asyncio.run(main())