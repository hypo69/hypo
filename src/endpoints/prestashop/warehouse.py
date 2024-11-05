#! /usr/bin/python
﻿## \file src/prestashop/warehouse.py
## \file /src/endpoints/prestashop/warehouse.py
# -*- coding: utf-8 -*-
# /path/to/interpreter/python
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