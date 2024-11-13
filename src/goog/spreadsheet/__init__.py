## \file hypotez/src/goog/spreadsheet/__init__.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe # <- venv win
## ~~~~~~~~~~~~~
""" module: src.goog.spreadsheet """
""" Google API """



from packaging.version import Version
from .version import __version__, __doc__, __details__ 

from .spreadsheet import SpreadSheet
from .reach_spreadsheet import ReachSpreadsheet