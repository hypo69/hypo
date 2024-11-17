## \file hypotez/src/ai/openai/model/__init__.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python
""" module: src.ai.openai.model """
MODE = 'development'


...

from packaging.version import Version
from .version import (__project_name__, 
                      __version__, 
                      __doc__, 
                      __details__, 
                      __author__
                    )

from .training import OpenAIModel



