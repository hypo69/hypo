﻿""" Обёртка для Хрома """
...
## \file ../src/webdriver/chrome/__init__.py
# -*- coding: utf-8 -*-
# /path/to/interpreter/python
...
from packaging.version import Version
from .version import __version__, __driver_version__, __name__, __doc__, __details__, __annotations__,  __author__

from .chrome import Chrome