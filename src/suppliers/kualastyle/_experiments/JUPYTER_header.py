## \file hypotez/src/suppliers/kualastyle/_experiments/JUPYTER_header.py
# -*- coding: utf-8 -*-

""" module: src.suppliers.kualastyle._experiments """
MODE = 'debug'
""" module: src.suppliers.kualastyle._experiments """
MODE = 'debug'
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


#from settings import gs
from src.webdriver import Driver
from src.suppliers import Supplier
from src.product import Product, ProductFields
from src.category import Category
from src.utils import StringFormatter, StringNormalizer
from src.utils import  pprint
from src.endpoints.prestashop import Product as PrestaProduct
, save_text_file
# ----------------

def start_supplier(supplier_prefix: str = 'aliexpress', locale: str = 'en' ):
    """ Старт поставщика """
    params: dict = \
    {
        'supplier_prefix': supplier_prefix,
        'locale': locale
    }
    
    return Supplier(**params))