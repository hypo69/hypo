

"""  Прослойка между разными вериями модулей взаимммодействия с престашоп 
Есть проблемы с аутентификацией на сайте клиента. Вполне возможно, 
что это связано с настройками PHP. В восьмой версии (e-cat.co.il) я получаю 401
"""

import header
from header import  ecat_api_credentials, emil_api_credentials
from src import gs
from prestapyt import PrestaShopWebServiceDict
from src.endpoints.PrestaShop.presta_apis.client import PrestaShop 
from src.endpoints.PrestaShop.presta_apis.presta_python_api_v2 import PrestaAPIV2
from src.endpoints.PrestaShop.presta_apis.presta_python_api_v3 import PrestaAPIV3, PrestaAPIV3Format, PrestaShopException, PrestaShopAuthenticationError


connector = PrestaShop(ecat_api_credentials)
...