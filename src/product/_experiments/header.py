## \file hypotez/src/product/_experiments/header.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
.. module:: src.product._experiments 
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
  
""" module: src.product._experiments """


import sys
import os
from pathlib import Path

dir_root : Path = Path (os.getcwd()[:os.getcwd().rfind('hypotez')+11])
sys.path.append (str (dir_root) )  # Добавляю корневую папку в sys.path
dir_src = Path (dir_root, 'src')
sys.path.append (str (dir_root) ) 
...

print(dir_root)
# ----------------
from pathlib import Path
import json
import re
# ----------------

from src import gs
from src.suppliers import Supplier
from src.product import Product, ProductFields, ProductFieldsLocators
from src.category import Category
from src.utils import StringFormatter, StringNormalizer
from src.utils.jjson import j_dumps, j_loads,   pprint, save_text_file
from src.logger.logger import logger

# ----------------

def start_supplier(supplier_prefix: str = 'aliexpress', locale: str = 'en' ):
    """ Старт поставщика """
    params: dict = \
    {
        'supplier_prefix': supplier_prefix,
        'locale': locale
    }
    
    return Supplier(**params)



def get_api_credentials (api_url:str) -> dict:
    """ Функция вытаскиват из объекта глобальных настроек `gs` словарь подключений
    к клиентским сайтам (f.e. https://e-cat.co.il/api, https://sergey.mymaster/api)
    @param url `str` - URI API клиента. (https://emil-design.com/api)
    @returns словарь API параметров подключения
    """
    
    return next((item for item in gs.presta_credentials if item['api_domain'] == api_url), None)




emil_api_credentials:dict = get_api_credentials('https://emil-design.com/api')
...

ecat_api_credentials:dict = get_api_credentials('https://e-cat.co.il/api'))