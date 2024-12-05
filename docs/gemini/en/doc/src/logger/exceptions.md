# hypotez/src/logger/exceptions.py

## Overview

This module defines custom exceptions used in the application.  It handles errors related to various application components, including file operations, product fields, KeePass database connections, and PrestaShop WebService errors.  The module provides a base `CustomException` class for consistent exception handling and logging.


## Classes

### `CustomException`

**Description**: The base custom exception class.  It handles logging of the exception and provides a mechanism for dealing with the original exception if it exists.

**Attributes**:

- `original_exception` (Optional[Exception]): The original exception that caused this custom exception, if any.
- `exc_info` (bool): A flag to indicate if exception information should be logged.

**Methods**:

- `__init__(self, message: str, e: Optional[Exception] = None, exc_info: bool = True)`: Initializes the `CustomException` with a message and an optional original exception. Logs the exception and the original exception, if available.

### `FileNotFoundError`

**Description**: Raised when a file is not found.  Inherits from `IOError` and `CustomException`.

### `ProductFieldException`

**Description**: Raised for errors related to product fields. Inherits from `CustomException`.


### `KeePassException`

**Description**: Raised for errors related to KeePass database connections. This exception inherits from various `pykeepass` exceptions, handling errors like credentials issues, binary errors, and checksum errors during database interaction.


### `DefaultSettingsException`

**Description**: Raised when there are issues with default settings. Inherits from `CustomException`.


### `WebDriverException`

**Description**: Raised for errors related to WebDriver. Inherits from `selenium.common.exceptions.WebDriverException`.


### `ExecuteLocatorException`

**Description**: Raised for errors related to locator executors.  Inherits from `CustomException`.


### `PrestaShopException`

**Description**: A generic exception for PrestaShop WebService errors.  Handles errors when interacting with the PrestaShop WebService.

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



## Functions

(No functions defined in this module)