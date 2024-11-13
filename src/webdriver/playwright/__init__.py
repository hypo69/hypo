## \file hypotez/src/webdriver/playwright/__init__.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe # <- venv win
## ~~~~~~~~~~~~~
""" module: src.webdriver.playwright """
""" Обёртка для Playwrid crawler"""

...
from packaging.version import Version
from .version import __version__, __driver_version__, __name__, __doc__, __details__, __annotations__,  __author__ 

from .playwrid import Playwrid
