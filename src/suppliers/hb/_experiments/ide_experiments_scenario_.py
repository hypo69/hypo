## \file /src/suppliers/hb/_experiments/ide_experiments_scenario_.py
# -*- coding: utf-8 -*-

#! .pyenv/bin/python3

"""
.. module:: src.suppliers.hb._experiments 
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
  
""" module: src.suppliers.hb._experiments """


"""  Файл проверки наполнения полей HB -> product_fields """



#from math import prod
import os, sys
from pathlib import Path
from typing import List, Union, Dict
from selenium.webdriver.remote.webelement import WebElement

################# добавление корневой директории позволяет мне плясать от печки ###################
dir_root: Path = Path(os.getcwd()[:os.getcwd().rfind('hypotez') + 7])
sys.path.append(str(dir_root))  # Adding the root folder to sys.path
dir_src = Path(dir_root, 'src')
sys.path.append(str(dir_root))
from src.webdriver import executor
"""  добавление корневой директории позволяет мне плясать от печки. """
####################################################################################################


from src import gs
from src.suppliers import Supplier
from src.product import Product, ProductFields
from src.scenario import run_scenarios

from src.logger.logger import logger, ExecuteLocatorException
from src.webdriver.driver import Driver
from src.utils import StringFormatter, StringNormalizer


s: Supplier = Supplier(supplier_prefix = 'hb')
p: Product = Product(s)
l: dict = s.locators['product']
d: Driver = s.driver
f: ProductFields = ProductFields(s)


s.current_scenario: dict =  {
      "url": "https://hbdeadsea.co.il/product-category/bodyspa/feet-hand-treatment/",
      "name": "טיפוח כפות ידיים ורגליים",
      "condition": "new",
      "presta_categories": {
        "default_category": 11259,
        "additional_categories": []
      }
    }

ret = run_scenarios(s, s.current_scenario)
...


