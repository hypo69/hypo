## \file hypotez/src/endpoints/prestashop/supplier.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe # <- venv win
## ~~~~~~~~~~~~~
""" module: src.endpoints.prestashop """

""" @namespace src.pestashop 
Класс поставщика в `Prestashop`"""
...
from types import SimpleNamespace
from src import gs
from src.logger import logger
from src.utils import j_loads as j_loads
from .api import Prestashop


class PrestaSupplier (Prestashop):
    """ """
    def __init__(self, api_credentials: dict | SimpleNamespace, *args,**kwards):
        super().__init__(
            api_credentials['api_domain'], 
            api_credentials['api_key'], *args,**kwards)

