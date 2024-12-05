# hypotez/src/suppliers/aliexpress/api/errors/exceptions.py

## Overview

This module defines custom exceptions for the AliExpress API interactions. It provides a base class (`AliexpressException`) and several specialized exceptions to handle various error scenarios.


## Classes

### `AliexpressException`

**Description**: The base class for all AliExpress API exceptions. It stores a reason string for the exception.

**Methods**:

- `__init__(self, reason: str)`: Initializes the exception with the provided reason.
- `__str__(self) -> str`: Returns a string representation of the exception, containing the reason.

### `InvalidArgumentException`

**Description**: Raised when arguments provided to the AliExpress API are invalid.

**Inheritance**: Inherits from `AliexpressException`.


### `ProductIdNotFoundException`

**Description**: Raised when a specified product ID is not found in the AliExpress API response.

**Inheritance**: Inherits from `AliexpressException`.


### `ApiRequestException`

**Description**: Raised when a request to the AliExpress API fails, typically due to network issues or server errors.

**Inheritance**: Inherits from `AliexpressException`.


### `ApiRequestResponseException`

**Description**: Raised when the response received from the AliExpress API is not in a valid format.

**Inheritance**: Inherits from `AliexpressException`.


### `ProductsNotFoudException`

**Description**: Raised when no products are found in the AliExpress API response.


**Inheritance**: Inherits from `AliexpressException`.


### `CategoriesNotFoudException`

**Description**: Raised when no categories are found in the AliExpress API response.


**Inheritance**: Inherits from `AliexpressException`.


### `InvalidTrackingIdException`

**Description**: Raised when the provided tracking ID is invalid or missing.

**Inheritance**: Inherits from `AliexpressException`.