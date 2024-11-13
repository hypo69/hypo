## \file hypotez/src/webdriver/_experiments/start_driver.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe # <- venv win
## ~~~~~~~~~~~~~
""" module: src.webdriver._experiments """
import header
from src.webdriver import Driver, Firefox, Chrome, Edge


d = Driver(Chrome)
...

url = 'https://google.com'

d.get_url(url)

...



