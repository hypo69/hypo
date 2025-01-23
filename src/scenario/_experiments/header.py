## \file /src/scenario/_experiments/header.py
# -*- coding: utf-8 -*-

#! .pyenv/bin/python3

"""
.. module:: src.scenario._experiments 
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
  
""" module: src.scenario._experiments """


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
from src import gs
from src.suppliers import Supplier
from src.product import Product
from categories import Category
from src.logger.logger import logger,log_decorator, pprint


def start_supplier(supplier_prefix):
    params: dict = \
    {
        'supplier_prefix': supplier_prefix
    }
    
    return Supplier(**params))