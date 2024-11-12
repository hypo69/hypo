## \file hypotez/src/endpoints/prestashop/api/_experiments/ide_experiments_PrestaAPIV.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe # <- venv win
#! venv/bin/python # <- venv linux/macos
#! py # <- system win
#! /usr/bin/python # <- system linux/macos
## ~~~~~~~~~~~~~
""" module: src.endpoints.prestashop.api._experiments """
"""  Прослойка между разными вериями модулей взаимммодействия с престашоп 
Есть проблемы с аутентификацией на сайте клиента. Вполне возможно, 
что это связано с настройками PHP. В восьмой версии (e-cat.co.il) я получаю 401
"""

import header
from header import  ecat_api_credentials, emil_api_credentials
from src import gs
from prestapyt import PrestaShopWebServiceDict
from src.endpoints.prestashop.presta_apis.client import Prestashop 
from src.endpoints.prestashop.presta_apis.presta_python_api_v2 import PrestaAPIV2
from src.endpoints.prestashop.presta_apis.presta_python_api_v3 import PrestaAPIV3, PrestaAPIV3Format, PrestaShopException, PrestaShopAuthenticationError


connector = Prestashop(ecat_api_credentials)
...