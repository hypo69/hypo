## \file ./src/webdriver/crawlee_python/__init__.py
# -*- coding: utf-8 -*-
#! /venv/Scripts/python.exe
#! /usr/bin/python
""" Обёртка для Crawlee"""
# /path/to/interpreter/python
...
from packaging.version import Version
from .version import __version__, __driver_version__, __name__, __doc__, __details__, __annotations__,  __author__ 

from .crawlee_python import CrawleePython
