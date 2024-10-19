## \file ../header.py
# -*- coding: utf-8 -*-
# /path/to/interpreter/python
"""! Absolute path to modules  """

import sys,os
from pathlib import Path
__root__ : Path = os.getcwd() [:os.getcwd().rfind(r'hypotez')+7]
sys.path.append (__root__)  