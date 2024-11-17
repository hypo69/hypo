## \file hypotez/src/webdriver/crawlee_python/_experiments/header.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python
""" module: src.webdriver.crawlee_python._experiments """
MODE = 'development'


""" Эксперименты с библиотекой crawlee-python """

import sys,os
from pathlib import Path
__root__ : Path = os.getcwd() [:os.getcwd().rfind(r'hypotez')+7]
sys.path.append (__root__)     
 


