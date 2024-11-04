""" вебдрайвер Firefox

This code defines a subclass of webdriver.Firefox called Firefox. 
It provides additional functionality such as the ability to launch Firefox 
in kiosk mode and the ability to set up a Firefox profile for the webdriver.

@image html class_firefox.png
"""
## \file ../src/webdriver/chrome/_experiments/start_driver.py
# -*- coding: utf-8 -*-
# /path/to/interpreter/python

import os
from pathlib import Path
from types import SimpleNamespace
from typing import Optional

import header
from header import __root__
from src.webdriver import  Driver, Firefox, Chrome
from src.utils import j_loads_ns
from src.logger import logger

__bin__ =  Path(__root__, 'bin')
__src__ = Path(__root__, 'src')


#f = Firefox()
#c = Chrome()
d = Driver(Chrome)
...