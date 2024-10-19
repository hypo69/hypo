## \file ../src/suppliers/amazon/_experiments/scenarois/all_scenarios_from_amazon/murano_glass/header.py
## \file src/suppliers/amazon/_experiments/scenarois/all_scenarios_from_amazon/murano_glass/header.py
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
from src.webdriver import Driver
from src.category import Category
from src.utils import StringFormatter, StringNormalizer
from src.utils import  pprint

from src.prestashop import PrestaAPIV, upload_image
# ----------------

def start_supplier(supplier_prefix: str = 'amazon' ):
    """ Старт поставщика (amazon)"""

def start_supplier(supplier_prefix):
    params: dict = \
    {
        'supplier_prefix': supplier_prefix
    }
    
    return Supplier(**params))