## \file hypotez/src/gui/context_menu/tkinter/header.py
# -*- coding: utf-8 -*-

""" module: src.gui.context_menu.tkinter """
MODE = 'debug'
""" module: src.gui.context_menu.tkinter """
MODE = 'debug'


import sys,os
from pathlib import Path
__root__ : Path = os.getcwd() [:os.getcwd().rfind(r'hypotez')+7]
sys.path.append (__root__)  