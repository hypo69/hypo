## \file hypotez/pytest/src/utils/printer/__init__.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
.. module: pytest.src.utils.printer 
	:platform: Windows, Unix
	:synopsis:

"""
MODE = 'development'

"""
	:platform: Windows, Unix
	:synopsis:

"""

"""
	:platform: Windows, Unix
	:synopsis:

"""

"""
  :platform: Windows, Unix

"""
"""
  :platform: Windows, Unix
  :platform: Windows, Unix
  :synopsis:
"""MODE = 'development'
  
""" module: pytest.src.utils.printer """


""" This module initializes the `utils` package.

This module imports the `pprint` function from the `printer` module. It is designed to provide utility functions and tools to support various operations within the package.

Importing `pprint` allows for pretty-printing of data structures in a readable format.

"""
from .version import __version__, __doc__, __author__, __details__ 
from .test_printer import (test_pprint_dict, 
						   test_pprint_file, 
						   test_pprint_list, 
						   test_pprint_object, 
						   test_pprint_string
							)
