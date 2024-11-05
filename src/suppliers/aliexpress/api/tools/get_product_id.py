#! /usr/bin/python
## \file /src/suppliers/aliexpress/api/tools/get_product_id.py
## \file src/suppliers/aliexpress/api/tools/get_product_id.py
"""Some useful tools."""

from ..errors import ProductIdNotFoundException
from src.suppliers.aliexpress.utils.extract_product_id import extract_prod_ids
import re


def get_product_id(raw_product_id: str) -> str:
    """Returns the product ID from a given text. Raises ProductIdNotFoundException on fail."""
    return extract_prod_ids(raw_product_id)
    # if re.search(r'^[0-9]*$', text):
    #     return text

    # # Extract product ID from URL
    # asin = re.search(r'(\/)([0-9]*)(\.)', text)
    # if asin:
    #     return asin.group(2)
    # else:
    #     raise ProductIdNotFoundException('Product id not found: ' + text)

