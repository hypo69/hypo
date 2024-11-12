## \file hypotez/src/endpoints/prestashop/warehouse.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe # <- venv win
#! venv/bin/python # <- venv linux/macos
#! py # <- system win
#! /usr/bin/python # <- system linux/macos
## ~~~~~~~~~~~~~
""" module: src.endpoints.prestashop """

""" Класс склада (warwehouse) `Prestashop`"""


import os,sys
from attr import attr, attrs
from pathlib import Path

from src import gs
from src.utils import  pprint
from .api import Prestashop
from src.logger import logger


class PrestaWarehouse(Prestashop): 
    ...