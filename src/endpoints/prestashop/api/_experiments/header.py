## \file hypotez/src/endpoints/prestashop/api/_experiments/header.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
.. module:: src.endpoints.prestashop.api._experiments 
	:platform: Windows, Unix
	:synopsis:

"""
MODE = 'dev'

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
"""MODE = 'dev'
  
""" module: src.endpoints.prestashop.api._experiments """


""" Тестовые настройки для проверки PrestaAPIV.
создает словари подключеня к API PrestaShop из списка `gs.presta_credentials`

"""
 
import os, sys
from pathlib import Path

# ----------------
dir_root : Path = Path (os.getcwd()[:os.getcwd().rfind('hypotez')+7])
sys.path.append (str (dir_root) )  # Добавляю корневую папку в sys.path
dir_src = Path (dir_root, 'src')
sys.path.append (str (dir_root) ) 
# ----------------

from src import gs
from src.utils.printer import pprint,jprint
#from src.suppliers import Supplier
#from src.product import Product, ProductFields
from src.logger.logger import logger


def get_api_credentials (api_url:str) -> dict:
    """ Функция вытаскиват из объекта глобальных настроек `gs` список словарей подключений
    к клиентским сайтам (f.e. https://e-cat.co.il/api, https://sergey.mymaster/api)
    @param api_url `str` - URI API клиента. (https://emil-design.com/api)
    @returns словарь API параметров подключения
    """
    
    return next((item for item in gs.credentials     if api_url == item['api_domain']), None)


emil_api_credentials:dict = get_api_credentials('https://emil-design.com/api')

ecat_api_credentials:dict = get_api_credentials('https://e-cat.co.il/api'))