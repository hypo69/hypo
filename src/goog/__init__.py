## \file hypotez/src/goog/__init__.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python
""" module: src.goog """
MODE = 'development'



""" Google API.
ИИ Generative AI находится в src.ai."""

from packaging.version import Version
from .version import __version__, __doc__, __details__ 

from .spreadsheet import SpreadSheet
