# AliexpressAffiliateOrderGetRequest

## Overview

This module defines the `AliexpressAffiliateOrderGetRequest` class, which is a subclass of `RestApi`. This class is used to make requests to the AliExpress Affiliate Order Get API endpoint. It provides methods for initializing the API client and retrieving the API name.

## Table of Contents

* [AliexpressAffiliateOrderGetRequest](#aliexpressaffiliateordergetrequest)
    * [__init__](#__init__)
    * [getapiname](#getapiname)


## Classes

### `AliexpressAffiliateOrderGetRequest`

**Description**: This class handles requests to the AliExpress Affiliate Order Get API. It inherits from the `RestApi` class.

**Methods**:

#### `__init__`

**Description**: Initializes the `AliexpressAffiliateOrderGetRequest` object.

**Parameters**:

- `domain` (str, optional): The domain of the API endpoint. Defaults to `"api-sg.aliexpress.com"`.
- `port` (int, optional): The port of the API endpoint. Defaults to `80`.

**Raises**:

- No exceptions are explicitly documented in the code.


#### `getapiname`

**Description**: Returns the name of the API endpoint.

**Returns**:

- str: The name of the API endpoint (`"aliexpress.affiliate.order.get"`).

**Raises**:

- No exceptions are explicitly documented in the code.