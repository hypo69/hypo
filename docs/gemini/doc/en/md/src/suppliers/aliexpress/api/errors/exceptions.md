# hypotez/src/suppliers/aliexpress/api/errors/exceptions.py

## Overview

This module defines custom exceptions for handling errors encountered when interacting with the AliExpress API.  It provides a common base class `AliexpressException` and several specific exception types for different error scenarios.


## Classes

### `AliexpressException`

**Description**: Common base class for all AliExpress API exceptions.

**Methods**:

- `__init__(self, reason: str)`:
    **Description**: Initializes the exception with a reason string.
    **Parameters**:
        - `reason` (str): The reason for the exception.
    **Returns**:
        - None

- `__str__(self)`:
    **Description**: Returns a string representation of the exception.
    **Returns**:
        - str: The exception reason.


### `InvalidArgumentException`

**Description**: Raised when arguments passed to an AliExpress API method are invalid.

**Inheritance**: Inherits from `AliexpressException`.


### `ProductIdNotFoundException`

**Description**: Raised if the specified product ID cannot be found.

**Inheritance**: Inherits from `AliexpressException`.


### `ApiRequestException`

**Description**: Raised if there is a problem with the request to the AliExpress API, such as a network issue or server error.

**Inheritance**: Inherits from `AliexpressException`.


### `ApiRequestResponseException`

**Description**: Raised if the response received from the AliExpress API is not in the expected format or is invalid.

**Inheritance**: Inherits from `AliexpressException`.


### `ProductsNotFoudException`

**Description**: Raised if no products matching the search criteria are found.

**Inheritance**: Inherits from `AliexpressException`.


### `CategoriesNotFoudException`

**Description**: Raised if no categories matching the search criteria are found.

**Inheritance**: Inherits from `AliexpressException`.


### `InvalidTrackingIdException`

**Description**: Raised if the provided tracking ID is invalid or not present.

**Inheritance**: Inherits from `AliexpressException`.