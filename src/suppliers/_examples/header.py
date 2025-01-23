## \file /src/suppliers/_examples/header.py
# -*- coding: utf-8 -*-

#! .pyenv/bin/python3

"""
.. module:: src.suppliers._examples 
	:platform: Windows, Unix
	:synopsis:

"""


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
"""
  
""" module: src.suppliers._examples """


import os
import sys
from pathlib import Path

dir_root : Path = Path (os.getcwd()[:os.getcwd().rfind('hypotez')+7]) ## <- Корневая директория проекта
sys.path.append (str (dir_root) )  # Добавляю корневую директорию в sys.path
dir_src = Path (dir_root, 'src') 
sys.path.append (str (dir_root) ) # Добавляю рабочую директорию в sys.path 
 


