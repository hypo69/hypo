## \file hypotez/src/endpoints/prestashop/warehouse.py
# -*- coding: utf-8 -*-

""" module: src.endpoints.prestashop """
MODE = 'debug'
""" module: src.endpoints.prestashop """
MODE = 'debug'

""" Класс склада (warwehouse) `Prestashop`"""


import os,sys
from attr import attr, attrs
from pathlib import Path

from __init__ import gs
from src.utils import  pprint
from .api import Prestashop
from src.logger import logger


class PrestaWarehouse(Prestashop): 
    ...