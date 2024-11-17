## \file hypotez/src/ai/openai/__init__.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python
""" module: src.ai.openai """
MODE = 'development'


""" OpenAI """




from packaging.version import Version
from .version import __version__,  __doc__, __details__

from .translator import translate
from .model import OpenAIModel

