# AliexpressAffiliateFeaturedpromoGetRequest

## Overview

This module defines the `AliexpressAffiliateFeaturedpromoGetRequest` class, which is a subclass of the `RestApi` class. It provides functionality for interacting with the AliExpress affiliate featured promo API.

## Table of Contents

* [Classes](#classes)
    * [AliexpressAffiliateFeaturedpromoGetRequest](#aliexpressaffiliatefeaturedpromogetrequest)

## Classes

### `AliexpressAffiliateFeaturedpromoGetRequest`

**Description**: This class provides methods for interacting with the AliExpress affiliate featured promo API. It inherits from the `RestApi` class.

**Methods**

#### `__init__`

**Description**: Initializes an instance of the `AliexpressAffiliateFeaturedpromoGetRequest` class.

**Parameters**

- `domain` (str, optional): The domain for the API endpoint. Defaults to `"api-sg.aliexpress.com"`.
- `port` (int, optional): The port for the API endpoint. Defaults to `80`.

**Raises**

- None

#### `getapiname`

**Description**: Returns the API name for this request.

**Parameters**

- None

**Returns**

- str: The name of the API.  Returns `"aliexpress.affiliate.featuredpromo.get"`.

**Raises**

- None