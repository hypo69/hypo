## \file hypotez/src/suppliers/kualastyle/_experiments/notebook_header.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python
""" module: src.suppliers.kualastyle._experiments """
MODE = 'development'


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
from src.utils import  pprint

#from src.endpoints.PrestaShop import Product as PrestaProduct, PrestaAPIV1, PrestaAPIV2, PrestaAPIV3
# ----------------

def start_supplier(supplier_prefix: str = 'kualastyle' ):
    """ Старт поставщика (kualastyle)"""
    params: dict = \
    {
        'supplier_prefix': supplier_prefix
    }
    
    return Supplier(**params))