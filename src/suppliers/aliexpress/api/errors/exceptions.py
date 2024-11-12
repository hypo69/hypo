## \file hypotez/src/suppliers/aliexpress/api/errors/exceptions.py
# -*- coding: utf-8 -*-
#! venv/Scripts/python.exe # <- venv win
#! venv/bin/python # <- venv linux/macos
#! py # <- system win
#! /usr/bin/python # <- system linux/macos
## ~~~~~~~~~~~~~
""" module: src.suppliers.aliexpress.api.errors """
"""Custom exceptions module"""


class AliexpressException(Exception):
    """Common base class for all AliExpress API exceptions."""
    def __init__(self, reason: str):
        super().__init__()
        self.reason = reason

    def __str__(self) -> str:
        return '%s' % self.reason


class InvalidArgumentException(AliexpressException):
    """Raised when arguments are not correct."""
    pass


class ProductIdNotFoundException(AliexpressException):
    """Raised if the product ID is not found."""
    pass

class ApiRequestException(AliexpressException):
    """Raised if the request to AliExpress API fails"""
    pass

class ApiRequestResponseException(AliexpressException):
    """Raised if the request response is not valid"""
    pass

class ProductsNotFoudException(AliexpressException):
    """Raised if no products are found"""
    pass

class CategoriesNotFoudException(AliexpressException):
    """Raised if no categories are found"""
    pass

class InvalidTrackingIdException(AliexpressException):
    """Raised if the tracking ID is not present or invalid"""
    pass

