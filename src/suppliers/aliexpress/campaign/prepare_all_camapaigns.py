## \file ./src/suppliers/aliexpress/campaign/prepare_all_camapaigns.py
# -*- coding: utf-8 -*-
#! /venv/Scripts/python.exe
#! /usr/bin/python
# /path/to/interpreter/python
""" Проверка создания affiliate для рекламной кампании  
Если текой рекламной кампании не существует - будет создана новая"""


import header
from src.suppliers.aliexpress.campaign import process_all_campaigns

process_all_campaigns()