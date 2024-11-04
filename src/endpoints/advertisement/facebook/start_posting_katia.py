## \file ../src/endpoints/advertisement/facebook/start_posting_katia.py
# -*- coding: utf-8 -*-
# /path/to/interpreter/python
"""Отправка рекламных объявлений в группы фейсбук """

import header 
from src.webdriver import Driver, Chrome
from src.advertisement.facebook.promoter import FacebookPromoter
from src.logger import logger

d = Driver(Chrome)
d.get_url(r"https://facebook.com")

filenames:list = ['katia_homepage.json',]
campaigns:list = [ 'sport_and_activity',
                  'bags_backpacks_suitcases',
                    'pain',
                    'brands',
                    'mom_and_baby',
                    'house',
                ]
promoter = FacebookPromoter(d, group_file_paths = filenames, no_video = False)

try:
    promoter.run_campaigns(campaigns)
except KeyboardInterrupt:
    logger.info("Campaign promotion interrupted.")