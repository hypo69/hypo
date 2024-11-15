## \file hypotez/src/suppliers/aliexpress/api/models/category.py
# -*- coding: utf-8 -*-

""" module: src.suppliers.aliexpress.api.models """
MODE = 'debug'
""" module: src.suppliers.aliexpress.api.models """
MODE = 'debug'
class Category:
    category_id: int
    category_name: str


class ChildCategory(Category):
    parent_category_id: int

