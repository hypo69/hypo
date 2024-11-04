## \file src/logger/exceptions.py
﻿# -*- coding: utf-8 -*-
# /path/to/interpreter/python
""" Program Exceptions """
from typing import Optional
from src.logger import logger
from selenium.common.exceptions import WebDriverException as WDriverException
from pykeepass.exceptions import (CredentialsError, BinaryError,
                                   HeaderChecksumError, PayloadChecksumError, 
                                   UnableToSendToRecycleBin)

class CustomException(Exception):
    """Base custom exception."""
    
    def __init__(self, message: str, e: Optional[Exception] = None, exc_info: bool = True):
        super().__init__(message)
        self.original_exception = e
        self.exc_info = exc_info
        self.handle_exception()

    def handle_exception(self):
        """Handles the exception based on its type and logs the necessary information."""
        logger.error(f"Exception occurred: {self}")
        if self.original_exception:
            logger.debug(f"Original exception: {self.original_exception}")
        # Здесь можно добавить логику для восстановления, повторных попыток и т.д.

class FileNotFoundError(CustomException, IOError):
    """Exception raised when a file is not found."""
    pass

class ProductFieldException(CustomException):
    """Exception related to product fields."""
    pass

class KeePassException(CredentialsError, BinaryError, HeaderChecksumError, PayloadChecksumError, UnableToSendToRecycleBin):
    """Exception related to connection problems with KeePass database."""
    pass

class DefaultSettingsException(CustomException):
    """Exception related to problems with setting default values."""
    pass

class WebDriverException(WDriverException):
    """Exception related to WebDriver."""
    pass

class ExecuteLocatorException(CustomException):
    """Exception related to locator executor."""
    pass

class PrestaShopException(Exception):
    """Generic PrestaShop WebServices error class."""
    
    def __init__(self, msg: str, error_code: Optional[int] = None, 
                 ps_error_msg: str = '', ps_error_code: Optional[int] = None):
        self.msg = msg
        self.error_code = error_code
        self.ps_error_msg = ps_error_msg
        self.ps_error_code = ps_error_code

    def __str__(self):
        """Include custom msg."""
        return repr(self.ps_error_msg or self.msg)

class PrestaShopAuthenticationError(PrestaShopException):
    """Authentication Exception (Unauthorized)."""
    pass
