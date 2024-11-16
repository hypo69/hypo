## \file hypotez/src/webdriver/chrome/_experiments/header.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe

""" module: src.webdriver.chrome._experiments """
MODE = 'debug'
""" module: src.webdriver.chrome._experiments """
MODE = 'debug'
""" Установкя кораня проекта в системный путь """

import sys,os
from pathlib import Path
__root__ : Path = os.getcwd() [:os.getcwd().rfind(r'hypotez')+7]
sys.path.append (__root__)   
