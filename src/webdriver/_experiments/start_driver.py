## \file hypotez/src/webdriver/_experiments/start_driver.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python
""" module: src.webdriver._experiments """
MODE = 'development'


import header
from src.webdriver import Driver, Firefox, Chrome, Edge


d = Driver(Chrome)
...

url = 'https://google.com'

d.get_url(url)

...



