## \file hypotez/src/ai/gemini/__init__.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe # <- venv win
#! venv/bin/python # <- venv linux/macos
#! py # <- system win
#! /usr/bin/python # <- system linux/macos
## ~~~~~~~~~~~~~
""" module: src.ai.gemini """
""" AI Suppliers """
import sys
from pathlib import Path


from packaging.version import Version
from .version import __version__, __doc__, __details__, __root__ 

from .generative_ai import GoogleGenerativeAI
