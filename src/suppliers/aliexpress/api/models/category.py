## \file hypotez/src/suppliers/aliexpress/api/models/category.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe
#! venv/bin/python
""" module: src.suppliers.aliexpress.api.models """
MODE = 'development'


class Category:
    category_id: int
    category_name: str


class ChildCategory(Category):
    parent_category_id: int

