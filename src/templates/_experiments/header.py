## \file hypotez/src/templates/_experiments/header.py
# -*- coding: utf-8 -*-

""" module: src.templates._experiments """
MODE = 'debug'
""" module: src.templates._experiments """
MODE = 'debug'
import os
import sys
from pathlib import Path

dir_root : Path = Path (os.getcwd()[:os.getcwd().rfind('hypotez')+7]) ## <- Корневая директория проекта
sys.path.append (str (dir_root) )  # Добавляю корневую директорию в sys.path
dir_src = Path (dir_root, 'src') 
sys.path.append (str (dir_root) ) # Добавляю рабочую директорию в sys.path 
 
from __init__ import gs
from src.endpoints.advertisement.facebook import  facebook

