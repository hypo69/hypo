## \file hypotez/src/endpoints/prestashop/api/_experiments/header.py
# -*- coding: utf-8 -*-

""" module: src.endpoints.prestashop.api._experiments """
MODE = 'debug'
""" module: src.endpoints.prestashop.api._experiments """
MODE = 'debug'
""" Тестовые настройки для проверки PrestaAPIV.
создает словари подключеня к API Prestashop из списка `gs.presta_credentials`

"""
 
import os, sys
from pathlib import Path

# ----------------
dir_root : Path = Path (os.getcwd()[:os.getcwd().rfind('hypotez')+7])
sys.path.append (str (dir_root) )  # Добавляю корневую папку в sys.path
dir_src = Path (dir_root, 'src')
sys.path.append (str (dir_root) ) 
# ----------------

from __init__ import gs
from src.utils import pprint,jprint
#from src.suppliers import Supplier
#from src.product import Product, ProductFields
from src.logger import logger


def get_api_credentials (api_url:str) -> dict:
    """ Функция вытаскиват из объекта глобальных настроек `gs` список словарей подключений
    к клиентским сайтам (f.e. https://e-cat.co.il/api, https://sergey.mymaster/api)
    @param api_url `str` - URI API клиента. (https://emil-design.com/api)
    @returns словарь API параметров подключения
    """
    
    return next((item for item in gs.credentials     if api_url == item['api_domain']), None)


emil_api_credentials:dict = get_api_credentials('https://emil-design.com/api')

ecat_api_credentials:dict = get_api_credentials('https://e-cat.co.il/api'))