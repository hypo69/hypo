## \file hypotez/src/utils/string/__init__.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
.. module: src.utils.string 
	:platform: Windows, Unix
	:synopsis:

"""
MODE = 'development'

from .formatter import StringFormatter
from .validator import ProductFieldsValidator
from .normalizer import StringNormalizer
from .url import extract_url_params, is_url

