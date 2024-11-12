## \file hypotez/pytest/src/utils/printer/__init__.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe # <- venv win
#! venv/bin/python # <- venv linux/macos
#! py # <- system win
#! /usr/bin/python # <- system linux/macos
## ~~~~~~~~~~~~~
""" module: pytest.src.utils.printer """
"""! This module initializes the `utils` package.

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
