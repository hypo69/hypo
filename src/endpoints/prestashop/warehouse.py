## \file hypotez/src/endpoints/prestashop/warehouse.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
.. module: src.endpoints.prestashop 
	:platform: Windows, Unix
	:synopsis:

"""
MODE = 'dev'

import os,sys
from attr import attr, attrs
from pathlib import Path
import header
from src import gs
from src.utils.printer import  pprint
from .api import PrestaShop
from src.logger import logger


class PrestaWarehouse(PrestaShop): 
    ...