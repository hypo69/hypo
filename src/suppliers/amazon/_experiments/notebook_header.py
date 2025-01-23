## \file /src/suppliers/amazon/_experiments/notebook_header.py
# -*- coding: utf-8 -*-

#! .pyenv/bin/python3

"""
.. module:: src.suppliers.amazon._experiments 
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
  
""" module: src.suppliers.amazon._experiments """


import sys
import os
from pathlib import Path

# ----------------
dir_root : Path = Path (os.getcwd()[:os.getcwd().rfind('hypotez')+7])
sys.path.append (str (dir_root) )  # Добавляю корневую папку в sys.path
dir_src = Path (dir_root, 'src')
sys.path.append (str (dir_root) ) 
# ----------------

from pathlib import Path
import json
import re



from src import gs
from src.webdriver.driver import Driver, executor
from src.suppliers import Supplier
from src.product import Product, ProductFields
from src.category import Category
from src.utils import StringFormatter, StringNormalizer
from src.utils.printer import  pprint
, save_text_file
# ----------------

def start_supplier(supplier_prefix, locale):
    """ Старт поставщика """
    if not supplier_prefix and not locale: return "Не задан сценарий и язык"
    
    params: dict = \
    {
        'supplier_prefix': supplier_prefix,
        'locale': locale
    }
    
    return Supplier(**params))