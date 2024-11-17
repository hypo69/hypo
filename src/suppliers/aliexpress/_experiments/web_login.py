## \file hypotez/src/suppliers/aliexpress/_experiments/web_login.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python
""" module: src.suppliers.aliexpress._experiments """
MODE = 'development'


""" Aliexpress Проверки логин, кукис итп. """



import header
from pathlib import Path
import pickle
import requests

from src import gs
from src.suppliers import Supplier
from src.utils import pprint

a = Supplier('aliexpress')

d = a.driver
d.get_url('https://aliexpress.com')