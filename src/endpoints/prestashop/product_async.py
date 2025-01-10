
# -*- coding: utf-8 -*-
"""
.. module:: src.product.product 
    :platform: Windows, Unix
    :synopsis: Interaction between website, product, and PrestaShop.
Defines the behavior of a product in the project.

"""
import asyncio
from dataclasses import dataclass, field
from typing import List, Dict, Any, Optional

import header
from src import gs
from src.endpoints.prestashop import PrestaShopAsync, PrestaCategoryAsync

from src.endpoints.prestashop.product_fields import ProductFields
from src.utils.convertors.any import any2dict
from src.utils.printer import pprint as print
from src.logger.logger import logger




class ProductAsync(PrestaShopAsync, PrestaCategoryAsync):
    """Manipulations with the product.
    Initially, I instruct the grabber to fetch data from the product page,
    and then work with the PrestaShop API.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes a Product object.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        PrestaShopAsync.__init__(self, *args, **kwargs)
        PrestaCategoryAsync.__init__(self, *args, **kwargs)



    async def add_new_product(self, f: ProductFields) -> ProductFields | None:
        """
        Add a new product to PrestaShop.

        Args:
            f (ProductFields): An instance of the ProductFields data class containing the product information.

        Returns:
            ProductFields | None: Returns the `ProductFields` object with `id_product` set, if the product was added successfully, `None` otherwise.
        """

        f.additional_categories = self.get_parent_categories_list(f.id_category_default)
        f_dict: dict = any2dict(f)
        
        new_f:ProductFields = await self.create('products', f_dict)

        if not new_f:
            logger.error(f"Товар не был добавлен в базу данных Presyashop")
            ...
            return
        self.create_binary(f'images/products/{new_f.id}' f.local_image_path ,)


    # Example of async method, if necessary
    async def fetch_data_async(self) -> None:
         """
         Simulates fetching data asynchronously.
         """
         await asyncio.sleep(1) # Simulate async IO
         logger.info(f"Async data fetching completed")


async def main():
    # Example usage
    product = Product()
    product_fields = ProductFields(
        lang_index = 1,
        name='Test Product Async',
        price=19.99,
        description='This is an asynchronous test product.',
    )
    
    parent_categories = await Product.get_parent_categories(id_category=3)
    print(f'Parent categories: {parent_categories}')


    new_product = await product.add_new_product(product_fields)
    if new_product:
        print(f'New product id = {new_product.id_product}')
    else:
        print(f'Error add new product')

    await product.fetch_data_async()

if __name__ == '__main__':
    asyncio.run(main())