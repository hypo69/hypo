

import header
from header import  ecat_api_credentials, emil_api_credentials
from header import pprint, jprint
from src import gs
from src.endpoints.PrestaShop.presta_apis.client import PrestaShop

client = PrestaShop(ecat_api_credentials)

    
while True:
    #get = client.get('languages')
    get = client.get('products')
    pprint(get)
    ...
...