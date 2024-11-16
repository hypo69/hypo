## \file hypotez/src/endpoints/prestashop/supplier.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe

""" module: src.endpoints.prestashop """
MODE = 'debug'
""" module: src.endpoints.prestashop """
MODE = 'debug'

""" @namespace src.pestashop 
Класс поставщика в `Prestashop`"""
...
from types import SimpleNamespace
import header
from src import gs
from src.logger import logger
from src.utils import j_loads as j_loads
from .api import Prestashop


class PrestaSupplier (Prestashop):
    """ """
    def __init__(self, api_credentials: dict | SimpleNamespace, *args,**kwards):
        super().__init__(
            api_credentials.get('api_domain', None), 
            api_credentials('api_key', None), *args,**kwards)

