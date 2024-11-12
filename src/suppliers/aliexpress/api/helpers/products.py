## \file hypotez/src/suppliers/aliexpress/api/helpers/products.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe # <- venv win
#! venv/bin/python # <- venv linux/macos
#! py # <- system win
#! /usr/bin/python # <- system linux/macos
## ~~~~~~~~~~~~~
""" module: src.suppliers.aliexpress.api.helpers """
def parse_product(product):
    product.product_small_image_urls = product.product_small_image_urls.string
    return product


def parse_products(products):
    new_products = []

    for product in products:
        new_products.append(parse_product(product))

    return new_products

