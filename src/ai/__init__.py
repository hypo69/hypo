## \file hypotez/src/ai/__init__.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe # <- venv win
## ~~~~~~~~~~~~~
""" module: src.ai """
""" AI Suppliers """



from packaging.version import Version
from .version import __version__, __doc__, __details__

from .gemini import GoogleGenerativeAI
from .openai import OpenAIModel