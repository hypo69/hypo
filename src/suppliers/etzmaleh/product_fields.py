## \file src/suppliers/etzmaleh/product_fields.py
"""   [File's Description]

@namespace src: src
 \package src.suppliers.etzmaleh
\file product_fields.py
 
 @section libs imports:
  - sqlite3 
  - typing 
  - pathlib 
  - attr 
  - enum 
  - helpers 
  - gs 
  - tools 
  - product 
  - gs 
Author(s):
  - Created by Davidka on 09.11.2023 .
"""
## \file ../src/suppliers/etzmaleh/product_fields.py
# -*- coding: utf-8 -*-
# /path/to/interpreter/python

from sqlite3 import Date
from typing import Union
from pathlib import Path
from attr import attr, attrs
from enum import Enum

# --------------------------------------------
from src.logger import logger
from src.utils import j_loads as j_loads
from src.utils import StringFormatter, StringNormalizer
from src.product import Product_fields
product_fields.ProductFields()
from src.settings import GlobalSettings
gs = GlobalSettings.get_instance()
# --------------------------------------------


class ProductFields(product_fields.ProductFields):


    def __init__(self, *args, **kwards):
        """ См информавию в модуле родителе """
        super().__init__()



