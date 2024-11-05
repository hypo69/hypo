#! /usr/bin/python
﻿## \file src/scenario/_experiments/header.py
import sys
import os
path = os.getcwd()[:os.getcwd().rfind(r'hypotez')+7]
sys.path.append(path)  # Добавляю корневую папку в sys.path
# ----------------
## \file /src/scenario/_experiments/header.py
# -*- coding: utf-8 -*-
# /path/to/interpreter/python

from pathlib import Path
import json
import re
# ----------------
#from hypotez import gs, Supplier, Product
from src import gs
from src.suppliers import Supplier
from src.product import Product
from categories import Category
from src.logger import logger,log_decorator, pprint


def start_supplier(supplier_prefix):
    params: dict = \
    {
        'supplier_prefix': supplier_prefix
    }
    
    return Supplier(**params))