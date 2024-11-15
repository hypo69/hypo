## \file hypotez/src/ai/helicone/header.py
# -*- coding: utf-8 -*-

""" module: src.ai.helicone """
MODE = 'debug'
""" module: src.ai.helicone """
MODE = 'debug'

""" Absolute path to modules  """

import sys,os
from pathlib import Path
__root__ : Path = os.getcwd() [:os.getcwd().rfind(r'hypotez')+7]
sys.path.append (__root__)  