## \file hypotez/src/goog/drive/header.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe

""" module: src.goog.drive """
MODE = 'debug'
""" module: src.goog.drive """
MODE = 'debug'


import sys,os
from pathlib import Path
__root__ : Path = os.getcwd() [:os.getcwd().rfind(r'hypotez')+7]
sys.path.append (__root__)  