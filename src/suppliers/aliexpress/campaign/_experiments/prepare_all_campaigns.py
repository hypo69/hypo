#! /usr/bin/python
﻿## \file src/suppliers/aliexpress/campaign/_experiments/prepare_campaign.py
## \file /src/suppliers/aliexpress/campaign/_experiments/prepare_all_campaigns.py
# -*- coding: utf-8 -*-
# /path/to/interpreter/python
""" Прогоняет все рекламные кампании для всех языков с поиском названий категорий из директорий """
...
import header
from src.suppliers.aliexpress.campaign.prepare_campaigns import process_all_campaigns, main_process

# locales = {'EN': 'USD', 'HE': 'ILS', 'RU': 'ILS'}
# campaign_name:str = 'rc'
# language: str = 'EN'
# currency: str = 'USD'
# campaign_file:str = None
# # Если текой рекламной кампании не существует - будет создана новая

process_campaign(campaign_name = campaign_name, language = language, currency = currency, campaign_file = campaign_file)
main_process('brands',['mrgreen'])
#process_all_campaigns()

    