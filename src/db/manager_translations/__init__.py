﻿""" Менеджер переводов """
...
## \file ../src/db/manager_translations/__init__.py
# -*- coding: utf-8 -*-
# /path/to/interpreter/python
...
from packaging.version import Version
from .version import __version__, __doc__, __details__ 

from .product_translations import ProductTranslationsManager
from .category_translations import CategoryTranslationsManager