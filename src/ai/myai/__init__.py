## \file hypotez/src/ai/myai/__init__.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe

""" module: src.ai.myai """
MODE = 'debug'
""" module: src.ai.myai """
MODE = 'debug'
""" AI Suppliers """



from packaging.version import Version
from .version import __version__, __doc__, __details__

from .gooogle_generativeai import GoogleGenerativeAI
from .openai import OpenAIModel