## \file hypotez/src/suppliers/aliexpress/scenarios/_experiments/promote_deal.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe

""" module: src.suppliers.aliexpress.scenarios._experiments """
MODE = 'debug'
""" module: src.suppliers.aliexpress.scenarios._experiments """
MODE = 'debug'

""" Создание рекламной кампании """

import header

from src.suppliers.aliexpress.scenarios import AliPromoDeal

deal = AliPromoDeal('150624_baseus_deals')

#product = deal.get_next_product()
products = deal.get_all_products_details()

...