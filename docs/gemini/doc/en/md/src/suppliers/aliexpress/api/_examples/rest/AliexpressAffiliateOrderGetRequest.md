# AliexpressAffiliateOrderGetRequest

## Overview

This module defines the `AliexpressAffiliateOrderGetRequest` class, which is a subclass of `RestApi`, providing functionality for retrieving affiliate order information from AliExpress.


## Table of Contents

* [AliexpressAffiliateOrderGetRequest](#aliexpressaffiliateordergetrequest)
    * [__init__](#__init__)
    * [getapiname](#getapiname)


## Classes

### `AliexpressAffiliateOrderGetRequest`

**Description**: This class extends `RestApi` to handle requests for affiliate order information from the AliExpress API.

**Methods**

#### `__init__`

**Description**: Initializes an `AliexpressAffiliateOrderGetRequest` object.

**Parameters**

* `domain` (str, optional): The domain of the API endpoint. Defaults to "api-sg.aliexpress.com".
* `port` (int, optional): The port number of the API endpoint. Defaults to 80.


**Raises**:
  * `Exception`:  Raised if there's an issue during initialization. (Details may be specific to the `RestApi` class)

#### `getapiname`

**Description**: Returns the name of the API method.

**Parameters**:
  None

**Returns**:
  str: The name of the API method, "aliexpress.affiliate.order.get".

**Raises**: None