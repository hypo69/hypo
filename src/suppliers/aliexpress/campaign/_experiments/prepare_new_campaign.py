## \file hypotez/src/suppliers/aliexpress/campaign/_experiments/prepare_new_campaign.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe

""" module: src.suppliers.aliexpress.campaign._experiments """
MODE = 'debug'
""" module: src.suppliers.aliexpress.campaign._experiments """
MODE = 'debug'


""" Эксперименты над сценарием новой рекламной камании """
...
import header

from pathlib import Path

from __init__ import gs

from src.suppliers.aliexpress.campaign import AliCampaignEditor
from src.utils import get_filenames, get_directory_names
from src.utils import pprint
from src.logger import logger

campaign_name = 'rc'
aliexpress_editor =  AliCampaignEditor(campaign_name)
aliexpress_editor.process_new_campaign(campaign_name)