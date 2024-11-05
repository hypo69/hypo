## \file ./src/suppliers/aliexpress/_experiments/alirequests.py
# -*- coding: utf-8 -*-
#! /venv/Scripts/python.exe
#! /usr/bin/python
""" HERE SHOULD BE A DESCRIPTION OF THE MODULE OPERATION ! """
# /path/to/interpreter/python
import header   

from src.webdriver import Driver, Chrome, Firefox

d = Driver(Firefox)
d.get_url(r"https://www.aliexpress.com")
...