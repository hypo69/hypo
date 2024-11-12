## \file hypotez/src/suppliers/ebay/__init__.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe # <- venv win
#! venv/bin/python # <- venv linux/macos
#! py # <- system win
#! /usr/bin/python # <- system linux/macos
## ~~~~~~~~~~~~~
""" module: src.suppliers.ebay """

"""  Постaвщик <i>wallmart</i>
"""

from packaging.version import Version
from .version import __version__, __doc__, __details__ 

from .graber import Graber


