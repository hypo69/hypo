## \file hypotez/src/product/_experiments/ping.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python
""" module: src.product._experiments """
MODE = 'development'


import header
from header import  ecat_api_credentials, emil_api_credentials
from header import pprint, jprint
from src import gs
from src.endpoints.PrestaShop.presta_apis.client import PrestaShop

client = PrestaShop(ecat_api_credentials)

    
while True:
    reference = '11267-204'
    search_filter = { 'filter[reference]': '['+ reference + ']',  }
    #get = client.get('languages')
    get = client.get('products', search_filter = search_filter)
    pprint(get)
    ...
...