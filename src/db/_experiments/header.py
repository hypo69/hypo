## \file hypotez/src/db/_experiments/header.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe

""" module: src.db._experiments """
MODE = 'debug'
""" module: src.db._experiments """
MODE = 'debug'
""" @namespace src.db._experiments """
import sys, os
from pathlib import Path
# ----------------
dir_root : Path = Path (os.getcwd()[:os.getcwd().rfind('hypotez')+7])
sys.path.append (str (dir_root) )  # Добавляю корневую папку в sys.path
dir_src = Path (dir_root, 'src')
sys.path.append (str (dir_root) ) 
# ----------------
from src import gss