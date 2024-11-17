## \file hypotez/src/suppliers/bangood/__init__.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python
""" module: src.suppliers.bangood """
MODE = 'development'



"""  Постaвщик <i>wallmart</i>
"""

from packaging.version import Version
from .version import __version__, __doc__, __details__ 

from .graber import Graber


