#! /usr/bin/python
﻿""" Google API """

## \file /src/goog/spreadsheet/__init__.py
# -*- coding: utf-8 -*-
# /path/to/interpreter/python

from packaging.version import Version
from .version import __version__, __doc__, __details__ 

from .spreadsheet import SpreadSheet
from .reach_spreadsheet import ReachSpreadsheet