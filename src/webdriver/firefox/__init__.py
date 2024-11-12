## \file hypotez/src/webdriver/firefox/__init__.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe # <- venv win
#! venv/bin/python # <- venv linux/macos
#! py # <- system win
#! /usr/bin/python # <- system linux/macos
## ~~~~~~~~~~~~~
""" module: src.webdriver.firefox """
""" Оболочка для Firefox"""

...
from packaging.version import Version
from .version import __version__, __driver_version__, __name__, __doc__, __details__, __annotations__,  __author__ 

from .firefox import Firefox