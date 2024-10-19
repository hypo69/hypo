""" Progam Exceptions """
## \file ../src/logger/exceptions.py
# -*- coding: utf-8 -*-
# /path/to/interpreter/python
...
from typing import Dict, List, Any
from src.logger import logger
from selenium.common.exceptions import WebDriverException as WDriverException
from pykeepass.exceptions import CredentialsError, BinaryError, HeaderChecksumError, PayloadChecksumError, UnableToSendToRecycleBin
...

e = Exception


# class CustomException(Exception):
#     """Base class for custom exceptions."""
#     ...
#     def __init__(self, message, e: Exception = None, exc_info:bool = True):
#         super().__init__(message, e, exc_info)
#         # Add logic here
#     ...

class CustomException(Exception):
    """Base custom exception."""
    ...
    def __init__(self, message, e: Exception = None, exc_info:bool = True):
        super().__init__(message)
        self.original_exception = e
        self.exc_info = exc_info
        # Add logic here
    ...

class FileNotFoundError(CustomException, IOError):
    """Exception related to a file not found."""
    def __init__(self, message, e: Exception = None, exc_info:bool = True):
        super().__init__(message, e, exc_info)
        # Add logic here
    
class ProductFieldException(CustomException):
    """Exception related to product fields."""
    ...
    def __init__(self, message, e: Exception = None, exc_info:bool = True):
        super().__init__(message, e, exc_info)
        # Add logic here
    ...

class KeePassException(CredentialsError, BinaryError, HeaderChecksumError, PayloadChecksumError, UnableToSendToRecycleBin):
    """Exception related to connection problems with Kee... database."""
    ...
    def __init__(self, message, e: Exception = None, exc_info:bool = True):
        super().__init__(message, e, exc_info)
        # Add logic here
    ...

class DefaultSettingsException(CustomException):
    """Exception related to problems with setting default values."""
    ...
    def __init__(self, message, e: Exception = None, exc_info:bool = True):
        super().__init__(message, e, exc_info)
        # Add logic here
    ...

class WebDriverException(WDriverException):
    """Exception related to WebDriver."""
    ...
    def __init__(self, message, e: Exception = None, exc_info:bool = True):
        super().__init__(message, e, exc_info)
        # Add logic here
    ...

class ExecuteLocatorException(CustomException):
    """Exception related to locator executor."""
    ...
    def __init__(self, message, e: Exception = None, exc_info:bool = True):
        super().__init__(message, e, exc_info)
        # Add logic here
    ...
    
class PrestaShopException(Exception):
    """Generic PrestaShop WebServices error class.
    """

    def __init__(self, msg, error_code=None,
                 ps_error_msg='', ps_error_code=None):
        """Intiliaze webservice error."""
        self.msg = msg
        self.error_code = error_code
        self.ps_error_msg = ps_error_msg
        self.ps_error_code = ps_error_code

    def __str__(self):
        """Include custom msg."""
        return repr(self.ps_error_msg or self.msg)


class PrestaShopAuthenticationError(PrestaShopException):
    """Authentication Exception
        PrestaShopException (Unauthorized)
    """
    ...