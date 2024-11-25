# AliexpressAffiliateCategoryGetRequest

## Overview

This module defines the `AliexpressAffiliateCategoryGetRequest` class, which is a subclass of `RestApi`. It provides methods for interacting with the AliExpress affiliate category API.  It's designed for use within the `aliexpress` supplier's API.

## Table of Contents

* [Classes](#classes)
    * [AliexpressAffiliateCategoryGetRequest](#aliexpressaffiliatecategorygetrequest)

## Classes

### `AliexpressAffiliateCategoryGetRequest`

**Description**: This class handles requests to the AliExpress affiliate category API.  It inherits from `RestApi` for common API functionality.

**Methods**:

#### `__init__`

**Description**: Initializes an instance of `AliexpressAffiliateCategoryGetRequest`.

**Parameters**:

- `domain` (str, optional): The API domain. Defaults to "api-sg.aliexpress.com".
- `port` (int, optional): The API port. Defaults to 80.

**Raises**:

-  No exceptions are explicitly documented in the provided code.  Assume no exceptions are raised during initialization.


#### `getapiname`

**Description**: Returns the API name for the request.

**Parameters**:

-  No parameters are required.

**Returns**:

- `str`: The API name.  In this case, "aliexpress.affiliate.category.get".

**Raises**:

-  No exceptions are explicitly documented in the provided code. Assume no exceptions are raised during API name retrieval.