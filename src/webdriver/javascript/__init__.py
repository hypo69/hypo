## \file hypotez/src/webdriver/javascript/__init__.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe # <- venv win
## ~~~~~~~~~~~~~
""" module: src.webdriver.javascript """
"""  Модуль Javasript
Выполнает операции javasript для драйвера
"""


from packaging.version import Version
from .version import __version__, __doc__, __details__  

from .js import JavaScript
