## \file src/prestashop/customer.py
## \file ../src/endpoints/prestashop/customer.py
# -*- coding: utf-8 -*-
# /path/to/interpreter/python
"""  Класс клиента в `Prestashop`"""
...

import sys
import os
from attr import attr, attrs
from pathlib import Path
from typing import Union
# ----------------------------------
from src import gs
from src.logger import logger
from src.utils import j_loads as j_loads
from .api import Prestashop
from src.logger import logger
from src.logger.exceptions import PrestaShopException

class PrestaCustomer(Prestashop): ...