## \file hypotez/src/utils/convertors/_experiments/header.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python
""" module: src.utils.convertors._experiments """
MODE = 'development'



""" Absolute path to modules  """

import sys,os
from pathlib import Path
__root__ : Path = os.getcwd() [:os.getcwd().rfind(r'hypotez')+7]
sys.path.append (__root__)  