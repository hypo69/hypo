## \file /src/suppliers/aliexpress/campaign/_experiments/prepare_campaign.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
.. module:: src.suppliers.aliexpress.campaign._experiments 
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
  
""" module: src.suppliers.aliexpress.campaign._experiments """


""" Проверка создания affiliate для рекламной кампании  
Если текой рекламной кампании не существует - будет создана новая"""

...
import header
from src.suppliers.aliexpress.campaign import process_campaign

locales = {'EN': 'USD', 'HE': 'ILS', 'RU': 'ILS'}
language: str = 'EN'
currency: str = 'USD'
campaign_name:str = 'brands'
# Если текой рекламной кампании не существует - будет создана новая

#process_campaign(campaign_name = campaign_name, language = language, currency = currency, campaign_file = campaign_file)
process_campaign(campaign_name = campaign_name)

    