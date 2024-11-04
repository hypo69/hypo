""" Примеры создания рекламной кампании """

## \file src/suppliers/aliexpress/campaign/_examples/_example_ali_promo_campaign.py
# -*- coding: utf-8 -*-
# /path/to/interpreter/python

...
import header
from pathlib import Path
from types import SimpleNamespace
from src import gs
from src.suppliers.aliexpress import AliPromoCampaign
from src.suppliers.aliexpress import AliAffiliatedProducts
from src.utils import get_filenames, get_directory_names, read_text_file, csv2dict
from src.utils import j_loads_ns
from src.utils import pprint
from src.logger import logger

campaigns_directory = Path(gs.path.google_drive, 'aliexpress', 'campaigns')
campaign_names = get_directory_names(campaigns_directory)

campaign_name = '280624_cleararanse'
category_name = 'gaming_comuter_accessories'
language = 'EN'
currency = 'USD'

a:SimpleNamespace = AliPromoCampaign(campaign_name = campaign_name, 
                     category_name = category_name, 
                     language = language, 
                     currency = currency) 

campaign = a.campaign
category = a.category
products = a.category.products

# dict
a = AliPromoCampaign(campaign_name,category_name,{'EN':'USD'})
# string
a = AliPromoCampaign(campaign_name,category_name, 'EN','USD')))