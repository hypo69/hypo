## \file hypotez/src/endpoints/prestashop/language.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe

""" module: src.endpoints.prestashop """
MODE = 'debug'
""" module: src.endpoints.prestashop """
MODE = 'debug'

"""   класс языка в `Prestashop` """
...
from .api import Prestashop
from __init__ import gs
from src.utils import  pprint
from .api import Prestashop
from src.logger import logger
from src.logger.exceptions import PrestaShopException

class PrestaLanguage(Prestashop):
    """ Класс, отвечающий за настройки языков магазина"""
    def __init__(self, api_credentials, *args,**kwards):
        super().__init__(api_credentials, *args,**kwards)
        
    

            

