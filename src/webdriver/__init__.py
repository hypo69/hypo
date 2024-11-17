## \file hypotez/src/webdriver/__init__.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python
""" module: src.webdriver """
MODE = 'development'


#from .header import (gs,  __root__, __version__, __doc__, __details__, __project_name__, __author__, __copyright__, __cofee__)         

from .driver import Driver
from .chrome import Chrome
from .firefox import Firefox
from .edge import Edge
from .bs import BS
from .playwright import Playwrid
from .crawlee_python import CrawleePython

