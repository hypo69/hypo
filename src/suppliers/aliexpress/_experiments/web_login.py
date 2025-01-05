## \file /src/suppliers/aliexpress/_experiments/web_login.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python/python3.12

"""
.. module:: src.suppliers.aliexpress._experiments 
	:platform: Windows, Unix
	:synopsis:

"""


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
"""
  
""" module: src.suppliers.aliexpress._experiments """


""" Aliexpress Проверки логин, кукис итп. """



import header
from pathlib import Path
import pickle
import requests

from src import gs
from src.suppliers import Supplier
from src.utils.printer import pprint

a = Supplier('aliexpress')

d = a.driver
d.get_url('https://aliexpress.com')