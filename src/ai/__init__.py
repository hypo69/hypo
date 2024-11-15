## \file hypotez/src/ai/__init__.py
# -*- coding: utf-8 -*-

""" module: src.ai """
MODE = 'debug'
""" module: src.ai """
MODE = 'debug'
""" AI Suppliers """



from packaging.version import Version
from .version import __version__, __doc__, __details__

from .gemini import GoogleGenerativeAI
from .openai import OpenAIModel