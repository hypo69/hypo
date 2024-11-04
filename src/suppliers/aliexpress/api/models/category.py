## \file src/suppliers/aliexpress/api/models/category.py
## \file src/suppliers/aliexpress/api/models/category.py
class Category:
    category_id: int
    category_name: str


class ChildCategory(Category):
    parent_category_id: int

