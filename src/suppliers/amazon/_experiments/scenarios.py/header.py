## \file hypotez/src/suppliers/amazon/_experiments/scenarios.py/header.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python
""" module: src.suppliers.amazon._experiments.scenarios.py """
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

from src.endpoints.PrestaShop import Product as PrestaProduct

def start_supplier(supplier_prefix: str = 'amazon' ):
    """ Старт поставщика (amazon)"""

def start_supplier(supplier_prefix = 'amazon'):
    params: dict = \
    {
        'supplier_prefix': supplier_prefix
    }
    
    return Supplier(**params))