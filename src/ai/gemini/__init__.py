## \file hypotez/src/ai/gemini/__init__.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python
""" module: src.ai.gemini """
MODE = 'development'


""" AI Suppliers """
import sys
from pathlib import Path


from packaging.version import Version
from .version import __version__, __doc__, __details__, __root__ 

from .generative_ai import GoogleGenerativeAI
