#! /usr/bin/python
""" Aliexpress API wrapper"""
...
## \file /src/suppliers/aliexpress/api/__init__.py
# -*- coding: utf-8 -*-
# /path/to/interpreter/python
...
from packaging.version import Version
from .version import __version__, __doc__, __details__  

from .api import AliexpressApi
from . import models



