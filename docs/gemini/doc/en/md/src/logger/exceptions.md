# hypotez/src/logger/exceptions.py

## Overview

This module defines custom exceptions used in the application for handling errors related to various components, including file operations, product fields, KeePass database connections, and PrestaShop WebService errors.  It provides a base class (`CustomException`) for handling logging and potentially original exception details.


## Classes

### `CustomException`

**Description**: The base custom exception class.  It handles logging of the exception and provides a mechanism for dealing with the original exception if it exists.

**Attributes**:

- `original_exception` (Optional[Exception]): The original exception that caused this custom exception, if any.
- `exc_info` (bool): A flag to indicate if exception information should be logged.


**Methods**:

- `__init__(self, message: str, e: Optional[Exception] = None, exc_info: bool = True)`: Initializes the `CustomException` with a message and an optional original exception.


### `FileNotFoundError`

**Description**: Raised when a file is not found.


### `ProductFieldException`

**Description**: Raised for errors related to product fields.


### `KeePassException`

**Description**: Raised for errors related to KeePass database connections.  It inherits from several `pykeepass` exceptions.


### `DefaultSettingsException`

**Description**: Raised when there are issues with default settings.


### `WebDriverException`

**Description**: Raised for errors related to WebDriver.


### `ExecuteLocatorException`

**Description**: Raised for errors related to locator executors.


### `PrestaShopException`

**Description**: Generic exception for PrestaShop WebService errors. Handles errors from the PrestaShop WebService.

**Attributes**:

- `msg` (str): A custom error message.
- `error_code` (Optional[int]): The error code returned by PrestaShop.
- `ps_error_msg` (str): The error message from PrestaShop.
- `ps_error_code` (Optional[int]): The PrestaShop error code.


**Methods**:

- `__init__(self, msg: str, error_code: Optional[int] = None, ps_error_msg: str = '', ps_error_code: Optional[int] = None)`: Initializes the `PrestaShopException` with the provided message and error details.
- `__str__(self)`: Returns the string representation of the exception.


### `PrestaShopAuthenticationError`

**Description**: Raised for PrestaShop authentication errors (Unauthorized). Inherits from `PrestaShopException`.