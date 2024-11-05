## \file ./src/endpoints/prestashop/api/_experiments/ping.py
# -*- coding: utf-8 -*-
#! /venv/Scripts/python.exe
#! /usr/bin/python
import header
from header import  ecat_api_credentials, emil_api_credentials
from header import pprint, jprint
from src import gs
from src.endpoints.prestashop.presta_apis.client import Prestashop

client = Prestashop(ecat_api_credentials)

    
while True:
    #get = client.get('languages')
    get = client.get('products')
    pprint(get)
    ...
...