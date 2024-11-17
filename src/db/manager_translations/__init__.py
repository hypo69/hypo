## \file hypotez/src/db/manager_translations/__init__.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python
""" module: src.db.manager_translations """
MODE = 'development'


""" Менеджер переводов """
...

...
from packaging.version import Version
from .version import __version__, __doc__, __details__ 

from .product_translations import ProductTranslationsManager
from .category_translations import CategoryTranslationsManager