## \file src/suppliers/cdata/__init__.py
## \file ../src/suppliers/cdata/__init__.py
# -*- coding: utf-8 -*-
"""  Поставщик <I>cdata.co.il</I>
@details execute `cdata` via vebdriver

@todo `cdata` не реализован

@section libs imports:
- login 
"""
...
from packaging.version import Version
from .version import __version__, __doc__, __details__  

from .login import login
