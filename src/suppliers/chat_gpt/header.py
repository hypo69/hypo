## \file hypotez/src/suppliers/chat_gpt/header.py
# -*- coding: utf-8 -*-

""" module: src.suppliers.chat_gpt """
MODE = 'debug'
""" module: src.suppliers.chat_gpt """
MODE = 'debug'
""" Модуль управления моделью OpenAI 
"""


import sys,os
from pathlib import Path
__root__ : Path = os.getcwd() [:os.getcwd().rfind(r'hypotez')+7]
sys.path.append (__root__)     