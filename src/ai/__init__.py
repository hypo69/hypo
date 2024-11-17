## \file hypotez/src/ai/__init__.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python
""" module: src.ai """
MODE = 'development'


from .gemini import GoogleGenerativeAI
from .openai import OpenAIModel