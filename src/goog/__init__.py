#! /usr/bin/python
﻿## \file src/goog/__init__.py
## \file /src/goog/__init__.py
# -*- coding: utf-8 -*-
# /path/to/interpreter/python
""" Google API.
ИИ Generative AI находится в src.ai."""

from packaging.version import Version
from .version import __version__, __doc__, __details__ 

from .spreadsheet import SpreadSheet
