# AliexpressAffiliateHotproductQueryRequest

## Overview

This module defines the `AliexpressAffiliateHotproductQueryRequest` class, which is used to query hot products on AliExpress through its affiliate API. It inherits from the `RestApi` base class.

## Table of Contents

* [AliexpressAffiliateHotproductQueryRequest](#aliexpressaffiliatehotproductqueryrequest)
    * [Overview](#overview)
    * [Class `AliexpressAffiliateHotproductQueryRequest`](#class-aliexpressaffiliatehotproductqueryrequest)
        * [__init__](#init)
        * [getapiname](#getapiname)


## Class `AliexpressAffiliateHotproductQueryRequest`

**Description**: This class implements the request for querying hot products from the AliExpress affiliate API.

### `__init__`

**Description**: Initializes the `AliexpressAffiliateHotproductQueryRequest` object.

**Parameters**:

- `domain` (str, optional): The domain of the AliExpress API endpoint. Defaults to "api-sg.aliexpress.com".
- `port` (int, optional): The port of the AliExpress API endpoint. Defaults to 80.


**Raises**:

- No exceptions are explicitly raised in the `__init__` method.


### `getapiname`

**Description**: Returns the API name for the hot product query.

**Returns**:

- str: The API name "aliexpress.affiliate.hotproduct.query".

**Raises**:

- No exceptions are explicitly raised in the `getapiname` method.