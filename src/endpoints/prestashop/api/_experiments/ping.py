## \file hypotez/src/endpoints/prestashop/api/_experiments/ping.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe

""" module: src.endpoints.prestashop.api._experiments """
MODE = 'debug'
""" module: src.endpoints.prestashop.api._experiments """
MODE = 'debug'
import header
from header import  ecat_api_credentials, emil_api_credentials
from header import pprint, jprint
from __init__ import gs
from src.endpoints.prestashop.presta_apis.client import Prestashop

client = Prestashop(ecat_api_credentials)

    
while True:
    #get = client.get('languages')
    get = client.get('products')
    pprint(get)
    ...
...