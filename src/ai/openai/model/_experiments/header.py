## \file hypotez/src/ai/openai/model/_experiments/header.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe # <- venv win
## ~~~~~~~~~~~~~
""" module: src.ai.openai.model._experiments """
""" Модуль управления моделью OpenAI 
"""


import sys,os
from pathlib import Path
__root__ : Path = os.getcwd() [:os.getcwd().rfind(r'hypotez')+7]
ffmpeg: Path = Path( __root__ , 'bin' , 'ffmpeg' , 'bin' , 'ffmpeg.exe') 
sys.path.append (__root__)   
sys.path.append (ffmpeg)