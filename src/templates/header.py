## \file hypotez/src/templates/header.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
.. module: src.templates 
	:platform: Windows, Unix
	:synopsis:

"""
MODE = 'dev'

"""
	:platform: Windows, Unix
	:synopsis:

"""

"""
	:platform: Windows, Unix
	:synopsis:

"""

"""
  :platform: Windows, Unix

"""
"""
  :platform: Windows, Unix
  :platform: Windows, Unix
  :synopsis:
"""MODE = 'dev'
  
""" module: src.templates """


from pathlib import Path
import sys

src_path = str(Path(__file__).resolve().parent.parent.parent)
# HERE MUST BE RELATIVE TO ROOT--------^^^^^^^^^^^^^^^^^^^^^

if src_path not in sys.path:
    sys.path.append(src_path)

from src.credentials import gs
