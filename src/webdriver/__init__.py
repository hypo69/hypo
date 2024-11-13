## \file hypotez/src/webdriver/__init__.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe # <- venv win
## ~~~~~~~~~~~~~
""" module: src.webdriver """

"""  Модуль вебдрайвера
Я объединил в класс `Driver` все, что взаимодействует по протоколу `HTTP`:
- `selenium`
- `Mozilla/Chrome/Edge..` вебдрайвер 
- моя реализация работы с локаторами `execute_locator.py`


@image html webdriver.png                                     Skip to main panel


@todo
    1. У меня не получается сделать расширение под Firefox
"""


from packaging.version import Version
from .version import __doc__, __details__, __version__  

from .driver import Driver
from .chrome import Chrome
from .firefox import Firefox
from .edge import Edge
from .bs import BS
from .playwright import Playwrid
from .crawlee_python import CrawleePython

