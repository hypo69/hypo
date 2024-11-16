## \file hypotez/src/suppliers/grandadvance/__init__.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe

""" module: src.suppliers.grandadvance """
MODE = 'debug'
""" module: src.suppliers.grandadvance """
MODE = 'debug'

"""  Постaвщик <i>wallmart</i>
"""

from packaging.version import Version
from .version import __version__, __doc__, __details__ 

from .graber import Graber


