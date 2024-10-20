﻿"""  Class `Product`. Interaction between website, product, and PrestaShop.
@details Defines the behavior of a product in the project.
"""

## \file ../src/product/product.py
# -*- coding: utf-8 -*-
# /path/to/interpreter/python

from src import gs
from src.prestashop import Prestashop
from src.category import Category
from src.product.product_fields import ProductFields
from src.logger import logger


class Product(ProductFields, Prestashop):
    """  Manipulations with the product.
    @details Initially, I instruct the grabber to fetch data from the product page,
    and then work with the PrestaShop API.
    """
    def __init__(self, *args, **kwargs):
        super().__init__( *args, **kwargs)
        ...

    @staticmethod
    def get_parent_categories(id_category: int, dept: int = 0) -> list:
        """ Collects parent categories from the specified category.
        Duplicates the function get_parents() from the Category class.
        """
        return Category.get_parents(id_category, dept)
