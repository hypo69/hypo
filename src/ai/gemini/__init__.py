## \file hypotez/src/ai/gemini/__init__.py
# -*- coding: utf-8 -*-

""" module: src.ai.gemini """
MODE = 'debug'
""" module: src.ai.gemini """
MODE = 'debug'
""" AI Suppliers """
import sys
from pathlib import Path


from packaging.version import Version
from .version import __version__, __doc__, __details__, __root__ 

from .generative_ai import GoogleGenerativeAI
