## \file hypotez/src/suppliers/aliexpress/_experiments/alirequests.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe # <- venv win
#! venv/bin/python # <- venv linux/macos
#! py # <- system win
#! /usr/bin/python # <- system linux/macos
## ~~~~~~~~~~~~~
""" module: src.suppliers.aliexpress._experiments """
""" HERE SHOULD BE A DESCRIPTION OF THE MODULE OPERATION ! """

import header   

from src.webdriver import Driver, Chrome, Firefox

d = Driver(Firefox)
d.get_url(r"https://www.aliexpress.com")
...