## \file hypotez/src/bots/discord/header.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe

""" module: src.bots.discord """
MODE = 'debug'
""" module: src.bots.discord """
MODE = 'debug'


import sys,os
from pathlib import Path
__root__ : Path = os.getcwd() [:os.getcwd().rfind(r'hypotez')+7]
sys.path.append (__root__)     