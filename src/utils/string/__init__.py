## \file hypotez/src/utils/string/__init__.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
.. module:: src.utils.string 
	:platform: Windows, Unix
	:synopsis:

"""


from .validator import ProductFieldsValidator
from .normalizer import (
						normalize_string,
						normalize_int,
						normalize_float,
						normalize_boolean,
						normalize_sql_date,
					)


