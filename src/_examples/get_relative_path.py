## \file /src/utils/_examples/get_relative_path.py
# -*- coding: utf-8 -*-

#! .pyenv/bin/python3

"""
.. module:: src.utils._examples.get_relative_path 
	:platform: Windows, Unix
	:synopsis:

"""
from pathlib import Path



import header
from src.utils.path import get_relative_path

relative_path = get_relative_path(Path(__file__).resolve(), 'hypotez')
print(relative_path)


