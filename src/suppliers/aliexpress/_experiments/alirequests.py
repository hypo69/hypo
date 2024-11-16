## \file hypotez/src/suppliers/aliexpress/_experiments/alirequests.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe

""" module: src.suppliers.aliexpress._experiments """
MODE = 'debug'
""" module: src.suppliers.aliexpress._experiments """
MODE = 'debug'
""" HERE SHOULD BE A DESCRIPTION OF THE MODULE OPERATION ! """

import header   

from src.webdriver import Driver, Chrome, Firefox

d = Driver(Firefox)
d.get_url(r"https://www.aliexpress.com")
...