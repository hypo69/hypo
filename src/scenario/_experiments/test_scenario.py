## \file /src/scenario/_experiments/test_scenario.py
# -*- coding: utf-8 -*-

#! .pyenv/bin/python3

"""
.. module:: src.scenario._experiments 
	:platform: Windows, Unix
	:synopsis:

"""


"""
	:platform: Windows, Unix
	:synopsis:

"""

"""
	:platform: Windows, Unix
	:synopsis:

"""

"""
  :platform: Windows, Unix

"""
"""
  :platform: Windows, Unix
  :platform: Windows, Unix
  :synopsis:
"""
  
""" module: src.scenario._experiments """


import sys
import os
path = os.getcwd()[:os.getcwd().rfind(r'hypotez')]
sys.path.append(path)  # Добавляю корневую папку в sys.path
# ----------------
from pathlib import Path
import json
import re
# ----------------
from hypotez import gs
from src.utils.printer import  pprint

from src.scenario import Scenario
from src.suppliers import Supplier

def start_supplier(supplier_prefix):
    params: dict = \
    {
        'supplier_prefix': supplier_prefix
    }
    
    return Supplier(**params)


supplier_prefix = 'aliexpress'
#supplier_prefix = 'amazon'
#supplier_prefix = 'kualastyle'
#supplier_prefix = 'ebay'

s = start_supplier(supplier_prefix)
""" s - на протяжении всего кода означает класс `Supplier` """

print(" Можно продолжать ")

scenario = Scenario(s)

scenario.run_scenarios())