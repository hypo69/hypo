## \file hypotez/src/suppliers/bangood/__init__.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python
""" module: src.suppliers.bangood """
MODE = 'development'


from .graber import Graber
from .scenario import get_list_categories_from_site, get_list_products_in_category


