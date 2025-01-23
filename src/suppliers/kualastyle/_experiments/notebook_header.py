## \file /src/suppliers/kualastyle/_experiments/notebook_header.py
# -*- coding: utf-8 -*-

#! .pyenv/bin/python3

"""
.. module:: src.suppliers.kualastyle._experiments 
	:platform: Windows, Unix
	:synopsis:

"""


"""
	:platform: Windows, Unix
	:synopsis:

"""

"""
	:platform: Windows, Unix
	:synopsis:

"""

"""
  :platform: Windows, Unix

"""
"""
  :platform: Windows, Unix
  :platform: Windows, Unix
  :synopsis:
"""
  
""" module: src.suppliers.kualastyle._experiments """


import sys
import os
path = os.getcwd()[:os.getcwd().rfind(r'hypotez')+7]
sys.path.append(path)  # Добавляю корневую папку в sys.path

# ----------------
from pathlib import Path
import json
import re
# ----------------

from src import gs
from src.suppliers import Supplier
from src.product import Product, ProductFields
from categories import Category
from src.utils import StringFormatter, StringNormalizer, translate
from src.utils.printer import  pprint

#from src.endpoints.PrestaShop import Product as PrestaProduct, PrestaAPIV1, PrestaAPIV2, PrestaAPIV3
# ----------------

def start_supplier(supplier_prefix: str = 'kualastyle' ):
    """ Старт поставщика (kualastyle)"""
    params: dict = \
    {
        'supplier_prefix': supplier_prefix
    }
    
    return Supplier(**params))