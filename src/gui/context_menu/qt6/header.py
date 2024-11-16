## \file hypotez/src/gui/context_menu/qt6/header.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe

""" module: src.gui.context_menu.qt6 """
MODE = 'debug'
""" module: src.gui.context_menu.qt6 """
MODE = 'debug'


import sys,os
from pathlib import Path
__root__ : Path = os.getcwd() [:os.getcwd().rfind(r'hypotez')+7]
sys.path.append (__root__)  