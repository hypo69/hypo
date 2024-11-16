## \file hypotez/src/suppliers/hb/_experiments/notebook_header-Copy1.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe

""" module: src.suppliers.hb._experiments """
MODE = 'debug'
""" module: src.suppliers.hb._experiments """
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



from __init__ import gs
from src.webdriver import Driver, executor
from src.suppliers import Supplier
from src.product import Product, ProductFields
from src.category import Category
from src.utils import StringFormatter, StringNormalizer
from src.utils import  pprint
, save_text_file
from src.scenario import run_scenarios
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