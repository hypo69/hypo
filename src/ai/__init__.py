## \file hypotez/src/ai/__init__.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
.. module: src.ai 
	:platform: Windows, Unix
	:synopsis:

"""
MODE = 'dev'


from .gemini import GoogleGenerativeAI
from .openai import OpenAIModel