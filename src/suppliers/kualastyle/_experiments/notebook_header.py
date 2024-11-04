## \file src/suppliers/kualastyle/_experiments/notebook_header.py
## \file src/suppliers/kualastyle/_experiments/notebook_header.py
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

#from src.endpoints.prestashop import Product as PrestaProduct, PrestaAPIV1, PrestaAPIV2, PrestaAPIV3
# ----------------

def start_supplier(supplier_prefix: str = 'kualastyle' ):
    """ Старт поставщика (kualastyle)"""
    params: dict = \
    {
        'supplier_prefix': supplier_prefix
    }
    
    return Supplier(**params))