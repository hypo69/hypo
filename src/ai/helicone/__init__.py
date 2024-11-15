## \file hypotez/src/ai/helicone/__init__.py
# -*- coding: utf-8 -*-

""" module: src.ai.helicone """
MODE = 'debug'
""" module: src.ai.helicone """
MODE = 'debug'
""" OpenAI """




from packaging.version import Version
from .version import __version__,  __doc__, __details__

from .translator import translate
from .model import OpenAIModel

