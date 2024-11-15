## \file hypotez/src/scenario/_experiments/header.py
# -*- coding: utf-8 -*-

""" module: src.scenario._experiments """
MODE = 'debug'
""" module: src.scenario._experiments """
MODE = 'debug'
import sys
import os
path = os.getcwd()[:os.getcwd().rfind(r'hypotez')+7]
sys.path.append(path)  # Добавляю корневую папку в sys.path
# ----------------


from pathlib import Path
import json
import re
# ----------------
#from hypotez import gs, Supplier, Product
from __init__ import gs
from src.suppliers import Supplier
from src.product import Product
from categories import Category
from src.logger import logger,log_decorator, pprint


def start_supplier(supplier_prefix):
    params: dict = \
    {
        'supplier_prefix': supplier_prefix
    }
    
    return Supplier(**params))