## \file src/suppliers/amazon/__init__.py
## \file ../src/suppliers/amazon/__init__.py
# -*- coding: utf-8 -*-
# /path/to/interpreter/python
"""  Поставщик <I>amazon.com</I>

 
 @section libs imports:
  - .login 
  - .update_product_fields 
  - .via_webdriver 
  - src.gs 
  - src.gs 
  - src.gs 
  - webdriver 
  
Author(s):
  - Created by [Name] [Last Name] on 07.11.2023 .
"""
...
from packaging.version import Version
from .version import __version__, __doc__, __details__  

from .api import api
#from .api import start as apistart
from .graber import async_grab_page
from .login import loginn