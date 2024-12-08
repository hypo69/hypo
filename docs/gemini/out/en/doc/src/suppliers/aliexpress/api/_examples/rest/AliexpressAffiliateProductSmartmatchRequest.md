# AliexpressAffiliateProductSmartmatchRequest

## Overview

This module defines the `AliexpressAffiliateProductSmartmatchRequest` class, which is a subclass of `RestApi`. This class is used for interacting with the AliExpress Affiliate Product Smartmatch API. It allows for retrieving product information based on various criteria.

## Table of Contents

* [AliexpressAffiliateProductSmartmatchRequest](#aliexpressaffiliateproductスマートmatchrequest)
    * [Methods](#methods)
        * [getapiname](#getapiname)

## Classes

### `AliexpressAffiliateProductSmartmatchRequest`

**Description**: This class allows for interacting with the AliExpress Affiliate Product Smartmatch API.  It handles the request parameters and API interaction.

**Methods**:

#### `__init__`

**Description**: Initializes an instance of `AliexpressAffiliateProductSmartmatchRequest`.

**Parameters**:

- `domain` (str, optional): The API domain. Defaults to "api-sg.aliexpress.com".
- `port` (int, optional): The API port. Defaults to 80.

**Raises**:

- `Exception`: If any error occurs during initialization.



#### `getapiname`

**Description**: Returns the API name for the `aliexpress.affiliate.product.smartmatch` endpoint.

**Returns**:

- `str`: The API name, which is "aliexpress.affiliate.product.smartmatch".

**Raises**:

- `Exception`: If there's an issue determining the API name.


```python
def getapiname(self):
    """
    Returns the API name for the aliexpress.affiliate.product.smartmatch endpoint.

    Returns:
        str: The API name, which is "aliexpress.affiliate.product.smartmatch".

    Raises:
        Exception: If there's an issue determining the API name.
    """
    return 'aliexpress.affiliate.product.smartmatch'
```