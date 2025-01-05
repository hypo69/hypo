## \file /src/suppliers/aliexpress/api/helpers/categories.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe # <- venv win
## ~~~~~~~~~~~~~
""" module: src.suppliers.aliexpress.api.helpers """

"""  функции для фильтрации категорий и подкатегорий API Aliexpress"""
from typing import List, Union
from .. import models
#from src.suppliers.aliexpress.api.api import models

def filter_parent_categories(categories: List[models.Category | models.ChildCategory]) -> List[models.Category]:
    """
    Filters and returns a list of categories that do not have a parent category.

    @param categories: List of category or child category objects.
    @return: List of category objects without a parent category.
    """
    filtered_categories = []
    
    if isinstance(categories, (str, int, float)):
        categories = [categories]  # Convert to list if a single non-category value is passed.

    for category in categories:
        if not hasattr(category, 'parent_category_id'):
            filtered_categories.append(category)

    return filtered_categories

def filter_child_categories(categories: List[models.Category | models.ChildCategory],
                            parent_category_id: int) -> List[models.ChildCategory]:
    """
    Filters and returns a list of child categories that belong to the specified parent category.

    @param categories: List of category or child category objects.
    @param parent_category_id: The ID of the parent category to filter child categories by.
    @return: List of child category objects with the specified parent category ID.
    """
    filtered_categories = []
    
    if isinstance(categories, (str, int, float)):
        categories = [categories]  # Convert to list if a single non-category value is passed.

    for category in categories:
        if hasattr(category, 'parent_category_id') and category.parent_category_id == parent_category_id:
            filtered_categories.append(category)

    return filtered_categories

