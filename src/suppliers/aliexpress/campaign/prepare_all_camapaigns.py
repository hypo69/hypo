## \file hypotez/src/suppliers/aliexpress/campaign/prepare_all_camapaigns.py
# -*- coding: utf-8 -*-

""" module: src.suppliers.aliexpress.campaign """
MODE = 'debug'
""" module: src.suppliers.aliexpress.campaign """
MODE = 'debug'

""" Проверка создания affiliate для рекламной кампании  
Если текой рекламной кампании не существует - будет создана новая"""


import header
from src.suppliers.aliexpress.campaign import process_all_campaigns

process_all_campaigns()