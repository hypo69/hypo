""" AI Suppliers """

## \file src/ai/myai/__init__.py
# -*- coding: utf-8 -*-
# /path/to/interpreter/python

from packaging.version import Version
from .version import __version__, __doc__, __details__

from .gooogle_generativeai import GoogleGenerativeAI
from .openai import OpenAIModel