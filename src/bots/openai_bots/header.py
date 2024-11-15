## \file hypotez/src/bots/openai_bots/header.py
# -*- coding: utf-8 -*-

""" module: src.bots.openai_bots """
MODE = 'debug'
""" module: src.bots.openai_bots """
MODE = 'debug'


import sys,os
from pathlib import Path
__root__ : Path = os.getcwd() [:os.getcwd().rfind(r'hypotez')+7]
sys.path.append (__root__)     