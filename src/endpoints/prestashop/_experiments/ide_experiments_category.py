## \file hypotez/src/endpoints/prestashop/_experiments/ide_experiments_category.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
.. module: src.endpoints.prestashop._experiments 
	:platform: Windows, Unix
	:synopsis:

"""
MODE = 'dev'

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
"""MODE = 'dev'
  
""" module: src.endpoints.prestashop._experiments """


import ide_header
from ide_header import  gs
from src.category import  Category

c = Category()
list_parent_categories_from_PrestaShop = c.get_parent_categories_list(11036)
print(list_parent_categories_from_PrestaShop)
...
...