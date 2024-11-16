## \file hypotez/src/endpoints/prestashop/_experiments/notebook_header.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe

""" module: src.endpoints.prestashop._experiments """
MODE = 'debug'
""" module: src.endpoints.prestashop._experiments """
MODE = 'debug'
import sys
import os
from pathlib import Path

dir_root : Path = Path (os.getcwd()[:os.getcwd().rfind('hypotez')+7])
sys.path.append (str (dir_root) )  # Добавляю корневую папку в sys.path
dir_src = Path (dir_root, 'src')
sys.path.append (str (dir_root) ) 

