## \file hypotez/src/suppliers/aliexpress/campaign/_examples/_example_edit_campaign.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe # <- venv win
## ~~~~~~~~~~~~~
""" module: src.suppliers.aliexpress.campaign._examples """

""" Редактор рекламной кампании
"""
...
import re
import shutil
from pathlib import Path
from typing import List, Optional, Union
from types import SimpleNamespace
from __init__ import gs
from src.suppliers.aliexpress.scenarios.campaigns import AliPromoCampaign
from src.suppliers.aliexpress.affiliated_products_generator import AliAffiliatedProducts
from src.suppliers.aliexpress.utils.extract_product_id import extract_prod_ids
from src.suppliers.aliexpress.utils.set_full_https import ensure_https
from src.utils import j_loads_ns, j_loads
from src.utils.convertors import list2string, csv2dict
from src.utils import pprint
from src.utils.jjson import j_dumps, j_loads, j_loads_ns
from utils.interface import read_text_file, get_filenames
from src.logger import logger

class AliCampaignEditor(AliPromoCampaign):
    """ Редактор реклманой камапнии """
    ...

    def __init__(self, campaign_name: str, category_name: str, language: str = 'EN', currency: str = 'USD'):
        """"""
        ...
        super().__init__(campaign_name, category_name, language, currency)
        


