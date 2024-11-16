## \file hypotez/src/ai/openai/header.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe

""" module: src.ai.openai """
MODE = 'debug'
""" module: src.ai.openai """
MODE = 'debug'


import sys,os
from pathlib import Path
__root__ : Path = os.getcwd() [:os.getcwd().rfind(r'hypotez')+7]
sys.path.append (__root__)  