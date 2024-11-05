#! /usr/bin/python
﻿"""  Модуль Javasript
Выполнает операции javasript для драйвера
"""
## \file /src/webdriver/javascript/__init__.py
# -*- coding: utf-8 -*-
# /path/to/interpreter/python

from packaging.version import Version
from .version import __version__, __doc__, __details__  

from .js import JavaScript
