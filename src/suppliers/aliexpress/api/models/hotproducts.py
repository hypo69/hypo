#! /usr/bin/python
## \file /src/suppliers/aliexpress/api/models/hotproducts.py
## \file src/suppliers/aliexpress/api/models/hotproducts.py
from .product import Product
from typing import List


class HotProductsResponse:
    current_page_no: int
    current_record_count: int
    total_record_count: int
    products: List[Product]

