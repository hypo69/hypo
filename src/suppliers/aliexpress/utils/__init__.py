""" модули управления рекламной кампанией Aliexpress:

 
"""
...
## \file src/suppliers/aliexpress/utils/__init__.py
# -*- coding: utf-8 -*-
# /path/to/interpreter/python
...
from packaging.version import Version
from .version import __version__, __doc__, __details__ 

from .extract_product_id import extract_prod_ids
from .ensure_https import ensure_https
from .locales import locales
