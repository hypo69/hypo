## \file /src/suppliers/amazon/_experiments/scenarois/all_scenarios_from_amazon/murano_glass/header.py
# -*- coding: utf-8 -*-

#! .pyenv/bin/python3

"""
.. module:: src.suppliers.amazon._experiments.scenarois.all_scenarios_from_amazon.murano_glass 
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
  
""" module: src.suppliers.amazon._experiments.scenarois.all_scenarios_from_amazon.murano_glass """


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
from src.webdriver.driver import Driver
from src.category import Category
from src.utils import StringFormatter, StringNormalizer
from src.utils.printer import  pprint

from src.endpoints.PrestaShop import PrestaAPIV, upload_image
# ----------------

def start_supplier(supplier_prefix: str = 'amazon' ):
    """ Старт поставщика (amazon)"""

def start_supplier(supplier_prefix):
    params: dict = \
    {
        'supplier_prefix': supplier_prefix
    }
    
    return Supplier(**params))