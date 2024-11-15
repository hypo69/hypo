## \file hypotez/src/endpoints/prestashop/product.py
# -*- coding: utf-8 -*-

""" module: src.endpoints.prestashop """
MODE = 'debug'
""" module: src.endpoints.prestashop """
MODE = 'debug'

""" Класс товара `Prestashop`"""
...

import os,sys
from attr import attr, attrs
from pathlib import Path
from typing import Dict, List
# ----------------------------------
from __init__ import gs
from src.utils import  pprint
from .api import Prestashop
from src.logger import logger
from src.logger.exceptions import PrestaShopException


class PrestaProduct(Prestashop):
    """ Класс товара из модуля prestashop
   Непосредственно выполняет все операции через API
   ------------------------------------
   Methods:
    check(product_reference: str): Проверка наличия товара в бд
        по product_reference (SKU, MKT)
        Вернет словарь товара, если товар есть, иначе False
    search(filter: str, value: str): Расширенный поиск в БД по фильтрам
    get(id_product): Возвращает информацию о товаре по ID
    """

    
    def __init__(self, *args,**kwards):
        super().__init__( *args,**kwards)


     