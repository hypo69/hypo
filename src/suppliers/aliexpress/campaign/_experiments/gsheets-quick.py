## \file hypotez/src/suppliers/aliexpress/campaign/_experiments/gsheets-quick.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
.. module: src.suppliers.aliexpress.campaign._experiments 
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
  
""" module: src.suppliers.aliexpress.campaign._experiments """


""" Работа с гугл таблицами """


from unicodedata import category
import header
from types import SimpleNamespace
from gspread import Worksheet, Spreadsheet
from src.suppliers.aliexpress.campaign import AliCampaignGoogleSheet
from src.suppliers.aliexpress.campaign.ttypes import CampaignType, CategoryType, ProductType
from src.utils.printer import pprint
from src.logger import logger


campaign_name = "lighting"
category_name = "chandeliers"
language = 'EN'
currency = 'USD'

gs = AliCampaignGoogleSheet(campaign_name=campaign_name, language=language, currency=currency)

gs.set_products_worksheet(category_name)
#gs.save_categories_from_worksheet(False)
gs.save_campaign_from_worksheet()
...
