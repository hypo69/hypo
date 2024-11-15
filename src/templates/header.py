## \file hypotez/src/templates/header.py
# -*- coding: utf-8 -*-

""" module: src.templates """
MODE = 'debug'
""" module: src.templates """
MODE = 'debug'
"""module: `src.<module_name>`"""
from pathlib import Path
import sys

src_path = str(Path(__file__).resolve().parent.parent.parent)
# HERE MUST BE RELATIVE TO ROOT--------^^^^^^^^^^^^^^^^^^^^^

if src_path not in sys.path:
    sys.path.append(src_path)

from src.credentials import gs
