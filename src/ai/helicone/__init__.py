#! /usr/bin/python
""" OpenAI """

## \file /src/ai/helicone/__init__.py
# -*- coding: utf-8 -*-
# /path/to/interpreter/python


from packaging.version import Version
from .version import __version__,  __doc__, __details__

from .translator import translate
from .model import OpenAIModel

