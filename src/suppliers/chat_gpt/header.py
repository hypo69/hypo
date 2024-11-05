## \file ./src/suppliers/chat_gpt/header.py
# -*- coding: utf-8 -*-
#! /venv/Scripts/python.exe
#! /usr/bin/python
""" Модуль управления моделью OpenAI 
"""
# /path/to/interpreter/python

import sys,os
from pathlib import Path
__root__ : Path = os.getcwd() [:os.getcwd().rfind(r'hypotez')+7]
sys.path.append (__root__)     