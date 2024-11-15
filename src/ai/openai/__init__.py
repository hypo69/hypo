## \file hypotez/src/ai/openai/__init__.py
# -*- coding: utf-8 -*-

""" module: src.ai.openai """
MODE = 'debug'
""" module: src.ai.openai """
MODE = 'debug'
""" OpenAI """




from packaging.version import Version
from .version import __version__,  __doc__, __details__

from .translator import translate
from .model import OpenAIModel

