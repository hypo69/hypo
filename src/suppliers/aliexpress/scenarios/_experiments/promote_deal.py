#! /usr/bin/python
﻿## \file src/suppliers/aliexpress/scenarios/_experiments/promote_deal.py
## \file /src/suppliers/aliexpress/scenarios/_experiments/promote_deal.py
# -*- coding: utf-8 -*-
# /path/to/interpreter/python
""" Создание рекламной кампании """

import header

from src.suppliers.aliexpress.scenarios import AliPromoDeal

deal = AliPromoDeal('150624_baseus_deals')

#product = deal.get_next_product()
products = deal.get_all_products_details()

...