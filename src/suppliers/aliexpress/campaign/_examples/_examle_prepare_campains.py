## \file hypotez/src/suppliers/aliexpress/campaign/_examples/_examle_prepare_campains.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe

""" module: src.suppliers.aliexpress.campaign._examples """
MODE = 'debug'
""" module: src.suppliers.aliexpress.campaign._examples """
MODE = 'debug'
from ..prepare_campaigns import *

# Example 1: Process a Single Campaign Category
process_campaign_category("SummerSale", "Electronics", "EN", "USD", force=True)

# Example 2: Process a Specific Campaign
process_campaign("WinterSale", categories=["Clothing", "Toys"], language="EN", currency="USD", force=False)

# Example 3: Process All Campaigns
process_all_campaigns(language="EN", currency="USD", force=True)


campaigns_directory = Path(gs.path.google_drive,'aliexpress','campaigns')
campaign_names = get_directory_names(campaigns_directory)
languages = {'EN': 'USD', 'HE': 'ILS', 'RU': 'ILS'}



