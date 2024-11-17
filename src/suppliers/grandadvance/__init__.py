## \file hypotez/src/suppliers/grandadvance/__init__.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python
""" module: src.suppliers.grandadvance """
MODE = 'development'



"""  Постaвщик <i>wallmart</i>
"""

from packaging.version import Version
from .version import __version__, __doc__, __details__ 

from .graber import Graber


