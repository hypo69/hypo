## \file ../src/prestashop/api/_experiments/ping.py
## \file src/prestashop/api/_experiments/ping.py
import header
from header import  ecat_api_credentials, emil_api_credentials
from header import pprint, jprint
from src import gs
from src.prestashop.presta_apis.client import Prestashop

client = Prestashop(ecat_api_credentials)

    
while True:
    #get = client.get('languages')
    get = client.get('products')
    pprint(get)
    ...
...