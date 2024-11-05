## \file ./src/webdriver/_experiments/start_driver.py
# -*- coding: utf-8 -*-
#! /venv/Scripts/python.exe
#! /usr/bin/python
import header
from src.webdriver import Driver, Firefox, Chrome, Edge


d = Driver(Chrome)
...

url = 'https://google.com'

d.get_url(url)

...



