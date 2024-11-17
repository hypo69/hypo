## \file hypotez/src/suppliers/aliexpress/_experiments/header.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python
""" module: src.suppliers.aliexpress._experiments """
MODE = 'development'


""" Header  """



import sys,os
from pathlib import Path
__root__ : Path = os.getcwd() [:os.getcwd().rfind(r'hypotez')+7]
sys.path.append (__root__)  