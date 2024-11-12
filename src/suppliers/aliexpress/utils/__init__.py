## \file hypotez/src/suppliers/aliexpress/utils/__init__.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe # <- venv win
#! venv/bin/python # <- venv linux/macos
#! py # <- system win
#! /usr/bin/python # <- system linux/macos
## ~~~~~~~~~~~~~
""" module: src.suppliers.aliexpress.utils """
""" модули управления рекламной кампанией Aliexpress:

 
"""
...

...
from packaging.version import Version
from .version import __version__, __doc__, __details__ 

from .extract_product_id import extract_prod_ids
from .ensure_https import ensure_https
from .locales import locales
