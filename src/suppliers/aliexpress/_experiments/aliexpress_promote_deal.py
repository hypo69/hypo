## \file hypotez/src/suppliers/aliexpress/_experiments/aliexpress_promote_deal.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe # <- venv win
#! venv/bin/python # <- venv linux/macos
#! py # <- system win
#! /usr/bin/python # <- system linux/macos
## ~~~~~~~~~~~~~
""" module: src.suppliers.aliexpress._experiments """
""" Deal, event
Подготовка объявления в формате для фейсбук
"""


...
import header
from src.suppliers.aliexpress import AliPromoDeal

deal_name = '150624_baseus_deals'
a = AliPromoDeal(deal_name)
#products = a.prepare_products_for_deal()
...