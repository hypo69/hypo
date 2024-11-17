## \file hypotez/src/utils/string/__init__.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python
""" module: src.utils.string """
MODE = 'development'



""" """
...

from packaging.version import Version
from .version import __version__, __doc__, __details__
...
from .formatter import StringFormatter
from .validator import ProductFieldsValidator
from .normalizer import StringNormalizer
from .url import extract_url_params, is_url

