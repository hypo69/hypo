## \file hypotez/src/endpoints/prestashop/customer.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe

""" module: src.endpoints.prestashop """
MODE = 'debug'
""" module: src.endpoints.prestashop """
MODE = 'debug'

"""  Класс клиента в `Prestashop`"""
...

import sys
import os
from attr import attr, attrs
from pathlib import Path
from typing import Union
# ----------------------------------
from __init__ import gs
from src.logger import logger
from src.utils import j_loads as j_loads
from .api import Prestashop
from src.logger import logger
from src.logger.exceptions import PrestaShopException

class PrestaCustomer(Prestashop): ...