## \file ../src/advertisement/facebook/start_sergey.py
# -*- coding: utf-8 -*-
# /path/to/interpreter/python
"""Отправка рекламных объявлений в группы фейсбук """

from math import log
import header
import time
from src.webdriver import Driver, Chrome
from src.advertisement.facebook import FacebookPromoter
from src.logger import logger

d = Driver(Chrome)
d.get_url(r"https://facebook.com")

group_file_paths:list[str] = [
                        "sergey_page_ru.json",
                        ]


campaigns:list = ['kazarinov_ru']
group_categories_to_adv = ['sales','biz']
promoter:FacebookPromoter = FacebookPromoter(d, promoter = 'kazarinov')

try:
    while True:
        language, currency = "RU", "ILS"

        logger.debug(f"waikig up {time.strftime('%H:%M:%S')}",None,False)

        promoter.run_campaigns(campaigns = campaigns, 
                               group_file_paths = group_file_paths, 
                               group_categories_to_adv =  group_categories_to_adv,
                               language = language, 
                               currency = currency,
                               no_video = True)

        logger.debug(f"going to sleep at {time.strftime('%H:%M:%S')}",None,False)
        time.sleep(7200)
        
except KeyboardInterrupt:
    logger.info("Campaign promotion interrupted.")