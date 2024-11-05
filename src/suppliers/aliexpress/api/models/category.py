## \file ./src/suppliers/aliexpress/api/models/category.py
# -*- coding: utf-8 -*-
#! /venv/Scripts/python.exe
#! /usr/bin/python
class Category:
    category_id: int
    category_name: str


class ChildCategory(Category):
    parent_category_id: int

