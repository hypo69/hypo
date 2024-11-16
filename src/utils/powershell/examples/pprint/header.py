## \file hypotez/src/utils/powershell/examples/pprint/header.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe

""" module: src.utils.powershell.examples.pprint """
MODE = 'debug'
""" module: src.utils.powershell.examples.pprint """
MODE = 'debug'

"""! Absolute path to modules  """

import sys,os
from pathlib import Path
__root__ : Path = os.getcwd() [:os.getcwd().rfind(r'hypotez')+7]
sys.path.append (__root__)  