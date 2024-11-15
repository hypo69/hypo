## \file hypotez/src/endpoints/prestashop/_experiments/ide_experiments_category.py
# -*- coding: utf-8 -*-

""" module: src.endpoints.prestashop._experiments """
MODE = 'debug'
""" module: src.endpoints.prestashop._experiments """
MODE = 'debug'
import ide_header
from ide_header import  gs
from src.category import  Category

c = Category()
list_parent_categories_from_prestashop = c.get_parent_categories_list(11036)
print(list_parent_categories_from_prestashop)
...
...