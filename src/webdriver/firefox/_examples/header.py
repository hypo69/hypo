## \file hypotez/src/webdriver/firefox/_examples/header.py
# -*- coding: utf-8 -*-

""" module: src.webdriver.firefox._examples """
MODE = 'debug'
""" module: src.webdriver.firefox._examples """
MODE = 'debug'
""" Установкя кораня проекта в системный путь """

import sys,os
from pathlib import Path
__root__ : Path = os.getcwd() [:os.getcwd().rfind(r'hypotez')+7]
sys.path.append (__root__)   
